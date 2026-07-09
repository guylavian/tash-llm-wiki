# Plan — Graphify×Obsidian deepening + client PDF upload + correctness backlog

*Authored 2026-07-09 (Fable 5 orchestrator + 9-agent Sonnet workflow: 5 line-cited subsystem
readers → 3 designers → 1 adversarial critic). Adversarial pass was **same-family — NOT
independent** per the validation-independence standing rule; a different-family or human pass
is still required before any sign-off that cites this plan.*

---

## 0. What the request assumed vs. what already exists (verified)

| Ask | Reality (verified this session) |
|---|---|
| "Implement Graphify + Obsidian together" | **Already shipped 2026-07-07**: `GRAPHIFY-SYNC.md`, `sync-graph.sh`, `tkg/graphify_export.py`, `graphify-out/` (595 nodes · 2,655 edges · 23 Leiden communities). What's broken: the documented auto-sync **hook was never installed** (`git config core.hooksPath` → unset; `_meta/hooks/` doesn't exist) and both `GRAPHIFY-SYNC.md:60` and `sync-graph.sh:5` still say `wiki/_meta/hooks` — a **stale pre-flatten path**. `graphify-out/` is stale (built at `bd1aca7a`; HEAD is `ca228f7`). |
| "Enable clients to upload PDFs as wiki sources" | **The extractor already exists and is finished**: `_meta/wikikb/corpus/pdf_to_corpus.py` (pdftotext ladder, `.txt`-sibling sealed-box path, `<!-- p.N -->` page markers, `--chunk-pages`, loud skip of scanned PDFs, dry-run default). Registered in `__main__.py:23`, covered by selftest — but the file is **untracked, zero commit history**. What's missing is only the client-facing surface + pending-work visibility. |

