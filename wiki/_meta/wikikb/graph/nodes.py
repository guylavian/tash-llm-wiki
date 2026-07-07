"""graph/nodes.py — the QUERY/INGEST graph nodes. stdlib-safe (no langgraph/litellm at module scope).

Each node is a plain function(state: dict) -> dict-update — so it is unit-testable WITHOUT langgraph
(the package degrades gracefully and the faithfulness probes can exercise nodes directly). Every node
calls the EXISTING deterministic tools (kb/route/expand) or the real gate (lint.gate_banner) or the
optional local gateway (llm.complete) — none of that logic is re-implemented here (the faithfulness
invariant, BF-4). Recall-shaped ranking reuses kb.score, exactly as eval.py does.
"""
import re
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

# Numeric-table-serving-fidelity: a plain `[:CTX_CHARS]` slice can land mid-row inside a markdown
# table or list, silently dropping the numbers a sizing/threshold answer depends on (and leaving a
# half-row that reads as a complete fact). _assemble_context cuts on LINE boundaries only; when the
# cut would land inside a table/list run it trims the partial run entirely and appends an explicit
# truncation marker naming the note — a missing table that says so beats a corrupted one.
_TABLE_OR_LIST_LINE_RE = re.compile(r"^\s*(\||[-*+]\s|\d+\.\s)")
_TRUNC_MARK = "[…context truncated mid-table — open %s for the full table]"


def _fit_lines(body, budget):
    """Largest whole-line prefix of `body` that fits `budget` chars — a row is either fully in or
    fully out, so a numeric cell can never be clipped into a different number. Returns
    (text, cut_tabular): cut_tabular is True when the first DROPPED line is a table/list row,
    i.e. the cut clipped a run and the caller must flag the omission instead of staying silent.
    Kept rows stay kept (they are complete and correct; the marker covers the missing tail)."""
    kept, used = [], 0
    for ln in body.splitlines():
        need = len(ln) + (1 if kept else 0)
        if used + need > budget:
            return "\n".join(kept), bool(_TABLE_OR_LIST_LINE_RE.match(ln))
        kept.append(ln)
        used += need
    return "\n".join(kept), False


def _fit_candidate(cid, body, budget, first):
    """Fit ONE candidate's body into `budget` chars (whole-line, via _fit_lines), reserving room for
    the header and a possible _TRUNC_MARK. Returns (piece_or_None, chars_used) — None when even the
    header+marker don't fit in this share (caller skips and moves on, never crashes)."""
    header = "[%s]\n" % cid
    sep = 2 if not first else 0                     # the "\n\n" join separator
    avail = budget - sep - len(header) - len(_TRUNC_MARK % cid) - 1
    if avail <= 0:
        return None, 0
    if len(body) <= avail:
        piece = header + body
        return piece, sep + len(piece)
    fitted, cut_tabular = _fit_lines(body, avail)
    piece = header + fitted
    if cut_tabular:
        piece += "\n" + _TRUNC_MARK % cid
    return piece, sep + len(piece)


def _assemble_context(cands, limit=CTX_CHARS):
    """Join candidate (id, body) pairs into one `[id]\\n<body>` context string capped at `limit`
    chars. Fair-share budgeting (fixes the 2026-07 context-starvation bug: one huge rank-1 note
    was evicting every other candidate): each candidate's share is `remaining // remaining_count`,
    recomputed as we go, so a candidate that needs less than its share leaves the leftover for the
    ones after it — every candidate gets SOME context before any one of them gets all of it. The
    cut is still whole-line only (see _fit_lines) and a clipped table run still gets _TRUNC_MARK,
    now per-candidate rather than only on the last one served."""
    cands = [(cid, body) for cid, body in cands if body]
    out, remaining = [], limit
    for i, (cid, body) in enumerate(cands):
        share = remaining // (len(cands) - i)
        piece, used = _fit_candidate(cid, body, share, first=not out)
        if piece is None:
            continue                                # this share was too small even for the header — skip, try next
        out.append(piece)
        remaining -= used
    return "\n\n".join(out)


# ---------- QUERY nodes -----------------------------------------------------------------------

def route_node(state):
    """route.route() -> the domain to search + the router's confidence (Phase-1)."""
    doms, confident = route.route(state["query"])
    domain = state.get("domain") or (doms[0] if doms else None)
    return {"domain": domain, "confident": confident}


