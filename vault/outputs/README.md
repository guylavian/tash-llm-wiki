# outputs/ — the derived-artifact tier

Deliverables **compiled from the synthesis layer**: upgrade runbooks, failure-mode cheat
sheets, version-comparison tables, onboarding guides. They are real wiki pages — full
frontmatter, linted, indexed, crosslinked, gated — that happen to be *assembled from*
`topics/` + `entities/` + `questions/` rather than from the raw tier directly.

Why a tier and not a topic page: a runbook is a **presentation** of knowledge, not new
knowledge. Keeping it out of `topics/` stops deliverables from bloating the syntheses
they're built from, and keeping it *in the vault* means the next artifact builds on every
previous one instead of being re-derived in a chat window and lost.

```markdown
---
title: RHBK 26.4 → 26.6 upgrade runbook
type: output                       # index.py groups it, tkg labels it Output
domain: keycloak
slug: rhbk-26-6-upgrade-runbook
summary: Step-by-step upgrade path with the breaking changes and the rollback point.
sources:                           # the SAME contract as every page — no exemption
  - kb:7032207
provenance_extracted: 9
provenance_inferred: 2
provenance_ambiguous: 0
status: draft
updated: 2026-07-24
---
```

**Provenance is not relaxed here.** An artifact assembled from wiki pages still cites the
underlying `kb:`/`guide:`/`ref:` records those pages cite — the Confidence gate's H2
(`extracted == 0`) fires on an output page exactly as it does anywhere else.

Link the pages it was compiled from with ordinary `[[wikilinks]]` in the body — that IS the
"derived from" edge (`LINKS_TO` in the TKG). No separate `derived_from:` field.
