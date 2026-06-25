#!/usr/bin/env python3
"""gate_page_probe.py — verify the PAGE-LEVEL arm of the Confidence gate. stdlib only.

FAITHFUL: imports lint.py and calls lint.page_gate_verdict() — the SAME rule lint
enforces — so the probe can NOT drift from enforcement (as eval.py imports kb.py).

Tests GATE BEHAVIOUR (does the provenance arm flag a page), NOT answer-correctness — so
it is O(1) per page and never needs to know the "right answer" to a question. The
negative (clean) case is the calibration proof: without it the probe only shows
over-eager firing, not correctness.

Cases: _meta/eval/gate_page_cases.jsonl  {page, expect ∈ {flag, clean}, why}
Exit: 0 all pass · 1 a case failed (CI gate) · 2 bad input.

Usage:
    python3 wiki/_meta/tests/gate_page_probe.py
    python3 wiki/_meta/tests/gate_page_probe.py --cases _meta/eval/gate_page_cases.jsonl
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
WIKI = os.path.dirname(META)                            # wiki
sys.dont_write_bytecode = True
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable
from wikikb.quality import lint  # faithful: reuse the real frontmatter parser AND the gate rule


def verdict(page_path):
    """('flag'|'clean', reasons) for a page, via the exact rule lint enforces."""
    with open(page_path, encoding="utf-8") as fh:
        fm = lint.parse_frontmatter(fh.read())
    if fm is None:
        return "flag", ["no frontmatter"]
    reasons = lint.page_gate_verdict(fm)
    return ("flag" if reasons else "clean"), reasons


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "gate_page_cases.jsonl"))
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
                print("bad JSON at line %d: %s" % (ln, e))
                sys.exit(2)

    print("=" * 82)
    print("CONFIDENCE-GATE PROBE — page-level (provenance) arm  (%d cases)" % len(cases))
    print("rule: lint.page_gate_verdict() — H2 extracted==0, H3 reviewed AND inferred>=extracted")
    print("=" * 82)

    fails = []
    for c in cases:
        pg = os.path.join(WIKI, c["page"])
        if not os.path.isfile(pg):
            fails.append(c)
            print("  FAIL  %-48s — page not found" % c["page"])
            continue
        v, reasons = verdict(pg)
        ok = (v == c["expect"])
        if not ok:
            fails.append(c)
        print("  %s  %-48s => %-6s (expect %-6s)" % ("PASS" if ok else "FAIL", c["page"], v, c["expect"]))
        if reasons:
            print("          fired: %s" % "; ".join(reasons))
    print("-" * 82)
    print("%d/%d passed%s" % (len(cases) - len(fails), len(cases),
                              "" if not fails else "  — FAILURES ABOVE"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
