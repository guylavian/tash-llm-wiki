#!/usr/bin/env python3
"""docs_to_corpus.py — turn a tree of Microsoft Learn (DocFX) Markdown into a corpus.

The Windows Server / Active Directory documentation is published as open-source
Markdown in the public GitHub repo `MicrosoftDocs/windowsserverdocs` (AD content
under `WindowsServerDocs/identity/`). This harvester walks such a tree and emits the
exact `corpora/<domain>/index.jsonl` + body files that the existing, proven
`corpus_to_vault.py` consumes — so onboarding a corpus-backed domain from a docs repo
is two stdlib commands and no bespoke fold-in code:

    # 1. docs tree -> corpus  (this script)
    python3 -m wikikb docs_to_corpus \\
        --src wiki/_sources/active-directory/_raw/identity \\
        --domain active-directory --apply

    # 2. corpus -> immutable in-vault reference notes  (existing tool, unchanged)
    python3 -m wikikb corpus_to_vault --domain active-directory --apply

Each `.md` file becomes one record: its DocFX frontmatter `title`/`description`
become the note title/abstract, the body (frontmatter stripped) is the doc body, and
the live learn.microsoft.com URL is derived from the path. `includes/` partials,
`TOC.yml`, and non-Markdown assets are skipped.

stdlib only, no network. Run the GitHub clone on a networked machine, copy the tree
into `_sources/<domain>/_raw/`, then run this offline.
"""
import argparse
import json
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
ROOT = str(paths.ROOT)

# learn.microsoft.com docset base for windowsserverdocs: the repo's `WindowsServerDocs/`
# content folder maps to `/windows-server/`, so a file at `…/identity/ad-ds/foo.md`
# is published at `…/windows-server/identity/ad-ds/foo`.
DEFAULT_URL_BASE = "https://learn.microsoft.com/en-us/windows-server"

SKIP_DIR = {"includes", "media", "images", ".git"}
FM_DELIM = "---"


def parse_frontmatter(text):
    """Return (frontmatter_dict, body_without_frontmatter). Minimal top-level key: value."""
    fm = {}
    body = text
    if text.startswith(FM_DELIM):
        end = text.find("\n" + FM_DELIM, len(FM_DELIM))
        if end != -1:
            block = text[len(FM_DELIM):end]
            body = text[end + len(FM_DELIM) + 1:].lstrip("\n")
            for line in block.splitlines():
                m = re.match(r"^([A-Za-z0-9_.\-]+)\s*:\s*(.*)$", line)
                if m:
                    key = m.group(1).strip()
                    val = m.group(2).strip().strip('"').strip("'")
                    if key not in fm:           # first occurrence wins (skip nested list items)
                        fm[key] = val
    return fm, body


def first_h1(body):
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def derive_url(url_base, src_root, path):
    """learn.microsoft URL from the file path, relative to the PARENT of --src so the
    docset segment (e.g. `identity/…`) is preserved. `index.md` maps to its folder."""
    parent = os.path.dirname(os.path.abspath(src_root.rstrip("/")))
    rel = os.path.relpath(os.path.abspath(path), parent).replace(os.sep, "/")
    rel = re.sub(r"\.md$", "", rel)
    rel = re.sub(r"/index$", "", rel)           # folder landing pages
    rel = re.sub(r"^index$", "", rel)
    return url_base.rstrip("/") + "/" + rel.lstrip("/")


def family_of(src_root, path):
    """Top section under --src (ad-ds, ad-cs, ad-fs, identity, …) → slug family."""
    rel = os.path.relpath(os.path.abspath(path), os.path.abspath(src_root)).replace(os.sep, "/")
    first = rel.split("/", 1)[0]
    return re.sub(r"[^a-z0-9]+", "-", first.lower()).strip("-") or "doc"


def walk_docs(src_root):
    for dirpath, dirnames, filenames in os.walk(src_root):
        dirnames[:] = [d for d in dirnames if d.lower() not in SKIP_DIR]
        for fn in sorted(filenames):
            if fn.lower().endswith(".md"):
                yield os.path.join(dirpath, fn)


def build(src_root, domain, url_base):
    recs, bodies = [], {}
    for path in walk_docs(src_root):
        with open(path, encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        fm, body = parse_frontmatter(raw)
        if not body.strip():
            continue
        title = fm.get("title") or first_h1(body) or os.path.splitext(os.path.basename(path))[0]
        url = derive_url(url_base, src_root, path)
        body_file = "bodies/" + re.sub(r"[^a-z0-9]+", "-",
                                       url.split("//", 1)[-1].lower()).strip("-") + ".md"
        recs.append({
            "title": title,
            "url": url,
            "family": family_of(src_root, path),
            "documentKind": fm.get("ms.topic") or "doc",
            "abstract": fm.get("description") or "",
            "body_status": "fetched",
            "body_file": body_file,
        })
        bodies[body_file] = body
    return recs, bodies


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True,
                    help="path to the cloned docs tree (e.g. .../WindowsServerDocs/identity)")
    ap.add_argument("--domain", required=True)
    ap.add_argument("--url-base", default=DEFAULT_URL_BASE,
                    help=f"learn.microsoft docset base (default: {DEFAULT_URL_BASE})")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    src = args.src
    if not os.path.isdir(src):
        raise SystemExit(f"--src not found: {src}\n"
                         f"(clone MicrosoftDocs/windowsserverdocs and point --src at its "
                         f"WindowsServerDocs/identity folder)")

    recs, bodies = build(src, args.domain, args.url_base)
    outdir = os.path.join(ROOT, "corpora", args.domain)
    rel = os.path.relpath(outdir, ROOT)
    fams = {}
    for r in recs:
        fams[r["family"]] = fams.get(r["family"], 0) + 1

    print(f"domain={args.domain}  src={src}")
    print(f"markdown docs found={len(recs)}")
    print("by family: " + ", ".join(f"{k}={v}" for k, v in sorted(fams.items())))
    print(f"target: {rel}/index.jsonl + {rel}/bodies/*.md")
    if recs:
        print(f"sample url: {recs[0]['url']}")

    if not args.apply:
        print("\n--- DRY RUN (no files written). Re-run with --apply, then "
              "corpus_to_vault.py --domain "
              f"{args.domain} --apply ---")
        return

    os.makedirs(os.path.join(outdir, "bodies"), exist_ok=True)
    for bf, text in bodies.items():
        with open(os.path.join(outdir, bf), "w", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
    with open(os.path.join(outdir, "index.jsonl"), "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"\nWROTE {rel}/index.jsonl ({len(recs)} records) + {len(bodies)} body files")
    print(f"NEXT: python3 -m wikikb corpus_to_vault --domain {args.domain} --apply")


if __name__ == "__main__":
    main()
