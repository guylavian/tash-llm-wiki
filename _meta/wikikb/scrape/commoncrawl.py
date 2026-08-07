#!/usr/bin/env python3
"""commoncrawl.py — look a URL up in the Common Crawl index and pull its archived capture.

stdlib only (urllib + gzip + json). ONLINE MODE ONLY: every function that opens a socket goes
through `_http()`, which calls `modes.require_online()` FIRST — so importing this module on a
sealed box is inert, and a future mis-wired caller still cannot reach the network from an airgapped
deployment (modes.py, property 2).

WHY COMMON CRAWL AND NOT A CRAWLER. Harvesting from CC means the wiki's upstream tier is fed from
an archive that is already fetched, already deduplicated, already dated, and — the part that
matters here — already POLITE: no robots budget is spent, no origin server is hit, and the capture
carries a crawl timestamp that becomes the `fetched` date in the `web:` provenance token. A live
fetch is available as an explicit per-source opt-in (`"direct": true`, see scrape.py), never the
default.

THE FOUR STEPS, AND THE ONE THAT IS NOT OBVIOUS:

    1. collinfo.json          -> the list of crawls, newest first. Cached on disk (TTL) because it
                                 changes ~monthly and every scrape would otherwise refetch it.
    2. <index>-index?url=...  -> CDXJ records: which WARC file, at which byte offset, with what
                                 length. THIS IS THE FLAKY STEP (see below).
    3. Range: bytes=o-o+l-1   -> that one record out of a ~1 GB WARC, from data.commoncrawl.org.
    4. gunzip + parse         -> the archived HTTP response, i.e. the page as the crawler saw it.

STEP 2 HAS TWO BACKENDS, AND THAT IS THE LOAD-BEARING DESIGN DECISION HERE.
`index.commoncrawl.org` is a free, heavily-loaded service that answers 503/504 for long stretches —
verified while writing this module: every request to it returned "504 Gateway Time-out" across four
crawls and repeated retries, while `data.commoncrawl.org` served range requests fine throughout. A
scraper with only the API backend would therefore be a scraper that mostly does not work.

  api      GET <cdx-api>?url=...&output=json — one request, richest filtering. Tried first.
  cluster  The index files themselves, from data.commoncrawl.org: BINARY-SEARCH `cluster.idx` (a
           ~100 MB sorted SURT->block map) with HTTP range requests — ~15 ranged reads of 16 KB,
           never the whole file — then range-fetch and gunzip the one ~250 KB `cdx-000NN.gz` block
           it points at and scan it. Slower per lookup, but it depends only on the bucket that is
           actually reliable.

`WIKIKB_CC_LOOKUP=auto|api|cluster` picks; `auto` (the default) tries the API and falls back to the
cluster on ANY failure. Pin it to `cluster` on a box where the API is chronically down to skip a
guaranteed-wasted request per URL.

# ponytail: no columnar/Athena backend and no WAT/WET support — the CDX + WARC pair answers "is
# this page indexed, and give me its HTML", which is the whole question this module exists to ask.
"""
import gzip
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from wikikb import modes
from wikikb import paths

COLLINFO_URL = "https://index.commoncrawl.org/collinfo.json"
DATA_HOST = "https://data.commoncrawl.org"

# A crawler that does not say who it is gets blocked, and rightly. Overridable so an operator can
# put a real contact address in it — CC asks for one, and it is the difference between being rate
# limited and being banned.
USER_AGENT = (os.environ.get("WIKIKB_SCRAPE_UA")
              or "wikikb-scrape/1.0 (LLM wiki harvester; +https://github.com/)")
TIMEOUT = int(os.environ.get("WIKIKB_CC_TIMEOUT") or 90)
RETRIES = int(os.environ.get("WIKIKB_CC_RETRIES") or 4)
LOOKUP_BACKEND = (os.environ.get("WIKIKB_CC_LOOKUP") or "auto").strip().lower()
INDEX_PIN = (os.environ.get("WIKIKB_CC_INDEX") or "").strip()      # e.g. CC-MAIN-2026-30
COLLINFO_TTL = int(os.environ.get("WIKIKB_CC_COLLINFO_TTL") or 86400)

