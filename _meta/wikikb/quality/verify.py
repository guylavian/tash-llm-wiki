#!/usr/bin/env python3
"""verify.py — answer-time source verification: catch the wrong-cached-number class systematically.

Motivating incident (2026-07-05): a cached question page served "~1 vCPU per 120 client
credentials/s" while its cited source note says 200 — the amortization failure mode (a wrong
number served forever) was caught by luck. This tool catches it by machine:

For every numeric claim on a synthesis page (a number adjacent to a unit/rate token), bind the
claim to lines of the page's cited `kb:` reference notes that share the claim's LOCAL context
tokens (a ±window around the number, not the whole line — one line can carry several rates and
whole-line matching would false-negative the exact incident). Then:

  VERIFIED    — a bound source line contains the claimed number.
  MISMATCH    — bound source lines carry numbers for this context, none of them the claimed one.
                This is the incident class -> ERROR, exit 2 (build fails loudly).
  UNGROUNDED  — no source line binds. WARNING only; a page-level pile of these should already be
                carrying (inferred) tags, which this tool excludes from grading (still counted in
                the census below).

Precision over recall: lines tagged (inferred)/(ambiguous)/(upstream) or carrying an inline
web:/https cite are EXEMPT from grading — they are out of corpus-verification scope per the
schema — but every numeric-claim candidate on the page (exempt or not, scenario page or not, kb:
sourced or not) is counted toward the honest denominator an audit can check (2026-07-05 coverage
audit: the true fraction being machine-graded was invisible before this).

Three extraction fixes on top of the original number+unit adjacency scan:
  - Cross-line wrap: a hard-wrapped sentence ("The default" / "`X` is 30 seconds") splits a
    number from the context word that would have bound it. `_logical_lines` rejoins wrapped
    paragraph/list-item continuation lines (not table rows, not fences) before extraction, so
    the claim keeps its full local context.
  - Table cells: a bare numeric table cell ("| ... | 120 | ...") carries no adjacent unit of its
    own — the column header does. `_cell_claims` extracts these using the row's first cell +
    header as context, on both the page side and the cited source notes' own tables (fed into
    the same `_bind` used for prose, so it is graded "the same way").

Usage:
    python3 -m wikikb verify                      # all domains, all pages with kb: sources
    python3 -m wikikb verify --domain keycloak
    python3 -m wikikb verify --page rhbk-oscp-scaling-resources
    python3 -m wikikb verify --file <path>.md     # a fixture/out-of-tree page (regression tests)
Exit codes: 0 clean · 2 at least one MISMATCH.

Correction workflow (see CLAUDE.md Operation: VERIFY): on MISMATCH, read the quoted source line,
fix the page against the source, bump `updated:`, re-run `python3 -m wikikb build`.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True

from wikikb import paths
from wikikb.build import crosslink

WIKI = str(paths.WIKI)
REF = os.path.join(WIKI, "reference")
PAGE_DIRS = paths.PAGE_DIRS

# number + unit/rate adjacency. Rate forms ("/s", "per second") and count units. A bare number
# with no unit (versions, years, step numbers) is deliberately NOT a claim.
# left word-boundary: a digit fused to letters is an identifier, not a number — without this
# `re.findall` leaks "2" from "Argon2", "256" from "HS256", "4" from "IPv4" into source-line
# number sets, producing false VERIFIED binds (independent-audit finding, 2026-07-06).
NUM = r"(?<![A-Za-z0-9])(\d[\d,]*(?:\.\d+)?)"
UNIT = (r"(vCPU|CPU|MiB|MB|GiB|GB|IOPS|ms|milliseconds?|seconds?|minutes?|%|"
        r"connections?|sessions?|pods?|requests?|entries|iterations?)")
CLAIM_RE = re.compile(r"%s\s*%s\b" % (NUM, UNIT), re.IGNORECASE)
RATE_RE = re.compile(r"%s\s*(?:/s\b|per second)" % NUM, re.IGNORECASE)

# unit-normalization classes: a bound source line must talk about the same KIND of quantity
UNIT_CLASS = {"vcpu": "cpu", "cpu": "cpu", "mib": "mem", "mb": "mem", "gib": "mem", "gb": "mem",
              "iops": "iops", "ms": "time", "millisecond": "time", "milliseconds": "time",
              "second": "time", "seconds": "time", "minute": "time", "minutes": "time",
              "%": "pct", "connection": "count", "connections": "count", "session": "count",
              "sessions": "count", "pod": "count", "pods": "count", "request": "count",
              "requests": "count", "entries": "count", "iteration": "count", "iterations": "count",
              "rate": "rate"}

SKIP_MARKERS = ("(inferred", "(ambiguous", "(upstream", "(scenario premise", "web:", "https://",
                "http://")
STOP = {"the", "a", "an", "for", "each", "per", "second", "seconds", "with", "and", "this",
        "that", "than", "then", "from", "into", "when", "tested", "up", "to", "of", "in",
        "on", "is", "are", "was", "it", "its", "at", "as", "or", "not", "no", "by", "be",
        "use", "using", "used", "also", "see", "e.g", "i.e"}
_WTOK = re.compile(r"[a-z0-9]+")
WINDOW = 5   # tokens each side of the number that form its local context


def _wtoks(s):
    return _WTOK.findall(s.lower())


def _norm_num(s):
    return s.replace(",", "")


def _fm_and_body(text):
    m = crosslink.FM_RE.match(text)
    if not m:
        return {}, text
    return crosslink.top_fields(m.group(1)), text[m.end():]


_NUM_WORD = re.compile(r"^\D*?(\d[\d,]*(?:\.\d+)?)")
_MARKER_DIST = 6   # a number claims the class of the nearest unit/rate marker within this many words
_WIKILINK = re.compile(r"\[\[[^\]]*\]\]")


def _stem(t):
    """Light plural stem for binding only: credentials==credential, grants==grant."""
    return t[:-1] if len(t) > 4 and t.endswith("s") and not t.endswith("ss") else t


def _unit_of(word, prev=""):
    w = word.lower().strip(".,;:()*")
    if w.endswith("/s") or w == "seconds":
        return "rate"
    if w == "second":                     # bare singular is usually the ORDINAL ("the second site")
        return "rate" if prev.lower() == "per" else None
    if w.endswith("%") or w == "%":
        return "pct"
    return UNIT_CLASS.get(w) or UNIT_CLASS.get(w.rstrip("s"))


def _line_exempt(text):
    """SKIP_MARKERS lines are out of grading scope (inferred/ambiguous/upstream/web) — but their
    claims still count toward the FIX-D census, so this is checked separately from extraction."""
    return any(mk in text for mk in SKIP_MARKERS)


def _claims_in_line(line):
    """[(number, unit_class, context_tokens)] for one body line. A number is a claim iff a unit/rate
    marker sits within _MARKER_DIST words (versions, years, step numbers carry no nearby unit). The
    ±WINDOW local context lets a line carrying several rates bind each number to ITS OWN neighbors —
    whole-line context would false-negative the exact 120-vs-200 incident. NOTE: SKIP_MARKERS
    exemption is NOT applied here (see `_line_exempt`) so callers can still count these as
    numeric-claim candidates for the honest-denominator census."""
    low = line.strip()
    if not low or low.startswith(("#", "<!--")):
        return []
    if "kb:" in low:
        return []                      # citation lines — ids carry numbers, not claims
    if low.startswith(("-", "*")) and "[[" in low and "]]" in low:
        # a bullet that IS a link ("- [[slug|Chapter 8. Title]]", crosslink's generated
        # ## Sources list) carries no claim — its digits are chapter numbers, not facts. But
        # FIX C can join a wrapped bullet whose SENTENCE merely references a [[page]] mid-text
        # and states a real claim afterward — only skip if nothing but the link (+ punctuation)
        # remains once the wikilink markup itself is removed.
        if not _WIKILINK.sub("", low).lstrip("-* ").strip():
            return []
    words = low.split()
    unit_pos = [(i, u) for i, w in enumerate(words)
                if (u := _unit_of(w, words[i - 1] if i else ""))]
    out = []
    for i, w in enumerate(words):
        if i == 0 and re.match(r"^\d+[.)]$", w):
            continue                     # list ordinal ("2." / "3)") — not a claim
        if re.search(r"\d[-–]\d", w) or re.match(r"^[A-Za-z_`\[(≥≤<>]", w):
            continue                     # ranges (4-22, 10–15), ids/code (v1, `le=`), comparatives
        # compound "5-minute"/"30d"-style: unit fused to the number
        comp = re.match(r"^(\d[\d,]*(?:\.\d+)?)-([a-z]+)", w.lower())
        m = _NUM_WORD.match(w)
        if not m or not any(ch.isdigit() for ch in w):
            continue
        num = _norm_num(m.group(1))
        if num in ("0", "1"):
            continue                     # 0/1 are structure ("USN 0", "1 of") far more often than facts
        if comp and UNIT_CLASS.get(comp.group(2).rstrip("s")):
            uclass = UNIT_CLASS[comp.group(2).rstrip("s")]
        else:
            if "." in num:               # dotted numbers are versions unless a unit follows directly
                nxt = words[i + 1] if i + 1 < len(words) else ""
                if not _unit_of(nxt, w):
                    continue
            near = [(j - i, u) for j, u in unit_pos if abs(j - i) <= _MARKER_DIST]
            if not near:
                continue
            # closest wins; on a DISTANCE TIE prefer the marker AFTER the number ("100
            # requests/s") over one before it ("vCPU per 100") — a join (FIX C) can put a number
            # exactly between two equidistant markers, and English "A units per B other-units/s"
            # binds the second number to what follows it, not what preceded the ratio.
            near.sort(key=lambda t: (abs(t[0]), t[0] <= 0))
            uclass = near[0][1]
        # 4xx/5xx status codes are enumerable and never worth an accusation — BUT only treat a
        # 400-599 number as http when an http-signal word is actually nearby; otherwise a real
        # rate like "410 req/s" was getting the context-free http path and rubber-stamped VERIFIED
        # against any unrelated "410" in the corpus (independent-audit finding, 2026-07-06).
        if uclass != "pct" and re.match(r"^[45]\d\d$", num):
            _win = " ".join(words[max(0, i - WINDOW):i + WINDOW + 1]).lower()
            if re.search(r"\b(http|https|status|response|code|error|4xx|5xx|rest|endpoint|returns?)\b", _win):
                uclass = "http"
        lo, hi = max(0, i - WINDOW), min(len(words), i + WINDOW + 1)
        ctx = {_stem(t) for t in _wtoks(" ".join(words[lo:hi]))
               if t not in STOP and not t.isdigit() and len(t) >= 3}
        out.append((_norm_num(m.group(1)), uclass, ctx))
    return out


_HEADING_LIKE = re.compile(r"^(chapter\s+\d|\d+(\.\d+)*\.?\s)", re.IGNORECASE)

# ---- markdown tables (FIX B): a bare numeric cell has no unit of its own — the column header
# supplies it, and the row's first cell (usually a label) supplies the rest of the context. ----
_TABLE_ROW = re.compile(r"^\s*\|")
_SEP_CELL = re.compile(r"^:?-{1,}:?$")
_CELL_NUM = re.compile(r"^(\d[\d,]*(?:\.\d+)?)\s*([A-Za-z%/]*)$")


def _split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _find_tables(body):
    """[(header_cells, [(row_cells, lineno), ...]), ...] for markdown tables outside fences.
    lineno is 1-based, matching the page's own line numbers."""
    lines = body.splitlines()
    n = len(lines)
    fence = False
    tables = []
    i = 0
    while i < n:
        s = lines[i].strip()
        if s.startswith("```"):
            fence = not fence
            i += 1
            continue
        if fence:
            i += 1
            continue
        if _TABLE_ROW.match(lines[i]) and i + 1 < n and _TABLE_ROW.match(lines[i + 1]):
            hdr = _split_row(lines[i])
            sep = _split_row(lines[i + 1])
            if sep and len(sep) == len(hdr) and all(_SEP_CELL.match(c) for c in sep):
                rows = []
                j = i + 2
                while j < n and _TABLE_ROW.match(lines[j]):
                    rows.append((_split_row(lines[j]), j + 1))
                    j += 1
                tables.append((hdr, rows))
                i = j
                continue
        i += 1
    return tables


