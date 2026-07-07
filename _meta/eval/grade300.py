#!/usr/bin/env python3
"""grade300.py — mechanical grader for the 300-case end-to-end eval set (cases300.jsonl).

Usage:
    python3 grade300.py --cases cases300.jsonl --answers answers.jsonl [--json report.json]

answers.jsonl: one {"id": "<case id>", "answer": "<full answer text>"} per line, produced by
whatever harness ran the questions (any agent/model). Optional keys: "filed_page" (path of the
questions/ page the run created), "elapsed_s".

Scoring is deliberately mechanical (stdlib, no LLM):
  retrieval  — an expected slug appears in the answer (as [[slug]] or bare)
  refusal    — fabrication traps: answer says not-found and does NOT define the fake token as real
  banner     — out-of-coverage: the H1 banner text is present
  contract   — a References section citing both tiers (kb:/guide:/ref: AND [[wiki]] links)
  gold       — fraction of gold_facts whose distinctive tokens appear (loose; low scores are
               flagged for a human/LLM judge pass, not auto-failed)
Cache-repeat pairs additionally require the two answers to agree on gold facts.

Exit 1 if any hard gate fails (refusal/banner), else 0. `# ponytail: string heuristics — swap
the gold-fact check for an LLM judge only on flagged cases if precision matters.`
"""
import argparse, json, re, sys
from collections import defaultdict

STOP = set("""a an the of in on for to and or is are was were be been it its this that with as by
from at into over under about when what which how why do does did not no yes you your must can
than more most less least same other another one two only also just very each every both any all
some new old set sets setting get gets got use uses used using make makes made making need needs
needed want wants way ways thing things read reads write writes has have had having will would
should could may might shall between among within without across during after before while
""".split())


NARRATION = re.compile(
    r"^.*\b(file (this|the|it) (answer )?back|filing (this|the) answer|filed (as|at|into)|"
    r"let me file|i'll file|now i'll|lint is clean|running lint|wiki now compounds)\b.*$",
    re.I | re.M)
EVAL_INTENT = re.compile(r"[^.!?\n]*\b(the question|this) (expects|is testing|wants) (the model|me) to\b[^.!?\n]*[.!?]?", re.I)


def clean(answer):
    """Strip agent scratchpad narration (whole line) and eval-intent echoes (sentence only)."""
    return EVAL_INTENT.sub("", NARRATION.sub("", answer))


def toks(s):
    return [t for t in re.findall(r"[a-z0-9_.:-]{3,}", s.lower()) if t not in STOP]


def has_slug(answer, slugs):
    low = answer.lower()
    return any(s.lower() in low for s in slugs)


def refused(answer, token):
    low = re.sub(r"[*_`]", "", answer.lower())  # markdown emphasis breaks word boundaries
    saidno = re.search(
        r"(not|n't|no)\s+(exist|found|present|document|appear|defined|valid|real)|"
        r"not\s+a\s+real\b|no such|no\s+\w+\s+(named|called)|is\s+(actually|fabricated|hallucinated)|"
        r"you (likely|probably) mean|did you mean|\bnote:|instead of|rather than|"
        r"correct (name|form|spelling|option)|"
        r"zero hits|not in the (corpus|kb|knowledge|wiki|docs)|couldn.t find", low)
    # defining the fake token as real = fail even if hedged
    defined = re.search(re.escape(token.lower()) + r"\s+(is the|controls|sets|configures|specifies|enables)\b", low)
    return bool(saidno) and not defined


def bannered(answer):
    return bool(re.search(r"⚠|out of (corpus )?coverage|tier is not ingested", answer, re.I))


def contract(answer):
    has_ref_heading = re.search(r"^#+\s*references|^\*\*references\*\*|^references\b", answer, re.I | re.M)
    rh = re.search(r"\b(kb:|guide:|ref:)", answer)
    wiki = "[[" in answer
    return bool(has_ref_heading and rh and wiki)


def gold_ratio(answer, facts):
    if not facts:
        return 1.0
    low = answer.lower()
    hit = 0
    for f in facts:
        ft = toks(f)
        if not ft:
            hit += 1
            continue
        found = sum(1 for t in ft if t in low or t.rstrip("s") in low)
        if found / len(ft) >= 0.5:
            hit += 1
    return hit / len(facts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True)
    ap.add_argument("--answers", required=True)
    ap.add_argument("--json", help="write full per-case report here")
    args = ap.parse_args()

    cases = {}
    with open(args.cases, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                c = json.loads(line)
                cases[c["id"]] = c
    answers = {}
    with open(args.answers, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                a = json.loads(line)
                answers[a["id"]] = a

    rows, agg = [], defaultdict(lambda: defaultdict(int))
    hard_fail = 0
    for cid, c in sorted(cases.items()):
        a = answers.get(cid)
        row = {"id": cid, "type": c["type"], "domain": c["domain"], "answered": bool(a)}
        if a:
            ans = clean(a.get("answer", ""))
            row["retrieval"] = has_slug(ans, c.get("expected_slugs", []))
            row["gold"] = round(gold_ratio(ans, c.get("gold_facts", [])), 2)
            row["contract"] = contract(ans)
            if c.get("must_refuse"):
                row["refusal"] = refused(ans, c.get("fabricated_token", ""))
                hard_fail += 0 if row["refusal"] else 1
            if c.get("must_banner"):
                row["banner"] = bannered(ans)
                hard_fail += 0 if row["banner"] else 1
            row["judge_flag"] = row["gold"] < 0.5  # send these to a human/LLM judge
        rows.append(row)
        t = agg[c["type"]]
        t["n"] += 1
        if a:
            t["answered"] += 1
            t["retrieval"] += row["retrieval"]
            t["contract"] += row["contract"]
            t["gold_sum"] += row["gold"]
            if "refusal" in row:
                t["refused"] += row["refusal"]
            if "banner" in row:
                t["bannered"] += row["banner"]

    # cache-repeat consistency: both members must land the same gold facts
    for cid, c in cases.items():
        if c["type"] == "cache-repeat" and c.get("repeat_of") in answers and cid in answers:
            g1 = gold_ratio(answers[c["repeat_of"]]["answer"], c.get("gold_facts", []))
            g2 = gold_ratio(answers[cid]["answer"], c.get("gold_facts", []))
            if abs(g1 - g2) > 0.34:
                print(f"  DRIFT {cid}: repeat answer disagrees with original (gold {g1:.2f} vs {g2:.2f})")

    print(f"GRADE300 — {len(cases)} cases, {len(answers)} answered")
    for t in sorted(agg):
        s = agg[t]
        n, ans = s["n"], s["answered"]
        line = f"  {t:<16} {ans}/{n} answered  retrieval {s['retrieval']}/{ans}  contract {s['contract']}/{ans}"
        if ans:
            line += f"  gold {s['gold_sum']/ans:.2f}"
        if "refused" in s:
            line += f"  REFUSED {s['refused']}/{ans}"
        if "bannered" in s:
            line += f"  BANNER {s['bannered']}/{ans}"
        print(line)
    flagged = [r["id"] for r in rows if r.get("judge_flag")]
    print(f"  judge-flagged (gold<0.5, needs human/LLM verify): {len(flagged)}")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1)
        print(f"  full report -> {args.json}")
    sys.exit(1 if hard_fail else 0)


if __name__ == "__main__":
    main()
