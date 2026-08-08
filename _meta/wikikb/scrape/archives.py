#!/usr/bin/env python3
"""archives.py — the WEB INDEXES a harvest may consult, behind one interface. ONLINE MODE ONLY.

`commoncrawl.py` answers "is this URL in Common Crawl, and give me the capture". This module asks
the SAME question of several archives and hands `scrape.py` a uniform answer, so a watchlist source
is checked against every index that might hold it instead of only the one we happened to build
first.

WHY MORE THAN ONE INDEX — the measurement that forced this (2026-08-07, live):

    support.checkpoint.com/results/sk   CC newest crawl: 1,757 captures   Wayback: 4,382 URLs
    access.redhat.com/solutions          CC newest crawl:   775 captures   Wayback: >50,000 (capped)
    www.cisco.com/c/en/us/td             CC newest crawl: 12,166 captures  Wayback: >50,000 (capped)
    sc1.checkpoint.com/documents         CC: thin                          Wayback: 30,788 HTML pages

Common Crawl SAMPLES the web; the Internet Archive keeps what it (and its partners) chose to save.
They miss different things, so the union is strictly larger than either — and for vendor
documentation, which CC's frontier ranks poorly, the difference is one to two orders of magnitude.

THE FOUR ARCHIVES, AND WHY THESE FOUR. Each was probed live before being wired in; the ones that
answered 403/redirect/timeouts (Library of Congress, Archive-It's `/all` endpoint, the UK Web
Archive, the Memento TimeTravel aggregator, archive.today) are deliberately ABSENT — an index that
cannot be queried without a browser challenge is not an index this can use.

    commoncrawl  WARC + CDX, range-fetched. The existing implementation, wrapped unchanged.
    wayback      Internet Archive. The big win above. CDX server + `id_` raw replay.
    arquivo      arquivo.pt (Portuguese national archive, pywb). Broad but old for vendor sites.
    vefsafn      vefsafn.is (Icelandic national archive, OpenWayback). Captures back to 1996.

Only `commoncrawl,wayback` are enabled by default (`WIKIKB_SCRAPE_ARCHIVES`): those two carry the
vendor coverage, and turning all four on for every source would quadruple a nightly run's request
budget to add captures that are mostly a decade stale. The other two are a per-source opt-in
(`"archives": [...]` on a watchlist entry) for a site the first two do not cover.

TWO DESIGN DECISIONS THAT ARE LOAD-BEARING:

1. THE LEDGER'S IMMUTABILITY ARGUMENT HAD TO BE RE-EARNED, NOT ASSUMED. `state.py` may record a
   (source, index) pair as done FOREVER because a published Common Crawl index never changes. A
   replay archive has no such partition — `web.archive.org` is one continuously growing index, so
   "I have checked Wayback for this source" is a statement with a shelf life of one day.
   So a replay archive is partitioned into YEAR BUCKETS (`IA-2019`, `AQ-2011`, `IS-2004`), queried
   with the CDX server's own `from`/`to` range. A CLOSED year is immutable in practice and is
   recorded done; the CURRENT year is marked `provisional` in the ledger and re-checked on every
   run. Without that split the scraper would either re-scan three decades nightly, or record
   "2026: done" in January and never look again.

2. EVERY SOCKET IS STILL `commoncrawl._http`. This module opens no connection of its own — it
   calls the one function that already carries `modes.require_online()`, the retry/Retry-After
   policy, and the User-Agent. That keeps the egress guard a single chokepoint (CLAUDE.md: "the
   guard is at the socket, not the router", asserted by `mode_probe.py`), so adding three archives
   adds zero new ways to reach the network from a sealed box.

Index ids are globally unique strings across archives (`CC-MAIN-2026-30` vs `IA-2026`), which is
why the ledger needed no schema change to hold four archives' histories side by side.
"""
import json
import os
import re
import time
from urllib.parse import urlencode

from wikikb.scrape import commoncrawl as cc

# One error type for every archive, and it is CC's: `scrape.py` already catches `cc.CrawlError`
# around the whole harvest, and a parallel exception class would mean two catch clauses that must
# be kept in sync forever for no behavioural gain.
ArchiveError = cc.CrawlError

