# _meta/eval — acceptance banks, graders, goldens

- `answers300-partial-legacy.jsonl` — an INCOMPLETE historical cohort (137/300 answered,
  five of seven categories at zero). Kept as evidence, renamed 2026-07-12 when `grade300.py`
  gained its completeness gate; grading it now exits 2 (incomplete), which is correct —
  it was never a 300-case acceptance result. Do not append to it; `run300.py` starts new
  cohorts on fresh timestamped files.
- `grade300.py` exit codes: 0 complete+clean · 1 complete with hard-gate failures ·
  2 incomplete/malformed cohort (missing ids, empty/`[RUN-ERROR]` answers, duplicate or
  unknown ids). The scoreboard always prints; the exit code carries acceptance semantics.
