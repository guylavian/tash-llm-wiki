# Overnight autonomous session — 2026-07-12 → 13

## STATUS (FINAL — session closed 2026-07-14 by user handoff-to-PR)
- **DONE:** N1 premise layer (c606dd6 — extraction+table+post-gate+langgraph-schema fix+text_of
  reasoning_content fallback; Codex ACCEPT after 1 reject cycle; live Gemma evidence both
  outcomes) · N3-scope bank v4 frozen (c8f0b32) · bank v3 frozen (b6db012, pre-contract).
- **PARTIAL:** examiner-gate Phase 0 — transcripts dumped (_meta/eval/transcripts-20260712/,
  model-attributed), mandated checks done: S8 announce-time = EXAMINER-ERROR (real syntax at
  cisco-ospf-ospf-stub-router-advertisement.md:130,147,150,261 → C3 dropped), S9 restricted-v3 =
  gold-was-wrong, real content (nodes-4-22-nodes-pods-user-namespaces.md:53,61;
  authentication-4-22-managing-security-context-constraints.md:200,209 → C5 positive control),
  S4 2^30 corpus-grounded (ad-ds-managing-rid-issuance.md:73). Full-table extraction agent
  STALLED at the grep phase (transcripts read, sweep unfinished) — restart needed.
- **NOT DONE:** N2 verbatim-gate scope fix, v5 bank build (Phase 1), Phase 2 contamination sweep,
  Phase 3 grading integration, N4 design doc, N5 answer_source, N6 crosslink invest, N7
  References-decision writeup, morning report.
- **Handoff:** user requested commit-all + PR (2026-07-14). Everything below this STATUS block is
  the append-only event log as written during the night.

## STATUS (live — superseded)
- **Currently executing:** N1 — finish premise layer (integration evidence + Codex adversarial review)
- **Queue:** FROZEN 23:04 — N1 premise finish (M, C→X) · N2 verbatim-gate scope (M, X→C) ·
  N3 bank v4 two classes (S, X→C... impl X, review C) · N4 contract design doc + thin scaffold
  (M, C→X) · N5 answer_source (S, C→X) · N6 crosslink investigation (S, X→C) ·
  N7 References-decision writeup (S, X drafts, no code) · PARKED: D-2 ablations
- **Blockers:** none
- **Detached runs:** none (both 2026-07-12 cohorts completed and committed at fd039fd)
- **Eval lock:** no eval running; no vault builds planned
- **Git remote:** team/overnight-20260712 (push after every commit; never team/main)
- **Codex thread:** 019f57e0-2b4e-71f3-86fa-15f3917b8ab3 (old threads dead)

---

## [22:46] Session start — contract received mid-flight; inherited state captured
**what:** Overnight contract activated while the premise-correction-dropout task (user-issued
~22:00) was ~80% executed. Inherited in-flight state, verbatim:
- IMPLEMENTED (uncommitted, UNREVIEWED): `lint.extract_premises` + `lint.premise_gate`
  (_meta/wikikb/quality/lint.py), injected premise-table prompt + post-gate wiring
  (_meta/wikikb/graph/nodes.py), `premise_flags` in public_result + strict-withhold on
  premise_unaddressed (_meta/wikikb/graph/ask.py), selftest check 47d (_meta/tests/selftest.py),
  grade300 `premise_corrected` report-only column (_meta/eval/grade300.py).
- COMMITTED: bank v3 frozen pre-run, own commit **b6db012** (25 cases: v2's 20 byte-carried +
  sub-021 RID session-#4 incident + 4 synthetic premise traps; 5/5 planted premises verified
  extractable BEFORE freeze — D8 clean).
- VERIFICATION so far: selftest 70/78 — premise check 47d PASS; the 8 FAILs are pre-existing
  (other session's uncommitted vault content: 4 golden cost-proxy shifts from modified index files,
  lint/index/crosslink drift from untracked cohort question pages). D5 PROOF RUN: `wikikb evaluate`
  output byte-identical with vs without the premise diff (git-stash A/B) — my diff is
  golden-neutral; goldens NOT regenerated.
