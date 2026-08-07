#!/usr/bin/env python3
"""domains.py — full CRUD over the DOMAIN DECLARATIONS in the vault taxonomy. stdlib only, no network.

Importing this module opens nothing and reads nothing; every entry point is an explicit call.

THE FILE IS `vault/taxonomy.md` — `paths.TAXONOMY`, so it follows `WIKIKB_VAULT_ROOT` and travels
with a copied vault, exactly like `scrape-sources.json`. Nothing about a domain is stored under
`_meta/`: a domain declaration describes the CONTENT ("this knowledge base covers these
technologies"), and a vault copied without it lints every page as an unknown domain and indexes
nothing — the failure that moved taxonomy.md into the vault in the first place.

WHY A FIFTH PARSER IS *NOT* WHAT THIS IS. Four modules already read this file, each for one field
and each authoritative for it:

    tags.load_domains()          `- domain:`        which domains exist (lint validates against it)
    route._domain_areas()        `- areas:`         the routing vocabulary
    coverage.load_tiers_covered() `- tiers-covered:` the Confidence gate's H1 coverage arm
    index.domain_meta()          `- shape:`/`- review-moc:`  the generated per-domain index

This module is the **write** side — the one place that emits a block, and therefore the one place
that has to satisfy all four readers at once. That is a real constraint, not a formality: they
disagree on where a domain's *name* comes from (`coverage` keys off the `### heading`, the other
three off the `- domain:` line), so a block whose heading and `domain:` line differ is a domain lint
accepts and the gate cannot find a coverage tier for. `add()`/`update()` keep them identical by
construction and `list_domains()` reports `header_mismatch` on a hand-edited block that drifted.
`domains_probe.py` asserts the round trip through all four readers, so a change to the emitted shape
that any of them stops parsing fails CI rather than silently producing an invisible domain.

IDENTITY: the domain NAME is not patchable. It is the value of every page's `domain:` frontmatter,
the directory name of the immutable `reference/<domain>/` tier, the stem of the generated
`index.<domain>.md`, and the key the scrape watchlist points at. Renaming it here would leave all of
those addressed under the old name while the taxonomy claims the new one. A rename is remove + add
plus a deliberate pass over the pages — two explicit acts, same rule the scrape watchlist applies to
a source URL.

REMOVAL NEVER DELETES CONTENT. Undeclaring a domain drops the declaration, not the knowledge: the
reference/_sources tiers are immutable ground truth and pages cite them. Withdrawing what a domain
knows is Operation: RETRACT, an explicitly authored act. Removal therefore REFUSES while pages still
carry the domain (unless forced), because the alternative is a vault where lint rejects every one of
those pages with no hint of why.

Writes are atomic (tmp + os.replace) and preserve the file's existing newline style: the API can
edit the taxonomy while `serve` is answering a query out of it, and a torn file would take every
reader down at once.
"""
import argparse
import os
import re
import sys
import tempfile

from wikikb import paths
from wikikb.build import tags

# The emitted field order — the shape ADD-DOMAIN step 2 documents and every reader above expects.
FIELD_ORDER = ("domain", "areas", "shape", "sources", "review-moc", "tiers-covered")
LIST_FIELDS = ("areas", "sources", "tiers-covered")
# Everything except the name. `domain` is absent on purpose: see IDENTITY above.
PATCHABLE = ("areas", "shape", "sources", "review-moc", "tiers-covered")
SHAPES = ("notes-first", "corpus-backed")
# The fixed, deliberately tiny coverage vocabulary (taxonomy.md, ## Domains). Do NOT grow it into an
# ontology — the Confidence gate's H1 arm is only high-precision because the set is coarse.
TIERS = ("conceptual", "support-kb", "scenarios")
MAX_DOMAINS = 200            # bounded like every other API-writable list here

# Two chars minimum, not one: coverage.py matches `^###\s+([a-z][a-z0-9-]+)\s*$` and lint.py matches
# review-moc with the same `+`, so a single-letter domain would be declared, linted, and then
# invisible to the gate. The strictest reader sets the rule.
NAME_RE = re.compile(r"^[a-z][a-z0-9-]+$")
AREA_RE = re.compile(r"^[a-z][a-z0-9-]+$")