def _clean_cell(c):
    return c.strip().strip("`*_").strip()


def _header_uclass(header_cell):
    words = header_cell.split()
    for i, w in enumerate(words):
        u = _unit_of(w, words[i - 1] if i else "")
        if u:
            return u
    return None


def _cell_claims(hdr, cells):
    """[(number, unit_class, context_tokens)] for one table data row. Context = the column
    header + the row's first cell (the usual row label); unit class prefers an inline suffix
    fused to the cell ("1000 ms") and falls back to the header ("Default iterations")."""
    if not hdr or not cells:
        return []
    label = _clean_cell(cells[0])
    out = []
    for c in range(min(len(cells), len(hdr))):
        m = _CELL_NUM.match(_clean_cell(cells[c]))
        if not m:
            continue
        num = _norm_num(m.group(1))
        if num in ("0", "1"):
            continue
        suffix = m.group(2)
        uclass = (_unit_of(suffix) if suffix else None) or _header_uclass(hdr[c])
        if not uclass:
            continue
        ctx = {_stem(t) for t in _wtoks(hdr[c] + " " + label)
               if t not in STOP and not t.isdigit() and len(t) >= 3}
        out.append((num, uclass, ctx))
    return out


def _source_lines(note_paths):
    """([(line_text, token_set, number_set, unit_classes)], df) across all cited notes (bodies only).
    Section-heading-like lines ('Chapter 6…', '2.1.2 Vertical…') are excluded — their numbers are
    structure, not facts, and they were the top false-positive source in the precision audit.
    df counts token document-frequency over ALL body lines (not just numeric ones) — rarity judged
    against the numeric subset made common words like 'replication' look distinctive (audit FP).
    Also folds in bare table cells (FIX B) as synthetic entries so a page's table claims can bind
    against the cited note's own tables the same way prose claims bind against prose lines."""
    lines, df = [], Counter()
    for p in note_paths:
        try:
            _, body = _fm_and_body(open(p, encoding="utf-8").read())
        except OSError:
            continue
        fence = False
        for ln in body.splitlines():
            ln = ln.strip()
            if ln.startswith("```"):
                fence = not fence
                continue
            if fence or not ln or ln.startswith("#") or _HEADING_LIKE.match(ln):
                continue               # fenced code (YAML/CLI blobs) is noise for prose binding
            toks = {_stem(t) for t in _wtoks(ln) if t not in STOP and len(t) >= 3}
            df.update(toks)
            nums = {_norm_num(n) for n in re.findall(NUM, ln)}
            if not nums:
                continue
            ws = ln.split()
            uclasses = {u for k, w in enumerate(ws) if (u := _unit_of(w, ws[k - 1] if k else ""))}
            lines.append((ln, toks, nums, uclasses))
        for hdr, rows in _find_tables(body):
            for cells, _lineno in rows:
                for num, uclass, ctx in _cell_claims(hdr, cells):
                    df.update(ctx)
                    label = " | ".join(c for c in cells if c) or "(table row)"
                    lines.append((label, ctx, {num}, {uclass}))
    return lines, df


