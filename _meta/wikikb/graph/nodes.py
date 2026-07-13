"""graph/nodes.py — the QUERY/INGEST graph nodes. stdlib-safe (no langgraph/litellm at module scope).

Each node is a plain function(state: dict) -> dict-update — so it is unit-testable WITHOUT langgraph
(the package degrades gracefully and the faithfulness probes can exercise nodes directly). Every node
calls the EXISTING deterministic tools (kb/route/expand) or the real gate (lint.gate_banner) or the
optional local gateway (llm.complete) — none of that logic is re-implemented here (the faithfulness
invariant, BF-4). Recall-shaped ranking reuses kb.score, exactly as eval.py does.
"""
import os
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
_GENERIC_TRUNC_MARK = "[…context truncated — open %s for the full note]"


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
    """Fit one candidate into its share, returning ``(piece, chars_used, truncated)``.

    Every body cut gets a marker: the existing table-specific marker when the first dropped line is
    tabular, otherwise the generic full-note marker. If the share cannot hold header+marker, emit a
    marker-only piece when possible so a wholly skipped candidate is not silently invisible."""
    header = "[%s]\n" % cid
    sep = 2 if not first else 0                     # the "\n\n" join separator
    if sep + len(header) + len(body) <= budget:     # true all-fit: preserve historical bytes exactly
        piece = header + body
        return piece, sep + len(piece), False
    avail = budget - sep - len(header) - len(_TRUNC_MARK % cid) - 1
    if avail <= 0:
        marker = _GENERIC_TRUNC_MARK % cid
        if sep + len(marker) <= budget:
            return marker, sep + len(marker), True
        return None, 0, True
    fitted, cut_tabular = _fit_lines(body, avail)
    piece = header + fitted
    marker = (_TRUNC_MARK if cut_tabular else _GENERIC_TRUNC_MARK) % cid
    piece += "\n" + marker
    return piece, sep + len(piece), True


def _assemble_context(cands, limit=CTX_CHARS, return_truncated=False):
    """Join candidate (id, body) pairs into one `[id]\\n<body>` context string capped at `limit`
    chars. Fair-share budgeting (fixes the 2026-07 context-starvation bug: one huge rank-1 note
    was evicting every other candidate): each candidate's share is `remaining // remaining_count`,
    recomputed as we go, so a candidate that needs less than its share leaves the leftover for the
    ones after it — every candidate gets SOME context before any one of them gets all of it. The
    cut is still whole-line only (see _fit_lines). Every drop is explicit: table/list cuts retain
    the distinct _TRUNC_MARK; prose cuts and wholly skipped candidates get _GENERIC_TRUNC_MARK.
    With ``return_truncated=True``, also return the ordered ids whose bodies were incomplete."""
    cands = [(cid, body) for cid, body in cands if body]
    out, truncated_ids, remaining = [], [], limit
    for i, (cid, body) in enumerate(cands):
        share = remaining // (len(cands) - i)
        piece, used, truncated = _fit_candidate(cid, body, share, first=not out)
        if truncated:
            truncated_ids.append(cid)
        if piece is None:
            continue                                # too little room even for marker-only; id remains recorded
        out.append(piece)
        remaining -= used
    context = "\n\n".join(out)
    return (context, truncated_ids) if return_truncated else context


# ---------- QUERY nodes -----------------------------------------------------------------------

def route_node(state):
    """route.route() -> the domain to search + the router's confidence (Phase-1)."""
    doms, confident = route.route(state["query"])
    domain = state.get("domain") or (doms[0] if doms else None)
    return {"domain": domain, "confident": confident}


