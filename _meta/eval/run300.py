#!/usr/bin/env python3
"""run300.py — run the cases300.jsonl eval through `opencode run` in parallel, then grade.

Usage:
    python3 run300.py [--model opencode/deepseek-v4-flash-free] [--workers 4]
                      [--limit N] [--timeout 300] [--answers answers300.jsonl]
                      [--new-run] [--overwrite]

Cohort identity (consensus 2026-07-12 — resume must never mix experiments):
    Every run writes a sidecar manifest `<answers>.manifest.json` (run_id, model, cases
    sha256+count, git commit + dirty flag, started_utc, workers, timeout, isolation) and stamps
    every answer row with {run_id, model}. Resuming an existing answers file requires the
    manifest to exist and match on model + cases hash; any mismatch exits 2. `--new-run` starts
    a FRESH timestamped answers path (never touches the existing one); `--overwrite` explicitly
    truncates the existing path + manifest. grade300.py rejects mixed-run_id cohorts.

Resumable: already-answered ids are skipped, answers append as they finish.
cache-repeat cases run in a second phase (their originals must answer first).
Grade afterwards with:
    python3 grade300.py --cases cases300.jsonl --answers <answers.jsonl> --json report300.json
"""
import argparse, datetime, hashlib, json, os, pathlib, re, shutil, subprocess, sys, tarfile, tempfile, threading, time, uuid
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait

HERE = pathlib.Path(__file__).resolve().parent
WIKI = HERE.parent.parent
LOCK = threading.Lock()
MANIFEST_SCHEMA = "run300/2"
ISOLATION = "manifest-commit-full-copy"
WORKSPACE_ROOT = pathlib.Path(tempfile.gettempdir()) / "wikikb-eval-workspaces"
COHORT_ROOT = WORKSPACE_ROOT / "cohorts"
# One spec, two views: this skeleton and grade300.contract() must stay in lockstep —
# the grader requires these literal heading lines, not just "labeled groups".
OUTPUT_CONTRACT = ("\n\nMandatory output contract — end your answer with exactly this Markdown "
                   "skeleton (heading lines verbatim):\n"
                   "## References\n"
                   "### RH ground-truth\n"
                   "- the kb:<id>, guide:<slug>, or ref:<file> sources actually used — at least one "
                   "verified kb:, guide:, or ref: source; or exactly the line: no verified source was used\n"
                   "### Wiki\n"
                   "- the [[slug]] wiki pages used; or exactly the line: no wiki page was used\n"
                   "Never invent a source.")


def _git(*args):
    try:
        p = subprocess.run(["git", *args], capture_output=True, text=True, cwd=str(WIKI), timeout=10)
        return p.stdout.strip() if p.returncode == 0 else None
    except Exception:
        return None


def input_fingerprint():
    """Fast live-input identity: paths + mtimes + sizes, excluding evaluator outputs/caches."""
    h = hashlib.sha256()
    for root, dirs, files in os.walk(WIKI):
        relroot = pathlib.Path(root).relative_to(WIKI)
        dirs[:] = sorted(d for d in dirs if d not in {".git", ".obsidian", "__pycache__"}
                        and not (relroot == pathlib.Path("_meta") and d == "eval"))
        for name in sorted(files):
            p = pathlib.Path(root) / name
            rel = p.relative_to(WIKI)
            st = p.stat()
            h.update((str(rel) + "\0" + str(st.st_mtime_ns) + "\0" + str(st.st_size) + "\n").encode())
    return h.hexdigest()


def build_manifest(args, cases_path):
    blob = pathlib.Path(cases_path).read_bytes()
    commit = _git("rev-parse", "HEAD")
    status = _git("status", "--porcelain")
    return {
        "schema": MANIFEST_SCHEMA,
        "run_id": (datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                   + "-" + uuid.uuid4().hex[:8]),
        "model": args.model,
        "cases_sha256": hashlib.sha256(blob).hexdigest(),
        "cases_count": sum(1 for l in blob.splitlines() if l.strip()),
        "git_commit": commit,
        "git_status_ok": status is not None,
        "git_dirty": bool(status),
        "allow_dirty": bool(args.allow_dirty),
        # record-only provenance, NOT a resume invariant: live-vault changes cannot
        # affect the archived commit snapshot cases actually run against
        "input_fingerprint": input_fingerprint(),
        # live wikikb code/package; case-snapshot vault DATA via WIKIKB_VAULT_ROOT
        # injected into the examinee env (opencode ignores per-project MCP config —
        # falsified 2026-07-12; verified live by tests/opencode_merge_probe.py +
        # deterministically by tests/mcp_isolation_probe.py)
        "mcp_vault_source": "case-snapshot",
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "workers": args.workers,
        "timeout": args.timeout,
        "max_consecutive_timeouts": args.max_consecutive_timeouts,
        "isolation": ISOLATION,
        "expand": not args.no_expand,
        "prompt_sha256": hashlib.sha256(OUTPUT_CONTRACT.encode()).hexdigest(),
    }


