# Agent instructions — multi-domain LLM wiki (this repo IS the vault)

This repo root is an Obsidian vault: an LLM-maintained, offline knowledge wiki
(keycloak / active-directory / openshift / cisco-ios-xe). Use it to answer
questions instead of guessing or going to the internet.

- **For a QUERY, read `QUERY-CARD.md`** — the extracted per-query protocol
  (budget directives + the QUERY operation). Read `CLAUDE.md` (the full schema)
  only for INGEST / ADD-DOMAIN / page-editing operations.
- Entry point: `index.md` (global router) → `index.<domain>.md`. Pages
  cross-link with `[[slug]]` (bare slug under `topics/` or `entities/`).
- Raw ground truth lives in-vault: `reference/<domain>/` (folded-in corpus
  notes) + `references/` (curated guides, `ref:` tier) + `_sources/<domain>/`
  (notes-first domains). Cited by wiki pages; **never edit** — immutable.
- Tooling (stdlib, air-gapped) is the `wikikb` package under `_meta/`:
  `python3 -m wikikb {ask,kb,route,expand,lint,manifest,index,card,build,tkg,…}`
  run from `_meta/` (or `PYTHONPATH=<repo>/_meta`). MCP stdio server:
  `python3 -m wikikb mcp` (tools: wiki_ask / wiki_search / wiki_route / wiki_read_page;
  only wiki_ask can write — file_back=true files a questions/ draft).
- Every page carries `summary:`, two-tier `sources:`, and per-claim
  `provenance:` counts (`extracted`/`inferred`/`ambiguous`) — never fabricate them.

## Hard rules
- Writes go **only** to the synthesis layer (`topics/` `entities/` `questions/`) —
  never edit the immutable `reference/`, `references/`, or `_sources/` tiers.
- Offline only: no network, no webfetch; retrieval is grep over the vault or
  `python3 -m wikikb kb --domain <d> search`.
- Never serve inference as fact — the Confidence gate + identifier guard in
  `wikikb ask` are the enforcement; obey their banners verbatim.
