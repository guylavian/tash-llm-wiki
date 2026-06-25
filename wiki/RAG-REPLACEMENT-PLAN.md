# RAG Replacement Plan — turning this LLM-Wiki into an SRE brain

## Is this a RAG replacement? Yes — a structurally stronger one, running on two of three cylinders.

Classic vector-RAG = chunk everything → embed → top-k cosine → stuff a prompt. It has no provenance, no "this is inference not fact" signal, no temporal/version awareness, no memory of past answers. This wiki is a different, stronger paradigm — *compiled / structured RAG*: a curated synthesis layer (`topics/entities/questions/`) over frozen sources, with a **citation contract**, a **5-arm Confidence gate** (never serve inference as fact), a **deterministic temporal knowledge graph**, and a **`questions/` answer cache** that amortizes. That's exactly what production RAG is criticized for lacking.

**But three layers are scaffolded, not operational** (verified in code):

1. **Dense semantic retrieval** — `embed.py` is complete (RRF fusion) but **no model is vendored and no index is built**. Retrieval is lexical+graph only, so **paraphrase recall collapses** (eval: `dpop` exact @7 → paraphrase @118; `kerberos-delegation` @1 → @87). Recall ceiling ~74% @10.
2. **LLM synthesis** — `online/llm.py` (LiteLLM, loopback-gated) + the LangGraph QUERY graph exist but default `WIKI_LLM=off`. **No running answer path** — the host agent improvises.
3. **Graphiti/Kuzu graph** — `tkg/graphiti_backend.py` is complete (bi-temporal, raw `kuzu`, no LLM) but `WIKI_TKG` is off; only the JSON store is built.

**Goal:** activate them into one air-gapped, cited, gated **`wikikb ask`** pipeline — an OpenCode agent consumes it now; an **SRE agent** consumes it later, turning an alert/symptom into a cited probable-cause + suggested fix with a confidence banner.

### Decisions (locked)
- **LLM backend:** local **Qwen ~27–32B via Ollama** (loopback, fully offline — honors the air-gap).
- **LLM × graph:** **propose-only** — the LLM may *suggest* edges into a staging file; the canonical graph stays deterministic (rule **R3**). *Evidence:* Graphiti is itself hybrid (LLM at ingest, deterministic MinHash/LSH + BM25/cosine at query); 2025–26 GraphRAG practice for **high-stakes** domains is schema-validate triples + human/gate-in-the-loop, because early extraction errors *magnify* downstream. An SRE brain is high-stakes — a hallucinated edge = a confidently-wrong fix.
- **Deliverable:** a `wikikb ask` CLI verb (agent-consumable, `--json`), SRE symptom→cause→fix oriented. OpenAI-compatible HTTP shim **deferred**.

---

## Phase 1 — Activate dense semantic retrieval  *(the actual recall fix; highest leverage, no new code)*

Most important for SRE: **alert text is always a paraphrase** of doc language.
- Vendor **BGE-small-en-v1.5** (~130 MB, 384-dim) → `_meta/models/bge-small-en-v1.5/` (offline `pip download … --only-binary` → `--no-index` install), per `_meta/models/README.md`.
- Build: `python3 -m wikikb embed build --domain {keycloak,active-directory,cisco-ios-xe}` → `_meta/embeddings/<d>.npz`+`.json` (delta-aware, SHA-gated). **Embed both** `reference/` bodies **and** synthesis pages.
- Validate lift: `wikikb evaluate --hybrid` — expect `dpop`/`kerberos`/`token-exchange` paraphrases into top-10. **Re-record `baseline.eval*.out`** after (index grows).
- Files: `retrieval/embed.py` (`build`/`dense_rank`/`rrf_fuse`), `retrieval/kb.py` (`--hybrid`), `quality/evaluate.py` (`hybrid_rank`). **Activation only.**

## Phase 2 — Local Qwen + ship `wikikb ask`  *(the generation half)*

- `ollama pull qwen2.5:32b` (or the Qwen3 ~30B named). `_meta/llm.config.yaml` (gitignored) → `api_base: http://127.0.0.1:11434`, `model: ollama/qwen2.5:32b`; set `WIKI_LLM=local`. The `_enforce_local` loopback gate already permits this and refuses egress.
- **New thin verb `wikikb ask "<q>"`** = wrap existing `graph/query_graph.run_query` (route → retrieve → [expand if thin] → gate → synthesize). Already imports `lint.gate_banner` (faithful gate) and **falls back to extractive when LLM off** (works before Ollama is up). Output = answer + **two-tier References** (RH `kb:`/`guide:`/`ref:` + Wiki/`web:`) + gate banner; add `--json`.
- Cost: `online/cost.py measure()` → `_meta/eval/cost_report.json`; surfaced by `lint --status`. Local = `unpriced/local`.
- **Guardrail:** `evaluate.py` recall stays LLM-free (no second source of truth).

