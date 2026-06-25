---
name: wiki-lint
description: Health-check the RHBK/Keycloak wiki/ — broken/wanted links, orphans, missing summary/sources/provenance, provenance drift, auto-seeded summaries, link hubs, and stale pages. Use after a batch ingest or before shipping wiki changes.
---

# wiki-lint

Packages the **LINT** operation. Behavior is defined in **`wiki/CLAUDE.md`**
("Operation: LINT"); this is a thin pointer.

## Do this
```bash
python3 -m wikikb lint            # health check (stdlib, no network)
python3 -m wikikb lint --strict   # exit 1 on any error (broken link / no sources)
python3 -m wikikb index           # regenerate routing indexes if lint reports them stale
```
Then resolve what it reports: write wanted pages, link orphans, fill stubs, replace
auto-seeded summaries with real ones, assign real provenance to `needs-review`
pages, add a missing/undeclared `domain:`, regenerate stale `index.<domain>.md`,
reconcile contradictions.

Only `wiki/{topics,entities,questions}/` are scanned; `wiki/_meta/` and the
generated `index*.md` are tooling/output, not pages. Edits go only to `wiki/`.