# The default set. Order matters only for reporting — the harvest interleaves them (see
# `scrape.plan_indexes`) so a bounded run makes progress on every archive rather than spending its
# whole budget on the first.
DEFAULT_ARCHIVES = tuple(
    a.strip().lower()
    for a in (os.environ.get("WIKIKB_SCRAPE_ARCHIVES") or "commoncrawl,wayback").split(",")
    if a.strip()
)

# How far back the year-bucket walk goes. 1996 is the Internet Archive's first year; there is no
# vendor documentation older than that and every bucket costs a request.
FIRST_YEAR = int(os.environ.get("WIKIKB_SCRAPE_FIRST_YEAR") or 1996)


# --- CDX parsing: three wire formats, one record shape --------------------------------------------

def parse_cdx(text):
    """Parse a CDX response into CC-shaped records, whatever dialect the server speaks.

    The three shapes actually served by the archives wired in here (all verified live):

        [["urlkey","timestamp","original",…],[…],…]   web.archive.org, output=json — ONE json array
        {"urlkey":…,"timestamp":…,"url":…}\\n…         arquivo.pt (pywb) — NDJSON objects
        com,cisco)/ 19961220164811 {"url":…}\\n…       vefsafn.is (OpenWayback) — CDXJ lines

    Field names are normalized to Common Crawl's (`url`, `mime`, `status`), because the two
    functions that decide WHICH capture to keep — `cc._keep` and `cc._newest_per_url` — are reused
    verbatim rather than re-implemented per archive. One rule for "newest capture per URL, HTML,
    200 only" is worth more than three parsers that each nearly agree with it.
    """
    text = (text or "").strip()
    if not text:
        return []
    out = []
    if text.startswith("["):
        try:
            rows = json.loads(text)
        except ValueError as e:
            raise ArchiveError("CDX response is not valid JSON: %s" % e)
        if not rows:
            return []
        header, body = rows[0], rows[1:]
        if not isinstance(header, list):
            return []
        for row in body:
            if isinstance(row, list) and len(row) == len(header):
                out.append(_normalize(dict(zip(header, row))))
        return out
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("{"):
            try:
                out.append(_normalize(json.loads(line)))
            except ValueError:
                continue
            continue
        parts = line.split(" ", 2)                 # `<surt> <timestamp> {json}`
        if len(parts) < 3 or not parts[2].startswith("{"):
            continue
        try:
            rec = json.loads(parts[2])
        except ValueError:
            continue
        # The timestamp is a LINE field in CDXJ and is not necessarily inside the JSON — the same
        # trap `lookup_cluster` documents. Losing it makes every capture fall back to "today" as its
        # `fetched` date, i.e. an immutable note claiming to be fresher than it is.
        rec.setdefault("timestamp", parts[1])
        rec.setdefault("urlkey", parts[0])
        out.append(_normalize(rec))
    return out


_ALIASES = (("original", "url"), ("mimetype", "mime"), ("statuscode", "status"))


def _normalize(rec):
    for src, dst in _ALIASES:
        if rec.get(src) and not rec.get(dst):
            rec[dst] = rec[src]
    for key in ("status", "timestamp", "length", "offset"):
        if rec.get(key) is not None and not isinstance(rec[key], str):
            rec[key] = str(rec[key])
    return rec


# --- the two archive kinds -------------------------------------------------------------------------

class CommonCrawlArchive:
    """Common Crawl, delegating to `commoncrawl.py` unchanged.

    A wrapper, not a reimplementation: the WARC range-fetch, the cluster.idx binary search and the
    collinfo cache are the parts of this package with the most hard-won detail in them, and the
    point of the registry is to add archives beside that, never to fork it.
    """

    name = "commoncrawl"
    label = "Common Crawl"

    def indexes(self):
        return cc.all_indexes()

    def is_provisional(self, index_id):
        return False                    # a published crawl never changes — the original argument

    def lookup(self, url, index_id, match="exact", limit=50):
        return cc.lookup(url, index_id=index_id, match=match, limit=limit)

    def fetch_capture(self, rec):
        return cc.fetch_capture(rec)


