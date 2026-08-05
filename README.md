# llm-wiki — multi-domain LLM-maintained knowledge wiki

An **LLM-maintained, multi-domain knowledge wiki** — Keycloak / Red Hat build of
Keycloak (RHBK), OpenShift/Kubernetes, PowerShell, SCCM, Windows Server, SharePoint,
Exchange, Active Directory, and Cisco IOS-XE, with new domains onboarded via
ADD-DOMAIN — following Andrej Karpathy's "LLM Wiki" pattern:
immutable raw corpora stay frozen in the vault, the wiki is the *compiled,
cross-linked synthesis* on top, and it compounds across sessions because every
answered question is filed back as a durable page.

Open **the repo root** as the Obsidian vault — the vault IS the repo, and it rules
all the data.

![Architecture and flow: harvest → the vault → query & serve](architecture.png)

## What's here

Nine corpus-backed domains; each raw tier is immutable doc-body notes under
`vault/reference/<domain>/`, with hand notes staged in `vault/_sources/<domain>/`.

| Domain | Raw notes | Tiers covered |
|---|---|---|
| **powershell** | 4,579 | conceptual |
| **openshift** | 3,908 | conceptual (Kubernetes + OpenShift 4.22) |
| **sccm** | 2,773 | conceptual, support-kb |
| **windows-server** | 2,006 | conceptual |
| **sharepoint** | 936 | conceptual |
| **keycloak** | 833 | conceptual, support-kb |
| **active-directory** | 313 | conceptual |
| **cisco-ios-xe** | 173 | conceptual |
| **exchange** | 80 | conceptual |

Synthesis so far: **66 topics · 267 entities · 153 answered questions**, all
cross-linked with `[[slug]]`.

## Layout

```
<repo-root>/
├── CLAUDE.md            # THE schema + ingest/query/lint workflows — read this first
├── SKILL.md · AGENTS.md # skill trigger manifest + thin agent pointer to CLAUDE.md
├── .claude/             # shared Claude Code config: commands/ + agents/ (session state ignored)
├── .env.example         # runtime config template → copy to .env (gitignored)
├── Dockerfile · docker-compose.yml
├── _meta/               # tooling (the `wikikb` package); excluded from scanners
└── vault/               # ← THE OBSIDIAN VAULT. Open THIS in Obsidian.
    ├── index.md             # global router → per-domain indexes
    ├── index.<domain>.md    # per-domain routing index (titles + summaries; generated)
    ├── taxonomy.md          # controlled vocab every page's `domain:` is validated against
    ├── topics/              # multi-source syntheses ("how LDAP federation works")
    ├── entities/            # one page per concrete thing (a flag, SPI, config key)
    ├── questions/           # answered queries, filed back as durable pages
    ├── outputs/             # derived artifacts (runbooks, cheat sheets)
    ├── references/          # curated reference guides (ref: tier) — never edit
    ├── reference/<domain>/  # IMMUTABLE imported doc bodies — never edit
    └── _sources/<domain>/   # raw hand notes for notes-first material — never edit
```

**`vault/` is the portable unit.** Everything non-regenerable lives under it — including
`taxonomy.md` and `.manifest.json`, which used to sit in `_meta/` and were silently left
behind whenever the content moved. Migrating between machines is a copy of that one
directory; what stays behind under `_meta/` is either code or rebuildable
(`embeddings/`, `tkg/`). Point the toolchain at any location with `WIKIKB_VAULT_ROOT=<path>`.

## Running it in a container

```bash
cp .env.example .env          # then set HOST_VAULT_DIR to your content directory
docker compose up -d
open http://localhost:8642/docs           # self-contained API reference (no CDN)
```

Content lives on the host and the image holds only code, so updating pages never
rebuilds the image. `.env` controls the operation mode, the vault mount, the published
port, the MCP route (`WIKIKB_MCP_PATH`, default `/mcp`), auth, and whether the PDF
upload surface is enabled.

### Two operation modes (`WIKIKB_MODE`)