_H2 = re.compile(r"^##\s+(.*?)\s*$")
_H3 = re.compile(r"^###\s+(.*?)\s*$")
_FIELD = re.compile(r"^\s*-\s*([a-z][a-z-]*):\s*(.*?)\s*$")

# JSON/CLI spellings that mean the same field. Accepted on input, never emitted.
ALIASES = {"review_moc": "review-moc", "tiers_covered": "tiers-covered", "tiers": "tiers-covered",
           "moc": "review-moc"}


class DomainError(ValueError):
    """Invalid domain operation (bad name, unknown area, still in use, …). Reported to the operator
    as text — 400/404/409 over HTTP, a SystemExit line on the CLI — never handled differently."""


# --- reading -------------------------------------------------------------------------------------

def _read(path=None):
    p = str(path or paths.TAXONOMY)
    if not os.path.isfile(p):
        raise DomainError("no taxonomy at %s — run `python3 -m wikikb bootstrap` first" % p)
    with open(p, encoding="utf-8", newline="") as fh:
        text = fh.read()
    # Preserve the file's own line endings. The vault is edited in Obsidian on Windows as often as
    # by these tools; rewriting a CRLF file as LF would turn a one-field patch into a whole-file diff.
    newline = "\r\n" if "\r\n" in text else "\n"
    return p, text.splitlines(), newline


def _write(p, lines, newline):
    """Atomic replace, byte-exact newline style. tmp lands in the same directory so os.replace is a
    rename, not a cross-device copy."""
    d = os.path.dirname(p) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".taxonomy-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(newline.join(lines) + newline)
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return p


def _section_span(lines, prefix):
    """(start, end) line indices of a `## <prefix>…` section's BODY, or (None, None).

    `end` is the next `## ` heading (exclusive) or EOF — so an insertion at `end` lands inside the
    section, which is what add() needs.
    """
    start = end = None
    for i, line in enumerate(lines):
        m = _H2.match(line)
        if not m:
            continue
        if start is None:
            if m.group(1).strip().lower().startswith(prefix):
                start = i + 1
        else:
            end = i
            break
    if start is None:
        return None, None
    return start, (len(lines) if end is None else end)


def _split_comment(raw):
    """`[a, b]   # why` -> (`[a, b]`, `# why`). No taxonomy field value contains a '#', so the first
    one starts the trailing comment. Comments are PRESERVED across an update: several carry the real
    reason a domain covers only `conceptual`, and silently dropping that on an unrelated patch would
    delete the justification for a gate decision."""
    idx = raw.find("#")
    if idx < 0:
        return raw.strip(), None
    return raw[:idx].strip(), raw[idx:].strip()


def _parse_value(key, s):
    if key in LIST_FIELDS or (s.startswith("[") and s.endswith("]")):
        inner = s.strip()
        if inner.startswith("["):
            inner = inner[1:]
        if inner.endswith("]"):
            inner = inner[:-1]
        return [x.strip() for x in inner.split(",") if x.strip()]
    return s.strip()


def _blocks(lines):
    """The `### <name>` blocks under `## Domains`, in file order.

    Each block records its line span so a later edit is a splice, not a rewrite. An HTML comment
    ENDS the current block and is skipped whole — that is what keeps the inert `<!-- Template -->`
    from parsing as a real domain (its `<domain>` placeholder would fail NAME_RE anyway, but the
    template also must never be picked as the insertion anchor's contents).
    """
    start, end = _section_span(lines, "domains")
    if start is None:
        raise DomainError("taxonomy has no `## Domains` section — repair it with "
                          "`python3 -m wikikb bootstrap`")
    out, cur, in_comment = [], None, False
    for i in range(start, end):
        line = lines[i]
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.lstrip().startswith("<!--"):
            in_comment = "-->" not in line
            if cur is not None:
                cur["end"] = i
                cur = None
            continue
        h = _H3.match(line)
        if h:
            if cur is not None:
                cur["end"] = i
            cur = {"heading": h.group(1).strip(), "start": i, "end": end, "fields": {}}
            out.append(cur)
            continue
        if cur is None:
            continue
        fm = _FIELD.match(line)
        if fm:
            key, raw = fm.group(1), fm.group(2)
            value, comment = _split_comment(raw)
            cur["fields"][key] = {"line": i, "value": _parse_value(key, value), "comment": comment}
    return out, start, end


