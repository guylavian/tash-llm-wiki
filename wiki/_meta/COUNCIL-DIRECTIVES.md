# PRE-EXECUTION DIRECTIVES — LiteLLM / LangGraph / Cost Migration

**Convened:** LLM Council (5 members + cross-reviews) → Chairman synthesis · **Date:** 2026-06-23
**Binds:** the implementer of `wiki/_meta/MIGRATION-litellm-langgraph.md`. **Where this document and
the plan disagree, this document governs.** Every numeric/structural claim was re-verified by the
chairman against the source; disputed digits were re-run on the real `cases.jsonl` (19 cases).

> Captured baseline (this box, 2026-06-23): `selftest.py` = **9/11** (pre-existing reds: check #4
> `lint --strict`, check #6 `crosslink` 12 unresolved kb tokens). `lint --strict` rc=1. Golden eval
> outputs committed at `_meta/eval/baseline.eval{,.route,.graph}.out`. **"selftest green" is struck
> from every phase exit criterion → replaced with "no NEW failures vs the 9/11 baseline."**

---

## 1. GO / NO-GO

**Overall: GO — with blocking corrections.** Architecture sound (eval imports the real tools; recall
kept off the graph; offline-degrade mirrors `embed.py`; air-gap = local loopback + opt-in-remote
double-gate). But the plan's Phase-0 "byte-identical" claim is arithmetically false as written, and
two faithfulness invariants are violated. All fixes are small but load-bearing.

| Phase | Verdict | Clears when |
|---|---|---|
| 0 | NO-GO until re-specced | float `proxy_tokens` (BF-1) + golden-stdout selftest (BF-2) |
| 1 | NO-GO until re-specced | drop hallucinated `embed.tokenizer_count` tier (BF-3) |
| 2 | GO w/ fixes | env-ordering (BF-5), IP loopback enforce (BF-6), pinned reqs (BF-7) |
| 3 | GO w/ fixes | defensive `_hidden_params`/tuple `cost_per_token` (BF-8); budget in cost.py (BF-9) |
| 4 | NO-GO until re-specced | 5-arm gate via one lint fn + real `question_tier` (BF-4); pkg (BF-7); probe via `lint.parse_frontmatter` (BF-10); CUT tools.py+state.py+SqliteSaver |
| 5 | GO w/ fixes + cuts | lazy/guarded ledger in `lint --status` (BF-11); disk-cache deferred |

---

## 2. BLOCKING MUST-FIXES

**BF-1 — Phase 0 byte-identical: `count_tokens` must be FLOAT on the proxy path.** Verified: default
"mean TOTAL ctx tokens" flips 98325→98324 with integer floor; 6/19 verbose lines flip. Rule: *float,
not floor*. `cost.py` exposes TWO functions, never collapsed:
- `proxy_tokens(n_chars:int)->float` = `n_chars / CHARS_PER_TOKEN` — wired into `eval.py:175-177`, MUST NOT floor.
- `count_tokens(text:str, model=None)->int` — real per-string count for the MEASURED path ONLY (Phase 1+); never wired to the proxy.
`eval.py:175-177` → `idx_t=cost.proxy_tokens(index_bytes(...))`, `snip_t=cost.proxy_tokens(SNIPPET_CHARS)*scanned`, `body_t=cost.proxy_tokens(sum(opened_bodies))`. (Granularity irrelevant once float; snippet site `260/4==260//4` never breaks.)

**BF-2 — Phase 0 tripwire.** Capture today's output to committed fixtures BEFORE wiring:
`_meta/eval/baseline.eval{,.route,.graph}.out`. Selftest runs eval (default, `--route`, `--graph`)
with `WIKI_LLM` unset + no tokenizer and asserts **stdout == fixture byte-for-byte**. New checks
additive; record the 2 known reds in a comment.

**BF-3 — `embed.tokenizer_count` does NOT exist.** Drop tier-2. `count_tokens` is TWO-tier: tier-1 =
vendored `tokenizer.json` by path via `len(tok.encode(text).ids)`; tier-3 = `len(text)//CHARS_PER_TOKEN`.
List `tokenizers` (Rust wheel) in `requirements-online.txt` as compiled/arch-fragile.

**BF-4 — Gate node covers only 3 of 5 arms; H1 has no input producer.** `page_gate_verdict(fm)` =
H2/H3 only. H4 (`status==needs-review`) and Provisional-L are in NEITHER imported fn. `route.route()`
returns `(domains, confident)` — a domain, not a tier; no free-text `question_tier` classifier exists.
Fix (both required):
1. Consolidate all 5 arms into ONE lint-exported `gate_banner(fm, question_tier=None, covered=None)->list[str]`
   that calls `page_gate_verdict(fm)` (H2/H3, unchanged, MOC-exempt H2) then appends H4
   (`status=='needs-review'` fires ALONE), Provisional-L (`status!='reviewed' and isinstance(prov,dict)
   and inf>=ext and (ext or inf)`), and H1 (only when `question_tier` & `covered` supplied, via
   `gate_probe.gate_verdict`). MOC carve-out stays scoped to H2 only. **Do NOT extend `page_gate_verdict`
   in place** (keeps `gate_page_probe.py` text valid) — add arms in the wrapper.
2. H1 input: node does NOT classify; caller/host passes `question_tier`; node reads
   `gate_probe.load_tiers_covered()[domain]` for `covered`. Document: graph applies H2/H3/H4/L
   deterministically over frontmatter, H1 only when a `question_tier` is supplied. No classifier introduced.

**BF-5 — Price-map env at MODULE TOP LEVEL.** `LITELLM_LOCAL_MODEL_COST_MAP` is read at litellm
import time. In `llm.py` set `os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP","True")` at module
top (pure stdlib, no 3rd-party import). Attr toggles (`litellm.telemetry=False`, `success_callback=[]`,
`suppress_debug_info=True`) set inside the fn immediately after the lazy `import litellm`, before any
`completion()`. Network tripwire must fire on first `import litellm`.

**BF-6 — Loopback enforcement IP-based + allowlist, before the call.** Substring check insufficient
(bare `model="gpt-4o"` has no `api_base`). Two gates before any `completion()` (both pass unless
`WIKI_LLM_ALLOW_REMOTE=1` AND provider key env present): (1) model provider prefix ∈ allowlist; (2)
`api_base` host loopback via `urllib.parse` + `ipaddress.ip_address(host).is_loopback` (accept
127.0.0.1/::1/localhost); reject non-loopback literal host and reject a bare cloud model with no
`api_base`. vLLM: set dummy `api_key="sk-noop"`.

**BF-7 — `requirements-online.txt` packaging.** Pin EXACT (`==`); re-verify each symbol vs the pinned
version before coding. `SqliteSaver` is in `langgraph-checkpoint-sqlite` (`from_conn_string`, not
`SqliteSaver(path)`) → DROPPED (use MemorySaver/none). `ChatLiteLLM` is in `langchain-litellm`
(community deprecated) → CUT (no langchain). README mandates `pip download --platform <triple>
--python-version <X.Y> --implementation cp --only-binary=:all:` on the networked box; document target triple.

**BF-8 — Defensive response parsing (never KeyError).** `hp = getattr(resp,"_hidden_params",{}) or {}`;
`gen_cost = hp.get("response_cost")`; `cached = hp.get("cache_hit",False)`. `cost_per_token` returns a
TUPLE `(prompt,completion)` — destructure & sum. Prefer guarded `litellm.completion_cost(resp)`.
Unpriced local → `gen_cost=None` tagged `unpriced/local` (ollama/* likely has NO price entry → no
lookup, not $0.00).

**BF-9 — Budget gate in `cost.py`, not `litellm.max_budget`.** Pure stdlib comparison raising your own
exception (and `eval.py --budget-tokens` exit code 3 — verified free; only 0/2 used today). `cost_probe.py`
asserts YOUR check raises on an over-budget stubbed usage dict. Budget compares against the SAME float
proxy mean `eval` prints (BF-1).

**BF-10 — Faithfulness probe via `lint.parse_frontmatter` (dual-representation hazard).** Verified:
`selftest.py` check #11 duplicates the rule inline AND reads `fm['_provenance']` (nested) → `None` on
live flat-key pages → silently misses H3, disagreeing with `page_gate_verdict` (which reads flat keys
via `provenance_of`). Fix: (1) Phase-4 probe builds `fm` via `lint.parse_frontmatter(text)` and asserts
`graph verdict == lint.gate_banner(fm,…)`. (2) Opportunistically fix selftest #11 to call
`lint.gate_banner`/`page_gate_verdict` instead of its inline copy.

**BF-11 — `lint --status` spend table lazy + guarded; NO module-scope cost import in `lint.py`.** Read
`cost_report.json` inside the `--status` block; missing → "(spend table unavailable)" and continue.
LINT/STATUS stays stdlib-only and green when the online tier was never installed.

---

## 3. CONFIRMED EXTERNAL API SURFACE (pin + re-verify; all libs ABSENT on this box)

| Symbol | Verdict | Directive |
|---|---|---|
| `litellm.completion(model,api_base,messages)` | standard | USE; verify ollama loopback on pinned ver |
| `litellm.token_counter` | EXISTS | **NEVER CALL** (tiktoken download). Vendored tokenizer instead |
| `litellm.completion_cost(resp)` | plausible | USE guarded, best-effort |
| `litellm.cost_per_token(...)` | returns TUPLE | destructure & sum |
| `litellm.register_model` | plausible | DEFER (shadow-$ cut) |
| `litellm.cache=Cache(type='disk',...)` | kwarg version-fragile | DEFER (cut/best-effort) |
| `litellm.max_budget`/`BudgetExceededError` | doubtful on bare SDK | budget in cost.py (BF-9) |
| `resp.usage.prompt_tokens/completion_tokens` | OpenAI-shaped likely | USE |
| `resp._hidden_params['response_cost'\|'cache_hit']` | private, absent for local | `.get()` only (BF-8) |
| `litellm.telemetry/success_callback/suppress_debug_info`/`LITELLM_LOCAL_MODEL_COST_MAP` | offline knobs | BF-5 |
| bundled `model_prices_and_context_window.json` | path version-fragile | `importlib.resources`/`find_spec`, best-effort → unpriced/local |
| `langchain ChatLiteLLM` | langchain-litellm, NOT core | **CUT** — direct `llm.complete()` |
| LCEL `ChatPromptTemplate/RunnableLambda` | core | framework **CUT** (plain node fn) |
| `get_openai_callback` | $0 for ollama | borrow shape only; read `resp.usage` |
| `langgraph StateGraph/add_conditional_edges/END`/TypedDict | stable | USE |
| `langgraph SqliteSaver` | separate pkg, ctx-mgr ctor | **CUT** → MemorySaver/none |
| `embed.tokenizer_count` | **DOES NOT EXIST** | remove (BF-3) |
| `lint.page_gate_verdict(fm)->list[str]` | **VERIFIED** H2/H3 | import; extend via `gate_banner` (BF-4) |
| `gate_probe.gate_verdict(question_tier,covered)` | **VERIFIED** H1 | import; needs supplied tier (BF-4) |
| `route.route(query)->(domains,confident)` | **VERIFIED** domain not tier | not a tier classifier |

---

## 4. CORRECTED PER-PHASE SPEC (exit tests)

- **P0** — `cost.py`(NEW: `proxy_tokens`→float, `count_tokens`→int heuristic-only, `have_library`/`available`→False, `status_str`→"heuristic", `UsageRecorder`), `eval.py`(wire 175-177 to proxy_tokens; `--budget-tokens`/`--budget-usd` exit 3 on float proxy mean), `selftest.py`(golden diff), `_meta/eval/baseline.eval*.out`(committed). **Budget micro-step lands FIRST.** Tests: eval default/route/graph == golden byte-for-byte; `proxy_tokens(17003)==4250.75` (not 4250); `import cost` with libs absent; `--budget-tokens <tiny>` exits 3, default exits 0 unchanged.
- **P1** — `cost.py`(two-tier count_tokens + guarded bundled-price reader → unpriced/local), `eval.py`(calibration caption), `_meta/cost/README.md`. Tests: no tokenizer → byte-identical to P0 golden; with tokenizer → real tokens; network tripwire green (monkeypatch socket; assert none on count_tokens AND first `import litellm`).
- **P2** — `llm.py`(NEW), `llm.config.yaml.sample`, `llm/README.md`, `requirements-online.txt`(pinned, retro-doc ST+numpy), `.gitignore`(add artifacts; mirror `dir/* + !dir/README.md` for cost/ + llm/), `cost_probe.py`. `llm.available()` = lib AND config AND `WIKI_LLM!=off` — NO live socket probe (`--probe` for active). Env at top (BF-5); IP loopback+allowlist (BF-6). Tests: degrade with libs masked-absent (subprocess); grep: no module-scope 3rd-party import under `_meta/wikikb/`; cloud api_base/bare cloud model rejected unless ALLOW_REMOTE+key; network tripwire on first import.
- **P3** — `eval.py`(`--measure-llm`, `gen_*` block, `cached` col; recall untouched, cost computed AFTER recall row), `cost.py`(`measure()` wraps `llm.complete()`, defensive BF-8, writes cost_report.json), `selftest.py`. Tests: offline → `n/a (offline)`, recall == P0 golden; eval exits 0 with langgraph/langchain/litellm masked-absent (incl. hidden `cases[:1]` hybrid pre-pass); cost_probe stub → well-formed dict, no KeyError; over-budget stub raises.
- **P4 (RESCOPED)** — `graph/__init__.py`, `graph/nodes.py`, `graph/query_graph.py`. CUT `tools.py`+`state.py` (nodes call kb/route/expand/embed directly; merge WikiState into query_graph). `build_query_graph()` imports langgraph inside factory. `synthesize_node` = plain fn calling `llm.complete()` (no LCEL). `confidence_gate_node` imports `lint.gate_banner`. No SqliteSaver → MemorySaver/none. Tests: `import graph.query_graph` with libs absent; grep no module-scope 3rd-party; default-off stops before synthesize; faithfulness probe: `fm=lint.parse_frontmatter(text)`, gate verdict == `lint.gate_banner(fm,q_tier,covered)` across H2/H3 AND H4 (needs-review+grounded — a case page_gate_verdict alone returns [] for) AND L AND H1 (`(active-directory,support-kb)→out-of-coverage`).
- **P5 (RESCOPED)** — `graph/ingest_graph.py`(manifest-gated loop), `lint.py`(`--status` spend table lazy/guarded — BF-11), `CLAUDE.md`(deferred items). Disk-cache deferred; 32b→7b routing kept. Keep approved order (QUERY=graph; do NOT reorder). Tests: INGEST round-trips offline; `lint --status` shows table when report exists, "(unavailable)" when absent, non-status output unchanged; no NEW selftest failures; gate probes green.

---

## 5. VALUE CUTS (kept cut — value/over-engineering reviewer enforces)
1. **CUT LangChain entirely** (LCEL + ChatLiteLLM) — `synthesize_node` = plain node fn over `llm.complete()`.
2. **CUT `graph/tools.py`** — nodes call stdlib tools directly (that IS the faithfulness contract).
3. **MERGE `graph/state.py`** into `query_graph.py` (one TypedDict).
4. **DROP SqliteSaver** → MemorySaver/none (gate is deterministic; nothing to checkpoint).
5. **DEFER `litellm.cache`** disk caching (wiki already amortizes via filed questions/; temperature=0 ≠ bit-stable on local GPU).
6. **DROP shadow $-rate** (`register_model`) — lead with tokens+latency; local `$` = `unpriced/local`.
7. **Calibration ratio** kept but does NOT gate P0–3 acceptance.

---

## 6. STANDING POST-PHASE CODE-REVIEW CHARTER (6 distinct purposes; ≤2 per reviewer)
1. **Byte-identical / regression guardian** — diff eval (default+route+graph) vs golden; recall unmoved; no NEW selftest fail vs 9/11. (BF-1/BF-2)
2. **Air-gap / network tripwire auditor** — grep module-scope 3rd-party imports; socket-block monkeypatch over first-import AND cost/tokenizer; env-at-top ordering; IP-loopback+allowlist (incl. bare cloud id reject). (BF-5/BF-6)
3. **External-API reality checker** — every litellm/langgraph/langchain symbol exists in pinned source; tuple destructure; `_hidden_params.get()`. (BF-7/BF-8/§3)
4. **Faithfulness lock** — gate verdict == `lint.gate_banner(lint.parse_frontmatter(text),…)` across 5 arms; graph wrappers == direct-call; eval recall never imports graph; `fm` never hand-built. (BF-4/BF-10)
5. **Degradation contract reviewer** — `import cost`/`llm`/`graph.query_graph` stdlib-safe libs-masked; `complete()`/`measure()` never raise; `lint --status` green when report absent + no module-scope cost import. (BF-9/BF-11)
6. **Value / over-engineering challenger** — every new file/dep/knob names a concrete consumer; §5 cuts stayed cut; flag creep toward LCEL/SqliteSaver/tools.py/shadow-rate.
