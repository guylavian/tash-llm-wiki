#!/usr/bin/env python3
"""state.py — the harvest LEDGER: which crawl has been processed for which source. stdlib, no network.

Lives in the vault (`vault/.scrape-state.json`, hidden like `.manifest.json`) because it is the
scraper's MEMORY, and memory is data. Copy the vault to another machine and the far end resumes
exactly where this one stopped instead of re-downloading a decade of Common Crawl.

WHY A LEDGER EXISTS AT ALL — the fact everything here rests on:

    A PUBLISHED CRAWL IS IMMUTABLE.

`CC-MAIN-2026-30` will contain the same captures forever; Common Crawl never rewrites a published
index. So "source Y has been harvested against index X" is not a cache that can go stale — it is
permanently true. That makes the skip decision exact rather than heuristic, and it is why a
NEGATIVE result is recorded too: if a crawl held nothing for a source, it never will, so re-checking
it on every future run would be pure waste. Without that, a watchlist source would re-scan all 126
crawls nightly to discover the same nothing.

WHAT IS RECORDED, AND AT WHAT GRANULARITY. One row per **(source, crawl)** — not per URL. A
`match: prefix` source expands to a different set of URLs in every crawl (measured: 3 of 4 pages
harvested from `support.checkpoint.com` appear in ONLY the newest crawl), so per-URL rows could not
answer the question the loop actually asks, which is "do I need to look in this crawl at all?".
Per-URL provenance already lives where it belongs: the raw-tier sidecar next to the harvested file.

THE MATCH MODE IS PART OF THE KEY. Flipping a source from `exact` to `prefix` changes what a crawl
would yield, so previously-done crawls are no longer done — the stored rows are invalidated rather
than silently trusted, which would otherwise leave a widened source permanently under-harvested.

The collinfo cache rides along in the same file: it is the other piece of "what this vault knows
about Common Crawl", and one file means one thing to copy and one thing to lock.
"""
import json
import os
import tempfile
import time

from wikikb import paths

VERSION = 1
COLLINFO_TTL = int(os.environ.get("WIKIKB_CC_COLLINFO_TTL") or 86400)


def _blank():
    return {"version": VERSION, "collinfo": None, "sources": {}}


def load(path=None):
    """The ledger. A missing file is an empty ledger — a vault that has never scraped is normal.

    A CORRUPT file is NOT silently treated as empty: that would re-harvest every crawl for every
    source, which is hours of network for what is really a one-line JSON problem. It raises, and the
    caller reports it.
    """
    p = str(path or paths.SCRAPE_STATE)
    if not os.path.isfile(p):
        return _blank()
    try:
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as e:
        raise ValueError("cannot read the scrape ledger %s: %s" % (p, e))
    if not isinstance(doc, dict) or not isinstance(doc.get("sources"), dict):
        raise ValueError('%s: expected {"version":1,"collinfo":…,"sources":{…}}' % p)
    doc.setdefault("collinfo", None)
    return doc


def update(mutate, path=None):
    """Load fresh → mutate → save. **The only supported way to write the ledger.**

    WHY NOT load-once-then-save-later: the ledger holds two independently-written things — the
    collinfo cache and the per-crawl rows — and they are written by different call paths. A harvest
    that loaded the doc, then called `cc.all_indexes()` (which fetches and stores collinfo through
    its OWN load/save), then saved its stale copy would silently roll the collinfo cache back to
    None. That is exactly what happened on the first multi-index run: the crawl rows landed, the
    cached crawl list vanished, and the next run refetched it as if nothing had been stored.

    Re-reading immediately before every write makes each writer see the others' committed state. The
    job runner is single-worker and the CLI is single-process, so a fresh read plus the atomic
    replace in save() is sufficient — this is about two code paths in ONE process, not concurrency.
    """
    doc = load(path)
    mutate(doc)
    save(doc, path)
    return doc


def save(doc, path=None):
    """Atomic write (tmp + os.replace). Prefer `update()` — see the warning there.

    Saved after EVERY crawl, not once at the end: a full first run over 126 crawls is long enough to
    be interrupted by a job timeout, a restart, or Ctrl-C, and a ledger written only at the end would
    turn any of those into "start over from 2008". Incremental saves make the run resumable, which is
    the difference between a feature and an ordeal.
    """
    p = str(path or paths.SCRAPE_STATE)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    doc["version"] = VERSION
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or ".", prefix=".scrape-state-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return p


# --- the collinfo cache ---------------------------------------------------------------------

def collinfo_get(doc, max_age=None):
    """The cached crawl list if it is fresh enough, else None.

    Unlike the per-crawl rows, this one IS a real cache with a TTL: new crawls are published
    roughly monthly, so the list itself changes — only the crawls already in it are immutable.
    """
    entry = (doc or {}).get("collinfo") or {}
    cols = entry.get("collections")
    if not cols:
        return None
    age = time.time() - float(entry.get("fetched") or 0)
    if age > (COLLINFO_TTL if max_age is None else max_age):
        return None
    return cols


def collinfo_put(doc, collections):
    doc["collinfo"] = {"fetched": time.time(), "collections": collections}
    return doc


# --- the per-(source, crawl) rows -------------------------------------------------------------

def _src(doc, url, match):
    """The row-set for one source, reset when the match mode changed (see the module docstring)."""
    row = doc["sources"].get(url)
    if row is None or row.get("match") != match:
        row = {"match": match, "indexes": {}}
        doc["sources"][url] = row
    return row


def done_indexes(doc, url, match):
    """Crawl ids already processed for this source — the set the harvest loop skips."""
    row = doc["sources"].get(url)
    if row is None or row.get("match") != match:
        return set()                 # match changed ⇒ nothing counts as done any more
    return set(row.get("indexes") or {})


def record(doc, url, match, index_id, stats, today=None):
    """Mark (source, crawl) processed, with what it yielded. Mutates `doc`; caller saves."""
    row = _src(doc, url, match)
    entry = {"harvested": today or time.strftime("%Y-%m-%d")}
    entry.update({k: v for k, v in (stats or {}).items() if v})
    row["indexes"][index_id] = entry
    return doc


def forget(doc, url, index_id=None):
    """Drop one crawl's row, or the whole source's history (index_id=None).

    The re-harvest escape hatch: an extractor fix or a widened `match` can make a previously
    processed crawl worth revisiting, and without this the ledger's own correctness guarantee
    ("done means done") would make that impossible without hand-editing JSON.
    """
    row = doc["sources"].get(url)
    if not row:
        return False
    if index_id is None:
        del doc["sources"][url]
        return True
    return row.get("indexes", {}).pop(index_id, None) is not None


def summary(doc, url):
    """Per-source roll-up for `GET /scrape/sources` and `--list`."""
    row = (doc.get("sources") or {}).get(url)
    if not row:
        return {"indexes_done": 0, "documents": 0, "last_index": None, "last_harvested": None}
    idx = row.get("indexes") or {}
    docs = sum(int(e.get("new", 0)) + int(e.get("updated", 0)) for e in idx.values())
    newest = max(idx, default=None)          # crawl ids sort chronologically as strings
    return {"indexes_done": len(idx), "documents": docs, "last_index": newest,
            "last_harvested": (idx.get(newest) or {}).get("harvested") if newest else None}
