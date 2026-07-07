#!/usr/bin/env python3
"""livebank.py — the live-query bank: `wikikb livebank`. stdlib only, no network.

BRIEF O2: two "clean" structural-validation rounds passed, then the first real user question
surfaced a wrong cached number and a dropped table. This is the sign-off gate that would have
caught it — it runs realistic 3am-SRE queries (short, jargony: "ospf stuck exstart") through the
FULL serve path, not a frontmatter/lint check.

Each case in eval/livebank.jsonl calls `wikikb.graph.ask.ask()` IN-PROCESS — the same route ->
retrieve -> expand-if-thin -> gate -> synthesize sequence the CLI/serve path runs (faithful: no
re-implementation) — and checks:
  - expect_facts / forbid: graded against the ANSWER TEXT ONLY (2026-07 audit fix — grading
    against "answer + candidate bodies" let a factless "[extractive fallback]" answer pass just
    because the right fact happened to be floating in the retrieved corpus; the thing a real user
    reads is the answer, so that is the only thing a fact claim can be checked against).
  - expect_gate: "none" -> banner empty; "gate-note" -> a banner mentions the untiered/partial-coverage
    note (gate_node's "coverage gate not evaluated" line); "out-of-coverage" -> a real H1 banner
    (lint.gate_banner's "out-of-coverage: ..." line). Matched on the distinguishing phrase rather than
    the shared "(H1)" suffix so the two banners can't be confused for each other. ALWAYS graded,
    fallback-answer or not — a gate mismatch is a FAIL regardless.

Outcome per case is one of PASS / FAIL / UNGRADED:
  - When the pipeline produced no real model prose (the deterministic "[extractive fallback ...]"
    or the "[ungrounded synthesis withheld ...]" answer — see graph/nodes.py), there is no prose
    to check a fact claim against: it is structurally impossible to grade, so the case is UNGRADED,
    never counted as a PASS (and never as a FAIL either) — UNLESS the gate itself mismatches, which
    is graded unconditionally and fails the case outright.
  - Otherwise PASS iff every expect_facts regex is found, no forbid regex is found, and the gate
    matches expect_gate.
The scoreboard reports the pass rate over GRADED cases only, plus an explicit UNGRADED count so an
ungraded case can never silently masquerade as a pass.

Usage:
    python3 -m wikikb livebank                    # full bank, text scoreboard
    python3 -m wikikb livebank --ci                # only the ci:true fast subset
    python3 -m wikikb livebank --json              # structured output for agents
    python3 -m wikikb livebank --cases PATH         # run against an alternate case file
    python3 -m wikikb livebank --min-pass 80       # exit 3 if graded pass rate < 80%
"""
import argparse
import json
import os
import re
import sys

from wikikb import paths
EVAL = str(paths.EVAL)
sys.dont_write_bytecode = True

from wikikb.graph import ask as ask_pipeline   # the real QUERY pipeline (faithful, no re-implementation)

DEFAULT_CASES = os.path.join(EVAL, "livebank.jsonl")

# The two shapes graph/nodes.synthesize_node emits when there is no real model prose to grade —
# a case can never be scored PASS/FAIL against these, only UNGRADED (see module docstring).
_UNGRADED_MARKERS = ("[extractive fallback", "[ungrounded synthesis withheld")


def load_cases(path=None):
    path = path or DEFAULT_CASES
    if not os.path.isfile(path):
        print("livebank cases not found: %s" % path, file=sys.stderr)
        sys.exit(2)
    cases = []
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                c = json.loads(line)
            except json.JSONDecodeError as e:
                print("bad JSON at line %d: %s" % (ln, e), file=sys.stderr)
                sys.exit(2)
            c.setdefault("tier", None)
            c.setdefault("expect_facts", [])
            c.setdefault("forbid", [])
            c.setdefault("expect_gate", "none")
            c.setdefault("ci", False)
            cases.append(c)
    return cases


def _search_any(pattern, text):
    return re.search(pattern, text, re.IGNORECASE) is not None


def _gate_ok(banner, expect_gate):
    banner = banner or []
    low = [b.lower() for b in banner]
    if expect_gate == "none":
        return len(banner) == 0
    if expect_gate == "gate-note":
        return any("coverage gate not evaluated" in b for b in low)
    if expect_gate == "out-of-coverage":
        return any("out-of-coverage" in b for b in low)
    print("unknown expect_gate label %r — treating as FAILURE" % expect_gate, file=sys.stderr)
    return False


def _is_ungraded_answer(answer):
    """True iff `answer` is a deterministic fallback/withheld shape with no real model prose to
    grade a fact claim against (see _UNGRADED_MARKERS)."""
    return any(m in (answer or "") for m in _UNGRADED_MARKERS)


def check_case(c):
    """Run the ask pipeline for one case; return a result dict with per-check detail and an
    `outcome` of PASS / FAIL / UNGRADED (never a bare bool — see module docstring)."""
    st = ask_pipeline.ask(c["query"], domain=c["domain"], k=5, question_tier=c.get("tier"))
    answer = st.get("answer", "")
    banner = st.get("banner") or []
    candidates = st.get("candidates", [])

    # expect_facts/forbid are graded against the ANSWER TEXT ONLY (not candidate bodies — a fact
    # merely present in the retrieved corpus but never surfaced in the answer is not "served").
    missing_facts = [p for p in c["expect_facts"] if not _search_any(p, answer)]
    hit_forbid = [p for p in c["forbid"] if _search_any(p, answer)]
    gate_ok = _gate_ok(banner, c["expect_gate"])
    ungraded = _is_ungraded_answer(answer)

    if not gate_ok:
        outcome = "FAIL"                      # the gate is ALWAYS graded, fallback answer or not
    elif ungraded:
        outcome = "UNGRADED"                  # no real prose — structurally impossible to grade facts
    else:
        outcome = "PASS" if (not missing_facts and not hit_forbid) else "FAIL"

    return {
        "id": c["id"], "domain": c["domain"], "tier": c.get("tier"), "query": c["query"],
        "outcome": outcome,
        "ungraded": ungraded,
        "missing_facts": missing_facts,
        "hit_forbid": hit_forbid,
        "gate_ok": gate_ok, "expect_gate": c["expect_gate"], "banner": banner,
        "n_candidates": len(candidates),
        "answer_preview": answer[:160],
    }