One image, one compose file, two postures — and they are **additive**, so `online` is a
strict superset of `airgapped` and a client written against either works against both:

| | `airgapped` (default) | `online` |
|---|---|---|
| Vault + MCP + PDF upload/ingest | ✅ | ✅ |
| Web scraper (`/scrape`) | — | ✅ *(seam — answers 501 until implemented)* |
| Outbound network | never | scraper only |

In airgapped mode the `/scrape` paths answer exactly like an unknown path and are absent
from `/openapi.json`, so a sealed instance doesn't advertise a surface it refuses to
serve. An unknown `WIKIKB_MODE` **refuses to start** rather than guessing a default.
`GET /health` reports the live mode and its capabilities.

> A bind mount **shadows** the image's baked `vault/` rather than merging with it —
> seed the host directory first (`cp -a ./vault/. $HOST_VAULT_DIR/`) or you will serve
> an empty wiki with no error.

## Using it

**As a human / in Obsidian:** start at `index.md`, follow `[[links]]`. Every page
carries a `summary:` so you can skim before opening bodies.

**As an agent:** read `CLAUDE.md` — it is the single source of truth for the
ingest / query / lint operations. The `.claude/skills/` packages are thin
pointers back to it.

**Tools** (stdlib only, air-gapped, no `pip install`) — run from `_meta/`:

```bash
python3 -m wikikb route  "<query>"           # route a question to its domain(s)
python3 -m wikikb kb --domain keycloak search "<terms>"   # search the raw tier
python3 -m wikikb ask --domain keycloak "<question>"      # gated, cited answer
python3 -m wikikb build                       # regen chain: tags → crosslink → index → tkg → lint → verify
python3 -m wikikb lint [--status]             # health check + audit
python3 _meta/tests/selftest.py               # run the test suite
```

**Serving:** `python3 -m wikikb serve` exposes the same tools as a loopback JSON
API (`/route /search /ask /page /expand`); `python3 -m wikikb mcp` serves them
over MCP stdio (`claude mcp add wikikb -- python3 -m wikikb mcp`). See
`CLAUDE.md` → "Serving the wiki".

**Adding a PDF over HTTP** (write surface, opt-in via `WIKIKB_ALLOW_UPLOAD=1`):

```bash
curl -T guide.pdf http://localhost:8642/upload/keycloak/guide.pdf
# -> 201 {"stored": "...", "job_id": "9f2c1a0b4d7e", "status_url": "/jobs/9f2c1a0b4d7e"}
curl http://localhost:8642/jobs/9f2c1a0b4d7e
```

Storing the file also **queues the conversion** in the background —
`pdf_to_corpus --append` → `corpus_to_vault` → `build` — so the drop becomes an
immutable reference note that is crosslinked into the rest of the Markdown, without a
second command. One serialized worker; a second queued job for the same domain coalesces
into the first. `WIKIKB_AUTO_INGEST=0` keeps uploads store-only and lets you batch several
drops into one run with `POST /ingest/<domain>`.

## Rules

- **Writes go only under `vault/topics/ vault/entities/ vault/questions/`.** The raw tiers
  (`reference/`, `_sources/`, `references/`) are immutable ground truth.
- **Cite everything.** Every claim traces to a `kb:`/`guide:`/`ref:`/`note:`/`web:`
  source; no uncited synthesis. Per-claim provenance (`extracted`/`inferred`/
  `ambiguous`) is assigned by reading the claim against its source — never by
  counting bullets.
- **Versions matter.** RHBK ships 26.0 / 26.2 / 26.4 / 26.6; say which when behavior
  differs.

See `CLAUDE.md` for the full page format, the Confidence gate, and the
ADD-DOMAIN / INGEST / QUERY / LINT / STATUS / VERIFY operations.

## Roadmap

- **`_meta/ROADMAP.md`** — the live roadmap. Dense retrieval, graph expansion, the
  temporal knowledge graph, and the cited/gated `wikikb ask` + serve/MCP pipeline
  have landed; see the roadmap for what's next.
