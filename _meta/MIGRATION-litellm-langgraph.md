# Migration Plan: An Optional, Offline-First LLM / Cost / Orchestration Tier for the Wiki

**Author:** lead architect (Claude, via design workflow) · **Date:** 2026-06-23 · **Status:** proposed
**Scope:** introduce LiteLLM (LLM gateway), LangGraph + LangChain (orchestration), and a measured
token/$/latency cost layer into the RHBK/Keycloak wiki repo **without breaking the air-gap,
stdlib-default, or faithfulness invariants.**

> Produced by a judged design workflow: 4 independent architectures → 8 adversarial critiques
> (air-gap lens + faithfulness/fit lens) → 3 decisions (LangChain-vs-LangGraph, cost-tracking,
> air-gap reconciliation) → synthesis. Winning spine: **EVAL-&-COST-FIRST** (avg 5.5), with grafts
> from the other three. All structural claims were verified against the source.

### Stakeholder decisions (confirmed 2026-06-23)
- **Orchestration → LangGraph as planned** (§3 verdict stands: LangGraph for QUERY/INGEST, LCEL leaf
  for the single synthesize step, neither framework for LINT/STATUS). The lightweight-stdlib-runner
  alternative is **not** taken.
- **Remote endpoints → opt-in allowed** (OQ#5 resolved): keep the `WIKI_LLM_ALLOW_REMOTE=1` + key-env
  **double-opt-in** for cloud models (and real $ cost). The default remains local-loopback-only; the
  remote path is a loud, logged, explicit escape hatch — **not** structurally removed.
- **Implementation status → SHIPPED (Phases 0–5 complete, 2026-06-25).** The full Phase 0–5 migration
  has landed: `cost.py`/`llm.py` (loopback-gated LiteLLM gateway), the LangGraph QUERY + INGEST graphs
  (`graph/query_graph.py`, `graph/ingest_graph.py`), `evaluate.py --measure-llm` + budget gates, and
  the `lint.py --status` spend table. **Phase 5 closed** with the 32B→7B routing lever delegated to
  `litellm.Router` (OSS — `llm.complete_routed()`, cheap/hard model groups + fallbacks); disk response
  caching stays deliberately deferred (the `questions/` tier already amortizes; temp=0 ≠ bit-stable on
  local GPU). With `WIKI_LLM` unset and no optional deps, the wiki behaves exactly as it did pre-Phase-0.
  Successor work is tracked in `_meta/ROADMAP.md`.

---

## 1. Executive summary + the central tension

The repo today has **zero LLM calls and zero pip dependencies** (verified: no
`requirements*.txt`/`pyproject.toml`/`setup.py` anywhere; no top-level 3rd-party import in
`wiki/_meta/wikikb/*.py`). The "agent loop" is supplied by the **host runtime** (Claude Code /
OpenCode) executing the prose operations in `wiki/CLAUDE.md`; the deterministic Python tools
(`kb`, `route`, `expand`, `embed`, `eval`, `lint`, `gate_probe`, `gate_page_probe`) are the *value*
and are explicitly **not** LLM calls. The only cost signal is the `CHARS_PER_TOKEN = 4` heuristic
(verified at `eval.py:51`, replicated as inline `len//4` at `lint.py:345` and `embed.py:43`).

**The central tension.** The user wants (A) the agent/API calls migrated to **LiteLLM**, (B) a
**LangChain-vs-LangGraph** decision, and (C) the **evals + cost optimization** migrated to these
tools with measured tokens + $. But every one of those tools is a network client by nature, and the
repo's load-bearing identity is **air-gapped, stdlib-only, no network egress** (`AGENTS.md`,
`.opencode/agent/wiki.md` `webfetch:false`, every tool docstring, enforced by `selftest.py` check #10).

**How this plan resolves it — three moves:**

1. **Reframe "migrate the agent calls."** There are zero calls to migrate. So we *introduce* an
   explicit, programmatic LLM-gateway seam for the operations that are currently prose-defined and
   runtime-executed — **as an optional, off-by-default tier**, never a default code path. The host
   runtime stays a valid agent loop with the tier absent.
2. **Reconcile the air-gap by pointing LiteLLM at a LOCAL endpoint.** LiteLLM's `api_base` targets a
   loopback Ollama/vLLM server (the design's stated ~27B target). The gateway exists with **no
   internet egress**. This is the same reconciliation the dense layer already uses (a vendored model
   loaded by path).
3. **Follow the `embed.py` precedent exactly, plus one hard correction.** Every new dependency is
   lazy-imported inside functions behind `try/except`, gated by a flag, vendored as an optional
   extra, and **degrades to today's stdlib behavior byte-for-byte when absent**. The correction
   (load-bearing): **do not use `litellm.token_counter` for tokenization** — it transitively triggers
   a `tiktoken` `cl100k_base` *network download* for unknown/local models (the #1 fatal flaw across
   the judged critiques). Real-token counting uses a **vendored-by-path tokenizer**, mirroring
   `embed.py`'s by-path model load; LiteLLM is used only for the gateway call + `$` pricing read from
   its **bundled static JSON**.

The offline path is the **contract**; the online tier is an **accelerator**, exactly as the dense
layer is to lexical search.

---

## 2. Chosen architecture (text diagram)

The spine is the **EVAL-&-COST-FIRST** measurement seam. Grafted onto it: the **`llm.py`
generation-side twin of `embed.py`**, the **LangGraph QUERY/INGEST graph with an LCEL leaf**, the
**gate-as-imported-node** faithfulness lock, and the **vendored-tokenizer** air-gap fix.

```
                       wiki/CLAUDE.md  ── single source of truth (prose ops) ──┐
                                                                               │ faithful mechanization
  HOST RUNTIME (Claude Code / OpenCode)  ── default agent loop, always valid ──┤ (optional, off by default)
                                                                               ▼
  ┌─────────────────────────────────  OPTIONAL ONLINE TIER  (WIKI_LLM=off by default) ─────────────────────────────┐
  │                                                                                                                 │
  │   LangGraph StateGraph  (QUERY, INGEST)   ← orchestration; conditional edges, loop, gate node, checkpoint       │
  │   ┌──────────┬──────────┬─────────────┬───────────────┬──────────────────────┬───────────┬──────────────┐      │
  │   │ route_   │ tiered_  │ graph_      │ raw_fallback_ │ confidence_gate_node │ synthesize│ file_back_   │      │
  │   │ node     │ read_node│ expand_node │ node (hybrid) │ (CONDITIONAL EDGE)   │ _node     │ node + loop  │      │
  │   └────┬─────┴────┬─────┴──────┬──────┴───────┬───────┴──────────┬───────────┴─────┬─────┴──────┬───────┘      │
  │        │ calls    │ calls      │ calls        │ calls            │ IMPORTS         │ LCEL leaf  │ shells out   │
  │        ▼          ▼            ▼              ▼                  ▼                 ▼            ▼              │
  │   route.route  kb.load/   expand.expand/  embed.dense_rank/  lint.page_gate_   ChatPrompt |   manifest.py    │
  │   (stdlib)     kb.score   graph_notes     embed.rrf_fuse     verdict (H2/H3)   ChatLiteLLM |  crosslink.py   │
  │                (stdlib)   (stdlib)        (optional dense)   gate_probe.gate_  parser         index.py       │
  │                                                              verdict (H1)      (LangChain     (stdlib)       │
  │                                                              (stdlib, IMPORTED)  LCEL)         ───────        │
  │                                                                                   │                          │
  │                                                                                   ▼                          │
  │                                                            llm.py  ──gateway──►  litellm.completion(         │
  │                                                            (lazy/guarded,         model='ollama/<27b>',      │
  │                                                             embed.py twin)        api_base='localhost:11434')│
  │                                                                                   ──► LOCAL Ollama / vLLM    │
  │                                                                                                              │
  │   cost.py  ── token/$/latency oracle ──►  tok via VENDORED tokenizer (by path) | len//4 fallback            │
  │   (lazy/guarded, embed.py twin)            $ via litellm bundled price JSON read directly | $0.00 local     │
  │                                            latency via time.perf_counter (pure stdlib)                      │
  └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
            ▲                                                                              ▲
            │ imports the REAL tools (faithfulness)                                        │ imports the REAL cost path
  eval.py ──┘  recall@k over kb/route/expand/embed (UNCHANGED) + 2 cost columns ───────────┘

  LINT / STATUS:  lint.py, manifest.py  ── NEITHER framework, plain stdlib, UNTOUCHED ──
```

**Where each piece sits:**
- **`cost.py`** (NEW) — the measurement oracle. The *whole spine*. Token/$/latency, lazy
  LiteLLM-pricing + vendored-tokenizer, `embed.py` degradation contract. Lives behind `eval.py` first.
- **`llm.py`** (NEW) — the generation-side twin of `embed.py`. The single LLM seam:
  `litellm.completion()` → local Ollama. Default-off.
- **LangGraph** — orchestrates QUERY and INGEST as `StateGraph`s whose nodes *wrap the existing
  stdlib tools*. The deterministic tools stay deterministic.
- **LangChain (LCEL)** — used **only** for the one genuine LLM leaf
  (`synthesize`/`ingest-extract` = `prompt | ChatLiteLLM | parser`) and its usage callbacks.
- **`lint` / `manifest` (LINT, STATUS)** — get **neither** framework. Plain stdlib.
- **`eval.py`** — keeps importing the real `kb`/`route`/`expand`/`embed` (faithfulness) and gains two
  cost columns from `cost.py`.

---

## 3. The LangChain-vs-LangGraph verdict (Decision B)

**Verdict: Both, with a hard boundary.**

> LangGraph (StateGraph) owns QUERY and INGEST — the two stateful, branching, looping, gate-bearing
> operations. LangChain (LCEL) owns ONLY the single genuinely-LLM leaf inside them: the
> synthesize-and-cite step, expressed as a `prompt | llm | parser` Runnable wrapped around LiteLLM.
> LINT and STATUS get NEITHER framework — they are deterministic Python and stay plain
> subprocess/library calls. The existing deterministic tools (route, expand, kb, embed, eval, and
> crucially the Confidence gate `page_gate_verdict`/`gate_verdict`) become LangGraph NODES and EDGES,
> never LLM calls — they are the value of the system and must not be re-implemented as prompts.
> LiteLLM under the one LCEL leaf is configured with `api_base` pointing at the local Ollama/vLLM
> endpoint, so the air-gap invariant holds and the `embed.py` precedent is followed: optional,
> lazy-imported, behind a flag, graceful degradation when offline.

**Control-flow reasoning (verified against the code):**

QUERY is **not** a linear pipe. Per `CLAUDE.md`'s QUERY op + the code, it is:

```
route.route() → (confident? skip global index : read it)        # conditional edge
  → tiered summary read
  → expand.graph_notes(seed vs closure)                          # conditional
  → CONDITIONAL escalating raw/--hybrid fallback (only if thin)  # conditional edge
  → Confidence gate: H1/H2/H3/H4 each-fires-alone + L-combo      # 5-arm DECISION NODE
  → synthesize + cite (the ONE LLM leaf)
  → file-back + OPTIONAL mini-INGEST                             # loop into a subgraph
```

That is **branching + conditional escalation + a decision node + a cycle + accumulating state**.
LCEL chains model a DAG of `Runnable`s and express branching only through awkward nested
`RunnableBranch`/`RunnableLambda`, with **no first-class state object, no checkpoint, no clean
cycle** — you fight the abstraction. `LangGraph.StateGraph` *is* this shape: a typed `TypedDict`
state, `add_conditional_edges` (the gate's natural home), cycles (file-back → mini-INGEST), and
`SqliteSaver` checkpointing (resume/replay the gate decision — exactly the auditability "never serve
inference as fact" demands).

INGEST is a manifest-gated loop:
`manifest.status → (empty delta? END) → per-source find-or-create page (LLM leaf) → assign
provenance → manifest.record → loop`. Again a `StateGraph`, not a chain.

The **only true LLM leaf** in the whole system is "write the prose answer and tag each claim's
provenance" — the textbook LCEL `prompt | llm | parser`, slotting in as one LangGraph node.

**Rejected:**
- A **full LangChain ReAct/tools agent** for orchestration — it duplicates the host runtime's agent
  loop and re-introduces nondeterminism into routing/recall/gate, which the design (and
  `gate_probe`/`gate_page_probe`/`eval` CI) deliberately made deterministic.
- **LCEL chains for the whole QUERY pipeline** — branching, the 5-arm gate, the escalating fallback,
  and the file-back cycle map poorly onto `RunnableBranch` nesting and have no state/checkpoint/loop
  primitive.

---

## 4. LiteLLM integration design (SDK, not proxy, local-first)

**SDK, not the proxy server.** Use `litellm.completion(...)` from one module,
`wiki/_meta/wikikb/llm.py`. A proxy is a **long-running daemon** — a process class the repo has never
had (verified: zero `serve|daemon|uvicorn|fastapi` precedent; every tool is a one-shot stdlib script
that exits). The proxy's spend-DB also implies `prisma` migrations at boot, with no analog in a
"copy a model dir" install. The proxy (budgets, virtual keys) is documented in
`llm.config.yaml.sample` as the **deferred** future hop, **not introduced now**.

**`llm.py` mirrors `embed.py` exactly** (verified contract: `have_library()` `embed.py:56`,
`available()` `:70`, `status_str()` `:75`, lazy import-inside-function `:144`, graceful `None`
fallback `:223`):
- `have_library()` → `try: import litellm` (lazy, in-function).
- `available()` → library importable **AND** an endpoint reachable/configured **AND** `WIKI_LLM != off`.
- `status_str()` → which path is active (for the eval/CI banner).
- `complete(messages, **kw)` → the gateway call; returns the deterministic **extractive answer** (top
  snippets) when unavailable, *never* raises — identical to `embed.dense_rank()` returning `None`.

**Local-Ollama default + providers:**
```yaml
# wiki/_meta/llm.config.yaml.sample  (real config gitignored)
model:    "ollama/qwen2.5:32b"          # the design's ~27B Ollama-class target
api_base: "http://127.0.0.1:11434"      # loopback ONLY
provider_allowlist: ["ollama", "openai-compatible-localhost", "vllm"]
max_tokens: 2048
temperature: 0                          # determinism: filed answers must not drift the cache
budget_per_query_tokens: 32000
```
- **Default boot is local-only.** `llm.py` validates the configured provider against
  `provider_allowlist` and refuses any non-loopback `api_base` unless `WIKI_LLM_ALLOW_REMOTE=1` is
  **explicitly** set (a second, loud, logged opt-in). A misconfigured cloud `api_base` therefore
  cannot silently regress the air-gap.
- vLLM is reachable as `openai/<model>` + `api_base=http://127.0.0.1:8000/v1` — still loopback.
- **Telemetry off at import** (before the lazy call): `litellm.telemetry = False`,
  `litellm.success_callback = []`, `litellm.suppress_debug_info = True`, and
  `os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"` so LiteLLM never attempts its GitHub
  price-map refresh. *(These are runtime flags; the air-gap is additionally defended structurally —
  see §5/§7 — by **not** calling the networked `token_counter`.)*

**Fallback / routing (SDK-level, local-only by default):**
- `num_retries` + a local fallback `ollama/qwen2.5:32b → ollama/qwen2.5:7b` on error/timeout (32b for
  synthesis, 7b for cheap routing/summaries). Pure config inside `llm.py` / the LCEL leaf — no proxy
  needed.
- A cloud fallback model is reachable **only** when `WIKI_LLM_ALLOW_REMOTE=1` **and** a key env-var
  is present. Never in the default path.

`litellm.embedding` stays **unused** by default — `embed.py`'s vendored `sentence-transformers`
remains the dense layer (keeps the offline-degrade we already test). A LiteLLM `embedding` model
entry is offered only as a commented, env-gated alternate.

---

## 5. Cost tracking + optimization design (Decision C — the spine)

**Verdict: a NEW, OPTIONAL, lazily-imported `cost.py` owns ALL real token/$/latency accounting, and
`eval.py`'s single "cost" number is SPLIT into two orthogonal columns.**

### 5.1 Two columns, not one (the load-bearing distinction)
The existing `ctx_t` proxy and an LLM-call bill are **different quantities measuring different
things**. Collapsing them destroys the very signal `route`/`expand`/`dense` are tuned against. So:

1. **RETRIEVAL cost — keep `ctx_t` EXACTLY as-is** (`eval.py:175-177`: `idx_t + snip_t + body_t`, all
   `/CHARS_PER_TOKEN`). This is what router-skip and graph-rescue optimize (verified: a graph-rescued
   case opens **1** note instead of `miss_opens`, `eval.py:166-174`). **It must not regress.**
2. **GENERATION cost — a NEW measured token+$+latency column**, populated **only** when a real LLM
   call happens through the local gateway. `n/a (offline)` in the default run.

### 5.2 The air-gap-correct tokenizer (the decisive graft)
**Do NOT use `litellm.token_counter`.** For an unknown/local model it falls back to `tiktoken`, which
**downloads `cl100k_base.tiktoken` from `openaipublic.blob.core.windows.net`** on first use, and in
recent LiteLLM the `tiktoken` import is *eager* — so even a lazy `import litellm` can trip the fetch,
and the failure can be an unhandled `ConnectionError` or a hang behind a proxy. This is the #1 fatal
flaw the judged critiques identified, and it is precisely the call the EVAL-&-COST-FIRST design made
primary.

**Instead, `cost.count_tokens()` uses a VENDORED-BY-PATH tokenizer — the literal `embed.py`
precedent** (model loaded by path, no socket):
```python
# cost.py — count_tokens(): three-tier, all offline
def count_tokens(text, model=None):
    try:                                   # tier 1: vendored tokenizer.json by path
        return _vendored_tok(model).encode(text).__len__()   # _meta/models/<model>/tokenizer.json
    except Exception:
        try:                               # tier 2: reuse embed.py's already-vendored ST tokenizer
            return embed.tokenizer_count(text)
        except Exception:
            return len(text) // CHARS_PER_TOKEN              # tier 3: today's exact heuristic
```
This delivers **real per-model tokens, fully offline**, without LiteLLM's import-time network hazard.
When no tokenizer is vendored it returns **byte-identical numbers to today**.

### 5.3 The `$` column (offline-safe)
- `$` is read from LiteLLM's **bundled static** `model_prices_and_context_window.json` — **read
  directly as JSON if possible**, decoupling pricing from the `tiktoken`/import hazard; or via
  `litellm.cost_per_token(...)` with the `LITELLM_LOCAL_MODEL_COST_MAP` guard set. Neither opens a
  socket.
- For a local `ollama/*` model the price map yields **$0.00**, tagged `unpriced/local`. Optionally
  register a **shadow rate** (`litellm.register_model({... input_cost_per_token ...})`) so the `$`
  column is a meaningful *compute-cost proxy* even offline. Real $ only appears on the opt-in remote
  path.

### 5.4 Latency (free, stdlib)
`time.perf_counter()` around each LLM call and each eval-case retrieval → p50/p95 ms. The **most
actionable signal for a local 27B model**. Zero deps.

### 5.5 The retrieval-cost ↔ LLM-cost relationship (made explicit in `eval` output)
- `ctx_t` (proxy) ≈ the **prompt-side** token budget the retriever *assembles* (index + snippets +
  opened bodies).
- `gen_prompt_tok` (measured) = the **ground truth** for that same context once the real model
  tokenizes it.
- Their ratio `gen_prompt_tok / ctx_t` **calibrates** the 4-chars/token heuristic per model *without
  replacing it* — so `route`/`expand`/`dense` keep optimizing the cheap offline proxy, and the
  measured column validates/recalibrates it.
- `gen_completion_tok` is the **net-new generation axis** (answer length, unrelated to retrieval).

### 5.6 Budgets, caching, routing (optimization levers)
- **Budget gate (no new dep needed):** `eval.py --budget-tokens` / `--budget-usd` set **exit code 3**
  when a run's mean exceeds budget → a context-cost regression **fails CI** alongside recall.
  Implementable on the heuristic *or* measured number; ships **today** with no LiteLLM. For
  in-process generation budgets, set `litellm.max_budget` and catch `litellm.BudgetExceededError`.
- **Caching:** `litellm.cache = Cache(type="disk", disk_cache_dir="_meta/.llm_cache")` (disk, **not
  redis**, to stay air-gapped). A re-asked QUERY is a $0/0-token cache hit — dovetailing with
  CLAUDE.md's "amortization makes the filed answer the cheap cache hit." `resp._hidden_params
  ['cache_hit']` feeds a `cached` column.
- **Routing:** local 7b for routing/summaries, 32b for synthesis; `32b→7b` fallback. Cuts cost with
  no code change.
- **RRF-narrowed context:** the cheapest lever already exists (`kb.py --hybrid` / `expand.py`):
  fewer, higher-precision opened notes → fewer `gen_prompt_tok`. The measured column will *show* this
  saving in real tokens/$.
- **Ledger:** a `UsageRecorder` shaped like LangChain's `OpenAICallbackHandler` accumulates a
  run-total `{tokens, $, by domain/kind}` to `_meta/eval/cost_report.json` (gitignored, regenerable
  like the embeddings index). When LangGraph is introduced, the same recorder snaps in unchanged.

---

## 6. Evals migration (recall scoreboard + gate probes evolve; faithfulness preserved)

**The recall scoreboard does not move.** `eval.py` keeps importing the real `kb`/`route`/`expand`/
`embed` (verified `:46-49`) and keeps `evaluate()`'s ranking, `first_hit`, `graph_hit`, and rescue
logic **byte-for-byte**. Recall is a retrieval property, model-independent; it is computed with
`WIKI_LLM` unset so **no model runs in CI**. The frozen `cases.jsonl` / `cases.heldout.jsonl` schema
is **unchanged** (cost is *computed*, not annotated).

**Cost columns are additive (`--measure-llm` flag):**
- Default run: `cost.count_tokens()` returns today's `len//4` numbers (no tokenizer vendored) →
  **byte-identical to the frozen baseline**. The migration is a strict superset.
- With a vendored tokenizer present: the three `/CHARS_PER_TOKEN` sites tokenize the *genuine*
  index/snippet/body strings → faithfulness on the cost axis **improves** (measures real
  bytes-entering-context, not a char count).
- With `WIKI_LLM=local` + `--measure-llm`: a new block **"LLM-CALL COST (measured via LiteLLM; n/a
  offline)"** prints `gen_prompt_tok / gen_completion_tok / gen_cost_usd / gen_latency_ms` beside the
  existing **"CONTEXT-TOKEN PROXY"** block. When `cost.available()` is `False` it prints `n/a
  (offline)` — same UX as eval's existing `Phase-3 dense: ... INACTIVE (lexical fallback)` line.
- `eval.py` prints `cost.status_str()` at startup, exactly as it prints `embed.status_str()` for
  `--hybrid`, so a run self-declares which path ran.

**Faithfulness kept three ways:**
1. eval still imports the real `kb`/`route`/`expand`/`embed` for ranking;
2. the LLM-cost column is produced by importing the **same `cost.measure`** the QUERY operation calls
   — eval does not re-estimate tokens, it reports what the gateway/tokenizer actually counted;
3. when the optional deps/model are absent the numbers are identical to the frozen baseline →
   `cases.jsonl` stays a valid frozen reference; CI pins one mode.

**Gate probes evolve into shared-rule assertions.** `gate_probe.py` and `gate_page_probe.py` stay
**unchanged** and now **double as unit tests of the LangGraph `confidence_gate_node`**, because the
node calls their exact functions — `lint.page_gate_verdict()` (H2/H3, verified `lint.py:131`) and
`gate_probe.gate_verdict()`/`load_tiers_covered()` (H1, verified `gate_probe.py:39,64`).
**Faithfulness invariant extended:** the gate the runtime executes, the gate `lint` enforces, and the
gate CI probes assert are provably the **same code**.

> **Critical guard against the "second source of truth" risk:** `eval.py` recall **does not** run
> through the LangGraph. The graph is the *generation/orchestration* path; eval's recall path stays
> the small, verified, stdlib replay so it runs offline with no langgraph installed. A `selftest`
> check asserts `eval.py` exits 0 with `WIKI_LLM` unset and **no** orchestration deps present.

**New metrics:** measured `gen_*` tokens, `gen_cost_usd` (or `unpriced/local`), `gen_latency_ms`
p50/p95, the `gen_prompt_tok/ctx_t` calibration ratio, a `cached` flag, and a **gate-fire-rate**
column (run `lint.page_gate_verdict` over each candidate page's frontmatter — pure stdlib, no model,
measures "how often the gate saves us").

---

## 7. Air-gap reconciliation

**Feature flag / config.** `WIKI_LLM=off|local|cloud` (default `off`) + optional gitignored
`wiki/_meta/llm.config.yaml`. With `off`, `llm.py`, `cost.py`, `eval.py`, and the LangGraph runner
behave **byte-identically to today** (host-runtime-driven, stdlib proxy cost).

**Offline default + `embed.py`-style lazy/graceful pattern.** All heavy imports (`litellm`,
`langgraph`, `langchain_core`) are **lazy, inside functions, behind `try/except`**. `import llm`,
`import cost`, and `import graph.query_graph` must be **stdlib-safe**:
- `cost.py` / `llm.py` keep all 3rd-party imports inside functions — trivially safe.
- **`graph/query_graph.py` requires care:** `StateGraph`/`BaseTool`/`BaseCallbackHandler` are base
  classes used at *definition* time. So `build_query_graph()` does its `from langgraph.graph import
  StateGraph` **inside the factory function**, not at module scope. A `selftest` grep asserts **no
  module imports `litellm`/`langchain`/`langgraph` at top level** — a regression guard that the tier
  never becomes eager.

**Structural air-gap, not just configurational.** The two real network hazards are (a) the `tiktoken`
download — **eliminated** by using a vendored tokenizer, never `token_counter` (§5.2); and (b) the
LiteLLM GitHub price refresh — disabled by `LITELLM_LOCAL_MODEL_COST_MAP=True` *and* preferably
bypassed by reading the bundled JSON directly. The only socket ever opened is to the **loopback**
model server the operator chose to run.

**Dependency packaging / vendoring.** No base `requirements.txt` (the zero-pip default holds). Add
**optional extras**:
- `wiki/_meta/requirements-online.txt` — pinned `litellm`, `langgraph`, `langchain-core`, vendored
  offline: `pip download -d ./wheels` on a networked box → `pip install --no-index --find-links
  ./wheels` on the sealed box (exactly the `_meta/models/README.md` pattern). **Caveat:**
  `tiktoken`/`tokenizers` ship **compiled (Rust) wheels** that must match the target's
  CPython/OS/arch — call this out in the README.
- Also **retro-document** the existing optional `sentence-transformers`+`numpy` here (today it lives
  only in `models/README.md` prose) so the "air-gap-with-optional-deps" story is written down once.
- `wiki/_meta/.gitignore` extended to ignore `llm.config.yaml`, `wheels/`, `.llm_cache/`,
  `cost_report.json` — **keep the READMEs** (same `models/* / !models/README.md` pattern, verified).

**selftest / CI proof (the tripwire).** Add checks mirroring check #10:
1. `cost.py --status` and `llm.py --status` exit 0 with the libs **absent**;
2. `cost.count_tokens('x') > 0` and `eval.py` exit 0 with `WIKI_LLM` unset → **graceful degrade**;
3. a grep asserts no top-level 3rd-party import;
4. the rendered default config has **no non-loopback host** unless `WIKI_LLM_ALLOW_REMOTE=1`;
5. a `cost_probe.py` (analogue of `gate_probe.py`) feeds a **stubbed** LiteLLM response and asserts
   the token/$/latency dict is well-formed and `BudgetExceededError` is raised — an O(1) behavior
   probe, **no real model**, faithful to the real `cost.measure` path.

**Contracts amended (kept as thin pointers to `CLAUDE.md`):**
- `wiki/CLAUDE.md` — under *Tooling & packaging* and *Operation: QUERY*, an **"Optional online
  tier"** note: gateway off by default, local-first, the offline grep/kb path unchanged and
  authoritative; cost is measured tokens+$ via `cost.py` (optional, falls back to chars/4). `cost.py`
  and `llm.py` added to the tooling list as "the SECOND/THIRD allowed dependencies — same
  lazy/guarded/graceful contract as `embed.py`, local-only."
- `wiki/_meta/wikikb/evaluate.py` docstring — measured tokens/$ optional; `CHARS_PER_TOKEN` is the offline
  default/fallback.
- `wiki/_meta/wikikb/embed.py` header — extend "the ONLY 3rd-party dep" to "`embed.py`, `cost.py`, and
  the optional `llm.py` gateway are the only third-party deps; all lazy/optional/local-first."
- `AGENTS.md` + `.opencode/agent/wiki.md` — clarify network stays disabled (`webfetch:false`
  **untouched**), the optional gateway targets a **local** endpoint only, default behavior unchanged.
- `.opencode/command/query.md` + `.skills/wiki-query/SKILL.md` — note the optional LangGraph runner
  is an *alternative* to the host loop, not a replacement; point back to `CLAUDE.md`.

---

## 8. Phased implementation roadmap

Ordered so **the offline guarantee is never broken** and each phase is **independently shippable**.
Phases 0–3 add **no required dep** and need no model; the heavy deps and the graph come last.

### Phase 0 — Stdlib seam, byte-identical (no deps)
**Goal:** prove the measurement seam is non-breaking before any dependency exists.
**Changes:**
- `wiki/_meta/wikikb/cost.py` (NEW) — stdlib-only path: `count_tokens = len//4`, `price = (0.0,
  unpriced=True)`, `status_str = "heuristic"`, `available()/have_library()` (return False),
  `UsageRecorder` (stdlib class), `time.perf_counter` latency.
- `wiki/_meta/wikikb/evaluate.py` (EDIT) — route the three `/CHARS_PER_TOKEN` sites through
  `cost.count_tokens()`; keep the constant as the fallback. Add `--budget-tokens`/`--budget-usd`
  (exit code 3) on the existing number.
- `wiki/_meta/tests/selftest.py` (EDIT) — assert `cost.py` imports stdlib-safe and `eval.py` output is
  byte-identical to baseline.
**Exit criteria:** `eval.py` output byte-identical to today; `selftest.py` green; `--budget-tokens`
fails a deliberately-too-low budget with exit 3.

### Phase 1 — Vendored real tokenizer (optional, still no network)
**Goal:** real per-model tokens, fully offline; validate the chars/4 proxy.
**Changes:**
- `cost.py` (EDIT) — tier-1 vendored-`tokenizer.json`-by-path + tier-2 reuse of `embed.py`'s
  tokenizer; tier-3 heuristic fallback. Add the `$` reader from LiteLLM's **bundled JSON read
  directly** (lazy, guarded), tagged `unpriced/local` for `ollama/*`.
- `eval.py` (EDIT) — print the `gen_prompt_tok/ctx_t` calibration ratio; second "measured tokens (via
  vendored tokenizer | heuristic)" caption.
- `wiki/_meta/cost/README.md` (NEW) — offline tokenizer vendoring + price-JSON notes.
**Exit criteria:** with no tokenizer vendored, identical to Phase 0; with one vendored, eval reports
real tokens and the calibration ratio; **no socket opened** (selftest network-tripwire green).

### Phase 2 — `llm.py` gateway scaffold (optional dep, default-off, local-only)
**Goal:** the single LLM seam; prove the air-gap contract before any orchestration.
**Changes:**
- `wiki/_meta/wikikb/llm.py` (NEW) — `have_library()/available()/status_str()/complete()`; local Ollama
  default; provider allowlist + loopback check; `WIKI_LLM` gate; telemetry off;
  `LITELLM_LOCAL_MODEL_COST_MAP=True` before lazy import.
- `wiki/_meta/llm.config.yaml.sample` (NEW), `wiki/_meta/llm/README.md` (NEW),
  `wiki/_meta/requirements-online.txt` (NEW, also retro-documents `sentence-transformers`),
  `wiki/_meta/.gitignore` (EDIT).
- `wiki/_meta/tests/cost_probe.py` (NEW) — stubbed-response token/$/latency + `BudgetExceededError`
  probe.
- `selftest.py` (EDIT) — `llm.py`/`cost.py` degrade with libs absent; no top-level 3rd-party import;
  default config has no non-loopback host.
**Exit criteria:** with `litellm` absent OR `WIKI_LLM=off`, everything behaves as Phase 1; with a
local Ollama running + `WIKI_LLM=local`, `llm.complete()` returns from `qwen2.5`; `cost_probe.py`
green; `selftest.py` green.

### Phase 3 — Measured generation cost in eval (optional)
**Goal:** the GENERATION cost column.
**Changes:**
- `eval.py` (EDIT) — `--measure-llm`: per case, feed the assembled context into `cost.measure()`;
  record `gen_*`; print the "LLM-CALL COST (n/a offline)" block; `cached` column. Recall path
  **untouched** and **never routed through any graph**.
- `cost.py` (EDIT) — `measure()` wraps `llm.complete()`, pulls `resp.usage` +
  `resp._hidden_params['response_cost']`/`completion_cost`, latency, `cache_hit`; writes
  `_meta/eval/cost_report.json`.
- `selftest.py` (EDIT) — `eval.py` exits 0 with `WIKI_LLM` unset and orchestration deps absent.
**Exit criteria:** offline run prints `n/a (offline)` and recall numbers unchanged; with a local
model, measured tokens/$/latency appear; `$0.00 unpriced/local` honestly tagged.

### Phase 4 — LangGraph QUERY graph + LCEL leaf (optional dep)
**Goal:** the programmatic, faithful mechanization of the QUERY prose op.
**Changes:**
- `wiki/_meta/wikikb/graph/__init__.py`, `state.py` (TypedDict `WikiState`), `tools.py` (thin LangChain
  `Tool` wrappers over `kb`/`route`/`expand`/`embed`), `nodes.py`, `query_graph.py` (NEW).
  `build_query_graph()` does its langgraph imports **inside the factory**. `confidence_gate_node`
  **imports** `lint.page_gate_verdict` (H2/H3) + `gate_probe.gate_verdict` (H1) — never
  re-implements. `synthesize_node` = LCEL `ChatPromptTemplate | ChatLiteLLM(model=..., api_base=...)
  | parser`, `temperature=0`. `SqliteSaver` checkpoint at `_meta/.checkpoints/query.sqlite`.
- `selftest.py` (EDIT) — `import graph.query_graph` stdlib-safe (no eager dep); invoking the graph
  with `WIKI_LLM` unset stops before `synthesize` (default-off proof); a probe asserts the graph's
  gate verdict == `lint.page_gate_verdict`.
- `CLAUDE.md`, `AGENTS.md`, `.opencode/agent/wiki.md`, `.opencode/command/query.md`,
  `.skills/wiki-query/SKILL.md` (EDIT) — document the optional runner; `webfetch:false` unchanged.
**Exit criteria:** graph importable with deps absent; default-off run = today's behavior;
gate-verdict probe green; with a local model, the full QUERY graph answers and writes a
`cost_report.json` ledger entry.

### Phase 5 — INGEST graph + optimization pass (optional)
**Goal:** the INGEST loop as a graph; turn on the cost levers.
**Changes:**
- `wiki/_meta/wikikb/graph/ingest_graph.py` (NEW) — `manifest.status → (empty? END) → find-or-create
  page (LCEL leaf) → provenance-assign → manifest.record → loop`; calls `crosslink.py`/`index.py` as
  nodes.
- `cost.py`/`llm.py` (EDIT) — enable `litellm.cache = Cache(type="disk", ...)`; `32b→7b` routing +
  fallback; budget-guard short-circuit node.
- `lint.py --status` (EDIT) — surface a per-domain budget/spend table from the local ledger (additive
  to STATUS; no new entry point).
- `CLAUDE.md` (EDIT) — record the deferred items explicitly out of scope: LiteLLM **proxy** + virtual
  keys, semantic caching beyond disk, cloud routing.
**Exit criteria:** INGEST graph round-trips a source offline (extractive) and with a local model;
repeated QUERY is a $0/cache-hit; `lint.py --status` shows the spend table; full `selftest.py` +
`eval.py` + both gate probes green offline.

---

## 9. File-by-file change table

| Path | Change |
|---|---|
| `wiki/_meta/wikikb/cost.py` | **NEW** — token/$/latency oracle; vendored-tokenizer (by path) + bundled-price-JSON, `embed.py` degradation contract; `UsageRecorder`; `measure()`. The spine. |
| `wiki/_meta/wikikb/llm.py` | **NEW** — LiteLLM-SDK gateway, local-Ollama default, `WIKI_LLM` gate, provider allowlist + loopback check, telemetry off; `embed.py` twin. |
| `wiki/_meta/tests/cost_probe.py` | **NEW** — stubbed-response cost/budget probe (analogue of `gate_probe.py`). |
| `wiki/_meta/wikikb/graph/__init__.py` | **NEW** — package. |
| `wiki/_meta/wikikb/graph/state.py` | **NEW** — `WikiState` TypedDict. |
| `wiki/_meta/wikikb/graph/tools.py` | **NEW** — thin LangChain `Tool` wrappers over `kb`/`route`/`expand`/`embed` (read-only; no logic). |
| `wiki/_meta/wikikb/graph/nodes.py` | **NEW** — node fns; gate node **imports** `lint.page_gate_verdict` + `gate_probe.gate_verdict`. |
| `wiki/_meta/wikikb/graph/query_graph.py` | **NEW** — `build_query_graph()` StateGraph (factory-local langgraph import); LCEL `synthesize` leaf; `SqliteSaver`. |
| `wiki/_meta/wikikb/graph/ingest_graph.py` | **NEW** — `build_ingest_graph()` manifest-gated loop. |
| `wiki/_meta/wikikb/evaluate.py` | **EDIT** — route cost through `cost.py`; keep `ctx_t` proxy + `CHARS_PER_TOKEN` fallback; add `--measure-llm`, `--budget-tokens`, `--budget-usd`; two cost blocks + calibration ratio + gate-fire-rate; recall path unchanged and never graph-routed. |
| `wiki/_meta/tests/selftest.py` | **EDIT** — graceful-degrade checks for `cost`/`llm`/`graph`; no-top-level-import grep; no-non-loopback-host check; gate-verdict==`lint` probe; `eval` exits 0 offline. |
| `wiki/_meta/wikikb/lint.py` | **EDIT (Phase 5 only)** — `--status` per-domain budget/spend table from the local ledger. Gate rule, `len//4`, all scanners **untouched**. |
| `wiki/_meta/llm.config.yaml.sample` | **NEW** — committed sample (local model, loopback `api_base`, budgets, allowlist; proxy notes as deferred). |
| `wiki/_meta/llm/README.md` | **NEW** — offline Ollama bring-up + vendoring (parallels `models/README.md`). |
| `wiki/_meta/cost/README.md` | **NEW** — vendored-tokenizer + bundled-price-JSON + env vars. |
| `wiki/_meta/requirements-online.txt` | **NEW** — pinned optional `litellm`/`langgraph`/`langchain-core`; retro-documents `sentence-transformers`+`numpy`; offline-wheel + compiled-wheel-arch caveat. |
| `wiki/_meta/.gitignore` | **EDIT** — ignore `llm.config.yaml`, `wheels/`, `.llm_cache/`, `cost_report.json`, `.checkpoints/`; keep READMEs. |
| `wiki/_meta/eval/cost_report.json` | **NEW (generated, gitignored)** — run-total ledger. |
| `wiki/CLAUDE.md` | **EDIT** — Optional online tier note (QUERY + Tooling); `cost.py`/`llm.py` in the tooling list; deferred-proxy note. |
| `wiki/_meta/wikikb/embed.py` | **EDIT (header comment only)** — extend "the ONLY 3rd-party dep" line. |
| `AGENTS.md`, `.opencode/agent/wiki.md` | **EDIT** — optional local gateway; `webfetch:false` unchanged. |
| `.opencode/command/query.md`, `.skills/wiki-query/SKILL.md` | **EDIT** — optional LangGraph runner is an alternative, not a replacement. |
| `kb.py`, `route.py`, `expand.py`, `manifest.py`, `crosslink.py`, `index.py`, `tags.py`, `gate_probe.py`, `gate_page_probe.py` | **UNCHANGED** — load-bearing deterministic tools; wrapped as nodes, never re-implemented or LLM-ified. |

---

## 10. Risks + mitigations, and OPEN QUESTIONS

### Risks → mitigations
1. **`tiktoken` network download via `litellm.token_counter`** *(the #1 fatal flaw across
   critiques).* → **Never call `token_counter`.** Tokenize with a vendored-by-path tokenizer (§5.2);
   read `$` from the bundled JSON directly. Selftest network-tripwire asserts no socket on a cost run.
2. **Dependency weight** — `litellm`+`langgraph`+`langchain-core` pull a large, partly **compiled
   (Rust)** transitive tree (`tiktoken`/`tokenizers`/`pydantic-core`); the offline wheelhouse is an
   order of magnitude past `embed.py` and **arch-fragile**. → Strictly optional; base repo stays
   zero-pip; Phases 0–3 need **no** heavy dep; `requirements-online.txt` documents the cross-arch
   wheel caveat. **Phases 4–5 are genuinely optional** — a team that only wants measured cost can
   stop at Phase 3.
3. **Air-gap downgraded from structural to configurational on the gateway** — `litellm.completion`
   *is* a network client; loopback safety rests on config + flags a future version could regress. →
   Default-off + double-opt-in for remote + telemetry-off + selftest config assertion. Structurally,
   the **only** socket is loopback; the tokenizer/price paths are kept structurally offline.
4. **Two cost columns confuse readers** — proxy vs measured measure different things. → Deliberate;
   the calibration ratio links them and keeps the cheap proxy honest. Documented in eval output +
   `cost/README.md`.
5. **`$0.00` for local models reads as "cost tracking does nothing."** → Lead with **tokens +
   latency** (the real local budget); `$` is a tagged what-if for hosted capacity planning, with an
   optional registered shadow rate.
6. **Prose↔graph drift** (the QUERY op now exists in `CLAUDE.md` prose *and* `query_graph.py`). → The
   graph is positioned as a *faithful mechanization* (CLAUDE.md stays the contract); `synthesize` is
   the only LLM node; a selftest probe asserts graph-gate-verdict == `lint.page_gate_verdict`. **eval
   recall never runs through the graph** (stays the verified stdlib replay).
7. **Eager-import regression** breaks `import graph.query_graph` offline. → Factory-local langgraph
   imports + a selftest grep banning top-level 3rd-party imports.
8. **Local-model nondeterminism pollutes the amortized cache.** → `temperature=0`, disk cache keyed
   on assembled context, `file_back` gated on the same Confidence checks `lint` enforces.

### OPEN QUESTIONS for the user
1. ~~**Stop at Phase 3?**~~ **RESOLVED (2026-06-23):** full Phase 0–5 migration is the target
   (LangGraph adopted as planned), but **implementation is deferred** — this plan is approved as the
   reference, no code yet. Phases 0–3 still stand as the dependency-light, model-free *first
   increment* to ship when work begins; Phases 4–5 add the LangGraph orchestration on top.
2. **Vendored tokenizer choice.** Vendor the **exact Ollama model's `tokenizer.json`** (most
   accurate, per-model) or **reuse `embed.py`'s already-vendored ST tokenizer** (zero extra
   vendoring, approximate)? Affects accuracy vs offline-bundle size.
3. **Default local model id.** `ollama/qwen2.5:32b` is assumed from the design's ~27B target. Confirm
   the model + endpoint (Ollama `:11434` vs vLLM `:8000/v1`), and whether a 7b router/summarizer
   model is available for the routing/fallback optimization.
4. **Shadow `$` rates for local inference?** Register a compute-cost-per-token so the `$` column is
   meaningful offline, or leave it `$0.00 unpriced/local`?
5. ~~**Remote fallback policy.**~~ **RESOLVED (2026-06-23):** `WIKI_LLM_ALLOW_REMOTE` **stays** as a
   loud, logged double-opt-in (default local-loopback-only). The cloud path is **not** structurally
   removed — it's an explicit escape hatch for hosted models + real $ cost when deliberately enabled.
6. **CI cost mode.** Should CI run the **proxy/heuristic** number (deterministic, model-free —
   recommended) and reserve measured-token runs for an occasional calibration job, or gate on
   measured tokens (requires a vendored tokenizer in CI)?
