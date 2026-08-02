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

## Known accepted misses

> Sign-off: given by the project owner (Guy) on 2026-07-23 via interactive approval
> in the orchestrating session ("Sign off — regenerate"); goldens regenerated the same
> day per the procedure below. The case-13 `expect_any_of` revisit remains a separate,
> still-open human decision (frozen-bank rule).

`baseline.eval.out` / `baseline.eval.route.out` / `baseline.eval.graph.out` are
currently **out of date** relative to `wiki/reference/active-directory/` — the four
`selftest.py` byte-identical checks (Phase-0 #12, Phase-3 #23) correctly FAIL. This
is an open finding, not yet resolved; the goldens have **not** been regenerated.

- **What changed**: 2026-07-23 corpus growth added 69 new `active-directory` reference
  notes (AD CS, LAPS, securing-privileged-access, software-restriction-policies:
  244 → 313 records), alongside five unrelated new domains. Adding to an
  already-eval-covered domain shifted `kb.lexical_rank`'s BM25 IDF/avgdl stats for
  that pool.
- **Effect on `cases.jsonl` case 13** (pair `kerberos-delegation`, kind `easy`/`exact`,
  query "resource based constrained delegation S4U2Self S4U2Proxy
  msDS-AllowedToActOnBehalfOfOtherIdentity"): both `expect_any_of` targets fell out of
  the `kmax=10` window —
  `ad-ds-configure-kerberos-delegation-group-managed-service-accounts` rank 9 → 31,
  `ad-ds-schema-updates` rank 9 → 122. The rank-9 hit that made this case pass before
  was `ad-ds-schema-updates`, a 1.38 MB schema-attribute dump that matched by brute
  lexical coverage, not genuine relevance — the corpus growth exposed a pre-existing
  weak spot in this case rather than creating a new one.
  Phase-2 graph-expand correctly rescues the miss to the right note
  (`ad-ds-configure-kerberos-delegation-group-managed-service-accounts`); **final
  ceiling recall is unchanged (27/29, 93%)**. The regression is confined to the raw
  lexical @5/@10 rows and MRR (see the eval-warden report, 2026-07-23, for the full
  before/after table).
- **NOT a route.py issue**: `evaluate.py` searches each case's labeled domain
  regardless of routing confidence, and `route.py --eval` shows
  `CONFIDENT-WRONG=0`, precision 100%, confident-skip count unchanged (22/29) —
  ruled out explicitly before attributing the regression to corpus growth.
- **Deferred to a human**: whether to revisit case 13's `expect_any_of` is barred
  from this fix by the frozen-bank rule (`cases.jsonl` is never edited after
  results) and is a human call, not an agent one. Separately, and for the same
  reason (no self-adjudication of a contested eval finding), regenerating the three
  goldens to accept this regression as new ground truth also needs an explicit
  human sign-off — an agent should not both find and clear this one. Once that
  sign-off exists, regenerate with: `python3 -m wikikb evaluate > eval/baseline.eval.out`,
  `... --route > eval/baseline.eval.route.out`, `... --graph > eval/baseline.eval.graph.out`,
  then rerun `python3 tests/selftest.py` and rename this section "Known accepted misses".
