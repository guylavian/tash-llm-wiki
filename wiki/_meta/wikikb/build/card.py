"""card.py — generate QUERY-CARD.md: the ~1.5k-token per-query protocol card (F4, 100k-budget plan).

An agentic QUERY session was paying a fixed ~24k-token protocol tax (CLAUDE.md 12.4k + the domain
index 11.4k) before reading any evidence. The card replaces the per-query CLAUDE.md read: it is the
`## Operation: QUERY` section MECHANICALLY sliced out of CLAUDE.md (never hand-copied — a hand copy
drifts the first time the Confidence gate changes), prefixed with the budget directives (F2/F5).
Full CLAUDE.md stays the schema of record, read for INGEST/ADD-DOMAIN/edit operations only.

    python3 -m wikikb card            # regenerate wiki/QUERY-CARD.md
    python3 -m wikikb card --check    # exit 1 if stale vs CLAUDE.md (lint calls this)
"""
import argparse
import hashlib
import re
import sys

sys.dont_write_bytecode = True
from wikikb import paths

CLAUDE = paths.WIKI / "CLAUDE.md"
CARD = paths.WIKI / "QUERY-CARD.md"

HEADER = """\
# QUERY protocol card (generated — edit CLAUDE.md, then `python3 -m wikikb card`)

**Budget directives (read first):**
- Retrieval is served in bounded slices (pages ≤ ~2k tokens/call; `next_offset` pages more).
- Watch `session_tokens_served` on every tool result: past the stop-line the result carries a
  `budget_directive` — obey it: STOP retrieving, answer from evidence already read.
- Search-first: `route` then `search`/`expand` snippets. Read `index.<domain>.md` ONLY when the
  router abstains; never read the global index on a confident route.
- Do NOT read CLAUDE.md for a QUERY — this card is the extracted QUERY contract. Read CLAUDE.md
  only for INGEST / ADD-DOMAIN / page-editing operations.

---
"""


def query_section():
    text = CLAUDE.read_text(encoding="utf-8")
    m = re.search(r"^## Operation: QUERY\n.*?(?=^## Operation: |^---$)", text, re.M | re.S)
    if not m:
        raise SystemExit("CLAUDE.md: '## Operation: QUERY' section not found")
    return m.group(0).rstrip() + "\n"


def digest(section):
    return hashlib.sha256(section.encode("utf-8")).hexdigest()[:16]


def render():
    section = query_section()
    return "%s%s\n<!-- source-digest: %s -->\n" % (HEADER, section, digest(section))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="exit 1 if the card is stale vs CLAUDE.md")
    args = ap.parse_args()
    want = render()
    if args.check:
        have = CARD.read_text(encoding="utf-8") if CARD.exists() else ""
        if have != want:
            print("QUERY-CARD.md is STALE (or missing) — run: python3 -m wikikb card")
            raise SystemExit(1)
        print("QUERY-CARD.md up to date")
        return
    CARD.write_text(want, encoding="utf-8")
    print("wrote %s (%d chars ~%d tok)" % (CARD, len(want), len(want) // 4))


if __name__ == "__main__":
    main()