# Bounds on the cluster backend. A prefix lookup can in principle span many index blocks; each one
# is a ~250 KB ranged GET plus a gunzip, so it is capped rather than left to the shape of the input.
CLUSTER_CHUNK = 16384          # bytes per probe during the binary search
CLUSTER_WINDOW = 65536         # switch to a linear scan once the search range is this small
MAX_BLOCKS = int(os.environ.get("WIKIKB_CC_MAX_BLOCKS") or 8)
MAX_RECORD_BYTES = int(os.environ.get("WIKIKB_CC_MAX_RECORD") or 32 * 1024 * 1024)


class CrawlError(RuntimeError):
    """Any failure talking to Common Crawl: HTTP error, exhausted retries, malformed record.

    One type for all of them because the caller's response is the same in every case — report which
    URL could not be harvested and move to the next source. A run must not die because one site's
    capture is missing.
    """


# --- HTTP --------------------------------------------------------------------------------------

def _http(url, byte_range=None, timeout=None, retries=None, method="GET"):
    """One request, with retries. The ONLY place this package opens a socket.

    `require_online()` is called per REQUEST, not once at import: registration-time gating alone
    would let a stale import or a future refactor reach the network from a sealed deployment.

    Retries cover 429/500/502/503/504 and transient socket errors — the CDX API's normal failure
    mode, not an exceptional one. `Retry-After` is honoured when present (capped, so a hostile or
    fat-fingered header cannot park the job runner's single worker for an hour); otherwise the wait
    is exponential with a ceiling.
    """
    modes.require_online("Common Crawl lookup")
    timeout = TIMEOUT if timeout is None else timeout
    retries = RETRIES if retries is None else retries
    headers = {"User-Agent": USER_AGENT, "Accept-Encoding": "identity"}
    if byte_range:
        headers["Range"] = "bytes=%d-%d" % byte_range
    last = None
    for attempt in range(max(1, retries)):
        req = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read() if method != "HEAD" else b"", dict(r.headers), r.status
        except urllib.error.HTTPError as e:
            last = "HTTP %s %s" % (e.code, e.reason)
            if e.code not in (408, 429, 500, 502, 503, 504):
                raise CrawlError("%s for %s" % (last, url))
            wait = _retry_after(e.headers) if e.headers else None
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            last = "%s: %s" % (type(e).__name__, e)
            wait = None
        if attempt == retries - 1:
            break
        time.sleep(wait if wait is not None else min(30, 2 ** attempt + 1))
    raise CrawlError("%s after %d attempts for %s" % (last, retries, url))


def _retry_after(headers):
    """Seconds from a Retry-After header (delta form only), capped at 60. A date-form value or an
    absurd delta falls back to the exponential schedule — waiting an hour inside the single
    serialized job worker would stall every queued ingest behind it."""
    v = (headers.get("Retry-After") or "").strip()
    if v.isdigit():
        return min(60, int(v))
    return None


def _size(url):
    _, headers, _ = _http(url, method="HEAD")
    try:
        return int(headers.get("Content-Length"))
    except (TypeError, ValueError):
        raise CrawlError("no Content-Length for %s (cannot range-search it)" % url)


# --- step 1: the crawl list ---------------------------------------------------------------------

