"""graph/ingest_graph.py — the INGEST operation as a manifest-gated LangGraph loop (optional tier).

INGEST is a DELTA LOOP, not a chain: consult the manifest for sources cited but not yet recorded, and
for each one find-or-create the synthesized page, assign provenance, record it, then loop until the
delta is empty. Modelled as a langgraph.StateGraph with a CYCLE (delta -> extract -> provenance ->
record -> delta) — the loop is exactly why this is a graph, not a chain. langgraph is imported INSIDE
build_ingest_graph() so this module imports stdlib-safe (the air-gap invariant).

Nodes call the REAL tools: manifest (delta + record), and the optional llm gateway for the extract
step (extractive fallback offline). DRY-RUN by default — the manifest write happens only with
apply=True, so the graph is safe to exercise offline and never mutates the vault unasked. Refreshing
the graph/routing indexes (crosslink.py / index.py) is left to the operator post-batch, as today.
No LangChain/LCEL; no SqliteSaver (COUNCIL-DIRECTIVES.md §5).

Usage (optional online tier; raises offline):
    from wikikb.graph.ingest_graph import run_ingest
    run_ingest(apply=False)        # dry-run the delta loop
"""
import sys
from typing import List, Optional
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

sys.dont_write_bytecode = True
from wikikb.build import manifest    # the real delta manifest (collect / load / cmd_record)
from wikikb.online import llm         # optional local-loopback gateway (None offline -> extractive)


class IngestState(TypedDict, total=False):
    apply: bool
    pending: List[str]
    current: Optional[str]
    drafts: dict
    done: List[str]


def delta_node(state):
    """The manifest delta: source tokens cited in the wiki but not yet recorded (the work list). On
    the first visit it computes the list; subsequent visits drain the threaded `pending` (so the loop
    terminates even in dry-run, where `recorded` never grows)."""
    pending = state.get("pending")
    if pending is None:
        cited = manifest.collect()                      # token -> citing pages (real tool)
        recorded = manifest.load().get("sources", {})
        pending = sorted(set(cited) - set(recorded))
    current = pending[0] if pending else None
    return {"pending": pending[1:] if pending else [], "current": current,
            "done": state.get("done", [])}


def has_pending(state):
    """Conditional edge: keep looping while a source remains, else END."""
    return "extract" if state.get("current") else "END"


def extract_node(state):
    """Find-or-create the page for the current source. The LLM leaf (llm.complete) drafts the
    synthesis; offline it degrades to an extractive stub. No vault write here — drafts only."""
    tok = state.get("current")
    messages = [{"role": "system", "content": "Summarize the source into durable, cited wiki facts."},
                {"role": "user", "content": "Source token: %s" % tok}]
    resp = llm.complete(messages)
    text = llm.text_of(resp) if resp is not None else None
    drafts = dict(state.get("drafts", {}))
    drafts[tok] = {"source": tok, "mode": "llm" if text else "extractive",
                   "text": text or ("[extractive] would synthesize a page for %s" % tok)}
    return {"drafts": drafts}


def provenance_node(state):
    """Assign per-claim provenance for the current draft — never mechanical in real INGEST, but here
    the draft mode picks the honest default (extractive draft -> extracted; llm draft -> inferred)."""
    tok = state.get("current")
    drafts = dict(state.get("drafts", {}))
    if tok in drafts:
        ext = 1 if drafts[tok]["mode"] == "extractive" else 0
        drafts[tok]["provenance"] = {"extracted": ext, "inferred": 1 - ext, "ambiguous": 0}
    return {"drafts": drafts}


def record_node(state):
    """Record the source in the manifest (the REAL tool) — ONLY when apply=True. Dry-run by default,
    so exercising the loop offline mutates nothing."""
    tok = state.get("current")
    done = list(state.get("done", []))
    if tok:
        if state.get("apply"):
            try:
                import argparse
                manifest.cmd_record(argparse.Namespace(source=tok, pages="", date=None))
            except Exception:
                pass
        done.append(tok)
    return {"done": done, "current": None}


def build_ingest_graph():
    """Compile the INGEST StateGraph (a cycle). Raises when langgraph is absent — the optional online
    tier; the default INGEST path is the host runtime over wiki/CLAUDE.md."""
    try:
        from langgraph.graph import StateGraph, END
    except Exception as e:
        raise RuntimeError(
            "LangGraph not installed — the INGEST graph is the optional online tier. Use the "
            "host-runtime INGEST path (wiki/CLAUDE.md). (%s)" % e)
    g = StateGraph(IngestState)
    g.add_node("delta", delta_node)
    g.add_node("extract", extract_node)
    g.add_node("provenance", provenance_node)
    g.add_node("record", record_node)
    g.set_entry_point("delta")
    g.add_conditional_edges("delta", has_pending, {"extract": "extract", "END": END})
    g.add_edge("extract", "provenance")
    g.add_edge("provenance", "record")
    g.add_edge("record", "delta")                      # loop until the delta is empty
    return g.compile()


def run_ingest(apply=False):
    """Build + run the INGEST delta loop (optional online tier; raises offline)."""
    app = build_ingest_graph()
    # size the recursion limit to the delta: the 4-node cycle uses ~4 super-steps per source, so a
    # fixed 500 would GraphRecursionError on a large delta (e.g. ~156 pending -> ~625 needed). x8 +
    # headroom, computed from the real delta (cheap stdlib read).
    pending = sorted(set(manifest.collect()) - set(manifest.load().get("sources", {})))
    limit = max(100, 8 * (len(pending) + 2))
    return app.invoke({"apply": apply}, {"recursion_limit": limit})
