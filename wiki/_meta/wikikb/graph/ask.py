"""graph/ask.py — `wikikb ask "<question>"`: the QUERY pipeline as one cited, gated answer.

Sequences the graph/nodes.py functions directly — route -> retrieve -> (expand if thin) -> gate ->
synthesize — so it needs NO langgraph. The StateGraph in query_graph.py is the OPTIONAL online tier;
this is the always-available host path that runs the SAME nodes (faithful: it reuses kb/route/expand,
the real lint.gate_banner, and the local llm.complete — nothing re-implemented).

Offline (WIKI_LLM=off, the default) synthesize_node returns the deterministic extractive answer, so
`ask` works with zero network and zero extra deps. With WIKI_LLM=local it returns the local model's
grounded answer. A tripped Confidence banner is already prepended by synthesize_node. Dense retrieval
is used automatically when the embedding model + index are present (run under the venv that has them).

    python3 -m wikikb ask "how do I bind a token to a client key" --domain keycloak
    python3 -m wikikb ask "<alert/symptom>" --json        # agent-consumable
"""
import argparse
import json
import sys

sys.dont_write_bytecode = True
from wikikb.graph import nodes              # stdlib-safe node functions (no langgraph)
from wikikb.retrieval import kb             # to resolve cited reference notes -> source URLs


def ask(query, domain=None, k=5, question_tier=None):
    """Run the QUERY node sequence on a plain state dict and return the final state."""
    state = {"query": query, "k": k, "question_tier": question_tier}
    if domain:
        state["domain"] = domain
    state.update(nodes.route_node(state))
    state.update(nodes.retrieve_node(state))
    if state.get("thin"):
        state.update(nodes.expand_node(state))
    state.update(nodes.gate_node(state))
    state.update(nodes.synthesize_node(state))
    # QUERY-side anti-fabrication guard (deterministic, model-independent): an identifier asked
    # about but absent from the entire domain corpus gets a leading NOT-FOUND verdict — the model
    # never gets to define it from parametric memory (adjacent-real-substitution failure mode).
    from wikikb.quality import lint
    guard = lint.identifier_guard(query, state.get("domain"))
    if guard:
        lines = []
        for gitem in guard:
            near = ", ".join("`%s`" % n for n in gitem["nearest"]) or "none found"
            lines.append("⚠️ `%s` does NOT appear anywhere in the `%s` reference corpus — treat it as "
                         "non-existent; do not define it. Nearest real option(s): %s."
                         % (gitem["token"], state.get("domain"), near))
        state["guard"] = guard
        state["answer"] = "\n".join(lines) + "\n\n" + state.get("answer", "")
    return state


def ask_graph(query, domain=None, k=5, question_tier=None):
    """Same QUERY nodes as ask(), but orchestrated through the compiled LangGraph StateGraph (the
    OPTIONAL online tier). Identical result to ask() — the graph is the substrate, not a better answer;
    it exists so `/query` genuinely runs the StateGraph. Raises if langgraph is absent (run under the
    venv that has it: wiki/_meta/.venv-online)."""
    from wikikb.graph.query_graph import build_query_graph
    init = {"query": query, "k": k, "question_tier": question_tier}
    if domain:
        init["domain"] = domain            # route_node honors a pre-set domain (same as ask())
    return build_query_graph().invoke(init)


def references(domain, used):
    """Resolve the cited reference-note ids -> {id, source} from their frontmatter (RH ground truth).
    These are the notes the answer was grounded in; the id is resolvable in the vault either way."""
    by_id = {r.get("id"): r for r in (kb.load(domain) or [])}
    out = []
    for cid in used:
        r = by_id.get(cid) or {}
        out.append({"id": cid, "source": r.get("source") or r.get("url") or ""})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?",
                    help="the question (or use --query-file to avoid shell-quoting issues)")
    ap.add_argument("--query-file", dest="query_file",
                    help="read the question from this file verbatim — robust against quotes/newlines "
                         "in the query (the /query opencode command writes the question here)")
    ap.add_argument("--domain", help="skip routing and search this domain")
    ap.add_argument("--k", type=int, default=5, help="lexical candidates to retrieve (default 5)")
    ap.add_argument("--tier", dest="question_tier",
                    help="question tier for the H1 coverage gate (conceptual|support-kb|scenarios)")
    ap.add_argument("--json", action="store_true", help="structured output for agents")
    ap.add_argument("--graph", action="store_true",
                    help="orchestrate via the LangGraph StateGraph (optional online tier; needs "
                         "langgraph). Same nodes/result as the default linear path.")
    args = ap.parse_args()

    query = args.query
    if args.query_file:
        query = open(args.query_file, encoding="utf-8").read().strip()
    if not query:
        ap.error("provide a query argument or --query-file")

    runner = ask_graph if args.graph else ask
    st = runner(query, domain=args.domain, k=args.k, question_tier=args.question_tier)
    refs = references(st.get("domain"), st.get("used", []))

    if args.json:
        print(json.dumps({
            "query": query,
            "domain": st.get("domain"),
            "confident": st.get("confident"),
            "thin": st.get("thin"),
            "banner": st.get("banner") or [],
            "guard": st.get("guard") or [],
            "answer": st.get("answer", ""),
            "references": refs,
        }, indent=2, ensure_ascii=False))
        return

    print(st.get("answer", "(no answer)"))
    if refs:
        print("\nReferences (RH ground-truth notes):")
        for rf in refs:
            print("  - %s%s" % (rf["id"], ("  %s" % rf["source"]) if rf["source"] else ""))
    else:
        print("\n(no candidates matched — try --domain or rephrase)")


if __name__ == "__main__":
    main()
