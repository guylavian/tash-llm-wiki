#!/usr/bin/env python3
"""faithfulness_probe.py — CI probe for ranking parity + the LLM synthesis faithfulness eval.

Two sections, in order:

1. RANKING PARITY (deterministic, stdlib, always runs — WI-5 acceptance): asserts that the four
   ranked surfaces — kb CLI search, serve /search, graph retrieve_node, evaluate.rank — produce
   IDENTICAL ordered ids for the same domain/query/pool, i.e. they all consume kb.lexical_rank
   (the single ranking home) and none has drifted back to a private re-implementation. Queries
   come from the frozen eval cases. Dense fusion is forced off for the comparison (the parity
   contract is about the lexical primitive; hybrid consumes its output and is probed elsewhere).

2. SYNTHESIS (wraps wikikb.quality.faithfulness — the real eval logic, no re-implementation,
   BF-4). Needs an active LLM gateway; when the gateway is off this section is SKIPPED with a
   notice (it does NOT fail the probe — parity alone then decides the exit code).

Pairs with: eval.py (retrieval recall), gate_probe.py (tier-coverage gate),
gate_page_probe.py (page-level provenance gate).

Usage:
    python3 wiki/_meta/tests/faithfulness_probe.py
    python3 wiki/_meta/tests/faithfulness_probe.py --cases _meta/eval/faithfulness_cases.jsonl
    python3 wiki/_meta/tests/faithfulness_probe.py --verbose

Exit code: 0 = parity passed and synthesis passed-or-skipped, 1 = ≥1 failure, 2 = bad input.
"""
import argparse
import contextlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
WIKI = os.path.dirname(META)                            # wiki
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable

from wikikb.quality import faithfulness

PARITY_K = 5                    # retrieve_node's default candidate window
PARITY_QUERIES_PER_DOMAIN = 2   # frozen eval-case queries sampled per domain