def _entry(block):
    """A block as a plain JSON-able dict. The NAME comes from `- domain:` when present (three of the
    four readers key off it); a heading that disagrees is reported rather than silently preferred."""
    fields = block["fields"]
    name = (fields.get("domain") or {}).get("value") or block["heading"]
    e = {"domain": name}
    for key in FIELD_ORDER[1:]:
        f = fields.get(key)
        e[key] = f["value"] if f else ([] if key in LIST_FIELDS else None)
        if f and f["comment"]:
            e.setdefault("comments", {})[key] = f["comment"]
    if block["heading"] != name:
        # coverage.py keys tiers-covered off the ### heading while lint/index/route key off
        # `- domain:` — so this block declares one domain the gate can see and another it cannot.
        e["header_mismatch"] = block["heading"]
    return e


def list_domains(path=None):
    """Every declared domain, in file order."""
    _, lines, _ = _read(path)
    blocks, _, _ = _blocks(lines)
    return [_entry(b) for b in blocks if NAME_RE.match(_entry(b)["domain"] or "")]


def get(name, path=None):
    """One domain's declaration, or None."""
    for e in list_domains(path):
        if e["domain"] == name:
            return e
    return None


def known_areas(path=None):
    """The flat `## Areas` union — slug -> description. A domain's `areas:` must be a subset."""
    _, lines, _ = _read(path)
    start, end = _section_span(lines, "areas")
    out = {}
    if start is None:
        return out
    for i in range(start, end):
        m = tags.BACKTICK_RE.search(lines[i])
        if m and lines[i].lstrip().startswith("-"):
            _, _, desc = lines[i].partition("—")
            out[m.group(1)] = desc.strip()
    return out


# --- usage (what a removal would strand) ----------------------------------------------------------

_FM_DOMAIN_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.DOTALL)


def _page_domain(text):
    """The `domain:` of a page's frontmatter — the same tiny top-level-scalar read every module here
    carries locally rather than pulling in a YAML parser."""
    m = _FM_DOMAIN_RE.match(text)
    if not m:
        return None
    for line in m.group(1).splitlines():
        if line.startswith("domain:"):
            return line.partition(":")[2].strip().strip("\"'")
    return None


def usage(name):
    """What currently depends on this domain — the input to the removal refusal, and worth showing
    on a plain GET so an operator sees the blast radius before asking for it."""
    pages = []
    for _, slug, full in tags.page_files():
        try:
            with open(full, encoding="utf-8") as fh:
                if _page_domain(fh.read()) == name:
                    pages.append(slug)
        except OSError:
            continue
    def _count(d):
        return len([f for f in os.listdir(d) if f.endswith(".md")]) if os.path.isdir(d) else 0
    ref = os.path.join(str(paths.REFERENCE), name)
    src = os.path.join(str(paths.WIKI), "_sources", name)
    watched = 0
    try:                                    # lazy: the scrape subpackage is not a build dependency
        from wikikb.scrape import sources as srcmod
        watched = len(srcmod.list_sources(domain=name))
    except Exception:                       # noqa: BLE001 — a corrupt watchlist must not break a GET
        watched = 0
    return {"pages": len(pages), "page_slugs": sorted(pages)[:20],
            "reference_notes": _count(ref), "reference_dir": ref,
            "source_notes": _count(src), "sources_dir": src,
            "scrape_sources": watched,
            "index": os.path.join(str(paths.WIKI), "index.%s.md" % name)}


# --- validation ------------------------------------------------------------------------------------

def _check_name(name):
    if not name or not NAME_RE.match(name):
        raise DomainError("domain name must be kebab-case, 2+ chars, starting with a letter "
                          "(got %r) — it becomes every page's `domain:` and the reference/<domain>/ "
                          "directory name" % (name,))
    return name


def _norm_fields(fields):
    """Accept the JSON/CLI spellings (`review_moc`, `tiers`) and reject anything else by NAME, so a
    typo'd key is an error instead of a silently ignored field."""
    out = {}
    for k, v in fields.items():
        out[ALIASES.get(k, k)] = v
    return out


def _check_list(key, value, allowed=None):
    if isinstance(value, str):
        value = [x.strip() for x in value.split(",") if x.strip()]
    if not isinstance(value, (list, tuple)) or not all(isinstance(x, str) for x in value):
        raise DomainError("%s must be a list of strings" % key)
    value = [x.strip() for x in value if x.strip()]
    if not value:
        raise DomainError("%s must not be empty" % key)
    if allowed:
        bad = [x for x in value if x not in allowed]
        if bad:
            raise DomainError("%s: unknown value(s) %s (allowed: %s)"
                              % (key, ", ".join(bad), ", ".join(allowed)))
    return value