def manifest_path(answers_path):
    return pathlib.Path(str(answers_path) + ".manifest.json")


def _refuse(msg):
    print("refusing resume: " + msg, file=sys.stderr)
    sys.exit(2)


def _load_manifest(mp):
    """Parse + shape-check a cohort manifest; any defect is a refusal (exit 2), never a crash."""
    try:
        man = json.loads(mp.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        _refuse("unreadable manifest %s (%s). Use --new-run or --overwrite." % (mp, e))
    if not isinstance(man, dict) or man.get("schema") != MANIFEST_SCHEMA:
        _refuse("manifest %s has wrong/missing schema (want %r). Use --new-run or --overwrite."
                % (mp, MANIFEST_SCHEMA))
    for key in ("run_id", "model", "cases_sha256"):
        if not isinstance(man.get(key), str) or not man[key].strip():
            _refuse("manifest %s missing/invalid %r. Use --new-run or --overwrite." % (mp, key))
    return man


def _check_existing_rows(out, man):
    """Every existing row must belong to THIS cohort before we append to it — a stamped stranger
    row would corrupt the cohort silently until grading. Refusal (exit 2) happens BEFORE any
    worker launches, not after an expensive run."""
    try:
        lines = out.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        _refuse("unreadable answers file %s (%s)" % (out, e))
    for ln, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            _refuse("%s line %d is not valid JSON" % (out, ln))
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            _refuse("%s line %d is not an answer row" % (out, ln))
        if row.get("run_id") != man["run_id"] or row.get("model") != man["model"]:
            _refuse("%s line %d is stamped run_id=%r/model=%r but the manifest says %r/%r — "
                    "mixed cohort. Use --new-run." % (out, ln, row.get("run_id"),
                    row.get("model"), man["run_id"], man["model"]))


def _establish(out, fresh):
    """Atomically stand up a new cohort: manifest + an (empty) answers file, so zero-work runs
    (--limit 0, empty banks) still leave a complete, gradeable cohort on disk."""
    manifest_path(out).write_text(json.dumps(fresh, indent=1), encoding="utf-8")
    out.touch()
    return out, fresh


def resolve_cohort(args, cases_path):
    """Decide (answers_path, manifest) honoring resume/--new-run/--overwrite. Exits 2 on any
    identity mismatch — a cohort manifest is useless if resume can silently mix experiments."""
    out = pathlib.Path(args.answers)
    if args.new_run:                            # fresh timestamped path; never touches the old one
        fresh = build_manifest(args, cases_path)
        out = out.with_name(out.stem + "-" + fresh["run_id"] + out.suffix)
        if out.exists():
            print("--new-run target %s already exists (improbable collision) — rerun" % out,
                  file=sys.stderr)
            sys.exit(2)
        return _establish(out, fresh)
    mp = manifest_path(out)
    if out.exists() and not args.overwrite:
        if not mp.exists():
            _refuse("%s exists but has no manifest (legacy/unknown cohort). Use --new-run for a "
                    "fresh cohort or --overwrite to replace it." % out)
        man = _load_manifest(mp)
        fresh = build_manifest(args, cases_path)
        for key in ("model", "cases_sha256", "isolation", "expand", "prompt_sha256",
                    "workers", "timeout", "max_consecutive_timeouts"):
            if man.get(key) != fresh[key]:
                _refuse("manifest %s mismatch (manifest=%r, now=%r). Use --new-run or --overwrite."
                        % (key, man.get(key), fresh[key]))
        _check_existing_rows(out, man)
        return out, man                          # same cohort — resume under the ORIGINAL run_id
    fresh = build_manifest(args, cases_path)     # new file, or explicit --overwrite
    if args.overwrite:
        out.write_text("", encoding="utf-8")
    return _establish(out, fresh)


def _reference_state(root):
    """relpath -> (inode, mtime_ns, size) for the hardlinked immutable reference tier."""
    ref = pathlib.Path(root) / "reference"
    out = {}
    if not ref.is_dir():
        return out
    for path in sorted(p for p in ref.rglob("*") if p.is_file()):
        st = path.stat()
        out[str(path.relative_to(ref))] = (st.st_ino, st.st_mtime_ns, st.st_size)
    return out


def _frontmatter_block(text):
    """The opening `--- … ---` block only — a body line must never match (veto fix)."""
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def _strip_eval_born_pages(root):
    """Drop pages tagged `origin: eval-cohort` from a cohort snapshot: prior cohorts'
    filed answers are eval exhaust, not vault knowledge — a future examinee must not
    cache-hit them. Returns the removed relpaths (recorded in the manifest)."""
    removed = []
    for d in ("questions", "topics", "entities"):
        base = root / d
        if not base.is_dir():
            continue
        for p in sorted(base.glob("*.md")):
            fm = _frontmatter_block(p.read_text(encoding="utf-8", errors="replace"))
            if re.search(r"^origin:\s*eval-cohort\s*$", fm, re.M):
                p.unlink()
                removed.append(str(p.relative_to(root)))
    return removed


def materialize_cohort_snapshot(manifest):
    """Materialize the exact recorded commit once; never source cases from the live vault."""
    commit = manifest.get("git_commit")
    if not commit:
        _refuse("manifest has no valid git commit")
    base = COHORT_ROOT / manifest["run_id"]
    if base.is_dir():
        marker = base / ".wikikb-commit"
        if not marker.is_file() or marker.read_text(encoding="utf-8").strip() != commit:
            _refuse("cached cohort snapshot has wrong/missing commit marker")
        # veto correction (blocker 2): the stripped list must survive resume — recover
        # it from the snapshot's durable record and verify against the manifest.
        stripped_file = base / ".wikikb-stripped.json"
        if not stripped_file.is_file():
            _refuse("cached cohort snapshot missing .wikikb-stripped.json (case-snapshot cohort)")
        try:
            cached = json.loads(stripped_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            _refuse("unreadable .wikikb-stripped.json in cached snapshot (%s)" % e)
        recorded = manifest.get("eval_born_pages_stripped")
        if not isinstance(recorded, list):
            _refuse("manifest missing/invalid eval_born_pages_stripped — cannot verify "
                    "cached snapshot; use --new-run")
        if recorded != cached:
            _refuse("eval_born_pages_stripped mismatch: manifest %r vs snapshot %r"
                    % (recorded, cached))
        return base
    COHORT_ROOT.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=manifest["run_id"] + "-", dir=str(COHORT_ROOT)))
    try:
        p = subprocess.Popen(["git", "archive", "--format=tar", commit], cwd=str(WIKI),
                             stdout=subprocess.PIPE)
        with tarfile.open(fileobj=p.stdout, mode="r|") as tf:
            tf.extractall(tmp, filter="data")
        if p.wait() != 0:
            raise RuntimeError("git archive failed")
        manifest["eval_born_pages_stripped"] = _strip_eval_born_pages(tmp)
        (tmp / ".wikikb-stripped.json").write_text(
            json.dumps(manifest["eval_born_pages_stripped"]), encoding="utf-8")
        (tmp / ".wikikb-commit").write_text(commit + "\n", encoding="utf-8")
        for path in sorted(tmp.rglob("*"), reverse=True):
            path.chmod(0o555 if path.is_dir() else 0o444)
        tmp.chmod(0o555)
        tmp.rename(base)
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    return base


