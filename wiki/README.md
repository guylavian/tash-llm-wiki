# Keycloak/RHBK Knowledge Wiki

An **LLM-maintained knowledge wiki** for Keycloak / Red Hat build of Keycloak (RHBK)
and adjacent infra domains, following Andrej Karpathy's "LLM Wiki" pattern: raw
sources stay frozen, the wiki is the *compiled, cross-linked synthesis* on top, and
it compounds across sessions.

Open **this directory** (`wiki/`) as the Obsidian vault root — it rules all the data.

## What's here

| Domain | Shape | Raw tier |
|---|---|---|
| **keycloak** | corpus-backed | 832 immutable doc-body notes in `reference/keycloak/` |
| **active-directory** | notes-first | hand notes in `_sources/active-directory/` |
| **cisco-ios-xe** | notes-first | `_sources/cisco-ios-xe/` |

Synthesis so far: **42 topics · 187 entities · 22 answered questions**, all
cross-linked with `[[slug]]`.

## Layout

```
wiki/
├── CLAUDE.md            # THE schema + ingest/query/lint workflows — read this first
├── AGENTS.md            # thin pointer to CLAUDE.md for agents
├── index.md             # global router → per-domain indexes
├── index.<domain>.md    # per-domain routing index (titles + summaries; generated)
├── topics/              # multi-source syntheses ("how LDAP federation works")
├── entities/            # one page per concrete thing (a flag, SPI, config key)
├── questions/           # answered queries, filed back as durable pages
├── reference/<domain>/  # IMMUTABLE imported doc bodies — never edit
├── _sources/<domain>/   # raw hand notes for notes-first domains — never edit
└── _meta/               # tooling (the `wikikb` package); excluded from scanners
```

## Using it

**As a human / in Obsidian:** start at `index.md`, follow `[[links]]`. Every page
carries a `summary:` so you can skim before opening bodies.

**As an agent:** read `CLAUDE.md` — it is the single source of truth for the
ingest / query / lint operations. The `.skills/` packages and `.opencode/`
commands are thin pointers back to it.

**Tools** (stdlib only, air-gapped, no `pip install`) — run from `_meta/`:

```bash
python3 -m wikikb route  "<query>"           # route a question to its domain(s)
python3 -m wikikb kb --domain keycloak search "<terms>"   # search the raw tier
python3 -m wikikb index                       # regenerate the routing indexes
python3 -m wikikb lint [--status]             # health check + audit
python3 wiki/_meta/tests/selftest.py          # run the test suite
```

## Rules

- **Writes go only under `topics/ entities/ questions/`.** The raw tiers
  (`reference/`, `_sources/`, `../references/`) are immutable ground truth.
- **Cite everything.** Every claim traces to a `kb:`/`guide:`/`ref:`/`note:`/`web:`
  source; no uncited synthesis. Per-claim provenance (`extracted`/`inferred`/
  `ambiguous`) is assigned by reading the claim against its source — never by
  counting bullets.
- **Versions matter.** RHBK ships 26.0 / 26.2 / 26.4 / 26.6; say which when behavior
  differs.

See `CLAUDE.md` for the full page format, the Confidence gate, and the
ADD-DOMAIN / INGEST / QUERY / LINT / STATUS operations.

## Roadmap

- **`RAG-REPLACEMENT-PLAN.md`** — how this wiki becomes a working, air-gapped RAG
  replacement / SRE brain: activate the dormant dense-retrieval, local-LLM synthesis,
  and Graphiti/Kuzu graph layers into one cited, gated `wikikb ask` pipeline.
- **`REVIEW.md`** — project health review (toolchain, lint/selftest baseline).