- IN FLIGHT: integration run (b) — session-#4 RID question through real `ask` on Gemma-4-12b
  via LM Studio (PID 18131, started 22:42, expect ~3-6 min at CPU speeds). Negative control (c)
  not yet run. Codex review of Parts 1+3 NOT yet done (adversarial mandate pending).
**why:** contract rule 3 — nothing lands on self-review; the premise work becomes queue item #1.
**files touched:** none this entry (log creation only).
**next:** git-remote check; collect Gemma result; ULTRATHINK night plan; open Codex.

## [22:52] Remote push channel established
`git push team master:refs/heads/overnight-20260712` → new branch created. All overnight commits
push there (never to team/main). Log survivability satisfied.

## [22:55] Phase I — Claude's independent night plan (ULTRATHINK, pre-Codex, anti-anchoring)
Ordering rationale: (value × confidence) / risk, local-first, S/M only. The premise layer is
nearly done and unreviewed — finishing it is the cheapest high-value item and unblocks the bank
classes that grade against it. The verbatim-gate scope fix is the sharpest small item: filed
questions/ pages currently count as existence evidence in corpus-grounding scans, so a filed
fabrication could self-license later answers — a circularity that gets worse every night the
wiki amortizes. Architecture (section-type contract) is deliberately mid-queue: it needs the
ULTRATHINK design slot, but refactoring the premise code the same night it was written is churn
risk — so the night delivers the DESIGN + scaffold, and the premise-table refactor into type #1
is explicitly parked for daylight.
- N1 (M, Claude impl → Codex review): FINISH premise layer — Gemma integration (b) + negative
  control (c), Codex adversarial review of Parts 1+3 (mandate: adversarial phrasings, negated
  premises, Hebrew-mixed, split-across-sentences; safe-degradation ruling), single commit
  (lint+nodes+ask+selftest+grade300). Acceptance: selftest premise check PASS + D5 A/B proof.
- N2 (S, Claude impl → Codex review): verbatim-gate scope fix — questions/ (and synthesis tiers)
  excluded as existence evidence in identifier/citation grounding scans. Acceptance: a token
  present ONLY in a questions/ page is flagged as non-existent (new selftest case).
- N3 (S, Codex impl → Claude review): bank v4 frozen — 2 remaining manual-session classes
  (fabricated-provenance-of-absence, cache-hit-unlabeled), D8, extractability/gradability
  verified pre-freeze. Acceptance: grade300 smoke on synthetic answers.
- N4 (M, ULTRATHINK design; Claude authors → Codex review): structured answer contract DESIGN
  DOC + minimal section-type registry scaffold (no premise refactor tonight). Acceptance:
  doc + scaffold imports clean; premise gate untouched byte-wise.
- N5 (S, Codex impl → Claude review): answer_source in public_result (filed-page vs
  fresh-retrieval vs extractive-fallback). Acceptance: selftest asserts tag on both paths.
- N6 (S, investigation): crosslink guide: tokens, 17 pages — findings logged; fixes only if S.
- N7 (report item): References-enforcement decision (D-ii) — argued for morning report.
- PARKED-BY-DEFAULT: D-2 ablation arms (quota unknown; lock conflicts with N1-N5 writes).
**next:** Codex blind plan request.