def _bind(claim_ctx, uclass, src_lines, df):
    """ASYMMETRIC binding — confirmations are lenient, accusations are strict.
    Returns (lenient, strict): `lenient` = class-matching lines sharing >=2 context tokens (used to
    grant VERIFIED — a true number must not lose to a rarity bar; 'refresh'/'token' are frequent in
    a sizing note). `strict` = the lenient subset that also shares a distinctive token (df<=3),
    rarity-ranked (used to assert MISMATCH — an accusation needs distinctive evidence)."""
    lenient, scored = [], []
    for ln, toks, nums, uclasses in src_lines:
        if uclass not in uclasses:
            continue
        shared = claim_ctx & toks
        if len(shared) < 2:
            continue
        lenient.append((ln, nums))
        if any(df.get(t, 99) <= 3 for t in shared):
            scored.append((sum(1.0 / max(df.get(t, 1), 1) for t in shared), ln, nums))
    scored.sort(reverse=True)
    return lenient, [(ln, nums) for _, ln, nums in scored]


# ---- paragraph/list-item joining (FIX C): a markdown hard-wrap splits a number from the word
# that would bind it ("The default" / "`X` is 30 seconds"). Table rows and fences are untouched —
# each stays its own single-line unit (tables get their own extraction above; fences are dropped).
_MD_LIST = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def _logical_lines(body):
    """[(text, start_line, end_line)] — physical lines merged at the paragraph/list-item level.
    A logical line's `text` is the joined, single-spaced prose; start/end are the original 1-based
    line numbers it came from (for reporting)."""
    lines = body.splitlines()
    out = []
    fence = False
    buf = buf_start = buf_end = None

    def flush():
        nonlocal buf, buf_start, buf_end
        if buf is not None:
            out.append((buf, buf_start, buf_end))
        buf = buf_start = buf_end = None

    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            flush()
            fence = not fence
            continue
        if fence:
            continue
        if not s:
            flush()
            continue
        if s.startswith("|") or s.startswith("#"):
            flush()
            out.append((line, i, i))          # table row / heading: standalone, own extraction
            continue
        if _MD_LIST.match(line) or buf is None:
            flush()
            buf, buf_start, buf_end = s, i, i
        else:
            buf = buf + " " + s               # continuation of the same paragraph/list item
            buf_end = i
    flush()
    return out


