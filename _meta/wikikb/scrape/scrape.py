#!/usr/bin/env python3
"""scrape.py — harvest web sources into the raw tier. ONLINE MODE ONLY (`WIKIKB_MODE=online`).

    python3 -m wikikb scrape --domain keycloak --all             # everything on the watchlist
    python3 -m wikikb scrape --domain keycloak --url https://…   # one URL, watchlist or not
    python3 -m wikikb scrape --domain keycloak --url … --dry-run # look it up, write nothing
    python3 -m wikikb scrape --all --archive wayback             # one web index only, this run

    # watchlist CRUD — the same operations as GET/POST/PATCH/DELETE /scrape/sources, available on a
    # box where nothing is serving. These edit a JSON file and open no socket, so unlike a harvest
    # they work in AIRGAPPED mode too:
    python3 -m wikikb scrape --list                              # what is configured
    python3 -m wikikb scrape --add https://… --domain keycloak --label "…" --match prefix
    python3 -m wikikb scrape --update https://… --disable        # partial: only what you pass
    python3 -m wikikb scrape --remove https://…                  # harvested notes are KEPT

WHAT IT DOES, AND WHERE IT STOPS. A harvest asks EVERY enabled web index (`archives.py`:
Common Crawl, the Internet Archive, arquivo.pt, vefsafn.is) whether the URL is captured, pulls the
captures, extracts Markdown, and writes ONE file plus ONE sidecar per URL into
`vault/_sources/<domain>/_raw/web/`. It does not write a corpus record, a reference note, or a
synthesis page — those are the next three commands (`web_to_corpus` -> `corpus_to_vault` ->
`build`), which is exactly the chain the PDF upload path already runs. Keeping the fetch separate
from the fold-in is what lets a failed extraction be retried without regenerating the vault, and
what lets several harvests share one `build`.

SEVERAL ARCHIVES, ONE NOTE PER URL. Two archives holding the same page do NOT produce two notes:
the note is named from the URL, and `_write_note`'s never-overwrite-a-newer-capture rule decides
which archive's capture the note holds — the newest, regardless of which archive was walked last.
That is what makes taking the union of four indexes safe rather than a source of duplicates.

THREE RULES THIS MODULE ENFORCES, EACH BECAUSE THE ALTERNATIVE IS SILENTLY WRONG:

  1. THE RAW TIER IS APPEND/REPLACE-ONLY, PER SOURCE. A harvest writes `<slug>.md` for its own URL
     and nothing else. It never edits another source's file, never touches
     `vault/reference/<domain>/`, and never writes a page under `topics/`|`entities/`|`questions/`.
  2. UNCHANGED CAPTURES ARE SKIPPED, NOT REWRITTEN. The sidecar stores the extracted body's digest;
     a re-run that computes the same digest leaves the file alone. Rewriting it would bump mtimes
     across the raw tier every night and make "what actually changed" unanswerable.
  3. THE ARCHIVES FIRST; A LIVE FETCH IS OPT-IN. `"direct": true` on a source (or `--direct`) lets
     a URL that NO archive captured be fetched from the origin. It is off by default because the
     point of harvesting from an archive is not to hit other people's servers on a cron, and
     because a direct fetch is the only path here that can be aimed at an arbitrary host — which is
     why it also carries the address guard in `_guard_direct()`. Adding archives makes this hatch
     needed less often, not more: a page missing from Common Crawl is frequently in the Wayback
     Machine, and a capture costs the origin nothing.

PROVENANCE. Each harvested note is cited as `web:<url> (<label>, fetched YYYY-MM-DD)` where the
date is the CAPTURE date, not today's — the document is what the crawler saw then. Per CLAUDE.md's
source tiers, a page synthesizing from it must mark the material as upstream/community, never as a
vendor support statement.
"""
import argparse
import hashlib
import ipaddress
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import urlsplit

from wikikb import modes
from wikikb import paths
from wikikb.scrape import archives as archmod
from wikikb.scrape import commoncrawl as cc
from wikikb.scrape import extract as extractor
from wikikb.scrape import sources as srcmod
from wikikb.scrape import state as statemod

sys.dont_write_bytecode = True

MIN_CHARS = int(os.environ.get("WIKIKB_SCRAPE_MIN_CHARS") or 200)
DIRECT_MAX_BYTES = int(os.environ.get("WIKIKB_SCRAPE_MAX_BYTES") or 8 * 1024 * 1024)
# How many indexed pages a single `match: prefix` source may pull in one run. A prefix over a large
# documentation site can match thousands of captures; a cron that occasionally decides to write ten
# thousand notes into the immutable tier is a runaway, so the ceiling is explicit and reportable
# rather than implied by whatever the index happens to hold.
PREFIX_LIMIT = int(os.environ.get("WIKIKB_SCRAPE_PREFIX_LIMIT") or 25)


