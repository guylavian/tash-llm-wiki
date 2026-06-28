# spec.md — Air-Gapped LLM-Wiki Serving Layer

> Single source of truth. EARS-form requirements, each with a unique ID and acceptance
> criteria. Living spec: amend HERE first, then propagate to design/tasks/code.
> Status: Phase 1 self-reviewed. Date: 2026-06-28.

## 1. Purpose & scope

This service is the **read-only serving layer** that lets an offline SRE agent route a query
to the right curated Markdown section and fetch it, over HTTP, inside an air-gapped network.

**It serves**: ranked routing (`/route`) and scoped retrieval (`/get`) over the *routable*
curated docs (`references/`, `**/references/`), version-gated, with provenance.

**It explicitly does NOT**: generate text (Qwen is a separate service), run a graph database,
run a vector-DB server, embed or serve full document bodies into an embedding store, reach any
public network, or write per-request state to disk. Generation, authoring, and frontmatter
*validation* (owned by `tools/wikidoc.py`) are out of scope.

## 2. Glossary

- **Routable**: a Markdown file with frontmatter `routable: true`, under a routable glob. Only
  routable files are indexed and served.
- **Source-only**: files under `wiki/reference/`, `raw/`, `harvest/` — raw/harvest material.
  Never indexed, never served, regardless of frontmatter.
- **Section**: the text under one `## H2` heading (its anchor + line range). The unit of
  retrieval when `inject: section`.
- **Inject mode**: frontmatter `inject` — `section` (serve the matched H2 + frontmatter) or
  `full` (serve the whole file body).
- **Version-gating**: a hard pre-filter that drops any entry whose `applies_to` does not
  contain the caller-supplied version, applied *before* ranking.
- **Ranker**: a strategy that orders candidate sections for a query. `LexicalRanker` (default,
  zero-ML) and `EmbeddingRanker` (Stage 1) behind one interface; `hybrid` fuses both.
- **Hit**: one ranked result `{path, section, title, domain, type, inject, applies_to, score,
  source_provenance}`.

## 3. Functional requirements

**FR-1 — Index build.**
The system SHALL build an in-memory index ONLY from the routable globs (`references/**/*.md`,
`**/references/**/*.md`). It SHALL exclude every source-only directory (`wiki/reference/`,
`raw/`, `harvest/`) and every file whose frontmatter `routable` is not exactly `true`. It
SHALL split each indexed file into `## H2` sections, each carrying an anchor and a
`[start_line, end_line]` range.
- AC-1.1: A file under `wiki/reference/` is absent from the index even if it declares
  `routable: true`.
- AC-1.2: A `references/` file with `routable: false` (or no frontmatter) is absent.
- AC-1.3: A 3-H2 file yields ≥3 sections, each with a distinct anchor and non-overlapping
  line range; preamble before the first H2 is retained as section `__intro__`.

**FR-2 — `/route`.**
WHEN the system receives `POST /route {query, k?, version?, domain?, type?}` it SHALL return
the top-k ranked hits, each hit containing `{path, section, title, domain, type, inject,
applies_to, score, source_provenance}`, ordered by descending score.
- AC-2.1: Response is a JSON list of ≤ k hits with all listed keys present.
- AC-2.2: `k` defaults to 5 when omitted; `k` is clamped to [1, 50].

**FR-3 — Version-gating (hard pre-filter, every ranker).**
WHEN `version` is supplied, the system SHALL drop every candidate whose `applies_to` does not
contain that version BEFORE ranking, in EVERY ranker (enforced in the base class).
- AC-3.1: `version=26.6` never returns a hit from a doc whose `applies_to=[26.2]`.
- AC-3.2: Omitting `version` disables the filter (all versions eligible).

