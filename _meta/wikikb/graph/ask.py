"""graph/ask.py — `wikikb ask "<question>"`: the QUERY pipeline as one cited, gated answer.

GRAPH BY DEFAULT (2026-07-09): when langgraph is installed, ask() orchestrates through the compiled
StateGraph in query_graph.py; when it is absent, ask() degrades to sequencing the SAME graph/nodes.py
functions linearly — route -> retrieve -> expand -> gate -> synthesize. Identical nodes, identical
result; langgraph is imported lazily so importing this module stays stdlib-safe (the air-gap
invariant). Faithful either way: it reuses kb/route/expand, the real lint.gate_banner, and the local
llm.complete — nothing re-implemented.

Offline (WIKI_LLM=off, the default) synthesize_node returns the deterministic extractive answer, so
`ask` works with zero network and zero extra deps. With WIKI_LLM=local it returns the local model's
grounded answer. A tripped Confidence banner is already prepended by synthesize_node. Dense retrieval
is used automatically when the embedding model + index are present (run under the venv that has them).

    python3 -m wikikb ask "how do I bind a token to a client key" --domain keycloak
    python3 -m wikikb ask "<alert/symptom>" --json        # agent-consumable
"""
import argparse
import json
import os
import sys

sys.dont_write_bytecode = True
from wikikb.graph import nodes              # stdlib-safe node functions (no langgraph)
from wikikb.retrieval import kb             # to resolve cited reference notes -> source URLs


def ask(query, domain=None, k=5, question_tier=None, require_graph=False, no_expand=False):
    """Run the QUERY pipeline and return the final state — via the LangGraph StateGraph when
    langgraph is installed (the default orchestrator), else the same nodes sequenced linearly.
    require_graph=True raises instead of degrading (strict --graph mode)."""
    state = {"query": query, "k": k, "question_tier": question_tier,
             "no_expand": no_expand}
    if domain:
        state["domain"] = domain
    try:
        from wikikb.graph.query_graph import build_query_graph
        app = build_query_graph()
    except RuntimeError:                      # langgraph absent — the offline linear path
        if require_graph:
            raise
        app = None
    if app is not None:
        state = dict(app.invoke(state))
        state["orchestrator"] = "langgraph"
    else:
        state.update(nodes.route_node(state))
        state.update(nodes.retrieve_node(state))
        # ALWAYS graph-expand (2026-07-05): the live-query bank proved expand-only-when-thin loses real
        # answers — lexical/dense top-k misses notes that query-matched wiki pages directly cite (e.g.
        # AD delegation/sizing facts). Seed-source notes are high-precision and appended after the
        # ranked hits, so they add recall without displacing them. (Was: only when thin < 3 hits.)
        state.update(nodes.expand_node(state))
        state.update(nodes.gate_node(state))
        state.update(nodes.synthesize_node(state))
        state["orchestrator"] = "linear"
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


def ask_graph(query, domain=None, k=5, question_tier=None, no_expand=False):
    """STRICT graph mode: ask() but raises when langgraph is absent instead of degrading to the
    linear path (run under the venv that has it: wiki/_meta/.venv-online). ask() already prefers
    the StateGraph when available — this only removes the fallback. Kept for the `--graph` flag
    and callers that must prove the StateGraph ran; now also applies the identifier guard (it
    previously bypassed it)."""
    return ask(query, domain=domain, k=k, question_tier=question_tier,
               require_graph=True, no_expand=no_expand)


_WITHHELD_LINE = ("[withheld by strict grounding mode — grounding_fail=%s, ungrounded_identifiers=%s] "
                  "cited: %s")


def strict_default():
    """Operator-level strict switch, honored consistently by every surface (CLI/serve/mcp):
    WIKI_STRICT_GROUNDING=1 makes strict withholding the default; a per-call flag still wins."""
    return os.environ.get("WIKI_STRICT_GROUNDING") == "1"


def resolve_strict(explicit):
    """Tri-state per-call precedence over the env default: explicit True/False (the caller said so)
    wins outright — including an explicit False overriding WIKI_STRICT_GROUNDING=1; only an
    UNSPECIFIED call (None) falls back to strict_default(). Every surface resolves through here."""
    return strict_default() if explicit is None else bool(explicit)


