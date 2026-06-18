---
description: Audit the wiki — delta manifest (ingested-vs-pending), hubs, orphans, stale
agent: wiki
---

Report the wiki status across all domains: the delta manifest (ingested-vs-pending
sources, new/changed/gone, pending references), link hubs, orphans, stale routing
indexes, and per-domain context-budget warnings. See the `wiki-status` skill and
"Operation: STATUS" in `wiki/CLAUDE.md`.

Audit output:
!`python3 wiki/_meta/bin/lint.py --status`

Reads `references/` read-only; writes only `wiki/_meta/.manifest.json`.
