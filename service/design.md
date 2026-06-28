# design.md — Serving Layer Design

> Derived from spec.md. Every element cites the FR/NFR it satisfies. Phase 2, self-reviewed.

## Module map

| Module | Responsibility | Owns |
|--------|----------------|------|
| `config.py` | Read env vars into a frozen `Config`; no IO on import. | NFR-5, FR-9 env surface |
| `index.py` | Walk routable globs, exclude source-only, parse frontmatter (reuse `tools/wikidoc._split_frontmatter`), split H2 sections, build `Index`. Path-safety helpers. | FR-1, FR-5, NFR-4, NFR-6 |
| `ranking.py` | `Ranker` base (hard version pre-filter + stable sort), `LexicalRanker`, `EmbeddingRanker`, `HybridRanker`, factory. | FR-2, FR-3, FR-8, NFR-3 |
| `embedding.py` | Local embed-source resolution (endpoint / model path), metadata-only corpus builder, numpy-flat store, graceful fallback. | FR-9, FR-10 |
| `app.py` | FastAPI app: `/route`, `/get`, `/reload`, `/healthz`, `/metrics`; atomic index swap; admin-token gate. | FR-2, FR-4, FR-6, FR-7, NFR-1 |

Import direction: `app → ranking → index → config`; `ranking → embedding → config`. No cycles.

## Contracts (typed schemas)

`POST /route` request `RouteRequest`:
```
{ query: str (required), k: int = 5, version: str|null, domain: str|null, type: str|null }
```
`RouteRequest` → `200 list[Hit]` (FR-2):
```
Hit = { path: str, section: str, title: str, domain: str, type: str,
        inject: "full"|"section", applies_to: list[str], score: float,
        source_provenance: list[{ref: str, visibility: str}] }
```
`GET /get?path&section` → `200 GetResponse` | `400` | `404` (FR-4, NFR-4):
```
GetResponse = { path, section: str|null, inject, frontmatter: dict, body: str,
                source_provenance: list[...] }
Error       = { reason: "source-only"|"not-routable"|"not-found"|"unsafe-path"|"no-section" }
```
`POST /reload` (header `X-Admin-Token`) → `200 {reloaded:true, files, sections}` | `401` (FR-6).
`GET /healthz` → `{status:"ok", files, sections, ranker, version_filter:true}` (FR-7).
`GET /metrics` → Prometheus text (FR-7).

## Data model (frozen dataclasses)

```
@dataclass(frozen=True)
class Section:    # one H2 (or __intro__)
    anchor: str; title: str; start_line: int; end_line: int; text: str; summary: str

@dataclass(frozen=True)
class Entry:      # one routable file
    path: str                 # POSIX, repo-relative (NFR-6)
    frontmatter: Mapping      # full fm (FR-5 provenance source)
    domain: str; title: str; type: str; inject: str
    applies_to: tuple[str,...]
    sections: tuple[Section,...]

@dataclass(frozen=True)
class Index:
    entries: tuple[Entry,...]
    postings: Mapping[str, tuple[tuple[int,int],...]]   # token -> ((entry_i, section_i),...)
    built_at: str
```
**Inverted index** (`postings`): token → list of `(entry_index, section_index)`. Tokeniser:
lowercase, split on `[^a-z0-9._-]+` (keeps `iso8601`, error codes like `ispn000541`,
versions). Candidate generation for a query = union of postings for its query tokens; the
ranker then scores only those candidates (FR-2). Empty query-token set → all sections are
candidates (so version/domain/type filters still work).

## Ranker interface (FR-8) with the FR-3 pre-filter in the base class

```
class Ranker(ABC):
    def rank(self, query, candidates, *, version=None, domain=None, type=None, k=5) -> list[Hit]:
        cands = self._prefilter(candidates, version, domain, type)   # FR-3 hard gate, shared
        scored = self._score(query, cands)                            # subclass
        scored.sort(key=lambda h: (-h.score, h.path, h.section))      # NFR-3 stable, deterministic
        return scored[:k]
    @staticmethod
    def _prefilter(cands, version, domain, type):
        out = cands
        if version: out = [c for c in out if version in c.entry.applies_to]   # AC-3.1
        if domain:  out = [c for c in out if c.entry.domain == domain]
        if type:    out = [c for c in out if c.entry.type == type]
        return out
    @abstractmethod
    def _score(self, query, cands) -> list[Hit]: ...
```
- `LexicalRanker._score`: BM25-lite over `(frontmatter keywords ×3, title ×2, section title
  ×2, summary ×1)` + exact-token bonus for error-code-shaped tokens. Zero deps (AC-8.1).