def retrieve_node(state):
    """Candidate retrieval — consumes kb.lexical_rank, the single ranking home (WI-5), so this path
    is identical-by-construction to the CLI/eval/serve ordering instead of replaying it. When the
    dense embedding model+index are present, fuses the lexical and dense rankings via RRF — identical
    to kb.py --hybrid — so the answer path gets the paraphrase lift Phase 1 built. Fusion consumes the
    primitive's POSITIVE-score ordering (this path previously fed zero-score records into RRF, a
    divergence from cmd_search's hybrid that WI-5 removes); dense-only notes still enter via the
    filtered-pool lookup. Lazy+guarded: with the model/index absent it DEGRADES to the exact lexical
    baseline (evaluate.rank()'s faithful ordering). `thin` drives the graph-expansion edge."""
    domain, query, k = state["domain"], state["query"], state.get("k", 5)
    _terms, pool, scored = kb.lexical_rank(domain, query)
    dense = None
    try:                                          # lazy + guarded (air-gap): None when model/index absent
        from wikikb.retrieval import embed
        dense = embed.dense_rank(domain, query)
    except Exception:
        dense = None
    if dense:                                     # hybrid: RRF-fuse lexical + dense, incl. dense-only notes
        rec_by_id = {r.get("id"): r for r in pool}
        fused, seen = [], set()
        for sid in embed.rrf_fuse([r.get("id") for _, r, _ in scored], dense):
            r = rec_by_id.get(sid)
            if r is not None and sid not in seen:
                seen.add(sid)
                fused.append(r)
        cands = [(r.get("id"), kb.body_text(r)) for r in fused[:k]]
    else:                                         # UNCHANGED lexical baseline (faithful to eval.rank())
        cands = [(r.get("id"), bt) for _, r, bt in scored[:k]]
    return {"candidates": cands, "thin": len(cands) < THIN_K}


def _grounded_seeds(seeds):
    """`expand.expand()`'s top-k=10 lexical page seeds routinely include a page that matched on
    vocabulary alone but cites NO reference note (`note_sources` empty — most often a domain's broad
    `<domain>-implementation-review` MOC, whose rule/anti-pattern table lexically overlaps almost any
    in-domain query). Gating the answer on such a page's OWN provenance would flag it for a claim it
    contributes NOTHING to (live-tested: it tripped Confidence-gate Provisional on unrelated queries
    across every domain via livebank). A seed with real note_sources DOES traceably back the served
    context (its notes feed `candidates` below) so it stays in scope, kept or dropped by its own
    provenance like any other candidate page."""
    G = expand.load_pages()
    return [s for s in seeds if G.get(s, {}).get("note_sources")]


def _seed_page_fms(seeds):
    """Frontmatter dicts for the synthesized (topics/entities/questions) SEED pages `expand.expand()`
    matched for this query -- i.e. the actual candidate synthesis page(s) the answer draws on. Reuses
    lint.parse_frontmatter (the SAME parser page_gate_verdict/gate_banner consume; no re-implementation)
    against the real page file, not expand.load_pages()'s trimmed dict, so back-compat nested
    `provenance:` blocks are read exactly like lint/gate_page_probe read them (faithfulness, BF-4/BF-10).
    A seed slug is looked up across expand.PAGE_DIRS; missing files (shouldn't happen -- seeds come
    from the same page-dir scan) are skipped rather than raising."""
    fms = []
    for slug in seeds:
        for d in expand.PAGE_DIRS:
            path = os.path.join(expand.WIKI, d, slug + ".md")
            if os.path.isfile(path):
                with open(path, encoding="utf-8") as fh:
                    fm = lint.parse_frontmatter(fh.read())
                if fm:
                    fms.append(fm)
                break
    return fms


def expand_node(state):
    """expand.expand() -> the 1-hop neighborhood of the query-matched synthesized SEED pages: their
    reference notes (the multi-hop entry-point rescue, added to `candidates` if not already retrieved)
    AND their own frontmatter, threaded into `page_fm` so gate_node's H2/H3/H4/Provisional arms see the
    REAL candidate page(s) the answer is drawing on instead of the placeholder {} (was: only H1 fired
    on the live path -- root cause per PLAN-graphify-pdf-upload.md Phase 3 item 1). page_fm is scoped to
    _grounded_seeds -- seeds that actually cite a reference note -- so a page's presence in `page_fm`
    always means it concretely stands behind the served context, never a bare lexical coincidence."""
    if state.get("no_expand") or os.environ.get("WIKIKB_NO_EXPAND") == "1":
        return {"graph_notes": [], "graph_pages": [],
                "candidates": list(state.get("candidates", [])), "page_fm": []}
    domain, query = state["domain"], state["query"]
    e = expand.expand(domain, query) or {}
    notes = e.get("notes_seed") or set()
    have = {cid for cid, _ in state.get("candidates", [])}
    new = sorted(n for n in notes if n not in have)
    bodies = {}
    if new:
        for r in (kb.load(domain) or []):
            if r.get("id") in new:
                bodies[r.get("id")] = kb.body_text(r)
    extra = [(nid, bodies.get(nid, "")) for nid in new]
    return {"graph_notes": sorted(notes), "graph_pages": sorted(e.get("seeds") or []),
            "candidates": state.get("candidates", []) + extra,
            "page_fm": _seed_page_fms(_grounded_seeds(e.get("seeds") or []))}


