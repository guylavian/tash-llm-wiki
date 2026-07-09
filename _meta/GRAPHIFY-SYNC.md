# Obsidian ↔ Graphify integration — curated semantic graph for agent retrieval

Graphify's own markdown extraction is structural (a node per heading → 80% "contains"
noise). This integration inverts the flow: **Obsidian stays the source of truth, the
wiki toolchain builds the semantic graph, and Graphify consumes it** — its
`query`/`path`/`explain` CLI, Leiden communities, report, and `graph.html` all run over
the *curated* relations instead of re-extraction.

## Topology (what the agent traverses)

Node = one page = one concept (the wiki's page-per-concept contract; all English).
Node kinds and the ONLY two edge types exported:

```
Domain MOC (<domain>-implementation-review)
   │ references                       ┌────────────────────────────┐
Topic (synthesis, e.g. tokens-and-sessions)                        │
   │ references (bidirectional [[wikilinks]])                      │ cites
Entity (one concept: dpop, distributed-caches) ────────────────────┤ (provenance,
   │ references                                                    │  version-dated)
Question (filed answers / post-mortems)                            ▼
                                                     Source (immutable reference/<d>/ note)
```

- **`references`** (2,068) — `[[wikilink]]` edges between synthesis pages. These are
  hand-curated semantic relations (service → dependency, feature → failure mode,
  topic → its entities), never folder hierarchy.
- **`cites`** (587) — page → the immutable reference note that grounds it, resolved by
  `crosslink.py` (newest doc version wins); version-temporal edges carry `valid_from`.
- **Excluded by design:** `IN_DOMAIN` edges + Domain nodes (god-nodes, degree 69–178 —
  they flood traversal; `domain` is a node *attribute* for filtering), and all
  heading/section nodes. This is what keeps 1-hop expansion high-precision.

Retrieval pattern the topology serves (same as QUERY step 2): route → seed page(s) →
1-hop `references` for related concepts → `cites` for ground truth. Hubs are the
per-domain review MOCs, so symptom-style queries land 1 hop from every failure-mode page.

## Bootstrap (new codebase/domain)

1. Author the wiki per `CLAUDE.md` (ADD DOMAIN + INGEST): page per concept, `[[links]]`
   for semantic relations, `kb:` tokens for provenance. English throughout.
2. `sh _meta/sync-graph.sh` — builds everything below from scratch.
3. Optional code-side graph: `graphify update <src-repo>` on the *source code* repo
   (AST extraction is good for code) and `graphify merge-graphs` it with this one.

## Sync (when notes change)

`_meta/sync-graph.sh` chains, idempotently:

```
wikikb crosslink --apply   # kb: tokens → generated ## Sources [[links]]
wikikb index               # routing indexes
wikikb tkg ingest          # typed graph → _meta/tkg/graph.json (canonical)
wikikb.tkg.graphify_export # → graphify-out/graph.json (Graphify schema)
wikikb.tkg.viewer          # → _meta/tkg/graph.html (typed-edge view)
graphify cluster-only . --no-label   # communities + GRAPH_REPORT + graph.html
```

Auto-run on commits that touch synthesis pages:
`git config core.hooksPath _meta/hooks` (installs the `post-commit` hook).

**Never run `graphify update .` on the wiki** — it re-extracts headings and clobbers
the curated export. `.graphifyignore` excludes raw tiers as a backstop.

## Querying (agent side)

- `graphify path "dpop" "token-revocation"` — shortest semantic path between concepts.
- `graphify explain "distributed-caches"` — a node + its typed neighborhood.
- `python3 -m wikikb expand --domain <d> "<query>"` — seed→1-hop with source notes
  (the wiki-native equivalent, used by QUERY).
- `graphify-out/graph.json` — machine-readable for any other consumer.