def _check_areas(areas, path, adding=()):
    areas = _check_list("areas", areas)
    bad_shape = [a for a in areas if not AREA_RE.match(a)]
    if bad_shape:
        raise DomainError("areas must be kebab-case tokens: %s" % ", ".join(bad_shape))
    known = set(known_areas(path)) | set(adding)
    missing = [a for a in areas if a not in known]
    if missing:
        # Not auto-created: areas are a FLAT UNION shared by every domain, and each one carries a
        # description the router tokenizes into that domain's profile. An area invented with no
        # description would route nothing and would look identical to a typo of an existing one.
        raise DomainError("area(s) not in the `## Areas` vocabulary: %s — send them in `new_areas` "
                          "with a description, or fix the spelling (known: %s)"
                          % (", ".join(missing), ", ".join(sorted(known)) or "none"))
    return areas


def _norm_new_areas(new_areas):
    """{slug: description} | [{"area":…,"description":…}] | ["slug=description"] -> [(slug, desc)]."""
    if not new_areas:
        return []
    items = []
    if isinstance(new_areas, dict):
        items = list(new_areas.items())
    else:
        for x in new_areas:
            if isinstance(x, dict):
                items.append((x.get("area") or x.get("name"), x.get("description") or x.get("desc")))
            elif isinstance(x, str) and "=" in x:
                k, _, v = x.partition("=")
                items.append((k, v))
            else:
                raise DomainError("new_areas entries look like {\"area\":…,\"description\":…} "
                                  "or \"slug=description\" (got %r)" % (x,))
    out = []
    for slug, desc in items:
        slug = (slug or "").strip()
        desc = (desc or "").strip()
        if not AREA_RE.match(slug):
            raise DomainError("new area %r must be a kebab-case token, 2+ chars" % slug)
        if not desc:
            raise DomainError("new area %r needs a description — the router tokenizes it into this "
                              "domain's keyword profile, so an undescribed area routes nothing" % slug)
        out.append((slug, desc))
    return out


# --- writing ---------------------------------------------------------------------------------------

def _render_field(key, value, comment=None):
    v = "[%s]" % ", ".join(value) if isinstance(value, (list, tuple)) else str(value)
    line = "- %s: %s" % (key, v)
    return line + ("   " + comment if comment else "")


def _render_block(entry):
    out = ["### %s" % entry["domain"]]
    comments = entry.get("comments") or {}
    for key in FIELD_ORDER:
        value = entry["domain"] if key == "domain" else entry.get(key)
        if value in (None, [], ""):
            continue
        out.append(_render_field(key, value, comments.get(key)))
    return out


def _insert_at(lines, start, end):
    """Where a new block goes: at the end of `## Domains`, but BEFORE the trailing `<!-- Template -->`
    comment, so the template stays the last thing in the section where a human expects to find it."""
    anchor = end
    in_comment = False
    for i in range(start, end):
        line = lines[i]
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.lstrip().startswith("<!--"):
            in_comment = "-->" not in line
            anchor = min(anchor, i)
    return anchor


def _append_areas(lines, new_areas, domain):
    """Append `- \\`slug\\` — description` lines to `## Areas`, in the same shape the file already
    uses, tagged with the domain that introduced them (every existing group carries such a marker)."""
    start, end = _section_span(lines, "areas")
    if start is None:
        raise DomainError("taxonomy has no `## Areas` section — repair it with `wikikb bootstrap`")
    at = end
    while at - 1 > start and not lines[at - 1].strip():
        at -= 1
    block = ["<!-- %s areas -->" % domain] + ["- `%s` — %s" % (s, d) for s, d in new_areas]
    return lines[:at] + block + lines[at:], len(new_areas)


