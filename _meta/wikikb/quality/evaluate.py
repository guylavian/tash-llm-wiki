#!/usr/bin/env python3
"""eval.py — recall + context-cost scoreboard for the wiki retriever. stdlib only, no network.

WHY: every retrieval change (router-skip, graph-expand, hybrid-dense) must be *measured*,
not asserted. This is the scoreboard. Cases live in `_meta/eval/cases.jsonl` (FROZEN);
post-hoc cases go in `cases.heldout.jsonl` and are run separately.

FAITHFULNESS: it does NOT re-implement scoring. It imports kb.py and replays
kb.load() + kb.score() + kb's exact sort, so the reference-note ranking is identical to
`python3 kb.py --domain <d> search "<q>"` with default flags (gated notes excluded).

METRICS
  recall@k (lexical)      — expected note in the top-k reference-note ranking?
  recall@k (lexical+graph)— OR reachable 1-hop from a top-k *synthesized page* via its
                            `## Sources` block / `[[links]]` (the Phase-2 ceiling, measured
                            read-only over edges crosslink.py already wrote). The gap
                            between the two isolates entry-point misses (a graph solves)
                            from true retrieval misses (need dense / Phase 3).
  context-token proxy     — tokens that ACTUALLY enter the answer context, NOT the sum of
                            every full body touched:
                              index read  (global index.md + index.<domain>.md; --route
                                           skips the global one — Phase-1 accounting)
                            + snippets    (~SNIPPET_CHARS each) for the candidates skimmed
                            + full bodies of ONLY the notes actually opened
                                (1 on a hit; --miss-opens, default 2, on a miss).

GRACEFUL: lexical is the default and the fallback. --hybrid is reserved for Phase 3
(hooks in once an embedding index exists); absent it, the baseline is pure lexical.

Usage:
    python3 -m wikikb evaluate
    python3 -m wikikb evaluate --verbose
    python3 -m wikikb evaluate --route                 # Phase-1 accounting (skip index.md)
    python3 -m wikikb evaluate --cases _meta/eval/cases.heldout.jsonl
"""
import argparse
import json
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
sys.dont_write_bytecode = True          # keep _meta/wikikb/ free of __pycache__
from wikikb.retrieval import kb                               # faithful: reuse the real loader + ranker
from wikikb.retrieval import route                            # Phase-1 router (cheap domain pick)
from wikikb.retrieval import expand                           # Phase-2 graph expansion (the real tool, imported)
from wikikb.retrieval import embed                            # Phase-3 dense layer (lazy heavy imports inside)
from wikikb.online import cost                             # token/$/latency seam (proxy_tokens = float; BF-1)

CHARS_PER_TOKEN = cost.CHARS_PER_TOKEN  # single home in cost.py; value 4 (air-gap heuristic, no tiktoken)
SNIPPET_CHARS = 260                     # matches kb.snippet() width — a skimmed candidate line

_recs_cache = {}


# ---------- reference tier (the retrieval target) -------------------------------------

def records(domain):
    if domain not in _recs_cache:
        _recs_cache[domain] = kb.load(domain) or []
    return _recs_cache[domain]


def note_ids(domain):
    return {r.get("id") for r in records(domain)}


def rank(domain, query):
    """Replay kb.py's default `search` ranking via kb.lexical_rank — the single ranking home
    (WI-5); this replay can no longer drift from the CLI. Default search excludes gated.
    Return [(note_id, body_len), ...] best-first."""
    _terms, _pool, scored = kb.lexical_rank(domain, query, records(domain))
    return [(r.get("id"), len(bt)) for _, r, bt in scored]


# Phase-2 graph expansion lives in expand.py (imported above); the eval measures the
# real tool, exactly as it imports kb.py for the lexical ranking.

# ---------- cost + recall -------------------------------------------------------------

def index_bytes(domain, route):
    total = 0
    if not route:
        g = os.path.join(WIKI, "index.md")
        if os.path.isfile(g):
            total += os.path.getsize(g)
    d = os.path.join(WIKI, "index.%s.md" % domain)
    if os.path.isfile(d):
        total += os.path.getsize(d)
    return total


