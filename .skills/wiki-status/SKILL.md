---
name: wiki-status
description: Audit the multi-domain wiki/ (all domains in wiki/_meta/taxonomy.md) — the delta manifest (ingested-vs-pending sources, new/changed/gone, pending references), plus link hubs, orphans, and stale pages. Use to see what is left to ingest and the overall health of the wiki.
---

# wiki-status

Packages the **STATUS / audit** operation. Behavior is defined in
**`wiki/CLAUDE.md`** ("Operation: STATUS"); this is a thin pointer. It reuses the
lint scanners and the delta manifest rather than duplicating them.

## Do this
```bash
python3 -m wikikb lint --status     # lint report + delta-manifest audit
python3 -m wikikb manifest status   # just the delta-manifest audit
python3 -m wikikb manifest seed     # rebuild the manifest from current pages
```
`ref:` sources are content-hashed (real change detection); `kb:`/`guide:`/`note:`/`web:`
are presence-tracked. Reads `references/` read-only; writes only
`wiki/_meta/.manifest.json`. Never touches the immutable `wiki/reference/`,
`wiki/_sources/`, or `references/`.
