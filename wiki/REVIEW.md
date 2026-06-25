# Project Review — Keycloak/RHBK LLM Wiki

**Reviewed:** 2026-06-25 · **Scope:** `wiki/` vault + `_meta/wikikb/` toolchain (35 py files, ~5,700 LOC)
**Method:** read `CLAUDE.md`/`AGENTS.md`, ran the project's own `lint`, `selftest`, `evaluate`, and `index --check`; inspected git state.

---

## Verdict

A genuinely well-architected, self-documenting knowledge system — the design is the strong part, and it holds up under its own tooling. **The code is healthy; the content artifacts were out of date.** Every fixable failure was regeneration drift from the just-added `cisco-ios-xe` domain (HEAD commit `5e32a00`), not a toolchain defect — **regenerated in this pass (35/42 → 40/42).** The two remaining reds are documented intentional fixtures and must stay red.

| Signal | Result |
|---|---|
| `selftest.py` | **40/42 pass** (was 35/42 before regen) — the 2 remaining reds are *documented intentional fixtures*, not failures |
| `lint` | 251 pages, **2 errors** (both the intentional ISSU gate fixture), 154 warnings |
| Toolchain logic tests (gate, tkg, graph, llm, dispatcher) | **all pass** — core is sound |
| Architecture & docs | excellent (see Strengths) |

> **42/42 is not the target — 40/42 is.** `selftest.py` (lines 127–133) documents its own baseline: two permanent reds — `lint --strict` (the deliberately-unfixed ISSU gate fixture) and `crosslink` (~20 gated Red-Hat solution ids with no offline reference note). The bar is "no NEW failures vs that baseline." Both are *features* of the design, not debt.

---

## Strengths

1. **The schema is the source of truth, and it's enforced.** `CLAUDE.md` isn't aspirational prose — the 5-arm Confidence gate, the provenance contract, and the immutable-raw-tier rule are all *checked by `lint.py` and asserted by `selftest.py`*. Docs that can't drift from code are rare. The `.skills/` and `.opencode/` packages are deliberately thin pointers back to `CLAUDE.md` — the right call against duplication.

2. **Layering is disciplined.** Raw (`reference/`, `_sources/`) immutable · synthesis (`topics/entities/questions/`) LLM-maintained · `_meta/` tooling excluded from scanners. The "writes go only under the synthesis layer" rule is load-bearing and respected.

3. **Air-gapped, stdlib-only, no install.** `python3 -m wikikb <tool>` runs anywhere; the optional online tier (LiteLLM/LangGraph) and dense/TKG backends are all lazy-imported behind flags with graceful degradation — `selftest` actively asserts no module-scope third-party import leaks in. This is the correct way to keep an offline tool offline.

4. **Retrieval is measured, not asserted.** `evaluate.py` prints real recall (lexical → +graph → +closure: 47%→63%→74% @10) and a context-token proxy. A wiki that benchmarks its own retrieval and commits goldens is doing more than most production RAG.

---

## Findings

### 🟢 The 2 lint "errors" are a DELIBERATE fixture — do NOT fix

- **`questions/c9500-issu-svl-blackhole-nsf-gr.md`** trips gate arms **H2** (`extracted==0`) + **H3** (`reviewed` & `inferred≥extracted`) — *by design*. `CLAUDE.md` ("let the page be its first catch"), `selftest.py:116` (`_BASELINE_GATE`, "documented deliberate non-fix"), and the BF-10 probe all **require** this page to stay flagged: it's the Confidence gate's own living test case. "Fixing" it (ingesting a source or setting `draft`) would break `selftest` check #11 and erase the fixture. **Correct action: leave it.** *(My first-pass review wrongly called this a defect — corrected here after reading the test harness.)*

### 🟠 Stale generated artifacts (5 of the 7 fails) — regeneration drift, now FIXED

The `cisco-ios-xe` brain was added in the HEAD commit; the derived artifacts weren't rebuilt after. All idempotent regenerations — **done in this pass**:

| Failing check | Cause | Action taken | Now |
|---|---|---|---|
| `index --check up to date` | `index.keycloak.md` stale | `wikikb index` (rebuilt 3 domain indexes) | ✅ pass |
| `eval … byte-identical` (×4) | index grew 23 tokens (12,977→13,000); goldens stale | re-recorded `eval/baseline.eval*.out` | ✅ pass |
| `lint --strict` missing `tags:` | 8 question pages untagged | `wikikb tags backfill --apply` | tags added (lint still reds on the ISSU fixture — *expected*) |
| `crosslink 0 unresolved kb:` | ~20 **gated** Red-Hat solution ids with no offline note | `wikikb crosslink --apply` (185 edges written) | ✅ edges applied; **the ~20 gated ids are unresolvable by design** → check stays red (documented baseline) |

> The eval drift was *cosmetic* — recall numbers unchanged; only the context-token proxy moved 23 tokens because the routing index gained a domain. Goldens re-recorded → green.

### 🟡 Warnings (155) — expected backlog, mostly intentional

- **~30 `provenance: needs-review`** — legacy pages migrated before the per-claim provenance rule. The system *correctly* refuses to fabricate counts; these are honest TODOs, not errors.
- **Tags not in taxonomy** (`deploy`, `logical-design`, `virtualization`, `how-to`, …) — the AD/Cisco domains introduced tags never registered in `_meta/taxonomy.md`. Either add them to the controlled vocab or drop them.
- **27 wanted pages** — intentional `[[slug]]` TODO markers (`bgp-route-dampening`, `ospf-nssa`, …). Working as designed.
- **`[[slug]]` literal link** referenced by 4 pages — a copy-paste of the frontmatter *template's* placeholder leaked into 4 real pages' bodies. Minor: grep `\[\[slug\]\]` and fix.

### Observations (not defects)

- **Cross-domain link** `cross-site-split-brain-pac-signing` (AD) → `active-passive-failover-sessions-lost` (keycloak) — flagged by lint as cross-domain; legitimate, just noting the graph now spans domains.
- **Retrieval gap is known and documented.** Paraphrase queries collapse (dpop exact @7 → paraphrase @118). `CLAUDE.md` already names the fix (the optional dense/embedding layer) and `--hybrid` degrades gracefully when it's absent. Honest about its own ceiling.

---

## Recommendations

**Done in this pass (35/42 → 40/42):**
```bash
cd wiki/_meta
python3 -m wikikb index                          # ✅ rebuilt 3 domain indexes
python3 -m wikikb crosslink --apply              # ✅ wrote 185 wiki→KB edges
python3 -m wikikb tags backfill --apply          # ✅ tagged 8 pages
python3 -m wikikb evaluate        > eval/baseline.eval.out        # ✅ re-recorded
python3 -m wikikb evaluate --route > eval/baseline.eval.route.out # ✅
python3 -m wikikb evaluate --graph > eval/baseline.eval.graph.out # ✅
python3 tests/selftest.py                        # → 40/42 (2 intentional fixtures)
```
> NOT done, on purpose: the `c9500-issu` page (gate fixture — fixing it breaks BF-10)
> and the ~20 gated solution-id crosslinks (no offline note exists). These are the
> documented baseline, not debt.

**Worth doing (future):**
1. **Add a `rebuild` verb** (or `make` target) chaining index + crosslink + tags + re-record. This drift recurs every time a domain is added; one command makes regen a pre-commit reflex instead of a forgotten step. *(ponytail: automate the regen, don't loosen the test.)*
2. **Register AD/Cisco tags in `taxonomy.md`** (`deploy`, `logical-design`, `virtualization`, `how-to`, …) to clear the tag-vocab warnings — or decide those domains don't tag yet. 16 entity pages also remain untagged (backfill only heuristically tags questions/topics).
3. **Drain `provenance: needs-review`** (~30 legacy pages) opportunistically — the one backlog that weakens the Confidence gate's guarantees the longer it sits.

**Don't:**
- Don't relax `selftest`/`lint --strict` to chase 42/42 — the two reds are the product working. Fix artifacts, never the gate or its fixtures.

---

## Bottom line

Architecture **A**, code health **A−**, content freshness **A** (after this pass). Nothing here was rotten — a well-built system caught mid-stride right after a domain was added, its own tooling loudly and correctly reporting exactly what was stale. The regen is done: `selftest` is at its documented-clean **40/42**, the two reds are intentional fixtures. The only genuine backlog is provenance hygiene (`needs-review` pages + untagged entities), which the tooling already tracks.
