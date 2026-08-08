#!/usr/bin/env python3
"""sources.py — the scrape watchlist: which websites this vault harvests, into which domain.

stdlib only, no network. Importing this module opens nothing and reads nothing; every entry point
is an explicit call. The network lives in `commoncrawl.py` / `scrape.py`, behind
`modes.require_online()`.

THE FILE (`vault/scrape-sources.json`, override with `WIKIKB_SCRAPE_SOURCES`):

    {
      "version": 1,
      "sources": [
        {"url": "https://www.keycloak.org/docs/latest/server_admin/",
         "domain": "keycloak",
         "label": "Keycloak Server Administration Guide (upstream)",
         "match": "exact",          # or "prefix" — harvest every indexed page under this path
         "enabled": true,
         "direct": false,           # allow a live fetch when NO archive has a capture
         "archives": null,          # null = the process default (WIKIKB_SCRAPE_ARCHIVES);
                                    #   ["wayback"] etc. pins which web indexes this site is
                                    #   looked up in — see archives.py
         "added": "2026-08-05"}
      ]
    }

WHY IT IS VAULT-RESIDENT AND WHY IT IS CONFIG-ONLY — the two decisions worth writing down:

  * Vault-resident (next to taxonomy.md, not under _meta/) because it describes the CONTENT: "this
    knowledge base tracks these upstream pages". A vault copied to another machine that silently
    stopped refreshing the sources it believes it is watching is the same class of failure that
    moved taxonomy.md into the vault in the first place.
  * CONFIG ONLY — no `last_scraped`, no `last_digest`, no run counters. This file is hand-editable
    in Obsidian AND rewritten by the API, so a scraper that also wrote fetch state into it would
    race a human's edit and lose it. Per-URL state lives in the raw-tier sidecar the harvest
    already writes (`_sources/<domain>/_raw/web/<slug>.json`), which is where provenance belongs:
    the record of what was fetched sits next to what was fetched.

THE URL IS THE KEY. `normalize()` canonicalizes before compare/store (lowercase scheme+host, drop
the fragment, drop a default port, empty path -> "/"), so adding the same page twice as
`HTTPS://Example.com/a#top` and `https://example.com/a` is one entry, not two — the duplicate would
otherwise harvest the same document into two reference notes with two different `kb:` tokens.

Writes are atomic (tmp + os.replace) because the API can add a source while the cron scheduler is
reading the list; a torn JSON file would take the scheduler down with a parse error on the next tick.
"""
import json
import os
import re
import tempfile
import time
from urllib.parse import urlsplit, urlunsplit

from wikikb import paths

VERSION = 1
MATCH_MODES = ("exact", "prefix")
MAX_SOURCES = 2000          # bounded like every other network-reachable list in this toolchain: the
                            # API can append to this file, and an unbounded watchlist is an
                            # unbounded cron workload, not just a big file.
DEFAULT_PORTS = {"http": "80", "https": "443"}


class SourceError(ValueError):
    """Invalid source (bad URL, unknown domain, duplicate, list full). Reported to the operator as
    text — 400 over HTTP, a SystemExit line on the CLI — never handled differently in code."""


# --- URL canonicalization ---------------------------------------------------------------------

def normalize(url):
    """Canonical form of a source URL, or raise SourceError.

    ONLY http/https. This is the first half of the SSRF boundary (the second is the address check
    in scrape.py's direct fetcher): a scheme allowlist here means `file:///etc/passwd`,
    `javascript:` and `gopher:` are rejected at the point a URL ENTERS the system, not at the point
    something tries to open it.
    """
    raw = (url or "").strip()
    if not raw:
        raise SourceError("url is required")
    if len(raw) > 2048:
        raise SourceError("url too long (max 2048 chars)")
    parts = urlsplit(raw)
    if parts.scheme.lower() not in ("http", "https"):
        raise SourceError("url must be http:// or https:// (got %r)" % (parts.scheme or "no scheme"))
    if not parts.hostname:
        raise SourceError("url has no host: %r" % url)
    scheme = parts.scheme.lower()
    host = parts.hostname.lower()
    netloc = host
    if parts.port and str(parts.port) != DEFAULT_PORTS[scheme]:
        netloc = "%s:%d" % (host, parts.port)
    path = parts.path or "/"
    # Fragment dropped: it never reaches the server, so two URLs differing only by #anchor are the
    # same document to a crawler AND to Common Crawl's index.
    return urlunsplit((scheme, netloc, path, parts.query, ""))


