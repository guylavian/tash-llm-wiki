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

Exit taxonomy (consensus 2026-07-12 — a partial or malformed cohort must never read as a pass):
  0 — COMPLETE cohort, all hard gates (refusal/banner) pass
  1 — COMPLETE cohort, at least one hard gate failed
  2 — INCOMPLETE or MALFORMED cohort: any case id missing from the answers file, any answer
      that is empty or a run300 `[RUN-ERROR]` sentinel (an error string is not an answer),
      any duplicate answer id, or any answer id not in the case bank. Takes precedence over 1:
      hard-gate results over a partial cohort are not interpretable as acceptance.
The scoreboard always prints in full before exiting, so partial runs remain inspectable —
the exit code alone carries the acceptance semantics.
`# ponytail: string heuristics — swap the gold-fact check for an LLM judge only on flagged
cases if precision matters.`
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
        r"(not|n't|no)\s+(exist|found|present|document|appear|defined|valid|real|"
        r"available|expos(?:e|ed)|referenc(?:e|ed)|support(?:ed)?)|"
        r"not\s+a\s+real\b|no such|no\s+\w+\s+(named|called)|is\s+(actually|fabricated|hallucinated)|"
        r"you (likely|probably) mean|did you mean|\bnote:|instead of|rather than|"
        r"correct (name|form|spelling|option)|"
        r"zero hits|not in the (corpus|kb|knowledge|wiki|docs)|couldn.t find", low)
    # defining the fake token as real = fail even if hedged
    defined = re.search(re.escape(token.lower()) + r"\s+(is the|controls|sets|configures|specifies|enables)\b", low)
    return bool(saidno) and not defined


def bannered(answer):
    return bool(re.search(r"⚠|out of (corpus )?coverage|tier is not ingested", answer, re.I))


def _ident_pat(token):
    """Boundary-aware pattern for an identifier/flag/phrase with ASYMMETRIC dot handling:
    LEFT boundary rejects any identifier char INCLUDING a dot (status.spec.foo never matches a
    real token spec.foo); RIGHT boundary rejects an identifier char or a dot that CONTINUES a
    dotted path (spec.foo.extra), while a bare sentence-ending period (spec.foo.) stays a
    boundary. So --proxy-header never matches inside --proxy-headers (fake-prefix-of-real) and
    --dest-dir is never credited by --dest-directory (real-prefix-of-longer)."""
    return re.compile(r"(?<![A-Za-z0-9_.-])%s(?!\.?[A-Za-z0-9_-])" % re.escape(token.lower()))


def corrected(answer, real, fake):
    """REPORT-ONLY (WI-8, ledger D8): did the answer correct a rationalized-substitution premise —
    signal the fake identifier is not real (same detector as refused()) AND name the real one?
    Boundary-aware both ways: WHOLE fake occurrences are blanked first (so a fake echo never
    credits a real token embedded in it — userAccountControl ⊂ userAccountControlFlags — while a
    real token that merely EXTENDS the fake — --proxy-header s— survives the blanking), and the
    real token must then match on identifier boundaries (no --dest-directory credit for
    --dest-dir). This metric may never feed hard_fail / the exit code — the bank is frozen and
    report-only by decision."""
    # strip markdown emphasis WITHOUT eating identifier underscores (refused() may strip _ because
    # it re-applies the token against the same stripped text; here the tokens keep their _)
    low = re.sub(r"[*`]", "", (answer or "").lower())
    named = bool(_ident_pat(real).search(_ident_pat(fake).sub(" ", low)))
    return refused(answer, fake) and named


