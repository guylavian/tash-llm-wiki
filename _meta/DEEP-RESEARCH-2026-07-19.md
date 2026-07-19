# Deep research — llm-wiki gaps (2026-07-19)

Research-only run (`מחקר בלבד`) — no fixes applied. Every seed finding (S1–S9) from
the 2026-07-18 audit was independently re-verified against current repo state
(commit `9308c1e`, branch `agent/add-llm-wiki-logical`); several were more/less
severe than claimed, one (S7) was flatly wrong as stated. Eleven new findings
(N1–N11) surfaced during synthesis, including two real failures in the
project's own test suite that the seed list never mentioned.

## Executive summary

- All 9 seed findings (S1–S9) confirmed true, with corrected specifics for S3/S7.
- **S7 is measurably wrong**: selftest.py runs in 4:23 (263s), not ">5 minutes."
  It's still slow enough to want a fast tier — the *conclusion* holds, the *evidence* doesn't.
- **New, most important finding (N10)**: selftest.py currently fails 2/78 checks.
  One (crosslink, 8 unresolved `kb:` tokens) is a documented, accepted pre-existing
  red. The other (serve SIGINT clean-exit) is **undocumented** and needs a rerun in
  isolation to confirm it's not a load-induced flake from this session's concurrency.
- **Citation-grounding lint warnings are mostly false positives** (N/S3): sampled
  4 of 16, all four were angle-bracket placeholder tokens (`<KEY_WITH_UNDERSCORES>`)
  or literal metadata values, not real fabricated citations. The heuristic needs a
  placeholder-token exclusion.
- **Dead infra shipping in the Docker path** (N1): docker-compose.yml/Dockerfile
  still install and configure the Kuzu/Graphiti TKG backend that was deleted from
  the codebase 2026-07-05.
- **README's numeric claims are stale everywhere they can be checked** (N2):
  questions undercounted by 52 (88 claimed vs 140 actual), all four reference-tier
  counts undercounted.
- **Dense retrieval is dark-launched** (N3): fully wired, never measured.
- **serve has no auth**, and the Dockerfile's own example binds it to `0.0.0.0` (N4).
- No CI exists (S8, confirmed) and grade300's exit code is gated on by nothing but
  its own self-test (N8) — real eval cohorts are graded by eyeball only.

## Findings table