_slug_bad = re.compile(r"[^a-z0-9]+")


def slug_for(url):
    """Stable filename stem for a URL's harvested note.

    Derived from the canonical URL minus its scheme, so the same page always lands on the same file
    and a re-scrape UPDATES that file instead of accumulating dated copies. The 120-char cap plus
    the 8-hex tail of the full URL keeps deep query-string URLs from colliding after truncation —
    two sources sharing a body file would silently overwrite each other's ground truth.
    """
    canon = normalize(url)
    bare = canon.split("//", 1)[-1]
    stem = _slug_bad.sub("-", bare.lower()).strip("-") or "page"
    if len(stem) > 120:
        import hashlib
        stem = stem[:112].rstrip("-") + "-" + hashlib.sha256(canon.encode("utf-8")).hexdigest()[:8]
    return stem


def surt(url):
    """SURT key for a URL — the sort key Common Crawl's index is ordered by.

    `https://www.keycloak.org/docs/x?a=1` -> `org,keycloak)/docs/x?a=1`. The `www.` prefix is
    dropped because that is what CC's canonicalizer does; keeping it would look up a key that
    never appears in the index and report every www-hosted page as "not indexed".
    """
    parts = urlsplit(normalize(url))
    host = parts.hostname or ""
    if host.startswith("www."):
        host = host[4:]
    rev = ",".join(reversed(host.split(".")))
    tail = parts.path or "/"
    if parts.query:
        tail += "?" + parts.query
    return "%s)%s" % (rev, tail.lower())


# --- the file ----------------------------------------------------------------------------------

def _blank():
    return {"version": VERSION, "sources": []}


def load(path=None):
    """Parsed watchlist. A MISSING file is an empty list, not an error — a vault that has never
    configured a source is a normal state, and making `GET /scrape/sources` 500 on it would send an
    operator hunting for a bug instead of showing them the empty list they actually have."""
    p = str(path or paths.SCRAPE_SOURCES)
    if not os.path.isfile(p):
        return _blank()
    try:
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as e:
        # A corrupt watchlist is NOT silently treated as empty: "no sources configured" and "your
        # sources file is unparseable" must not look the same, or a typo in a hand edit would show
        # up as a cron that quietly stopped harvesting.
        raise SourceError("cannot read %s: %s" % (p, e))
    if not isinstance(doc, dict) or not isinstance(doc.get("sources"), list):
        raise SourceError("%s: expected {\"version\":1,\"sources\":[...]}" % p)
    return doc


def save(doc, path=None):
    """Atomic write (tmp in the same directory + os.replace).

    The API can add a source while the cron scheduler is reading the list. A partially written file
    would make the scheduler's next tick raise a JSON parse error, i.e. one bad moment would turn
    into a stopped scraper — os.replace makes the swap indivisible on both POSIX and Windows.
    """
    p = str(path or paths.SCRAPE_SOURCES)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    doc["version"] = VERSION
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or ".", prefix=".scrape-sources-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2, sort_keys=False)
            fh.write("\n")
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return p


def list_sources(domain=None, enabled_only=False, path=None):
    out = []
    for s in load(path)["sources"]:
        if domain and s.get("domain") != domain:
            continue
        if enabled_only and not s.get("enabled", True):
            continue
        out.append(s)
    return out


