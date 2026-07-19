# Roadmap

## Landed
- Stdlib-only retrieval (route/search/expand), lint + Confidence gate, delta manifest.
- Optional dense retrieval (embed.py), graph-expansion (expand.py), the temporal
  knowledge graph (tkg/, JSON-store canonical), graph-by-default `ask`, and the
  cited/gated serve + MCP pipeline.
- Optional online tier (LiteLLM gateway, LangGraph orchestration) — off by default,
  local-first, graceful degradation verified by selftest.py.

## Now
- Versioned home for Claude Code commands/agents (S9/N11 in
  `_meta/DEEP-RESEARCH-2026-07-19.md`).
- A `<60s` fast test tier + a minimal CI pipeline (S7/S8, design in the same report).
- Strip dead Kuzu/Graphiti config from docker-compose.yml/Dockerfile (N1 — the
  backend was deleted 2026-07-05, the Docker image still installs it).
- Stale README numeric claims (N2) — generate counts mechanically instead of
  hand-maintaining prose.
- Citation-grounding lint false positives (S3b) — exclude `<...>` placeholder
  syntax and literal metadata values from the distinctive-token heuristic.

## Later
- A measured hybrid (lexical+dense) baseline committed alongside the lexical ones (N3).
- Auth/rate-limiting story for `serve` when bound off loopback (N4).
- Wire grade300's exit code into CI once it exists (N8); a case-count floor check.
- Atomic writes for the tkg JSON store (N6).
- Ingest the 4 PENDING references (admin-rest-api, authorization-services,
  observability, server-development) — cited nowhere yet per manifest status.