def public_result(query, st, refs, strict=False):
    """The ONE result serializer (WI-7) — CLI --json, serve /ask, and mcp ask all return exactly
    this shape, so no surface can drift back to a private field set. Grounding status is ALWAYS
    structured (D3): `grounding_fail`, `ungrounded_identifiers` (always a list, never an omitted
    key), `grounding_basis`, and `withheld` are present on every result — an automated consumer
    never parses warning prose. Flag-by-default: the (already banner-prefixed) answer text is
    served as-is. strict=True — the opt-in for unattended consumers (recommended for SRE
    automation) — WITHHOLDS the prose entirely when the answer is ungrounded (grounding_fail) or
    asserts identifiers its cited sources don't contain, replacing it with a deterministic
    withheld line. judge_verdict stays nullable (present only when the advisory judge ran)."""
    withheld = False
    answer = st.get("answer", "")
    ungrounded = st.get("ungrounded_identifiers") or []
    if strict and (st.get("grounding_fail") or ungrounded):
        withheld = True
        answer = _WITHHELD_LINE % (st.get("grounding_fail", False), ungrounded or "[]",
                                   ", ".join(st.get("used", [])[:5]) or "(none)")
    wiki_pages = list(dict.fromkeys(st.get("graph_pages") or []))
    reference_groups = {
        "rh_ground_truth": [{"token": "ref:" + r["id"], **r} for r in refs],
        "wiki": [{"slug": s, "wikilink": "[[%s]]" % s} for s in wiki_pages],
    }
    rh_lines = ["- `ref:%s` — %s" % (r["id"], r.get("source") or "vault reference note")
                for r in refs] or ["- No verified RH ground-truth source was cited."]
    wiki_lines = ["- [[%s]]" % s for s in wiki_pages] or ["- No synthesized Wiki page was used."]
    answer = answer.rstrip() + ("\n\n## References (canonical)\n\n### RH ground-truth\n%s\n\n"
                                "### Wiki\n%s" % ("\n".join(rh_lines), "\n".join(wiki_lines)))
    out = {
        "query": query,
        "orchestrator": st.get("orchestrator"),   # "langgraph" (default when installed) | "linear"
        "domain": st.get("domain"),
        "confident": st.get("confident"),
        "thin": st.get("thin"),
        "banner": st.get("banner") or [],
        "guard": st.get("guard") or [],
        "answer": answer,
        "cited": st.get("used", []),              # the REAL cited set (nodes.synthesize_node)
        "grounding_fail": st.get("grounding_fail", False),
        "ungrounded_identifiers": ungrounded,
        "grounding_basis": st.get("grounding_basis"),
        "withheld": withheld,
        "references": refs,
        "reference_groups": reference_groups,
    }
    if st.get("judge_verdict") is not None:       # nullable: key present only when the judge ran
        out["judge_verdict"] = st["judge_verdict"]
    return out


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
    ap.add_argument("--strict", action=argparse.BooleanOptionalAction, default=None,
                    help="withhold the answer prose when it is ungrounded or asserts identifiers "
                         "its cited sources don't contain (recommended for unattended consumers; "
                         "WIKI_STRICT_GROUNDING=1 makes this the default on every surface — "
                         "--no-strict overrides it per call)")
    ap.add_argument("--graph", action="store_true",
                    help="STRICT graph mode: fail if langgraph is absent instead of degrading to the "
                         "linear path. (The StateGraph is already the default when langgraph is "
                         "installed.)")
    ap.add_argument("--no-expand", action="store_true",
                    help="disable synthesized-page graph expansion; retain lexical candidates unchanged")
    args = ap.parse_args()

    query = args.query
    if args.query_file:
        query = open(args.query_file, encoding="utf-8").read().strip()
    if not query:
        ap.error("provide a query argument or --query-file")

    runner = ask_graph if args.graph else ask
    st = runner(query, domain=args.domain, k=args.k, question_tier=args.question_tier,
                no_expand=args.no_expand)
    refs = references(st.get("domain"), st.get("used", []))
    out = public_result(query, st, refs, strict=resolve_strict(args.strict))

    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    print(out.get("answer") or "(no answer)")


if __name__ == "__main__":
    main()
