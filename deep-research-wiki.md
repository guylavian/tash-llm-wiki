---
description: Deep-research the llm-wiki repo — verify known gaps, find new ones, produce a prioritized report (and optionally fix P0s). Checkpointed + resumable.
argument-hint: "[fix] — pass 'fix' to also implement P0 fixes"
model: sonnet
---

# Deep research: what is missing in llm-wiki

You are running a long, potentially interrupted research task on this repo
(the llm-wiki Obsidian vault + the `_meta/wikikb` toolchain). Work methodically.
**Stay on Sonnet for everything. Never switch to Opus.** Delegate bulk file
scanning to subagents so the main context stays lean.

## Token discipline (hard rules)

- NEVER read the raw corpus bodies (`reference/` is 92MB, `_sources/` is 48MB).
  Retrieval goes through `python3 -m wikikb kb --domain <d> search "<terms>"`
  from `_meta/`, or `grep -l` for existence checks only.
- Read file heads/sections, not whole files, unless the file is < 200 lines.
- The recon commands below are free (local Python) — prefer them over reading.
- Use extended thinking ONLY where Phase 2 says so. Everywhere else, act.

## Checkpoint protocol (this makes the run survive rate-limit cuts)

- State file: `_meta/DEEP-RESEARCH-STATE.md`.
- **First action every session:** if the state file exists, read it and resume
  from the recorded phase/step. Do not redo completed steps.
- After completing EVERY numbered step, append to the state file: timestamp,
  step id, one-line result, and the next step id. Keep it under 200 lines
  (compact old entries into a summary block).
- If you notice a usage-limit warning or the session is about to die: write the
  checkpoint immediately and stop cleanly. The outer script will resume you.
- If this is a git repo: work on branch `deep-research/$(date +%Y%m%d)` and
  commit after each phase (`git add -A && git commit -m "deep-research: <phase>"`).
  If not a git repo, skip commits.

## Phase 1 — Recon (cheap, mechanical)

1. From `_meta/`, run and capture:
   - `python3 -m wikikb lint --status` (full output)
   - `timeout 600 python3 tests/selftest.py` — record pass/fail and wall time
2. Read: `README.md`, `AGENTS.md`, `QUERY-CARD.md`, `_meta/eval/README.md`,
   `_meta/pyproject.toml`, and the section headers of `CLAUDE.md` (not the body).
3. List: `_meta/eval/`, `_meta/tests/`, `.skills/`, `.opencode/`, check for any
   CI config (`*.yml` at root, `.woodpecker*`, `.github/`).

## Phase 2 — Verify seeded findings, then discover new ones

A previous audit (2026-07-18) found the items below. For each: **verify it is
still true, cite evidence (file:line or command output), and classify
P0/P1/P2.** Do not take them on faith.

- S1. `_meta/ROADMAP.md` missing while `README.md` links to it as the live roadmap.
- S2. `pyproject.toml [tool.setuptools] packages` omits `wikikb.mcp`,
  `wikikb.serve`, `wikikb.tkg` → editable install ships an incomplete package.
- S3. Lint: 53 warnings — ~10 citation-grounding suspects ("possible fabricated
  citation"), ~20 pages with provenance drift (inferred>=extracted), ~15 tags
  outside `_meta/taxonomy.md`, one page missing `domain:`,
  `questions/sso-implementation-review-framework.md` still `needs-review`.
- S4. Manifest drift: `.manifest.json` generated 2026-07-09; STATUS reports
  116 NEW cited-not-recorded sources, 6 GONE, 4 PENDING references never
  ingested (admin-rest-api, authorization-services, observability,
  server-development).
- S5. Dozens of `questions/*.md` missing `tags:` (backfill never run on them).
- S6. Eval doc drift: `eval/README.md` declares `cases-substitution.v2.jsonl`
  CURRENT, but only v4 files exist; the "preserved unchanged" v1/v2 banks are
  absent from the tree.
- S7. `selftest.py` exceeds 5 minutes; no fast tier / markers for a quick gate.
- S8. No CI config anywhere in the repo (Woodpecker is available in this org).
- S9. `.claude/` is fully gitignored, so Claude Code commands/agents have no
  versioned home, unlike `.opencode/command/`.

Then, **ultrathink**: with the recon data and verified findings in front of
you, do ONE deep synthesis pass over these axes and hunt for gaps the seed
list missed:

- Correctness: are the citation-grounding suspects real fabrications or
  tokenizer false positives? Sample 3 and check against their cited sources
  via `kb search`.
- Data hygiene: manifest regeneration path, taxonomy completeness, tag
  normalization coverage.
- Eval integrity: cohort completeness gates, frozen-bank preservation,
  validation-independence rule vs same-family banks, whether grade300's exit
  codes are actually enforced anywhere.
- Retrieval: lexical vs dense — is `embed.py` evaluated at all? Is there a
  measured comparison, or is dense retrieval dark-launched?
- Testing: unit coverage vs subprocess smoke; propose a <60s fast tier.
- Ops: serve/MCP hardening defaults, tkg rebuild verification, Docker images
  vs current layout.
- Docs: every claim in README/CLAUDE.md that names a file, count, or command —
  spot-check 10 for truth.
- DX: where should Claude Code slash commands live given S9.

## Phase 3 — Report

Write `_meta/DEEP-RESEARCH-<YYYY-MM-DD>.md` containing, in prose + tables:

1. Executive summary (10 lines max).
2. Findings table: id, severity (P0/P1/P2), evidence, proposed fix, est. effort.
3. A drafted `_meta/ROADMAP.md` (so S1 can be closed by review, not invention).
4. A proposed `<60s` fast-test tier design and a minimal Woodpecker pipeline
   (lint + fast tier on push; full selftest nightly).

## Phase 4 — Fix (ONLY if "$ARGUMENTS" contains "fix")

Implement P0s only, one commit each, re-running `python3 -m wikikb lint` after
each: S2 (pyproject packages), S5 (`tags.py` backfill), S4 (regenerate
manifest via the documented manifest tool), S6 (eval README v2→v4 correction),
S1 (commit the ROADMAP draft from the report). Never touch `reference/`,
`references/`, or `_sources/` — they are immutable.

## Completion sentinel

When the report exists and (if requested) fixes are committed, print exactly:

<<DEEP-RESEARCH-COMPLETE>>

on its own line as the final output. Print it ONLY when genuinely done — the
outer retry loop uses it to stop.
