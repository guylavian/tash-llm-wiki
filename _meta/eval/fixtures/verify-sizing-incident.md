---
title: FIXTURE — the 2026-07-05 sizing incident (wrong cached number)
type: question
domain: keycloak
slug: verify-sizing-incident-fixture
summary: "Regression fixture for wikikb verify: reproduces the cached page text that carried 120 client-credentials/s per vCPU against a source (RHBK 26.0 sizing) that says 200. verify MUST flag the 120 claim as MISMATCH."
sources:
  - kb:rhbk-26-0-concepts-memory-and-cpu-sizing
provenance:
  extracted: 3
  inferred: 0
  ambiguous: 0
status: draft
updated: 2026-07-05
---

# Fixture — sizing incident

2. **CPU sizing model** — ~1 vCPU per 15 password logins/s, per 120 client credentials/s, per 120 refresh tokens/s, plus 150% headroom.