def first_hit(ranked_ids, expected):
    for i, rid in enumerate(ranked_ids, 1):
        if rid in expected:
            return i
    return None


def note_len(domain, nid):
    for r in records(domain):
        if r.get("id") == nid:
            return len(kb.body_text(r))
    return 0


def body_of(domain, nid):
    """The reference-note body text for a slug (Phase-3 --measure-llm context assembly)."""
    for r in records(domain):
        if r.get("id") == nid:
            return kb.body_text(r)
    return ""


def hybrid_rank(domain, query):
    """Phase-3: fuse lexical with dense (RRF). Returns ([(id, body_len), ...], active).
    `active` is False — and the result is plain lexical — when the dense library / vendored
    model / index is absent (graceful degradation, the air-gap invariant)."""
    lex = rank(domain, query)
    try:
        dense = embed.dense_rank(domain, query)
    except Exception:
        dense = None
    if not dense:
        return lex, False
    lenmap = {i: ln for i, ln in lex}
    fused = [(sid, lenmap.get(sid) if sid in lenmap else note_len(domain, sid))
             for sid in embed.rrf_fuse([i for i, _ in lex], dense)]
    return fused, True


def evaluate(cases, kmax, use_route, miss_opens, use_graph, use_hybrid=False):
    rows = []
    for c in cases:
        domain = c.get("domain")
        expected = set(c["expect_any_of"])
        # Phase-1 routing: skip the global index.md ONLY when the router is confident.
        # Search the labeled domain regardless, so recall is unchanged by construction;
        # router precision (confident-never-wrong) is verified separately by route.py --eval.
        if use_route:
            pred, confident = route.route(c["query"])
            skip_global = confident and pred and pred[0] == domain
        else:
            confident, skip_global = False, False
        if use_hybrid:
            ranked, hybrid_active = hybrid_rank(domain, c["query"])
        else:
            ranked, hybrid_active = rank(domain, c["query"]), False
        ids = [rid for rid, _ in ranked]
        lens = [ln for _, ln in ranked]
        hit = first_hit(ids, expected)                       # 1-based lexical rank or None
        found = hit is not None and hit <= kmax              # lexical found within the window?

        # Phase-2 graph expansion: seed-source notes (primary, high-precision) vs 1-hop closure
        gseed = expand.graph_notes(domain, c["query"], kmax, closure=False)
        gclose = expand.graph_notes(domain, c["query"], kmax, closure=True)
        lex_topk = set(ids[:kmax])
        graph_hit = found or bool(expected & (lex_topk | gseed))            # operative (primary)
        graph_hit_closure = found or bool(expected & (lex_topk | gclose))   # ceiling
        rescued = use_graph and (not found) and bool(expected & gseed)

        # context-token proxy: index + snippets skimmed + full bodies actually opened.
        # Graph mode turns a lexical miss that the graph rescues into ONE correct open
        # (the cited note) instead of `miss_opens` wasted opens -> recall up, cost down.
        if found:
            scanned = hit                                    # stop skimming at the hit
            opened_bodies = [lens[hit - 1]]                  # open the one true source
            opened_ids = [ids[hit - 1]]
        elif rescued:
            scanned = min(kmax, len(ids))
            # deterministic tie-break: a set's iteration order varies per process (hash
            # randomization), which made --graph output nondeterministic run-to-run and a
            # byte-for-byte golden impossible. min() picks the lexicographically smallest slug;
            # aggregate recall is unchanged (any expected∩gseed note counts as a rescue).
            rnote = min(expected & gseed)                    # the note the graph handed us
            opened_bodies = [note_len(domain, rnote)]
            opened_ids = [rnote]
        else:
            scanned = min(kmax, len(ids))
            opened_bodies = [lens[i] for i in range(min(miss_opens, len(ids)))]  # open a few, fail
            opened_ids = [ids[i] for i in range(min(miss_opens, len(ids)))]
        idx_t = cost.proxy_tokens(index_bytes(domain, skip_global))       # FLOAT proxy (BF-1)
        snip_t = cost.proxy_tokens(SNIPPET_CHARS) * scanned               # == (260/4)*scanned
        body_t = cost.proxy_tokens(sum(opened_bodies))
        rows.append({
            "query": c["query"], "domain": domain, "kind": c.get("kind", "?"),
            "pair": c.get("pair"), "variant": c.get("variant"),
            "expected": sorted(expected), "hit_rank": hit,
            "found": found, "found_eff": found or rescued,
            "graph_hit": graph_hit, "graph_hit_closure": graph_hit_closure,
            "graph_only": graph_hit and not found, "rescued": rescued,
            "scanned": scanned, "opened": len(opened_bodies), "opened_ids": opened_ids,
            "confident": confident, "skip_global": skip_global, "hybrid_active": hybrid_active,
            "idx_t": idx_t, "snip_t": snip_t, "body_t": body_t,
            "ctx_t": idx_t + snip_t + body_t, "top5": ids[:5],
        })
    return rows