def contract(answer):
    heading = re.search(r"^#+\s*references[^\n]*\n(?P<body>.*)", answer, re.I | re.M | re.S)
    if not heading:
        return False
    body = heading.group("body")
    rh = re.search(r"^#+\s*rh ground-truth\s*$\n(?P<body>.*?)(?=^#+\s|\Z)",
                   body, re.I | re.M | re.S)
    wiki = re.search(r"^#+\s*wiki\s*$\n(?P<body>.*?)(?=^#+\s|\Z)",
                     body, re.I | re.M | re.S)
    if not (rh and wiki):
        return False
    rh_ok = re.search(r"\b(kb:|guide:|ref:)", rh.group("body"), re.I) or re.search(
        r"no verified .*source", rh.group("body"), re.I)
    wiki_ok = "[[" in wiki.group("body") or re.search(r"no .*wiki page", wiki.group("body"), re.I)
    return bool(rh_ok and wiki_ok)


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


def premise_corrected(answer, premise_tokens):
    """REPORT-ONLY (premise-trap class, bank v3): does the answer's Premise-check table contain a
    row naming one of the planted false-premise tokens AND carrying the CORRECTED verdict? String
    match on table lines only — same report-only discipline as corrected(); never feeds hard_fail
    or the exit code. Promotion to a hard gate is a separate decision after the FP rate is known."""
    for line in (answer or "").splitlines():
        if line.strip().startswith("|") and "CORRECTED" in line.upper():
            if any(t.lower() in line.lower() for t in premise_tokens):
                return True
    return False


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
                if c.get("_meta"):        # bank header record (authorship label etc.), not a case
                    continue
                cases[c["id"]] = c
    answers, malformed = {}, []
    with open(args.answers, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                a = json.loads(line)
            except json.JSONDecodeError:
                malformed.append("line %d: invalid JSON" % ln)
                continue
            if not isinstance(a, dict) or not isinstance(a.get("id"), str):
                malformed.append("line %d: not an answer row (need object with string id)" % ln)
                continue
            if a["id"] in answers:
                malformed.append("duplicate id: %s" % a["id"])
            answers[a["id"]] = a
    for u in sorted(set(answers) - set(cases)):
        malformed.append("unknown id (not in case bank): %s" % u)

    # COHORT IDENTITY (WI-3): rows are stamped {run_id, model} by run300. A file mixing runs is
    # not one cohort and must never grade as one. All-unstamped = one LEGACY cohort (warn only).
    run_ids = set()
    for a in answers.values():
        rid = a.get("run_id")
        if rid is None:
            run_ids.add(None)
        elif not isinstance(rid, str) or not rid.strip():
            malformed.append("invalid run_id (non-string/empty) on %s" % a.get("id"))
        else:
            run_ids.add(rid)
    legacy_cohort = bool(answers) and run_ids == {None}
    stamped = sorted(r for r in run_ids if r is not None)
    if len(stamped) > 1:
        malformed.append("mixed cohorts: %d distinct run_ids (%s)" % (len(stamped), ", ".join(stamped[:3])))
    elif stamped and None in run_ids:
        malformed.append("mixed cohorts: stamped and unstamped (legacy) rows in one file")

    rows, agg = [], defaultdict(lambda: defaultdict(int))
    hard_fail = 0
    missing, errored = [], []
    for cid, c in sorted(cases.items()):
        a = answers.get(cid)
        if a is None:
            missing.append(cid)
        else:
            ans_text = a.get("answer")
            if (not isinstance(ans_text, str) or not ans_text.strip()
                    or ans_text.lstrip().startswith("[RUN-ERROR]")):
                errored.append(cid)   # a null/empty/error string is NOT an answer — ungraded, incomplete
                a = None
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
            if c.get("must_correct") and c.get("substituted_token"):
                # WI-8: REPORT-ONLY — never contributes to hard_fail/exit
                row["corrected"] = corrected(ans, c.get("real_token", ""),
                                             c.get("substituted_token", ""))
            if c.get("must_correct") and c.get("premise_tokens"):
                # premise-trap class (bank v3): REPORT-ONLY — CORRECTED table row names the premise
                row["premise_corrected"] = premise_corrected(ans, c["premise_tokens"])
            # C-5 (2026-07-12, post-results metric correction — always dual-report
            # against the raw-v1 grader): a must_refuse case passes ONLY by refusing;
            # gold overlap stays reported but is never pass-determinative for that
            # class (token overlap with gold facts that NAME the fake token was
            # awarding passes to fabrications — fab-013/026).
            row["passed"] = bool(row["refusal"]) if c.get("must_refuse") else row["gold"] >= 0.5
            row["judge_flag"] = row["gold"] < 0.5  # send these to a human/LLM judge
        rows.append(row)
        t = agg[c["type"]]
        t["n"] += 1
        if a:
            t["answered"] += 1
            t["passed"] = t.get("passed", 0) + row["passed"]
            t["retrieval"] += row["retrieval"]
            t["contract"] += row["contract"]
            t["gold_sum"] += row["gold"]
            if "refusal" in row:
                t["refused"] += row["refusal"]
            if "banner" in row:
                t["bannered"] += row["banner"]
            if "corrected" in row:
                t["corrected"] += row["corrected"]
            if "premise_corrected" in row:
                t["premise_corrected"] += row["premise_corrected"]

    # cache-repeat consistency: both members must land the same gold facts
    for cid, c in cases.items():
        if c["type"] == "cache-repeat" and c.get("repeat_of") in answers and cid in answers:
            _a1 = answers[c["repeat_of"]].get("answer")
            _a2 = answers[cid].get("answer")
            if not (isinstance(_a1, str) and isinstance(_a2, str)):
                continue                       # null/malformed answers already drive exit 2 above
            g1 = gold_ratio(_a1, c.get("gold_facts", []))
            g2 = gold_ratio(_a2, c.get("gold_facts", []))
            if abs(g1 - g2) > 0.34:
                print(f"  DRIFT {cid}: repeat answer disagrees with original (gold {g1:.2f} vs {g2:.2f})")

    print(f"GRADE300 — {len(cases)} cases, {len(answers)} answered")
    for t in sorted(agg):
        s = agg[t]
        n, ans = s["n"], s["answered"]
        line = f"  {t:<16} {ans}/{n} answered  retrieval {s['retrieval']}/{ans}  contract {s['contract']}/{ans}"
        if ans:
            line += f"  gold {s['gold_sum']/ans:.2f}  PASS {s.get('passed', 0)}/{ans}"
        if "refused" in s:
            line += f"  REFUSED {s['refused']}/{ans}"
        if "bannered" in s:
            line += f"  BANNER {s['bannered']}/{ans}"
        if "corrected" in s:
            line += f"  CORRECTED {s['corrected']}/{ans} (report-only)"
        if "premise_corrected" in s:
            line += f"  P-CORRECTED {s['premise_corrected']}/{ans} (report-only)"
        print(line)
    flagged = [r["id"] for r in rows if r.get("judge_flag")]
    print(f"  judge-flagged (gold<0.5, needs human/LLM verify): {len(flagged)}")

    # COMPLETENESS + MALFORMEDNESS (exit 2) — a cohort with holes is never an acceptance result.
    def _preview(ids):
        return ", ".join(ids[:6]) + ("…" if len(ids) > 6 else "")
    if legacy_cohort:
        print("  note: legacy cohort (no run_id stamps) — treated as one cohort; new runs are stamped")
    if malformed:
        print(f"  MALFORMED ({len(malformed)}): {_preview(malformed)}")
    if missing or errored:
        print(f"  INCOMPLETE — {len(missing)} case(s) missing from answers file, "
              f"{len(errored)} error/empty answer(s)"
              + (f"  missing: {_preview(missing)}" if missing else "")
              + (f"  errored: {_preview(errored)}" if errored else ""))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1)
        print(f"  full report -> {args.json}")
    # exit taxonomy (see module docstring): incomplete/malformed (2) > hard-gate fail (1) > clean (0)
    sys.exit(2 if (malformed or missing or errored) else (1 if hard_fail else 0))


if __name__ == "__main__":
    main()
