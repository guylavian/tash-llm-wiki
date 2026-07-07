#!/usr/bin/env python3
"""faithfulness.py — eval harness for the LLM synthesis tier. stdlib only at import.

Measures whether the LLM's answers to known questions are *faithful* to the retrieved context:
1. **Citation recall** — does the LLM cite the correct reference notes?
2. **Substance** — did the LLM produce actual text (not just extractive fallback)?
3. **Term overlap** — does the answer mention key terms from the expected notes?
4. **No contamination** — does the answer avoid obviously unrelated concepts?
5. **Gate correctness** — does the Confidence banner fire / not-fire as expected?

This is the synthesis twin of evaluate.py (which measures retrieval recall). The gap between
the two isolates: retrieval-perfect but synthesis-wrong (hallucination, mis-citation).

Faithfulness cases: _meta/eval/faithfulness_cases.jsonl — one JSON object per line:
  {query, domain, kind, expect_any_of, expect_terms, reject_terms, expect_gate, question_tier}

Usage:
    python3 -m wikikb faithfulness                          # run all cases, summary
    python3 -m wikikb faithfulness --verbose                 # per-case details
    python3 -m wikikb faithfulness --cases _meta/eval/faithfulness_cases.jsonl
    python3 -m wikikb faithfulness --golden _meta/eval/baseline.eval.faithfulness.out --diff
"""
import argparse
import json
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
EVAL = str(paths.EVAL)
sys.dont_write_bytecode = True

# Import the real ask pipeline (faithful: same nodes as the --json CLI, no re-implementation)
from wikikb.graph import ask as ask_pipeline
from wikikb.retrieval import kb
from wikikb.quality import lint, coverage


# ---------- case loading ------------------------------------------------------------------------