def verify_page(path, ref_idx):
    """-> (findings, total_candidates) for one synthesis page. `findings` is the graded subset
    (VERIFIED/MISMATCH/UNGROUNDED); `total_candidates` is every numeric-claim candidate on the
    page including ones excluded from grading (scenario pages, exempt lines, no-kb: pages) —
    the honest denominator (FIX D)."""
    raw = open(path, encoding="utf-8").read()
    fm, body = _fm_and_body(raw)
    scenario = fm.get("question_tier") == "scenarios"
    domain = fm.get("domain") or ""
    notes = []
    if not scenario:
        m = crosslink.FM_RE.match(raw)
        tokens = [t for t in crosslink.source_tokens(m.group(1)) if t.startswith("kb:")] if m else []
        for t in tokens:
            r = crosslink.resolve(t, domain, ref_idx)
            if r:
                notes.append(os.path.join(REF, domain, r["slug"] + ".md"))
    graded = bool(notes)   # scenario pages never resolve notes above, so this covers both gates
    src, df = _source_lines(notes) if notes else ([], Counter())

    table_by_row = {}
    for hdr, rows in _find_tables(body):
        for cells, lineno in rows:
            cl = _cell_claims(hdr, cells)
            if cl:
                table_by_row[lineno] = cl

    findings = []
    total = 0
    for text, start, end in _logical_lines(body):
        exempt = _line_exempt(text)
        claims = list(_claims_in_line(text))
        have = {c[0] for c in claims}
        if start == end and start in table_by_row:
            for c in table_by_row[start]:
                if c[0] not in have:          # don't double-count a cell the prose scan already found
                    claims.append(c)
                    have.add(c[0])
        for num, uclass, ctx in claims:
            total += 1
            if not graded or exempt:
                continue
            if uclass == "http":             # status codes: verify by presence anywhere, never accuse
                anywhere = next((ln for ln, _, nums, _ in src if num in nums), None)
                findings.append({"status": "VERIFIED" if anywhere else "UNGROUNDED", "number": num,
                                 "claim": text.strip()[:160],
                                 "source_line": anywhere[:160] if anywhere else None})
                continue
            lenient, strict = _bind(ctx, uclass, src, df)
            hit = next((ln for ln, nums in lenient if num in nums), None)
            if hit is not None:
                findings.append({"status": "VERIFIED", "number": num,
                                 "claim": text.strip()[:160], "source_line": hit[:160]})
            elif strict:
                findings.append({"status": "MISMATCH", "number": num,
                                 "claim": text.strip()[:160],
                                 "source_line": strict[0][0][:200],
                                 "source_numbers": sorted(strict[0][1])})
            else:
                findings.append({"status": "UNGROUNDED", "number": num,
                                 "claim": text.strip()[:160], "source_line": None})
    return findings, total