def retrieve_node(state):
    """Candidate retrieval — reuses kb.load + kb.score + kb's ordering (identical to eval.py's recall
    path; faithful). When the dense embedding model+index are present, fuses the lexical and dense
    rankings via RRF — identical to kb.py --hybrid — so the answer path gets the paraphrase lift Phase 1
    built. Lazy+guarded: with the model/index absent it DEGRADES to the exact lexical baseline (and the
    evaluate.rank() faithful ordering). `thin` drives the conditional edge to graph expansion."""
    domain, query, k = state["domain"], state["query"], state.get("k", 5)
    recs = [r for r in (kb.load(domain) or []) if r.get("body_status") == "fetched"]
    terms = kb.expand_query_terms(domain, kb.toks(query))
    idf, avgdl = kb.build_idf(recs), kb.avg_dl(recs)   # once per query, same pool eval.rank() uses
    # identical ordering to kb.py:226 / eval.rank(): (-score, then newest version) — the secondary
    # key keeps score-tied notes of differing version in the SAME order the retriever/eval use.
    scored = sorted(((kb.score(r, terms, kb.body_text(r), idf, avgdl), r) for r in recs),
                    key=lambda x: (-x[0], -kb.vkey(x[1].get("version"))[0] if x[1].get("version") else 0))
    dense = None
    try:                                          # lazy + guarded (air-gap): None when model/index absent
        from wikikb.retrieval import embed
        dense = embed.dense_rank(domain, query)
    except Exception:
        dense = None
    if dense:                                     # hybrid: RRF-fuse lexical + dense, incl. dense-only notes
        rec_by_id = {r.get("id"): r for r in recs}
        fused, seen = [], set()
        for sid in embed.rrf_fuse([r.get("id") for _, r in scored], dense):
            r = rec_by_id.get(sid)
            if r is not None and sid not in seen:
                seen.add(sid)
                fused.append(r)
        cands = [(r.get("id"), kb.body_text(r)) for r in fused[:k]]
    else:                                         # UNCHANGED lexical baseline (faithful to eval.rank())
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
    # Honesty note (validator defect D8): with no question_tier the H1 arm silently skips, so an
    # untiered break-fix ask against a partially-covered domain returns banner=[] — a false all-clear.
    # Say the gate wasn't evaluated instead of staying silent. Deterministic, never suppresses H arms.
    ALL_TIERS = {"conceptual", "support-kb", "scenarios"}
    if state.get("question_tier") is None and covered and set(covered) < ALL_TIERS:
        banner = banner + ["coverage gate not evaluated — no question tier supplied and domain %r "
                           "covers only %s; pass --tier conceptual|support-kb|scenarios (H1-unknown)"
                           % (domain, list(covered))]
    return {"banner": banner, "covered": covered}


# Lenient on FORMAT (colon optional, any case — small local models approximate the token),
# strict on MEMBERSHIP (id must be in the retrieved candidate set) — that is the security property.
_CITE_RE = re.compile(r"\[cite[:\s]\s*([A-Za-z0-9._/-]+)\]", re.IGNORECASE)
_GROUNDING_FAIL_BANNER = ("Ungrounded synthesis — the model cited none of the retrieved sources; "
                          "treat as inference, verify the References.")
_VERDICT_RE = re.compile(r"\b(SUPPORTED|PARTIAL|UNSUPPORTED)\b", re.IGNORECASE)
_JUDGE_ADVISORY_BANNER = "judge (advisory): answer not supported by cited sources"


def _judge_verdict(query, answer, ctx):
    """ADVISORY ONLY — ask the judge model (llm.complete_routed(tier='judge')) whether `answer` is
    actually backed by `ctx` (the same capped candidate bodies the answering model saw). Returns
    {'verdict': SUPPORTED|PARTIAL|UNSUPPORTED, 'raw': <judge's line>} or None on any absence/failure.
    NEVER touches lint.gate_banner or the H-arm logic — this is an annotation on the state, not a gate."""
    messages = [
        {"role": "system", "content": (
            "You are a strict fact-checking judge. Given a question, a candidate answer, and the "
            "source notes it should be grounded in, reply with ONE line: the verdict SUPPORTED, "
            "PARTIAL, or UNSUPPORTED, followed by which cited note ids are actually supported by "
            "the sources.")},
        {"role": "user", "content": "Question: %s\n\nAnswer:\n%s\n\nSource notes:\n%s" % (query, answer, ctx)},
    ]
    resp = llm.complete_routed(messages, tier="judge")
    text = llm.text_of(resp) if resp is not None else None
    if not text:
        return None
    m = _VERDICT_RE.search(text)
    return {"verdict": m.group(1).upper() if m else "PARTIAL", "raw": text.strip()}


