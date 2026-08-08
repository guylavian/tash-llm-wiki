# Tutorial — Add a new technology "brain" (domain) from zero to hero

This is the **hands-on, end-to-end walkthrough** for onboarding a new technology
domain into the vault. The canonical definition of the operation lives in
[`../CLAUDE.md`](../CLAUDE.md) → **Operation: ADD DOMAIN**; this file is the
copy-paste tutorial that doesn't drift from it. Worked against the two real
examples we shipped: **Active Directory** (notes-first → corpus-backed) and
**Cisco IOS XE** (notes-first).

> **What you'll build.** A new, independently-queryable "brain" inside the same
> Obsidian vault: its own raw tier, its own routing index, its own review lens,
> all sharing one tag/area vocabulary and one set of stdlib tools. Nothing about
> the existing brains (keycloak, active-directory, cisco-ios-xe) changes.

---

## The 60-second mental model

The vault has **three layers** (see `../CLAUDE.md`):

| Layer | Location | Mutability | Your job |
|---|---|---|---|
| **Raw sources** | `vault/reference/<domain>/` (folded corpus) · `vault/_sources/<domain>/` (hand notes) · `../references/` | **IMMUTABLE** — never edit | create once, then freeze |
| **Synthesis** | `topics/` · `entities/` · `questions/` | LLM-maintained | this is where you write |
| **Schema** | `CLAUDE.md` + `vault/taxonomy.md` | human + LLM | declare the domain here |

**Hard rule — writes go *only* under `wiki/{topics,entities,questions}/` and
`wiki/_meta/`.** Never edit `vault/reference/<domain>/`, `vault/_sources/<domain>/`, or
`../references/` — they are immutable and integrity-locked (`_meta/reference.lock.json`,
sha256 per note). All tooling is **stdlib-only and offline**; the *one* optional
third-party dependency is the local embedding layer (`embed.py`), which degrades
gracefully to lexical search when absent.

Adding a brain is six steps: **(1) declare it → (2) give it areas → (3) give it a
raw tier → (4) seed three synthesis pages → (5) wire the graph + indexes → (6)
lint until green.** Then you grow it with INGEST / QUERY.

---

## Prerequisites

- You're working inside the vault root (`wiki/`) — the directory you open in Obsidian.
- `python3` (stdlib only — no `pip install` needed for the core path).
- Know your **sources** for the new tech: either a harvestable doc corpus
  (corpus-backed) or the knowledge you'll hand-author (notes-first).
- Read `../CLAUDE.md` once. This tutorial is the executable version of its
  *Operation: ADD DOMAIN*.

---

## Step 0 — Decide the shape

| Shape | When | Raw tier | Source tokens |
|---|---|---|---|
| **notes-first** | No harvestable corpus — you author the ground truth (Cisco IOS XE, Windows Server, SCCM) | `_sources/<domain>/*.md` (immutable once written) | `note:` + `web:` |
| **corpus-backed** | You have a doc corpus to freeze (Red Hat docs, MicrosoftDocs Markdown) | `reference/<domain>/*.md` (folded in by `corpus_to_vault.py`) | `kb:`/`guide:`/`ref:` + `web:` |

**Rule of thumb:** notes-first is the default. Start notes-first; you can *promote*
to corpus-backed later if a harvestable source appears (that's exactly the AD path —
seeded notes-first against Microsoft Learn, then folded in the `windowsserverdocs`
Markdown tree).

> The shape only changes the **raw tier and the source tokens**. Steps 1, 2, 4, 5,
> 6 are identical for both.

---

## Step 1 — Register the domain in `taxonomy.md` (the load-bearing step)

Edit `vault/taxonomy.md`. Copy the `<!-- Template -->` block under `## Domains` and
fill it in. This is the single most important step: **three tools parse these exact
lines.**