def add(name, areas, shape="notes-first", sources=None, review_moc=None, tiers_covered=None,
        new_areas=None, path=None):
    """Declare a new domain. Returns the stored entry.

    Defaults follow the ADD-DOMAIN template rather than inventing anything: `sources:` is the raw
    tier(s) the shape implies, and `review-moc:` is `<domain>-implementation-review` (step 5 of that
    operation names the page you then have to write — the declaration is what makes lint start
    asking for it).

    It creates `vault/_sources/<domain>/` with a README, because that directory is the domain's raw
    tier and the PDF/scrape drop path writes into it; nothing else is created. It writes NO pages
    and NO index: seeding the synthesis is a human/LLM act (ADD DOMAIN step 5) and the indexes are
    `wikikb index`'s output.
    """
    name = _check_name(name)
    if shape not in SHAPES:
        raise DomainError("shape must be one of %s" % ", ".join(SHAPES))
    tiers = _check_list("tiers-covered", tiers_covered or ["conceptual"], allowed=TIERS)
    fresh = _norm_new_areas(new_areas)
    areas = _check_areas(areas, path, adding=[s for s, _ in fresh])

    p, lines, newline = _read(path)
    blocks, start, end = _blocks(lines)
    existing = {(_entry(b)["domain"] or "").lower() for b in blocks}
    if name.lower() in existing:
        raise DomainError("domain already declared: %s (patch it with PATCH /domains/%s)" % (name, name))
    if len(blocks) >= MAX_DOMAINS:
        raise DomainError("taxonomy already declares %d domains" % len(blocks))

    if sources is None:
        sources = (["reference/%s/" % name, "corpora/%s/" % name, "_sources/%s/" % name]
                   if shape == "corpus-backed" else ["_sources/%s/" % name])
    sources = _check_list("sources", sources)
    entry = {"domain": name, "areas": areas, "shape": shape, "sources": sources,
             "review-moc": (review_moc or "%s-implementation-review" % name).strip(),
             "tiers-covered": tiers}

    if fresh:
        # Areas first: the block we are about to write references them, and a crash between the two
        # writes must not leave a domain declaring areas that do not exist.
        lines, _ = _append_areas(lines, fresh, name)
        blocks, start, end = _blocks(lines)

    at = _insert_at(lines, start, end)
    # `block + one blank` is exactly what remove() takes back out (its span runs to the next
    # heading/comment), so add-then-remove leaves the file byte-identical — a probe asserts it.
    lead = [] if at == 0 or not lines[at - 1].strip() else [""]
    lines = lines[:at] + lead + _render_block(entry) + [""] + lines[at:]
    _write(p, lines, newline)

    created = _seed_raw_tier(name)
    entry = dict(entry)
    entry["new_areas"] = [s for s, _ in fresh]
    entry["created"] = created
    entry["file"] = p
    return entry


def _seed_raw_tier(name):
    """Create `vault/_sources/<domain>/` + a README if absent. Create-if-absent only — it never
    touches an existing file, same contract as bootstrap.py."""
    created = []
    d = os.path.join(str(paths.WIKI), "_sources", name)
    try:
        if not os.path.isdir(d):
            os.makedirs(d, exist_ok=True)
            created.append(os.path.relpath(d, str(paths.WIKI)))
        readme = os.path.join(d, "README.md")
        if not os.path.exists(readme):
            with open(readme, "w", encoding="utf-8") as fh:
                fh.write("# %s — raw source tier\n\n"
                         "IMMUTABLE ground truth for the `%s` domain. Hand-authored notes go here "
                         "(cite them as `note:_sources/%s/<file>.md`); harvested PDFs land in "
                         "`_raw/pdfs/` and scraped pages in `_raw/web/`. Never edit a note here to "
                         "fix a synthesis page — fix the page.\n" % (name, name, name))
            created.append(os.path.relpath(readme, str(paths.WIKI)))
    except OSError:
        pass                                 # a read-only vault warns elsewhere; it must not fail the declaration
    return created


