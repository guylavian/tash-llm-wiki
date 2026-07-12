# Eval checkpoint report — model invariants & graph contribution (v1, pre-ablation)

**Status: interim publication draft.** Both cohorts are PARTIAL; the causal ablation arms
(Phase D) have not run — every causal cell below is explicitly labeled. Nothing in this
report is tuned against the bank (frozen at `cbcf843c…`, restored in `a216aae`).

Vault commit at cohort creation: `bcfaa84` (dirty) — **caveat: this was never the state any
case actually saw** (live-tree snapshots + mid-run mutation at 14:09:10 local; see caveats).
Graders: `raw-v1` = grade300.py@`136f886^` · `C-5` = grade300.py@`136f886` (post-results
metric correction, Codex-ruled, dual-reported by mandate). Bank: `edb6936^` (pinned,
hash-matches both cohort manifests).

## T1 — MODEL INVARIANTS (per cohort, pinned bank, dual-graded)

| | DeepSeek v4-flash-free | LFM2.5-1.2B (local) | Qwen (planned) |
|---|---|---|---|
| Cohort | `20260712T101300Z-41879c9c`, PARTIAL 111/300 (paused: provider congestion) | `20260712T110010Z-5791e7f5`, PARTIAL 109/300 (closed by operator) | pending |
| **INVARIANTS** | | | |
| fabrication-passed (C-5) | **0/30** | **0/28** | pending |
| fabrication-passed (raw-v1) | 0/30 | 5/28 — all adjudicated grader artifacts: fab-022/029/030 refusal-regex false negatives, fab-013/026 gold-token-overlap false credits | pending |
| ungrounded-served | 0 observed — **BLOCKED-ENV**: LLM gateway down all day, every `wikikb ask` served the extractive fallback; deterministic guard/banner gates were active but the measurement surface (banner-parse of served synthesis) never exercised | same | pending |
| wrong-in-confident | ≤9 (answered-wrong, no gate marker; 10 judge-flags open) | ≤80 (83 judge-flags open) | pending |
| **VARIABLES** | | | |
| gold mean (fab / lexical) | 0.93 / 0.76 | 0.14 / 0.16 | pending |
| withhold/refusal (fab, C-5) | 30/30 | 9/28 (raw-v1: 5/28) | pending |
| coverage (answered/300) | 111 (37%) | 109 (36%) | pending |
| protocol-failure rate (bucket c) | 7/111 (3 workspace-integrity from the 14:09–15:09 live-vault churn + 4 provider double-timeouts lex-kc-042..045) | 3/109 | pending |
| buckets a/b/c | 63 / 32 / 7 (+9 answered-failed-ungated) | 17 / 9 / 3 (+80 answered-failed-ungated) | pending |

**Reading the invariant line:** the small-model stress test behaved as designed — LFM2.5
contributed ~nothing (gold ≈0.15) and fabricated freely (fluent, documentation-styled,
wrong), yet **zero fabrications passed** under the refusal-gated metric on either grader
once C-5 removed two token-overlap false credits. DeepSeek held the invariant clean on both
graders.

### Inline honesty caveats (binding on any citation of T1)
1. **v1 cohorts ran bare-prompt** — the References contract was never delivered to the
   examinee; contract column is **VOID** ("protocol not delivered"), and the 59 DS
   pass-no-evidence cases are "evidence-trail unmeasured", not upgraded, not discounted.
2. **Vault mutated mid-cohorts at 14:09:10 local** (crosslink `--apply`, 168 keycloak pages,
   Sources-block link edges only, zero gold-fact surface): DS split at case #57, LFM at #4.
   Aggregate keycloak metrics mix two retrieval configurations; DS-vs-LFM on keycloak
   fab-004..018 is confounded (DS pre, LFM post).
3. **Cross-cohort amortization contamination**: examinee wikikb-MCP reads hit the live vault
   (recorded in manifests as `mcp_vault_source: live-vault` from run300/2 onward); later
   cases could see earlier cohorts' filed pages. DS fab-001 visibly cache-hit its own smoke
   page.
4. **C-5 is a post-results metric correction** (defined 2026-07-12 after inspecting
   partials) — tainted for confirmatory claims; hence dual reporting. Prospective for
   future cohorts.
5. **DS congestion window**: lex-kc-042..045 are environment failures (provider), kept in
   bucket (c), never counted against gates or model competence.
6. LFM ran at 32,768-token context (reloaded from a 4,096 default that would have truncated
   the harness); peak observed usage ≈17k/call.

## T2 — GRAPH CONTRIBUTION

| Measure | Value | Status |
|---|---|---|
| Pass rate with vs without expand, per domain (causal) | — | **BLOCKED-ENV**: the two v2 ablation arms (DeepSeek, `--no-expand` first, clean committed tree, per consensus protocol) have not run — provider quota exhausted tonight |
| Offline retrieval-recall corroboration (committed, `baseline.eval.graph.out:6-8`) | lexical recall@10 20/29 (69%) → graph seed-source 26/29 (90%) → 1-hop closure 27/29 (93%) | measured, **retrieval-recall only** — not answer pass rate, not causal |
| "13%/34% citation-trace analysis" | **not found in the repository** (full sweep incl. git history); omitted pending provenance | — |
| Reconstructed graph-linked citation share (defined 2026-07-12) | — | computed at D-2 from the with-expand arm's answers vs crosslink Sources blocks; a citation-match metric, not strict causal dependence |
| Cost: build time | not instrumented | never inferred from unrelated timestamps |
| Cost: expand context-token proxy | 6/29 eval cases rescued in-proxy (`baseline.eval.graph.out:30-37`) | committed measurement |
| Cost: expand latency delta | — | measured live during the D arms |

**D-2 protocol (consensus):** both arms fresh under run300/2 (same prompt hash, same bank,
same clean commit, isolation probe green — verified 2026-07-12), `--no-expand` first or
randomized-and-recorded, opencode session DB snapshotted between arms, no concurrent
probes on the provider quota, symmetric RUN-ERROR exclusion, "inconclusive" declared
rather than post-hoc corrected if congestion differs; analysis against the `9b06e6e` tree
with per-case boundary annotation.

---
Artifacts: `report300-<cohort>.{c5,rawv1}.json` (this directory) · consensus ledger in the
Codex thread `019f56fe-c992-7a13-b972-98bdb2b2cee9` (rounds 1–2 closed) · commits
`a216aae`·`24410bb`·`0f9ec41`·`263fcda`·`7fdb7ef`·`136f886`.
