#!/usr/bin/env python3
"""Delta manifest for the Keycloak/RHBK LLM Wiki — stdlib only, no network.

The manifest (`wiki/_meta/.manifest.json`) records every *ingested* source: the
sources cited by wiki pages, a content hash (for sources that map to a single
file), timestamps, and which wiki pages each source produced. INGEST consults it
so it only does work for new or changed sources instead of re-reading the corpus.

Source tiers and how they are tracked (see wiki/CLAUDE.md):
  - ref:<file>     content-hashed against ../references/<file>   (change-detected)
  - kb:<id>        presence-tracked only (kb ids are loose: solution numbers or
                   symbolic slugs that don't map 1:1 to a body file)  hash=null
  - guide:<slug>   presence-tracked only (a guide spans many records) hash=null
  - web:<url ...>  presence-tracked only (external/upstream)          hash=null

This script reads ../references/ READ-ONLY for hashing and never writes outside
wiki/_meta/. It never touches ../references/ or the in-vault reference/ tier.

Adapted from the delta-manifest idea in the obsidian-wiki framework
(github.com/Ar9av/obsidian-wiki), reworked for this skill's immutable two-tier
corpus and fs retriever.

Usage:
    python3 -m wikikb manifest seed              # (re)build from current pages
    python3 -m wikikb manifest status            # ingested-vs-pending + delta
    python3 -m wikikb manifest record ref:server-configuration.md --pages a,b
    # all commands accept --date YYYY-MM-DD (defaults to today)
"""
import argparse
import datetime
import hashlib
import json
import os
import re

from wikikb import paths
from wikikb.build.tags import load_domains
from wikikb.corpus.pdf_to_corpus import slugify
META = str(paths.META)
WIKI = str(paths.WIKI)
ROOT = str(paths.ROOT)
REFERENCES = str(paths.REFERENCES)
MANIFEST = str(paths.MANIFEST)
CORPORA = str(paths.CORPORA)

PAGE_DIRS = paths.PAGE_DIRS
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
# a source token: "- kb:7032207", "- ref:foo.md", "- web:https://... (label)"
SRC_RE = re.compile(r"^\s*-\s*((?:kb|guide|ref|web):\S+)")


def today(args):
    return getattr(args, "date", None) or datetime.date.today().isoformat()


def iter_pages():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield fn[:-3], os.path.join(full, fn)


def page_sources(text):
    m = FM_RE.match(text)
    if not m:
        return []
    out = []
    in_sources = False
    for line in m.group(1).splitlines():
        if re.match(r"^sources:\s*$", line):
            in_sources = True
            continue
        if in_sources:
            sm = SRC_RE.match(line)
            if sm:
                out.append(sm.group(1))
            elif not line.startswith((" ", "\t", "-")):
                in_sources = False  # left the sources: block
    return out


def hash_source(tok):
    """Content hash for file-backed sources; None for presence-tracked tiers."""
    if tok.startswith("ref:"):
        path = os.path.join(REFERENCES, tok[len("ref:"):])
        if os.path.isfile(path):
            with open(path, "rb") as fh:
                return "sha256:" + hashlib.sha256(fh.read()).hexdigest()[:16]
        return "MISSING"
    return None  # kb: / guide: / web: are presence-tracked


def collect():
    """source token -> set of page slugs that cite it (from the live wiki)."""
    cited = {}
    for slug, path in iter_pages():
        with open(path, encoding="utf-8") as fh:
            for tok in page_sources(fh.read()):
                cited.setdefault(tok, set()).add(slug)
    return cited


def load():
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as fh:
            return json.load(fh)
    return {"generated": None, "sources": {}}


def save(man):
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=2, sort_keys=True)
        fh.write("\n")


def cmd_seed(args):
    cited = collect()
    day = today(args)
    man = load()
    src = man.get("sources", {})
    for tok, pages in cited.items():
        entry = src.get(tok, {})
        entry.setdefault("first_ingested", day)
        entry["last_seen"] = day
        entry["hash"] = hash_source(tok)
        entry["pages"] = sorted(pages)
        src[tok] = entry
    man["sources"] = src
    man["generated"] = day
    save(man)
    print("Seeded manifest: %d sources across %d pages -> %s"
          % (len(src), len({p for ps in cited.values() for p in ps}),
             os.path.relpath(MANIFEST, ROOT)))


