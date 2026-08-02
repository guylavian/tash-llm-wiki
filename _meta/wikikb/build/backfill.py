#!/usr/bin/env python3
"""One-time, deterministic, idempotent backfill for pre-framework wiki pages.

Two modes (first positional arg; `frontmatter` is the default, for back-compat):

frontmatter (default) adds only what can be derived honestly, without inventing facts:
  - summary:  lifted verbatim from the page's own bold one-line definition
              (the `**...**` line). lint.py flags these as "auto-seeded" so a
              human can later replace them with a real summary.
  - provenance: needs-review   — a HONEST placeholder. Per-claim provenance can
              only be assigned by reading each claim against its source, so we do
              NOT manufacture extracted/inferred counts here. Real provenance goes
              forward at INGEST write-time and on hand-authored pages.

  - domain:   stamped from --domain (default keycloak) on any page missing it,
              inserted right after type: per the frontmatter spec. Pages already
              carrying domain: are left untouched.

Tags are intentionally NOT backfilled — they belong to Pass 2 (taxonomy).

question-tier stamps `question_tier:` on questions/*.md pages that don't yet carry
one (right after `type:`), via a deterministic regex heuristic over title/body/
frontmatter — see classify_tier(). When the assigned tier falls outside the page's
domain's `tiers-covered:` (_meta/taxonomy.md, read the same way lint.py does — via
wikikb.quality.coverage.load_tiers_covered(), never re-parsed here) and the body
carries no H1 out-of-coverage banner yet (wikikb.quality.lint.has_out_of_coverage_banner),
also inserts the reader-facing banner line right after the first `# ` heading, in the
exact format lint's banner detector and CLAUDE.md's H1 template both expect.

Pages that already have a summary:/provenance:/domain:/question_tier: are left
untouched (idempotent). Only edits files under wiki/{topics,entities,questions}/ —
never corpora/ or references/.

Usage:
    python3 -m wikikb backfill                          # dry-run: list what would change
    python3 -m wikikb backfill --apply                   # write the changes
    python3 -m wikikb backfill question-tier              # dry-run: planned tier distribution
    python3 -m wikikb backfill question-tier --apply      # write question_tier: + banners
"""
import argparse
import os
import re

from wikikb import paths
from wikikb.quality import coverage as covmod
from wikikb.quality.lint import has_out_of_coverage_banner, unquote
WIKI = str(paths.WIKI)
PAGE_DIRS = paths.PAGE_DIRS
FM_RE = re.compile(r"^(---\n)(.*?)(\n---)", re.DOTALL)


def page_files():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield os.path.join(full, fn)


def bold_definition(body):
    """The page's leading bold one-line definition (`**...**`), even if it wraps
    across lines. Whitespace is collapsed; a trailing period is dropped so the
    value is stable for the lint auto-seeded comparison."""
    b = re.sub(r"^\s*#.*\n", "", body.lstrip(), count=1).lstrip()
    if not b.startswith("**"):
        return None
    m = re.match(r"\*\*(.+?)\*\*", b, re.DOTALL)
    if not m:
        return None
    return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")


def yaml_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def backfill(text, domain="keycloak"):
    """Return (new_text, actions) or (text, []) if nothing to do."""
    m = FM_RE.match(text)
    if not m:
        return text, []
    block = m.group(2)
    lines = block.splitlines()
    has_summary = any(re.match(r"^summary:\s*\S", ln) for ln in lines)
    has_prov = any(re.match(r"^provenance:\s*", ln) for ln in lines)
    has_domain = any(re.match(r"^domain:\s*\S", ln) for ln in lines)
    actions = []

    if not has_domain:
        # insert domain: right after type: (or title:) — matches the frontmatter spec order
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("type:")), -1)
        if idx == -1:
            idx = next((i for i, ln in enumerate(lines) if ln.startswith("title:")), -1)
        lines.insert(idx + 1, "domain: " + domain)
        actions.append("domain")

    if not has_summary:
        body = text[m.end():]
        bd = bold_definition(body)
        if bd:
            # insert summary right after the slug: line (or at top of block)
            idx = next((i for i, ln in enumerate(lines) if ln.startswith("slug:")), -1)
            lines.insert(idx + 1, "summary: " + yaml_quote(bd))
            actions.append("summary")

    if not has_prov:
        # insert provenance just before status: (or at end of block)
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("status:")), len(lines))
        lines.insert(idx, "provenance: needs-review")
        actions.append("provenance")

    if not actions:
        return text, []
    new_block = "\n".join(lines)
    return text[:m.start()] + m.group(1) + new_block + m.group(3) + text[m.end():], actions


# ---- question-tier mode ------------------------------------------------------------
# Deterministic regex heuristic — no ML, no page-by-page judgment call. Priority order
# (first match wins), per CLAUDE.md's tier-class definitions:
#   scenarios   — the question IS an incident/postmortem: title or body names one, or the
#                 title itself carries a literal incident date (`\b20\d\d-\d\d-\d\d\b`).
#                 The date check is TITLE-ONLY (ponytail: a body date is usually just a
#                 citation `fetched 2026-06-18`, not the incident date — checking body would
#                 false-positive most sourced pages into `scenarios`).
#   support-kb  — a break-fix/known-issue page: a `symptoms:` frontmatter block (the
#                 troubleshooting-page marker), or the title itself reads like one.
#   conceptual  — everything else (the default, always in every domain's tiers-covered).
_SCENARIO_RE = re.compile(r"\bpost-?mortems?\b|\bincidents?\b|\boutages?\b", re.I)
_DATE_IN_TITLE_RE = re.compile(r"\b20\d\d-\d\d-\d\d\b")
_SUPPORT_KB_TITLE_RE = re.compile(
    r"error|fail|broke|fix|troubleshoot|crash|loop|timeout|known.issue|upgrade", re.I)