def update(name, path=None, **fields):
    """Patch ONE domain in place. Only the fields actually passed are touched.

    Returns (entry, changed) — `changed` is the field names that really moved, so a caller can tell
    "updated" from "you sent what it already had", and a no-op does not rewrite the file (a taxonomy
    that keeps getting new mtimes makes "when did this last actually change?" unanswerable).

    The NAME is not patchable; see IDENTITY in the module docstring.
    """
    fields = _norm_fields(fields)
    new_areas = _norm_new_areas(fields.pop("new_areas", None))
    unknown = sorted(set(fields) - set(PATCHABLE))
    if unknown:
        if {"domain", "name", "new_name", "rename"} & set(unknown):
            raise DomainError(
                "the domain name is its identity and cannot be patched — it is every page's "
                "`domain:`, the reference/%s/ directory, and the index.%s.md stem, so patching it "
                "here would leave all of them addressed under the old name. Remove it and declare "
                "the new one (and repoint the pages) instead." % (name, name))
        raise DomainError("not updatable: %s (allowed: %s, new_areas)"
                          % (", ".join(unknown), ", ".join(PATCHABLE)))
    if not fields and not new_areas:
        raise DomainError("nothing to update — send at least one of: %s" % ", ".join(PATCHABLE))

    if "shape" in fields and fields["shape"] not in SHAPES:
        raise DomainError("shape must be one of %s" % ", ".join(SHAPES))
    if "tiers-covered" in fields:
        fields["tiers-covered"] = _check_list("tiers-covered", fields["tiers-covered"], allowed=TIERS)
    if "sources" in fields:
        fields["sources"] = _check_list("sources", fields["sources"])
    if "review-moc" in fields:
        moc = (fields["review-moc"] or "").strip()
        if not NAME_RE.match(moc):
            raise DomainError("review-moc must be a kebab-case page slug (got %r)" % moc)
        fields["review-moc"] = moc
    if "areas" in fields:
        fields["areas"] = _check_areas(fields["areas"], path, adding=[s for s, _ in new_areas])

    p, lines, newline = _read(path)
    if new_areas:
        known = set(known_areas(path))
        dupes = [s for s, _ in new_areas if s in known]
        if dupes:
            raise DomainError("area(s) already in the vocabulary: %s" % ", ".join(dupes))
        lines, _ = _append_areas(lines, new_areas, name)
    blocks, _, _ = _blocks(lines)
    for b in blocks:
        if _entry(b)["domain"] != name:
            continue
        changed = []
        for key, value in fields.items():
            f = b["fields"].get(key)
            if f and f["value"] == value:
                continue
            changed.append(key)
            new_line = _render_field(key, value, f["comment"] if f else None)
            if f:
                lines[f["line"]] = new_line
            else:
                # Absent field (a hand-written partial block): insert it after the last field so the
                # block keeps FIELD_ORDER instead of growing a tail in patch order.
                last = max((x["line"] for x in b["fields"].values()), default=b["start"])
                lines.insert(last + 1, new_line)
                blocks, _, _ = _blocks(lines)
                for nb in blocks:
                    if _entry(nb)["domain"] == name:
                        b = nb
                        break
        if new_areas:
            changed.append("new_areas")
        if changed:
            _write(p, lines, newline)
        blocks, _, _ = _blocks(lines)
        out = next(_entry(x) for x in blocks if _entry(x)["domain"] == name)
        out["file"] = p
        return out, changed
    raise DomainError("no such domain: %s" % name)


def remove(name, path=None, force=False):
    """Undeclare a domain. Returns the removed entry.

    It deletes the DECLARATION and the generated `index.<domain>.md` (a derived artifact that would
    otherwise sit there describing a domain nothing can validate). It does NOT delete the immutable
    reference/_sources tiers or a single page — that is Operation: RETRACT, an explicitly authored
    act, and doing it as a side effect of a config edit would destroy ground truth over a typo.

    It REFUSES while pages still declare the domain, because the state that produces is worse than
    either alternative: every one of those pages fails lint with "unknown domain" and nothing points
    back at the removal. `force=true` is the operator saying they will repoint the pages themselves.
    """
    p, lines, newline = _read(path)
    blocks, _, _ = _blocks(lines)
    for b in blocks:
        e = _entry(b)
        if e["domain"] != name:
            continue
        use = usage(name)
        if not force and (use["pages"] or use["scrape_sources"]):
            raise DomainError(
                "%s is still in use: %d page(s) declare it%s. Removing it would make every one of "
                "them fail lint as an unknown domain. Repoint or retract them first (CLAUDE.md, "
                "Operation: RETRACT), or pass force=true to remove the declaration anyway."
                % (name, use["pages"],
                   " and %d scrape source(s) target it" % use["scrape_sources"]
                   if use["scrape_sources"] else ""))
        lines = lines[:b["start"]] + lines[b["end"]:]
        _write(p, lines, newline)
        removed_generated = []
        idx = use["index"]
        try:
            if os.path.isfile(idx):
                os.remove(idx)
                removed_generated.append(os.path.relpath(idx, str(paths.WIKI)))
        except OSError:
            pass
        e["file"] = p
        e["usage"] = use
        e["removed_generated"] = removed_generated
        e["kept"] = [x for x in (use["reference_dir"], use["sources_dir"]) if os.path.isdir(x)]
        return e
    raise DomainError("no such domain: %s" % name)


