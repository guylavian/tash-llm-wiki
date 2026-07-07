# PRODUCTION READINESS — LLM-Wiki / SRE-brain

## VERDICT (2026-07-06): NOT signed off for unsupervised production. Positioned as a
## cited-source retrieval system, not a verified-answer system. Four audit findings
## remediated + independently re-verified; the honest numbers are below.

The prior "SIGNED OFF … 100% livebank" claim is **withdrawn**. An independent audit
(auditor did not build the system) found the 100% measured retrieval-pool quality, not
answer quality; the only answer-generating config scored ~0/10 on blind questions. This
document replaces that claim with measured, blind-authored, answer-text-graded numbers.

---

## Fix 1 — Livebank independence + the live-model failure (the real blocker)

**Root cause of the live-model failures (traced, not guessed):**
- **FSMO "Infrastructure Master" + invented GPO path, fabricated `dsrepadmin /forceauth`,
  DPoP "not before 26.6", PLEG→corosync/STONITH** — every one was a *synthesis* failure,
  not (only) retrieval: the correct page was often in the candidate set, but the synthesis
  context assembler (`graph/nodes.py::_assemble_context`) filled to an 8000-char cap
  **sequentially**, so a single large rank-1 note (e.g. a 47k-char virtualized-DC note)
  evicted every other candidate — including the one holding the answer — before the model
  saw it. Fixed: **fair-share budgeting** (each candidate gets ≥ its equal share, surplus
  donated forward; verified a real 18-candidate/4k–115k-char query now gives all 18 real
  content). Regression test added (selftest).
- **Zero-citation hallucinations are now withheld.** When the model cites *none* of the
  offered sources, the prose is **withheld entirely** — served text becomes
  `[ungrounded synthesis withheld — model cited none of the retrieved sources]`.
  **Scope (independent-verifier finding, honest):** this catches only the *zero-citation*
  case. It does **not** catch the *fabricated-citation* class — model cites a real source ID
  but attaches invented facts, or cites an irrelevant note (verified live on bank case ke2-2:
  the model invented "5 failures / 1 hour" lockout values and mis-cited a federation note).
  Such answers are **still served** (and correctly graded FAIL by the bank — scoreboard
  integrity holds — but a caller receives them). Closing the fabricated-citation class
  (per-claim grounding, the `SSO_HTTPS_CIPHER_SUITES` precedent) is an **open item**, not
  done. So: the system withholds *some* hallucinations, not all.
- **Dead-endpoint config** (`llm.config.yaml` → LM Studio :1234) silently degraded to the
  factless fallback, inflating the failure count. Repaired to the live Ollama endpoint
  (`ollama/qwen2.5:3b`, `127.0.0.1:11434`); the fallback line now **names the reason** when
  the gateway is meant to be on but returns nothing.

**Livebank rebuilt (blind-authored, answer-text-graded):**
- v1 frozen as `eval/livebank-v1-DEPRECATED.jsonl` (co-tuned with the fixes it measured —
  kept for regression only, no longer a gate).
- v2 = **24 cases authored by 4 per-domain agents with no visibility into system behavior
  or prior failures**, from `reference/<domain>/` notes only, **git-committed before the
  first run** (commit `a24d368`, 2026-07-06 11:47 +0300), never edited after seeing results.
  *Forensic caveat (independent-verifier note):* the repo is a fresh init with a squashed
  initial commit, so "committed before first run" rests on the commit message + this record,
  not on a chain of separately-timestamped commits. Future bank changes should land in their
  own commit, with the results-recording run in a later commit, so the ordering is provable
  from git history alone.
- Grading is on the **served answer text only**. A fallback/withheld answer is **UNGRADED**
  (never a pass); `forbid` runs on the answer text; the coverage **gate is graded
  independently** and always.

**The honest numbers (first and only run of v2):**

| Config | Graded pass | UNGRADED (withheld/fallback) | Gate correctness |
|---|---|---|---|
| Offline (default, `WIKI_LLM` unset) | 0/0 — **no answers produced** | 24/24 | **24/24** |
| Live model (qwen2.5:3b, repaired) | **2/15 graded = 13.3%** | 9/24 | **24/24** |

So: with the local 3B model the system correctly answers ~13% of blind questions, withholds
~38% rather than hallucinating, and its **coverage gate is 100% correct** (both
out-of-coverage banners fired; every tier decision right). The old "100%" is not comparable —
it graded retrieval pools and could pass on an empty answer. **13.3% is the answer-quality
number that stands next to it.**

**Product positioning (Fix 1c — decided):** this ships as **"returns cited primary sources
for a human/stronger-model to read,"** NOT "returns verified answers." The retrieval + gate +
citation chain is the product; local-3B synthesis is not reliable enough to be the product
and is now honest about it (withholds, names failures). A larger synthesis model is the path
to raising 13.3%, tracked separately.

---

## Fix 2 — Adversarial review independence (standing process rule, in CLAUDE.md)