**FR-4 — `/get`.**
WHEN the system receives `GET /get?path=<p>&section=<anchor>` it SHALL, for a routable file:
return the scoped H2 section body + the file frontmatter when `inject: section`; return the
whole file body + frontmatter when `inject: full`. It SHALL respond `404` with a machine
-readable `reason` when the path is source-only, non-existent, or `routable != true`.
- AC-4.1: `inject: section` returns only the requested section body (not sibling sections) +
  frontmatter.
- AC-4.2: `inject: full` returns the entire body.
- AC-4.3: `/get` on a `wiki/reference/` path → `404 {reason: "source-only"}`.
- AC-4.4: `/get` on a `routable:false` path → `404 {reason: "not-routable"}`.

**FR-5 — Provenance.**
The system SHALL attach `source_provenance` (a list of `{ref, visibility}`) to every `/route`
hit and every `/get` response, copied verbatim from frontmatter.
- AC-5.1: Every hit and every `/get` body contains a non-empty `source_provenance` with
  `visibility` on each entry.

**FR-6 — `/reload`.**
WHEN the system receives `POST /reload` with a valid `X-Admin-Token` it SHALL rebuild the
index from disk and atomically swap it in (readers never see a partial index). Without a valid
token it SHALL respond `401`.
- AC-6.1: Bad/missing token → `401`, index unchanged.
- AC-6.2: Valid token → `200`, subsequent `/route` reflects on-disk changes.

**FR-7 — `/healthz`, `/metrics`.**
The system SHALL expose `GET /healthz` (status + index stats) and `GET /metrics`
(Prometheus text exposition, local scrape only).
- AC-7.1: `/healthz` returns `{status:"ok", files, sections, ranker}`.
- AC-7.2: `/metrics` returns Prometheus text with at least request-count and index-size gauges.

**FR-8 — Rankers + hybrid.**
The system SHALL provide `LexicalRanker` (default, zero ML deps) and `EmbeddingRanker`
(Stage 1) behind ONE `Ranker` interface, and SHALL support a `hybrid` mode fusing both with
normalized scores.
- AC-8.1: With `WIKI_RANKER=lexical` the service runs with zero ML dependencies installed.
- AC-8.2: In `hybrid`, an exact error-code/keyword query out-ranks a semantically-near but
  wrong doc.

**FR-9 — Embedding source (local only, graceful fallback).**
The embedding source SHALL be LOCAL only: an internal `/embeddings` HTTP endpoint
(`WIKI_EMBED_ENDPOINT`) or a staged model path (`WIKI_EMBED_MODEL_PATH`). WHEN neither
resolves, the system SHALL still start, log a warning, and serve using `LexicalRanker`.
- AC-9.1: `WIKI_RANKER=embedding` with no endpoint and no model path → service starts, emits a
  warning, and `/healthz.ranker == "lexical"`.
- AC-9.2: The system SHALL NOT attempt any non-loopback network call to resolve embeddings.

**FR-10 — Embedding corpus (metadata only).**
The embedding corpus SHALL contain ONLY frontmatter fields + headings + per-section summaries.
It SHALL NEVER contain full section/body text.
- AC-10.1: For every embedded record, the verbatim body text of its section is NOT a substring
  of the embedded text.

**FR-11 — Agent contract.**
The service SHALL be consumable via `wiki_route` / `wiki_get` tools. The agent contract SHALL
require calling `wiki_route` before answering operational questions and SHALL require
escalation (not fabrication) when the top hit is gated (`visibility != public`), out-of
-version (empty after FR-3 filter), or absent.
- AC-11.1: `agent/wiki_tools.json` defines `wiki_route` and `wiki_get` with schemas matching
  FR-2/FR-4.
- AC-11.2: `AGENTS.md.snippet` states the route-first and escalate-don't-fabricate rules.

## 4. Non-functional requirements

- **NFR-1 — Stateless.** The system SHALL NOT write to disk per request; only the in-memory
  index object mutates, via atomic swap. *(AC: no file created under repo during a `/route`/`/get`.)*
- **NFR-2 — No egress / no phone-home.** The system SHALL make no public-network call and emit
  no telemetry. *(AC: only loopback sockets opened; static analysis finds no external host.)*