## Phase 3 — Activate Graphiti/Kuzu bi-temporal graph  *(multi-hop + temporal retrieval)*

- `pip install kuzu` (embedded, no socket), `WIKI_TKG=kuzu`, `wikikb tkg ingest` → loads deterministic nodes/edges into Kuzu (`valid_at`/`invalid_at`, Graphiti-schema-compatible). JSON store stays canonical; Kuzu accelerates queries.
- Extend retrieval beyond 1-hop `expand.py`: multi-hop "symptom → component → cause"; use `temporal-query`/`cross-domain-query`. The `symptoms:` frontmatter + `*-implementation-review` MOCs (symptom→cause reverse index) are the SRE lookup surface.
- **Keep R3:** edges stay deterministic (`[[links]]`, `kb:`, `domain:`).

## Phase 4 — LLM-proposed graph enrichment, gated  *(the "graphiti + llm", done safely)*

- **New `wikikb propose-edges --domain <d>`**: LLM proposes entity/relation edges → written **only** to `_meta/tkg/proposed-edges.jsonl` (staging, gitignored), tagged `inferred` with source span. **Never auto-merged.**
- **Deterministic schema validator** (stdlib): each proposal must reference real nodes, a known rel type, a resolvable source (the query-checker pattern that catches ~85% of errors). Reject otherwise.
- **Promotion** is explicit (`--promote <id>`): materializes a normal deterministic edge with a real citation → canonical graph stays byte-reproducible/auditable.
- Files: new `graph/propose.py` (LLM via `online/llm.py`, `None`-safe) + validator reusing `tkg/model.py` + `crosslink.resolve()`.

## Phase 5 — SRE-agent surface  *(the end goal)*

- `wikikb ask --sre "<alert / log signature / symptom>"`: route via `symptoms:` + review MOC → graph-traverse to cause page → synthesize **suggested remediation** with citations, the gate banner, and a mandatory *"verify before applying"* line. `--json` → `{cause, evidence[], fix_steps[], confidence, citations[]}`.
- Wire into OpenCode: add `.opencode/command/ask.md` (thin pointer like existing `ingest/lint/query`). Future SRE agent calls the same verb.

---

## Guardrails (enforced by existing tests)
- **Air-gap:** new deps lazy-imported, off-by-default, loopback-only; `selftest.py` asserts no module-scope 3rd-party import + DNS/socket block — stays green.
- **Gate faithfulness:** generation reuses `lint.gate_banner` (same 5 arms as `lint --strict`) — never re-implemented (BF-4).
- **Determinism:** canonical TKG + `evaluate.py` recall stay LLM-free; LLM touches only synthesis + the *staging* file.
- **Goldens:** re-record after Phase 1; keep the documented **40/42** baseline (2 reds are intentional fixtures — do not "fix").
- **Tokenization:** vendored-by-path only; never `litellm.token_counter` (tiktoken egress — BF-3).

## Verification (end-to-end)
1. `python3 tests/selftest.py` → still 40/42, no NEW reds, after each phase.
2. **P1:** `evaluate --hybrid` lifts the 3 paraphrase cases into @10; goldens re-recorded.
3. **P2:** `WIKI_LLM=local wikikb ask "bind an access token to a client key so a stolen token can't be replayed"` → cited answer naming DPoP + gate banner + two-tier refs; `WIKI_LLM=off` still returns extractive fallback.
4. **P3:** `WIKI_TKG=kuzu wikikb tkg temporal-query --as-of 26.2` + a multi-hop symptom→cause traversal return from Kuzu; `graph-status` shows backend active.
5. **P4:** `propose-edges` writes only to `proposed-edges.jsonl`; canonical `tkg ingest` output byte-identical before/after (R3 intact); an invalid proposal is rejected.
6. **P5:** `ask --sre "ISPN000541 dns_query CrashLoopBackOff after scale-up"` → `{cause, fix_steps, confidence, citations}` JSON with verify-before-applying banner; OpenCode agent calls it via `.opencode/command/ask.md`.

## Sequencing
P1 first (biggest recall win, no new code). P2 (makes it answer). P3–5 build the SRE graph brain. **P1–3 are activation of already-written code; P4–5 are the only meaningful net-new code, both small and isolated.**

---
*Research informing propose-only:* Zep/Graphiti temporal-KG architecture (arXiv 2501.13956); GraphRAG hallucination + human-in-the-loop surveys (2025–26); schema-aware query-checking (~85% of extraction errors caught).
