---
name: wiki-ingest
description: Fold a raw source (a kb:<id>/guide/ref for a corpus-backed domain, a hand-authored note:_sources/<domain>/*.md for a notes-first domain, or a query result) into the LLM-maintained wiki/ — creating or updating cross-linked, domain-stamped topic/entity pages without duplicating the immutable corpus. Use when asked to ingest, capture, or "write up" a source into the wiki.
---

# wiki-ingest

This skill packages the **INGEST** operation. Its behavior is defined in one place
— **`wiki/CLAUDE.md`** (the schema and single source of truth). This file is a thin
pointer so the runtime can discover the op; do not duplicate the rules here.

## Do this
1. **Read `wiki/CLAUDE.md` first** — follow "Operation: INGEST" exactly.
2. Check the delta manifest so you only process new/changed sources:
   `python3 -m wikikb manifest status`
3. Extract durable facts → create/update `wiki/entities/*.md` and place synthesis
   in `wiki/topics/*.md`; cross-link with `[[slug]]`.
4. Every page needs: `domain:` (validated against taxonomy), `summary:`, `sources:`
   provenance, a `provenance:` block with real per-claim counts
   (`extracted`/`inferred`/`ambiguous` — never mechanical), `status:`, `updated:`.
   Tag `(inferred)`/`(ambiguous)` claims inline.
5. Record what you ingested, then regenerate the routing indexes:
   `python3 -m wikikb manifest record <source> --pages <slug,...>` then
   `python3 -m wikikb index` (refreshes `index.<domain>.md` + the `index.md` router).
6. Lint: `python3 -m wikikb lint`

## Hard rule
Edits go **only** to the synthesis layer (`wiki/{topics,entities,questions}/`). Never
edit the immutable raw tiers `wiki/reference/` / `wiki/_sources/` or `references/` —
they are ground truth. No network, no `webfetch`, stdlib only.