class ReplayArchive:
    """Any CDX-server + `id_`-replay archive (Wayback, pywb, OpenWayback).

    `id_` (or `noFrame`) is the modifier that returns the capture as it was archived — no banner, no
    rewritten links, original headers. Replay is a plain ranged-free GET, which is why these three
    archives cost a fraction of Common Crawl's four-step WARC dance to add.
    """

    def __init__(self, name, label, cdx_url, replay, first_year=FIRST_YEAR, prefix="IA",
                 extra=None):
        self.name = name
        self.label = label
        self.cdx_url = cdx_url
        self.replay = replay            # a format string with {ts} and {url}
        self.first_year = first_year
        self.prefix = prefix
        self.extra = extra or {}

    # -- the year partition ------------------------------------------------------------------------

    def indexes(self):
        """`<PREFIX>-YYYY`, newest first, down to `first_year`.

        Newest-first is the same rule Common Crawl's walk follows and for the same two reasons: an
        interrupted run keeps the most CURRENT material, and it makes `_write_note`'s
        never-overwrite-a-newer-capture guard cheap, because the good copy is always written first.
        """
        now = time.gmtime().tm_year
        return ["%s-%d" % (self.prefix, y) for y in range(now, self.first_year - 1, -1)]

    def year_of(self, index_id):
        m = re.search(r"-(\d{4})$", index_id or "")
        if not m:
            raise ArchiveError("%s: not a year bucket: %r" % (self.name, index_id))
        return int(m.group(1))

    def is_provisional(self, index_id):
        """The current year is still being written to, so it is never recorded as done.

        This is the whole reason a replay archive needed its own partition: a closed year is
        immutable in practice (the archive does backfill occasionally, which `--forget` covers),
        but "2026" in August 2026 is a moving target, and recording it done in January would freeze
        the source's coverage for eleven months with nothing to show that it had.
        """
        return self.year_of(index_id) >= time.gmtime().tm_year

    # -- lookup ------------------------------------------------------------------------------------

    def lookup(self, url, index_id, match="exact", limit=50):
        year = self.year_of(index_id)
        params = {
            "url": url,
            "output": "json",
            "from": "%d0101000000" % year,
            "to": "%d1231235959" % year,
            # Server-side filtering, even though `cc._keep` re-checks it: without it the row budget
            # is spent on redirects and 404 shells before a single 200 is seen.
            "filter": ["statuscode:200", "mimetype:text/html"],
            # One capture per URL per MONTH, not per URL. `collapse=urlkey` would return the FIRST
            # capture in the range — for the current year that is January's, so a page revised in
            # July would never be re-harvested no matter how often the provisional bucket is
            # re-checked. Collapsing on the 6-digit timestamp prefix keeps ≤12 rows per URL and lets
            # `_newest_per_url` pick the right one.
            "collapse": "timestamp:6",
            "limit": str(max(1, limit) * 12),
        }
        if match == "prefix":
            params["matchType"] = "prefix"
        params.update(self.extra)
        try:
            body, _, _ = cc._http("%s?%s" % (self.cdx_url, urlencode(params, doseq=True)))
        except ArchiveError as e:
            # 404 means "nothing captured", which is an ANSWER. Only "could not find out" may
            # propagate — the harvest records a crawl as done only when it was actually answered,
            # and conflating the two would permanently skip a bucket never really checked.
            if "HTTP 404" in str(e):
                return []
            raise
        recs = parse_cdx(body.decode("utf-8", "replace"))
        for r in recs:
            r["archive"] = self.name
            r["index_id"] = index_id
        return cc._newest_per_url([r for r in recs if cc._keep(r)])[:max(1, limit)]

    # -- replay ------------------------------------------------------------------------------------

    def fetch_capture(self, rec):
        """GET the archived body itself. Returns (bytes, meta) — the same pair CC's WARC path does."""
        ts, url = rec.get("timestamp"), rec.get("url")
        if not ts or not url:
            raise ArchiveError("%s: capture record is missing timestamp/url" % self.name)
        body, headers, status = cc._http(self.replay.format(ts=ts, url=url))
        if len(body) > cc.MAX_RECORD_BYTES:
            raise ArchiveError("%s: replayed body exceeds %d bytes for %s"
                               % (self.name, cc.MAX_RECORD_BYTES, url))
        # A replay returns the ORIGINAL payload, so a page archived gzip-encoded arrives encoded.
        # Same decode the WARC path applies, from the same helper — a second copy of this would be a
        # second place for "the extractor received binary noise" to come back.
        body = cc.decode_content_encoding(body, (headers.get("Content-Encoding") or ""))
        return body, {
            "url": url,
            "timestamp": ts,
            "digest": rec.get("digest"),
            "http_status": status,
            "content_type": headers.get("Content-Type", ""),
            "archive": self.name,
        }


