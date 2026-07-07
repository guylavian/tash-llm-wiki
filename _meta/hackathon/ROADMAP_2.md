# ROADMAP 2 — Cycle 2: close validation defects, ship the agent-native surface, prove two clean rounds

Date: 2026-07-05 (overnight, cycle 2). Input: validation round 1 (flagship PARTIAL + AD PARTIAL +
XE PARTIAL, 19 defects total) + research verdicts (WORKLOG).

## What round 1 proved
- The pipeline works end-to-end: a wiki-only agent deployed Keycloak, got a verified token, proved a
  hardening control. Page discipline held (H1 banners fired where written; validators always knew
  synthesis from ground truth).
- The failure class is consistent across all 3 domains: **conceptual coverage strong, operational
  keys/commands thin** (REST attribute keys, w32tm, dsacls, mtu-ignore, verification steps), plus one
  systemic gate hole (untiered ask silently skipped H1 — fixed, see below).

## Cycle-2 items
| # | Item | Status |
|---|------|--------|
| E | Flagship defects D1-D5 → keycloak content (web-verified `web:` citations) | in flight |
| G | AD defects → w32tm re-grounding (BLOCKER), verify/rollback subsections, Kerberos-policy contradiction | in flight |
| H | XE defects → EtherChannel consistency rule, command re-grounding, MOC row split | in flight |
| F | Gate honesty: untiered ask on partially-covered domain now emits "coverage gate not evaluated" (architect, DONE — verified, 55/55) | done |
| I | **Bold bet: MCP stdio server** (`wikikb/mcp/`, pure stdlib JSON-RPC; tools: ask/search/route/read_page) — per R3 verdict; makes the wiki natively consumable by MCP hosts incl. Claude Code | next |
| J | Judge tier (`model_judge` third group in llm.py, advisory-only annotation, never the gate) + **delete tkg/graphiti_backend.py** (Kuzu archived upstream; R1 verdict + deletion-architect + judges) | next |
| V2 | Validation round 2: adversarial sweeps ×3 (never completed in round 1 — infra), flagship re-run spot-check on fixed pages, AD/XE re-checks of the specific defect fixes | after E/G/H |

## Exit criteria for the night
- Round 2: zero blocker/major defects on the re-checked paths; sweeps report only P3s or clean.
- If round 2 finds significant defects → fix → round 3. Two consecutive significant-defect-free
  rounds required before PRODUCTION_READINESS.md.
- selftest green (55+ checks), lint 0 errors, all goldens honest.

## Explicitly deferred (documented, not forgotten)
- Authorization-code-flow browser validation (needs headless browser; wiki-only rule makes login-form
  knowledge unavailable — revisit with a scripted flow page in the wiki).
- Dense-layer eval integration (--hybrid recall line in evaluate.py) and openshift-scc paraphrase miss.
- index.keycloak.md oversize (~11k tokens) — split or trim summaries.
- 114 auto-seeded summaries; alias: frontmatter enrichment (only dpop has aliases today).
- Ollama llm.config.yaml stale api_base note → operator doc.
