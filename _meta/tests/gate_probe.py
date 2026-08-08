#!/usr/bin/env python3
"""gate_probe.py — verify the QUERY Confidence gate's tier-coverage arm. stdlib only.

WHY: the Confidence gate (CLAUDE.md, Operation: QUERY) is a POLICY. A policy *described*
as working is not *verified* as working — the same "not on luck" bar the wiki applies to
the corpus must apply to the gate itself. This converts the gate's deterministic tier-arm
into a CI assertion: a question of `question_tier` against a `domain` whose
`tiers-covered:` (in _meta/taxonomy.md) lacks that tier MUST yield `out-of-coverage`; a
domain that covers the tier MUST NOT fire.

It tests GATE BEHAVIOR, not answer correctness — so it is O(1) per question-class, not
O(human) per gap (no need to pre-know the right answer to each probe). The negative case
(a covered tier that must NOT fire) is what catches over-firing — a probe with only
positive cases is half a probe.

It is also a live COVERAGE TRACKER: when a missing tier is finally ingested and its
`tiers-covered:` is updated, the corresponding positive case flips to FAIL — forcing the
expectation to be updated, i.e. signalling the gap is closed.

Pairs with: eval.py (recall), lint.py (the page-level `extracted==0` / reviewed-incoherence
arm over filed pages).

Usage:
    python3 wiki/_meta/tests/gate_probe.py
    python3 wiki/_meta/tests/gate_probe.py --cases _meta/eval/gate_cases.jsonl
Exit code: 0 = all pass, 1 = a case failed (CI gate), 2 = bad input.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable
# WIKI comes from wikikb.paths — the ONE definition. Re-deriving it here as
# `os.path.dirname(META)` silently broke when content moved under <repo>/vault/ (2026-08-05),
# and it also ignored WIKIKB_VAULT_ROOT, so a sandboxed run probed the live tree.
from wikikb import paths as _paths  # noqa: E402 — must follow the sys.path bootstrap
WIKI = str(_paths.WIKI)

# The H1 rule + tiers-covered parsing live in the package (wikikb.coverage) so the LangGraph gate
# node, lint.gate_banner, and THIS probe assert the SAME code (the faithfulness invariant). The probe
# re-exports them so its body below is unchanged.
from wikikb.quality.coverage import gate_verdict, load_tiers_covered  # noqa: F401


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(str(_paths.EVAL), "gate_cases.jsonl"))
    args = ap.parse_args()

    tiers = load_tiers_covered()
    path = args.cases if os.path.isabs(args.cases) else os.path.join(str(_paths.ROOT), args.cases)
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
                print("bad JSON at line %d: %s" % (ln, e))
                sys.exit(2)

    print("=" * 80)
    print("CONFIDENCE-GATE PROBE — tier-coverage arm  (%d cases)" % len(cases))
    print("tiers-covered (parsed from taxonomy.md):")
    for d in sorted(tiers):
        print("  %-18s %s" % (d, tiers[d]))
    print("=" * 80)

    fails = []
    for c in cases:
        dom = c["domain"]
        covered = tiers.get(dom)
        if covered is None:
            fails.append(c)
            print("  FAIL  [%s] domain not declared / no tiers-covered in taxonomy" % dom)
            continue
        verdict = gate_verdict(c["question_tier"], covered)
        ok = (verdict == c["expect_gate"])
        if not ok:
            fails.append(c)
        print("  %s  %-16s tier=%-10s covered=%-24s => %-15s (expect %-15s)"
              % ("PASS" if ok else "FAIL", dom, c["question_tier"], str(covered),
                 verdict, c["expect_gate"]))
        print("          q: %s" % c["query"][:78])
    print("-" * 80)
    print("%d/%d passed%s" % (len(cases) - len(fails), len(cases),
                              "" if not fails else "  — FAILURES ABOVE"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
