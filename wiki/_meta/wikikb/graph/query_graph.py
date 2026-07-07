"""graph/query_graph.py — the QUERY operation as a LangGraph StateGraph (the optional online tier).

The control flow CLAUDE.md's QUERY op describes is a branching, gated graph — NOT a linear chain:
    route -> retrieve -> (thin? -> expand) -> gate -> synthesize -> END
so it is modelled as a langgraph.StateGraph with a conditional edge (the council's LangGraph-over-LCEL
decision). langgraph is imported INSIDE build_query_graph() so THIS MODULE imports stdlib-safe (the
air-gap invariant): `import graph.query_graph` never pulls in langgraph; only building the graph does,
and it raises a clear error when langgraph is absent (use the host-runtime QUERY path instead).

No LangChain / LCEL (synthesize is a plain node calling llm.complete); no checkpointer by default
(single-shot DAG) and no SqliteSaver (COUNCIL-DIRECTIVES.md §5). The nodes (graph/nodes.py) wrap the
real tools + the real gate.

Usage (requires the optional online tier installed — see _meta/requirements-online.txt):
    from wikikb.graph.query_graph import run_query
    result = run_query("rp-initiated logout id_token_hint", question_tier="conceptual")
"""
import sys
from typing import Any, List, Optional, Tuple
try:
    from typing import TypedDict
except ImportError:                       # py<3.8 (not expected here; py3.14)
    TypedDict = dict

sys.dont_write_bytecode = True
from . import nodes                       # stdlib-safe node functions


class WikiState(TypedDict, total=False):
    """The QUERY graph state (merged here per §5 cut #3 — no separate state.py)."""
    query: str
    question_tier: Optional[str]
    domain: Optional[str]
    confident: bool
    candidates: List[Tuple[str, str]]
    graph_notes: List[str]
    thin: bool
    covered: Optional[list]
    banner: List[str]
    answer: str
    used: List[str]
    page_fm: dict
    k: int


def build_query_graph(checkpointer=None):
    """Compile the QUERY StateGraph. Raises RuntimeError when langgraph is absent — the graph is the
    OPTIONAL online tier; the default QUERY path is the host runtime over wiki/CLAUDE.md."""
    try:
        from langgraph.graph import StateGraph, END
    except Exception as e:
        raise RuntimeError(
            "LangGraph not installed — the QUERY graph is the optional online tier. Install per "
            "_meta/requirements-online.txt, or use the host-runtime QUERY path (wiki/CLAUDE.md). (%s)" % e)
    g = StateGraph(WikiState)
    g.add_node("route", nodes.route_node)
    g.add_node("retrieve", nodes.retrieve_node)
    g.add_node("expand", nodes.expand_node)
    g.add_node("gate", nodes.gate_node)
    g.add_node("synthesize", nodes.synthesize_node)
    g.set_entry_point("route")
    g.add_edge("route", "retrieve")
    # 2026-07-05: expand is now UNCONDITIONAL (was: only when thin) — the live-query bank proved
    # expand-on-thin loses answers whose notes the query-matched wiki pages directly cite. The
    # `thin` flag is still computed/threaded for observability.
    g.add_edge("retrieve", "expand")
    g.add_edge("expand", "gate")
    g.add_edge("gate", "synthesize")
    g.add_edge("synthesize", END)
    # §5 cut #4: the gate is deterministic and QUERY is a SINGLE-SHOT DAG — nothing to checkpoint, so
    # default to NO checkpointer. (A default MemorySaver would force every .invoke() to pass a
    # configurable.thread_id and crash run_query; no SqliteSaver either.) A caller may still pass one.
    return g.compile(checkpointer=checkpointer) if checkpointer is not None else g.compile()


def run_query(query, question_tier=None, k=5):
    """Build + invoke the QUERY graph for a single question (optional online tier; raises offline)."""
    app = build_query_graph()
    return app.invoke({"query": query, "question_tier": question_tier, "k": k})