def validate(cases):
    bad = []
    for c in cases:
        ids = note_ids(c.get("domain"))
        for t in c["expect_any_of"]:
            if t not in ids:
                bad.append((c.get("domain"), t, c["query"][:50]))
    return bad


def pct(n, d):
    return (100.0 * n / d) if d else 0.0


def rec(rowset, k, key):
    if key == "lex":
        h = sum(1 for r in rowset if r["hit_rank"] and r["hit_rank"] <= k)
    else:  # boolean recall flag (graph_hit / graph_hit_closure)
        h = sum(1 for r in rowset if r[key])
    return h, len(rowset)


def mrr(rows):
    """Mean reciprocal rank over the (unbounded) lexical hit_rank — 0 for a miss. Same rank
    numbers the PAIRED section prints (e.g. dpop paraphrase @118), just averaged."""
    if not rows:
        return 0.0
    return sum((1.0 / r["hit_rank"]) if r["hit_rank"] else 0.0 for r in rows) / len(rows)


def precision_at5(rows):
    """Mean precision@5 over the lexical top-5: (# of the top-5 ids that are in `expected`) / 5.
    `expected` is already the expect_any_of set (e.g. the same guide chapter across RHBK
    versions), so a case with several acceptable notes earns partial credit for each one surfaced."""
    if not rows:
        return 0.0
    return sum(sum(1 for rid in r["top5"] if rid in r["expected"]) / 5.0 for r in rows) / len(rows)


