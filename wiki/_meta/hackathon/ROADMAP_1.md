# ROADMAP 1 — Cycle 1: fix the answer path, prove it with a real deploy

Date: 2026-07-04 (overnight hackathon). Architect: Fable 5. Team: wiki-implementer (sonnet),
sre-validator (sonnet), adversarial-reviewer (haiku), researcher (sonnet) — `.claude/agents/`.

## Mission bar
An SRE agent consuming ONLY this wiki must correctly perform real operational tasks.
Flagship: deploy + configure Keycloak (RHBK) end-to-end with a verified auth flow, using Docker
Desktop locally, every domain fact sourced from the wiki.

## Baseline (measured, 2026-07-04, post-Phase-0)
- Retrieval: lexical r@5 48% / r@10 59% (17/29); +graph 90%; +closure 93%. Paraphrase ranks:
  dpop@118, kerberos-delegation@88, openshift-scc@298, ospf@76, token-exchange@10.
- Precision failure: openshift "crashloopbackoff image pull" → 1,274 hits, top-5 irrelevant (raw TF, no IDF).
- Trust chain: `used` = all retrieved candidates (citation never verified); gate hole — `reviewed` page
  with NO provenance keys passes silently; 2 AD scenario questions lack the mandatory H1 banner.
- Content: 23 lint warnings; 114 auto-seeded summaries; index.keycloak.md ~11k tokens (oversize).
- Tests: selftest 50/50; 29 recall + 19 faithfulness cases; no numeric CI threshold; heldout unused.
- Scenario success rate: NO BASELINE (never measured) — cycle 1 establishes it.

## Cycle-1 items (dispatched)
| # | Item | Why (impact on agent task success) | Executor |
|---|------|-----------------------------------|----------|
| A | BM25/IDF scorer + alias expansion + MRR/precision@5 + `--min-recall` CI gate | Multi-term precision + paraphrase recall are the top confirmed retrieval defects; the CI gate makes regressions fail loud | wiki-implementer (brief A) |
| B | Parse real `[cite:]` from answers; `used` = cited∩candidates; grounding-fail banner; gate fires H2 on missing provenance; `question_tier:` + H1 lint enforcement + backfill | The provenance story is the system's differentiator vs RAG and it is currently fake at the LLM seam; gate holes = silent bad answers | wiki-implementer (brief B) |
| C | `wikikb serve` — stdlib JSON API (/health /route /search /ask /page /expand), loopback default | The "production agent consumes the wiki" path must be real, not a CLI convention; stdlib keeps the air-gap contract | wiki-implementer (brief C) |
| R1-R3 | Research: Graphiti/Zep/Letta; BM25F/RRF/RAGAS params; LangGraph-vs-alternatives + MCP serving | Definition-of-done requires written tool verdicts; cycle-2 bets chosen from evidence | researcher ×3 |

## Validation plan (after A-C integrate)
1. **Flagship (sre-validator):** deploy Keycloak via Docker using only wiki guidance: run container,
   create realm + OIDC client, create user, obtain a token (password or auth-code flow), verify it,
   exercise one hardening step (e.g. brute-force detection). PASS = working token flow with zero
   unsourced domain facts. Every gap → structured defect.
2. **AD scenario (paper):** delegate a password-reset over an OU + diagnose a Kerberos clock-skew
   auth failure — wiki-only walkthrough, defects logged.
3. **IOS-XE scenario (paper):** mixed-speed port-channel misbehavior + OSPF adjacency stuck — via the
   implementation-review MOC symptom tables.
4. **Adversarial sweeps (adversarial-reviewer ×3):** keycloak hubs+questions; AD MOC; IOS-XE MOC.

## Metrics to move this cycle
- Paraphrase ranks: ≥3 of 5 materially better (target median <30).
- Live precision sanity on the crashloop query.
- Gate: H2 fires on missing provenance (probe-verified); 0 unbannered out-of-coverage questions.
- Scenario baseline established: flagship verdict + defect count by severity.

## Bold bets deferred to Cycle 2 (pending research)
- MCP server surface for the wiki (if R3 supports it) — the native agent-consumption standard.
- Brain/worker/judge role map in llm.py + judge node in the QUERY graph (needs online tier verified
  on this box).
- tkg: keep/delete Kuzu backend per R1 verdict.