def raw_dir(domain):
    """`vault/_sources/<domain>/_raw/web/` — the ONE directory a harvest may write to."""
    return os.path.join(str(paths.WIKI), "_sources", domain, "_raw", "web")


# --- the direct-fetch escape hatch --------------------------------------------------------------

def _guard_direct(url):
    """Refuse a live fetch aimed at a non-public address.

    This is the second half of the SSRF boundary (the first is the http/https scheme allowlist in
    `sources.normalize`). It matters because `POST /scrape {"url": …, "direct": true}` lets a caller
    name ANY host, and this process typically runs somewhere `169.254.169.254`, `10.x`, and
    `localhost:<admin-port>` are all reachable and all interesting. Resolution happens HERE and
    EVERY resolved address must be public — checking the hostname alone is defeated by a name that
    resolves to a private address.

    # ponytail: not TOCTOU-proof — a hostile DNS server could answer differently for the check and
    # for the fetch. Closing that needs pinning the resolved IP into the connection, which stdlib
    # urllib does not expose. The guard still stops the ordinary metadata-endpoint and
    # internal-service cases, which is what an opt-in fetcher on a watchlist actually faces.
    """
    host = urlsplit(url).hostname
    if not host:
        raise ValueError("no host in %r" % url)
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as e:
        raise ValueError("cannot resolve %s: %s" % (host, e))
    for info in infos:
        addr = ipaddress.ip_address(info[4][0])
        if (addr.is_private or addr.is_loopback or addr.is_link_local or addr.is_multicast
                or addr.is_reserved or addr.is_unspecified):
            raise ValueError("refusing a direct fetch of %s: resolves to the non-public address %s"
                             % (host, addr))
    return True