def report(rows, ks, kmax, verbose):
    n = len(rows)
    print("=" * 84)
    print("RETRIEVER EVAL — %d cases  (recall window kmax=%d)" % (n, kmax))
    print("=" * 84)

    if verbose:
        print("\nPer-case:")
        for r in rows:
            mark = ("@%d" % r["hit_rank"]) if r["hit_rank"] else "MISS"
            g = "G" if r["graph_only"] else (" " if r["found"] else "x")
            print("  [%-12s %-15s] lex=%-5s graph=%s ctx≈%5dtok  %s"
                  % (r["kind"], r["domain"], mark, g, r["ctx_t"], r["query"][:54]))
            if not r["found"]:
                print("        expected: %s" % ", ".join(r["expected"]))
                print("        top5 lex: %s" % (", ".join(r["top5"]) or "(none)"))

    print("\nRECALL  (lexical -> +graph seed-sources -> +graph 1-hop closure)")
    for k in ks:
        hl, d = rec(rows, k, "lex")
        if k == kmax:
            hg, _ = rec(rows, k, "graph_hit")
            hc, _ = rec(rows, k, "graph_hit_closure")
            print("  @%-2d  lexical %2d/%-2d (%3.0f%%)  ->  +graph %2d/%-2d (%3.0f%%)  ->  +closure %2d/%-2d (%3.0f%%)"
                  % (k, hl, d, pct(hl, d), hg, d, pct(hg, d), hc, d, pct(hc, d)))
            print("       graph-rescued (primary): %d   |   closure adds: %d" % (hg - hl, hc - hg))
        else:
            print("  @%-2d  lexical %2d/%-2d (%3.0f%%)" % (k, hl, d, pct(hl, d)))

    print("\n  MRR (lexical, unbounded rank) : %.3f" % mrr(rows))
    print("  precision@5 (lexical)         : %.3f" % precision_at5(rows))

    print("\n  by domain (lexical r@%d -> +graph):" % kmax)
    for dom in sorted({r["domain"] for r in rows}):
        sub = [r for r in rows if r["domain"] == dom]
        hl, d = rec(sub, kmax, "lex")
        hg, _ = rec(sub, kmax, "graph_hit")
        print("    %-18s  %d/%d  ->  %d/%d" % (dom, hl, d, hg, d))

    print("\n  by kind (lexical r@%d -> +graph):" % kmax)
    for kind in sorted({r["kind"] for r in rows}):
        sub = [r for r in rows if r["kind"] == kind]
        hl, d = rec(sub, kmax, "lex")
        hg, _ = rec(sub, kmax, "graph_hit")
        print("    %-18s  %d/%d  ->  %d/%d" % (kind, hl, d, hg, d))

    # paired exact->paraphrase deltas (the lexical-gap proof)
    pairs = {}
    for r in rows:
        if r["pair"]:
            pairs.setdefault(r["pair"], {})[r["variant"]] = r
    if pairs:
        print("\nPAIRED exact -> paraphrase (same target; the lexical-recall gap):")
        for name, var in sorted(pairs.items()):
            e, p = var.get("exact"), var.get("paraphrase")
            er = ("@%d" % e["hit_rank"]) if e and e["hit_rank"] else "MISS"
            pr = ("@%d" % p["hit_rank"]) if p and p["hit_rank"] else "MISS"
            print("  %-18s exact %-5s ->  paraphrase %-5s" % (name, er, pr))

    print("\nCONTEXT-TOKEN PROXY  (index + snippets skimmed + bodies actually opened; chars/%d)"
          % CHARS_PER_TOKEN)
    mi = sum(r["idx_t"] for r in rows) / n
    ms = sum(r["snip_t"] for r in rows) / n
    mb = sum(r["body_t"] for r in rows) / n
    mo = sum(r["opened"] for r in rows) / n
    print("  mean index    tokens : %6d" % mi)
    print("  mean snippet  tokens : %6d  (%.1f candidates skimmed/case)" % (ms, ms / (SNIPPET_CHARS / CHARS_PER_TOKEN)))
    print("  mean opened-body tok : %6d  (%.2f full notes opened/case)" % (mb, mo))
    print("  mean TOTAL ctx tokens: %6d   <-- Phase 1 cuts index; Phase 2/3 cut opened-body" % (mi + ms + mb))

    rescued_rows = [r for r in rows if r["rescued"]]
    if rescued_rows:
        print("\nGRAPH RESCUE (Phase 2: lexical misses the graph turns into 1 correct open)")
        print("  cases rescued in-proxy : %d  (each replaces wasted miss-opens with the cited note)"
              % len(rescued_rows))

    skipped = [r for r in rows if r["skip_global"]]
    if skipped or any(r["confident"] for r in rows):
        print("\nROUTING (Phase 1: skip global index.md on a confident route)")
        print("  confident skips      : %d/%d cases read only index.<domain>.md" % (len(skipped), n))
        print("  index tokens skipped : %6d total over the run (the Phase-1 saving)"
              % sum(int(os.path.getsize(os.path.join(WIKI, "index.md")) / CHARS_PER_TOKEN) for _ in skipped))

    misses = [r for r in rows if not r["found"]]
    still = [r for r in misses if not r["graph_hit"]]
    if misses:
        print("\nMISS BREAKDOWN @%d : %d miss  =  %d graph-rescued (Phase 2)  +  %d still-missing (Phase 3)"
              % (kmax, len(misses), len(misses) - len(still), len(still)))
        for r in misses:
            tag = "graph-rescued" if r["graph_hit"] else "STILL-MISSING"
            print("  - [%-13s] %s" % (tag, r["query"][:64]))


