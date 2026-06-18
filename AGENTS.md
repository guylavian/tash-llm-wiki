# Keycloak / RHBK knowledge base — agent instructions

This folder is an offline Keycloak / Red Hat build of Keycloak (RHBK) knowledge
base with three layers. Use it to answer Keycloak/RHBK questions instead of
guessing or going to the internet.

## Layers
- **Wiki** (`wiki/`) — LLM-maintained, cross-linked synthesis. **Start here.**
  - Read `wiki/CLAUDE.md` first — it's the schema + ingest/query/lint workflow.
  - Entry point: `wiki/index.md`. Pages cross-link with `[[slug]]` (bare slug,
    matches a file under `wiki/topics/` or `wiki/entities/`, no path/`.md`).
- **Raw corpus** (`kb/`, `references/`) — IMMUTABLE ground truth: 1,840 RHBK/RH-SSO
  records, 800 full bodies, 12 reference guides. Cited by wiki pages; never edit.

## How to answer a Keycloak/RHBK question
1. Search `wiki/` first — read `wiki/index.md`, then the matching topic/entity page,
   and follow `[[links]]`.
2. If the wiki is thin, query the raw corpus:
   `python3 kb/rhbk_kb.py search "<terms>"`  (add `--primary` / `--guide <slug>`
   to narrow; `--gated` for Red Hat login-only pointers).
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
Ingest/query operations may create or edit pages **under `wiki/` only**. Never
modify `kb/` or `references/` — that layer is regenerable ground truth. Offline
only: no network, no `webfetch`; the retriever is `kb/rhbk_kb.py`.