```markdown
### <domain>
- domain: <domain>                  # kebab-case, globally unique
- areas: [area-a, area-b, security, troubleshooting]
- shape: notes-first                # or corpus-backed
- sources: [vault/_sources/<domain>/]     # + corpora/<domain>/ if corpus-backed
- review-moc: <domain>-implementation-review
- tiers-covered: [conceptual]       # coarse knowledge-tiers ingested: conceptual | support-kb | scenarios
```

> **Don't skip `tiers-covered:`.** It is the coverage axis the QUERY **Confidence
> gate** reads (arm H1): if a question's tier isn't in this list, the answer is
> banner-flagged *Out of corpus coverage*. A new notes-first brain almost always
> starts `[conceptual]` only — declare that honestly rather than over-claiming.

Why it's load-bearing:
- **`lint.py`** validates every page's `domain:` against the `- domain:` lines here
  (an undeclared domain is flagged).
- **`index.py`** builds `index.<domain>.md` *only* for declared domains
  (`DOMAIN_RE` parses `- domain: <name>`; the `<placeholder>` template is skipped,
  so it stays inert).
- **`route.py`** builds that domain's router profile from its `areas:` + descriptions.

## Step 2 — Add any new `areas:` to the shared vocabulary

`## Areas` in `taxonomy.md` is a **flat union across all domains**; a domain's
`areas:` must be a subset of it. A genuinely new technology contributes several new
area tokens. Add each as a backticked token **with a one-line gloss** (the gloss
feeds `route.py`'s keyword profile — write it with the words a user would actually
query):

```markdown
- `routing-protocols` — dynamic IP routing: OSPF, BGP, EIGRP — adjacencies, metrics, path selection
- `lan-switching` — VLANs, 802.1Q trunking, inter-VLAN routing, access/trunk ports
```

Reuse the generic areas (`security`, `troubleshooting`, `users`, `migration`) where
they fit, rather than minting near-duplicates.

## Step 3 — Create the raw tier

### Notes-first

```bash
mkdir -p _sources/<domain>
```

Add a `README.md` declaring **these notes ARE the immutable ground truth** (copy
`_sources/cisco-ios-xe/README.md` or `_sources/active-directory/README.md`). Then
write notes — **one file per concept** — each recording its source (a `web:` URL +
fetch date, or a lab/ticket observation) and the load-bearing facts, **paraphrased**
(no long verbatim excerpts — provenance, not transcripts; copyright + the
"distill, don't copy" rule).

### Corpus-backed (the "give me *all* the docs" path)

For a DocFX/Markdown docs repo (e.g. `MicrosoftDocs/windowsserverdocs`), clone on a
networked machine, drop the relevant subtree into `_sources/<domain>/_raw/`, then run
two stdlib commands **offline**:

```bash
# docs tree -> corpus (index.jsonl + body files); derives the live source URLs
python3 -m wikikb docs_to_corpus --src vault/_sources/<domain>/_raw/<subtree> \
    --domain <domain> --apply

# corpus -> immutable in-vault reference notes (+ writes the integrity lock)
python3 -m wikikb corpus_to_vault --domain <domain> --apply
```

`corpus_to_vault.py` writes one note per source under `vault/reference/<domain>/` (body
present) or one pointer row in `_gated-kb-index.md` (gated body), and records a
sha256 per note in `_meta/reference.lock.json` so any later hand-edit is detectable
(`--verify`). After folding in, **flip `shape:` to `corpus-backed`** in
`taxonomy.md` and add `corpora/<domain>/` to its `sources:`.

