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

CHARS_PER_TOKEN = 4                     # air-gap-safe heuristic (matches lint.py); no tiktoken
SNIPPET_CHARS = 260                     # matches kb.snippet() width — a skimmed candidate line
PAGE_DIRS = ("topics", "entities", "questions")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
PAGELINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)\]\]")            # [[page-slug]] (no pipe)
SOURCES_BLOCK_RE = re.compile(r"## Sources\n<!-- crosslink:begin.*?-->(.*?)<!-- crosslink:end -->",
                              re.DOTALL)
SOURCES_NOTE_RE = re.compile(r"\[\[([^\]|#]+)")                     # [[note-slug|Title]] inside it

_recs_cache = {}
_pages_cache = None


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


# ---------- synthesized-page graph (the Phase-2 ceiling, measured read-only) ----------

def load_pages():
    """slug -> {domain, title, summary, body, note_sources:set, page_links:set}."""
    global _pages_cache
    if _pages_cache is not None:
        return _pages_cache
    G = {}
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            text = open(os.path.join(full, fn), encoding="utf-8").read()
            m = FM_RE.match(text)
            fm = {}
            if m:
                for line in m.group(1).splitlines():
                    if line and not line[0].isspace() and ":" in line and not line.startswith(("-", "#")):
                        k, _, v = line.partition(":")
                        fm[k.strip()] = v.strip().strip('"\'')
            sb = SOURCES_BLOCK_RE.search(text)
            note_sources = set(SOURCES_NOTE_RE.findall(sb.group(1))) if sb else set()
            body_wo_sources = SOURCES_BLOCK_RE.sub("", text)
            page_links = set(PAGELINK_RE.findall(body_wo_sources))
            G[fn[:-3]] = {
                "domain": fm.get("domain"), "title": fm.get("title") or fn[:-3],
                "summary": fm.get("summary") or "", "body": body_wo_sources,
                "note_sources": note_sources, "page_links": page_links,
            }
    _pages_cache = G
    return G


def rank_pages(domain, query):
    """Lexical rank of synthesized pages in this domain (reusing kb.score). Returns slugs."""
    terms = kb.toks(query)
    G = load_pages()
    scored = []
    for slug, p in G.items():
        if p["domain"] != domain:
            continue
        pseudo = {"title": p["title"], "abstract": p["summary"], "body_status": "fetched",
                  "primary": False, "family": None, "version": None}
        sc = kb.score(pseudo, terms, p["body"])
        if sc > 0:
            scored.append((sc, slug))
    scored.sort(key=lambda x: -x[0])
    return [slug for _, slug in scored]


def graph_notes(domain, query, k):
    """Reference notes reachable 1-hop from the top-k synthesized pages: their own
    ## Sources notes + their [[linked]] same-domain pages' ## Sources notes."""
    G = load_pages()
    out = set()
    for slug in rank_pages(domain, query)[:k]:
        p = G[slug]
        out |= p["note_sources"]
        for lp in p["page_links"]:
            q = G.get(lp)
            if q and q["domain"] == domain:
                out |= q["note_sources"]
    return out


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


def evaluate(cases, kmax, route, miss_opens):
    rows = []
    for c in cases:
        domain = c.get("domain")
        expected = set(c["expect_any_of"])
        ranked = rank(domain, c["query"])
        ids = [rid for rid, _ in ranked]
        lens = [ln for _, ln in ranked]
        hit = first_hit(ids, expected)                       # 1-based rank or None
        found = hit is not None and hit <= kmax              # found within the window?

        gnotes = graph_notes(domain, c["query"], kmax)
        graph_hit = found or bool(expected & (set(ids[:kmax]) | gnotes))

        # context-token proxy: index + snippets skimmed + full bodies actually opened
        if found:
            scanned = hit                                    # stop skimming at the hit
            opened = [hit - 1]                               # open the one true source
        else:
            scanned = min(kmax, len(ids))
            opened = list(range(min(miss_opens, len(ids))))  # open a few plausible, fail
        idx_t = index_bytes(domain, route) / CHARS_PER_TOKEN
        snip_t = (SNIPPET_CHARS / CHARS_PER_TOKEN) * scanned
        body_t = sum(lens[i] for i in opened) / CHARS_PER_TOKEN
        rows.append({
            "query": c["query"], "domain": domain, "kind": c.get("kind", "?"),
            "pair": c.get("pair"), "variant": c.get("variant"),
            "expected": sorted(expected), "hit_rank": hit, "found": found,
            "graph_hit": graph_hit, "graph_only": graph_hit and not found,
            "scanned": scanned, "opened": len(opened),
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
        h = sum(1 for r in rowset if (r[key] if key == "graph_hit" else (r["hit_rank"] and r["hit_rank"] <= k)))
        return h, len(rowset)

    print("\nRECALL  (lexical vs lexical+graph)")
    for k in ks:
        hl, d = rec(rows, k, "lex")
        hg, _ = rec(rows, k, "graph_hit") if k == kmax else (None, d)
        if k == kmax:
            print("  @%-2d  lexical %2d/%-2d (%3.0f%%)   +graph %2d/%-2d (%3.0f%%)   graph-rescued: %d"
                  % (k, hl, d, pct(hl, d), hg, d, pct(hg, d), hg - hl))
        else:
            print("  @%-2d  lexical %2d/%-2d (%3.0f%%)" % (k, hl, d, pct(hl, d)))

    print("\n  by domain (lexical r@%d / +graph):" % kmax)
    for dom in sorted({r["domain"] for r in rows}):
        sub = [r for r in rows if r["domain"] == dom]
        hl, d = rec(sub, kmax, "lex")
        hg, _ = rec(sub, kmax, "graph_hit")
        print("    %-18s  %d/%d  ->  %d/%d" % (dom, hl, d, hg, d))

    print("\n  by kind (lexical r@%d / +graph):" % kmax)
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
    rows = evaluate(cases, args.kmax, args.route, args.miss_opens)
    report(rows, ks, args.kmax, args.verbose)
    sys.exit(0)


if __name__ == "__main__":
    main()