If "graphifyy" meant **Graphiti** (Zep's temporal-KG library): its Kuzu backend was deliberately
**removed 2026-07-05** (upstream Kuzu archived; backend verified inert, zero consumers — see
CLAUDE.md `tkg/` section). Do not re-add it; the stdlib TKG JSON store is canonical and Graphify
is the graph-analytics layer on top.

Other facts the plan rests on (critic-verified, file:line):
- `serve.py` is **GET-only** (`do_GET` family only; traversal-safe `SLUG_RE` at serve.py:49). Its entire security model to date is "everything is read-only".
- The untracked root `Dockerfile` CMD binds **`0.0.0.0:8642`** by default (line 26) — the opposite of serve.py's loopback-by-default posture.
- On the live ask/serve/mcp path **only gate arm H1 fires** — `nodes.py:148-152`'s own docstring says `page_fm` is not threaded, so H2/H3/H4/Provisional can't trigger.
- Dense embedding indexes exist for keycloak / active-directory / cisco-ios-xe only — **no openshift** (`_meta/embeddings/`).
- `question_tier:` present on only **9/88** question pages; README.md:22 says "85" vs 88 actual.
- `manifest.py` `SRC_RE` (line 46) tracks `kb|guide|ref|web` only — no `note:`; no `_raw/` scan → a dropped-but-unprocessed PDF is invisible to `manifest status`.
- `selftest.py` `PKG_TOOLS` omits `adoc_to_corpus`; `build.py:1-8` docstring omits the `verify` step that `STEPS` (line 18-26) actually runs.

---

## Phase 1 — close the loop on what already exists (S; zero new surface; do first)

**1a. Install the Graphify auto-sync hook** *(Design A — critic verdict: sound)*
- New `_meta/hooks/post-commit` (~8 lines): run `sh _meta/sync-graph.sh` only when the commit
  touched `topics/ entities/ questions/`; use `git diff-tree --no-commit-id --name-only -r HEAD`
  (parent-free — safe on the first commit of a fresh clone, per critic fix #1); fork to
  background with a `# ponytail: fire-and-forget; sync.log may be truncated if the shell exits first`
  ceiling comment (critic fix #2).
- Operator step: `git config core.hooksPath _meta/hooks`.
- Fix the stale `wiki/_meta/hooks` path at `GRAPHIFY-SYNC.md:60` and `sync-graph.sh:5`.
- **Declined from Design A** (redundant/speculative — do not build): wiring `graphify-out/graph.json`
  into `expand`/`ask` (expand.py reads pages live with zero staleness; graph.json is a lossier,
  staler re-derivation), Bases-per-community views, canvas export, code-repo `merge-graphs` (no
  target repo today). Legitimate fast-follow, separate PR: betweenness/bridge surfacing in
  `lint --status` (new signal lint doesn't have).

**1b. Pending-PDF visibility in the manifest** *(Design B item (a) — the critic's "ship first")*
- ~25 lines in `manifest.py`: a `pending_raw_pdfs()` scan of `_sources/<domain>/_raw/pdfs/`
  comparing against `corpora/<domain>/index.jsonl` URLs (reuse `pdf_to_corpus.slugify` — import
  direction verified cycle-free), surfaced in `manifest status` and `lint --status`:
  `"3 PDFs dropped for <domain>, not yet harvested — run: python3 -m wikikb pdf_to_corpus …"`.
- Zero new state, pure read; reuses the drop-folder convention already documented
  (CLAUDE.md `_raw/` drop path; ADD-DOMAIN.md).

**1c. Hygiene commits**
- **Commit `pdf_to_corpus.py`** (it is load-bearing, dispatcher-registered, selftest-covered, and untracked).
- Add `adoc_to_corpus` to selftest `PKG_TOOLS`; fix `build.py` docstring (add `verify`);
  README 85→88 questions.
- Add a two-run `tkg ingest` idempotence assertion to selftest as a regression guard
  (replaces the audit's invalid "fix TKG --load doubling" item — that bug lives only in the
  **removed** Kuzu backend; `store.save_store()` overwrites wholesale by construction).

## Phase 2 — client PDF upload surface (M; new write surface — needs the full checklist)

*(Design B item (b) — critic verdict: right shape, ship only after the trust-boundary items land.)*

- **`PUT /upload/<domain>/<filename>` on serve.py — default OFF**, enabled only by explicit
  `--allow-upload`. Raw request body, one file per request (`curl -T guide.pdf …`).
  **Explicitly rejected:** multipart/form-data (stdlib has no parser since `cgi` removal in 3.13;
  hand-rolled MIME boundary parsing is a vuln class), any queue/DB machinery, auth subsystem,
  OCR dependency.
- Writes **only** into `_sources/<domain>/_raw/pdfs/` — never `reference/` or `corpora/` — so an
  upload is structurally incapable of touching the immutable tier; synthesis still requires the
  operator INGEST loop.
- Trust-boundary checklist (all mandatory):
  1. filename regex `^[A-Za-z0-9._-]+\.pdf$` (no `/`, no `..`); domain segment must be in
     `taxonomy.md` domains (cross-check `tags.load_domains()` values are kebab-case-matchable).
  2. `os.path.realpath` containment assertion of the resolved target under the vault root
     (defense-in-depth vs. planted symlinks) **before** `os.makedirs`/write.
  3. `O_CREAT|O_EXCL` — no overwrite, no races; collision → 409.
  4. size cap (default 50 MB) + `%PDF` magic-byte check on the first bytes.
  5. `do_PUT` defined **unconditionally**, gate checked inside, disabled → the **same 404 body**
     as an unknown GET path (defining it conditionally would leak a stdlib `501` fingerprint).
  6. selftest: (i) happy-path PUT lands in the staging folder; (ii) traversal/oversize/non-PDF
     rejected; (iii) **default-off returns byte-identical 404** to an unknown path.
- Dockerfile: document the `-v $(pwd):/wiki … --allow-upload` invocation; while touching it,
  reconsider the current `0.0.0.0` default bind (flag: the container default contradicts
  serve.py's loopback-by-default posture; at minimum document it as an explicit operator choice).
- OCR stance unchanged: scanned PDFs keep the loud skip; document `ocrmypdf` on a tooled box
  producing a `<stem>.txt` sibling, which the existing extraction ladder already prefers for free.
- End-to-end operator flow after this phase:
  `client PUTs pdf` → `manifest status` shows pending (Phase 1b) → operator:
  `pdf_to_corpus --apply` → `corpus_to_vault --apply` → `wikikb build` → INGEST synthesis session.

## Phase 3 — correctness backlog (audit Top-8, critic-adjusted, in build order)

1. **Thread `page_fm` into the live QUERY graph** so H2/H3/H4/Provisional actually fire on
   ask/serve/mcp (today only H1 does). Root cause per critic; mostly reuse: the frontmatter is
   already read per candidate — thread it into state and call the existing `lint.gate_banner()`.
   Verify with `gate_page_probe.py` + livebank; expect no golden bump (retrieval untouched) but confirm.
2. **Close the fabricated-citation class at answer time** (the one named still-open
   PRODUCTION_READINESS sign-off blocker) — follow-up to #1, scope the withhold-granularity
   decision explicitly before building.
3. **Openshift dense embedding index** — mechanical (`embed.py` exists; vendor model, build
   index for `reference/openshift/`), ROADMAP #4, biggest recall win for the 3,908-note corpus.
4. **Serve concurrency queue / threading posture** — urgent pairing with the Dockerfile
   `0.0.0.0` default; stdlib `ThreadingHTTPServer` is likely sufficient.
5. **`question_tier` backfill into `wikikb build`** — 9/88 pages carry it, so H1 lint
   enforcement is effectively opt-in today.
6. **Openshift synthesis grind** — 43 pages vs 3,813 notes (~1%); ongoing content work
   (ROADMAP #1), not a single fix; run as INGEST sessions.
7. OCP version-history/known-issues tier + SRE agent surface — deferred, unchanged from ROADMAP.

## Invariants (unchanged, binding on every phase)
Air-gap stdlib core, optional tiers lazy + default-off · raw tiers immutable · citation contract +
5-arm gate · eval-golden bumps deliberate and named · selftest green before a phase is "done" ·
max 3 concurrent subagents on this machine.