def fetch_direct(url):
    """Live GET from the origin. Opt-in only; guarded above. Returns (body_bytes, meta)."""
    modes.require_online("direct web fetch")
    _guard_direct(url)
    req = urllib.request.Request(url, headers={"User-Agent": cc.USER_AGENT,
                                               "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=cc.TIMEOUT) as r:
        body = r.read(DIRECT_MAX_BYTES + 1)
        if len(body) > DIRECT_MAX_BYTES:
            raise ValueError("response exceeds WIKIKB_SCRAPE_MAX_BYTES (%d)" % DIRECT_MAX_BYTES)
        return body, {"url": r.url, "http_status": r.status,
                      "content_type": r.headers.get("Content-Type", ""),
                      "timestamp": time.strftime("%Y%m%d%H%M%S", time.gmtime()),
                      "source": "direct"}


# --- writing one harvested note ------------------------------------------------------------------

def _capture_date(ts):
    """CC's `20260721135107` -> `2026-07-21`, the `fetched` date in the `web:` provenance token."""
    s = str(ts or "")
    return "%s-%s-%s" % (s[0:4], s[4:6], s[6:8]) if len(s) >= 8 else time.strftime("%Y-%m-%d")


def _write_note(domain, url, title, markdown, meta, label=None, dry_run=False):
    """Write `<slug>.md` + `<slug>.json` and return the result row.

    The Markdown file holds ONLY the document body — no frontmatter. It is raw material, and the
    frontmatter contract belongs to the reference note `corpus_to_vault` generates downstream; two
    frontmatter blocks in one pipeline would mean two places to keep the same provenance correct.
    Everything a later stage needs is in the sidecar.
    """
    stem = srcmod.slug_for(url)
    d = raw_dir(domain)
    md_path, side_path = os.path.join(d, stem + ".md"), os.path.join(d, stem + ".json")
    digest = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
    prior = None
    if os.path.isfile(side_path):
        try:
            with open(side_path, encoding="utf-8") as fh:
                prior = json.load(fh)
        except (OSError, ValueError):
            prior = None
    if prior and prior.get("body_sha256") == digest and os.path.isfile(md_path):
        return {"url": url, "domain": domain, "status": "unchanged", "file": stem + ".md",
                "chars": len(markdown), "captured": prior.get("captured"),
                "archive": meta.get("archive")}
    # NEVER LET AN OLDER CAPTURE OVERWRITE A NEWER ONE. Harvesting across many crawls means the same
    # URL is captured repeatedly, and every capture maps to the SAME note (the slug is derived from
    # the URL). Without this, walking the crawl history would leave each note holding whichever
    # crawl happened to be processed last — for a newest-first walk, that is the OLDEST capture, and
    # the note would silently regress to 2008 content carrying a 2008 `fetched` date that pages then
    # cite as current. Same-timestamp is allowed through so a re-extraction (better extractor, fixed
    # bug) can still update the body.
    new_ts = str(meta.get("timestamp") or "")
    old_ts = str((prior or {}).get("captured_ts") or "")
    if not old_ts and prior:                       # notes written before captured_ts existed
        old_ts = str(prior.get("captured") or "").replace("-", "")
    if prior and old_ts and new_ts and new_ts[:len(old_ts)] < old_ts:
        # This guard now also arbitrates BETWEEN archives, which is the whole reason several may
        # harvest the same URL safely: whichever archive holds the newest capture wins, regardless
        # of which one ran last. Without it, adding Wayback beside Common Crawl would mean the note
        # ended up holding whichever archive happened to be processed second.
        return {"url": url, "domain": domain, "status": "older-capture", "file": stem + ".md",
                "chars": len(markdown), "captured": prior.get("captured"),
                "archive": meta.get("archive"),
                "hint": "kept the newer capture already on disk (%s, via %s)"
                        % (prior.get("captured"), prior.get("archive") or "commoncrawl")}
    sidecar = {
        "url": url,
        "domain": domain,
        "title": title or url,
        "label": label or title or url,
        "captured": _capture_date(meta.get("timestamp")),
        # The full 14-digit crawl timestamp, kept alongside the human date because the
        # never-overwrite-newer comparison above needs more precision than a day: two crawls can
        # capture the same URL on the same date.
        "captured_ts": str(meta.get("timestamp") or ""),
        # WHICH archive and which of its generations this body came from. `cc_index` is kept beside
        # the generic pair because sidecars written before the multi-archive registry carry it, and
        # a field that silently changes name makes "where did this note come from?" unanswerable for
        # everything harvested before today.
        "archive": meta.get("archive") or meta.get("source") or "commoncrawl",
        "index_id": meta.get("index_id") or meta.get("cc_index"),
        "cc_index": meta.get("cc_index"),
        "warc_file": meta.get("warc_file"),
        "warc_digest": meta.get("digest"),
        "http_status": meta.get("http_status"),
        "content_type": meta.get("content_type"),
        "extractor": meta.get("extractor"),
        "source": meta.get("source", "commoncrawl"),
        "body_sha256": digest,
        "body_file": stem + ".md",
        "harvested": time.strftime("%Y-%m-%d"),
    }
    if dry_run:
        return {"url": url, "domain": domain, "status": "would-write", "file": stem + ".md",
                "chars": len(markdown), "captured": sidecar["captured"],
                "extractor": sidecar["extractor"], "archive": sidecar["archive"]}
    os.makedirs(d, exist_ok=True)
    # Containment assert before any write — the same belt-and-braces check `do_upload` does. The
    # slug is shape-safe by construction, but a planted symlink in the path chain is not shape.
    root = os.path.realpath(str(paths.WIKI)) + os.sep
    if not os.path.realpath(md_path).startswith(root):
        raise ValueError("refusing to write outside the vault: %s" % md_path)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(markdown.rstrip() + "\n")
    with open(side_path, "w", encoding="utf-8") as fh:
        json.dump(sidecar, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return {"url": url, "domain": domain, "status": "updated" if prior else "new",
            "file": stem + ".md", "chars": len(markdown), "captured": sidecar["captured"],
            "extractor": sidecar["extractor"], "archive": sidecar["archive"]}


# --- the public entry points ----------------------------------------------------------------------

def fetch(url, domain=None, match="exact", direct=False, index_id=None, label=None,
          dry_run=False, limit=None, archive="commoncrawl"):
    """Harvest ONE source from ONE index generation of ONE archive.

    `archive` names an entry in the registry (`archives.py`): `commoncrawl` walks crawls,
    `wayback`/`arquivo`/`vefsafn` walk year buckets. `index_id` is that archive's generation id —
    `CC-MAIN-2026-30`, `IA-2019`. The two always travel together, because an id only means anything
    to the archive that minted it.

    ONLINE MODE ONLY — `require_online()` is reached inside the archive's lookup / `fetch_direct`,
    i.e. at the socket, so no caller can route around it.

    Returns a LIST of result rows (one per document written or skipped). It does not raise for the
    ordinary "not in the index" case: that is an ANSWER, reported as `status: "not-indexed"`,
    because a run over a watchlist must not abort on the first site an archive happens not to cover.
    """
    modes.require_online("web scraping")
    if not domain:
        raise ValueError("--domain is required (which knowledge domain does this source feed?)")
    canon = srcmod.normalize(url)
    arch = archmod.get(archive) if not hasattr(archive, "lookup") else archive
    index_id = index_id or (cc.latest_index() if arch.name == "commoncrawl" else arch.indexes()[0])
    limit = limit or (PREFIX_LIMIT if match == "prefix" else 1)

    try:
        recs = arch.lookup(canon, index_id=index_id, match=match, limit=limit)
    except archmod.ArchiveError as e:
        if not direct:
            return [{"url": canon, "domain": domain, "status": "lookup-failed", "error": str(e),
                     "archive": arch.name, "index_id": index_id}]
        recs = []

    rows = []
    if not recs:
        if not direct:
            # The documented outcome of the archive-first design: consult the index, and when the
            # URL is not there, say so rather than quietly reaching for the origin server.
            return [{"url": canon, "domain": domain, "status": "not-indexed",
                     "archive": arch.name, "index_id": index_id}]
        try:
            body, meta = fetch_direct(canon)
        except (ValueError, urllib.error.URLError, OSError, TimeoutError) as e:
            return [{"url": canon, "domain": domain, "status": "fetch-failed", "error": str(e)}]
        captures = [(canon, body, meta)]
    else:
        captures = []
        for rec in recs[:limit]:
            try:
                body, meta = arch.fetch_capture(rec)
            except archmod.ArchiveError as e:
                rows.append({"url": rec.get("url"), "domain": domain, "status": "capture-failed",
                             "archive": arch.name, "error": str(e)})
                continue
            meta["index_id"] = index_id
            meta["archive"] = arch.name
            meta["source"] = arch.name
            if arch.name == "commoncrawl":
                meta["cc_index"] = index_id      # kept: the field name already on disk in sidecars
            captures.append((rec.get("url") or canon, body, meta))

    for got_url, body, meta in captures:
        text = cc.decode_body(body, meta.get("content_type", ""))
        title, markdown, used = extractor.to_markdown(text, url=got_url)
        meta["extractor"] = used
        if len(markdown) < MIN_CHARS:
            # A near-empty extraction is the JS-rendered-page case. Reporting it beats writing a
            # 40-character note into the IMMUTABLE tier, where it would then be cited as ground truth.
            # NO ARCHIVE FIXES THIS, which is why the hint says so: every index here stores the HTML
            # as SERVED, and a client-rendered page serves a shell. Measured 2026-08-07 on a Check
            # Point SK article — 287 visible characters live to a crawler UA, 129 from the Wayback
            # capture. Adding archives widens coverage of static docs; it cannot conjure a body the
            # server never sent.
            rows.append({"url": got_url, "domain": domain, "status": "too-thin",
                         "chars": len(markdown), "extractor": used, "archive": arch.name,
                         "hint": "page is likely JS-rendered; every web index stores the HTML as "
                                 "served, so no archive will hold this body — harvest the site's "
                                 "static doc portal instead"})
            continue
        rows.append(_write_note(domain, got_url, title, markdown, meta, label=label, dry_run=dry_run))
    return rows


def _tally_rows(rows):
    out = {}
    for r in rows:
        out[r["status"]] = out.get(r["status"], 0) + 1
    return out


def plan_indexes(archs, done, max_indexes=None):
    """The (archive, index_id) work list for one source, INTERLEAVED across archives.

    Round-robin, not archive-by-archive, and that is the point: a queued run is bounded
    (`WIKIKB_SCRAPE_MAX_INDEXES_PER_RUN`, 12 by default, so the step finishes inside its timeout).
    Draining Common Crawl's 126 crawls first would mean a nightly run never reached the Internet
    Archive at all for the first eleven days — the archive that, measured on vendor doc sites,
    holds one to two orders of magnitude more pages. Interleaving makes a bounded budget buy
    progress everywhere.

    Each archive contributes its own list newest-first, so the first documents written are the most
    current whichever archive they come from.
    """
    queues = []
    for a in archs:
        try:
            queues.append((a, [i for i in a.indexes() if i not in done]))
        except archmod.ArchiveError:
            continue            # an unreachable crawl list must not stop the archives that answer
    plan = []
    for depth in range(max((len(q) for _, q in queues), default=0)):
        for a, q in queues:
            if depth < len(q):
                plan.append((a, q[depth]))
    if max_indexes and max_indexes > 0:
        plan = plan[:max_indexes]
    return plan


def scrape_source(source, dry_run=False, index_id=None, max_indexes=None, progress=None,
                  state_path=None, archives=None):
    """Harvest ONE watchlist source across every index generation, of every archive, not yet done.

    THE POINT OF WALKING GENERATIONS: Common Crawl samples the web rather than exhaustively
    recrawling it, so which pages of a site appear varies enormously per crawl — measured on
    `support.checkpoint.com`, 3 of 4 harvested pages appear in ONLY the newest crawl. Harvesting
    just the newest index therefore captures a thin, arbitrary slice.

    THE POINT OF WALKING SEVERAL ARCHIVES: the same argument one level up. Different archives made
    different sampling decisions, so their coverage of a vendor doc site differs by orders of
    magnitude (see `archives.py` for the measurements). The union is what a knowledge base wants;
    the ledger and the never-overwrite-a-newer-capture rule are what make taking the union safe.

    THE LEDGER MAKES IT AFFORDABLE — with one asterisk this function is responsible for. A
    published CC crawl is immutable, so a processed one is done forever, including one that held
    NOTHING. A replay archive's CURRENT-YEAR bucket is not immutable, so it is recorded
    `provisional` and re-checked every run; closed years are recorded normally. That asterisk is
    why `record()` is passed the archive's own verdict instead of a blanket "done".

    State is saved after EVERY generation, so an interrupted run resumes instead of restarting.
    `index_id` pins one generation and bypasses the walk entirely (the reproducibility path); it
    needs `archive` too, since an id only means something to the archive that minted it.
    """
    url, domain = source["url"], source.get("domain")
    match = source.get("match", "exact")
    archs = [archmod.get(a) for a in archives] if archives else archmod.for_source(source)
    rows = []

    if index_id:                                   # pinned: one generation, no ledger involvement
        return fetch(url, domain, match=match, direct=bool(source.get("direct")),
                     index_id=index_id, label=source.get("label"), dry_run=dry_run,
                     archive=archs[0].name)

    try:
        done = statemod.done_indexes(statemod.load(state_path), url, match)
    except ValueError as e:
        return [{"url": url, "domain": domain, "status": "invalid", "error": str(e)}]
    # An archive's indexes() may itself write the collinfo cache, so the ledger is never held across
    # it — every write below goes through state.update(), which re-reads first.
    plan = plan_indexes(archs, done, max_indexes)
    if not plan:
        return [{"url": url, "domain": domain, "status": "up-to-date",
                 "hint": "every published index of %s already harvested for this source (%d done)"
                         % ("/".join(a.name for a in archs), len(done))}]

    for n, (arch, cid) in enumerate(plan, 1):
        if progress:
            progress("  [%d/%d] %-11s %-16s %s" % (n, len(plan), arch.name, cid, url))
        try:
            got = fetch(url, domain, match=match, direct=bool(source.get("direct")),
                        index_id=cid, label=source.get("label"), dry_run=dry_run, archive=arch)
        except (ValueError, srcmod.SourceError) as e:
            rows.append({"url": url, "domain": domain, "status": "invalid", "error": str(e)})
            break                                  # a bad source is bad for every archive
        except archmod.ArchiveError as e:
            rows.append({"url": url, "domain": domain, "status": "lookup-failed",
                         "archive": arch.name, "index_id": cid, "error": str(e)})
            continue                               # one unreachable index must not end the walk
        rows.extend(got)
        t = _tally_rows(got)
        # A generation is recorded ONLY when it was actually answered. A lookup failure is transient
        # (the CDX API 503s for long stretches; the IA rate-limits), and recording it as done would
        # permanently skip an index this source was never really checked against.
        if not dry_run and not t.get("lookup-failed"):
            stats = {"new": t.get("new", 0), "updated": t.get("updated", 0),
                     "unchanged": t.get("unchanged", 0), "too_thin": t.get("too-thin", 0),
                     "older": t.get("older-capture", 0), "empty": bool(t.get("not-indexed")),
                     "archive": arch.name,
                     # The asterisk from the docstring: a still-growing bucket is recorded so the
                     # run's progress is visible, but flagged so `done_indexes` does not skip it.
                     "provisional": bool(arch.is_provisional(cid))}
            # After EVERY generation — the run must be resumable. update() re-reads first, so this
            # cannot clobber the collinfo cache the index list may have written above.
            statemod.update(lambda d, c=cid, s=stats: statemod.record(d, url, match, c, s),
                            state_path)
    return rows


def scrape_all(domain=None, dry_run=False, index_id=None, path=None, max_indexes=None,
               progress=None, state_path=None, archives=None):
    """Harvest every ENABLED watchlist source (optionally just one domain's).

    One source's failure never stops the run — each row carries its own status, and the caller (CLI,
    job step, cron tick) reports the tally.
    """
    modes.require_online("web scraping")
    rows = []
    for s in srcmod.list_sources(domain=domain, enabled_only=True, path=path):
        if progress:
            progress("source: %s  [%s]" % (s.get("url"), s.get("domain")))
        try:
            rows.extend(scrape_source(s, dry_run=dry_run, index_id=index_id,
                                      max_indexes=max_indexes, progress=progress,
                                      state_path=state_path, archives=archives))
        except (ValueError, srcmod.SourceError) as e:
            rows.append({"url": s.get("url"), "domain": s.get("domain"), "status": "invalid",
                         "error": str(e)})
        except cc.CrawlError as e:
            rows.append({"url": s.get("url"), "domain": s.get("domain"), "status": "lookup-failed",
                         "error": str(e)})
    return rows


def sources():
    """The configured watchlist plus the runtime facts that decide what a harvest will do.

    Read-only and mode-INDEPENDENT on purpose: an operator debugging an airgapped box still needs to
    see what the watchlist says. Only the fetch itself is online-gated.
    """
    srcs = srcmod.list_sources()
    try:
        doc = statemod.load()
        ledger_error = None
    except ValueError as e:
        doc, ledger_error = statemod._blank(), str(e)
    # Each source carries its own harvest PROGRESS: how many published crawls it has been processed
    # against, how many documents that produced, and where it got to. Without this the API can say
    # what is configured but not what has actually been done — which is the question an operator
    # watching a long first run is actually asking.
    for s in srcs:
        s["state"] = statemod.summary(doc, s.get("url"))
        # What this source will ACTUALLY be checked against — the per-source override resolved
        # against the process default. An operator reading the watchlist should not have to
        # replay `archives.for_source()` in their head to answer "is Wayback on for this one?".
        s["archives_effective"] = [a.name for a in archmod.for_source(s)]
    cached = statemod.collinfo_get(doc, max_age=float("inf")) or []
    return {
        "file": str(paths.SCRAPE_SOURCES),
        "exists": os.path.isfile(str(paths.SCRAPE_SOURCES)),
        "sources": srcs,
        "extractor": extractor.available(),
        "archives": archmod.describe(),
        "lookup_backend": cc.LOOKUP_BACKEND,
        "index_pin": cc.INDEX_PIN or None,
        "state_file": str(paths.SCRAPE_STATE),
        "crawls_published": len(cached) or None,
        "ledger_error": ledger_error,
    }


# --- CLI -------------------------------------------------------------------------------------------

def _tally(rows):
    out = {}
    for r in rows:
        out[r["status"]] = out.get(r["status"], 0) + 1
    return out


def _print_rows(rows):
    for r in rows:
        line = "  %-14s %-11s %s" % (r["status"], r.get("archive") or "", r.get("url"))
        if r.get("chars"):
            line += "  (%d chars%s)" % (r["chars"], ", %s" % r["extractor"] if r.get("extractor") else "")
        if r.get("error"):
            line += "\n                 %s" % r["error"]
        if r.get("hint"):
            line += "\n                 hint: %s" % r["hint"]
        print(line)
    tally = _tally(rows)
    print("\n" + (", ".join("%s=%d" % kv for kv in sorted(tally.items())) or "nothing to do"))
    return tally


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", help="target domain (must be declared in vault/taxonomy.md)")
    ap.add_argument("--url", action="append", default=[],
                    help="harvest this URL (repeatable); need not be on the watchlist")
    ap.add_argument("--all", action="store_true", help="harvest every enabled watchlist source")
    # Watchlist CRUD, mirroring the HTTP surface so the same operations are available on a box
    # where nothing is serving. These four are MODE-INDEPENDENT: editing a config file opens no
    # socket, and an operator preparing a watchlist on an airgapped machine must not be refused.
    ap.add_argument("--list", action="store_true", help="print the watchlist and exit")
    ap.add_argument("--add", metavar="URL", help="add URL to the watchlist (needs --domain)")
    ap.add_argument("--remove", metavar="URL", help="remove URL from the watchlist (harvested notes are kept)")
    ap.add_argument("--update", metavar="URL",
                    help="update URL's entry — only the flags you also pass change "
                         "(--domain/--label/--match/--enable/--disable/--direct/--no-direct)")
    ap.add_argument("--label", help="human label for --add/--update (used in the web: token)")
    ap.add_argument("--enable", dest="enabled", action="store_true", default=None,
                    help="with --update: re-enable the source")
    ap.add_argument("--disable", dest="enabled", action="store_false", default=None,
                    help="with --update: pause the source without losing its configuration")
    ap.add_argument("--no-direct", dest="direct", action="store_false", default=None,
                    help="with --update: forbid the live origin fetch again")
    ap.add_argument("--match", choices=srcmod.MATCH_MODES, default="exact",
                    help="exact URL, or every indexed page under it (default: %(default)s)")
    # default=None, not False: `--direct` and `--no-direct` share this dest, and argparse takes the
    # default from the FIRST action declared for a dest. With False here, `--update <url> --label x`
    # would silently also send direct=False and clobber a source's opt-in — a partial update has to
    # be able to tell "not passed" from "passed as false". Falsy either way on the harvest path.
    ap.add_argument("--direct", action="store_true", default=None,
                    help="allow a LIVE fetch from the origin when Common Crawl has no capture "
                         "(off by default — the archive-first rule)")
    ap.add_argument("--index",
                    help="pin ONE index id — CC-MAIN-2026-30, IA-2019 — and skip the ledger "
                         "entirely (the reproducible path). Default: walk every index not yet "
                         "harvested for the source, newest first, across every enabled archive.")
    ap.add_argument("--archive", action="append", default=[], metavar="NAME",
                    help="query only this web index (repeatable): %s. Default: the source's own "
                         "`archives` list, else WIKIKB_SCRAPE_ARCHIVES (%s). With --add/--update "
                         "this SETS the source's list instead."
                         % (", ".join(archmod.names()), ",".join(archmod.DEFAULT_ARCHIVES)))
    ap.add_argument("--max-indexes", type=int, default=None,
                    help="process at most N not-yet-harvested indexes this run, interleaved across "
                         "archives. The history is ~126 Common Crawl crawls plus ~31 year buckets "
                         "per replay archive; use this to bound a first run and let later runs "
                         "continue (the ledger makes it resumable).")
    ap.add_argument("--forget", metavar="URL",
                    help="drop URL's harvest ledger so its crawls are reprocessed (use after an "
                         "extractor fix); with --index, forget just that one crawl")
    ap.add_argument("--limit", type=int, help="max documents for a --match prefix source")
    ap.add_argument("--dry-run", action="store_true", help="look everything up, write nothing")
    ap.add_argument("--json", action="store_true", help="machine-readable result rows")
    args = ap.parse_args()

    if args.list:
        info = sources()
        if args.json:
            print(json.dumps(info, indent=2, ensure_ascii=False))
        else:
            print("watchlist: %s%s" % (info["file"], "" if info["exists"] else "  (not created yet)"))
            print("extractor: %s   lookup: %s   index: %s"
                  % (info["extractor"], info["lookup_backend"], info["index_pin"] or "latest"))
            print("archives:  default %s   available %s"
                  % (",".join(info["archives"]["default"]), ",".join(info["archives"]["known"])))
            for s in info["sources"]:
                st = s.get("state") or {}
                print("  [%s] %-16s %s%s" % ("x" if s.get("enabled", True) else " ",
                                             s.get("domain"), s.get("url"),
                                             "  (%s)" % s["match"] if s.get("match") != "exact" else ""))
                print("      archives: %s   indexes harvested: %s   documents: %s   last: %s"
                      % (",".join(s.get("archives_effective") or []),
                         st.get("indexes_done", 0), st.get("documents", 0),
                         st.get("last_index") or "—"))
            if not info["sources"]:
                print("  (empty — add one: --add <URL> --domain <d>, POST /scrape/sources, "
                      "or edit the file)")
        return

    if args.forget:
        # Also mode-independent: it only edits the ledger. The escape hatch from the ledger's own
        # correctness rule ("a processed crawl is done forever") — needed after an extractor fix or
        # a widened match, where previously processed crawls really are worth revisiting.
        try:
            doc = statemod.load()
        except ValueError as e:
            raise SystemExit("scrape ▸ %s" % e)
        url = srcmod.normalize(args.forget)
        if statemod.forget(doc, url, args.index):
            statemod.save(doc)
            print("forgot %s for %s — it will be reprocessed on the next run"
                  % (args.index or "every crawl", url))
        else:
            print("nothing to forget for %s%s" % (url, " @ " + args.index if args.index else ""))
        return

    # --- watchlist CRUD -------------------------------------------------------------------------
    # Deliberately BEFORE the mode check: these only edit a JSON config file. Refusing to let an
    # operator prepare a watchlist on an airgapped box would be a posture check applied to
    # something that opens no socket.
    if args.add or args.remove or args.update:
        if sum(bool(x) for x in (args.add, args.remove, args.update)) > 1:
            raise SystemExit("scrape ▸ use one of --add / --remove / --update at a time")
        try:
            if args.add:
                if not args.domain:
                    raise SystemExit("scrape ▸ --add requires --domain")
                e = srcmod.add(args.add, args.domain, label=args.label, match=args.match,
                               direct=bool(args.direct), archives=args.archive or None)
                print("added   %s  [%s]%s\n        archives: %s"
                      % (e["url"], e["domain"],
                         "  (%s)" % e["match"] if e["match"] != "exact" else "",
                         ",".join(e.get("archives") or archmod.DEFAULT_ARCHIVES)))
            elif args.remove:
                e = srcmod.remove(args.remove)
                print("removed %s  [%s]\n        already-harvested notes are KEPT (the raw tier is "
                      "immutable) — to withdraw the knowledge, retract the pages citing it"
                      % (e["url"], e.get("domain")))
            else:
                # Only what was actually passed: `--match` carries an argparse default, so it is
                # forwarded ONLY when the user typed it, or every update would silently reset match.
                fields = {}
                if args.domain:
                    fields["domain"] = args.domain
                if args.label is not None:
                    fields["label"] = args.label
                if "--match" in sys.argv:
                    fields["match"] = args.match
                if args.enabled is not None:
                    fields["enabled"] = args.enabled
                if args.direct is not None:
                    fields["direct"] = args.direct
                if args.archive:
                    fields["archives"] = args.archive
                if not fields:
                    raise SystemExit("scrape ▸ --update needs at least one of --domain/--label/"
                                     "--match/--archive/--enable/--disable/--direct/--no-direct")
                e, changed = srcmod.update(args.update, **fields)
                print("updated %s  [%s]  changed: %s"
                      % (e["url"], e.get("domain"), ", ".join(changed) or "nothing (already set)"))
        except srcmod.SourceError as ex:
            raise SystemExit("scrape ▸ %s" % ex)
        return

    # Mode is checked before anything else so an airgapped refusal is the FIRST thing an operator
    # sees, rather than an argument error that hides which of the two is the real blocker.
    try:
        modes.require_online("web scraping")
    except modes.ModeError as e:
        raise SystemExit("scrape ▸ REFUSED: %s" % e)

    if not args.all and not args.url:
        raise SystemExit("scrape ▸ usage: --all, --url <URL> --domain <d>, --list, "
                         "or --add/--update/--remove <URL>")

    # Progress goes to stdout as it happens, not at the end: a first run walks 126 crawls and is
    # captured in a job log, so an operator (or a stalled-job diagnosis) needs to see WHICH crawl it
    # is on rather than a silent process for twenty minutes.
    progress = None if args.json else (lambda line: print(line, flush=True))
    # A pinned --index implies its archive: `IA-2019` handed to the Common Crawl adapter is not an
    # empty result, it is a mid-run parse error. An explicit --archive still wins.
    if args.index and not args.archive:
        owner = archmod.archive_for_index(args.index)
        if owner is None:
            raise SystemExit("scrape ▸ --index %s: no archive mints ids of that shape "
                             "(expected CC-MAIN-YYYY-NN, or one of %s with a -YYYY suffix)"
                             % (args.index, ", ".join(archmod.names())))
        args.archive = [owner.name]
    try:
        if args.all:
            rows = scrape_all(domain=args.domain, dry_run=args.dry_run, index_id=args.index,
                              max_indexes=args.max_indexes, progress=progress,
                              archives=args.archive or None)
        else:
            if not args.domain:
                raise SystemExit("scrape ▸ --url requires --domain")
            rows = []
            # An ad-hoc --url is NOT on the watchlist, so it has no ledger row and walking the full
            # history for a one-off lookup would be a surprise. It stays single-generation per
            # archive: pinned by --index, else each archive's newest. It DOES still ask every
            # enabled archive — "is this page anywhere" is the question being asked.
            for u in args.url:
                for a in (args.archive or archmod.DEFAULT_ARCHIVES):
                    rows.extend(fetch(u, args.domain, match=args.match, direct=args.direct,
                                      index_id=args.index, dry_run=args.dry_run, limit=args.limit,
                                      archive=a))
    except (srcmod.SourceError, ValueError) as e:
        raise SystemExit("scrape ▸ %s" % e)
    except archmod.ArchiveError as e:
        raise SystemExit("scrape ▸ archive lookup: %s" % e)

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        tally = _tally(rows)
    else:
        print("scrape ▸ indexes=%s  archives=%s  domain=%s" % (
            args.index or ("all not-yet-harvested" if args.all else "newest"),
            ",".join(args.archive) if args.archive else "per-source/default",
            args.domain or "(all)"))
        tally = _print_rows(rows)
        if not args.dry_run and (tally.get("new") or tally.get("updated")):
            print("NEXT: python3 -m wikikb web_to_corpus --domain %s --append --apply  "
                  "(then corpus_to_vault --apply, then build)" % (args.domain or "<domain>"))
    # Exit 1 when EVERY source failed and none succeeded — a cron tick that harvested nothing
    # because the index was unreachable must be distinguishable from one that found no changes.
    # A per-source failure alongside any success is reported, not fatal: the chain should still
    # fold in what it did get.
    hard = sum(tally.get(k, 0) for k in ("lookup-failed", "fetch-failed", "capture-failed", "invalid"))
    ok = sum(tally.get(k, 0) for k in ("new", "updated", "unchanged", "not-indexed", "would-write",
                                       "too-thin"))
    if hard and not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