The audit's finding — one model family end to end, weakest model attacking strongest,
architect self-adjudicating — is now a **standing rule** in `CLAUDE.md` ("Validation
independence"):
- No same-family adversarial pass counts as independent; where no other family is available
  (air-gapped: local Ollama or a human), the pass is **labeled "same-family — NOT
  independent"** in any sign-off it feeds.
- **No self-adjudication** — contested findings go to an uninvolved third party.
- Acceptance banks are **blind, git-frozen-before-run, answer-text-graded**, never tuned
  against.

**Known-backlog P2s from the audit's independent re-run — all fixed & rebuilt:**
CR_ACT_AS_USER GUID (confirmed *fabricated* against the MS-ADTS control-access-rights table,
removed + replaced with the correct ACE mechanism, web-cited); 32k-page attribute counts
(corrected to the maximum-limits note — surfaced a genuine 3,000-vs-3,200 MS-docs
discrepancy, now `(ambiguous)`-tagged); the unresolved `[[kubernetes-networkpolicy]]` link
(page created, grounded); "PSP deprecated in 1.25" (corrected to deprecated 1.21 / **removed**
1.25, version-attributed).

---

## Fix 3 — Verify-gate coverage (honest denominator now in every run)

Old headline "95 claims, 42 verified, 0 MISMATCH" implied near-total coverage. The verifier
now prints the **true denominator**:

> `verify — 45 verified / 125 eligible / 230 total numeric-claim candidates (20% of all
> claims machine-verified) · 0 MISMATCH · 80 ungrounded`

- **20% of all numeric claims are machine-verified** (was implied ~100%). The verified count
  dropped 47→45 after an independent-verifier finding (below) — a *more* honest number.
- Coverage extended to the two named gaps: **cross-line-wrapped claims** (the live-caught
  binder bug — a `terminationGracePeriodSeconds:30s` claim whose "default" fell on the prior
  wrapped line, one token short of the bind floor — root-caused and fixed; now VERIFIED, with
  a regression check) and **bare table cells** (bound via row-label + column-header context).
- **VERIFIED precision — two false-positive classes the independent verifier caught and I
  fixed:** (a) the number regex had no left word-boundary, so digits inside identifiers
  ("Argon2"→2, "HS256"→256) leaked into source-line number sets and produced false VERIFIED
  binds — fixed with a `(?<![A-Za-z0-9])` boundary; (b) any 400–599 number was unconditionally
  treated as an HTTP status code and verified by mere presence-anywhere, so a real "410 req/s"
  rate got rubber-stamped — now the http path requires an http-signal word nearby. Both drop
  false positives (47→45 verified). **Still open (not fixed):** the lenient `≥2 shared context
  tokens` bind threshold can still over-match on generic words (request/limit/memory) across
  unrelated sizing examples in the same corpus — a known precision limitation; verify is a
  backstop, not a guarantee.
- **0 MISMATCH: no missed contradiction found.** The independent adversarial spot-check found
  *no* case of a wrong number served as right (no missed MISMATCH); the false positives above
  were VERIFIED-precision defects, now reduced. The 80 ungrounded are honest gaps (comparator
  prose like "< 250 ms"; web-only-sourced pages; one immutable raw-layer table that lost its
  label column in doc conversion — left UNGROUNDED, not papered over). One content page that
  the verifier caught conflating two worked examples ("~410 req/s" attached to an unrelated
  resource block) was fixed by removing the ungrounded figure.

---

## Fix 4 — Concurrency ceiling: mechanism NAMED (was "unknown")

**Mechanism: memory exhaustion on a 16 GB box.** Measured at rest with Docker + Ollama
running: `PhysMem 15G used, 137M unused, compressor 4820M, swap 7358M/8192M used (90%)`.
Docker runs 5 containers (keycloak, litellm, litellm-postgres, grafana, openfga ≈ 1.3 GB+);
Ollama holds a resident 2.4 GB model. Three concurrent LLM calls each took ~17 s vs ~2 s
solo — an ~8× contention slowdown. Each additional concurrent subagent loads a Python venv +
embedding model (hundreds of MB) or an LLM call, pushing past the ~0 free-RAM ceiling into
swap → macOS memory-pressure stalls/kills. **So: "≤3 because a 16 GB box is already at its
memory ceiling from Docker + Ollama + the agent working set."** Mitigations (any one):
stop unused Docker containers during agent waves; use lexical-only (no embedding-model load)
for concurrent agents; more RAM. This is a **host constraint, not a code defect**, and it is
now documented with its cause.

**Serving path load-tested for the first time** (separate code path, never covered by the
≤3 finding): `ThreadingHTTPServer`, concurrent clients —
- 8 workers / 80 req: 200s clean, p50 51 ms, p95 2.1 s
- 32 workers / 200 req: 200s clean, p95 7.9 s
- 64 workers / 300 req: **10/300 connection errors**, p95 11.5 s
Throughput plateaus at **~16 rps regardless of concurrency** (single-model / GIL-bound
retrieval), degrading to connection failures at 64 concurrent. **Serving is safe for a
handful of concurrent agents, NOT for 64-way public load** — put a concurrency limit / queue
in front before exposing it. Documented as a known ceiling.

---

## Multi-skill / subagent enforcement (from the enforcement-gap tasks)

The query protocol is now **domain-agnostic** and enforced by **whichever layer writes the
user-facing answer** (CLAUDE.md: "The answer-producing layer owns this gate"). Fixes: subagent
research must return per-claim `file.md:line` citations + provenance tags; synthesis must
preserve them verbatim (no compression to file-level, no dropped tags); a **blocking final
self-check** checklist; and cross-skill handoff notes in the sibling skills (windows-eventlog).
Verified across domains: pages filed with per-claim line citations + extracted/(inferred) tags
for Kubernetes (`terminationgraceperiodseconds-zero-sigterm`), Cisco (`lacp-fast-switchover-prereqs`),
AD (`w32tm-resync-force-flag`), and two multi-skill matches (`kcd-rbcd-mutual-exclusivity`,
`kerberos-preauth-4771-bruteforce`).

---

## Current state (measured 2026-07-06)

- **selftest 63/63** (was 60/60; +regression checks for fair-share context, ungrounded-
  withhold, gateway-failure reason, verify wrap-bind, answer-graded livebank).
- **verify**: 47/125/230, **20% machine-verified, 0 MISMATCH** — honest denominator shipped.
- **livebank v2**: blind-authored, git-frozen pre-run; **live 13.3% graded, 24/24 gate,
  9 withheld**; offline 0 answers / 24 gate.
- **`wikikb build`** clean (tags→crosslink→index→tkg→lint→verify).
- git initialized; `reference/` + generated indexes gitignored per the storage decision.

## Honest limitations (unchanged truths + new)

1. Local-3B synthesis answers ~13% of blind questions — **the product is cited retrieval,
   not verified answers** until a stronger synthesis model is wired.
2. Dense/hybrid retrieval needs `.venv-embed`'s interpreter; plain `python3` is lexical-only.
3. Concurrency ≤3 is a **16 GB memory ceiling** (named); serving plateaus ~16 rps and errors
   at 64-way — not safe for public load without a queue.
4. 80% of numeric claims are not machine-verified (comparator prose, notes-first/web-cited
   lines, one damaged raw table) — verify is a backstop, not a guarantee.
5. Adversarial independence on an air-gapped box is bounded by having only one model family +
   local Ollama; genuine independence needs a different family or a human reviewer — labeled
   as such, never silently counted as independent.

## Independent re-verification (2026-07-06) — verdicts + what they changed

Four independent verifier agents (structurally separate from the implementers; audit-style
adversarial prompts) re-checked each fix. They did their job — two came back PARTIALLY_FIXED
with real defects the implementers missed:
- **Fix 4 (concurrency): CONFIRMED_FIXED** — memory-ceiling mechanism independently
  re-measured (16 GB, swap ~90% full, Ollama 2.39 GB resident, 7 Docker containers); serve
  load test reproduced (~16 rps plateau, errors at 64-way).
- **Fix 2 (content P2s): PARTIALLY_FIXED → now closed** — 3/4 P2s + all 5 new pages clean;
  the RBCD GUID fix was incomplete (fabricated GUID still printed in the technical body while
  labeled "removed"). **Fixed:** GUID now appears only in the Contradictions/caveats correction
  note, not the body.
- **Fix 3 (verify): PARTIALLY_FIXED → largely closed** — honest denominator + regression
  confirmed; two false-VERIFIED classes found (identifier-digit leak; HTTP-code loophole).
  **Both fixed** (47→45 verified); the lenient-threshold over-match remains a documented open
  precision limitation.
- **Fix 1 (livebank): PARTIALLY_FIXED** — blind/frozen/answer-graded/withhold + numbers all
  reproduced (13.3% graded, 24/24 gate); the withhold's scope was overstated. **Doc corrected**
  to scope it to the zero-citation case and name the fabricated-citation gap as open.

## Sign-off conditions still open (do NOT restore "production-ready" until met)
- Raise blind-bank live graded pass materially above 13.3% with a stronger synthesis model,
  OR ship+document as cited-retrieval-only (current positioning).
- **Close the fabricated-citation class** (per-claim grounding) so the withhold path catches
  invented-facts-on-a-real-citation, not just zero-citation — verified live as still-open.
- Tighten verify's bind threshold (rarity/specificity requirement) to remove the remaining
  generic-word over-match precision gap.
- A queue/limit in front of the serving path before any exposed deployment.
- A genuinely different-family (or human) adversarial round — this re-verification ran on the
  same family and is labeled as such, per the independence rule; it is not a substitute for
  cross-family review.
