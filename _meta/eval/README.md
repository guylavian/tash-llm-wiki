# _meta/eval — acceptance banks, graders, goldens

- `answers300-partial-legacy.jsonl` — an INCOMPLETE historical cohort (137/300 answered,
  five of seven categories at zero). Kept as evidence, renamed 2026-07-12 when `grade300.py`
  gained its completeness gate; grading it now exits 2 (incomplete), which is correct —
  it was never a 300-case acceptance result. Do not append to it; `run300.py` starts new
  cohorts on fresh timestamped files.
- `grade300.py` exit codes: 0 complete+clean · 1 complete with hard-gate failures ·
  2 incomplete/malformed cohort (missing ids, empty/`[RUN-ERROR]` answers, duplicate or
  unknown ids). The scoreboard always prints; the exit code carries acceptance semantics.
- `cases-substitution.v4.jsonl` (WI-8) — the CURRENT rationalized-substitution bank: 29
  questions that presuppose a plausible adjacent-real identifier which does NOT exist in the
  corpus. FROZEN at authoring (committed before any run; never edited after results). Header
  record carries the authorship label `same-family — NOT independent` (blind-ish sub-agent,
  same model family — per the validation-independence rule this bank can inform but never
  certify). v4 supersedes v3 (which supersedes v2, which supersedes v1) — each prior version
  was preserved unchanged in git history before superseding; only the current version is kept
  in the tree. See `GRADING-substitution.v4.md` for the v4-specific Class A/B grading notes.
  Grading: `must_correct` → the `CORRECTED n/m (report-only)` scoreboard column; it NEVER feeds
  hard_fail or the exit code.
  Grade with `python3 eval/grade300.py --cases eval/cases-substitution.v4.jsonl --answers <cohort>`.