def load_cases(case_path=None):
    """Load faithfulness cases from a JSONL file."""
    if case_path is None:
        case_path = os.path.join(EVAL, "faithfulness_cases.jsonl")
    if not os.path.isfile(case_path):
        print("faithfulness cases not found: %s" % case_path, file=sys.stderr)
        sys.exit(2)
    cases = []
    with open(case_path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                c = json.loads(line)
                c.setdefault("expect_terms", [])
                c.setdefault("reject_terms", [])
                c.setdefault("expect_gate", "none")
                c.setdefault("question_tier", "conceptual")
                cases.append(c)
            except json.JSONDecodeError as e:
                print("bad JSON at line %d: %s" % (ln, e), file=sys.stderr)
                sys.exit(2)
    return cases


# ---------- term extraction from expected notes (stdlib) ----------------------------------------

def extract_terms_from_notes(domain, note_ids, topn=15):
    """Extract the top-N meaningful terms from a set of reference note bodies.
    Simple TF: split on non-alpha, filter stopwords + short words, count, return top-N."""
    stopwords = {"the", "and", "for", "are", "but", "not", "you", "all", "can", "had", "her",
                 "was", "one", "our", "out", "has", "have", "been", "was", "were", "from", "this",
                 "that", "with", "will", "each", "make", "like", "just", "over", "such", "than",
                 "them", "very", "when", "come", "could", "into", "time", "only", "its", "also",
                 "after", "some", "then", "these", "two", "may", "might", "must", "should",
                 "using", "used", "use", "set", "see", "way", "get", "need", "based", "how"}
    term_counts = {}
    for r in (kb.load(domain) or []):
        if r.get("id") not in note_ids:
            continue
        body = kb.body_text(r)
        # extract words, keep alphanumeric with hyphens (e.g. "client-credentials", "dpop")
        for m in re.finditer(r"[A-Za-z][A-Za-z0-9-]{2,}", body):
            word = m.group(0).lower()
            if word in stopwords:
                continue
            # skip frontmatter keys
            if word in ("title", "type", "domain", "slug", "summary", "sources", "status", "updated",
                        "documentkind", "abstract", "url", "version", "body_status"):
                continue
            term_counts[word] = term_counts.get(word, 0) + 1
    # sort by count desc
    ranked = sorted(term_counts.items(), key=lambda kv: -kv[1])
    return [t for t, _ in ranked[:topn]]


# ---------- the single-case check ---------------------------------------------------------------

def check_case(c, verbose=False):
    """Run ask pipeline for one case and return a dict of faithfulness metrics.

    Checks:
    - citation_hit: any expected note appears in LLM references
    - llm_produced: answer is not extractive fallback
    - term_hit: answer contains ≥1 expected term (or auto-extracted from notes)
    - no_contamination: answer contains no rejected terms
    - gate_correct: banner matches expect_gate
    """
    query, domain = c["query"], c["domain"]
    expected = set(c.get("expect_any_of", []))
    expect_terms = [t.lower() for t in c.get("expect_terms", [])]
    reject_terms = [t.lower() for t in c.get("reject_terms", [])]
    expect_gate = c.get("expect_gate", "none")
    question_tier = c.get("question_tier", "conceptual")

    # Run the ask pipeline (uses LLM if WIKI_LLM=local, extractive if off)
    st = ask_pipeline.ask(query, domain=domain, k=5, question_tier=question_tier)
    answer = st.get("answer", "")
    banner = st.get("banner") or []
    refs = st.get("used", [])
    is_extractive = "[extractive fallback" in answer.lower()

    # 1. Citation recall — do the LLM's references include the expected notes?
    cited = set(refs)
    citation_hit = bool(expected & cited) if expected else None  # None = no expectation

    # 2. Substance — did the LLM produce text?
    llm_produced = not is_extractive

    # 3. Term overlap — answer contains key terms from expected notes
    # Auto-extract if no explicit terms provided
    if not expect_terms and expected:
        expect_terms = extract_terms_from_notes(domain, expected, topn=12)

    answer_lower = answer.lower()
    hit_terms = [t for t in expect_terms if t in answer_lower]
    term_hit = bool(hit_terms) if expect_terms else None

    # 4. Contamination — answer mentions unrelated concepts
    found_reject = [t for t in reject_terms if t in answer_lower]
    no_contamination = len(found_reject) == 0

    # 5. Gate correctness
    if expect_gate == "none":
        gate_correct = len(banner) == 0
    elif expect_gate == "out-of-coverage":
        gate_correct = any("out of coverage" in b.lower() for b in banner)
    else:
        # an unrecognized expect_gate label used to auto-pass silently — that let a typo'd case
        # rot in the suite forever without ever being checked. Fail loud instead.
        print("unknown expect_gate label %r (query=%r) — treating as FAILURE" % (expect_gate, query),
              file=sys.stderr)
        gate_correct = False

    result = {
        "query": query,
        "domain": domain,
        "kind": c.get("kind", "?"),
        "pair": c.get("pair"),
        "variant": c.get("variant"),
        "expected": sorted(expected),
        "citation_hit": citation_hit,
        "cited_refs": sorted(cited),
        "llm_produced": llm_produced,
        "is_extractive": is_extractive,
        "expect_terms": expect_terms,
        "hit_terms": hit_terms,
        "term_hit": term_hit,
        "no_contamination": no_contamination,
        "contamination": found_reject,
        "expect_gate": expect_gate,
        "banner": banner,
        "gate_correct": gate_correct,
        "answer_preview": answer[:120],
    }
    if verbose:
        result["answer"] = answer
    return result


# ---------- scoring + report --------------------------------------------------------------------

def score(rows):
    """Aggregate metrics from check_case results."""
    n = len(rows)
    if n == 0:
        return {}

    # Count non-None values for metrics that may be absent
    def pct_field(key):
        vals = [r[key] for r in rows if r[key] is not None]
        if not vals:
            return 0, 0
        return sum(1 for v in vals if v), len(vals)

    cite_ok, cite_total = pct_field("citation_hit")
    term_ok, term_total = pct_field("term_hit")
    llm_ok = sum(1 for r in rows if r["llm_produced"])
    contam_ok = sum(1 for r in rows if r["no_contamination"])
    gate_ok = sum(1 for r in rows if r["gate_correct"])
    all_ok = sum(1 for r in rows if all([
        (r["citation_hit"] if r["citation_hit"] is not None else True),
        r["llm_produced"],
        (r["term_hit"] if r["term_hit"] is not None else True),
        r["no_contamination"],
        r["gate_correct"],
    ]))

    return {
        "n": n,
        "cite_recall_pct": pct(cite_ok, cite_total),
        "cite_ok": cite_ok, "cite_total": cite_total,
        "term_overlap_pct": pct(term_ok, term_total),
        "term_ok": term_ok, "term_total": term_total,
        "llm_produced": llm_ok,
        "no_contamination": contam_ok,
        "gate_correct": gate_ok,
        "all_pass": all_ok,
        "all_pass_pct": pct(all_ok, n),
    }


def pct(n, d):
    return (100.0 * n / d) if d else 0.0


def report(rows, s, verbose=False):
    """Print the faithfulness eval report."""
    print("=" * 84)
    print("FAITHFULNESS EVAL — %d cases" % s["n"])
    print("=" * 84)

    if verbose:
        print("\nPer-case:")
        for r in rows:
            marks = []
            marks.append("C" if r["citation_hit"] else ("-" if r["citation_hit"] is None else "x"))
            marks.append("L" if r["llm_produced"] else "x")
            marks.append("T" if r["term_hit"] else ("-" if r["term_hit"] is None else "x"))
            marks.append("K" if r["no_contamination"] else "x")
            marks.append("G" if r["gate_correct"] else "x")
            tag = "".join(marks)
            all_ok = all([
                (r["citation_hit"] if r["citation_hit"] is not None else True),
                r["llm_produced"],
                (r["term_hit"] if r["term_hit"] is not None else True),
                r["no_contamination"],
                r["gate_correct"],
            ])
            status = "PASS" if all_ok else "FAIL"
            print("  [%s %-12s] %-5s %s" % (status, r["kind"], tag, r["query"][:60]))
            if not all_ok:
                if r["is_extractive"]:
                    print("        LLM did not produce text (extractive fallback)")
                if r["citation_hit"] is False:
                    print("        expected: %s | cited: %s" % (", ".join(r["expected"]), ", ".join(r["cited_refs"]) or "(none)"))
                if r["term_hit"] is False:
                    print("        expected terms: %s | hit: %s" % (", ".join(r["expect_terms"][:8]), ", ".join(r["hit_terms"]) or "(none)"))
                if not r["no_contamination"]:
                    print("        contamination: %s" % ", ".join(r["contamination"]))
                if not r["gate_correct"]:
                    print("        gate: expect=%s banner=%s" % (r["expect_gate"], r["banner"]))
            # Show the answer preview
            print("        => %s" % r["answer_preview"][:100])

    print("\nAGGREGATE:")
    print("  Citation recall  : %3d/%-3d (%3.0f%%)  — LLM cites the expected reference notes"
          % (s["cite_ok"], s["cite_total"], s["cite_recall_pct"]))
    print("  Term overlap     : %3d/%-3d (%3.0f%%)  — answer mentions key terms from expected notes"
          % (s["term_ok"], s["term_total"], s["term_overlap_pct"]))
    print("  LLM produced     : %3d/%-3d (%3.0f%%)  — LLM generated text (not extractive fallback)"
          % (s["llm_produced"], s["n"], pct(s["llm_produced"], s["n"])))
    print("  No contamination : %3d/%-3d (%3.0f%%)  — answer avoids unrelated concepts"
          % (s["no_contamination"], s["n"], pct(s["no_contamination"], s["n"])))
    print("  Gate correct     : %3d/%-3d (%3.0f%%)  — Confidence banner fires / doesn't fire correctly"
          % (s["gate_correct"], s["n"], pct(s["gate_correct"], s["n"])))
    print("  ALL PASS         : %3d/%-3d (%3.0f%%)"
          % (s["all_pass"], s["n"], s["all_pass_pct"]))

    print("\nLegend: C=citation L=LLM-produced T=term-overlap K=no-contamination G=gate-correct")
    print("  - = metric not applicable for this case")


# ---------- golden comparison -------------------------------------------------------------------

def load_golden(path):
    """Load a baseline golden output (the aggregate section of a previous run)."""
    if not os.path.isfile(path):
        return None
    agg = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\s+(\w[\w ]+)\s*:\s+(\d+)/(\d+)\s*\((\d+)%\)", line)
            if m:
                key = m.group(1).strip().lower().replace(" ", "_")
                agg[key] = {"ok": int(m.group(2)), "total": int(m.group(3)), "pct": int(m.group(4))}
    return agg


def diff_golden(s, golden):
    """Compare current scores against a golden baseline."""
    if golden is None:
        return
    print("\nGOLDEN DIFF (vs %s):" % os.path.basename(
        getattr(diff_golden, '_path', 'golden')))
    metrics = [
        ("citation_recall", s["cite_ok"], s["cite_total"]),
        ("term_overlap", s["term_ok"], s["term_total"]),
        ("llm_produced", s["llm_produced"], s["n"]),
        ("no_contamination", s["no_contamination"], s["n"]),
        ("gate_correct", s["gate_correct"], s["n"]),
        ("all_pass", s["all_pass"], s["n"]),
    ]
    for name, ok, total in metrics:
        g = golden.get(name)
        if g is None:
            continue
        delta = ok - g["ok"]
        sign = "+" if delta > 0 else ""
        status = "↑" if delta > 0 else ("↓" if delta < 0 else "=")
        print("  %-20s %s%d (%s%% vs %s%%)" % (name, sign, delta, pct(ok, total), g["pct"]))


# ---------- main --------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=None, help="path to faithfulness_cases.jsonl")
    ap.add_argument("--verbose", action="store_true", help="per-case details")
    ap.add_argument("--golden", default=None,
                    help="path to baseline.eval.faithfulness.out for comparison")
    ap.add_argument("--diff", action="store_true",
                    help="compare current run against the golden")
    args = ap.parse_args()

    cases = load_cases(args.cases)
    if not cases:
        print("no cases to run")
        sys.exit(2)

    # Check if LLM is available
    try:
        from wikikb.online import llm
        llm_active = llm.available()
    except Exception:
        llm_active = False

    if not llm_active:
        print("NOTE: WIKI_LLM is not active — all cases will use extractive fallback.",
              file=sys.stderr)
        print("      Set WIKI_LLM=local and configure llm.config.yaml for LLM synthesis eval.",
              file=sys.stderr)

    rows = []
    for c in cases:
        r = check_case(c, verbose=args.verbose)
        rows.append(r)

    s = score(rows)
    report(rows, s, verbose=args.verbose)

    if args.diff:
        gpath = args.golden or os.path.join(EVAL, "baseline.eval.faithfulness.out")
        golden = load_golden(gpath)
        if golden:
            diff_golden._path = gpath
            diff_golden(s, golden)
        else:
            print("\n(no golden found at %s)" % gpath)

    # Exit 1 if any case failed (CI gate)
    if s["all_pass"] < s["n"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