# --- CLI (mirrors the HTTP surface; edits a file, opens no socket, mode-independent) ---------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print the declared domains and exit")
    ap.add_argument("--show", metavar="NAME", help="print one domain's declaration + what uses it")
    ap.add_argument("--add", metavar="NAME", help="declare a new domain (needs --areas)")
    ap.add_argument("--update", metavar="NAME",
                    help="patch a domain — only the flags you also pass change")
    ap.add_argument("--remove", metavar="NAME", help="undeclare a domain (content is KEPT)")
    ap.add_argument("--force", action="store_true",
                    help="with --remove: proceed even while pages still declare the domain")
    ap.add_argument("--areas", help="comma-separated area slugs (must exist in ## Areas)")
    ap.add_argument("--new-area", action="append", default=[], metavar="SLUG=DESCRIPTION",
                    help="add a NEW area to the flat vocabulary first (repeatable)")
    # default=None on every patchable flag: a partial update has to tell "not passed" from "passed",
    # or `--update x --areas a` would silently also reset shape to the argparse default.
    ap.add_argument("--shape", choices=SHAPES, default=None)
    ap.add_argument("--sources", default=None, help="comma-separated raw-tier paths")
    ap.add_argument("--review-moc", dest="review_moc", default=None)
    ap.add_argument("--tiers", default=None,
                    help="comma-separated coverage tiers (%s)" % "|".join(TIERS))
    args = ap.parse_args()

    try:
        if args.list or not any((args.show, args.add, args.update, args.remove)):
            for e in list_domains():
                print("%-18s %-14s tiers=%-24s areas=%s"
                      % (e["domain"], e.get("shape") or "?",
                         ",".join(e.get("tiers-covered") or []) or "?",
                         ",".join(e.get("areas") or [])))
            return
        if args.show:
            e = get(args.show)
            if not e:
                raise SystemExit("domains ▸ no such domain: %s" % args.show)
            for k, v in e.items():
                if k == "comments":
                    for ck, cv in v.items():
                        print("%-16s %s %s" % ("", ck, cv))
                    continue
                print("%-16s %s" % (k + ":", ", ".join(v) if isinstance(v, list) else v))
            u = usage(args.show)
            print("%-16s %d pages, %d reference notes, %d source notes, %d scrape sources"
                  % ("uses:", u["pages"], u["reference_notes"], u["source_notes"], u["scrape_sources"]))
            return
        if args.add:
            if not args.areas:
                raise SystemExit("domains ▸ --add requires --areas")
            e = add(args.add, args.areas, shape=args.shape or "notes-first",
                    sources=args.sources, review_moc=args.review_moc,
                    tiers_covered=args.tiers, new_areas=args.new_area)
            print("declared %s in %s" % (e["domain"], e["file"]))
            for c in e["created"]:
                print("  created %s" % c)
            print("  next: write the overview topic + %s, then `python3 -m wikikb build`"
                  % e["review-moc"])
            return
        if args.update:
            fields = {}
            if args.areas is not None:
                fields["areas"] = args.areas
            if args.shape is not None:
                fields["shape"] = args.shape
            if args.sources is not None:
                fields["sources"] = args.sources
            if args.review_moc is not None:
                fields["review-moc"] = args.review_moc
            if args.tiers is not None:
                fields["tiers-covered"] = args.tiers
            if args.new_area:
                fields["new_areas"] = args.new_area
            e, changed = update(args.update, **fields)
            print("%s: %s" % (e["domain"], ", ".join(changed) if changed
                              else "no change (already held these values)"))
            return
        if args.remove:
            e = remove(args.remove, force=args.force)
            print("undeclared %s" % e["domain"])
            for k in e["kept"]:
                print("  KEPT (immutable) %s" % k)
            for g in e["removed_generated"]:
                print("  removed generated %s" % g)
            print("  next: `python3 -m wikikb build`")
            return
    except DomainError as e:
        raise SystemExit("domains ▸ %s" % e)


if __name__ == "__main__":
    sys.exit(main())
