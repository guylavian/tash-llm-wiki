# tasks.md — Ordered Implementation Tasks

> Ordered so the **lexical service is runnable before embedding is added**. Each task links the
> requirements it implements and the acceptance tests it must satisfy. No task without a
> requirement link. Phase 3, self-reviewed.

| Task | Description | Implements | Acceptance tests | Files |
|------|-------------|-----------|------------------|-------|
| **T1** | `Config` from env, frozen, no IO on import. | NFR-5, FR-9 surface | (covered via T7/T9) | `wiki_router/config.py` |
| **T2** | Index build: routable globs, exclude source-only + `routable!=true`, reuse `_split_frontmatter`, H2 split w/ anchors+line ranges, POSIX/UTF-8 paths, inverted index, path-safety `resolve_safe()`. | FR-1, FR-5, NFR-4, NFR-6 | AC-1.1, AC-1.2, AC-1.3, AC-NFR4 | `wiki_router/index.py` |
| **T3** | `Ranker` base: `_prefilter` (FR-3 version/domain/type), stable deterministic sort; `LexicalRanker` (BM25-lite + exact-code bonus, zero deps). | FR-2, FR-3, FR-8, NFR-3 | AC-2.1, AC-2.2, AC-3.1, AC-3.2, AC-NFR3, AC-8.1 | `wiki_router/ranking.py` |
| **T4** | FastAPI app: `/route`, `/get` (inject section/full, 404 reasons), `/healthz`, `/metrics`, `/reload` (atomic swap + `X-Admin-Token`). Provenance on every response. | FR-2, FR-4, FR-5, FR-6, FR-7, NFR-1 | AC-2.1, AC-4.1..4.4, AC-5.1, AC-6.1, AC-6.2, AC-7.1, AC-7.2 | `wiki_router/app.py` |
| **T5** | Embedding: `resolve_source` (endpoint/model/None, loopback-only), metadata-only corpus builder, numpy-flat `.npz` store, `EmbeddingRanker`. | FR-9, FR-10 | AC-9.1, AC-9.2, AC-10.1 | `wiki_router/embedding.py` |
| **T6** | `HybridRanker` + `make_ranker` factory (embedding/hybrid → fallback to lexical on no source, with warning). | FR-8, FR-9 | AC-8.2, AC-9.1 | `wiki_router/ranking.py`, `wiki_router/embedding.py` |
| **T7** | Test suite (fixtures incl. a `wiki/reference/` source file, a `routable:false` file, a 26.2-only and a 26.6 doc, an error-code doc + a near-miss doc) covering every AC; deterministic fake embedder for FR-8/9/10. | all ACs | full AC set | `tests/test_router.py`, `tests/fixtures/**` |
| **T8** | Packaging: `requirements.txt` (lexical core, pinned) + `requirements-embedding.txt` (numpy pinned); `Dockerfile` FROM pinned-by-digest, repo RO at `/repo`, HEALTHCHECK `/healthz`, uvicorn. | NFR-5, NFR-2 | (build + AC-7.1) | `Dockerfile`, `requirements*.txt` |
| **T9** | Agent contract: `wiki_tools.json` (wiki_route/wiki_get schemas) + `AGENTS.md.snippet` (route-first, escalate-don't-fabricate). | FR-11 | AC-11.1, AC-11.2 | `agent/wiki_tools.json`, `agent/AGENTS.md.snippet` |
| **T10** | Traceability matrix + test transcript + run/curl/docker instructions in PR. | Phase 5 | matrix complete | `service/TRACEABILITY.md` |

**Order rationale:** T1→T2→T3→T4 yields a runnable lexical service (the MVP) passing the
majority of ACs. T5→T6 add the optional embedding/hybrid path with guaranteed fallback. T7
verifies; T8 packages; T9 wires the agent; T10 proves traceability.
