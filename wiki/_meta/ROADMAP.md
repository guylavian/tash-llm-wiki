# Wiki Roadmap — successor plan (post Phase 0–5)

This is the live roadmap that succeeds `MIGRATION-litellm-langgraph.md` (whose Phase 0–5
LiteLLM/LangGraph migration **shipped 2026-06-25**) and `RAG-REPLACEMENT-PLAN.md`. It tracks what
is **done**, what is **in flight**, and the **next** work, across the multi-domain LLM-wiki.

---

## Done (shipped)

| Area | State |
|---|---|
| **Phases 0–5** (LiteLLM gateway, LangGraph QUERY/INGEST graphs, cost/budget, `lint --status` spend) | ✅ shipped 2026-06-25 |
| **Phase 5 routing lever** — 32B→7B via `litellm.Router` (OSS), `complete_routed()`, single-model degrade | ✅ |
| **Dense retrieval** (`embed.py` + RRF `--hybrid`), local LLM answer path (`wikikb ask`) | ✅ scaffolded + live under a venv/LM-Studio |
| **Faithfulness eval** (`quality/faithfulness.py` + probe + 19 cases) | ✅ |
| **TKG / Graphiti-Kuzu backend** | ✅ ON in the `keycloak-wiki` container (kuzu 0.11.3, raw-kuzu, no LLM); JSON store canonical on host |
| **4th domain — `openshift`** (Kubernetes + OpenShift) | ✅ corpus-backed: **3,813 reference notes** (1,602 k8s + 2,211 OCP 4.22) |
| **`adoc_to_corpus.py`** — AsciiDoc harvester (reusable for any RH docs repo) | ✅ new tool |

---

## In flight / next (prioritized)

### 1. Wire the openshift synthesis into its corpus (highest value) — ✅ graph-connected 2026-07-07
Done: 37 openshift pages (8 topics, 27 entities, 2 questions) now cite `kb:` tokens;
`crosslink --apply` + `tkg ingest` give **73 openshift Source nodes** (was 7) among 587 CITES
edges. Eval goldens regenerated (index tokens +155 mean, recall unchanged); selftest 50/50.
**Remaining:** keep growing the page count from 37 toward keycloak's ~178 as INGEST runs —
corpus citation coverage is still ~2% of 3,813 notes (the "what to write next" surface).

### 2. OCP version history 4.8 → 4.21 + known-issues tier
Only 4.22 is harvested. **Action:** re-run `adoc_to_corpus --version 4.<n> --append` per
`enterprise-4.<n>` branch for the minors you actually support; prioritize each branch's
`release_notes/` (the **known-issues history** the brain currently lacks — declare it as a
`support-kb`/`scenarios` tier in `tiers-covered` once ingested). Avoid harvesting all 15 minors in
full (≈95% duplicate; vault bloat) — version like keycloak (a few, newest wins via crosslink).

### 3. TKG/Kuzu hardening
- **Idempotent `--load`** — re-running appends edges (2,274 → 4,515 observed) because edges are
  `CREATE`d while the node `MERGE` is idempotent; `fresh=True` didn't fully clear on the mounted
  volume. **Action:** `DETACH DELETE`/drop-rel-table before reload, or upsert edges.
- **Host-side kuzu** — vendor the wheel offline (`pip download kuzu --only-binary=:all:` →
  `--no-index`) so `WIKI_TKG=kuzu` works on the host, not only in the container.
- Persist `WIKI_TKG=kuzu` in the container's compose env so the backend stays on across restarts.

### 4. Dense index for openshift
Build the embedding index over `reference/openshift/` so paraphrase queries recall (the notes-first
recall path, now also useful for the large OCP corpus). `embed.py` exists; just needs the model
vendored + index built for the new domain.

### 5. SRE agent surface (the RAG-replacement end goal)
`openshift-implementation-review` already carries a symptom→cause reverse index + `symptoms:`
frontmatter (CrashLoopBackOff / ImagePullBackOff / Pending / 503 / OOMKilled). **Action:** an agent
that turns an alert/`oc get co` Degraded signal into a cited probable-cause + fix via `wikikb ask`,
with the Confidence banner intact. Pairs with the existing `questions/` post-mortems.

---

## Standing invariants (do not regress)
- **Air-gap by default** — stdlib core; every optional tier (`embed`/`llm`/`cost`/graph/kuzu) is
  lazy-imported, default-off, and degrades to today's behavior when absent.
- **Citation contract + 5-arm Confidence gate** — never serve inference as fact.
- **Raw tiers immutable** — writes only under `topics/ entities/ questions/` and `_meta/`.
- **Adding a domain bumps the eval golden** (one extra router line ≈ +120 index tokens; recall
  unchanged) — regenerate `eval/baseline.eval*.out` and say so.
- Run `python3 _meta/tests/selftest.py` green (modulo known pre-existing content errors) before
  declaring a phase done.
