#!/usr/bin/env python3
"""eval.py — recall + token-cost scoreboard for the wiki retriever. stdlib only, no network.

WHY: every retrieval change (router-skip, graph-expand, hybrid-dense) must be *measured*,
not asserted. This is the scoreboard. It runs a fixed set of cases
(`_meta/eval/cases.jsonl`) through the CURRENT retriever and reports:

  - recall@k  — is an expected target note in the top-k ranking? (k=5 and k=10)
  - token proxy — chars (≈tokens) a naive QUERY answer path would consume:
        index bytes the routing step reads (global index.md + index.<domain>.md)
      + reference-note body bytes read top-down until the FIRST expected target
        is reached (capped at --kmax); a miss "reads" kmax notes and still fails.

FAITHFULNESS: it does NOT re-implement scoring. It imports kb.py and replays
kb.load() + kb.score() + kb's exact sort, so the ranking is identical to
`python3 kb.py --domain <d> search "<q>"` with default flags (gated notes excluded).

GRACEFUL: with --route it accounts the routing cost as index.<domain>.md only
(Phase 1, skip the global index). --hybrid/--expand are reserved for later phases;
absent those flags the baseline is pure lexical over the reference tier.

Usage:
    python3 wiki/_meta/bin/eval.py
    python3 wiki/_meta/bin/eval.py --verbose
    python3 wiki/_meta/bin/eval.py --route          # Phase 1 accounting (skip index.md)
    python3 wiki/_meta/bin/eval.py --cases _meta/eval/cases.jsonl --kmax 10
"""
import argparse
import json
import os
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))
sys.dont_write_bytecode = True          # keep _meta/bin/ free of __pycache__
sys.path.insert(0, BIN)
import kb                               # faithful: reuse the real loader + ranker

CHARS_PER_TOKEN = 4                     # air-gap-safe heuristic (matches lint.py); no tiktoken

_recs_cache = {}


def records(domain):
    if domain not in _recs_cache:
        _recs_cache[domain] = kb.load(domain) or []
    return _recs_cache[domain]


def note_ids(domain):
    return {r.get("id") for r in records(domain)}


def index_bytes(domain, route):
    """Bytes the QUERY routing step reads. Baseline = global index.md + the
    per-domain index; --route (Phase 1) skips the global index.md."""
    total = 0
    if not route:
        g = os.path.join(WIKI, "index.md")
        if os.path.isfile(g):
            total += os.path.getsize(g)
    d = os.path.join(WIKI, "index.%s.md" % domain)
    if os.path.isfile(d):
        total += os.path.getsize(d)
    return total


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
    # EXACT same sort key as kb.cmd_search (score desc, newest-version tiebreak)
    scored.sort(key=lambda x: (-x[0], -kb.vkey(x[1].get("version"))[0] if x[1].get("version") else 0))
    return [(r.get("id"), len(bt)) for _, r, bt in scored]


def first_hit(ranked_ids, expected):
    for i, rid in enumerate(ranked_ids, 1):
        if rid in expected:
            return i
    return None


def evaluate(cases, kmax, route):
    rows = []
    for c in cases:
        domain = c.get("domain")
        expected = set(c["expect_any_of"])
        ranked = rank(domain, c["query"])
        ids = [rid for rid, _ in ranked]
        lens = [ln for _, ln in ranked]
        hit = first_hit(ids, expected)                       # 1-based rank or None
        read = min(hit, kmax) if hit else min(kmax, len(ids))  # notes a naive path reads
        body_chars = sum(lens[:read])
        idx_chars = index_bytes(domain, route)
        proxy_chars = idx_chars + body_chars
        rows.append({
            "query": c["query"], "domain": domain, "kind": c.get("kind", "?"),
            "expected": sorted(expected), "hit_rank": hit,
            "notes_read": read, "idx_chars": idx_chars, "proxy_chars": proxy_chars,
            "top5": ids[:5],
        })
    return rows