def gate_node(state):
    """Apply the FULL Confidence gate via lint.gate_banner — the SAME rule lint enforces and the CI
    probes assert (faithfulness, BF-4). H1 uses the routed domain's tiers-covered. H2/H3/H4/L apply to
    the candidate synthesis PAGE(S)' frontmatter, threaded by expand_node into state['page_fm'] as a
    LIST of fm dicts — one per query-matched seed page — so H2/H3/H4/Provisional actually fire on the
    live ask/serve/mcp path (previously only H1 did; PLAN-graphify-pdf-upload.md Phase 3 item 1). A
    single fm dict is still accepted for back-compat (direct node callers / older tests).

    Multiple pages -> evaluate gate_banner PER page and take the UNION of reasons (order-preserving
    de-dup): a single clean page must never mask a tripping one (approved decision, not a merge of the
    fm dicts themselves, which would blur which page actually tripped which arm)."""
    domain = state.get("domain")
    try:
        covered = coverage.load_tiers_covered().get(domain)
    except Exception:
        covered = None
    page_fms = state.get("page_fm") or []
    if isinstance(page_fms, dict):                      # back-compat: a lone fm dict, not a list
        page_fms = [page_fms] if page_fms else []
    banner = []
    for fm in (page_fms or [{}]):                       # no candidate page -> still evaluate H1 alone
        for reason in lint.gate_banner(fm, question_tier=state.get("question_tier"), covered=covered):
            if reason not in banner:
                banner.append(reason)
    # Honesty note (validator defect D8): with no question_tier the H1 arm silently skips, so an
    # untiered break-fix ask against a partially-covered domain returns banner=[] — a false all-clear.
    # Say the gate wasn't evaluated instead of staying silent. Deterministic, never suppresses H arms.
    ALL_TIERS = {"conceptual", "support-kb", "scenarios"}
    if state.get("question_tier") is None and covered and set(covered) < ALL_TIERS:
        banner = banner + ["coverage gate not evaluated — no question tier supplied and domain %r "
                           "covers only %s; pass --tier conceptual|support-kb|scenarios (H1-unknown)"
                           % (domain, list(covered))]
    return {"banner": banner, "covered": covered}


_GROUNDING_FAIL_BANNER = ("Ungrounded synthesis — the model cited none of the retrieved sources; "
                          "treat as inference, verify the References.")
_VERDICT_RE = re.compile(r"\b(SUPPORTED|PARTIAL|UNSUPPORTED)\b", re.IGNORECASE)
_JUDGE_ADVISORY_BANNER = "judge (advisory): answer not supported by cited sources"
_FABRICATION_BANNER = ("Ungrounded identifier(s) in this answer — not found in the retrieved "
                       "context or the question, verify before relying on them: %s")