def domains(enabled_only=True, path=None):
    """Distinct target domains on the watchlist, in file order.

    This is what "scrape everything" fans out over: the conversion chain after a harvest
    (web_to_corpus -> corpus_to_vault -> build) is PER DOMAIN, so a run has to be one job per
    domain rather than one job over a mixed list.
    """
    seen = []
    for s in list_sources(enabled_only=enabled_only, path=path):
        d = s.get("domain")
        if d and d not in seen:
            seen.append(d)
    return seen


def find(url, path=None):
    """The stored entry for `url` (canonical compare), or None."""
    canon = normalize(url)
    for s in load(path)["sources"]:
        try:
            if normalize(s.get("url", "")) == canon:
                return s
        except SourceError:
            continue                    # a hand-edited bad entry must not break lookup of good ones
    return None


def _known_domains():
    """Declared domains, loaded lazily so this module stays importable in isolation (the probe
    imports it without a vault)."""
    from wikikb.build import tags
    return set(tags.load_domains())


def _validate_archives(selection):
    """Canonicalize an `archives` list through the registry, re-raising as SourceError.

    Same write-time rule as the domain, one level down: an entry naming an archive this build does
    not have would sit on the watchlist and be silently ignored on every tick, so the source would
    look configured while being checked against fewer indexes than its owner believes.
    """
    from wikikb.scrape import archives as archmod        # lazy: keeps this module import-light
    try:
        return archmod.validate(selection)
    except archmod.ArchiveError as e:
        raise SourceError(str(e))


def add(url, domain, label=None, match="exact", enabled=True, direct=False, today=None, path=None,
        archives=None):
    """Add one source. Returns the stored entry. Raises SourceError on anything invalid.

    The domain is validated against `vault/taxonomy.md` HERE rather than at harvest time on purpose:
    an entry naming a domain that does not exist would pass config, sit on the watchlist, and then
    fail every cron tick from then on with an error nobody is watching. Fail at write time, where a
    human is present to read the message. `archives` follows the same rule.
    """
    canon = normalize(url)
    if match not in MATCH_MODES:
        raise SourceError("match must be one of %s" % ", ".join(MATCH_MODES))
    archives = _validate_archives(archives)
    known = _known_domains()
    if domain not in known:
        raise SourceError("unknown domain %r — declare it in vault/taxonomy.md first (known: %s)"
                          % (domain, ", ".join(sorted(known)) or "none"))
    doc = load(path)
    for s in doc["sources"]:
        try:
            same = normalize(s.get("url", "")) == canon
        except SourceError:
            same = False
        if same:
            raise SourceError("already on the watchlist: %s (domain %s)" % (canon, s.get("domain")))
    if len(doc["sources"]) >= MAX_SOURCES:
        raise SourceError("watchlist full (%d sources); remove some before adding more" % MAX_SOURCES)
    entry = {"url": canon, "domain": domain, "label": (label or "").strip() or None,
             "match": match, "enabled": bool(enabled), "direct": bool(direct),
             # None, not the resolved default list: a source that inherits the default must KEEP
             # inheriting it. Freezing today's default into every entry would mean turning an
             # archive on later silently applied to nothing already on the watchlist.
             "archives": archives,
             "added": today or time.strftime("%Y-%m-%d")}
    doc["sources"].append(entry)
    save(doc, path)
    return entry


def remove(url, path=None):
    """Remove one source by URL (canonical compare). Returns the removed entry.

    Removing a source does NOT delete anything it already harvested. That is deliberate: the raw
    tier is immutable ground truth and synthesis pages cite it, so un-watching a site must not
    silently invalidate every page that cites what it produced. Withdrawing the KNOWLEDGE is
    Operation: RETRACT, a separate and explicitly authored act.
    """
    canon = normalize(url)
    doc = load(path)
    keep, removed = [], None
    for s in doc["sources"]:
        try:
            same = normalize(s.get("url", "")) == canon
        except SourceError:
            same = False
        if same and removed is None:
            removed = s
        else:
            keep.append(s)
    if removed is None:
        raise SourceError("not on the watchlist: %s" % canon)
    doc["sources"] = keep
    save(doc, path)
    return removed