def validate(cases):
    """Every expected target must be a real, loadable note id for its domain."""
    bad = []
    for c in cases:
        ids = note_ids(c.get("domain"))
        for t in c["expect_any_of"]:
            if t not in ids:
                bad.append((c["domain"], t, c["query"][:50]))
    return bad


def pct(n, d):
    return (100.0 * n / d) if d else 0.0


def report(rows, ks, verbose):
    n = len(rows)
    print("=" * 78)
    print("RETRIEVER EVAL — %d cases" % n)
    print("=" * 78)

    if verbose:
        print("\nPer-case:")
        for r in rows:
            mark = ("@%d" % r["hit_rank"]) if r["hit_rank"] else "MISS"
            print("  [%-12s %-15s] hit=%-5s read=%2d proxy≈%6dtok  %s"
                  % (r["kind"], r["domain"], mark, r["notes_read"],
                     r["proxy_chars"] // CHARS_PER_TOKEN, r["query"][:60]))
            if not r["hit_rank"]:
                print("        expected one of: %s" % ", ".join(r["expected"]))
                print("        top5 lexical:    %s" % ", ".join(r["top5"]) or "(none)")

    def recall_at(k, subset):
        sub = [r for r in subset if r["domain"]] if subset is None else subset
        hits = sum(1 for r in sub if r["hit_rank"] and r["hit_rank"] <= k)
        return hits, len(sub)

    print("\nRECALL")
    for k in ks:
        h, d = recall_at(k, rows)
        print("  recall@%-2d : %2d/%-2d  (%.0f%%)" % (k, h, d, pct(h, d)))

    print("\n  by domain:")
    for dom in sorted({r["domain"] for r in rows}):
        sub = [r for r in rows if r["domain"] == dom]
        line = "    %-18s" % dom
        for k in ks:
            h, d = recall_at(k, sub)
            line += "  r@%d %d/%d" % (k, h, d)
        print(line)

    print("\n  by kind:")
    for kind in sorted({r["kind"] for r in rows}):
        sub = [r for r in rows if r["kind"] == kind]
        line = "    %-18s" % kind
        for k in ks:
            h, d = recall_at(k, sub)
            line += "  r@%d %d/%d" % (k, h, d)
        print(line)

    print("\nTOKEN-COST PROXY  (index reads + bodies read to first hit; chars/%d)" % CHARS_PER_TOKEN)
    mean_read = sum(r["notes_read"] for r in rows) / n
    mean_proxy = sum(r["proxy_chars"] for r in rows) / n
    mean_idx = sum(r["idx_chars"] for r in rows) / n
    mean_body = mean_proxy - mean_idx
    print("  mean notes read / case : %.2f" % mean_read)
    print("  mean index tokens      : %6d" % (mean_idx / CHARS_PER_TOKEN))
    print("  mean body  tokens      : %6d" % (mean_body / CHARS_PER_TOKEN))
    print("  mean TOTAL proxy tokens: %6d   <-- the number Phases 1-3 must drop" % (mean_proxy / CHARS_PER_TOKEN))

    misses = [r for r in rows if not r["hit_rank"]]
    if misses:
        print("\nMISSES @%d (the recall gap Phase 2/3 must close): %d" % (max(ks), len(misses)))
        for r in misses:
            print("  - [%s] %s" % (r["kind"], r["query"][:66]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "cases.jsonl"))
    ap.add_argument("--k", default="5,10", help="comma-separated recall cutoffs (default 5,10)")
    ap.add_argument("--kmax", type=int, default=10, help="max notes a naive path reads (default 10)")
    ap.add_argument("--route", action="store_true", help="Phase-1 accounting: skip global index.md")
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

    bad = validate(cases)
    if bad:
        print("INVALID TARGETS (expected note id not found in its domain reference tier):")
        for dom, t, q in bad:
            print("  - [%s] %s   (case: %s…)" % (dom, t, q))
        print("Fix cases.jsonl before trusting recall numbers.\n")

    ks = [int(x) for x in args.k.split(",")]
    rows = evaluate(cases, args.kmax, args.route)
    report(rows, ks, args.verbose)
    sys.exit(0)


if __name__ == "__main__":
    main()
