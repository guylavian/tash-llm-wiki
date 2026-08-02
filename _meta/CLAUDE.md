# `_meta/` toolchain — optional subsystems

Loaded only when working under `_meta/`. Both tiers below are OFF by default;
with them absent the wiki behaves identically. Moved out of the root `CLAUDE.md`
2026-08-02 to keep always-loaded context lean — this is the single source of
truth for these two subsystems.

### Optional online tier (LiteLLM + LangGraph) — OFF by default, local-first

On top of the stdlib tools sits an **optional, off-by-default** measurement/orchestration tier that
follows the `embed.py` precedent exactly (lazy import, behind a flag, vendored offline, graceful
degradation). With it
absent or `WIKI_LLM` unset, the wiki behaves **identically to today** — the host runtime drives the
prose ops; the deterministic retrieval/eval/gate tools are unchanged.

- **`cost.py`** — token/$/latency accounting. `proxy_tokens()` (FLOAT) is the retrieval context-cost
  proxy `evaluate.py` already prints (byte-identical to the old `chars/4`); `count_tokens()` (vendored
  tokenizer, else heuristic) + `measure()` are the **measured generation** path, active only under
  `python3 -m wikikb evaluate --measure-llm`. Real tokens/$ never touch the retrieval proxy.
- **`llm.py`** — the LiteLLM gateway. Defaults to a **local loopback** Ollama/vLLM endpoint; a
  loopback+allowlist gate refuses any non-loopback model unless the explicit double opt-in
  (`WIKI_LLM_ALLOW_REMOTE=1` **and** a provider key). Returns None when off/absent → callers fall back
  to the deterministic/extractive answer. Never opens a socket on import.
- **`graph/`** — `query_graph.py` / `ingest_graph.py` mechanize QUERY/INGEST as **LangGraph**
  StateGraphs (the gate node imports `lint.gate_banner` — the SAME 5-arm Confidence gate `lint`
  enforces and the probes assert; no re-implementation). **Graph by default (2026-07-09):** `ask`
  (and every surface built on it — serve/mcp/livebank/faithfulness) orchestrates through the
  compiled StateGraph whenever `langgraph` is installed, and degrades to the same nodes sequenced
  linearly when it is absent (`ask --graph` = strict mode, fail instead of degrade). `langgraph`
  is still imported only inside the factory, so the modules import stdlib-safe (air-gap invariant)
  and offline behavior is byte-identical.
  **Table-safe context cap** — the synthesis context (`graph/nodes.py`) is assembled whole-line-only
  up to `CTX_CHARS`; a cut that would clip a markdown table/list stops at the row boundary and
  appends an explicit `[…context truncated mid-table — open <note> for the full table]` marker, so a
  numeric row is never half-served silently (all `ask` surfaces — CLI/serve/mcp/LangGraph — share
  this assembler). Numeric tables and rate/threshold values must be quoted VERBATIM from the page or
  note in any host synthesis — table re-generation is where numbers get dropped.
- **`python3 -m wikikb evaluate --measure-llm`** adds a measured generation tokens/$/latency block (prints `n/a (offline)`
  when the gateway is inactive); `--budget-tokens` / `--budget-usd` fail CI (exit 3) on a cost
  regression. **Recall never runs through the graph or the gateway.**
- **`lint.py --status`** appends an LLM-spend table read directly from the regenerable
  `_meta/eval/cost_report.json` ledger (no `cost`/`llm` import — LINT/STATUS stays stdlib-only).
- **Vendoring (offline):** `_meta/requirements-online.txt` + `_meta/{llm,cost}/README.md`
  (`pip download … --only-binary=:all:` on a networked box → `--no-index` on the sealed box). Config:
  `_meta/llm.config.yaml` (gitignored; copy the `.sample`).
- **Deliberately OUT of scope (deferred):** the LiteLLM **proxy server** + virtual keys, semantic /
  disk response caching beyond the wiki's own `questions/` amortization, cloud model routing, and a
  shadow `$`-rate for local models (local `$` stays `unpriced/local` — lead with tokens + latency).
- **Verification:** `selftest.py` carries the tripwires (byte-identical goldens, network/DNS block,
  no module-scope 3rd-party import, the 5-arm gate, graph offline-import, INGEST dry-run);
  `cost_probe.py` is the O(1) cost/budget probe. Network stays disabled by default (`webfetch:false`);
  the only socket the tier may open is to the operator's local loopback model.

### Temporal + cross-domain knowledge graph (`wikikb/tkg/`) — stdlib core, JSON store canonical

A downstream, **regenerable graph view** of the vault for temporal and cross-domain questions. Obsidian
stays the single source of truth; the graph is compiled from edges that *already exist*. Build it with
`python3 -m wikikb tkg ingest` (writes the derived JSON store under `_meta/tkg/`, gitignored). Five verbs:
`ingest · graph-status · cross-domain-query · provenance-trace · temporal-query`.

- **Nodes** (`WikiNode`, labels `Entity|Topic|Question|Source|Domain`): pages → Entity/Topic/Question by
  `type:`; each cited reference note → a Source; each `domain:` → a Domain.
- **Edges, deterministic only (rule R3 — NO LLM/inference):** `LINKS_TO` (page→page, from body
  `[[wikilinks]]`), `CITES` (page→Source, resolved by **reusing `crosslink.resolve()`** — primary/newest
  version wins), `IN_DOMAIN` (page→Domain). Non-`kb:` provenance (`guide:/ref:/web:/note:`) is kept on the
  Page node as `sources_raw` and surfaced by `provenance-trace` — never dropped, never an edge.
- **Two edge kinds (rule R4):** `structural` is the **hard default** (`valid_from = valid_until = None`). A
  `CITES` edge is promoted to `version-temporal` ONLY when all three hold: the reference note has a
  structured `version:` **and** `documentKind == Documentation` **and** `tkg/versions.py` returns a *usable*
  date. `valid_until` is **always None** — supersession is never inferred from version succession.
- **Temporal honesty (rules R1/R2):** `valid_from` originates **only** from `tkg/versions.py`, a curated
  registry of real, **publicly-sourced** release dates with a per-entry `precision` (`verified` = explicit GA
  announcement; `errata-confirmed` = a public RHSA/RHEA errata proving availability, a conservative lower
  bound — Red Hat's exact GA dates are paywalled; `approximate` = recorded but **excluded** from `valid_from`).
  **OMIT, NEVER FABRICATE:** no usable date ⇒ the edge stays structural. Every version-temporal edge carries
  `valid_from_precision` so `errata-confirmed` is never mistaken for an exact GA date. A Source node's version
  metadata is read **exclusively** from the immutable `reference/<domain>/` note frontmatter (a build-time
  assertion enforces the `reference/`-only path), so a synthesis page's **`updated:` can never become
  `valid_from`** — it is structurally unreachable, not merely discouraged.
- **Graphiti/Kuzu backend: REMOVED 2026-07-05.** The optional embedded-Kuzu write-side accelerator
  (`tkg/graphiti_backend.py`) was deleted after upstream Kuzu was archived (Oct 2025; Graphiti itself
  deprecated the backend) — it was verified inert here with zero consumers. The **JSON store under
  `_meta/tkg/` is canonical** and answers every query; at this graph's size (~600 nodes) a dict scan is
  milliseconds. `selftest.py` asserts the module stays gone and all five verbs run without it.

---