def build_case_snapshot(case_id, source_root):
    """Build one fully copied case workspace from the immutable cohort snapshot."""
    WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in str(case_id))[:80] or "case"
    snap = pathlib.Path(tempfile.mkdtemp(prefix=safe + "-", dir=str(WORKSPACE_ROOT)))
    shutil.rmtree(snap)                            # copytree requires a non-existent destination
    try:
        shutil.copytree(source_root, snap, copy_function=shutil.copy2,
                        ignore=shutil.ignore_patterns("__pycache__"))
        for path in sorted(snap.rglob("*"), reverse=True):
            if path.is_dir():
                path.chmod(0o755)
            else:
                path.chmod(0o755 if path.stat().st_mode & 0o111 else 0o644)
        snap.chmod(0o755)
        return snap
    except Exception:
        shutil.rmtree(snap, ignore_errors=True)
        raise


def reference_integrity_error(before):
    after = _reference_state(WIKI)
    if after == before:
        return None
    changed = sorted(set(before) ^ set(after))
    changed.extend(k for k in set(before) & set(after) if before[k] != after[k])
    return ("reference/ changed in the LIVE vault during this case (frozen-vault violation; "
            "first 5): %s" % ", ".join(sorted(set(changed))[:5]))


def ask(case, model, timeout, keep_workspace=False, no_expand=False, source_root=None):
    """Run one case in its own redacted snapshot; never share filed pages across cases."""
    snap = None
    try:
        snap = build_case_snapshot(case["id"], source_root)
        reference_before = _reference_state(WIKI)
        err = "no output"
        for attempt in (1, 2):
            try:
                env = os.environ.copy()
                # opencode resolves its project dir from $PWD, not the process cwd
                # (verified via its session DB) — without this, examinee file ops
                # and AGENTS.md loading target the LIVE vault, not the snapshot.
                env["PWD"] = str(snap)
                # deterministic snapshot-local package resolution for any direct
                # `python3 -m wikikb` the examinee runs (veto correction, blocker 1)
                env["PYTHONPATH"] = str(snap / "_meta")
                # THE effective MCP isolation: opencode ignores per-project MCP config
                # (verified 2026-07-12, tee probe), so the global-config wikikb server —
                # spawned fresh per `opencode run` — inherits this and scopes every
                # vault read to the case snapshot via paths.py.
                env["WIKIKB_VAULT_ROOT"] = str(snap)
                if no_expand:
                    env["WIKIKB_NO_EXPAND"] = "1"
                r = subprocess.run(
                    ["opencode", "run", "-m", model, case["question"] + OUTPUT_CONTRACT],
                    capture_output=True, text=True, timeout=timeout, cwd=str(snap), env=env)
                out = r.stdout.strip()
                if out:
                    break
                err = (r.stderr or "").strip()[-300:]
            except subprocess.TimeoutExpired:
                err = f"timeout {timeout}s"
            time.sleep(5 * attempt)  # ponytail: fixed backoff; free-tier rate limits are the ceiling
        else:
            out = ""
        integrity = reference_integrity_error(reference_before)
        if integrity:
            return "[RUN-ERROR] " + integrity
        return out if out else f"[RUN-ERROR] {err}"
    except Exception as e:
        return "[RUN-ERROR] workspace: %s" % e
    finally:
        if snap is not None:
            if keep_workspace:
                print("kept case workspace: %s" % snap, file=sys.stderr, flush=True)
            else:
                shutil.rmtree(snap, ignore_errors=True)