def iter_pages(domain=None, slug=None):
    for d in PAGE_DIRS:
        dd = os.path.join(WIKI, d)
        if not os.path.isdir(dd):
            continue
        for fn in sorted(os.listdir(dd)):
            if not fn.endswith(".md"):
                continue
            if slug and fn[:-3] != slug:
                continue
            p = os.path.join(dd, fn)
            if domain:
                fm, _ = _fm_and_body(open(p, encoding="utf-8").read())
                if fm.get("domain") != domain:
                    continue
            yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain")
    ap.add_argument("--page", help="verify a single page by slug")
    ap.add_argument("--file", help="verify an out-of-tree page file (fixtures/regression)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    ref_idx = crosslink.build_ref_index()
    results, mismatches, verified, ungrounded, total_candidates = {}, 0, 0, 0, 0
    files = [args.file] if args.file else list(iter_pages(args.domain, args.page))
    for p in files:
        f, total = verify_page(p, ref_idx)
        total_candidates += total
        if f:
            results[os.path.relpath(p, WIKI) if not args.file else p] = f
            mismatches += sum(1 for x in f if x["status"] == "MISMATCH")
            verified += sum(1 for x in f if x["status"] == "VERIFIED")
            ungrounded += sum(1 for x in f if x["status"] == "UNGROUNDED")

    eligible = verified + mismatches + ungrounded
    pct = round(100.0 * verified / total_candidates) if total_candidates else 0

    if args.json:
        print(json.dumps({"pages": results, "verified": verified, "mismatch": mismatches,
                          "ungrounded": ungrounded, "eligible": eligible,
                          "total_candidates": total_candidates, "pct_verified": pct}, indent=1))
    else:
        for page, f in sorted(results.items(),
                              key=lambda kv: -sum(x["status"] == "MISMATCH" for x in kv[1])):
            bad = [x for x in f if x["status"] == "MISMATCH"]
            if not bad:
                continue
            print("MISMATCH %s" % page)
            for x in bad:
                print("  claim : %s  (number %s)" % (x["claim"], x["number"]))
                print("  source: %s  (has: %s)" % (x["source_line"], ", ".join(x["source_numbers"])))
        print("verify — %d verified / %d eligible / %d total numeric-claim candidates "
              "(%d%% of all claims machine-verified) · %d MISMATCH · %d ungrounded"
              % (verified, eligible, total_candidates, pct, mismatches, ungrounded))
    sys.exit(2 if mismatches else 0)


if __name__ == "__main__":
    main()