def run_measure(rows, recorder):
    """Phase-3: for each case, assemble the prompt the QUERY op WOULD send (query + the opened
    context) and call the OPTIONAL local LLM gateway via cost.measure(). Populates row['gen'] and
    returns True iff any real call ran. This is POST-HOC — recall is already finalized and is never
    touched here; cost.measure degrades to 'n/a (offline)' when the gateway is off/absent, so recall
    is unaffected and offline runs add no real cost. The gateway only ever talks to a local loopback
    model (llm.py enforces it)."""
    any_active = False
    for r in rows:
        ctx = "\n\n".join(body_of(r["domain"], nid) for nid in r.get("opened_ids", []))
        system = "Answer the question using only the provided context."
        user = "Question: %s\n\nContext:\n%s" % (r["query"], ctx)
        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        # chars/4 proxy of the SAME prompt text — the apples-to-apples divisor for the calibration
        # ratio. NOT ctx_t: that carries ~13k/case index+snippet tokens never sent to the model, which
        # would inflate the divisor ~15% and deflate (lie about) the ratio (Phase-3 review #1).
        r["gen_prompt_proxy"] = cost.proxy_tokens(len(system) + len(user))
        r["gen"] = cost.measure(messages, domain=r["domain"], recorder=recorder)
        any_active = any_active or r["gen"].get("active", False)
    return any_active


