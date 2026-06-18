---
name: wiki-status
description: Audit the RHBK/Keycloak wiki/ — the delta manifest (ingested-vs-pending sources, new/changed/gone, pending references), plus link hubs, orphans, and stale pages. Use to see what is left to ingest and the overall health of the wiki.
---

# wiki-status

Packages the **STATUS / audit** operation. Behavior is defined in
**`wiki/CLAUDE.md`** ("Operation: STATUS"); this is a thin pointer. It reuses the
lint scanners and the delta manifest rather than duplicating them.

## Do this
```bash
python3 wiki/_meta/bin/lint.py --status     # lint report + delta-manifest audit
python3 wiki/_meta/bin/manifest.py status   # just the delta-manifest audit
python3 wiki/_meta/bin/manifest.py seed     # rebuild the manifest from current pages
```
`ref:` sources are content-hashed (real change detection); `kb:`/`guide:`/`note:`/`web:`
are presence-tracked. Reads `references/` read-only; writes only
`wiki/_meta/.manifest.json`. Never touches the immutable `wiki/reference/`,
`wiki/_sources/`, or `references/`.
