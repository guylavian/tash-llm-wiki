---
description: Ingest a raw source (kb:<id> | guide:<slug> | ref:<file> | note:<path>) into the wiki
agent: wiki
---

Ingest the following source into the wiki: **$ARGUMENTS**

Follow the `wiki-ingest` skill and "Operation: INGEST" in `wiki/CLAUDE.md` (the
source of truth). Check the manifest first, only do work for new/changed sources,
write/update cross-linked pages under `wiki/` — each stamped with `domain:`,
`summary:` + real `provenance:`. For a corpus-backed domain cite `kb:`/`guide:`/`ref:`;
for a notes-first domain cite `note:_sources/<domain>/…`. Record the source in the
manifest, regenerate the routing indexes (`python3 -m wikikb index`), then lint.

Current delta manifest status:
!`python3 -m wikikb manifest status`

Never edit the immutable `wiki/reference/`, `wiki/_sources/`, or `references/`. Offline only.
