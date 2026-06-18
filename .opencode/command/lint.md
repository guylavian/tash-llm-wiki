---
description: Health-check the wiki (broken links, orphans, provenance, stale, hubs)
agent: wiki
---

Health-check the wiki and resolve what it reports (write wanted pages, link
orphans, replace auto-seeded summaries, assign real provenance to `needs-review`
pages, add a missing `domain:`, regenerate stale routing indexes with
`python3 wiki/_meta/bin/index.py`). See the `wiki-lint` skill and "Operation: LINT"
in `wiki/CLAUDE.md`.

Lint output:
!`python3 wiki/_meta/bin/lint.py`

Edits go only to the synthesis layer. Never edit `wiki/reference/`, `wiki/_sources/`, or `references/`.
