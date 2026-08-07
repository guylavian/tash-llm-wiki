#!/usr/bin/env python3
"""jobs.py — the background job runner behind the ingest write surface. stdlib only, no network.

WHY THIS EXISTS: an upload has to TRIGGER the conversion chain (pdf → corpus → immutable reference
notes → crosslinked Markdown), and that chain is minutes of work, not milliseconds. Running it
inside the request handler would blow past `Handler.timeout = 30` and hold a worker thread for the
duration — the client would see a dead connection while the ingest was still running and writing to
the vault. So the PUT stores the file, hands the chain to this runner, and returns a job id the
caller polls at `GET /jobs/<id>`.

DESIGN — the three properties that matter:

  1. ONE WORKER, SERIALIZED. A single daemon thread drains the queue. `wikikb build` regenerates
     the indexes, the crosslink graph and the tkg store from the whole vault; two of them running
     concurrently would interleave writes to the same generated files. Serializing is not a
     performance compromise here, it is the correctness requirement.
  2. NOTHING STARTS AT IMPORT. The thread spawns on the first `submit()`, mirroring serve.py's "no
     socket opens at import time" rule — importing this module from a probe or from `mcp.py` must
     not fork a worker.
  3. BOUNDED EVERYTHING. Queue depth, retained job records, and captured log lines all have caps.
     A job record is held in memory and reachable over HTTP; unbounded output from a chatty
     subprocess would otherwise be a slow memory leak with a network-facing read path.

Job state is deliberately IN-MEMORY and lost on restart. The durable record of what was ingested is
the vault itself plus `.manifest.json` — a job row is progress reporting, not provenance, and
persisting it would create a second source of truth about ingest history that could disagree with
the manifest.
"""
import os
import subprocess
import sys
import threading
import time
import uuid
from collections import OrderedDict

from wikikb import paths

# --- caps -------------------------------------------------------------------------------------
MAX_QUEUED = 32            # submissions refused past this (429) rather than queued unboundedly
MAX_RETAINED = 100         # finished job records kept for polling; oldest evicted first
MAX_LOG_LINES = 60         # per step, tail-kept — enough to see the failure, bounded against a
MAX_LOG_CHARS = 8000       # runaway subprocess; both caps apply, whichever bites first
# A full chain on a large vault is minutes. Generous ceiling, still finite: a wedged subprocess must
# not park the single worker forever, because that would silently stall every later job.
STEP_TIMEOUT = int(os.environ.get("WIKIKB_JOB_TIMEOUT") or 1800)

QUEUED, RUNNING, DONE, FAILED = "queued", "running", "done", "failed"


def _tail(text):
    """Last MAX_LOG_LINES lines, also capped at MAX_LOG_CHARS. The TAIL, not the head: when a step
    fails, the traceback and the error summary are at the end."""
    if not text:
        return []
    lines = text.replace("\r\n", "\n").rstrip("\n").split("\n")[-MAX_LOG_LINES:]
    out, total = [], 0
    for line in reversed(lines):
        total += len(line) + 1
        if total > MAX_LOG_CHARS:
            break
        out.append(line)
    return list(reversed(out))