# --- the registry ------------------------------------------------------------------------------

_REGISTRY = {}


def _register(a):
    _REGISTRY[a.name] = a
    return a


_register(CommonCrawlArchive())
_register(ReplayArchive(
    "wayback", "Internet Archive Wayback Machine",
    cdx_url="https://web.archive.org/cdx/search/cdx",
    replay="https://web.archive.org/web/{ts}id_/{url}",
    prefix="IA"))
_register(ReplayArchive(
    "arquivo", "Arquivo.pt (Portuguese web archive)",
    cdx_url="https://arquivo.pt/wayback/cdx",
    replay="https://arquivo.pt/wayback/{ts}id_/{url}",
    prefix="AQ"))
_register(ReplayArchive(
    "vefsafn", "Vefsafn.is (Icelandic web archive)",
    cdx_url="https://vefsafn.is/cdx",
    replay="https://vefsafn.is/{ts}id_/{url}",
    prefix="IS"))


def names():
    """Every archive this build can query, in registration order."""
    return list(_REGISTRY)


def get(name):
    try:
        return _REGISTRY[(name or "").strip().lower()]
    except KeyError:
        raise ArchiveError("unknown archive %r (known: %s)" % (name, ", ".join(names())))


def archive_for_index(index_id):
    """Which archive minted this index id, or None.

    `--index CC-MAIN-2026-30` and `--index IA-2019` are both meaningful, and an id handed to the
    wrong archive is not a lookup that returns nothing — it is a parse error mid-run. Pinning an id
    therefore implies its archive unless the operator named one explicitly.
    """
    ident = (index_id or "").strip()
    if ident.upper().startswith("CC-MAIN"):
        return get("commoncrawl")
    for a in _REGISTRY.values():
        prefix = getattr(a, "prefix", None)
        if prefix and re.match(r"^%s-\d{4}$" % re.escape(prefix), ident, re.I):
            return a
    return None


def validate(selection):
    """Canonicalize a per-source `archives:` list, or raise ArchiveError.

    Validated where it is WRITTEN (watchlist add/update), not where it is used, for the same reason
    the domain is: an entry naming an archive that does not exist would sit on the list and fail
    every unattended tick with nobody reading the error.
    """
    if selection in (None, ""):
        return None
    if isinstance(selection, str):
        selection = [s for s in re.split(r"[,\s]+", selection) if s]
    if not isinstance(selection, (list, tuple)):
        raise ArchiveError("archives must be a list of names (known: %s)" % ", ".join(names()))
    out = []
    for item in selection:
        a = get(item)                                   # raises with the known-names list
        if a.name not in out:
            out.append(a.name)
    if not out:
        raise ArchiveError("archives must name at least one of: %s" % ", ".join(names()))
    return out


def for_source(source=None):
    """The archive objects one source should be checked against.

    Per-source `archives:` wins over the process default, so a site that only the Icelandic archive
    captured can be pointed at it without turning that archive on for the whole watchlist.
    """
    chosen = (source or {}).get("archives") or DEFAULT_ARCHIVES
    out = []
    for name in chosen:
        try:
            out.append(get(name))
        except ArchiveError:
            continue                    # a hand-edited unknown name must not break the other three
    return out or [get("commoncrawl")]


def describe():
    """Registry snapshot for `GET /scrape/sources` and `--list`."""
    return {
        "known": names(),
        "default": list(DEFAULT_ARCHIVES),
        "labels": {n: _REGISTRY[n].label for n in _REGISTRY},
    }
