#!/usr/bin/env python3
"""graphiti_backend.py — OPTIONAL accelerator: load the deterministic TKG into an embedded, bi-temporal
graph store (Kuzu — one of Graphiti's official drivers). The query-side twin of embed.py / llm.py.

WHY RAW KUZU, NOT THE Graphiti CLIENT (the load-bearing design decision):
  Graphiti's value is (a) a bi-temporal data model (valid_at / invalid_at) and (b) LLM-driven entity/edge
  EXTRACTION from episodes. This wiki forbids LLM-inferred edges (rule R3) — every edge is deterministic
  ([[wikilinks]] + crosslink). And `graphiti_core.Graphiti.__init__` instantiates an LLM client
  UNCONDITIONALLY (before any `add_episode`), which would break the air-gap on import. So we keep Graphiti's
  *bi-temporal model* but DROP its LLM pipeline: we write our already-built nodes/edges straight into the
  embedded Kuzu backend with raw `kuzu.Database`/`kuzu.Connection`, naming the temporal columns `valid_at` /
  `invalid_at` so the result is Graphiti-schema-compatible (a graphiti_core reader could query it) — without
  ever constructing a Graphiti client or calling an LLM. `valid_at` = our `valid_from`; `invalid_at` is
  always NULL (rule R4: no supersession inference).

AIR-GAP CONTRACT (the embed.py / llm.py precedent — selftest enforces it):
  - NO module-scope third-party import. `kuzu` is imported lazily INSIDE connect()/load_graph() only.
  - `available()` is config-only: it uses importlib.util.find_spec (which does NOT import) to see whether
    `kuzu` is installed. It opens no file and no socket.
  - With `kuzu` absent OR `WIKI_TKG` off, every entry point degrades to a no-op/None and the five CLI verbs
    keep answering from the canonical JSON store — the wiki behaves exactly as without this file.
  - Kuzu is EMBEDDED (a local file db) — it opens no network socket. graphiti_core is never imported here.

Enable with `WIKI_TKG=kuzu` (or `graphiti`/`1`). Stdlib only at import; never raises.
"""
import argparse
import importlib.util
import os
import shutil
import sys

from wikikb import paths

# Defensive, import-time-read env guard at MODULE TOP (the BF-5 analog), set with a pure stdlib os write
# before any lazy third-party import — so neither kuzu nor a stray graphiti import phones home. Idempotent.
os.environ.setdefault("GRAPHITI_TELEMETRY_ENABLED", "False")
os.environ.setdefault("KUZU_DISABLE_TELEMETRY", "1")

sys.dont_write_bytecode = True

DB_DIR = str(paths.TKG / "kuzu")          # derived, gitignored (under _meta/tkg/, like graph.json)
_ON = ("kuzu", "graphiti", "1", "on", "true")


def mode():
    return os.environ.get("WIKI_TKG", "off").strip().lower()


def enabled():
    return mode() in _ON


def have_kuzu():
    """True iff `kuzu` is importable — checked WITHOUT importing it (no socket, no side effects)."""
    try:
        return importlib.util.find_spec("kuzu") is not None
    except Exception:
        return False


def have_graphiti():
    try:
        return importlib.util.find_spec("graphiti_core") is not None
    except Exception:
        return False


def available():
    """True iff the backend COULD load: WIKI_TKG enabled AND kuzu installed. Config-only; no db/socket."""
    return enabled() and have_kuzu()


def status_str():
    if not enabled():
        return "tkg backend: off (WIKI_TKG unset/off — the JSON store answers all verbs; this is the default)"
    if not have_kuzu():
        return ("tkg backend: %s requested but `kuzu` not installed — inactive (JSON store still answers all "
                "verbs). Vendor kuzu offline to enable." % mode())
    extra = " (+graphiti_core present — schema is graphiti-compatible)" if have_graphiti() else ""
    return "tkg backend: %s, kuzu available → db=%s%s" % (mode(), DB_DIR, extra)


def connect(db_path=DB_DIR, fresh=False):
    """Open (lazily importing kuzu INSIDE this function) and return (kuzu_module, connection), or None when
    unavailable / on any error. NEVER raises — callers fall back to the JSON store. `fresh=True` rebuilds
    the db dir from scratch (the store is derived)."""
    if not available():
        return None
    try:
        import kuzu  # lazy — never at module scope (air-gap contract)
        if fresh and os.path.isdir(db_path):
            shutil.rmtree(db_path)
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        db = kuzu.Database(db_path)
        return kuzu, kuzu.Connection(db)
    except Exception:
        return None


def load_graph(graph, db_path=DB_DIR):
    """Bulk-load a WikiGraph into embedded Kuzu with a Graphiti-compatible bi-temporal schema (raw Kuzu —
    no GraphitiClient, no LLM). Returns a small summary dict, or None when the backend is unavailable / on
    error (graceful — the JSON store remains canonical). Idempotent: rebuilds the db fresh each call."""
    conn_t = connect(db_path, fresh=True)
    if conn_t is None:
        return None
    _kuzu, conn = conn_t
    try:
        conn.execute("CREATE NODE TABLE IF NOT EXISTS WikiNode("
                     "id STRING, label STRING, domain STRING, title STRING, PRIMARY KEY(id))")
        # One typed rel table; `valid_at`/`invalid_at` mirror Graphiti's bi-temporal edge vocabulary
        # (valid_at = our valid_from; invalid_at always NULL — R4). kind/precision/rel keep our semantics.
        conn.execute("CREATE REL TABLE IF NOT EXISTS EDGE(FROM WikiNode TO WikiNode, "
                     "rel STRING, kind STRING, valid_at STRING, invalid_at STRING, "
                     "valid_from_precision STRING, provenance STRING)")
        for n in graph.nodes.values():
            conn.execute(
                "MERGE (n:WikiNode {id: $id}) SET n.label=$label, n.domain=$domain, n.title=$title",
                {"id": n.id, "label": n.label, "domain": n.domain or "", "title": n.title or ""})
        edges = 0
        for e in graph.edges:
            conn.execute(
                "MATCH (a:WikiNode {id: $s}), (b:WikiNode {id: $d}) "
                "CREATE (a)-[:EDGE {rel:$rel, kind:$kind, valid_at:$vf, invalid_at:$vu, "
                "valid_from_precision:$vp, provenance:$prov}]->(b)",
                {"s": e.src, "d": e.dst, "rel": e.rel, "kind": e.kind,
                 "vf": e.valid_from or "", "vu": e.valid_until or "",
                 "vp": e.valid_from_precision or "", "prov": e.provenance or ""})
            edges += 1
        return {"db": db_path, "nodes": len(graph.nodes), "edges": edges,
                "graphiti_compatible": True, "client_used": False}
    except Exception as exc:
        return {"db": db_path, "error": str(exc)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", action="store_true", help="report backend state (no db/socket)")
    ap.add_argument("--load", action="store_true", help="ACTIVE: build the graph and load it into Kuzu")
    args = ap.parse_args()
    if args.load:
        if not available():
            print("load: unavailable — %s" % status_str())
            sys.exit(0)
        from wikikb.tkg import model
        res = load_graph(model.build_graph())
        print("load: %s" % (res if res else "failed (see status)"))
        sys.exit(0)
    print(status_str())


if __name__ == "__main__":
    main()
