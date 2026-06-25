"""graph/nodes.py — the QUERY/INGEST graph nodes. stdlib-safe (no langgraph/litellm at module scope).

Each node is a plain function(state: dict) -> dict-update — so it is unit-testable WITHOUT langgraph
(the package degrades gracefully and the faithfulness probes can exercise nodes directly). Every node
calls the EXISTING deterministic tools (kb/route/expand) or the real gate (lint.gate_banner) or the
optional local gateway (llm.complete) — none of that logic is re-implemented here (the faithfulness
invariant, BF-4). Recall-shaped ranking reuses kb.score, exactly as eval.py does.
"""
import sys

sys.dont_write_bytecode = True

from wikikb.retrieval import kb          # the real loader + ranker (faithful)
from wikikb.retrieval import route       # the real query->domain router
from wikikb.retrieval import expand      # the real graph expansion
from wikikb.quality import lint        # the real Confidence gate (gate_banner / page_gate_verdict)
from wikikb.quality import coverage    # tiers-covered for the H1 coverage arm (was gate_probe)
from wikikb.online import llm         # optional local-loopback LLM gateway (None offline)

CTX_CHARS = 8000   # cap the assembled context fed to the model (keeps the prompt bounded)
THIN_K = 3         # fewer than this many lexical hits -> "thin" -> graph-expand to rescue


# ---------- QUERY nodes -----------------------------------------------------------------------

def route_node(state):
    """route.route() -> the domain to search + the router's confidence (Phase-1)."""
    doms, confident = route.route(state["query"])
    domain = state.get("domain") or (doms[0] if doms else None)
    return {"domain": domain, "confident": confident}


def retrieve_node(state):
    """Lexical candidate retrieval — reuses kb.load + kb.score + kb's ordering (identical to eval.py's
    recall path; faithful). `thin` drives the conditional edge to graph expansion."""
    domain, query, k = state["domain"], state["query"], state.get("k", 5)
    recs = [r for r in (kb.load(domain) or []) if r.get("body_status") == "fetched"]
    terms = kb.toks(query)
    # identical ordering to kb.py:226 / eval.rank(): (-score, then newest version) — the secondary
    # key keeps score-tied notes of differing version in the SAME order the retriever/eval use.
    scored = sorted(((kb.score(r, terms, kb.body_text(r)), r) for r in recs),
                    key=lambda x: (-x[0], -kb.vkey(x[1].get("version"))[0] if x[1].get("version") else 0))
    cands = [(r.get("id"), kb.body_text(r)) for s, r in scored[:k] if s > 0]
    return {"candidates": cands, "thin": len(cands) < THIN_K}


def expand_node(state):
    """expand.graph_notes() -> reference notes reachable 1-hop from the matched synthesized pages.
    Adds any not already retrieved (the multi-hop entry-point rescue), with their bodies."""
    domain, query = state["domain"], state["query"]
    notes = expand.graph_notes(domain, query) or set()
    have = {cid for cid, _ in state.get("candidates", [])}
    new = sorted(n for n in notes if n not in have)
    bodies = {}
    if new:
        for r in (kb.load(domain) or []):
            if r.get("id") in new:
                bodies[r.get("id")] = kb.body_text(r)
    extra = [(nid, bodies.get(nid, "")) for nid in new]
    return {"graph_notes": sorted(notes), "candidates": state.get("candidates", []) + extra}


def gate_node(state):
    """Apply the FULL Confidence gate via lint.gate_banner — the SAME rule lint enforces and the CI
    probes assert (faithfulness, BF-4). H1 uses the routed domain's tiers-covered. H2/H3/H4/L apply to
    a candidate PAGE's frontmatter via state['page_fm'] — which the run_query convenience does NOT
    thread, so in the auto-graph only H1 fires; the page arms run when a host/file-back step supplies
    page_fm (and they are exercised directly by gate_page_probe + selftest)."""
    domain = state.get("domain")
    try:
        covered = coverage.load_tiers_covered().get(domain)
    except Exception:
        covered = None
    banner = lint.gate_banner(state.get("page_fm") or {},
                              question_tier=state.get("question_tier"), covered=covered)
    return {"banner": banner, "covered": covered}


def synthesize_node(state):
    """The ONE LLM leaf: prompt = system + question + retrieved context, sent through the local gateway
    (llm.complete). NO LangChain/LCEL — a plain call. When the gateway is off/absent, complete() returns
    None and we fall back to a deterministic extractive answer (the host-runtime / offline path), so the
    graph degrades gracefully. A tripped Confidence banner is prepended (never serve inference as fact)."""
    cands = state.get("candidates", [])
    ctx = "\n\n".join(body for _, body in cands if body)[:CTX_CHARS]
    messages = [
        {"role": "system", "content": "Answer the question using ONLY the provided context; cite note ids."},
        {"role": "user", "content": "Question: %s\n\nContext:\n%s" % (state["query"], ctx)},
    ]
    resp = llm.complete(messages)
    answer = llm.text_of(resp) if resp is not None else None
    if answer is None:
        ids = ", ".join(cid for cid, _ in cands[:5]) or "(no candidates)"
        answer = "[extractive fallback — LLM gateway inactive] top sources: %s" % ids
    banner = state.get("banner") or []
    if banner:
        answer = "⚠️ " + " | ".join(banner) + "\n\n" + answer
    return {"answer": answer, "used": [cid for cid, _ in cands]}
