# Agent instructions — Keycloak/RHBK wiki

This directory is an LLM-maintained Keycloak/RHBK knowledge wiki.

- **Read `CLAUDE.md` first** — it is the full schema and the ingest / query / lint
  workflow for this wiki.
- Entry point: `index.md`. Pages cross-link with `[[slug]]` (bare slug under
  `topics/` or `entities/`, no path or `.md`).
- Raw ground-truth corpus is one level up in `../kb/` and `../references/`. Query it
  with `python3 ../kb/rhbk_kb.py search "<terms>"` when the wiki is thin.
- **Operations** are packaged as Agent Skills in `../.skills/` (`wiki-ingest`,
  `wiki-query`, `wiki-lint`, `wiki-status`) and as OpenCode commands in
  `../.opencode/command/`. They are thin pointers — `CLAUDE.md` is the source of
  truth. Tooling (stdlib only) lives in `_meta/bin/`:
  - `python3 _meta/bin/lint.py [--status]` — health check + delta-manifest audit
  - `python3 _meta/bin/manifest.py {seed,status,record}` — delta manifest
  - `_meta/` (tooling + `.manifest.json`) is **excluded** from all scanners.
- Every page carries `summary:` (tiered query), two-tier `sources:`, and a
  per-claim `provenance:` block (`extracted`/`inferred`/`ambiguous`, or
  `needs-review` on un-audited legacy pages — never fabricate counts).
- **Hard rule:** edits go **only** to pages under this `wiki/` dir — never touch
  `../kb/` or `../references/`.