## [23:10] N3 DONE — bank v4 frozen (c8f0b32, pushed)
**what:** Codex implemented cases-substitution.v4.jsonl (supersedes v3, 25 byte-carried) +
GRADING-substitution.v4.md: sub-026/027 Class A fabricated-provenance-of-absence
(permission_resource_format IS documented — doc-7053211:35-37 verified by BOTH sides
independently), sub-028/029 Class B cache-hit-unlabeled (grading: pending-answer_source →
UNGRADED until N5, never vacuous pass). **Review:** 1 REJECT cycle (sub-027 was meta-phrased —
"can a model safely answer…" — rephrased to a direct user question), then ACCEPT with cited
checks (byte-carry programmatic compare, fact re-verified, labels, JSONL parse). Freeze commit
contains bank+grading note only (D8). **commit:** c8f0b32, pushed to team/overnight-20260712.
**next:** back to N1.

## [23:22] N1 integration evidence — CAUGHT A REAL CROSS-CUTTING BUG (this is why (b) exists)
**what:** Reran (b) RID + (c) control through real `ask` on Gemma-4-12b (LM Studio gateway,
gate=local-ok, PONG probe verified live first).
- (c) CONTROL: Gemma answered live; cited zero sources → WI-6 grounding_fail correctly WITHHELD
  the prose (machinery works). BUT `public_result` showed `grounding_fail: false,
  premise_flags: []` while the answer TEXT carried the withheld banner → **the langgraph
  StateGraph drops every state key not declared in WikiState** (query_graph.py TypedDict):
  grounding_fail, ungrounded_identifiers, grounding_basis, truncated_ids (WI-9!),
  premise_flags, premises, judge_verdict — all silently vanish on the langgraph path. Linear
  path (plain python3 — today's cohorts, serve/mcp/livebank offline) is UNAFFECTED; only
  .venv-online/langgraph surfaces lose the structured fields.
- (b) RID: gateway returned None (extractive fallback) on both chain attempts while the control
  succeeded — transient LM Studio model churn suspected; will retry after the schema fix.
**why:** integration testing on the REAL orchestrator; the linear-path selftests could never
catch a langgraph-only drop.
**files touched:** _meta/wikikb/graph/query_graph.py (WikiState + 7 declared keys + comment
making the invariant explicit).
**verification:** rerun (b)+(c) next; selftest full rerun before commit.
**next:** rerun (b) on fixed schema; then Codex review of N1 (Parts 1+3 + this fix).

## [23:04] Phase I closed — queue FROZEN (one debate round, 3/3 disputes conceded by Codex)
**what:** Codex (new thread 019f57e0…, prior threads dead) produced its blind queue: ~80%
congruent with mine. Dispute ledger:
- **D-a** structured-contract depth (Codex: implement skeleton tonight / me: design doc + thin
  registry scaffold + ONE wrapper hook, premise refactor parked for daylight) → **CONCEDED to me**;
  Codex added a boundary note: scaffold stays thin enough that it cannot become an implicit
  answer-generation rewrite. Accepted.
- **D-b** verbatim-gate position (me: #2 / Codex: #4) → **CONCEDED to me** (position 2); I accepted
  Codex's sizing (M) and its self-assignment as implementer.
- **D-c** References enforcement (Codex: implement / me: decision-writeup only — D-ii is the
  operator's carried-over call, morning-report material) → **CONCEDED to me**, zero code tonight.
Frozen queue as in STATUS. Codex's refused-list (no bank edits post-freeze, no big refactors, no
touching the other session's vault drift unless it breaks an acceptance test, no evals on an
unstable tree, no generalized truth-verification engine) adopted as night guardrails verbatim.
**next:** N1 execution — collect Gemma integration evidence, run negative control, then Codex
adversarial review of Parts 1+3.

## [22:46] Deviation note (loggable per contract)
The bank-v3 freeze commit (b6db012) and all premise implementation happened BEFORE this contract
arrived — they were the direct execution of the user's immediately-preceding task message. Logged
as inherited, not as post-freeze scope. The overnight backlog's "substitution bank v3: today's 3
manual-session cases" is PARTIALLY covered (premise-dropout ✓ as sub-021); the other two classes
(fabricated-provenance-of-absence, cache-hit-unlabeled) are NOT yet cases → queue candidates.