def update(url, path=None, **fields):
    """Patch ONE source in place. Only the fields actually passed are touched.

    Returns (entry, changed) where `changed` is the list of field names that really moved — so a
    caller can tell "updated" from "you sent the values it already had". Accepts `domain`, `label`,
    `match`, `enabled`, `direct`.

    THE URL IS NOT PATCHABLE, and that is the one rule worth stating out loud. The URL is this
    entry's IDENTITY: it is what the watchlist is keyed by, what the Common Crawl lookup is built
    from, and — through `slug_for()` — what names the harvested note and therefore the `kb:` token
    every citing page uses. Editing it in place would leave the already-harvested file sitting
    under the OLD slug while the source claims the new URL, i.e. a note whose provenance no longer
    matches anything on the watchlist. Renaming is DELETE + POST, two explicit acts.

    `domain` IS patchable, because picking the wrong one at add time is an ordinary mistake and the
    alternative (delete and re-add) loses the rest of the entry. It does not move anything already
    harvested — the caller is told so rather than left to assume either behaviour.
    """
    canon = normalize(url)
    unknown = sorted(set(fields) - {"domain", "label", "match", "enabled", "direct", "archives"})
    if unknown:
        # A rename attempt gets the REASON, not just "unknown field". `url` is the selector (the
        # caller passes it positionally), so a client trying to rename reaches for `new_url` — and
        # a bare "not updatable: new_url" would leave them guessing whether it is a spelling
        # problem or a rule.
        if {"url", "new_url", "newurl", "newUrl"} & set(unknown):
            raise SourceError(
                "the url is a source's identity and cannot be patched — it names the harvested note "
                "and the kb: token citing pages use, so patching it would strand the harvested file "
                "under the old slug. Remove %s and add the new url instead." % canon)
        raise SourceError("not updatable: %s (allowed: domain, label, match, enabled, direct, "
                          "archives)" % ", ".join(unknown))
    if "match" in fields and fields["match"] not in MATCH_MODES:
        raise SourceError("match must be one of %s" % ", ".join(MATCH_MODES))
    if "archives" in fields:
        # Widening this is the edit to make deliberately: it does NOT re-check indexes already
        # recorded done for the archives already on the list — those rows stay valid, which is the
        # point of the ledger. A newly added archive simply has no rows yet and is walked from
        # scratch. (Unlike `match`, which invalidates the whole history because it changes what
        # every index would have yielded.)
        fields["archives"] = _validate_archives(fields["archives"])
    if "domain" in fields:
        known = _known_domains()
        if fields["domain"] not in known:
            raise SourceError("unknown domain %r — declare it in vault/taxonomy.md first (known: %s)"
                              % (fields["domain"], ", ".join(sorted(known)) or "none"))

    doc = load(path)
    for s in doc["sources"]:
        try:
            same = normalize(s.get("url", "")) == canon
        except SourceError:
            same = False
        if not same:
            continue
        changed = []
        for key, value in fields.items():
            if key == "label":
                value = (value or "").strip() or None
            elif key in ("enabled", "direct"):
                value = bool(value)
            if s.get(key) != value:
                s[key] = value
                changed.append(key)
        if changed:                      # a no-op patch must not rewrite the file: an unchanged
            save(doc, path)              # watchlist that keeps getting new mtimes makes "when did
        return s, changed                # this last actually change?" unanswerable
    raise SourceError("not on the watchlist: %s" % canon)


def set_enabled(url, enabled, path=None):
    """Flip one source's `enabled` flag — pause a noisy site without losing its configuration.

    Delegates to `update()` rather than walking the file again: two copies of "find the entry and
    save" would be two places for the canonical-compare rule to drift.
    """
    return update(url, path=path, enabled=enabled)[0]
