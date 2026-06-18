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
    python3 wiki/_meta/bin/eval.py
    python3 wiki/_meta/bin/eval.py --verbose
    python3 wiki/_meta/bin/eval.py --route                 # Phase-1 accounting (skip index.md)
    python3 wiki/_meta/bin/eval.py --cases _meta/eval/cases.heldout.jsonl
"""
import argparse
import json
import os
import re
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))
sys.dont_write_bytecode = True          # keep _meta/bin/ free of __pycache__
sys.path.insert(0, BIN)
import kb                               # faithful: reuse the real loader + ranker
import route                            # Phase-1 router (cheap domain pick)
import expand                           # Phase-2 graph expansion (the real tool, imported)

CHARS_PER_TOKEN = 4                     # air-gap-safe heuristic (matches lint.py); no tiktoken
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
    """Replay kb.py's default `search` ranking. Return [(note_id, body_len), ...] best-first."""
    terms = kb.toks(query)
    scored = []
    for r in records(domain):
        if r.get("body_status") != "fetched":      # default search excludes gated pointers
            continue
        bt = kb.body_text(r)
        sc = kb.score(r, terms, bt)
        if sc > 0:
            scored.append((sc, r, bt))
    scored.sort(key=lambda x: (-x[0], -kb.vkey(x[1].get("version"))[0] if x[1].get("version") else 0))
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


def evaluate(cases, kmax, use_route, miss_opens, use_graph):
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
        ranked = rank(domain, c["query"])
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
        elif rescued:
            scanned = min(kmax, len(ids))
            rnote = next(iter(expected & gseed))             # the note the graph handed us
            opened_bodies = [note_len(domain, rnote)]
        else:
            scanned = min(kmax, len(ids))
            opened_bodies = [lens[i] for i in range(min(miss_opens, len(ids)))]  # open a few, fail
        idx_t = index_bytes(domain, skip_global) / CHARS_PER_TOKEN
        snip_t = (SNIPPET_CHARS / CHARS_PER_TOKEN) * scanned
        body_t = sum(opened_bodies) / CHARS_PER_TOKEN
        rows.append({
            "query": c["query"], "domain": domain, "kind": c.get("kind", "?"),
            "pair": c.get("pair"), "variant": c.get("variant"),
            "expected": sorted(expected), "hit_rank": hit,
            "found": found, "found_eff": found or rescued,
            "graph_hit": graph_hit, "graph_hit_closure": graph_hit_closure,
            "graph_only": graph_hit and not found, "rescued": rescued,
            "scanned": scanned, "opened": len(opened_bodies),
            "confident": confident, "skip_global": skip_global,
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

    def rec(rowset, k, key):
        if key == "lex":
            h = sum(1 for r in rowset if r["hit_rank"] and r["hit_rank"] <= k)
        else:  # boolean recall flag (graph_hit / graph_hit_closure)
            h = sum(1 for r in rowset if r[key])
        return h, len(rowset)

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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "cases.jsonl"))
    ap.add_argument("--k", default="5,10", help="comma-separated recall cutoffs (default 5,10)")
    ap.add_argument("--kmax", type=int, default=10, help="recall window + max notes skimmed (default 10)")
    ap.add_argument("--miss-opens", type=int, default=2, help="full notes opened on a miss (default 2)")
    ap.add_argument("--route", action="store_true", help="Phase-1: skip global index.md on a confident route")
    ap.add_argument("--graph", action="store_true", help="Phase-2: graph-expand to rescue lexical misses")
    ap.add_argument("--verbose", action="store_true")
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
    rows = evaluate(cases, args.kmax, args.route, args.miss_opens, args.graph)
    report(rows, ks, args.kmax, args.verbose)
    sys.exit(0)


if __name__ == "__main__":
    main()