_SYMPTOMS_BLOCK_RE = re.compile(r"^symptoms:", re.MULTILINE)
_TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
_H1_RE = re.compile(r"^# .*$", re.MULTILINE)
_TYPE_LINE_RE = re.compile(r"^type:")

# Exact wording of the CLAUDE.md H1 out-of-coverage banner template (Operation: QUERY,
# "Confidence gate" section) — copied verbatim so lint's has_out_of_coverage_banner()
# (which only requires a `⚠️ ...` line mentioning "coverage") recognizes it, and so a
# reader gets the same sentence regardless of which tool inserted it.
_BANNER_TMPL = ("> ⚠️ Out of corpus coverage — `{domain}` holds `{covered}` only; "
                "this is a `{tier}` question and that tier is not ingested; "
                "verify against the primary source.")


def classify_tier(title, body, fm_block):
    """title/body/fm_block -> 'scenarios' | 'support-kb' | 'conceptual'. Pure, no I/O."""
    if _SCENARIO_RE.search(title) or _SCENARIO_RE.search(body) or _DATE_IN_TITLE_RE.search(title):
        return "scenarios"
    if _SYMPTOMS_BLOCK_RE.search(fm_block) or _SUPPORT_KB_TITLE_RE.search(title):
        return "support-kb"
    return "conceptual"


def insert_banner(body, domain, covered, tier):
    """Insert the H1 banner immediately after the first `# ` heading in `body` (the
    text following the frontmatter's closing `---`). Returns (new_body, inserted)."""
    m = _H1_RE.search(body)
    if not m:
        return body, False
    banner = _BANNER_TMPL.format(domain=domain, covered=", ".join(covered) or "(nothing)", tier=tier)
    rest = body[m.end():].lstrip("\n")
    return body[:m.end()] + "\n\n" + banner + "\n\n" + rest, True


def question_tier_backfill(text, domain, tiers_covered):
    """Return (new_text, tier, banner_inserted). tier is None (text unchanged) if the
    page already carries question_tier: (idempotent) or has no frontmatter/type: line."""
    m = FM_RE.match(text)
    if not m:
        return text, None, False
    block = m.group(2)
    if re.search(r"^question_tier:\s*\S", block, re.MULTILINE):
        return text, None, False  # already tagged — never touched

    lines = block.splitlines()
    idx = next((i for i, ln in enumerate(lines) if _TYPE_LINE_RE.match(ln)), -1)
    if idx == -1:
        return text, None, False  # no type: line — malformed page, leave it for lint to flag

    title_m = _TITLE_RE.search(block)
    title = unquote(title_m.group(1)) if title_m else ""
    body = text[m.end():]
    tier = classify_tier(title, body, block)

    lines.insert(idx + 1, "question_tier: " + tier)
    new_block = "\n".join(lines)

    banner_inserted = False
    covered = tiers_covered.get(domain) or []
    if tier not in covered and not has_out_of_coverage_banner(text):
        body, banner_inserted = insert_banner(body, domain, covered, tier)

    new_text = text[:m.start()] + m.group(1) + new_block + m.group(3) + body
    return new_text, tier, banner_inserted


def question_files():
    full = os.path.join(WIKI, "questions")
    if not os.path.isdir(full):
        return
    for fn in sorted(os.listdir(full)):
        if fn.endswith(".md") and fn != "README.md":
            yield os.path.join(full, fn)


def run_question_tier(args):
    tiers_covered = covmod.load_tiers_covered()
    tally, banners, changed = {}, 0, 0
    for path in question_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        m = FM_RE.match(text)
        dom = None
        if m:
            dm = re.search(r"^domain:\s*(\S+)", m.group(2), re.MULTILINE)
            dom = dm.group(1) if dm else None
        new_text, tier, banner_inserted = question_tier_backfill(text, dom, tiers_covered)
        if tier is None:
            continue
        changed += 1
        tally[tier] = tally.get(tier, 0) + 1
        banners += banner_inserted
        rel = os.path.relpath(path, WIKI)
        note = " +banner" if banner_inserted else ""
        print(f"{'WROTE' if args.apply else 'would tag'} {rel}: question_tier={tier}{note}")
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
    dist = ", ".join(f"{k}={v}" for k, v in sorted(tally.items())) or "(none)"
    print(f"\n{changed} pages {'tagged' if args.apply else 'pending'} "
          f"({'apply' if args.apply else 'dry-run'}) — tier distribution: {dist}; "
          f"{banners} H1 banner(s) inserted")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", nargs="?", default="frontmatter",
                    choices=["frontmatter", "question-tier"],
                    help="frontmatter (default): domain/summary/provenance; "
                         "question-tier: backfill question_tier: + H1 banners")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--domain", default="keycloak",
                    help="domain to stamp on pages missing `domain:` (frontmatter mode only; default keycloak)")
    args = ap.parse_args()

    if args.mode == "question-tier":
        run_question_tier(args)
        return

    changed = 0
    for path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        new, actions = backfill(text, domain=args.domain)
        if actions:
            changed += 1
            rel = os.path.relpath(path, WIKI)
            print(f"{'WROTE' if args.apply else 'would change'} {rel}: +{', +'.join(actions)}")
            if args.apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    print(f"\n{changed} pages {'updated' if args.apply else 'pending'} "
          f"({'apply' if args.apply else 'dry-run'})")


if __name__ == "__main__":
    main()