_PREMISE_BANNER = ("Premise check incomplete — the question's assertions were not all verified "
                   "against the corpus (%s); treat the user's premises as unconfirmed.")


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
    withheld-answer line naming the top candidate ids, exactly like the extractive fallback shape.

    FABRICATED-CITATION CLASS (PLAN-graphify-pdf-upload.md Phase 3 item 2 — closes the still-open
    PRODUCTION_READINESS sign-off blocker): grounding_fail only catches zero-citation answers. A model
    that cites a REAL retrieved note but still invents a distinctive identifier that note never
    mentions (an ENV/CONST like `SSO_HTTPS_CIPHER_SUITES`, a GUID, a nonexistent flag) slips past it.
    `lint.validate_answer_grounding` is the single citation-aware validator: it parses legal cited ids
    and checks identifiers against the union of those cited notes' FULL bodies plus the query. Full
    bodies prevent false positives when a legitimate identifier lies beyond the served context cut;
    uncited candidates do not contribute grounding. Approved granularity: FLAG loudly, never silently
    rewrite the answer text — any leftover
    identifiers get a deterministic warning line (style-matched to the other gate banners) AND are
    returned as `ungrounded_identifiers` so serve/mcp/livebank callers can withhold on their own
    policy without this node making that call for them."""
    cands = state.get("candidates", [])
    cand_ids = [cid for cid, _ in cands]
    top_ids = ", ".join(cand_ids[:5]) or "(no candidates)"
    ctx, truncated_ids = _assemble_context(cands, return_truncated=True)
    # Premise-correction dropout fix (manual session #4, RID Block Size): deterministic extraction
    # (lint.extract_premises) + a MANDATORY pre-built table the model FILLS — structure, not
    # judgment; small local models complete tables far more reliably than they follow "be sure to
    # address the user's assumptions". The premises are injected as ready rows; the model never
    # has to discover them, only fill two cells per row.
    premises = lint.extract_premises(state["query"])
    sys_prompt = ("Answer the question using ONLY the provided context. After every claim, add an inline "
                  "citation in the exact form [cite: <note-id>], using ONLY the note ids shown in brackets "
                  "before each context chunk below — never invent or guess an id.")
    premise_block = ""
    if premises:
        rows = "\n".join("| %d | %s |  |  |" % (i, p["premise_text"].replace("|", "/"))
                         for i, p in enumerate(premises, 1))
        premise_block = ("\n\n## Premise check\n"
                         "| # | User's claim | Corpus says | Verdict |\n|---|---|---|---|\n"
                         + rows + "\n")
        sys_prompt += (
            "\n\nThe question contains factual assertions. Your answer MUST start with the exact "
            "'## Premise check' table given below the question: keep every row, fill ONLY the two "
            "empty cells per row. 'Corpus says' = what the provided context actually states. "
            "'Verdict' must be exactly one of: CONFIRMED, CORRECTED, NOT-IN-CORPUS. "
            "Example row (from a different question) — claim: 'global RID space is capped at 2^31'; "
            "context said: 'the global RID space was limited to 2^30 ... the 2^31 bit can be "
            "unlocked ... cannot be reverted'; correct fill -> Corpus says: 'default cap is 2^30; "
            "2^31 only via an irreversible unlock' | Verdict: CORRECTED. "
            "After the table, write the normal answer.")
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": "Question: %s%s\n\nContext:\n%s"
                                    % (state["query"], premise_block, ctx)},
    ]
    if llm.available():                              # config-only check (no socket) — so a blocking
        print("· querying local model (WIKI_LLM=%s); a reasoning model can take 30-200s…"
              % llm.mode(), file=sys.stderr, flush=True)   # the run doesn't look frozen
    resp = llm.complete_routed(messages, tier="hard")   # quality leaf -> large model (routes only if 2 configured)
    answer = llm.text_of(resp) if resp is not None else None

    grounding_fail = False
    judge_verdict = None
    ungrounded_identifiers = []
    premise_flags = []
    grounding_basis = {"cited_ids": [], "basis": "not-checked-extractive-fallback"}
    if answer:                                        # a real model answer — parse what it ACTUALLY cited
        # the dropout catcher: the model can still reason correctly and drop the correction — but
        # then the injected table row is missing/empty and this fires. Deterministic, post-hoc,
        # never runs on the extractive fallback (which makes no premise claims).
        premise_flags = lint.premise_gate(answer, premises, cands, state["query"])
        validation = lint.validate_answer_grounding(answer, cands, state["query"])
        used = validation["cited_ids"]
        grounding_basis = {"cited_ids": used, "basis": validation["basis"]}
        if not used:
            grounding_fail = True
        else:
            # fabricated-citation check: only meaningful once the answer cites something real —
            # a zero-citation answer is already withheld below by the existing grounding-fail path.
            ungrounded_identifiers = validation["ungrounded_identifiers"]
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
    if ungrounded_identifiers:
        prefix += "⚠️ %s\n\n" % (_FABRICATION_BANNER % ", ".join(ungrounded_identifiers))
    if premise_flags:
        prefix += "⚠️ %s\n\n" % (_PREMISE_BANNER % "; ".join(
            "%s: %s" % (f["flag"], f["premise"][:60]) for f in premise_flags))
    if judge_verdict and judge_verdict.get("verdict") == "UNSUPPORTED":
        prefix += "⚠️ %s\n\n" % _JUDGE_ADVISORY_BANNER
    if grounding_fail:
        # Never serve fabricated prose: a model that cited none of its sources gets no benefit of the
        # doubt — withhold the text entirely rather than gate-banner-and-serve-anyway.
        answer = ("[ungrounded synthesis withheld — model cited none of the retrieved sources] "
                  "top sources: %s" % top_ids)
    if prefix:
        answer = prefix + answer
    out = {"answer": answer, "used": used, "grounding_fail": grounding_fail,
           "ungrounded_identifiers": ungrounded_identifiers, "grounding_basis": grounding_basis,
           "truncated_ids": truncated_ids, "premise_flags": premise_flags,
           "premises": premises}
    if judge_verdict is not None:
        out["judge_verdict"] = judge_verdict
    return out
