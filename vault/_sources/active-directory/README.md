# `_sources/active-directory/` — raw notes (the immutable ground truth)

Active Directory is a **notes-first** domain: there is no harvested Red Hat-style
corpus. The Markdown notes in this folder **are** the raw tier — the ground truth
the `active-directory` synthesis pages are built on. Treat them like the immutable
`reference/<domain>/` notes for a corpus-backed domain:

- **One file per source/topic cluster.** Name it for the concept
  (`fsmo-roles.md`, `replication-topology.md`, `kerberos-auth.md`).
- **Cite it from synthesis pages** with `note:_sources/active-directory/<file>.md`
  in the page's `sources:` block (path is relative to `wiki/`).
- **Excluded from the content scanners.** `lint.py` / `index.py` / `crosslink.py`
  scan only `topics/ entities/ questions/`; files here are never linted or counted
  as pages — same discipline as `_sources/` for the upstream `web:` tier.
- **Provenance, not transcripts.** Record where each fact comes from (official
  Microsoft Learn URL + fetch date, a lab observation, a ticket). When you lift a
  fact from Microsoft docs, also carry the `web:` URL into the synthesis page.

Grow via the wiki **INGEST** op in `../../CLAUDE.md`; onboard the domain itself via
**Operation: ADD DOMAIN** (worked example: `../../_meta/ADD-DOMAIN.md`).
