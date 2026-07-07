#!/usr/bin/env python3
"""faithfulness_probe.py — CI probe for the LLM synthesis faithfulness eval.

Wraps wikikb.quality.faithfulness (the real eval logic — no re-implementation, BF-4).
Runs all faithfulness cases and exits 0/1 for CI gate usage.

Pairs with: eval.py (retrieval recall), gate_probe.py (tier-coverage gate),
gate_page_probe.py (page-level provenance gate). This is the SYNTHESIS quality gate.

Usage:
    python3 wiki/_meta/tests/faithfulness_probe.py
    python3 wiki/_meta/tests/faithfulness_probe.py --cases _meta/eval/faithfulness_cases.jsonl
    python3 wiki/_meta/tests/faithfulness_probe.py --verbose

Exit code: 0 = all cases pass, 1 = ≥1 case failed, 2 = bad input / LLM unavailable.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
WIKI = os.path.dirname(META)                            # wiki
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable

from wikikb.quality import faithfulness


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "faithfulness_cases.jsonl"))
    ap.add_argument("--verbose", action="store_true", help="per-case details")
    args = ap.parse_args()

    # Check LLM availability
    try:
        from wikikb.online import llm
        llm_active = llm.available()
    except Exception:
        llm_active = False

    if not llm_active:
        print("FAITHFULNESS PROBE — LLM synthesis tier not active.", file=sys.stderr)
        print("  Set WIKI_LLM=local and configure llm.config.yaml before running.", file=sys.stderr)
        print("  (The probe exits 2 to signal a configuration gap, not a quality failure.)", file=sys.stderr)
        sys.exit(2)

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

    if n_pass < n_total:
        print("FAILURES — synthesis quality gaps detected", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