> **PDF sources:** a *bulk PDF doc set* (vendor manuals, product guides) now has a
> first-class corpus path — `python3 -m wikikb pdf_to_corpus --src <folder-of-pdfs>
> --domain <d> --apply` (pdftotext extraction, `<!-- p.N -->` page markers for
> page-level citation, `--chunk-pages` for big books, pre-extracted `.txt` accepted
> for sealed boxes) → then `corpus_to_vault` as above. But a *judgment-heavy* PDF
> (a CIS/STIG benchmark you'd paraphrase anyway) is still better distilled into
> `vault/_sources/<domain>/` notes. Either way, keep product families separate — the
> Cisco WLC AireOS PDF was *not* folded into `cisco-ios-xe` because it's a
> different product family; it belongs in its own domain.

## Step 4 — Seed the synthesis (the minimum viable brain)

Write **three pages** so the brain is navigable and lintable. Every page carries the
full frontmatter contract:

```markdown
---
title: Human-readable title
type: topic | entity | question
domain: <domain>                 # REQUIRED — must match taxonomy.md
slug: kebab-case-matching-filename
summary: 1–2 sentence gist — read before the body   # REQUIRED (the tiered-query surface)
sources:                         # REQUIRED provenance
  - note:vault/_sources/<domain>/<file>.md      # notes-first
  - web:https://… (label, fetched 2026-06-18)
provenance:                      # REQUIRED — assign by READING each claim vs its source
  extracted: 7                   #   (never count bullets mechanically)
  inferred: 1
  ambiguous: 0
tags: [area-a, concept]          # from taxonomy.md ## Areas / ## Kinds
status: stub | draft | reviewed
updated: 2026-06-18              # ISO; use the date in session context
---

# Title

**One-line definition.**

## Body
Synthesis. Cross-link with [[slug]] (bare slug, no path, no .md).
Tag synthesis the LLM assembled across sources inline: `… (inferred).`

## See also
- [[related-slug]]
```

The three seed pages:

1. **Overview topic** — the spine. `topics/<domain>-overview.md`.
2. **The first entity** it links — `entities/<some-concept>.md`.
3. **The review MOC** named in Step 1's `review-moc:` —
   `topics/<domain>-implementation-review.md`. Copy the shape from
   `topics/sso-implementation-review.md` or `topics/cisco-ios-xe-implementation-review.md`:
   a **rule → anti-pattern → symptom** checklist plus a **symptom → likely-cause
   reverse index** (this is the lookup surface a future SRE/agent uses to turn an
   alert into a cause page; pair it with the optional `symptoms:` frontmatter field).

Slugs are kebab-case and **globally unique across `topics/` + `entities/`**. A
`[[slug]]` whose page doesn't exist yet is allowed — it's a `[[wanted]]` TODO marker,
not an error.

## Step 5 — Wire the graph + generate indexes

```bash
python3 -m wikikb crosslink --apply    # synthesis -> corpus graph edges (## Sources)
python3 -m wikikb index                # writes index.<domain>.md + updates the global router
```

- **`crosslink.py`** resolves each page's `kb:` source tokens to the matching
  `vault/reference/<domain>/` note and appends a generated `## Sources` block of
  `[[doc-id|Title]]` wikilinks — **these are the edges that connect your synthesis
  to the corpus in Obsidian's graph** (and the edges `expand.py` later walks for
  multi-hop retrieval). It's idempotent and never touches your `sources:` block.
  *Note:* it only resolves `kb:` tokens — a **notes-first** domain (`note:`/`web:`)
  gets no synthesis→corpus edges, so its graph is built from inline `[[slug]]` links
  alone. (That's a known limitation, not a mistake — see "Known seams" below.)
- **`index.py`** writes `index.<domain>.md` (titles + summaries only, never bodies)
  and regenerates the `index.md` global router block. The reference tier is
  **counted, not page-listed** (a generated `[[_ref-<domain>|N reference notes]]`
  hub keeps every corpus note graph-connected without polluting the page index).

## Step 6 — Lint and verify

```bash
python3 -m wikikb lint            # health check (add --strict to fail on errors)
python3 _meta/tests/selftest.py        # end-to-end smoke test (optional but recommended)
```

A **healthy new brain** looks like the cisco-ios-xe run:

- `wrote index.<domain>.md (N pages)` and the global `index.md` router gains a line
  like `- [<domain>](index.<domain>.md) — N pages · review lens [[<domain>-implementation-review]]`.
- **No orphans, no broken links, no missing-frontmatter/sources errors.**
- The *only* expected findings are: intentional `[[wanted]]` TODO markers (pages you
  deliberately left for later), and the review-MOC's `inferred >= extracted` drift
  warning — expected, because a MOC is pure synthesis (the sibling
  `sso-implementation-review` shows the same warning).

> **Provenance gate.** Once you set a page to `status: reviewed`, bad provenance
> (`needs-review`, or `inferred >= extracted`) becomes a **hard ERROR** under
> `lint.py --strict`. Keep synthesis-heavy pages at `status: draft` until a human/LLM
> pass has verified each claim against the raw layer.

## Step 7 — Record what you ingest

As you fold in real sources, record them so INGEST stays incremental:

```bash
python3 -m wikikb manifest record note:vault/_sources/<domain>/<file>.md --pages <slug,...>
# corpus-backed:
python3 -m wikikb manifest record kb:7032207 --pages <slug-a,slug-b>
```

---

## Worked example, end to end — `cisco-ios-xe` (notes-first)

The exact sequence we ran to add the third brain (13 synthesis pages from 4 IOS XE
config guides):

```bash
# 1–2. taxonomy.md: added the ### cisco-ios-xe block + 5 new areas
#      (routing-protocols, ip-routing, lan-switching, spanning-tree, etherchannel)

# 3. raw tier (notes-first): README + one paraphrased note per guide
mkdir -p _sources/cisco-ios-xe
#   _sources/cisco-ios-xe/{README,ospf-routing,bgp-routing,
#                          protocol-independent-routing,lan-switching}.md

# 4. seed synthesis: overview + 11 entities + the review MOC
#   topics/cisco-ios-xe-overview.md
#   topics/cisco-ios-xe-implementation-review.md     (rule→anti-pattern→symptom + reverse index)
#   entities/{ospf,bgp,bgp-path-attributes,bgp-route-reflector,
#             cisco-administrative-distance,static-and-default-routes,
#             route-redistribution-and-route-maps,policy-based-routing,
#             vlans-and-trunking,spanning-tree-protocol,etherchannel}.md

# 5. wire + index
python3 -m wikikb crosslink --apply     # (no-op for notes-first: note:/web: don't resolve)
python3 -m wikikb index                 # -> wrote index.cisco-ios-xe.md (13 pages)

# 6. verify
python3 -m wikikb lint --strict         # rc=0; only [[wanted]] + MOC drift findings
python3 _meta/tests/selftest.py              # 11/11

# 7. record
python3 -m wikikb manifest record note:_sources/cisco-ios-xe/ospf-routing.md \
    --pages cisco-ios-xe-overview,ospf
```

Result: a fully queryable brain. `route.py "ospf neighbor stuck in exstart"` →
confident `cisco-ios-xe`; the query reads only `index.cisco-ios-xe.md`, lands on
`[[ospf]]` / the review MOC's reverse index, and answers.

---

## Worked example, end to end — `openshift` (notes-first, corpus-backable)

The fourth brain (Kubernetes-based OpenShift), added 2026-06-25. Goal: stand it up like
keycloak, with a clear promotion path to the full harvested corpus.

```bash
# 1. taxonomy.md ## Domains: added the ### openshift block
#      areas: [workloads, cluster-networking, cluster-storage, operators-olm,
#              builds-images, cluster-auth, observability, security, troubleshooting, migration]
#      shape: notes-first   tiers-covered: [conceptual]   review-moc: openshift-implementation-review
# 2. taxonomy.md ## Areas: added 6 new area tokens (workloads … cluster-auth) with glosses

# 3. raw tier (notes-first): README + 4 paraphrased concept notes
mkdir -p _sources/openshift
#   _sources/openshift/{README,kubernetes-workloads,kubernetes-networking,
#                       kubernetes-storage,openshift-platform}.md

# 4. seed synthesis: overview + 4 entities + the review MOC
#   topics/openshift-overview.md
#   topics/openshift-implementation-review.md     (rule→anti-pattern→symptom + reverse index;
#                                                  symptoms: CrashLoopBackOff/ImagePullBackOff/Pending/503)
#   entities/{kubernetes-pod,kubernetes-service,openshift-route,security-context-constraints}.md

# 5. wire + index
python3 -m wikikb crosslink --apply     # (no-op for notes-first: note:/web: don't resolve to kb)
python3 -m wikikb index                 # -> wrote index.openshift.md (6 pages) + router line

# 6. verify  (regenerate the eval goldens — a new domain adds one router line, so the
#    per-query index-token proxy ticks up ~119 tok; RECALL is unchanged, this is a baseline bump)
python3 -m wikikb evaluate         > eval/baseline.eval.out
python3 -m wikikb evaluate --route > eval/baseline.eval.route.out
python3 -m wikikb evaluate --graph > eval/baseline.eval.graph.out
python3 _meta/tests/selftest.py         # only intentional [[wanted]] + MOC drift on openshift

# 7. record (note: tier — manifest tracks kb:/web:, not note:, so record what applies)
```

> **The notes-first retrieval reality (verified by self-test).** `wikikb ask
> --domain openshift` returns **no candidates** — the deterministic `ask`/`kb.search`
> graph searches `vault/reference/<domain>/` (the corpus tier) ONLY, which a notes-first
> domain doesn't have. The working query path is the host-runtime one: **route →
> read `index.openshift.md` → grep `_sources/openshift/` + the synthesis pages**, OR
> build the optional dense/embedding index. This is the documented notes-first limit
> (see *Known seams*) — promoting to corpus-backed (below) lights up the `ask` graph.

**Promoted to corpus-backed — the "all the docs like keycloak" harvest (DONE 2026-06-26).**
The openshift brain now carries **3,813 real doc bodies** in `reference/openshift/`:

```bash
# --- Kubernetes: Hugo MARKDOWN -> docs_to_corpus (the existing Markdown harvester) ---
git clone --depth 1 --filter=blob:none --sparse https://github.com/kubernetes/website.git
( cd website && git sparse-checkout set content/en/docs )            # 1,669 .md
cp -R website/content/en/docs _sources/openshift/_raw/docs
python3 -m wikikb docs_to_corpus --src _sources/openshift/_raw/docs \
    --domain openshift --url-base https://kubernetes.io --apply       # -> 1,602 records

# --- OpenShift: ASCIIDOC -> adoc_to_corpus (NEW harvester; resolves include:: inline) ---
git clone --depth 1 -b enterprise-4.22 https://github.com/openshift/openshift-docs.git
python3 -m wikikb adoc_to_corpus --src openshift-docs \
    --domain openshift --version 4.22 --append --apply                # -> +2,211 assemblies

# --- fold the combined corpus into immutable reference notes + integrity lock ---
python3 -m wikikb corpus_to_vault --domain openshift --apply          # -> 3,813 reference notes
#   flip shape: corpus-backed in taxonomy.md; crosslink --apply; index; regenerate eval goldens.
```

> **`adoc_to_corpus.py` (new, reusable for any Red Hat AsciiDoc docs repo).** The
> Markdown `docs_to_corpus` can't parse AsciiDoc; `adoc_to_corpus` walks the book dirs,
> treats each **assembly** (`= Title` page) as one record, **resolves its `include::modules/*.adoc[]`
> inline** so the body is the complete published page (not a fragment), lightly de-AsciiDocs
> the text (drops `ifdef`/attr-entries, flattens `xref:`/`link:`), and derives the
> docs.redhat.com URL. Emits the same `corpora/<domain>/index.jsonl` + `bodies/` the proven
> `corpus_to_vault` consumes. `--append` preserves an existing (e.g. Kubernetes) index.
>
> **Versions (4.8 → 4.22) and known-issues history** are an incremental **re-run per branch**:
> `git clone -b enterprise-4.<n>` then `adoc_to_corpus … --version 4.<n> --append --apply`. We
> harvested **4.22** (current) deliberately rather than all 15 minors — full multi-version bodies
> are ~95% near-duplicate and would bloat the vault to 100k+ notes; keycloak likewise keeps only a
> few RHBK versions and lets `crosslink` resolve `kb:` tokens to the newest. The OCP `release_notes`
> assemblies carry the per-version known-issues history when you do want a specific older minor.

---

## Grow it — the INGEST / QUERY loop

From here the brain grows through the normal ops in `../CLAUDE.md`:

- **INGEST** — `manifest.py status` (what's new/changed) → write/update pages →
  `crosslink.py --apply` → `index.py` → `lint.py` → `manifest.py record`.
- **QUERY** — `route.py "<q>"` (route to domain) → read `index.<domain>.md` +
  candidate summaries → `expand.py --domain <d> "<q>"` (1-hop graph neighborhood) →
  open bodies / grep `vault/reference/<domain>/` (or `_sources/`) only when needed →
  synthesize with the two-group References section → file the answer to
  `questions/<slug>.md` so the wiki compounds.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `lint.py`: "domain `<x>` not declared" | Page `domain:` doesn't match a `- domain:` line | Add/fix the `### <domain>` block in `taxonomy.md` (Step 1) |
| `index.py` doesn't create `index.<domain>.md` | Domain not declared, or the block is still the `<placeholder>` template | Fill the template with a real kebab-case slug |
| `lint.py`: tag `<t>` not in vocabulary | Used a `tags:` value not in `## Areas`/`## Kinds` | Add the token to `taxonomy.md`, or use an existing one |
| Reviewed page errors on provenance | `status: reviewed` + `inferred >= extracted` or `needs-review` | Lower to `status: draft`, or verify claims and fix the counts |
| New page flagged as orphan | Nothing links to it and the index doesn't list it | Add an inline `[[slug]]` from a related page; re-run `index.py` |
| `corpus_to_vault.py --verify` fails | A supposedly-immutable `reference/` note was hand-edited | Restore it; never edit the raw tier |
| Graph adds no retrieval lift for a notes-first domain | `crosslink.py` resolves only `kb:` tokens, so `## Sources` is empty | Expected. The dense layer (`embed.py`) is the recall path for notes-first domains |

---

## Known seams (be aware of these)

These are real tooling gaps surfaced by code review — none blocks adding a domain,
but know them:

- **`manifest.py` doesn't track the `note:` tier** (its `SRC_RE` matches only
  `kb:`/`guide:`/`ref:`/`web:`). So a pure notes-first domain's `note:` sources can't
  yet be marked "ingested" by `manifest.py status`. Record what you can; don't be
  surprised when notes-first sources don't show in the manifest tally.
- **`crosslink.py` only wires `kb:` → reference-note edges.** Notes-first domains
  (`note:`/`web:`) get no synthesis→corpus graph edges, so their multi-hop retrieval
  rescue is structurally weaker — the dense/embedding layer is their recall path.
- **`lint.py`'s link regex ignores the aliased `[[slug|Title]]` form** that
  `crosslink.py` itself writes, so generated `## Sources` edges don't count toward
  the linter's orphan/backlink accounting (handled separately via the `_ref-*` hubs).

---

## Per-tech quick checklist

- [ ] Shape chosen (notes-first vs corpus-backed)
- [ ] `### <domain>` block added under `## Domains` in `vault/taxonomy.md`
- [ ] New `areas:` added to `## Areas` (with one-line glosses)
- [ ] Raw tier created (`vault/_sources/<domain>/` + README, or `vault/reference/<domain>/`)
- [ ] Overview topic + first entity + `<domain>-implementation-review` MOC written
- [ ] `crosslink.py --apply` run (corpus-backed) → `index.py` → `index.<domain>.md` + router updated
- [ ] `lint.py --strict` clean (only intentional wanted-pages / MOC drift)
- [ ] Sources recorded in the manifest as they're ingested