| ID | Sev | Finding | Evidence | Proposed fix | Effort |
|----|-----|---------|----------|---------------|--------|
| S1 | P1 | `_meta/ROADMAP.md` missing; README.md:83 links it as "the live roadmap" | `ls _meta/ROADMAP.md` → ENOENT | Commit the draft in this report (§ Drafted ROADMAP.md) | S |
| S2 | P1 | `pyproject.toml` `[tool.setuptools] packages` omits `wikikb.mcp/.serve/.tkg` | `_meta/pyproject.toml:38-40`; dirs exist (`_meta/wikikb/{mcp,serve,tkg}/__init__.py`) | Add 3 names to the list. Note: Docker path (`PYTHONPATH`, no `pip install`) already sidesteps this — only the optional dev `pip install -e .` convenience is broken | XS |
| S3a | P1 | Lint: 53 warnings, exact breakdown: 16 citation-grounding, 17 provenance-drift, 16 tags-outside-taxonomy, 1 missing `domain:`, 1 `needs-review` | `python3 -m wikikb lint --status` full output | See S3b for the citation-grounding correctness finding; `tags.py normalize/backfill --apply` for the rest | M |
| S3b | P1 | **Citation-grounding suspects are mostly false positives.** Sampled 4/16, all 4 wrong: `KEY_WITH_UNDERSCORES`/`UPPER_SNAKE_CASE`/`AURORA_URL` are angle-bracket placeholders in a naming-convention example (`topics/server-configuration.md:26`, `questions/kc-db-url-password.md:31`, `entities/rhbk-db-connection-pool.md:45`); `VERBATIM_MATCH` is a literal frontmatter-adjacent field value (`questions/rhbk-login-storm-oom-queue-cap.md:35`), not a technical identifier | 4 direct greps, see transcript | Exclude `<...>`-bracketed placeholder tokens and known metadata-literal values from lint.py's distinctive-token heuristic | S-M |
| S4 | P1 | Manifest drift confirmed exact: 116 NEW cited-not-recorded, 6 GONE, 4 PENDING references never ingested | `lint --status` STATUS block | `manifest.py record` sweep + ingest the 4 pending references (admin-rest-api, authorization-services, observability, server-development) | M |
| S5 | P2 | ~90 pages missing `tags:` | `lint --status` WANTED/tags block | `python3 -m wikikb tags backfill --apply` | XS |
| S6 | P1 | `eval/README.md:11-20` tells the reader to grade against `cases-substitution.v2.jsonl` — doesn't exist; only v4 remains | `find _meta -iname "*substitution*"` → only v4 + GRADING-substitution.v4.md. Git history shows v1 (`4abc6a8`)/v2 (`4a2a2d5`)/v3 (`32e647b`) *did* exist and were properly frozen before runs, deleted later in `5efd1d8` | Update README to point at v4 + GRADING-substitution.v4.md | XS |
| S7 | P2 | **Claim was wrong as stated.** selftest.py measured: `4:22.97` (263s) wall, not ">5 minutes" | `time python3 tests/selftest.py` → `4:22.97 total`, 76/78 passed | Correct the claim; still slow enough to want a fast tier (see § Fast-tier design) | S |
| S8 | P2 | No CI config anywhere (only `_meta/docker-compose.yml`, not CI) | `find . -iname "*.yml" -o -iname ".github" -o -iname ".woodpecker*"` → nothing but docker-compose.yml | Minimal Woodpecker pipeline (§ below) | S |
| S9 | P1 | `.claude/` fully gitignored (`.gitignore:20`); contains exactly one file, `.claude/commands/deep-research-wiki.md` (the skill running *this* research), untracked | `git check-ignore -v .claude`, `git ls-files .claude` → empty | Un-ignore `.claude/commands/` and `.claude/agents/` specifically (keep session-state ignored); commit them, mirroring `.opencode/command/` | S |
| N1 | P0 | docker-compose.yml + Dockerfile still configure the **removed** Kuzu/Graphiti TKG backend: `WIKI_TKG=kuzu` env var, "Kuzu TKG backend" header, `pip install kuzu` + cmake/build-essential/git build deps — all for a module deleted 2026-07-05 | `docker-compose.yml:1,23`; Dockerfile kuzu install (per subagent, `_meta/wikikb/tkg/{tkg,store,__init__}.py` confirm removal; `selftest.py:522,536,663` assert it's gone) | Strip WIKI_TKG/kuzu from both files and the build-toolchain deps | S |
| N2 | P1 | README's numeric claims stale everywhere checkable: questions 88 claimed vs **140** actual (+52, ~60% undercount); reference/keycloak 800 vs 833; reference/openshift 3,813 vs 3,908; reference/active-directory 221 vs 236; reference/cisco-ios-xe 167 vs 173 | `ls questions/*.md \| wc -l` = 140 etc.; README untouched across 8+ content commits (`git log --oneline -- README.md`) | Generate these counts mechanically (e.g. a `--stats` line from index.py/lint.py) instead of hand-maintained prose | S |
| N3 | P2 | Dense retrieval (`embed.py`, `kb.py --hybrid`, `evaluate.py --hybrid`) is fully wired into every consumer but has **zero measured baseline** anywhere — no `baseline.eval.hybrid.out`, no vendored model/embeddings present, `evaluate.py` itself says hybrid is "reserved for Phase 3." Dark-launched. | subagent evidence: `embed.py:64-71`, `evaluate.py:28`, `selftest.py:156-159` only tests graceful degradation, never a measured delta | Vendor the offline model once, commit one hybrid baseline next to the lexical ones | M |
| N4 | P1 | `serve.py` has **no auth/rate-limiting** on `/ask /search /page /route /expand`; defaults to loopback (good) but the Dockerfile's own documented example explicitly shows `--bind 0.0.0.0` with no auth guidance | subagent evidence: `serve.py:11-12,305-307` (bind default), `serve.py:253-276` (no auth path); `/upload` by contrast is well-hardened (opt-in, traversal-safe, size/magic checks — verified by `upload_probe.py:119-168`) | Loud stderr warning on non-loopback `--bind`; document a reverse-proxy/auth recommendation next to the 0.0.0.0 example | S–M |
| N5 | P2 | Dockerfile `EXPOSE 8080` "not currently used" while serve.py's real default port is 8642; docker-compose.yml maps no ports at all | Dockerfile EXPOSE line vs `serve.py:15,304` | `EXPOSE 8642`, drop the stale line | XS |
| N6 | P2 | `tkg.py`'s `ingest` has no self-check against prior store before overwrite; `store.py` writes `graph.json` directly (no temp+rename) — crash mid-write corrupts the store (fails loud on next load, not silently). Note: selftest.py *does* externally verify ingest idempotence as a regression test, so drift is caught in dev/CI runs, just not guarded by the tool itself live | subagent evidence: `tkg.py:34-53`, `store.py:31-36,39-44` | Atomic write (`tmp` + `os.replace`) — near-zero cost | XS-S |
| N7 | — | Checked, **not an issue**: `tkg/versions.py` already covers RHBK 26.6 (errata-confirmed, RHEA-2026:22857) | subagent evidence, `versions.py:45-48` | none needed | — |
| N8 | P2 | grade300.py's exit code is gated on by **nothing** except its own self-test (`selftest.py:1198-1361`); `run300.py` only *prints* the suggested grade300 command, never invokes it. A vacuous 0-case `--cases` run currently exits 0 "clean" (untested edge case) | repo-wide grep for `grade300`; `run300.py:492` | Wire the exit code into CI once S8 lands; add a case-count floor to grade300.py | S (post-CI) |
| N9 | P2 | Three independent, uncoordinated exit-code taxonomies (grade300.py 0/1/2 ≠ gate_probe.py 0/1/2 ≠ others) — same numbers, different meanings | subagent cross-check | Document distinctly; no code change needed | — |
| N10 | P1 | **selftest.py fails 2/78 checks in this run.** (a) crosslink: 8 distinct unresolved `kb:` tokens — this IS a documented, accepted pre-existing red (`selftest.py:190-196`, "no NEW failures vs recorded baseline" per a `COUNCIL-DIRECTIVES.md` reference that itself doesn't exist in this repo — a dangling doc pointer). That same comment also lists `lint --strict` (check #4) as pre-existing-red, but check #4 **currently passes** — the comment is stale and should drop it. (b) `serve smoke: ... SIGINT -> clean exit 0` — **undocumented anywhere as expected**; `health_ok=True ask_ok=True exit_ok=False`. `serve.py`'s `main()` (~L302-328) catches `KeyboardInterrupt` correctly in isolation. This run had 3 parallel subagents + a full lint scan competing for CPU at the same time, which may have squeezed the test's 5s SIGINT-wait budget (a plausible culprit: `ThreadingHTTPServer`'s default `block_on_close=True` joining an in-flight handler thread inside `server_close()`) | full selftest.py transcript (76/78 passed) | Rerun `python3 tests/selftest.py` in isolation to confirm (b) isn't a load flake before treating it as a regression; if real, investigate `block_on_close`/thread lifetime in serve.py; fix the stale check-#4 comment either way | XS to confirm, S to fix if real |
| N11 | P2 | DX: given S9, the natural versioned home for Claude Code commands/agents is `.claude/commands/` + `.claude/agents/` specifically — not the whole `.claude/` tree, which also holds legitimately-ignorable machine-local state (shell-snapshots, settings.local.json). CLAUDE.md's own "Operational lessons" section documents a `.claude/agents/` subagent team meant to persist across sessions/machines, which the current blanket ignore makes impossible | `.gitignore:20`; CLAUDE.md "Operational lessons" section | Two `!` negation lines in `.gitignore` for `.claude/commands/` and `.claude/agents/`, mirroring `.opencode/command/` | XS |

## Drafted `_meta/ROADMAP.md`

Not committed (research-only run) — paste this in when S1 is picked up for a fix pass:

```markdown
# Roadmap

## Landed
- Stdlib-only retrieval (route/search/expand), lint + Confidence gate, delta manifest.
- Optional dense retrieval (embed.py), graph-expansion (expand.py), the temporal
  knowledge graph (tkg/, JSON-store canonical), graph-by-default `ask`, and the
  cited/gated serve + MCP pipeline.
- Optional online tier (LiteLLM gateway, LangGraph orchestration) — off by default,
  local-first, graceful degradation verified by selftest.py.

## Now
- Fix the P0/P1s from `_meta/DEEP-RESEARCH-2026-07-19.md`: dead Kuzu config in
  Docker (N1), stale README counts (N2), missing pyproject packages (S2), manifest
  drift (S4), eval README v2→v4 correction (S6), citation-grounding false positives
  (S3b), the undocumented serve-SIGINT test failure (N10b — confirm in isolation first).
- Versioned home for Claude Code commands/agents (S9/N11).
- A `<60s` fast test tier + a minimal CI pipeline (S7/S8, design in the same report).

## Later
- A measured hybrid (lexical+dense) baseline committed alongside the lexical ones (N3).
- Auth/rate-limiting story for `serve` when bound off loopback (N4).
- Wire grade300's exit code into CI once it exists (N8); a case-count floor check.
- Atomic writes for the tkg JSON store (N6).
```

## Fast (`<60s`) test-tier design

`selftest.py` is one linear stdlib script (79 `check()` calls, own PASS/FAIL tally,
no pytest) — 76/78 pass in 263s currently. The wall-time sinks are ~25 sections that
shell out to a subprocess over the full corpus/wiki tree: `lint --strict`, `index
--check`, bare `crosslink.py`, `corpus_to_vault --verify` (hashes the full 92MB
`reference/` tier), 7× `evaluate` invocations, 2× `livebank --ci` (24 real questions
through the full pipeline each), 3× `verify`, the serve/mcp smoke tests, and 7× `tkg`
subprocess calls. Everything else (~50+ checks) is in-process unit/fixture work.

Minimal-diff mechanism (reuses the existing `check()`/tally convention, no new
framework):

```python
FAST = os.environ.get("SELFTEST_FAST") == "1"   # one line after _ENV = {...}
```

Wrap each slow section in `if not FAST: <existing code>`; print
`f"  SKIP  {name} (SELFTEST_FAST)"` instead of calling `check()` when skipped — skips
shrink the denominator, never count as pass/fail.

- **Keep in fast tier**: all in-process unit/fixture checks, `kb domains`/`kb
  search`/`kb --hybrid` (cheap single lookups), embed/BM25/citation-grounding units,
  restructure/import guards, `crosslink.resolve_any` logic (in-process), the
  grade300/run300 mini-cohort checks (synthetic 1-2-row files), and the final
  grade300 run against the real bank (pure scoring, no retrieval).
- **Defer to nightly/full**: `lint --strict`, `index --check`, bare `crosslink.py` +
  its full-tree baseline walk, `corpus_to_vault --verify`, all 7 `evaluate` runs, both
  `livebank --ci` runs, all 3 `verify` calls, serve smoke, mcp smoke, all 7 `tkg` calls.

## Minimal Woodpecker pipeline (proposal, not committed)

```yaml
# .woodpecker.yml
pipeline:
  lint:
    image: python:3.12-slim
    commands:
      - cd _meta && python3 -m wikikb lint

  fast-tests:
    image: python:3.12-slim
    commands:
      - cd _meta && SELFTEST_FAST=1 python3 tests/selftest.py

  full-selftest:
    image: python:3.12-slim
    commands:
      - cd _meta && python3 tests/selftest.py
    when:
      event: cron
    # nightly only — the full 4-5min run, not on every push
```

`lint` + `fast-tests` on every push; `full-selftest` on a nightly cron trigger
(Woodpecker's `event: cron` + a matching cron schedule in project settings).

## Correctness sample (Phase 2, "is it real or a false positive?")

Sampled 4 of the 16 citation-grounding lint warnings directly (not delegated):

| Page | Flagged token | Actual context | Verdict |
|------|---------------|-----------------|---------|
| `topics/server-configuration.md:26` | `KEY_WITH_UNDERSCORES` | `` `KC_<KEY_WITH_UNDERSCORES>=<value>` `` — a naming-pattern placeholder | False positive |
| `questions/kc-db-url-password.md:31` | `UPPER_SNAKE_CASE` | `` `KC_<UPPER_SNAKE_CASE>` `` — same placeholder pattern | False positive |
| `entities/rhbk-db-connection-pool.md:45` | `AURORA_URL` | `` jdbc:aws-wrapper:postgresql://<AURORA_URL>:5432/keycloak `` — a template placeholder in a config example | False positive |
| `questions/rhbk-login-storm-oom-queue-cap.md:35` | `VERBATIM_MATCH` | `VERBATIM_MATCH: yes` — a literal grading/metadata-style field, not a product identifier | False positive |

4/4 sampled were false positives from the same root cause: lint.py's distinctive-token
heuristic doesn't exclude angle-bracket placeholder syntax (`<...>`) or literal
metadata-style field values. Given 100% of the sample was wrong, the other 12
citation-grounding warnings are likely mostly/all false positives too — worth a full
re-audit once the heuristic is fixed (S3b).

## Verified NOT an issue

- `tkg/versions.py` already has RHBK 26.6 (errata-confirmed) — not stale.
- The same-family substitution bank's "report-only" `must_correct` scoring is
  correctly kept out of `hard_fail`/exit code (grade300.py) — the disclosed caveat
  doesn't silently leak into a pass/fail signal.
- v1/v2/v3 substitution banks *did* exist in git, committed before any run — the
  validation-independence rule was honored at authoring time; they were later
  deleted in a cleanup commit, which is what left the README's v2 reference dangling
  (S6), not a violation of the freeze rule itself.
