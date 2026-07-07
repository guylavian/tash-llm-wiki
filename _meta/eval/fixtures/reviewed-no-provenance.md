---
title: "Synthetic gate-hole fixture — reviewed page, zero provenance keys"
type: entity
domain: keycloak
slug: reviewed-no-provenance-fixture
summary: Not a real content page. Exists only for gate_page_probe.py, to prove the GATE (not just the softer "missing provenance" lint warning) fires H2 when a page's frontmatter carries NO provenance keys at all (neither flat provenance_extracted/inferred/ambiguous nor a nested provenance: block) while self-tagging status: reviewed.
sources:
  - kb:none
status: reviewed
updated: 2026-07-04
---

# Synthetic gate-hole fixture

**This page intentionally has no `provenance:` block and no `provenance_extracted` /
`provenance_inferred` / `provenance_ambiguous` keys, while self-tagging `status: reviewed`.
Per CLAUDE.md's Confidence-gate contract ("extracted = provenance_extracted (0 if absent)"),
fully-missing provenance IS extracted==0 — H2 must fire, and `status: reviewed` must NOT
suppress it. It lives under `_meta/eval/fixtures/` (tooling, excluded from the content
scanners) purely so `gate_page_probe.py` has a real file to read.**