def run_bounded(cases, workers, ask_fn, on_result, max_consecutive_timeouts=3):
    """Run a bounded frontier; drain results after the timeout circuit opens, never refill it."""
    todo = iter(cases)
    bank_order = {c["id"]: i for i, c in enumerate(cases)}
    consecutive_timeouts = 0
    circuit_open = False
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {}
        for _ in range(min(workers, len(cases))):
            c = next(todo, None)
            if c is not None:
                futs[ex.submit(ask_fn, c)] = c
        while futs:
            finished, _ = wait(futs, return_when=FIRST_COMPLETED)
            for fut in sorted(finished, key=lambda f: bank_order[futs[f]["id"]]):
                c = futs.pop(fut)
                ans = fut.result()
                on_result(c, ans)
                consecutive_timeouts = (consecutive_timeouts + 1
                                        if ans.startswith("[RUN-ERROR] timeout") else 0)
                if (max_consecutive_timeouts and
                        consecutive_timeouts >= max_consecutive_timeouts):
                    circuit_open = True
            if not circuit_open:
                while len(futs) < workers:
                    c = next(todo, None)
                    if c is None:
                        break
                    futs[ex.submit(ask_fn, c)] = c
    return circuit_open


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="opencode/deepseek-v4-flash-free")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, help="run only the first N pending cases (smoke run)")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--max-consecutive-timeouts", type=int, default=3,
                    help="stop scheduling after this many consecutive double-timeout cases (0 disables)")
    ap.add_argument("--cases", default=str(HERE / "cases300.jsonl"))
    ap.add_argument("--answers", default=str(HERE / "answers300.jsonl"))
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--new-run", action="store_true", dest="new_run",
                     help="start a FRESH cohort on a timestamped answers path (never touches the old one)")
    grp.add_argument("--overwrite", action="store_true",
                     help="explicitly truncate the existing answers file + manifest and start over")
    ap.add_argument("--keep-workspace", action="store_true",
                    help="keep each per-case redacted workspace for inspection (default: delete)")
    ap.add_argument("--no-expand", action="store_true",
                    help="disable graph expansion for the ablation cohort")
    ap.add_argument("--allow-dirty", action="store_true",
                    help="permit a dirty initial vault for development only (recorded; not publishable)")
    args = ap.parse_args()
    if args.workers < 1:
        ap.error("--workers must be at least 1")

    cases = [json.loads(l) for l in open(args.cases, encoding="utf-8") if l.strip()]
    out, manifest = resolve_cohort(args, args.cases)
    if not manifest.get("git_commit") or not manifest.get("git_status_ok"):
        _refuse("git identity/status failed; publication cohorts require a valid clean commit")
    if manifest.get("git_dirty") and not manifest.get("allow_dirty"):
        _refuse("vault was dirty at cohort creation; clean it or use --allow-dirty for a non-publishable run")
    source_root = materialize_cohort_snapshot(manifest)
    # persist the finalized manifest (incl. eval_born_pages_stripped) ATOMICALLY —
    # a truncated manifest right before an expensive cohort would poison resume
    mp = manifest_path(out)
    tmp_mp = mp.with_suffix(".tmp")
    tmp_mp.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    os.replace(tmp_mp, mp)
    lock = WIKI / ".eval-lock"
    if lock.exists():
        try:
            holder = json.loads(lock.read_text(encoding="utf-8"))
            os.kill(int(holder.get("pid", 0)), 0)
            _refuse("another live cohort holds %s (run %s, pid %s) — one run at a time"
                    % (lock, holder.get("run_id"), holder.get("pid")))
        except (OSError, ValueError):
            pass                                   # stale lock — take it over
    lock.write_text(json.dumps({"run_id": manifest["run_id"], "pid": os.getpid()}),
                    encoding="utf-8")
    print(f"cohort {manifest['run_id']} (model {manifest['model']}) -> {out}")
    done = set()
    if out.exists():
        done = {json.loads(l)["id"] for l in open(out, encoding="utf-8") if l.strip()}

    circuit_open = False

    def run_phase(phase_cases, label):
        nonlocal circuit_open
        if circuit_open:
            return
        pending = [c for c in phase_cases if c["id"] not in done]
        if args.limit is not None:
            remaining = args.limit - len(done)
            pending = pending[:max(0, remaining)]
        if not pending:
            return
        print(f"{label}: {len(pending)} to run ({args.workers} workers, model {args.model})")
        t0 = time.time()
        n = 0
        def _ask_case(c):
            return ask(c, args.model, args.timeout, args.keep_workspace, args.no_expand, source_root)
        def _record(c, ans):
            nonlocal n
            n += 1
            with LOCK:
                with open(out, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"id": c["id"], "answer": ans,
                                         "run_id": manifest["run_id"],
                                         "model": manifest["model"]}, ensure_ascii=False) + "\n")
                done.add(c["id"])
            flag = " ERR" if ans.startswith("[RUN-ERROR]") else ""
            print(f"  [{n}/{len(pending)}] {c['id']}{flag}  ({time.time()-t0:.0f}s elapsed)", flush=True)
        opened = run_bounded(pending, args.workers, _ask_case, _record,
                             args.max_consecutive_timeouts)
        if opened:
            print("  CIRCUIT-BREAKER — consecutive timeout threshold reached; running work drained. "
                  "Cohort remains incomplete and exits 2.", flush=True)
            circuit_open = True

    firsts = [c for c in cases if c["type"] != "cache-repeat"]
    repeats = [c for c in cases if c["type"] == "cache-repeat"]
    try:
        run_phase(firsts, "phase 1 (originals)")
        run_phase(repeats, "phase 2 (cache-repeats)")
    finally:
        try:                                       # release the 15:09-rule vault lock
            if json.loads(lock.read_text(encoding="utf-8")).get("run_id") == manifest["run_id"]:
                lock.unlink()
        except (OSError, ValueError):
            pass

    errs = sum(1 for l in open(out, encoding="utf-8")
               if l.strip() and json.loads(l)["answer"].startswith("[RUN-ERROR]"))
    print(f"done: {len(done)}/{len(cases)} answered, {errs} run-errors -> {out}")
    print(f"grade: python3 {HERE/'grade300.py'} --cases {args.cases} --answers {out} --json {HERE/'report300.json'}")
    if circuit_open:
        sys.exit(2)


if __name__ == "__main__":
    main()