- **NFR-3 — Determinism.** Identical query → identical ordering (stable sort, tie-break by
  `(path, section)`, no randomness). *(AC-NFR3.)*
- **NFR-4 — Path safety.** `/get` SHALL reject any `path` that escapes the repo root (`..`,
  absolute, or out-of-root symlink) with `400`. *(AC-NFR4.)*
- **NFR-5 — Offline/air-gap.** All deps SHALL come from the internal mirror; the Docker base
  SHALL be pinned by DIGEST. *(AC: requirements.txt pinned; Dockerfile FROM ...@sha256.)*
- **NFR-6 — Windows-friendly + UTF-8.** Paths SHALL be normalized to POSIX form internally and
  all file IO SHALL be UTF-8. *(AC: backslash paths normalize; UTF-8 read everywhere.)*

## 5. Out of scope

Graph database; vector-DB *server* (Milvus/Qdrant/etc.); text generation; embedding or serving
full bodies; authoring/validation of frontmatter (that is `tools/wikidoc.py`); auth beyond the
`X-Admin-Token` admin gate; multi-tenant access control.

## 6. Open questions

- **OQ-1 (blocks: embedding accelerator only).** sqlite-vec and FAISS availability on the
  internal mirror is unverified from this environment, and the rules forbid fetching externally.
  **Resolution taken without guessing the mirror:** the Stage-1 embedded store ships as a
  single-file **numpy-flat cosine** store (`numpy` is already vendored in-repo at
  `wiki/_meta/.venv-embed`, confirmed present), which satisfies FR-8/FR-10 offline. sqlite-vec /
  FAISS remain an OPEN, deferred *accelerator* choice — NOT on the critical path. The lexical
  service has zero ML deps and is fully deliverable regardless. **Question for owner:** is
  sqlite-vec (preferred) present on the mirror, or should numpy-flat remain canonical?
- **OQ-2 (data-state, non-blocking).** As of this branch the 12 `references/*.md` files do **not
  yet carry frontmatter** (the wikidoc backfill is a separate, paused task). The serving layer is
  correct but will index **0 files** against the current tree until backfill lands. Tests
  therefore run against committed **fixtures** under `service/tests/fixtures/`. **Question for
  owner:** confirm tests-on-fixtures is acceptable for this PR, with a real-tree smoke test
  deferred until backfill merges.
- **OQ-3 (resolved by decision).** "section summary" for FR-10 is defined as: the section's H2
  heading text + its first non-empty line (≤ 200 chars), never the full body. Flagged here for
  visibility; see design.md §Embedding.
- **OQ-4 (blocks: Docker build only, NFR-5).** NFR-5 requires the base image pinned by DIGEST.
  The internal mirror's digest for `python:3.12-slim` cannot be resolved from the build sandbox
  and external fetch is forbidden. The `Dockerfile` carries a clearly-marked
  `sha256:<PIN_FROM_INTERNAL_MIRROR>` placeholder + the exact `docker inspect` command to fill
  it. **Question for owner:** provide the mirror's resolved digest (or confirm a digest-pinning
  CI step will inject it at build time). All non-Docker artifacts are unaffected.

## 7. Acceptance criteria summary

| AC | Proves | AC | Proves |
|----|--------|----|--------|
| AC-1.1/1.2/1.3 | FR-1 | AC-7.1/7.2 | FR-7 |
| AC-2.1/2.2 | FR-2 | AC-8.1/8.2 | FR-8 |
| AC-3.1/3.2 | FR-3 | AC-9.1/9.2 | FR-9 |
| AC-4.1..4.4 | FR-4 | AC-10.1 | FR-10 |
| AC-5.1 | FR-5 | AC-11.1/11.2 | FR-11 |
| AC-6.1/6.2 | FR-6 | AC-NFR3/NFR4 | NFR-3/NFR-4 |
