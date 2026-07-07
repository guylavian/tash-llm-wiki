"""wikikb.tkg — the temporal + cross-domain knowledge-graph tier over the Obsidian vault.

A deterministic, STDLIB-ONLY graph layer: it compiles the vault's *already-existing* edges
(`[[wikilinks]]` in page bodies + the `kb:`→reference-note citations `crosslink.py` resolves) into a
normalized node/edge model, serialized to a JSON store under `_meta/tkg/` (derived, like
`_meta/embeddings/`). Obsidian stays the single source of truth and the only editing surface; this tier
is a downstream, regenerable *view* of it.

Two design invariants make the tier honest and air-gap-safe:

  * NO LLM / NO inference for edges (rule R3): edges come only from the two deterministic sources above.
  * NO `updated:` as a temporal signal (rule R2): a Source node's version metadata is read EXCLUSIVELY
    from the immutable `reference/<domain>/` note frontmatter — never from a synthesis page (the only
    files that carry `updated:`). `valid_from` is therefore unreachable from edit metadata by construction.

This package exports ONLY stdlib symbols. The optional Graphiti/Kuzu accelerator (Phase 5) lives in
`tkg.graphiti_backend` and is NEVER imported here or at any module scope — it is lazy-imported inside its
own `connect()` factory, behind `WIKI_TKG` + `available()`, exactly like the `online/` tier. So a bare
`import wikikb.tkg` opens no socket and pulls no third-party package.
"""
from wikikb.tkg.model import WikiNode, WikiEdge, WikiGraph, build_graph
from wikikb.tkg.store import save_store, load_store

__all__ = ["WikiNode", "WikiEdge", "WikiGraph", "build_graph", "save_store", "load_store"]
