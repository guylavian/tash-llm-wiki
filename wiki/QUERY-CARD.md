# QUERY protocol card (generated — edit CLAUDE.md, then `python3 -m wikikb card`)

**Budget directives (read first):**
- Retrieval is served in bounded slices (pages ≤ ~2k tokens/call; `next_offset` pages more).
- Watch `session_tokens_served` on every tool result: past the stop-line the result carries a
  `budget_directive` — obey it: STOP retrieving, answer from evidence already read.
- Search-first: `route` then `search`/`expand` snippets. Read `index.<domain>.md` ONLY when the
  router abstains; never read the global index on a confident route.
- Do NOT read CLAUDE.md for a QUERY — this card is the extracted QUERY contract. Read CLAUDE.md
  only for INGEST / ADD-DOMAIN / page-editing operations.

---
## Operation: QUERY

Goal: answer a question, and leave the wiki richer than you found it.

1. **Cheap pass first (route → tiered read).** Route the query to its **domain(s)**
   with `python3 -m wikikb route "<query>"` (keyword match against the per-domain
   `areas:` vocabulary in `taxonomy.md`). On a **confident single-domain** route, read
   **only** that `index.<domain>.md` and **skip the global `index.md`** — it saves the
   ~4.3k-token cross-domain router on most queries. When the router **abstains**
   (ambiguous / no signal, e.g. cross-domain or shared-vocabulary queries), fall back to
   reading the global `index.md` first, then the per-domain index. Either way, then read
   the `title:` + `summary:` (+ `tags:`) of candidate pages; loading one domain's
   summary-level index (not the whole multi-domain wiki) keeps query cost flat and fits a
   local model's context window. Only **open page bodies** when the cheap pass can't
   answer. (The router is conservative by design: a *confident* route is never wrong, so
   skipping the global index never costs recall — verify with `route.py --eval` and the
   `_meta/eval/` scoreboard.)
