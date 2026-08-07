#!/usr/bin/env python3
"""scrape.py — harvest web sources into the raw tier. ONLINE MODE ONLY (`WIKIKB_MODE=online`).

    python3 -m wikikb scrape --domain keycloak --all             # everything on the watchlist
    python3 -m wikikb scrape --domain keycloak --url https://…   # one URL, watchlist or not
    python3 -m wikikb scrape --domain keycloak --url … --dry-run # look it up, write nothing

    # watchlist CRUD — the same operations as GET/POST/PATCH/DELETE /scrape/sources, available on a
    # box where nothing is serving. These edit a JSON file and open no socket, so unlike a harvest
    # they work in AIRGAPPED mode too:
    python3 -m wikikb scrape --list                              # what is configured
    python3 -m wikikb scrape --add https://… --domain keycloak --label "…" --match prefix
    python3 -m wikikb scrape --update https://… --disable        # partial: only what you pass
    python3 -m wikikb scrape --remove https://…                  # harvested notes are KEPT

WHAT IT DOES, AND WHERE IT STOPS. A harvest resolves the newest Common Crawl index, asks whether
the URL is in it, pulls that capture, extracts Markdown, and writes ONE file plus ONE sidecar into
`vault/_sources/<domain>/_raw/web/`. It does not write a corpus record, a reference note, or a
synthesis page — those are the next three commands (`web_to_corpus` -> `corpus_to_vault` ->
`build`), which is exactly the chain the PDF upload path already runs. Keeping the fetch separate
from the fold-in is what lets a failed extraction be retried without regenerating the vault, and
what lets several harvests share one `build`.

THREE RULES THIS MODULE ENFORCES, EACH BECAUSE THE ALTERNATIVE IS SILENTLY WRONG:

  1. THE RAW TIER IS APPEND/REPLACE-ONLY, PER SOURCE. A harvest writes `<slug>.md` for its own URL
     and nothing else. It never edits another source's file, never touches
     `vault/reference/<domain>/`, and never writes a page under `topics/`|`entities/`|`questions/`.
  2. UNCHANGED CAPTURES ARE SKIPPED, NOT REWRITTEN. The sidecar stores the extracted body's digest;
     a re-run that computes the same digest leaves the file alone. Rewriting it would bump mtimes
     across the raw tier every night and make "what actually changed" unanswerable.
  3. COMMON CRAWL FIRST; A LIVE FETCH IS OPT-IN. `"direct": true` on a source (or `--direct`) lets
     a URL with no capture be fetched from the origin. It is off by default because the point of
     harvesting from the archive is not to hit other people's servers on a cron, and because a
     direct fetch is the only path here that can be aimed at an arbitrary host — which is why it
     also carries the address guard in `_guard_direct()`.

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
from wikikb.scrape import commoncrawl as cc
from wikikb.scrape import extract as extractor
from wikikb.scrape import sources as srcmod

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
                "chars": len(markdown), "captured": prior.get("captured")}
    sidecar = {
        "url": url,
        "domain": domain,
        "title": title or url,
        "label": label or title or url,
        "captured": _capture_date(meta.get("timestamp")),
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
                "extractor": sidecar["extractor"]}
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
            "extractor": sidecar["extractor"]}


# --- the public entry points ----------------------------------------------------------------------

def fetch(url, domain=None, match="exact", direct=False, index_id=None, label=None,
          dry_run=False, limit=None):
    """Harvest ONE source (one URL, or every indexed page under it when `match="prefix"`).

    ONLINE MODE ONLY — `require_online()` is reached inside `cc.lookup` / `fetch_direct`, i.e. at
    the socket, so no caller can route around it.

    Returns a LIST of result rows (one per document written or skipped). It does not raise for the
    ordinary "not in the index" case: that is an ANSWER, reported as `status: "not-indexed"`,
    because a run over a watchlist must not abort on the first site the archive happens not to
    cover.
    """
    modes.require_online("web scraping")
    if not domain:
        raise ValueError("--domain is required (which knowledge domain does this source feed?)")
    canon = srcmod.normalize(url)
    index_id = index_id or cc.latest_index()
    limit = limit or (PREFIX_LIMIT if match == "prefix" else 1)

    try:
        recs = cc.lookup(canon, index_id=index_id, match=match, limit=limit)
    except cc.CrawlError as e:
        if not direct:
            return [{"url": canon, "domain": domain, "status": "lookup-failed", "error": str(e),
                     "cc_index": index_id}]
        recs = []

    rows = []
    if not recs:
        if not direct:
            # The documented outcome of the archive-first design: consult the index, and when the
            # URL is not there, say so rather than quietly reaching for the origin server.
            return [{"url": canon, "domain": domain, "status": "not-indexed", "cc_index": index_id}]
        try:
            body, meta = fetch_direct(canon)
        except (ValueError, urllib.error.URLError, OSError, TimeoutError) as e:
            return [{"url": canon, "domain": domain, "status": "fetch-failed", "error": str(e)}]
        captures = [(canon, body, meta)]
    else:
        captures = []
        for rec in recs[:limit]:
            try:
                body, meta = cc.fetch_capture(rec)
            except cc.CrawlError as e:
                rows.append({"url": rec.get("url"), "domain": domain, "status": "capture-failed",
                             "error": str(e)})
                continue
            meta["cc_index"] = index_id
            meta["source"] = "commoncrawl"
            captures.append((rec.get("url") or canon, body, meta))

    for got_url, body, meta in captures:
        text = cc.decode_body(body, meta.get("content_type", ""))
        title, markdown, used = extractor.to_markdown(text, url=got_url)
        meta["extractor"] = used
        if len(markdown) < MIN_CHARS:
            # A near-empty extraction is the JS-rendered-page case. Reporting it beats writing a
            # 40-character note into the IMMUTABLE tier, where it would then be cited as ground truth.
            rows.append({"url": got_url, "domain": domain, "status": "too-thin",
                         "chars": len(markdown), "extractor": used,
                         "hint": "page is likely JS-rendered; Common Crawl stores the served HTML only"})
            continue
        rows.append(_write_note(domain, got_url, title, markdown, meta, label=label, dry_run=dry_run))
    return rows


def scrape_all(domain=None, dry_run=False, index_id=None, path=None):
    """Harvest every ENABLED watchlist source (optionally just one domain's).

    One source's failure never stops the run — each row carries its own status, and the caller (CLI,
    job step, cron tick) reports the tally.
    """
    modes.require_online("web scraping")
    index_id = index_id or cc.latest_index()
    rows = []
    for s in srcmod.list_sources(domain=domain, enabled_only=True, path=path):
        try:
            rows.extend(fetch(s["url"], s.get("domain"), match=s.get("match", "exact"),
                              direct=bool(s.get("direct")), index_id=index_id,
                              label=s.get("label"), dry_run=dry_run))
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
    return {
        "file": str(paths.SCRAPE_SOURCES),
        "exists": os.path.isfile(str(paths.SCRAPE_SOURCES)),
        "sources": srcmod.list_sources(),
        "extractor": extractor.available(),
        "lookup_backend": cc.LOOKUP_BACKEND,
        "index_pin": cc.INDEX_PIN or None,
    }


# --- CLI -------------------------------------------------------------------------------------------

def _tally(rows):
    out = {}
    for r in rows:
        out[r["status"]] = out.get(r["status"], 0) + 1
    return out


def _print_rows(rows):
    for r in rows:
        line = "  %-14s %s" % (r["status"], r.get("url"))
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
    ap.add_argument("--index", help="pin a crawl id, e.g. CC-MAIN-2026-30 (default: the newest)")
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
            for s in info["sources"]:
                print("  [%s] %-16s %s%s" % ("x" if s.get("enabled", True) else " ",
                                             s.get("domain"), s.get("url"),
                                             "  (%s)" % s["match"] if s.get("match") != "exact" else ""))
            if not info["sources"]:
                print("  (empty — add one: --add <URL> --domain <d>, POST /scrape/sources, "
                      "or edit the file)")
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
                               direct=bool(args.direct))
                print("added   %s  [%s]%s" % (e["url"], e["domain"],
                                              "  (%s)" % e["match"] if e["match"] != "exact" else ""))
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
                if not fields:
                    raise SystemExit("scrape ▸ --update needs at least one of --domain/--label/"
                                     "--match/--enable/--disable/--direct/--no-direct")
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

    try:
        if args.all:
            rows = scrape_all(domain=args.domain, dry_run=args.dry_run, index_id=args.index)
        else:
            if not args.domain:
                raise SystemExit("scrape ▸ --url requires --domain")
            rows = []
            for u in args.url:
                rows.extend(fetch(u, args.domain, match=args.match, direct=args.direct,
                                  index_id=args.index, dry_run=args.dry_run, limit=args.limit))
    except (srcmod.SourceError, ValueError) as e:
        raise SystemExit("scrape ▸ %s" % e)
    except cc.CrawlError as e:
        raise SystemExit("scrape ▸ Common Crawl: %s" % e)

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        tally = _tally(rows)
    else:
        print("scrape ▸ index=%s  domain=%s" % (args.index or cc.latest_index(),
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