- `EmbeddingRanker._score`: cosine(query_vec, section_meta_vec) via the numpy-flat store;
  requires a resolved embed source else the factory degrades to lexical (FR-9).
- `HybridRanker._score`: `0.5·norm(lexical) + 0.5·norm(embedding)`, min-max normalized per
  query; exact-token bonus kept in the lexical half so exact codes win ties (AC-8.2).

`make_ranker(config, index)` (factory): resolves `WIKI_RANKER`; for `embedding`/`hybrid` it
calls `embedding.resolve_source(config)`; on `None` it logs a warning and returns
`LexicalRanker` (FR-9, AC-9.1).

## Embedding design (FR-9, FR-10)

- **Source resolution** `resolve_source(config)`: if `WIKI_EMBED_ENDPOINT` set → an
  `EndpointEmbedder` (POST loopback `/embeddings`, OpenAI-compatible); elif
  `WIKI_EMBED_MODEL_PATH` exists → a `LocalModelEmbedder` (sentence-transformers, lazy import);
  else `None`. Never calls a non-loopback host (AC-9.2): endpoint host must be
  `127.0.0.1/localhost` or the call is refused.
- **Corpus (metadata only, FR-10)**: per section, embed `summary_text =
  "{domain} | {file title} | {section title} | {keywords} | {first-line ≤200c}"`. The full
  section body is never included → AC-10.1 holds by construction.
- **Store**: single-file `embeddings.npz` (numpy float32 matrix + parallel id list). Flat
  cosine; no server, no graphdb (Out-of-scope, OQ-1). sqlite-vec/FAISS deferred (OQ-1).
- **Query embedding**: same embedder; `hybrid` normalizes both score vectors min-max.

## Config (env vars)

| Env | Default | Meaning |
|-----|---------|---------|
| `WIKI_REPO_ROOT` | repo root | Root scanned for routable globs (mounted read-only at `/repo`). |
| `WIKI_RANKER` | `lexical` | `lexical` \| `embedding` \| `hybrid` (FR-8). |
| `WIKI_EMBED_ENDPOINT` | unset | Loopback OpenAI-compatible `/embeddings` URL (FR-9). |
| `WIKI_EMBED_MODEL_PATH` | unset | Staged local ST model dir (FR-9). |
| `WIKI_EMBED_STORE` | `service/embeddings.npz` | numpy-flat store path. |
| `WIKI_ADMIN_TOKEN` | unset | Required for `/reload`; unset ⇒ `/reload` always `401` (FR-6). |
| `WIKI_DEFAULT_K` | `5` | Default top-k (AC-2.2). |

## Decisions (ADR-lite)

- **ADR-1: Filesystem + frontmatter over graphdb/vector-DB server.** The corpus is already
  curated, version-gated Markdown under GitOps; routing needs section selection + a hard
  version filter, not graph traversal or an always-on vector server. Filesystem index = zero
  infra, atomic reload, fully air-gapped. *(Scope §5, NFR-1/2/5.)*
- **ADR-2: Lexical default, zero ML deps.** Operational queries are dominated by exact error
  codes / config keys where lexical exact-match is strong and deterministic; ML is an opt-in
  accelerator. Keeps the default image tiny and offline. *(FR-8, AC-8.1.)*
- **ADR-3: Embed metadata only.** Embedding full bodies would (a) bloat the store, (b) risk
  leaking gated body text into a derived artifact, (c) add no routing value over
  title/keywords/summary. *(FR-10, Scope §5.)*
- **ADR-4: numpy-flat store, sqlite-vec/FAISS deferred.** numpy is already vendored offline;
  a flat cosine over ≤ a few-thousand sections is sub-millisecond. Avoids an unverified mirror
  dependency. *(OQ-1, NFR-5.)*
- **ADR-5: Hard version pre-filter in the base class.** Putting FR-3 in `Ranker._prefilter`
  guarantees BOTH rankers (and hybrid) inherit it — version-gating cannot be forgotten in a
  subclass. *(FR-3.)*

## Agent integration design (FR-11)

- `agent/wiki_tools.json`: two tools. `wiki_route(query, version?, domain?, type?, k?)` →
  hits; `wiki_get(path, section?)` → section. Schemas mirror the typed contracts above.
- `AGENTS.md.snippet` routing rules: (1) call `wiki_route` before any operational answer;
  (2) if `applies_to` of the top hit lacks the asked version → say out-of-version, escalate;
  (3) if `source_provenance.visibility != public` → tell the user it is gated, give the ref,
  do NOT paraphrase a fix; (4) if no hit → escalate, never fabricate. *(AC-11.2.)*