def collections(force=False):
    """The crawl list from collinfo.json, newest first. Cached IN THE VAULT with a TTL.

    The cache lives in `vault/.scrape-state.json` alongside the harvest ledger, so everything this
    vault knows about Common Crawl travels with a vault copy — including, on a box that cannot reach
    the network yet, the list of crawls it was working through.
    """
    from wikikb.scrape import state as statemod
    try:
        doc = statemod.load()
    except ValueError:
        doc = None                   # a corrupt ledger is reported by the harvest path, not here
    if not force and doc is not None:
        cached = statemod.collinfo_get(doc)
        if cached:
            return cached
    body, _, _ = _http(COLLINFO_URL)
    try:
        data = json.loads(body.decode("utf-8", "replace"))
    except ValueError as e:
        raise CrawlError("collinfo.json is not valid JSON: %s" % e)
    if not isinstance(data, list) or not data:
        raise CrawlError("collinfo.json returned no collections")
    if doc is not None:
        try:
            # update(), not save(): a caller may be holding its own older copy of the ledger, and a
            # blind write of ours would roll back whatever it has committed since.
            statemod.update(lambda d: statemod.collinfo_put(d, data))
        except (OSError, ValueError):
            pass                     # an unwritable vault degrades to "refetch every time"
    return data


def all_indexes(force=False, newest_first=True):
    """Every crawl id, newest first by default.

    NEWEST FIRST is the harvest order, and it is not cosmetic: a first run over the full history is
    long, so if it is cut short by a timeout or a restart, what it already has is the most current
    material rather than 2008's. It is also what makes the "never overwrite a newer capture" rule in
    scrape.py cheap — the good copy is written first and older crawls can only be skipped.
    """
    cols = sorted(collections(force=force), key=lambda c: (c.get("from") or "", c.get("id") or ""),
                  reverse=newest_first)
    return [c["id"] for c in cols if c.get("id")]


def latest_index(force=False):
    """The newest crawl's id, e.g. `CC-MAIN-2026-30`.

    collinfo.json IS served newest-first, but this sorts on the `from` timestamp anyway rather than
    trusting position: "the latest index" is the one fact this whole module is parameterized by,
    and getting it from an ordering convention that is documented nowhere would make a silent
    upstream reordering look like "the page stopped being indexed".

    `WIKIKB_CC_INDEX` pins a specific crawl — the reproducibility escape hatch, since a harvest run
    against a pinned crawl gives the same captures on any day.
    """
    if INDEX_PIN:
        return INDEX_PIN
    cols = collections(force=force)
    def key(c):
        return (c.get("from") or "", c.get("id") or "")
    best = max(cols, key=key)
    cid = best.get("id")
    if not cid:
        raise CrawlError("collinfo.json entries carry no id")
    return cid


def cdx_api_url(index_id, force=False):
    """The `cdx-api` endpoint collinfo.json advertises for a crawl, or the conventional form.

    Prefer what the file says over string-building the URL ourselves — the convention has changed
    before, and the file is authoritative about its own service.
    """
    try:
        for c in collections(force=force):
            if c.get("id") == index_id and c.get("cdx-api"):
                return c["cdx-api"]
    except CrawlError:
        pass
    return "https://index.commoncrawl.org/%s-index" % index_id


# --- step 2: is this URL indexed? ---------------------------------------------------------------

def _keep(rec, want_status="200", want_html=True):
    if want_status and str(rec.get("status") or "") != want_status:
        return False
    if want_html:
        mime = (rec.get("mime-detected") or rec.get("mime") or "").lower()
        if mime and not mime.startswith("text/html") and "xhtml" not in mime:
            return False
    return True


def _newest_per_url(recs):
    """One capture per URL — the newest. A crawl commonly holds several captures of the same page;
    harvesting all of them would write the same document into the raw tier N times under N
    timestamps, and the wiki would then cite whichever one happened to sort last."""
    best = {}
    for r in recs:
        u = r.get("url") or ""
        cur = best.get(u)
        if cur is None or (r.get("timestamp") or "") > (cur.get("timestamp") or ""):
            best[u] = r
    return sorted(best.values(), key=lambda r: r.get("url") or "")


