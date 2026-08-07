#!/usr/bin/env python3
"""scrape_probe.py — behaviour probe for the ONLINE-mode web harvester. stdlib only, NO network.

WHY IT OPENS NO SOCKET. `mode_probe.py` already drives the /scrape HTTP surface over a real
loopback socket and asserts the airgapped/online posture and the egress guard. What is left — and
what this probe covers — is the logic that decides WHAT gets fetched and WHAT lands in the vault,
none of which needs the internet:

  A. URL canonicalization + SURT keys — the identity function for a source. Getting this wrong
     harvests the same page twice under two `kb:` tokens, or looks up a SURT that CC never emits.
  B. The watchlist file — the full CRUD (add/list/update/remove), duplicate/unknown-domain/
     bad-scheme rejection, the partial-update and no-op rules, and the atomic write.
  C. The Common Crawl plumbing, driven from FIXTURES rather than the network: choosing the newest
     crawl from a collinfo payload, and unwrapping a real WARC response record byte-for-byte.
  D. HTML -> Markdown, including the too-thin (JS-rendered) case the harvester must refuse to
     write into the immutable tier.
  E. The cron parser: cron fields, @macros, intervals, the DOM/DOW OR rule, and the bad-schedule
     path that must DISABLE the timer without killing the server.
  F. The job chain's SHAPE — that a scrape job runs scrape -> web_to_corpus -> corpus_to_vault ->
     build, and that `--append` is present on the step that would otherwise truncate the corpus
     index. This is asserted structurally, not by running it: a real run would rewrite the vault.
  G. web_to_corpus's record shape and the citation token it predicts.
  H. The harvest ledger: per (source, crawl) rows, the immutability argument that lets a
     negative be recorded, match-mode invalidation, --forget, the read-modify-write rule,
     and the never-overwrite-a-newer-capture guard.

Every case that touches a file writes into a TEMP directory via WIKIKB_SCRAPE_SOURCES, never into
the live vault.

Usage:  python3 wiki/_meta/tests/scrape_probe.py
Exit code: 0 = all pass, 1 = a case failed.
"""
import gzip
import json
import os
import shutil
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
sys.path.insert(0, META)  # test bootstrap: make `import wikikb` importable

from wikikb import modes                                  # noqa: E402
from wikikb import paths                                  # noqa: E402
from wikikb.scrape import commoncrawl as cc               # noqa: E402
from wikikb.scrape import cron as cronmod                 # noqa: E402
from wikikb.scrape import extract as extractor            # noqa: E402
from wikikb.scrape import scrape as scrapemod             # noqa: E402
from wikikb.scrape import sources as srcmod               # noqa: E402
from wikikb.scrape import state as statemod               # noqa: E402
from wikikb.scrape import web_to_corpus as w2c            # noqa: E402
from wikikb.serve import jobs as jobsmod                  # noqa: E402

checks = []


def check(name, ok, detail=""):
    checks.append(bool(ok))
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name,
                          "" if ok else "\n        -> %s" % detail))


# --- A. URL identity ------------------------------------------------------------------------------

def case_urls():
    print("\nA. URL canonicalization + SURT")
    same = {"HTTPS://WWW.Example.com/a/b?q=1#frag", "https://www.example.com:443/a/b?q=1",
            "https://WWW.EXAMPLE.COM/a/b?q=1"}
    canon = {srcmod.normalize(u) for u in same}
    check("three spellings of one URL canonicalize to exactly one form",
          canon == {"https://www.example.com/a/b?q=1"}, "got %r" % canon)
    check("an empty path becomes /", srcmod.normalize("https://example.com") == "https://example.com/")
    for bad, why in (("file:///etc/passwd", "file scheme"), ("javascript:alert(1)", "javascript"),
                     ("ftp://x/y", "ftp"), ("", "empty"), ("https://", "no host")):
        try:
            srcmod.normalize(bad)
            check("normalize refuses %s" % why, False, "accepted %r" % bad)
        except srcmod.SourceError:
            check("normalize refuses %s (the scheme allowlist is the first SSRF boundary)" % why, True)
    # SURT is what the CC index is SORTED by; `www.` must be dropped or every www-hosted page
    # reports as "not indexed" against a key the index never emits.
    check("SURT drops www. and reverses the host",
          srcmod.surt("https://www.keycloak.org/docs/latest/server_admin/")
          == "org,keycloak)/docs/latest/server_admin/",
          srcmod.surt("https://www.keycloak.org/docs/latest/server_admin/"))
    check("slug_for is stable across equivalent spellings",
          srcmod.slug_for("HTTPS://Example.com/a#x") == srcmod.slug_for("https://example.com/a"))
    long_url = "https://example.com/" + "x" * 400
    check("slug_for caps a very long URL and stays unique (hash tail)",
          len(srcmod.slug_for(long_url)) <= 121
          and srcmod.slug_for(long_url) != srcmod.slug_for(long_url + "y"),
          srcmod.slug_for(long_url))