def _parity_queries(cases_path):
    """(domain, query) pairs from the frozen eval bank — first N per domain, stable order."""
    out, per_dom = [], {}
    with open(cases_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            c = json.loads(line)
            d = c.get("domain")
            if not d or per_dom.get(d, 0) >= PARITY_QUERIES_PER_DOMAIN:
                continue
            per_dom[d] = per_dom.get(d, 0) + 1
            out.append((d, c["query"]))
    return out


def run_parity(verbose=False):
    """WI-5 acceptance: identical ordered ids across the four ranked surfaces. Returns #failures.
    embed.dense_rank is patched to None ONLY for the duration of this function (try/finally):
    parity is the lexical-primitive contract, but the synthesis section that may follow must see
    the real dense layer."""
    import re
    from wikikb.retrieval import kb, embed
    from wikikb.graph import nodes
    from wikikb.serve import serve
    from wikikb.quality import evaluate

    _orig_dense = embed.dense_rank
    embed.dense_rank = lambda *a, **k: None   # force lexical for the comparison
    try:
        return _run_parity_inner(re, kb, nodes, serve, evaluate, verbose)
    finally:
        embed.dense_rank = _orig_dense


def _run_parity_inner(re, kb, nodes, serve, evaluate, verbose):
    cases_path = os.path.join(WIKI, "_meta", "eval", "cases.jsonl")
    pairs = _parity_queries(cases_path)
    if not pairs:
        print("parity: no eval cases found at %s" % cases_path, file=sys.stderr)
        return 1

    print("=" * 84)
    print("RANKING PARITY — kb.lexical_rank is the single home (%d domain/query pairs)" % len(pairs))
    print("surfaces: kb CLI search | serve /search | graph retrieve_node | evaluate.rank")
    print("=" * 84)
    fails = 0
    for domain, query in pairs:
        _terms, _pool, scored = kb.lexical_rank(domain, query)
        prim_ids = [r.get("id") for _, r, _ in scored]

        eval_ids = [rid for rid, _ in evaluate.rank(domain, query)]
        _st, hits = serve.do_search(domain, query, PARITY_K)
        serve_ids = [h["id"] for h in hits] if _st == 200 else ["<http %s>" % _st]
        node_ids = [cid for cid, _ in
                    nodes.retrieve_node({"domain": domain, "query": query, "k": PARITY_K})["candidates"]]

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            kb.cmd_search(kb.load(domain) or [], argparse.Namespace(
                query=query.split(), domain=domain, all_domains=False, kind=None, guide=None,
                version=None, family=None, primary=False, gated=False, hybrid=False,
                limit=PARITY_K, full=False))
        cli_out = buf.getvalue()
        cli_count = None
        m = cli_out.split(" hit(s)", 1)
        if len(m) == 2:
            try:
                cli_count = int(m[0].splitlines()[-1])
            except ValueError:
                pass
        # full ordered top-k sequence, not just the top hit: parse every numbered result line's
        # title ("NN. [ref] TITLE" — single-domain fetched-only, so no {dom} prefix / gate suffix)
        cli_titles = [t for _n, t in re.findall(r"^\s*(\d+)\.\s+\[[^\]]*\]\s+(.+)$", cli_out, re.M)]
        prim_titles = [r.get("title") for _, r, _ in scored[:PARITY_K]]
        cli_ok = (cli_count == len(prim_ids) and cli_titles == prim_titles) if prim_ids \
                 else ("No matches" in cli_out)

        checks = [
            ("evaluate.rank == primitive", eval_ids == prim_ids),
            ("serve /search == primitive[:k]", serve_ids == prim_ids[:PARITY_K]),
            ("retrieve_node == primitive[:k]", node_ids == prim_ids[:PARITY_K]),
            ("kb CLI hit-count+top-title == primitive", cli_ok),
        ]
        bad = [name for name, ok in checks if not ok]
        status = "PASS" if not bad else "FAIL"
        if bad:
            fails += 1
        print("  %s  {%s} %r%s" % (status, domain, query[:60], ("  <- " + "; ".join(bad)) if bad else ""))
        if verbose or bad:
            print("        primitive[:%d]=%s" % (PARITY_K, prim_ids[:PARITY_K]))
            if bad:
                print("        eval=%s serve=%s node=%s cli_count=%s" % (
                    eval_ids[:PARITY_K], serve_ids, node_ids, cli_count))
    print("parity: %d/%d pairs consistent" % (len(pairs) - fails, len(pairs)))
    return fails


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "faithfulness_cases.jsonl"))
    ap.add_argument("--verbose", action="store_true", help="per-case details")
    args = ap.parse_args()

    parity_fails = run_parity(verbose=args.verbose)

    # Check LLM availability — the synthesis section needs a live gateway; parity does not.
    try:
        from wikikb.online import llm
        llm_active = llm.available()
    except Exception:
        llm_active = False

    if not llm_active:
        print("SYNTHESIS SECTION SKIPPED — LLM gateway not active "
              "(set WIKI_LLM=local + llm.config.yaml to run it).", file=sys.stderr)
        sys.exit(1 if parity_fails else 0)
    if parity_fails:
        print("RANKING PARITY FAILED — fix before reading synthesis results", file=sys.stderr)

    cases = faithfulness.load_cases(args.cases)
    if not cases:
        print("no faithfulness cases found at %s" % args.cases, file=sys.stderr)
        sys.exit(2)

    print("=" * 84)
    print("FAITHFULNESS PROBE — LLM synthesis quality (%d cases)" % len(cases))
    print("checks: citation-recall | LLM-produced | term-overlap | no-contamination | gate-correct")
    print("=" * 84)

    rows = []
    for c in cases:
        r = faithfulness.check_case(c, verbose=args.verbose)
        rows.append(r)

    s = faithfulness.score(rows)
    faithfulness.report(rows, s, verbose=args.verbose)

    print("-" * 84)
    n_pass = s["all_pass"]
    n_total = s["n"]
    print("%d/%d cases passed" % (n_pass, n_total))

    if n_pass < n_total or parity_fails:
        print("FAILURES — %s detected" % ("ranking-parity + synthesis gaps" if parity_fails and n_pass < n_total
                                          else "ranking-parity drift" if parity_fails
                                          else "synthesis quality gaps"), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