2. **Graph-expand the seed pages before reading raw (use the link graph you built).**
   The candidate pages from step 1 are *seeds*: each carries a generated `## Sources`
   block (`[[reference-note]]` links written by `crosslink.py`) and `[[page]]` wikilinks
   to neighbors. `python3 -m wikikb expand --domain <d> "<query>"` returns that 1-hop
   neighborhood **with no new search** — the **seed-source notes** (the seeds' own
   `## Sources`; tight, high-precision) plus the looser **1-hop closure** (neighbor
   pages' sources). Open those cited reference notes *directly* instead of re-searching:
   on a paraphrased/multi-hop query whose answer note shares little surface vocabulary
   (so lexical ranks it deep), the query still matches a *page that cites it*, and the
   graph hands you the note — recall up at near-zero added cost. This is a multi-hop
   *entry-point* fix; it does **not** help where the synthesized graph is thin (e.g. a
   notes-first domain whose pages cite `note:`/`web:` tokens `crosslink.py` can't resolve
   to a reference note) — that gap is the dense/embedding layer's job.
3. If the pages and their graph neighborhood are still thin, fall back to the **raw
   reference tier — which also lives in the vault** (RETRIEVAL fallback, cheap-first):
   grep `reference/<domain>/` (the full doc bodies, one Markdown note per source) for a
   corpus-backed domain, or `_sources/<domain>/` for a notes-first domain. **There
   is no separate corpus query tool** — Obsidian/the vault holds all the data, so
   ripgrep/grep over Markdown + reading the matched notes *is* the search (the gated
   pointers are in `reference/<domain>/_gated-kb-index.md` — cite the URL). **Optional
   dense accelerator:** when a query is a *paraphrase* whose answer note shares little
   surface vocabulary (lexical ranks it deep, the graph didn't cite it), and an embedding
   index has been built, `python3 -m wikikb kb --domain <d> search "…" --hybrid` fuses
   the lexical and dense rankings (RRF) to surface it. The dense layer is **optional and
   offline** (`embed.py` + a vendored model — see `_meta/models/README.md`); absent it,
   `--hybrid` silently falls back to lexical. This governs *when to read more*; it is
   independent of the citation contract in step 4, which applies to **every** answer even
   when the synthesized pages alone sufficed.
4. **Confidence gate → synthesize → cite.** First apply the **Confidence gate**
   (below) and **prepend a banner** if it trips — a synthesized page is
   *interpretation*, and amortization makes whatever was filed the cheap cache hit, so
   never serve inference as fact. Then synthesize, and cite each claim to its tier. Every answer
   MUST end with a **References** section in two separate groups:
   - **RH ground-truth (`kb:` / `guide:` / `ref:`)** — for each wiki page you
     used, resolve its frontmatter `sources:` back to the underlying kb/guide/ref
     records and list them as **id + title**. Surface these **even when the wiki
     already synthesizes the point** — at citation time the kb is the *provenance*
     of the answer, **not** a long-tail-only retrieval fallback. Resolving a
     page's `sources:` is cheap — you need not re-search the corpus.
   - **Wiki** — the `[[slug]]` pages used, plus their upstream **`web:`** sources
     (RFC / OWASP / IETF draft) carried in those pages' `sources:`.
   If the two tiers disagree, **flag it** (prefer RH ground-truth for support
   questions and note the upstream difference — see "Two source tiers").

   > **kb as RETRIEVAL (when to search) is cheap-first and optional; kb as
   > PROVENANCE (what to cite) is mandatory in the output.** Keep them distinct:
   > the cheap-first read path is unchanged, but the answer's provenance always
   > surfaces both tiers.

   **Three anti-fabrication rules (a citation must EARN its place):**
   - **Verify content, not just existence.** Before citing `kb:X`/`ref:X` for a
     *specific* technical claim (an env var, flag, error code, default value), confirm
     that note actually *contains* it — resolving the token to an existing note is not
     enough. A real note cited for a claim it never makes is a **fabricated citation**
     (the `SSO_HTTPS_CIPHER_SUITES` failure). `lint.py`'s **citation-grounding** check
     is the backstop; don't rely on it — a distinctive claim you can't ground in a
     read source must be tagged `(inferred)` or dropped.
   - **Lead diagnostics with the observed signal.** For a break-fix/symptom question,
     the *first* step is to read the actual error string / log line / metric — it
     disambiguates the hypotheses. Never present one hypothesis as the confirmed root
     cause when the user hasn't shared the discriminating evidence; give the ranked
     hypotheses and the one observation that chooses between them.
   - **Break-fix over a conceptual-only tier ⇒ banner + `status: draft`.** When the
     question is `support-kb`/`scenarios` (an upgrade broke X, a known issue) but the
     routed domain's `tiers-covered:` is `conceptual` only, the answer is synthesis,
     not a confirmed fix — fire the **H1 out-of-coverage banner** and never file it
     `status: reviewed`.
5. **File the answer back**: create `questions/<slug>.md` with the question, the
   answer (**including the two-group References section**), and links into
   supporting pages. If answering surfaced a reusable fact, also run a
   mini-INGEST to capture it as an entity/topic.

### Confidence gate — never serve inference as fact

A synthesized page is *interpretation*, not raw truth, and **amortization makes whatever
was filed the cheap cache hit** — served fast, with provenance, *forever*. Before
returning a QUERY answer, run this **deterministic checklist** — compute every input; do
**not** rely on the page's self-description.

**Inputs** (per page used; provenance from the flat `provenance_*` keys):
`q_tier` = the question's tier-class (`conceptual` | `support-kb` | `scenarios`) ·
`covered` = the routed domain's `tiers-covered:` (`_meta/taxonomy.md`) ·
`extracted` = `provenance_extracted` (0 if absent) · `inferred` = `provenance_inferred` ·
`status`.

**Fire the banner if ANY high-precision arm is true — each fires ALONE, ignoring `status`:**
- **H1 — out of coverage:** `q_tier ∉ covered`.  *(verified: `_meta/tests/gate_probe.py`)*
- **H2 — ungrounded:** `extracted == 0`.  *(enforced: `lint.py`; verified: `gate_page_probe.py`)*
- **H3 — incoherent review:** `status == reviewed` **AND** `inferred ≥ extracted`.  *(enforced: `lint.py`)*
- **H4 — explicit:** `status == needs-review`.

**Else fire `Provisional` only IN COMBINATION (low-precision — never alone):**
`status ≠ reviewed` **AND** (`inferred ≥ extracted` **OR** the load-bearing claim is inline `(inferred)`/`(ambiguous)`).

**`status` is ADDITIVE-ONLY.** It may *raise* a banner (H3/H4/L); it must **NEVER
suppress** one. A page cannot earn silence by self-tagging `status: reviewed` — H1 and H2
ignore `status` entirely. (This was the exact bug the ISSU page exploited: `extracted: 0`
+ self-`reviewed` slipped past the old `status ≠ reviewed` conjunction.)

**Do NOT fire on a lone weak signal:** a `draft` page with `extracted > 0` **and**
`inferred < extracted` in a covered tier; a single non-load-bearing `(inferred)` bullet.

**Banners.** H1 → *⚠️ Out of corpus coverage — `<domain>` holds `<covered>` only; this is
a `<q_tier>` question and that tier is not ingested; verify against the primary source.*
· H2/H3 → *⚠️ Ungrounded / incoherent provenance — this answer rests on synthesis, not
extracted sources; weigh the References.* · H4/L → *⚠️ Provisional.*

**When filing back (step 5):** never file `status: reviewed` with `extracted == 0` or
`inferred ≥ extracted` (`lint.py` makes this a hard error). **Do not hand-patch a page to
silence the banner** — fix the *coverage* (ingest the missing tier via the `_raw/` drop
path → INGEST); the banner clears because its cause did. Build the mechanism; let the
page be its first catch.

### Query answering protocol (mandatory for every wiki-query answer)

This per-answer contract applies to **every** question answered through the QUERY
operation / `wiki-query` skill, regardless of phrasing or model confidence. It extends
(never replaces) the two-group References contract, the anti-fabrication rules, and the
Confidence gate above.

1. **Search first, never complete from memory.** Even when the answer seems obvious,
   grep the reference tier and read the relevant config/migration/deprecated notes
   before writing anything. If the term/command/variable in question doesn't appear
   anywhere in the corpus, **"it doesn't exist" is a valid and complete answer** — not
   a reason to guess.
2. **Derive the reasoning, don't stop at a single fact.** If the answer is "X doesn't
   exist" or "X behaves this way," explain *why* — naming convention, a relevant
   deprecated-file entry, a migration-changes note. An answer without structural
   justification is a confident-sounding guess.
3. **Distinguish what was asked from the actual correct approach.** If the question
   embeds a false premise (a non-existent env var, a removed flag, outdated syntax),
   don't just say "that doesn't work" — give the actual correct way to achieve what
   the user was likely trying to do.
4. **Cite at line granularity, not document granularity.** Every factual claim gets an
   exact citation (`filename.md:XXX-YYY`), never a vague "per the docs." If sources
   conflict or differ by version, state both with their respective versions. (The
   answer still ends with the two-group References section — line cites are in-body,
   References is the roll-up.)
5. **Tag provenance explicitly on every claim** — `extracted` (directly quoted from a
   source) vs `(inferred)` (your own derivation from multiple sources/principles, not
   a direct quote — the same inline tag defined under "Per-claim provenance"). Any
   inferred claim must be flagged in the chat summary as a reasonable inference, not
   confirmed fact, so the user can request further verification if it's load-bearing.
6. **File the answer back as a `questions/<slug>.md` page** (not just a chat reply),
   with full frontmatter: title, slug, summary, sources, provenance counts,
   `question_tier:`, `status:` (**default `draft`** — only promote to `reviewed` after
   independent verification; the gate's filing rules above still bind), and `updated:`.
   Link relevant existing pages with `[[slug]]`.
7. **End with a short chat summary**: the answer in 1–2 lines, where the page was
   filed, and which citations support it — so the user doesn't need to open the file
   to know if it's trustworthy.

If the search genuinely yields no clear answer after real effort, say so explicitly
("not found in corpus — here's my best-effort hypothesis and why") rather than
presenting a guess as settled fact.

**Scope: this protocol is domain-agnostic.** It binds for EVERY domain declared in
`_meta/taxonomy.md` (keycloak, openshift/kubernetes, active-directory, cisco-ios-xe, and
any domain added later via ADD DOMAIN). A query is never exempt because its domain has a
sibling skill, its corpus lives in a different `reference/<domain>/` tree, or the answer
"seems general knowledge." If a question touches a wiki domain, the protocol is active.

#### Final self-check (blocking — run before presenting ANY answer as complete)

This is not a suggestion; it is a gate. If any item fails, the answer is NOT final —
go back and complete the missing step first, then respond.

- [ ] Did I file a question page under `wiki/questions/` with full frontmatter
      (title, slug, summary, sources, provenance counts, `status: draft`, date)?
      If not, do it now before responding.
- [ ] Does every distinct factual claim in my answer have its OWN citation with a
      specific line range — not one broad range covering multiple claims?
- [ ] Did I tag each claim as extracted or `(inferred)`, and did I flag inferred
      claims explicitly in the chat summary (not just in the filed page)?
- [ ] Did I check whether the official/vendor documentation contains any explicit
      warning, caveat, or "don't do this" note related to the exact
      configuration/command in the question — not just the mechanical behavior, but
      the surrounding guidance? If the corpus has a warnings/best-practices/caveats
      section for this topic, it must be checked and surfaced if relevant.
- [ ] If any of the above is not satisfied, do NOT present the answer as final —
      go back and complete the missing step first.

**The answer-producing layer owns this gate (multi-skill / subagent cases).** When a
question matches several skills at once, or the research is delegated to a subagent
(Explore/general-purpose dispatch), the protocol is NOT discharged by a sub-step having
touched the wiki — **whichever layer writes the user-facing answer runs the Final
self-check.** Two binding rules:
- **Research subagents return protocol-grade findings**: instruct them to carry
  per-claim `file.md:line` citations and extracted/`(inferred)` tags in their returned
  text.
- **Synthesis preserves, never compresses**: the final synthesis must keep the
  subagent's line-level citations and provenance tags claim-by-claim — compressing
  granular citations to file-level or dropping tags is a protocol violation even when
  the underlying research was correct.

### Validation independence — standing rule

Adopted 2026-07-05 after the independent audit. These are process constraints, not
one-time fixes:
- **No same-family adversarial pass counts as independent.** The adversarial
  reviewer must not be the implementer's model family; where a different family is
  unavailable (air-gapped box: local Ollama models, or a human), the pass must be
  labeled "same-family — NOT independent" in any sign-off it feeds.
- **No self-adjudication.** A contested finding is decided by an uninvolved third
  party (different family, or a documented human review) — never by the
  system's architect/builder.
- **Acceptance banks are blind and frozen.** Questions are authored without
  visibility into current failure modes, committed to git BEFORE the first run, and
  never edited after seeing results. Grading runs on the served **answer text** —
  a case whose answer surface cannot contain the fact (extractive fallback) is
  UNGRADED, never a pass. No retrieval/serving change may be tuned against the same
  bank that reports its acceptance number.

<!-- source-digest: dac326129ff2ba57 -->
