#!/usr/bin/env python3
"""store.py — (de)serialize the WikiGraph to a JSON store. stdlib only.

The JSON store is the CANONICAL artifact every CLI verb reads; the optional Kuzu/Graphiti backend
(Phase 5) is layered on top and is never required. It is derived + regenerable from the vault (like
`_meta/embeddings/`), so it lives under `_meta/tkg/` and is gitignored — a missing store just means
"run `tkg ingest`", never data loss.
"""
import json
import os
from dataclasses import asdict

from wikikb import paths
from wikikb.tkg.model import WikiEdge, WikiGraph, WikiNode

DEFAULT_PATH = str(paths.TKG / "graph.json")
SCHEMA = "wikikb-tkg/1"


def graph_to_dict(graph: WikiGraph) -> dict:
    """The single canonical serialization shape — used by BOTH save_store and `tkg ingest --stdout` so
    the persisted store and the piped JSON can never diverge (incl. the top-level `schema` discriminator)."""
    return {
        "schema": SCHEMA,
        "meta": graph.meta,
        "nodes": [asdict(n) for n in graph.nodes.values()],
        "edges": [asdict(e) for e in graph.edges],
    }


def save_store(graph: WikiGraph, path: str = DEFAULT_PATH) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(graph_to_dict(graph), fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return path


def load_store(path: str = DEFAULT_PATH) -> WikiGraph:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    nodes = {n["id"]: WikiNode(**n) for n in data.get("nodes", [])}
    edges = [WikiEdge(**e) for e in data.get("edges", [])]
    return WikiGraph(nodes=nodes, edges=edges, meta=data.get("meta", {}))


def store_exists(path: str = DEFAULT_PATH) -> bool:
    return os.path.isfile(path)