def _child_env():
    """Env for a step subprocess.

    PYTHONPATH: the dispatcher is run from `_meta/` by contract, but a serve process may have been
    started from anywhere — putting META on the path makes the child's `import wikikb` work either
    way, exactly as the probes do it.
    PYTHONIOENCODING: without it a step that prints the ⚠ banner or an em-dash dies with a
    UnicodeEncodeError on a Windows console codepage — the step would "fail" for a reason that has
    nothing to do with the ingest. The Dockerfile sets this globally for the same reason.

    WIKIKB_VAULT_ROOT / WIKIKB_CORPORA_DIR are RE-EXPORTED ABSOLUTE, and this is load-bearing.
    `paths.py` resolves both with Path(...).resolve(), i.e. against the CURRENT WORKING DIRECTORY.
    Steps run with `cwd=_meta/` (below), while the serve process is typically started from the repo
    root — so a RELATIVE value like `WIKIKB_VAULT_ROOT=./vault-blank` means the parent and the child
    resolve two DIFFERENT vaults (`<repo>/vault-blank` vs `_meta/vault-blank`). Observed 2026-08-07:
    a scrape job's first step created and then harvested into `_meta/vault-blank`, found the empty
    watchlist there, reported "nothing to do", and the chain died at corpus_to_vault — while the
    server's own /scrape/sources went on listing the source from the real vault. Nothing looked
    wrong anywhere except the one bootstrap line naming the wrong directory.

    Pinning the PARENT's already-resolved paths removes the cwd dependency entirely: the child is
    told exactly which vault to use rather than being left to re-derive it. This is why `--src` was
    already passed absolute (see ingest_steps/scrape_steps) — the same rule, applied to the env
    instead of to one flag, so it covers every path a step resolves for itself.
    """
    meta = str(paths.META)
    env = dict(os.environ)
    env["PYTHONPATH"] = meta + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONIOENCODING"] = "utf-8"
    env["WIKIKB_VAULT_ROOT"] = str(paths.WIKI)
    env["WIKIKB_CORPORA_DIR"] = str(paths.CORPORA)
    return env


class Job:
    """One queued unit of work: an ordered list of (name, wikikb-argv) steps run to completion or
    to the first failure."""

    def __init__(self, kind, steps, domain=None, detail=None, coalesce_key=None):
        self.id = uuid.uuid4().hex[:12]
        self.kind = kind
        self.domain = domain
        self.steps = steps                     # [(name, [argv...]), ...]
        self.detail = detail or {}
        self.coalesce_key = coalesce_key
        self.state = QUEUED
        self.created = time.time()
        self.started = None
        self.finished = None
        self.results = []                      # [{step, exit, seconds, log:[...]}]
        self.error = None

    def to_dict(self):
        d = {
            "id": self.id,
            "kind": self.kind,
            "state": self.state,
            "created": self.created,
            "started": self.started,
            "finished": self.finished,
            "steps": [name for name, _ in self.steps],
            "results": self.results,
        }
        if self.domain:
            d["domain"] = self.domain
        if self.detail:
            d["detail"] = self.detail
        if self.error:
            d["error"] = self.error
        if self.state in (RUNNING, QUEUED):
            done_names = {r["step"] for r in self.results}
            pending = [name for name, _ in self.steps if name not in done_names]
            d["current_step"] = pending[0] if pending and self.state == RUNNING else None
        return d


