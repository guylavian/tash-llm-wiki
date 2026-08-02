# Production setup — decisions & operations (2026-07-22)

## Architecture: one repo, split at deploy
Code (`_meta/wikikb`) and content (vault) stay in ONE repo — the CLAUDE.md schema,
lint contract, and content co-evolve, and the air-gap copy-one-dir model depends on it.
The split happens at the **artifact** level, not the repo level:

- **Local (this Mac):** code and vault are the same tree; services read the vault live.
- **Container/cluster:** build the image from the Dockerfile for a baked snapshot, or
  run the slim variant — image with only `_meta/` + `pip` deps, vault volume-mounted
  and pointed at via `WIKIKB_VAULT_ROOT=<mount>` (`paths.py` already honors it) — so
  content updates never rebuild the image.

## Services on this Mac
| Surface | Mechanism | Consumer |
|---|---|---|
| HTTP JSON API `127.0.0.1:8642` | launchd `com.wikikb.serve` (`~/Library/LaunchAgents/com.wikikb.serve.plist`, KeepAlive + RunAtLoad, log: `~/Library/Logs/wikikb-serve.log`) | scripts, curl, cron |
| MCP (stdio) | `claude mcp` user-scope entry `wikikb` — spawned per session, no daemon | Claude Code / any MCP host |
| MCP over HTTP `POST /mcp` | same `serve` process as the JSON API — no second daemon | n8n, or any remote MCP host that can't spawn a stdio child |

Both run under `_meta/.venv-embed/bin/python` (symlink → repo-root `_meta/.venv-embed`)
so dense/hybrid retrieval is active.

**Auth (corrected 2026-08-02 — this section previously said "serve.py has no auth", which has
been false since the `POST /mcp` work landed).** `serve.py` ships an opt-in bearer gate: set
`WIKIKB_API_TOKEN` and every endpoint except `/health` requires `Authorization: Bearer <token>`
(`serve.py:_check_auth`). `/health` stays open on purpose — kubelet-style probes can't attach
custom headers. Unset (the local default) keeps the no-auth, loopback-only posture.

So the rule is no longer "never bind a real interface" but: **binding a real interface requires
`WIKIKB_API_TOKEN` to be set** — the process prints which posture is live at startup, so check the
first log line rather than assuming. `/mcp` additionally validates `Origin` (403 when present and
not in `WIKIKB_MCP_ALLOWED_ORIGINS`), which is the DNS-rebinding MUST; a backend client like n8n
sends no `Origin` and is unaffected.

## MCP protocol eras (2026-08-02)

`POST /mcp` is **dual-era**. MCP revision `2026-07-28` removed the `initialize` handshake, the GET
SSE stream, and protocol-level sessions, replacing them with per-request `_meta` plus required
`MCP-Protocol-Version` / `Mcp-Method` / `Mcp-Name` headers. The spec's own matrix says a modern
client against a legacy-only server **fails**, so the server now speaks both and picks per request:

- No modern `_meta` → the original legacy path, byte-for-byte unchanged (what n8n and Claude Code
  send today). Nothing about the working surface changed.
- Modern `_meta` → `server/discover`, `resultType: "complete"`, `_meta.serverInfo`, header/body
  cross-validation (`-32020`), `-32022` on an unknown version, `-32602` on missing required `_meta`,
  and `404` (not 200) for an unknown method.

`GET`/`DELETE /mcp` → 405 is now what the spec *mandates*, not merely permits.

Service ops:
```
launchctl kickstart -k gui/501/com.wikikb.serve     # restart (e.g. after wikikb code changes)
launchctl bootout   gui/501/com.wikikb.serve        # stop
curl -s localhost:8642/health                       # probe
```

## Layout invariants (post-cleanup 2026-07-22)
- Vault + toolchain: `<repo>/llm-wiki/` (this tree). Live venvs stay at repo-root
  `_meta/.venv-*` (venvs are not relocatable); `llm-wiki/_meta/.venv-{embed,online}`
  are symlinks to them. Rebuilding a venv in-place at `llm-wiki/_meta/` may replace
  the symlink whenever convenient.
- `models/` (vendored bge-small), `embeddings/` (dense index), `llm.config.yaml`
  (gitignored, live gateway config) all live in `llm-wiki/_meta/` now.
- Content updates: commit → post-commit hook runs `sync-graph.sh` (requires
  `git config core.hooksPath llm-wiki/_meta/hooks`); the HTTP service reads files
  live, no restart needed for content — restart only for `wikikb` code changes.