def cmd_record(args):
    day = today(args)
    man = load()
    src = man.setdefault("sources", {})
    tok = args.source
    pages = [p.strip() for p in (args.pages or "").split(",") if p.strip()]
    entry = src.get(tok, {})
    entry.setdefault("first_ingested", day)
    entry["last_seen"] = day
    entry["hash"] = hash_source(tok)
    entry["pages"] = sorted(set(entry.get("pages", [])) | set(pages))
    src[tok] = entry
    man["generated"] = day
    save(man)
    print("Recorded %s -> pages: %s" % (tok, ", ".join(entry["pages"]) or "(none)"))


def pending_raw_pdfs():
    """domain -> sorted list of PDF/txt stems dropped in `_sources/<domain>/_raw/pdfs/`
    that pdf_to_corpus.py hasn't harvested yet (their slugified stem isn't the URL tail
    of any record in `corpora/<domain>/index.jsonl`). Pure read, no new state — reuses
    the domain list from taxonomy.md and pdf_to_corpus's own slugify() so "pending"
    means exactly what pdf_to_corpus would produce."""
    pending = {}
    for domain in sorted(load_domains()):
        pdf_dir = os.path.join(WIKI, "_sources", domain, "_raw", "pdfs")
        if not os.path.isdir(pdf_dir):
            continue
        stems = sorted({os.path.splitext(fn)[0] for fn in os.listdir(pdf_dir)
                        if fn.lower().endswith((".pdf", ".txt"))})
        if not stems:
            continue
        idx = os.path.join(CORPORA, domain, "index.jsonl")
        harvested_tails = set()
        if os.path.isfile(idx):
            with open(idx, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        harvested_tails.add(json.loads(line)["url"].rsplit("/", 1)[-1])
        missing = [s for s in stems
                  if not any(t == slugify(s) or t.startswith(slugify(s) + "-p")
                             for t in harvested_tails)]
        if missing:
            pending[domain] = missing
    return pending


def status_lines():
    """Report lines for the audit; reused by lint.py --status."""
    man = load()
    recorded = man.get("sources", {})
    cited = collect()
    lines = []

    # tier counts
    tiers = {"kb": 0, "guide": 0, "ref": 0, "web": 0}
    for tok in cited:
        tiers[tok.split(":", 1)[0]] += 1
    lines.append("Manifest: %d sources recorded (generated %s)"
                 % (len(recorded), man.get("generated") or "never — run `manifest.py seed`"))
    lines.append("Cited in wiki now: kb=%d guide=%d ref=%d web=%d"
                 % (tiers["kb"], tiers["guide"], tiers["ref"], tiers["web"]))

    # new: cited but not yet recorded
    new = sorted(set(cited) - set(recorded))
    # gone: recorded but no longer cited
    gone = sorted(set(recorded) - set(cited))
    # changed: ref sources whose current hash != recorded hash
    changed = []
    for tok, entry in recorded.items():
        h = hash_source(tok)
        if h is not None and entry.get("hash") is not None and h != entry["hash"]:
            changed.append(tok)

    # pending references: reference files never ingested
    pending_refs = []
    if os.path.isdir(REFERENCES):
        all_refs = {"ref:" + fn for fn in os.listdir(REFERENCES) if fn.endswith(".md")}
        pending_refs = sorted(all_refs - set(cited))

    def block(label, items):
        if items:
            lines.append("  %s (%d): %s" % (label, len(items), ", ".join(items)))

    block("NEW (cited, not recorded)", new)
    block("CHANGED (ref hash drift)", sorted(changed))
    block("GONE (recorded, no longer cited)", gone)
    block("PENDING references (never ingested)", pending_refs)
    for domain, stems in pending_raw_pdfs().items():
        lines.append("  PENDING PDFs (%s) (%d): %s — next: python3 -m wikikb pdf_to_corpus "
                     "--src _sources/%s/_raw/pdfs --domain %s --apply"
                     % (domain, len(stems), ", ".join(stems), domain, domain))
    lines.append("Note: kb:/guide:/web: are presence-tracked (hash=null); "
                 "ref: change-detection is content-hashed. kb corpus is ~1,840 "
                 "records — 'pending' is tracked for references only.")
    return lines


def cmd_status(args):
    for ln in status_lines():
        print(ln)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("seed", cmd_seed), ("status", cmd_status)):
        p = sub.add_parser(name)
        p.add_argument("--date")
        p.set_defaults(fn=fn)
    pr = sub.add_parser("record")
    pr.add_argument("source")
    pr.add_argument("--pages", default="")
    pr.add_argument("--date")
    pr.set_defaults(fn=cmd_record)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