class Runner:
    """Single-worker FIFO job runner. One instance per process (see the module-level `RUNNER`)."""

    def __init__(self, start_worker=True):
        """start_worker=False queues without ever draining — the seam mode_probe.py uses to assert
        the coalescing rule deterministically. Racing a live worker to observe a QUEUED job would
        make that test flaky, and the alternative (letting the probe run a REAL ingest chain to
        observe it) would mutate the vault."""
        self._lock = threading.Lock()
        self._cv = threading.Condition(self._lock)
        self._pending = []                     # FIFO of Job
        self._jobs = OrderedDict()             # id -> Job (insertion-ordered, for retention)
        self._worker = None
        self._autostart = start_worker

    # --- submission ---------------------------------------------------------------------------

    def submit(self, job):
        """Enqueue `job`, or return the already-queued job it coalesces with.

        COALESCING: an ingest step processes the WHOLE `_raw/pdfs/` directory for its domain, so a
        second still-queued ingest for that same domain would redo byte-identical work — and, worse,
        run a second full `build`. Dropping five rapid uploads onto one pending job is therefore not
        a shortcut, it is the correct semantics: the one job that eventually runs sees all five
        files. A job already RUNNING is never coalesced into — it may have listed the directory
        before the newest file landed — so a fresh job is queued behind it.

        Returns (job, coalesced: bool). Raises RuntimeError when the queue is full.
        """
        with self._lock:
            if job.coalesce_key is not None:
                for q in self._pending:
                    if q.coalesce_key == job.coalesce_key and q.state == QUEUED:
                        return q, True
            if len(self._pending) >= MAX_QUEUED:
                raise RuntimeError("job queue full (%d pending); retry once the backlog drains"
                                   % MAX_QUEUED)
            self._jobs[job.id] = job
            self._pending.append(job)
            self._evict_locked()
            self._ensure_worker_locked()
            self._cv.notify()
            return job, False

    def get(self, job_id):
        with self._lock:
            return self._jobs.get(job_id)

    def list(self, limit=50):
        with self._lock:
            return list(self._jobs.values())[-limit:][::-1]      # newest first

    def stats(self):
        with self._lock:
            return {"pending": len(self._pending), "retained": len(self._jobs),
                    "worker": bool(self._worker and self._worker.is_alive())}

    # --- internals ----------------------------------------------------------------------------

    def _evict_locked(self):
        """Drop the oldest FINISHED records past MAX_RETAINED. A queued/running job is never
        evicted — its id has been handed to a client that is entitled to poll it."""
        if len(self._jobs) <= MAX_RETAINED:
            return
        for jid, j in list(self._jobs.items()):
            if len(self._jobs) <= MAX_RETAINED:
                break
            if j.state in (DONE, FAILED):
                del self._jobs[jid]

    def _ensure_worker_locked(self):
        if not self._autostart:
            return
        if self._worker is None or not self._worker.is_alive():
            self._worker = threading.Thread(target=self._run_forever, name="wikikb-jobs",
                                            daemon=True)
            self._worker.start()

    def _run_forever(self):
        while True:
            with self._cv:
                while not self._pending:
                    self._cv.wait()
                job = self._pending.pop(0)
                job.state = RUNNING
                job.started = time.time()
            try:
                self._run_job(job)
            except Exception as e:                      # noqa: BLE001 — the worker must outlive any
                job.state = FAILED                       # single bad job; a dead worker would wedge
                job.error = "runner error: %s" % e       # the queue with no way to notice
            finally:
                if job.state == RUNNING:
                    job.state = DONE
                job.finished = time.time()

    def _run_job(self, job):
        for name, argv in job.steps:
            t0 = time.time()
            cmd = [sys.executable, "-m", "wikikb"] + argv
            try:
                p = subprocess.run(cmd, cwd=str(paths.META), env=_child_env(),
                                   capture_output=True, text=True, errors="replace",
                                   timeout=STEP_TIMEOUT)
                rc, out = p.returncode, (p.stdout or "") + (p.stderr or "")
            except subprocess.TimeoutExpired:
                rc, out = -1, "step exceeded WIKIKB_JOB_TIMEOUT (%ds)" % STEP_TIMEOUT
            job.results.append({"step": name, "exit": rc, "seconds": round(time.time() - t0, 1),
                                "log": _tail(out)})
            if rc != 0:
                job.state = FAILED
                # The chain STOPS at the first failure — same contract as `wikikb build`. Continuing
                # past a failed pdf_to_corpus would run corpus_to_vault against a stale index and
                # write reference notes that do not correspond to the uploaded file.
                job.error = "step %r failed (exit %d)" % (name, rc)
                return
        job.state = DONE


RUNNER = Runner()


# --- the ingest chain --------------------------------------------------------------------------

def ingest_steps(domain):
    """The three commands CLAUDE.md's INGEST operation prescribes for a PDF drop, as job steps.

    pdf_to_corpus  — extracts each PDF's text into corpora/<domain>/ (the .md bodies + index.jsonl)
    corpus_to_vault— folds those into vault/reference/<domain>/*.md, the immutable reference notes
    build          — tags → CROSSLINK → index → tkg → lint → verify. Crosslink is the step that
                     "links to other md files": it resolves each page's kb: tokens to the matching
                     reference note and writes the generated `## Sources` wikilinks, which is what
                     puts the new document into the graph rather than leaving it a loose file.

    TWO FLAGS THAT ARE NOT OPTIONAL:

      --append   WITHOUT IT, pdf_to_corpus TRUNCATES corpora/<domain>/index.jsonl and rewrites it
                 from just the PDFs in --src. On a corpus-backed domain (keycloak has 800 harvested
                 reference notes) the next corpus_to_vault --apply would then regenerate
                 reference/keycloak/ from that truncated index. One uploaded PDF would silently
                 destroy the entire ground-truth tier. --append merges instead, with the new harvest
                 winning on a url collision.
      --apply    both tools are dry-run by default.

    --src is passed ABSOLUTE. The steps run with cwd=_meta/, and --src is an ordinary filesystem
    path resolved against cwd (not against the vault root), so a relative path would silently
    resolve to _meta/_sources/... — a directory that does not exist, or worse, one that does.
    """
    src = str(paths.WIKI / "_sources" / domain / "_raw" / "pdfs")
    return [
        ("pdf_to_corpus", ["pdf_to_corpus", "--src", src, "--domain", domain, "--append", "--apply"]),
        ("corpus_to_vault", ["corpus_to_vault", "--domain", domain, "--apply"]),
        ("build", ["build"]),
    ]