def lookup_api(url, index_id, match="exact", limit=50):
    """CDX HTTP API backend. Raises CrawlError when the service is unavailable (it often is)."""
    params = {"url": url, "output": "json", "limit": str(max(1, limit))}
    if match == "prefix":
        params["matchType"] = "prefix"
    endpoint = "%s?%s" % (cdx_api_url(index_id), urllib.parse.urlencode(params))
    try:
        body, _, _ = _http(endpoint)
    except CrawlError as e:
        # 404 from the CDX API means "no captures", which is an ANSWER, not a failure — the caller
        # must be able to tell "not indexed" apart from "index unreachable", because only the
        # second one should fall back to the other backend.
        if "HTTP 404" in str(e):
            return []
        raise
    out = []
    for line in body.decode("utf-8", "replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError:
            continue
    return out


def _cluster_url(index_id, name):
    return "%s/cc-index/collections/%s/indexes/%s" % (DATA_HOST, index_id, name)


def _cluster_blocks(index_id, key, max_blocks=MAX_BLOCKS):
    """The cluster.idx lines whose block can contain `key` (and the ones after it, for a prefix).

    cluster.idx is a ~100 MB file, sorted, one line per compressed CDX block:

        org,keycloak)/docs-api/... 20260721135107\\tcdx-00244.gz\\t38199450\\t262179\\t732137
        <SURT> <timestamp>         \\t<cdx file> \\t<offset>  \\t<length>\\t<block#>

    Block N covers `[key_N, key_{N+1})`, so the block that can contain `key` is the LAST line whose
    SURT is <= key. It is binary-searched with ranged reads (~15 probes of 16 KB) instead of being
    downloaded.

    THE SUBTLE PART, and the bug this comment exists to prevent recurring: the binary search must
    stop while the window is still bigger than a line and then LINEARLY scan that window. A pure
    bisection that keeps splitting will, once the range is shorter than one line, skip past the very
    line it is looking for and return the block BEFORE it — which reads as "URL not indexed" for a
    page that is indexed. That was reproducible on `org,keycloak)/docs/latest/server_admin/`: the
    correct block starts at `org,keycloak)/docs-api/...` (`-` sorts before `/`) and pure bisection
    returned the previous block, which ends before the target.
    """
    u = _cluster_url(index_id, "cluster.idx")
    n = _size(u)
    lo, hi = 0, n
    while hi - lo > CLUSTER_WINDOW:
        mid = (lo + hi) // 2
        buf = _http(u, (mid, min(n - 1, mid + CLUSTER_CHUNK)))[0].decode("utf-8", "replace")
        i = buf.find("\n")
        if i < 0:
            hi = mid
            continue
        first = buf[i + 1:].split("\n", 1)[0]
        if not first:
            hi = mid
            continue
        if first.split(" ", 1)[0] <= key:
            lo = mid
        else:
            hi = mid
    buf = _http(u, (lo, min(n - 1, hi + CLUSTER_CHUNK)))[0].decode("utf-8", "replace")
    lines = buf.split("\n")
    if lo > 0:
        lines = lines[1:]                      # first line is a fragment of the previous one
    good = [ln for ln in lines if "\t" in ln]
    at = -1
    for i, ln in enumerate(good):
        if ln.split(" ", 1)[0] <= key:
            at = i
        else:
            break
    if at < 0:
        return []
    return good[at:at + max_blocks]


def _parse_cluster_line(line):
    key, rest = line.split(" ", 1)
    _ts, cdxfile, off, length, _blk = rest.split("\t")[:5]
    return key, cdxfile, int(off), int(length)


def lookup_cluster(url, index_id, match="exact", limit=50, max_blocks=MAX_BLOCKS):
    """Index-file backend: binary-search cluster.idx, then scan the CDX block(s) it points at.

    Depends only on data.commoncrawl.org, the bucket that stays up when the CDX API does not.
    """
    key = None
    from wikikb.scrape import sources as srcmod
    key = srcmod.surt(url)
    prefix = key if match == "prefix" else key + " "
    out = []
    for line in _cluster_blocks(index_id, key, max_blocks):
        try:
            _bkey, cdxfile, off, length = _parse_cluster_line(line)
        except ValueError:
            continue
        raw = _http(_cluster_url(index_id, cdxfile), (off, off + length - 1))[0]
        try:
            text = gzip.decompress(raw).decode("utf-8", "replace")
        except (OSError, EOFError, gzip.BadGzipFile) as e:
            raise CrawlError("corrupt index block %s@%d: %s" % (cdxfile, off, e))
        hit_in_block = False
        for ln in text.split("\n"):
            if not ln.startswith(prefix):
                # Blocks are sorted, so once we are past the prefix nothing later in THIS block can
                # match — but a later block still can, which is why the outer loop continues.
                if hit_in_block and ln and ln.split(" ", 1)[0] > key:
                    break
                continue
            hit_in_block = True
            parts = ln.split(" ", 2)
            if len(parts) < 3:
                continue
            try:
                rec = json.loads(parts[2])
            except ValueError:
                continue
            # A CDXJ line is `<surt> <timestamp> {json}` — the timestamp is a LINE FIELD, and
            # (unlike the HTTP API's rows) it is NOT necessarily inside the JSON object. Dropping
            # it here would make every capture found through this backend fall back to "today" as
            # its `fetched` date, i.e. an immutable note would carry a fabricated capture date and
            # claim to be fresher than it is. Set it only when absent, so a JSON that DOES carry
            # one still wins.
            rec.setdefault("timestamp", parts[1])
            rec.setdefault("urlkey", parts[0])
            out.append(rec)
            if len(out) >= limit:
                return out
        if match == "exact" and hit_in_block:
            break                       # an exact key cannot continue into the next block
    return out


def lookup(url, index_id=None, match="exact", limit=50, backend=None, want_html=True):
    """Is `url` in the crawl, and where? Returns CDX records (newest capture per URL), possibly [].

    An EMPTY list is a legitimate answer meaning "not indexed" — the caller reports it and moves on.
    A CrawlError means "could not find out", which is a different fact and is reported differently.
    """
    index_id = index_id or latest_index()
    backend = (backend or LOOKUP_BACKEND or "auto").lower()
    recs, errs = [], []
    order = {"api": ["api"], "cluster": ["cluster"]}.get(backend, ["api", "cluster"])
    for name in order:
        try:
            recs = (lookup_api if name == "api" else lookup_cluster)(url, index_id, match, limit)
            break
        except CrawlError as e:
            errs.append("%s: %s" % (name, e))
    else:
        raise CrawlError("index lookup failed (%s)" % "; ".join(errs))
    return _newest_per_url([r for r in recs if _keep(r, want_html=want_html)])


# --- steps 3+4: pull the capture and unwrap it --------------------------------------------------

_CHARSET_RE = re.compile(rb"""charset\s*=\s*["']?\s*([A-Za-z0-9_\-.:]+)""", re.I)


def fetch_capture(rec):
    """Range-fetch one CDX record's WARC bytes and return the archived HTTP response.

    Returns (payload_bytes, meta) where meta carries the crawl timestamp, the WARC digest, the
    final content type and the archived URL — everything the raw-tier sidecar needs to make the
    harvest citable as `web:<url> (label, fetched YYYY-MM-DD)`.
    """
    for f in ("filename", "offset", "length"):
        if rec.get(f) in (None, ""):
            raise CrawlError("CDX record is missing %r — cannot locate the capture" % f)
    off, length = int(rec["offset"]), int(rec["length"])
    if length <= 0 or length > MAX_RECORD_BYTES:
        raise CrawlError("implausible record length %d for %s" % (length, rec.get("url")))
    raw = _http("%s/%s" % (DATA_HOST, rec["filename"].lstrip("/")), (off, off + length - 1))[0]
    try:
        record = gzip.decompress(raw)
    except (OSError, EOFError, gzip.BadGzipFile) as e:
        raise CrawlError("capture is not a gzip member (%s) for %s" % (e, rec.get("url")))
    warc_headers, http_status, http_headers, body = parse_warc_response(record)
    meta = {
        "url": rec.get("url") or warc_headers.get("warc-target-uri"),
        "timestamp": rec.get("timestamp"),
        "digest": rec.get("digest"),
        "http_status": http_status,
        "content_type": http_headers.get("content-type", ""),
        "warc_date": warc_headers.get("warc-date"),
        "warc_file": rec["filename"],
    }
    return body, meta


def parse_warc_response(record):
    """Split one WARC `response` record into (warc headers, HTTP status, HTTP headers, body).

    Written by hand rather than with warcio: this is ONE record of ONE type, already in memory, and
    a 30-line split is a smaller commitment than a dependency the air-gapped install has to carry.
    Content-Encoding IS decoded here — a WARC response stores the body exactly as it came off the
    wire, so a gzip-encoded page would otherwise reach the extractor as binary noise.
    """
    head, sep, rest = record.partition(b"\r\n\r\n")
    if not sep:
        raise CrawlError("malformed WARC record (no header/body separator)")
    warc_headers = _headers(head.decode("utf-8", "replace"), skip_first=True)
    if warc_headers.get("_type") and warc_headers["_type"].lower() != "response":
        raise CrawlError("expected a WARC response record, got %r" % warc_headers["_type"])
    http_head, sep2, body = rest.partition(b"\r\n\r\n")
    if not sep2:
        raise CrawlError("malformed archived HTTP response (no header/body separator)")
    text = http_head.decode("utf-8", "replace")
    status_line = text.split("\r\n", 1)[0]
    try:
        http_status = int(status_line.split(" ")[1])
    except (IndexError, ValueError):
        http_status = 0
    http_headers = _headers(text, skip_first=True)
    enc = (http_headers.get("content-encoding") or "").lower().strip()
    if enc in ("gzip", "x-gzip"):
        try:
            body = gzip.decompress(body)
        except (OSError, EOFError, gzip.BadGzipFile):
            pass                       # a mislabelled body is better served raw than not at all
    elif enc == "deflate":
        import zlib
        try:
            body = zlib.decompress(body)
        except zlib.error:
            try:
                body = zlib.decompress(body, -zlib.MAX_WBITS)
            except zlib.error:
                pass
    elif enc == "br":
        try:
            import brotli                                        # optional; absent on a stdlib box
            body = brotli.decompress(body)
        except Exception:                                        # noqa: BLE001
            raise CrawlError("capture is brotli-encoded and the `brotli` module is not installed")
    return warc_headers, http_status, http_headers, body


def _headers(text, skip_first=False):
    """`Name: value` lines -> lowercase-keyed dict. The first line (WARC/1.0 or the HTTP status
    line) is kept under `_type`/dropped rather than parsed as a header."""
    out = {}
    lines = text.replace("\r\n", "\n").split("\n")
    if skip_first and lines:
        lines = lines[1:]
    for ln in lines:
        if ":" not in ln:
            continue
        k, v = ln.split(":", 1)
        out[k.strip().lower()] = v.strip()
    if "warc-type" in out:
        out["_type"] = out["warc-type"]
    return out


def decode_body(body, content_type=""):
    """Bytes -> text, using the Content-Type charset, then a `<meta charset>`, then UTF-8.

    `errors="replace"` throughout: a single undecodable byte in a 300 KB page must not cost the
    whole document, and the replacement char is visible to a human reviewing the harvested note.
    """
    enc = None
    m = _CHARSET_RE.search((content_type or "").encode("ascii", "replace"))
    if m:
        enc = m.group(1).decode("ascii", "replace")
    if not enc:
        m = _CHARSET_RE.search(body[:4096])
        if m:
            enc = m.group(1).decode("ascii", "replace")
    for candidate in (enc, "utf-8"):
        if not candidate:
            continue
        try:
            return body.decode(candidate, "replace")
        except (LookupError, UnicodeDecodeError):
            continue
    return body.decode("utf-8", "replace")
