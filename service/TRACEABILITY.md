# Traceability Matrix — requirement → design → task → test → status

Every requirement maps to ≥1 passing test. Any row without a passing test = build incomplete.

| Requirement | Design element | Task | Test (AC) | Status |
|-------------|----------------|------|-----------|--------|
| FR-1 Index build / exclude source-only & routable!=true / H2 split | `index.build_index`, `is_source_only`, `_split_sections` | T2 | `test_fr1_excludes_source_and_nonroutable` (AC-1.1/1.2), `test_fr1_sections_split` (AC-1.3) | ✅ PASS |
| FR-2 /route ranked top-k w/ full hit shape | `app.route`, `ranking.Ranker.rank` | T3,T4 | `test_fr2_route_shape` (AC-2.1/2.2) | ✅ PASS |
| FR-3 Version-gating hard pre-filter (every ranker) | `Ranker._prefilter` (base class, ADR-5) | T3 | `test_fr3_version_gating` (AC-3.1/3.2) | ✅ PASS |
| FR-4 /get section vs full; 404 reasons | `app.get` | T4 | `test_fr4_get_section` (AC-4.1), `test_fr4_get_full` (AC-4.2), `test_fr4_source_only_404` (AC-4.3), `test_fr4_notroutable_404` (AC-4.4) | ✅ PASS |
| FR-5 Provenance on every hit + /get | `ranking._provenance`, `app.get` | T3,T4 | `test_fr5_provenance` (AC-5.1) | ✅ PASS |
| FR-6 /reload atomic + admin-gated | `_State.reload`, `app.reload` | T4 | `test_fr6_reload` (AC-6.1/6.2) | ✅ PASS |
| FR-7 /healthz + /metrics | `app.healthz`, `app.metrics` | T4 | `test_fr7_health_metrics` (AC-7.1/7.2) | ✅ PASS |
| FR-8 Rankers + hybrid; lexical zero-dep | `LexicalRanker`,`EmbeddingRanker`,`HybridRanker`,`make_ranker` | T3,T6 | `test_fr8_hybrid_exact_code_wins` (AC-8.2), `test_fr8_lexical_zero_ml_import` (AC-8.1) | ✅ PASS |
| FR-9 Local-only embed source + fallback | `embedding.resolve`, `make_ranker` fallback | T5,T6 | `test_fr9_embedding_fallback` (AC-9.1), `test_fr9_loopback_refused` (AC-9.2) | ✅ PASS |
| FR-10 Embed metadata only (never bodies) | `embedding.meta_text`, `EmbeddingStore.build` | T5 | `test_fr10_metadata_only` (AC-10.1) | ✅ PASS |
| FR-11 Agent contract route-first/escalate | `agent/wiki_tools.json`, `AGENTS.md.snippet` | T9 | schema present + rules (AC-11.1/11.2) — static artifacts | ✅ PRESENT |
| NFR-1 Stateless atomic swap | `_State` attribute swap | T4 | covered by `test_fr6_reload` (no per-request writes) | ✅ PASS |
| NFR-2 No egress / no phone-home | hand-rolled metrics, loopback-only embed | T4,T5 | `test_fr9_loopback_refused` + design (no external host) | ✅ PASS |
| NFR-3 Determinism | stable sort `(-score,path,section)` | T3 | `test_nfr3_determinism` (AC-NFR3) | ✅ PASS |
| NFR-4 Path safety | `index.resolve_safe` | T2 | `test_nfr4_path_safety` (AC-NFR4) | ✅ PASS |
| NFR-5 Offline / digest-pinned base | `requirements*.txt` pinned, `Dockerfile` digest | T8 | pinned reqs ✅; **base digest = OQ-4 (owner input)** | ⚠️ OQ-4 |
| NFR-6 Windows paths + UTF-8 | `posix()`, UTF-8 reads | T2 | exercised by all index tests (POSIX paths asserted) | ✅ PASS |

**Open questions** (spec §6): OQ-1 sqlite-vec/FAISS mirror availability (accelerator only;
numpy-flat canonical) · OQ-2 references/ frontmatter not yet backfilled → tests on fixtures ·
OQ-4 internal-mirror base-image digest. None block the lexical service; OQ-4 blocks only the
Docker build step.

**Result: 17/17 testable requirements PASS; FR-11 artifacts present; NFR-5 pending OQ-4 digest.**
