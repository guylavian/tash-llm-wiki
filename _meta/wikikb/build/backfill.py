#!/usr/bin/env python3
"""One-time, deterministic, idempotent backfill for pre-framework wiki pages.

Adds only what can be derived honestly, without inventing facts:
  - summary:  lifted verbatim from the page's own bold one-line definition
              (the `**...**` line). lint.py flags these as "auto-seeded" so a
              human can later replace them with a real summary.
  - provenance: needs-review   — a HONEST placeholder. Per-claim provenance can
              only be assigned by reading each claim against its source, so we do
              NOT manufacture extracted/inferred counts here. Real provenance goes
              forward at INGEST write-time and on hand-authored pages.

  - domain:   stamped from --domain (default keycloak) on any page missing it,
              inserted right after type: per the frontmatter spec. Pages already
              carrying domain: are left untouched.

Tags are intentionally NOT backfilled — they belong to Pass 2 (taxonomy).

Pages that already have a summary:/provenance:/domain: are left untouched (idempotent).
Only edits files under wiki/{topics,entities,questions}/ — never corpora/ or references/.

Usage:
    python3 -m wikikb backfill            # dry-run: list what would change
    python3 -m wikikb backfill --apply    # write the changes
"""
import argparse
import os
import re

from wikikb import paths
WIKI = str(paths.WIKI)
PAGE_DIRS = ("topics", "entities", "questions")
FM_RE = re.compile(r"^(---\n)(.*?)(\n---)", re.DOTALL)


def page_files():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield os.path.join(full, fn)


def bold_definition(body):
    """The page's leading bold one-line definition (`**...**`), even if it wraps
    across lines. Whitespace is collapsed; a trailing period is dropped so the
    value is stable for the lint auto-seeded comparison."""
    b = re.sub(r"^\s*#.*\n", "", body.lstrip(), count=1).lstrip()
    if not b.startswith("**"):
        return None
    m = re.match(r"\*\*(.+?)\*\*", b, re.DOTALL)
    if not m:
        return None
    return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")


def yaml_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def backfill(text, domain="keycloak"):
    """Return (new_text, actions) or (text, []) if nothing to do."""
    m = FM_RE.match(text)
    if not m:
        return text, []
    block = m.group(2)
    lines = block.splitlines()
    has_summary = any(re.match(r"^summary:\s*\S", ln) for ln in lines)
    has_prov = any(re.match(r"^provenance:\s*", ln) for ln in lines)
    has_domain = any(re.match(r"^domain:\s*\S", ln) for ln in lines)
    actions = []

    if not has_domain:
        # insert domain: right after type: (or title:) — matches the frontmatter spec order
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("type:")), -1)
        if idx == -1:
            idx = next((i for i, ln in enumerate(lines) if ln.startswith("title:")), -1)
        lines.insert(idx + 1, "domain: " + domain)
        actions.append("domain")

    if not has_summary:
        body = text[m.end():]
        bd = bold_definition(body)
        if bd:
            # insert summary right after the slug: line (or at top of block)
            idx = next((i for i, ln in enumerate(lines) if ln.startswith("slug:")), -1)
            lines.insert(idx + 1, "summary: " + yaml_quote(bd))
            actions.append("summary")

    if not has_prov:
        # insert provenance just before status: (or at end of block)
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("status:")), len(lines))
        lines.insert(idx, "provenance: needs-review")
        actions.append("provenance")

    if not actions:
        return text, []
    new_block = "\n".join(lines)
    return text[:m.start()] + m.group(1) + new_block + m.group(3) + text[m.end():], actions


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--domain", default="keycloak",
                    help="domain to stamp on pages missing `domain:` (default keycloak)")
    args = ap.parse_args()

    changed = 0
    for path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        new, actions = backfill(text, domain=args.domain)
        if actions:
            changed += 1
            rel = os.path.relpath(path, WIKI)
            print(f"{'WROTE' if args.apply else 'would change'} {rel}: +{', +'.join(actions)}")
            if args.apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    print(f"\n{changed} pages {'updated' if args.apply else 'pending'} "
          f"({'apply' if args.apply else 'dry-run'})")


if __name__ == "__main__":
    main()
