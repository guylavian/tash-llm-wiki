# Keycloak / RHBK knowledge base — agent instructions

This folder is an offline Keycloak / Red Hat build of Keycloak (RHBK) knowledge
base with three layers. Use it to answer Keycloak/RHBK questions instead of
guessing or going to the internet.

## Layers
- **Wiki** (`wiki/`) — LLM-maintained, cross-linked synthesis. **Start here.**
  - Read `wiki/CLAUDE.md` first — it's the schema + ingest/query/lint workflow.
  - Entry point: `wiki/index.md`. Pages cross-link with `[[slug]]` (bare slug,
    matches a file under `wiki/topics/` or `wiki/entities/`, no path/`.md`).
- **Raw tiers (in-vault, IMMUTABLE)** — the harvested corpus is folded into the vault
  as reference notes under `wiki/reference/keycloak/` (800 doc bodies + a gated-KB
  pointer index = 1,840 records), plus the 12 `references/` guides. Cited by wiki
  pages; never edit.

## How to answer a Keycloak/RHBK question
1. Search `wiki/` first — read `wiki/index.md`, then the matching topic/entity page,
   and follow `[[links]]`.
2. If the synthesized pages are thin, search the in-vault reference tier: grep
   `wiki/reference/keycloak/`, or `python3 wiki/_meta/bin/kb.py --domain keycloak
   search "<terms>"` (add `--primary` / `--guide <slug>` to narrow, `--gated` for
   Red Hat login-only pointers).
3. Synthesize the answer and cite the source (`kb:<id>`, `guide:<slug>`,
   `ref:<file>`).
4. Optionally file the answer back per `wiki/CLAUDE.md` (QUERY operation) so the
   wiki compounds.

## Operations (packaged skills + OpenCode commands)
The wiki's maintenance ops are packaged so they run in OpenCode (and Claude Code):
- **Agent Skills:** `.skills/wiki-ingest`, `.skills/wiki-query`, `.skills/wiki-lint`,
  `.skills/wiki-status`. For OpenCode, expose them by symlinking/copying into
  `~/.agents/skills/` (this `AGENTS.md` is the bootstrap that names them).
- **OpenCode commands/agent:** `.opencode/agent/wiki.md` + `.opencode/command/`
  (`/ingest`, `/query`, `/lint`, `/status`).
- These are **thin pointers**; `wiki/CLAUDE.md` is the single source of truth.
- **Tooling** (stdlib only, air-gapped) is in `wiki/_meta/bin/`:
  - `python3 wiki/_meta/bin/lint.py [--status]` — health check + delta-manifest audit
  - `python3 wiki/_meta/bin/manifest.py {seed,status,record}` — the delta manifest
    (`wiki/_meta/.manifest.json`): only ingest new/changed sources.

## Hard rule
Ingest/query operations may create or edit pages in the **synthesis layer**
(`wiki/{topics,entities,questions}/`) only. Never edit the immutable raw tiers
(`wiki/reference/`, `references/`) — regenerable ground truth. Offline only: no
network, no `webfetch`; retrieval is grep over the vault (or
`python3 wiki/_meta/bin/kb.py --domain <d> search`).