def synthesize_node(state):
    """The ONE LLM leaf: prompt = system + question + retrieved context, sent through the local gateway
    (llm.complete). NO LangChain/LCEL — a plain call. When the gateway is off/absent, complete() returns
    None and we fall back to a deterministic extractive answer (the host-runtime / offline path), so the
    graph degrades gracefully. A tripped Confidence banner is prepended (never serve inference as fact).

    Real citation chain: the system prompt requires an inline `[cite: <note-id>]` after every claim, and
    each context chunk is labelled with its own id so the model has something legal to cite. `used` is
    then the REAL cited set — parsed cite tokens intersected with the candidate ids actually offered, not
    "the top candidates" (that would be a retrieval fact, not a citation claim). If the model answered but
    cited none of its sources, `grounding_fail` fires and its own banner is prepended ahead of the
    Confidence-gate banner — an answer that cites nothing is a stronger red flag than a gated-but-cited
    one. The offline extractive fallback is unchanged: `used` = top candidates, `grounding_fail` = False,
    because it makes no citation claim to begin with — it's deterministic id passthrough.

    ADVISORY judge tier: after a REAL model answer (never the extractive fallback), when a judge model
    is configured (llm.has_judge()) the same candidate context is re-sent to the judge, which returns a
    one-line SUPPORTED/PARTIAL/UNSUPPORTED verdict. That verdict is recorded as `judge_verdict` and, only
    when UNSUPPORTED, adds one more prefix line. It is annotation, never a gate: it is never passed to
    lint.gate_banner and never changes `used`/`grounding_fail`/the H-arm banner.

    GROUNDING FAILURE WITHHOLDS THE PROSE (2026-07 audit): a model that cites none of the retrieved
    sources has demonstrated it isn't grounded in them — its prose (fabricated commands, wrong version
    claims) is no more trustworthy than a hallucination and must never reach the reader, banner or not.
    On `grounding_fail`, the model's text is discarded entirely and replaced with an explicit
    withheld-answer line naming the top candidate ids, exactly like the extractive fallback shape."""
    cands = state.get("candidates", [])
    cand_ids = [cid for cid, _ in cands]
    top_ids = ", ".join(cand_ids[:5]) or "(no candidates)"
    ctx = _assemble_context(cands)
    messages = [
        {"role": "system", "content": (
            "Answer the question using ONLY the provided context. After every claim, add an inline "
            "citation in the exact form [cite: <note-id>], using ONLY the note ids shown in brackets "
            "before each context chunk below — never invent or guess an id.")},
        {"role": "user", "content": "Question: %s\n\nContext:\n%s" % (state["query"], ctx)},
    ]
    if llm.available():                              # config-only check (no socket) — so a blocking
        print("· querying local model (WIKI_LLM=%s); a reasoning model can take 30-200s…"
              % llm.mode(), file=sys.stderr, flush=True)   # the run doesn't look frozen
    resp = llm.complete_routed(messages, tier="hard")   # quality leaf -> large model (routes only if 2 configured)
    answer = llm.text_of(resp) if resp is not None else None

    grounding_fail = False
    judge_verdict = None
    if answer:                                        # a real model answer — parse what it ACTUALLY cited
        cand_set = set(cand_ids)
        parsed = list(dict.fromkeys(_CITE_RE.findall(answer)))   # order-preserving de-dup
        used = [c for c in parsed if c in cand_set]
        if not used:
            grounding_fail = True
        if llm.has_judge():                            # advisory only — never touches the gate/used
            judge_verdict = _judge_verdict(state["query"], answer, ctx)
    else:                                             # None (gateway off) OR empty (e.g. a reasoning
        reason = ""                                    # model cut off mid-think)
        if llm.mode() != "off":                        # WIKI_LLM was meant to be active — never fail silently
            cfg = llm.load_config()
            endpoint = cfg.get("api_base") or cfg.get("model") or "no endpoint configured"
            reason = " (gateway returned no answer: %s)" % endpoint
        answer = "[extractive fallback — no model answer%s] top sources: %s" % (reason, top_ids)
        used = cand_ids                                # deterministic passthrough, not a citation claim

    prefix = ""
    if grounding_fail:
        prefix += "⚠️ %s\n\n" % _GROUNDING_FAIL_BANNER
    banner = state.get("banner") or []
    if banner:
        prefix += "⚠️ " + " | ".join(banner) + "\n\n"
    if judge_verdict and judge_verdict.get("verdict") == "UNSUPPORTED":
        prefix += "⚠️ %s\n\n" % _JUDGE_ADVISORY_BANNER
    if grounding_fail:
        # Never serve fabricated prose: a model that cited none of its sources gets no benefit of the
        # doubt — withhold the text entirely rather than gate-banner-and-serve-anyway.
        answer = ("[ungrounded synthesis withheld — model cited none of the retrieved sources] "
                  "top sources: %s" % top_ids)
    if prefix:
        answer = prefix + answer
    out = {"answer": answer, "used": used, "grounding_fail": grounding_fail}
    if judge_verdict is not None:
        out["judge_verdict"] = judge_verdict
    return out