def submit_ingest(domain, detail=None):
    """Queue the ingest chain for `domain`. Returns (job, coalesced)."""
    return RUNNER.submit(Job("ingest", ingest_steps(domain), domain=domain, detail=detail,
                             coalesce_key=("ingest", domain)))


# --- the scrape chain (ONLINE MODE) --------------------------------------------------------------

# How many not-yet-harvested crawls ONE queued run may walk. The full Common Crawl history is 126
# crawls and growing; walking all of them for a prefix source is hours, which would blow STEP_TIMEOUT
# and get the step killed — and a killed step fails the chain, so nothing would be folded into the
# vault even though the harvest itself had made progress. Bounding the run instead means every run
# finishes, folds in what it got, and the LEDGER makes the next one continue where it stopped. The
# CLI is deliberately unbounded by default: an operator watching a terminal can afford to wait.
MAX_INDEXES_PER_RUN = int(os.environ.get("WIKIKB_SCRAPE_MAX_INDEXES_PER_RUN") or 12)


def scrape_steps(domain, urls=None, match="exact", direct=False, max_indexes=None):
    """The web-harvest chain: the SAME shape as `ingest_steps`, with the web pair swapped in for the
    PDF pair. `scrape` fetches into `_sources/<domain>/_raw/web/`, `web_to_corpus` turns that into
    corpus records, and the last two steps are literally the same tools the PDF path ends with.

    urls=None harvests every ENABLED watchlist source for the domain; a list harvests exactly those
    URLs, which is how "scrape this one site, it need not be on the list" is served.

    --append CARRIES THE SAME WARNING IT DOES FOR PDFs: without it `web_to_corpus` truncates
    `corpora/<domain>/index.jsonl` and the next `corpus_to_vault --apply` would regenerate the
    reference tier from the truncation. One scraped page would destroy an 800-note ground truth.

    A per-URL run passes `--direct` through when the caller asked for it; a watchlist run does not,
    because there the flag is a PER-SOURCE property read from the file (`"direct": true`), not a
    property of the run.
    """
    argv = ["scrape", "--domain", domain]
    if urls:
        for u in urls:
            argv += ["--url", u]
        argv += ["--match", match]
        if direct:
            argv.append("--direct")
    else:
        # A watchlist run walks the crawl history, bounded per run (see MAX_INDEXES_PER_RUN).
        argv += ["--all", "--max-indexes", str(max_indexes or MAX_INDEXES_PER_RUN)]
    src = str(paths.WIKI / "_sources" / domain / "_raw" / "web")
    return [
        ("scrape", argv),
        ("web_to_corpus", ["web_to_corpus", "--domain", domain, "--src", src, "--append", "--apply"]),
        ("corpus_to_vault", ["corpus_to_vault", "--domain", domain, "--apply"]),
        ("build", ["build"]),
    ]


def submit_scrape(domain, urls=None, match="exact", direct=False, detail=None, max_indexes=None):
    """Queue the scrape chain for `domain`. Returns (job, coalesced).

    Only a WATCHLIST run (urls=None) coalesces, and for the same reason the ingest chain does: it
    reads the whole list, so a second queued run would redo byte-identical work. An explicit
    per-URL run never coalesces — folding "scrape example.com/a" into a pending "scrape everything"
    job would look like it succeeded while quietly harvesting a different set of URLs.
    """
    return RUNNER.submit(Job("scrape", scrape_steps(domain, urls, match, direct, max_indexes),
                             domain=domain, detail=detail,
                             coalesce_key=("scrape", domain) if not urls else None))