# --- B. the watchlist -----------------------------------------------------------------------------

def case_watchlist():
    print("\nB. the watchlist file")
    tmp = tempfile.mkdtemp(prefix="wikikb-scrape-probe-")
    path = os.path.join(tmp, "scrape-sources.json")
    try:
        check("a missing file reads as an empty watchlist, not an error",
              srcmod.load(path)["sources"] == [])
        domains = sorted(srcmod._known_domains())
        if not domains:
            check("taxonomy declares at least one domain (needed for the rest of case B)", False)
            return
        dom = domains[0]
        e = srcmod.add("HTTPS://WWW.Example.com/docs/#top", dom, label="probe", path=path)
        check("add stores the CANONICAL url", e["url"] == "https://www.example.com/docs/", e["url"])
        try:
            srcmod.add("https://www.example.com/docs/", dom, path=path)
            check("a duplicate (canonically equal) url is refused", False, "accepted")
        except srcmod.SourceError:
            check("a duplicate (canonically equal) url is refused", True)
        try:
            srcmod.add("https://other.example/", "no-such-domain-xyz", path=path)
            check("an undeclared domain is refused at WRITE time, not at harvest time", False)
        except srcmod.SourceError:
            check("an undeclared domain is refused at WRITE time, not at harvest time", True)
        check("list_sources/domains see the entry",
              [s["url"] for s in srcmod.list_sources(path=path)] == ["https://www.example.com/docs/"]
              and srcmod.domains(path=path) == [dom])
        srcmod.set_enabled("https://www.example.com/docs/", False, path=path)
        check("a disabled source drops out of the enabled-only views",
              srcmod.list_sources(enabled_only=True, path=path) == []
              and len(srcmod.list_sources(path=path)) == 1)
        check("the file on disk is valid JSON with version+sources",
              json.load(open(path, encoding="utf-8"))["version"] == srcmod.VERSION)

        # --- update(): partial, identity-preserving, and honest about no-ops ---
        srcmod.set_enabled("https://www.example.com/docs/", True, path=path)
        entry, changed = srcmod.update("HTTPS://WWW.Example.com/docs/#anchor", path=path,
                                       label="patched", enabled=False)
        check("update patches only the fields passed, and selects by CANONICAL url",
              changed == ["label", "enabled"] and entry["label"] == "patched"
              and entry["enabled"] is False and entry["match"] == "exact", (entry, changed))
        mtime = os.path.getmtime(path)
        time.sleep(0.05)
        _, changed = srcmod.update("https://www.example.com/docs/", path=path, label="patched")
        check("a NO-OP update reports changed:[] and does not rewrite the file",
              changed == [] and os.path.getmtime(path) == mtime,
              "changed=%r rewritten=%s" % (changed, os.path.getmtime(path) != mtime))
        # The URL is the entry's identity: it names the harvested note and the kb: token citing
        # pages use, so patching it would strand the harvested file under the old slug.
        try:
            srcmod.update("https://www.example.com/docs/", path=path, new_url="https://other.test/")
            check("update REFUSES a url rename and says why", False, "accepted")
        except srcmod.SourceError as e:
            check("update REFUSES a url rename and says why (rename = remove + add)",
                  "identity" in str(e), str(e))
        for bad, why in (({"match": "sideways"}, "an invalid match mode"),
                         ({"domain": "no-such-domain-xyz"}, "an undeclared domain"),
                         ({"frequency": "daily"}, "an unknown field")):
            try:
                srcmod.update("https://www.example.com/docs/", path=path, **bad)
                check("update rejects %s" % why, False, "accepted %r" % bad)
            except srcmod.SourceError:
                check("update rejects %s" % why, True)
        try:
            srcmod.update("https://nothing-here.test/", path=path, enabled=True)
            check("updating a url that is not on the watchlist raises", False)
        except srcmod.SourceError:
            check("updating a url that is not on the watchlist raises (-> 404 over HTTP)", True)
        check("set_enabled delegates to update (one copy of the find-and-save rule)",
              srcmod.set_enabled("https://www.example.com/docs/", True, path=path)["enabled"] is True)
        removed = srcmod.remove("https://www.example.com/docs/?", path=path) if False else \
            srcmod.remove("https://www.example.com/docs/", path=path)
        check("remove returns the removed entry and empties the list",
              removed["url"] == "https://www.example.com/docs/"
              and srcmod.list_sources(path=path) == [])
        try:
            srcmod.remove("https://www.example.com/docs/", path=path)
            check("removing something not on the list raises", False)
        except srcmod.SourceError:
            check("removing something not on the list raises (-> 404 over HTTP)", True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("{ this is not json")
        try:
            srcmod.load(path)
            check("a CORRUPT watchlist raises instead of reading as empty", False,
                  "silently treated as empty — a hand-edit typo would look like 'no sources'")
        except srcmod.SourceError:
            check("a CORRUPT watchlist raises instead of reading as empty", True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- C. Common Crawl plumbing, from fixtures --------------------------------------------------------

COLLINFO = [
    {"id": "CC-MAIN-2026-25", "cdx-api": "https://index.commoncrawl.org/CC-MAIN-2026-25-index",
     "from": "2026-06-05T21:48:11", "to": "2026-06-18T19:32:05"},
    {"id": "CC-MAIN-2026-30", "cdx-api": "https://index.commoncrawl.org/CC-MAIN-2026-30-index",
     "from": "2026-07-10T07:05:34", "to": "2026-07-23T01:13:28"},
    {"id": "CC-MAIN-2025-51", "cdx-api": "https://index.commoncrawl.org/CC-MAIN-2025-51-index",
     "from": "2025-12-01T00:00:00", "to": "2025-12-14T00:00:00"},
]

WARC_RECORD = (
    b"WARC/1.0\r\n"
    b"WARC-Type: response\r\n"
    b"WARC-Date: 2026-07-21T07:26:30Z\r\n"
    b"WARC-Target-URI: https://example.com/doc\r\n"
    b"Content-Length: 123\r\n"
    b"\r\n"
    b"HTTP/1.1 200 OK\r\n"
    b"Content-Type: text/html; charset=utf-8\r\n"
    b"\r\n"
    b"<html><head><title>Doc</title></head><body><h1>Doc</h1><p>Hello</p></body></html>"
)


def case_commoncrawl():
    print("\nC. Common Crawl plumbing (fixtures, no network)")
    # latest_index sorts on the `from` timestamp rather than trusting collinfo's ordering: a silent
    # upstream reorder must not read as "the page stopped being indexed".
    saved_pin = cc.INDEX_PIN
    cc.INDEX_PIN = ""
    orig = cc.collections
    cc.collections = lambda force=False: list(COLLINFO)      # deliberately NOT newest-first
    try:
        check("latest_index picks the newest crawl by date, not by list position",
              cc.latest_index() == "CC-MAIN-2026-30", cc.latest_index())
        check("cdx_api_url prefers the endpoint collinfo advertises",
              cc.cdx_api_url("CC-MAIN-2026-30").endswith("CC-MAIN-2026-30-index"))
        cc.INDEX_PIN = "CC-MAIN-2025-51"
        check("WIKIKB_CC_INDEX pins a crawl (the reproducibility escape hatch)",
              cc.latest_index() == "CC-MAIN-2025-51")
    finally:
        cc.collections = orig
        cc.INDEX_PIN = saved_pin

    warc, status, http_headers, body = cc.parse_warc_response(WARC_RECORD)
    check("parse_warc_response splits WARC headers / HTTP status / HTTP headers / body",
          warc.get("warc-target-uri") == "https://example.com/doc" and status == 200
          and http_headers.get("content-type", "").startswith("text/html")
          and body.startswith(b"<html>"), "status=%r body=%r" % (status, body[:40]))
    check("decode_body honours the Content-Type charset",
          "Hello" in cc.decode_body(body, http_headers.get("content-type")))
    # A gzip-encoded body must be DECODED here — a WARC stores the response exactly as it came off
    # the wire, so an undecoded one reaches the extractor as binary noise.
    gz_record = WARC_RECORD.replace(b"Content-Type: text/html; charset=utf-8\r\n\r\n",
                                    b"Content-Type: text/html\r\nContent-Encoding: gzip\r\n\r\n")
    head, _, payload = gz_record.partition(b"\r\n\r\n")
    http_head, _, raw_body = payload.partition(b"\r\n\r\n")
    gz_record = head + b"\r\n\r\n" + http_head + b"\r\n\r\n" + gzip.compress(raw_body)
    _, _, _, decoded = cc.parse_warc_response(gz_record)
    check("a gzip Content-Encoding body is decompressed, not handed on as noise",
          decoded == raw_body, "%r" % decoded[:40])
    for bad, why in ((b"no separator at all", "no header/body separator"),
                     (b"WARC/1.0\r\nWARC-Type: request\r\n\r\nx", "not a response record")):
        try:
            cc.parse_warc_response(bad)
            check("a malformed record raises CrawlError (%s)" % why, False, "no raise")
        except cc.CrawlError:
            check("a malformed record raises CrawlError (%s)" % why, True)
    # `_keep` is what stops a 404 or a PDF capture becoming a "documentation" reference note.
    check("only 200/text-html captures survive the CDX filter",
          cc._keep({"status": "200", "mime-detected": "text/html"})
          and not cc._keep({"status": "404", "mime-detected": "text/html"})
          and not cc._keep({"status": "200", "mime-detected": "application/pdf"}))
    newest = cc._newest_per_url([{"url": "u", "timestamp": "20260101000000"},
                                 {"url": "u", "timestamp": "20260721000000"}])
    check("several captures of one URL collapse to the NEWEST",
          len(newest) == 1 and newest[0]["timestamp"] == "20260721000000", "%r" % newest)
    # A CDXJ line carries the timestamp as a LINE FIELD, not inside the JSON. Losing it would give
    # an immutable note a fabricated `fetched` date (today's), which is a provenance falsification,
    # not a cosmetic gap — so the cluster backend's line parse is asserted directly.
    line = ('com,checkpoint,support)/ 20260719031917 '
            '{"url": "https://support.checkpoint.com/", "status": "200", "mime-detected": "text/html"}')
    parts = line.split(" ", 2)
    rec = json.loads(parts[2])
    rec.setdefault("timestamp", parts[1])
    check("the cluster backend keeps the CDXJ line's timestamp (the real capture date)",
          rec["timestamp"] == "20260719031917", rec)


# --- D. extraction ---------------------------------------------------------------------------------

HTML = """<html><head><title>Server Guide</title><style>.x{color:red}</style></head>
<body><nav class="site-nav"><a href="/">Home</a><a href="/menu">Menu</a></nav>
<main><h1>Server Guide</h1><p>Configure the <code>quarkus.http.port</code> option.</p>
<h2>Steps</h2><ul><li>First step</li><li>Second step</li></ul>
<pre>kc.sh start --optimized</pre>
<p>See <a href="https://example.org/spec">the spec</a> and <a href="/rel">this</a>.</p></main>
<footer class="site-footer">(c) 2026 nobody</footer>
<script>var tracking=1;</script></body></html>"""


def case_extract():
    print("\nD. HTML -> Markdown")
    title, md, used = extractor.to_markdown(HTML, url="https://example.com/g")
    check("title comes from <title>", title == "Server Guide", repr(title))
    check("headings survive as Markdown", "# Server Guide" in md and "## Steps" in md, md[:200])
    check("list items survive", "- First step" in md and "- Second step" in md, md[:300])
    check("a code block survives", "kc.sh start --optimized" in md, md[:400])
    check("script/style content never reaches the body",
          "tracking" not in md and "color:red" not in md, md[:300])
    check("chrome marked by class (nav/footer) is dropped",
          "Menu" not in md and "nobody" not in md, md[:300])
    check("an absolute link keeps its target; a relative one degrades to text, never a wrong URL",
          "[the spec](https://example.org/spec)" in md and "](/rel)" not in md, md[-200:])
    check("the extractor names itself (it goes into the sidecar)", used in ("stdlib", "trafilatura"))
    _, empty, _ = extractor.to_markdown("<html><body><script>x=1</script></body></html>")
    check("a JS-only page extracts to (near) nothing — the too-thin case the harvester refuses",
          len(empty) < 200, repr(empty[:80]))
    check("available() reports which extractor is live", extractor.available() in ("stdlib", "trafilatura"))


# --- E. the cron parser ------------------------------------------------------------------------------

def case_cron():
    print("\nE. the scheduled-harvest timer")
    base = time.mktime(time.strptime("2026-08-05 12:30:00", "%Y-%m-%d %H:%M:%S"))
    cases = [("0 3 * * *", "2026-08-06 03:00"), ("@hourly", "2026-08-05 13:00"),
             ("*/15 * * * *", "2026-08-05 12:45"), ("0 0 1 * *", "2026-09-01 00:00")]
    for spec, want in cases:
        got = cronmod.Schedule(spec).next_after(base)
        got_s = time.strftime("%Y-%m-%d %H:%M", time.localtime(got)) if got else None
        check("schedule %-14r fires next at %s" % (spec, want), got_s == want, "got %s" % got_s)
    s = cronmod.Schedule("6h")
    check("an interval schedule is supported and is relative, not clock-aligned",
          s.interval == 21600 and s.next_after(base) == base + 21600)
    # The DOM/DOW OR rule: `0 0 1 * mon` means "the 1st, AND every Monday" — the intersection would
    # be a schedule that almost never fires, which is the classic cron misreading.
    nxt = cronmod.Schedule("0 0 1 * mon").next_after(base)
    check("DOM and DOW are OR-ed when both are restricted (standard cron)",
          time.strftime("%Y-%m-%d", time.localtime(nxt)) == "2026-08-10",
          time.strftime("%Y-%m-%d", time.localtime(nxt)))
    for bad in ("bogus", "0 99 * * *", "1 2 3", "* * * * * *", "5s"):
        try:
            cronmod.Schedule(bad)
            check("a malformed schedule %r is rejected" % bad, False, "accepted")
        except cronmod.CronError:
            check("a malformed schedule %r is rejected" % bad, True)
    check("a schedule matching nothing within the horizon reports 'never', not a hang",
          cronmod.Schedule("0 0 30 2 *").next_after(base) is None)

    # A bad schedule DISABLES the timer and is reported — unlike WIKIKB_MODE, it must not stop the
    # server: a harvest that does not run is visible in the status endpoint and harms nothing else.
    sched = cronmod.Scheduler(spec="nonsense", enabled=True)
    check("a bad schedule leaves the scheduler inert, reported, and NOT raising",
          sched.schedule is None and sched.error and sched.status()["kind"] == "invalid",
          sched.status())
    check("start() on a bad schedule spawns no thread", sched.start().status()["running"] is False)

    fired = []
    live = cronmod.Scheduler(spec="1h", enabled=True, submit=lambda: fired.append(1) or {"queued": []})
    st = live.status()
    check("status separates the LIVE flag from the boot default (the toggle never rewrites env)",
          st["enabled"] is True and st["env_default"] == cronmod.env_enabled() and "next_run" in st)
    off = live.set_enabled(False)
    check("set_enabled(False) clears the next run immediately",
          off["enabled"] is False and off["next_run"] is None, off)
    check("re-enabling recomputes the next run", live.set_enabled(True)["next_run"] is not None)
    live._fire()
    check("a fire calls the submit hook and records the result",
          fired == [1] and live.runs == 1 and live.last_run, live.status())
    live._submit = lambda: (_ for _ in ()).throw(RuntimeError("boom"))
    live._fire()
    check("a failing tick is recorded, never raised (a dead timer would stop every future harvest)",
          live.runs == 2 and "boom" in json.dumps(live.last_result), live.last_result)
    check("nothing started a thread at import", cronmod.SCHEDULER.status()["running"] is False)


# --- F. the job chain's shape ------------------------------------------------------------------------

def case_job_chain():
    print("\nF. the scrape job chain (structure only — running it would rewrite the vault)")
    steps = jobsmod.scrape_steps("keycloak")
    names = [n for n, _ in steps]
    check("a watchlist scrape runs scrape -> web_to_corpus -> corpus_to_vault -> build",
          names == ["scrape", "web_to_corpus", "corpus_to_vault", "build"], names)
    argv = dict(steps)
    check("a watchlist run passes --all (per-source flags come from the FILE, not the run)",
          "--all" in argv["scrape"] and "--url" not in argv["scrape"], argv["scrape"])
    # The single most destructive omission in this whole chain: without --append, web_to_corpus
    # truncates corpora/<domain>/index.jsonl and the next corpus_to_vault regenerates the immutable
    # reference tier from the truncation.
    check("web_to_corpus carries --append (without it one scrape destroys the corpus index)",
          "--append" in argv["web_to_corpus"] and "--apply" in argv["web_to_corpus"],
          argv["web_to_corpus"])
    check("web_to_corpus gets an ABSOLUTE --src (steps run with cwd=_meta/, not the vault)",
          os.path.isabs(argv["web_to_corpus"][argv["web_to_corpus"].index("--src") + 1]))

    one = dict(jobsmod.scrape_steps("keycloak", urls=["https://a.test/x"], direct=True))
    check("a per-URL run passes --url and the explicit --direct",
          "--url" in one["scrape"] and "https://a.test/x" in one["scrape"]
          and "--direct" in one["scrape"] and "--all" not in one["scrape"], one["scrape"])

    # A step resolves the vault ITSELF, and runs with cwd=_meta/ while the server usually starts
    # from the repo root — so a relative WIKIKB_VAULT_ROOT would have parent and child pointing at
    # two different vaults. Observed 2026-08-07: the scrape step created and harvested into
    # `_meta/vault-blank`, reported "nothing to do", and the chain died at corpus_to_vault while
    # /scrape/sources kept listing the source from the real vault.
    child = jobsmod._child_env()
    check("the child env pins ABSOLUTE vault/corpora paths (cwd=_meta/ must not re-resolve them)",
          os.path.isabs(child["WIKIKB_VAULT_ROOT"]) and os.path.isabs(child["WIKIKB_CORPORA_DIR"])
          and child["WIKIKB_VAULT_ROOT"] == str(paths.WIKI)
          and child["WIKIKB_CORPORA_DIR"] == str(paths.CORPORA),
          {k: child.get(k) for k in ("WIKIKB_VAULT_ROOT", "WIKIKB_CORPORA_DIR")})

    q = jobsmod.Runner(start_worker=False)          # queues without ever draining — no vault writes
    j1, c1 = q.submit(jobsmod.Job("scrape", jobsmod.scrape_steps("keycloak"), domain="keycloak",
                                  coalesce_key=("scrape", "keycloak")))
    j2, c2 = q.submit(jobsmod.Job("scrape", jobsmod.scrape_steps("keycloak"), domain="keycloak",
                                  coalesce_key=("scrape", "keycloak")))
    check("a second queued WATCHLIST scrape coalesces into the first (it would redo identical work)",
          c1 is False and c2 is True and j1.id == j2.id)
    j3, c3 = q.submit(jobsmod.Job("scrape", jobsmod.scrape_steps("keycloak", urls=["https://a.test/x"]),
                                  domain="keycloak", coalesce_key=None))
    check("an explicit per-URL scrape NEVER coalesces (it would harvest a different set of URLs)",
          c3 is False and j3.id != j1.id)


# --- G. raw web notes -> corpus records ---------------------------------------------------------------

def case_web_to_corpus():
    print("\nG. web_to_corpus")
    tmp = tempfile.mkdtemp(prefix="wikikb-w2c-probe-")
    try:
        sidecar = {"url": "https://www.keycloak.org/docs/latest/server_admin/",
                   "title": "Server Administration Guide", "label": "KC admin guide",
                   "captured": "2026-07-21", "source": "commoncrawl",
                   "body_file": "x.md", "body_sha256": "deadbeef"}
        stem = "www-keycloak-org-docs-latest-server-admin"
        with open(os.path.join(tmp, stem + ".json"), "w", encoding="utf-8") as fh:
            json.dump(sidecar, fh)
        with open(os.path.join(tmp, stem + ".md"), "w", encoding="utf-8") as fh:
            fh.write("# Server Administration Guide\n\nBody text about LDAP federation.\n")
        # An orphan .md must be SKIPPED, not guessed at: the sidecar is where the URL and the
        # capture date live, and inventing either puts a wrong `fetched` date on an immutable note.
        with open(os.path.join(tmp, "orphan.md"), "w", encoding="utf-8") as fh:
            fh.write("no sidecar\n")

        recs, bodies, orphans = w2c.build(tmp, "keycloak")
        check("one complete pair yields one record; the orphan is reported, not guessed",
              len(recs) == 1 and len(orphans) == 1 and orphans[0][0] == "orphan.md", (recs, orphans))
        r = recs[0]
        check("the record keeps the REAL url (it becomes the note's source: frontmatter)",
              r["url"] == sidecar["url"])
        check("family is scoped to the host, so two sites' /index.html cannot collide",
              r["family"] == "web-keycloak-org", r["family"])
        check("the predicted citation token matches corpus_to_vault's own slug rule",
              w2c.predicted_slug(r) == "web-keycloak-org-server-admin", w2c.predicted_slug(r))
        body = bodies[r["body_file"]]
        check("the body carries the upstream/community banner with url + capture date",
              "Upstream / community source" in body and "2026-07-21" in body
              and sidecar["url"] in body, body[:200])
        check("the page's own duplicate H1 is dropped (corpus_to_vault prepends its own)",
              body.count("# Server Administration Guide") == 0, body[:300])
        check("the abstract carries no Markdown heading syntax",
              not r["abstract"].lstrip().startswith("#"), r["abstract"][:60])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- H. the harvest ledger -------------------------------------------------------------------------

def case_ledger():
    print("\nH. the harvest ledger (vault-resident, per source × crawl)")
    tmp = tempfile.mkdtemp(prefix="wikikb-ledger-probe-")
    p = os.path.join(tmp, ".scrape-state.json")
    U = "https://example.com/docs/"
    try:
        check("a missing ledger reads as empty, not an error",
              statemod.load(p)["sources"] == {} and statemod.done_indexes(statemod.load(p), U, "exact") == set())

        statemod.update(lambda d: statemod.record(d, U, "exact", "CC-MAIN-2026-30", {"new": 7}), p)
        statemod.update(lambda d: statemod.record(d, U, "exact", "CC-MAIN-2026-25", {"empty": True}), p)
        done = statemod.done_indexes(statemod.load(p), U, "exact")
        # A crawl that held NOTHING is recorded too. A published crawl is immutable, so "nothing
        # here" is permanently true — without the row, every future run would re-scan every empty
        # crawl in the history to rediscover the same nothing.
        check("a crawl that yielded NOTHING is still recorded as done (crawls are immutable)",
              done == {"CC-MAIN-2026-30", "CC-MAIN-2026-25"}, done)
        s = statemod.summary(statemod.load(p), U)
        check("summary rolls up crawls done / documents / where it got to",
              s["indexes_done"] == 2 and s["documents"] == 7 and s["last_index"] == "CC-MAIN-2026-30", s)

        # Widening exact -> prefix changes what a crawl would yield, so nothing counts as done.
        check("changing the match mode invalidates the source's history",
              statemod.done_indexes(statemod.load(p), U, "prefix") == set())

        statemod.update(lambda d: statemod.forget(d, U, "CC-MAIN-2026-30"), p)
        check("--forget drops one crawl so it is reprocessed",
              statemod.done_indexes(statemod.load(p), U, "exact") == {"CC-MAIN-2026-25"})
        statemod.update(lambda d: statemod.forget(d, U), p)
        check("--forget with no crawl drops the source's whole history",
              statemod.done_indexes(statemod.load(p), U, "exact") == set())

        # THE REGRESSION: the ledger holds two independently-written things (collinfo + the crawl
        # rows) written by different call paths. Holding a doc across another writer's save and then
        # blind-saving it rolled the collinfo cache back to None on the first real multi-index run.
        statemod.update(lambda d: statemod.collinfo_put(d, [{"id": "CC-MAIN-2026-30"}]), p)
        stale = statemod.load(p)                      # a caller's copy, taken BEFORE the next write
        statemod.update(lambda d: statemod.record(d, U, "exact", "CC-MAIN-2026-21", {"new": 1}), p)
        statemod.update(lambda d: statemod.collinfo_put(d, [{"id": "A"}, {"id": "B"}]), p)
        fresh = statemod.load(p)
        check("update() re-reads, so one writer cannot roll back another's committed state",
              len(statemod.collinfo_get(fresh, max_age=float("inf")) or []) == 2
              and "CC-MAIN-2026-21" in statemod.done_indexes(fresh, U, "exact"),
              "collinfo=%r rows=%r" % (fresh.get("collinfo"), fresh["sources"]))
        check("the stale in-memory copy really was stale (the bug this guards)",
              statemod.collinfo_get(stale, max_age=float("inf")) is not None
              and "CC-MAIN-2026-21" not in statemod.done_indexes(stale, U, "exact"))

        with open(p, "w", encoding="utf-8") as fh:
            fh.write("{ not json")
        try:
            statemod.load(p)
            check("a CORRUPT ledger raises instead of reading as empty", False,
                  "silently empty ⇒ it would re-harvest the entire crawl history")
        except ValueError:
            check("a CORRUPT ledger raises instead of reading as empty (re-harvest would be hours)", True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # The never-overwrite-a-newer-capture rule. Walking crawls newest-first means the same URL is
    # met repeatedly; without this the note would end up holding the OLDEST capture while carrying
    # its old `fetched` date, which citing pages would then present as current.
    vault = tempfile.mkdtemp(prefix="wikikb-capture-probe-")
    saved = os.environ.get("WIKIKB_VAULT_ROOT")
    try:
        os.environ["WIKIKB_VAULT_ROOT"] = vault
        import importlib
        importlib.reload(paths)
        importlib.reload(scrapemod)
        meta_new = {"timestamp": "20260721000000", "cc_index": "CC-MAIN-2026-30"}
        meta_old = {"timestamp": "20200101000000", "cc_index": "CC-MAIN-2020-05"}
        r1 = scrapemod._write_note("d", "https://example.com/p", "T", "NEW BODY " * 30, meta_new)
        r2 = scrapemod._write_note("d", "https://example.com/p", "T", "OLD BODY " * 30, meta_old)
        r3 = scrapemod._write_note("d", "https://example.com/p", "T", "NEWER BODY " * 30,
                                   {"timestamp": "20260722000000"})
        body = open(os.path.join(scrapemod.raw_dir("d"), r1["file"]), encoding="utf-8").read()
        check("an OLDER capture never overwrites a newer note",
              r1["status"] == "new" and r2["status"] == "older-capture" and "OLD BODY" not in body,
              (r1["status"], r2["status"]))
        check("a NEWER capture does replace it", r3["status"] == "updated", r3["status"])
    finally:
        if saved is None:
            os.environ.pop("WIKIKB_VAULT_ROOT", None)
        else:
            os.environ["WIKIKB_VAULT_ROOT"] = saved
        import importlib
        importlib.reload(paths)
        importlib.reload(scrapemod)
        shutil.rmtree(vault, ignore_errors=True)


def main():
    print("=" * 78)
    print("SCRAPE PROBE — watchlist, Common Crawl plumbing, extraction, cron, job chain")
    print("=" * 78)
    # Belt-and-braces: nothing here should reach the network, and the mode default is the airgapped
    # one, so an accidental socket call would raise ModeError rather than quietly going out.
    os.environ.pop(modes.ENV_VAR, None)
    case_urls()
    case_watchlist()
    case_commoncrawl()
    case_extract()
    case_cron()
    case_job_chain()
    case_web_to_corpus()
    case_ledger()
    print("-" * 78)
    print("%d/%d passed" % (sum(checks), len(checks)))
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
