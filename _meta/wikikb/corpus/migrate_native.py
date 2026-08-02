#!/usr/bin/env python3
"""migrate_native.py — ONE-TIME migration toward native Obsidian. stdlib only.

Two frontmatter transforms on every wiki/{topics,entities,questions} page:

  1. Flatten the nested `provenance:` map to flat scalar keys
     (`provenance_extracted` / `provenance_inferred` / `provenance_ambiguous`)
     so Obsidian's Properties UI and Bases can read them — nested YAML maps are
     second-class in both.

  2. Add a `source_notes:` LIST-OF-LINKS property resolving each `kb:` token in
     `sources:` to its reference note. These are the SAME targets crosslink.py
     writes into the generated `## Sources` body block — but now as native
     frontmatter links that feed Obsidian's graph + backlinks with NO generator.

It REUSES crosslink.py's resolver, so `source_notes:` is provably identical to
the `## Sources` targets (verify with --check). The generated `## Sources` block
is left UNTOUCHED so you can confirm the native edges match before retiring
crosslink.py. Idempotent — safe to re-run.

This script is transitional: run it once (then it can be deleted). The end state
has *less* Python, not more.

Usage:
    python3 -m wikikb migrate_native            # dry-run summary
    python3 -m wikikb migrate_native --check    # verify source_notes == ## Sources
    python3 -m wikikb migrate_native --apply    # write
"""
import argparse
import os
import re
import sys

from wikikb import paths
sys.dont_write_bytecode = True
from wikikb.build import crosslink  # reuse build_ref_index / source_tokens / resolve / top_fields

WIKI = crosslink.WIKI
PAGE_DIRS = paths.PAGE_DIRS
FM_RE = crosslink.FM_RE


def resolved_slugs(block, domain, idx):
    """The reference-note slugs a page's kb: tokens resolve to (crosslink's logic)."""
    seen = []
    for tok in crosslink.source_tokens(block):
        r = crosslink.resolve(tok, domain, idx)
        if r and r["slug"] not in seen:
            seen.append(r["slug"])
    return seen


def transform(block, domain, idx):
    """Return (new_frontmatter_block, slugs). Flattens provenance, refreshes source_notes."""
    slugs = resolved_slugs(block, domain, idx)
    lines = block.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^source_notes:\s*$", line):            # strip existing block (idempotent)
            i += 1
            while i < len(lines) and re.match(r"^\s+-\s", lines[i]):
                i += 1
            continue
        if re.match(r"^provenance:\s*$", line):              # flatten the nested map
            i += 1
            counts = []
            while i < len(lines):
                cm = re.match(r"^\s+(extracted|inferred|ambiguous):\s*(\d+)\s*$", lines[i])
                if not cm:
                    break
                counts.append((cm.group(1), cm.group(2)))
                i += 1
            out += [f"provenance_{k}: {v}" for k, v in counts]
            continue
        out.append(line)
        i += 1
    if slugs:                                                # insert source_notes after the sources block
        at = None
        for j, ln in enumerate(out):
            if re.match(r"^sources:\s*$", ln):
                k = j + 1
                while k < len(out) and re.match(r"^\s+-\s", out[k]):
                    k += 1
                at = k
                break
        blk = ["source_notes:"] + [f'  - "[[{s}]]"' for s in slugs]
        if at is None:
            out += blk
        else:
            out[at:at] = blk
    return "\n".join(out), slugs


def existing_sources_links(text):
    """Slugs crosslink wrote into the generated ## Sources block (for --check)."""
    m = re.search(r"## Sources\n<!-- crosslink:begin.*?-->\n(.*?)\n<!-- crosslink:end -->",
                  text, re.DOTALL)
    if not m:
        return []
    return re.findall(r"\[\[([a-z0-9][a-z0-9-]*)(?:\|[^\]]*)?\]\]", m.group(1))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="verify source_notes == the generated ## Sources targets")
    args = ap.parse_args()

    idx = crosslink.build_ref_index()
    n_pages = n_flat = n_links = n_edges = mismatches = 0
    sample = None
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            path = os.path.join(full, fn)
            text = open(path, encoding="utf-8").read()
            m = FM_RE.match(text)
            if not m:
                continue
            block = m.group(1)
            domain = crosslink.top_fields(block).get("domain")
            new_block, slugs = transform(block, domain, idx)
            if re.search(r"^provenance:\s*$", block, re.MULTILINE):
                n_flat += 1
            if slugs:
                n_links += 1
                n_edges += len(slugs)
            if args.check and slugs:
                old = existing_sources_links(text)
                if sorted(set(slugs)) != sorted(set(old)):
                    mismatches += 1
                    print(f"  MISMATCH {fn[:-3]}: source_notes={slugs} vs ##Sources={old}")
            new_text = "---\n" + new_block + "\n---" + text[m.end():]
            if new_text != text:
                n_pages += 1
                if sample is None and slugs:
                    sample = (fn[:-3], slugs)
                if args.apply:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(new_text)

    verb = "WROTE" if args.apply else "DRY RUN"
    print(f"{verb} — {n_pages} pages changed; {n_flat} provenance maps flattened; "
          f"{n_links} pages got source_notes ({n_edges} native graph edges)")
    if args.check:
        ok = "OK — native source_notes == generated ## Sources" if not mismatches \
             else f"{mismatches} mismatch(es) — investigate above (stale ## Sources?)"
        print(f"check: {ok}")
    if sample:
        print(f"sample — {sample[0]}.md  source_notes: {sample[1]}")
    if not args.apply:
        print("re-run with --apply to write.")


if __name__ == "__main__":
    main()