def report_measure(rows, recorder, active):
    """The GENERATION-cost block — orthogonal to the retrieval CONTEXT-TOKEN PROXY above. Prints
    'n/a (offline)' when the gateway is inactive (recall is unaffected — recall never calls a model)."""
    from wikikb.online import llm
    print("\nLLM-CALL COST (measured via LiteLLM; n/a offline)")
    print("  gateway: %s" % llm.status_str())
    if not active:
        print("  n/a (offline) — gateway inactive; recall above is unaffected (recall never calls the model)")
        return
    s = recorder.summary()
    n = max(1, s["calls"])
    print("  active calls          : %d/%d" % (s["calls"], len(rows)))
    print("  mean gen prompt tokens: %d" % (s["prompt_tokens"] / n))
    print("  mean gen completion   : %d" % (s["completion_tokens"] / n))
    if s["usd"] is not None and s["priced_calls"]:
        print("  mean gen $            : %.6f  (%d/%d calls priced)" % (s["usd"] / s["priced_calls"], s["priced_calls"], s["calls"]))
    else:
        print("  mean gen $            : unpriced/local (no $ for local models — lead with tokens + latency)")
    if s["latency_ms_p50"] is not None:
        print("  latency p50 / p95 ms  : %.0f / %.0f" % (s["latency_ms_p50"], s["latency_ms_p95"]))
    print("  cache hits            : %d" % s["cache_hits"])
    meas = [r["gen"]["gen_prompt_tok"] for r in rows if r.get("gen", {}).get("gen_prompt_tok")]
    prox = [r.get("gen_prompt_proxy", 0) for r in rows if r.get("gen", {}).get("gen_prompt_tok")]
    if meas and sum(prox):
        print("  calibration gen/proxy : %.3f  (measured prompt tokens / chars-4 proxy of the SAME prompt "
              "— recalibrates chars/4 for the model's tokenizer)" % (sum(meas) / sum(prox)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "cases.jsonl"))
    ap.add_argument("--k", default="5,10", help="comma-separated recall cutoffs (default 5,10)")
    ap.add_argument("--kmax", type=int, default=10, help="recall window + max notes skimmed (default 10)")
    ap.add_argument("--miss-opens", type=int, default=2, help="full notes opened on a miss (default 2)")
    ap.add_argument("--route", action="store_true", help="Phase-1: skip global index.md on a confident route")
    ap.add_argument("--graph", action="store_true", help="Phase-2: graph-expand to rescue lexical misses")
    ap.add_argument("--hybrid", action="store_true", help="Phase-3: fuse dense embeddings (RRF); lexical fallback if absent")
    ap.add_argument("--measure-llm", action="store_true",
                    help="Phase-3: call the local LLM gateway per case and report measured gen tokens/$/latency (n/a offline)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--budget-tokens", type=float, default=None,
                    help="fail (exit 3) if the mean context-token proxy exceeds this budget")
    ap.add_argument("--budget-usd", type=float, default=None,
                    help="fail (exit 3) if mean measured generation $ exceeds this (needs --measure-llm; n/a offline)")
    ap.add_argument("--min-recall", type=float, default=None,
                    help="fail (exit 3) if the FINAL +closure r@kmax percentage is below this (0-100)")
    args = ap.parse_args()

    path = args.cases if os.path.isabs(args.cases) else os.path.join(WIKI, args.cases)
    if not os.path.isfile(path):
        print("cases file not found: %s" % path)
        sys.exit(2)
    cases = []
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as e:
                print("bad JSON at %s:%d — %s" % (os.path.relpath(path, WIKI), ln, e))
                sys.exit(2)
    if not cases:
        print("no cases in %s (empty held-out set?)" % os.path.relpath(path, WIKI))
        sys.exit(0)

    bad = validate(cases)
    if bad:
        print("INVALID TARGETS (expected note id not in its domain reference tier):")
        for dom, t, q in bad:
            print("  - [%s] %s   (case: %s…)" % (dom, t, q))
        print("Fix the cases before trusting recall.\n")

    ks = [int(x) for x in args.k.split(",")]
    if args.kmax not in ks:
        ks.append(args.kmax)
    ks = sorted(set(ks))
    if args.hybrid:
        active = any(r["hybrid_active"] for r in evaluate(cases[:1], args.kmax, False, args.miss_opens, False, True))
        print("Phase-3 dense: %s  -> hybrid %s\n"
              % (embed.status_str(), "ACTIVE" if active else "INACTIVE (lexical fallback)"))
    rows = evaluate(cases, args.kmax, args.route, args.miss_opens, args.graph, args.hybrid)
    report(rows, ks, args.kmax, args.verbose)

    # Phase-3 measured GENERATION cost — flag-gated, post-hoc (recall already finalized above and
    # never routed through this). Default run (no --measure-llm) prints nothing here -> byte-identical.
    recorder, measured_active = None, False
    if args.measure_llm:
        recorder = cost.UsageRecorder()
        measured_active = run_measure(rows, recorder)
        report_measure(rows, recorder, measured_active)
        recorder.write_report()

    # budget gate (BF-9): --budget-tokens vs the untruncated float proxy mean (report() displays it
    # floored via %6d); --budget-usd vs measured generation $ (only when --measure-llm produced priced
    # calls). Exit 3 on breach. Default run (no budget flags) prints nothing here — byte-identical.
    if args.budget_tokens is not None or args.budget_usd is not None:
        mean_ctx = (sum(r["ctx_t"] for r in rows) / len(rows)) if rows else 0.0
        try:
            cost.check_budget(mean_ctx, args.budget_tokens, "ctx-token")
        except cost.BudgetExceeded as e:
            print("\nBUDGET: %s" % e)
            sys.exit(3)
        if args.budget_usd is not None:
            if measured_active and recorder and recorder.priced_calls:
                try:
                    cost.check_budget(recorder.usd / max(1, recorder.calls), args.budget_usd, "gen-$")
                except cost.BudgetExceeded as e:
                    print("\nBUDGET: %s" % e)
                    sys.exit(3)
            else:
                print("\nBUDGET: --budget-usd is n/a (no measured generation $ — needs --measure-llm + a "
                      "priced model) — not enforced")

    # min-recall gate: FINAL +closure r@kmax vs --min-recall (mirrors the --budget-tokens exit-3
    # pattern). Default run (no --min-recall) prints nothing here — byte-identical.
    if args.min_recall is not None:
        hc, d = rec(rows, args.kmax, "graph_hit_closure")
        closure_pct = pct(hc, d)
        if closure_pct < args.min_recall:
            print("\nMIN-RECALL: +closure r@%d = %.1f%% < required %.1f%%" % (args.kmax, closure_pct, args.min_recall))
            sys.exit(3)
    sys.exit(0)


if __name__ == "__main__":
    main()