def scoreboard(rows):
    """Per-domain: pass/graded (ungraded excluded from the denominator) + an explicit ungraded count."""
    by_domain = {}
    for r in rows:
        d = by_domain.setdefault(r["domain"], {"pass": 0, "graded": 0, "ungraded": 0, "total": 0})
        d["total"] += 1
        if r["outcome"] == "UNGRADED":
            d["ungraded"] += 1
        else:
            d["graded"] += 1
            d["pass"] += 1 if r["outcome"] == "PASS" else 0
    return by_domain


def report(rows):
    total_graded = sum(1 for r in rows if r["outcome"] != "UNGRADED")
    total_pass = sum(1 for r in rows if r["outcome"] == "PASS")
    total_ungraded = sum(1 for r in rows if r["outcome"] == "UNGRADED")
    n_gate_ok = sum(1 for r in rows if r["gate_ok"])
    print("=" * 84)
    print("LIVE-QUERY BANK — %d cases" % len(rows))
    print("=" * 84)
    print("\nPer-domain pass rate (graded cases only; UNGRADED excluded from the rate):")
    for d, s in sorted(scoreboard(rows).items()):
        pct = graded_pass_pct(s["pass"], s["graded"])
        print("  %-18s %3d/%-3d graded (%3.0f%%)   ungraded=%d" % (d, s["pass"], s["graded"], pct, s["ungraded"]))
    print("\nOVERALL: %d/%d graded (%.0f%%)   UNGRADED: %d" %
          (total_pass, total_graded, graded_pass_pct(total_pass, total_graded), total_ungraded))
    print("GATE checks: %d/%d passing (%.0f%%) — graded independently of fact-grading" %
          (n_gate_ok, len(rows), pct_of(n_gate_ok, len(rows))))

    fails = [r for r in rows if r["outcome"] == "FAIL"]
    ungraded = [r for r in rows if r["outcome"] == "UNGRADED"]
    if fails:
        print("\nFAILURES:")
        for r in fails:
            print("  [%s] %s (%s / tier=%s)" % (r["id"], r["query"][:70], r["domain"], r["tier"]))
            if r["missing_facts"]:
                print("        missing expect_facts: %s" % r["missing_facts"])
            if r["hit_forbid"]:
                print("        hit forbid: %s" % r["hit_forbid"])
            if not r["gate_ok"]:
                print("        gate mismatch: expected=%s got banner=%s" % (r["expect_gate"], r["banner"]))
    else:
        print("\nNo graded failures.")
    if ungraded:
        print("\nUNGRADED (no real model prose — fact claims not checked; gate still passed):")
        for r in ungraded:
            print("  [%s] %s (%s / tier=%s) — %s" % (r["id"], r["query"][:70], r["domain"], r["tier"],
                                                       r["answer_preview"][:60]))


def pct_of(n, d):
    return (100.0 * n / d) if d else 0.0


def graded_pass_pct(n_pass, n_graded):
    """Pass rate over GRADED cases only. Vacuously 100% when nothing was gradable (n_graded == 0,
    e.g. every case in the bank hit the offline extractive fallback) — UNGRADED is not a failure
    signal, so an all-UNGRADED run must never trip --min-pass on its own."""
    return 100.0 if n_graded == 0 else pct_of(n_pass, n_graded)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=None, help="path to livebank.jsonl (default: eval/livebank.jsonl)")
    ap.add_argument("--ci", action="store_true", help="run only the ci:true fast subset")
    ap.add_argument("--json", action="store_true", help="structured output for agents")
    ap.add_argument("--min-pass", type=float, default=None, dest="min_pass",
                    help="exit 3 if the GRADED pass rate is below this percentage")
    args = ap.parse_args()

    cases = load_cases(args.cases)
    if args.ci:
        cases = [c for c in cases if c.get("ci")]
    if not cases:
        print("no cases to run" + (" (--ci matched none)" if args.ci else ""), file=sys.stderr)
        sys.exit(2)

    rows = [check_case(c) for c in cases]
    total_graded = sum(1 for r in rows if r["outcome"] != "UNGRADED")
    total_pass = sum(1 for r in rows if r["outcome"] == "PASS")
    total_ungraded = sum(1 for r in rows if r["outcome"] == "UNGRADED")
    graded_pct = graded_pass_pct(total_pass, total_graded)

    if args.json:
        print(json.dumps({"n": len(rows), "n_graded": total_graded, "n_ungraded": total_ungraded,
                          "graded_pass_pct": graded_pct, "by_domain": scoreboard(rows),
                          "results": rows}, indent=2, ensure_ascii=False))
    else:
        report(rows)

    if args.min_pass is not None and graded_pct < args.min_pass:
        sys.exit(3)


if __name__ == "__main__":
    main()
