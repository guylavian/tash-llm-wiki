# Tutorial — Add a new technology "brain" (domain) to the wiki

This is the **hands-on, per-tech checklist** for onboarding a new technology domain
into the vault, worked through with the real example we used to add **Active
Directory**. The canonical definition of the operation lives in
[`../CLAUDE.md`](../CLAUDE.md) → **Operation: ADD DOMAIN**; this file is the
copy-paste walkthrough that doesn't drift from it.

> **Mental model.** Each domain is an independent "brain" sharing one Obsidian
> vault, one set of tools, and one tag/area vocabulary. A page belongs to a brain
> via its `domain:` frontmatter. Adding a brain = (1) declare it, (2) give it a raw
> tier, (3) seed its synthesis, (4) regenerate + lint. Nothing about the keycloak
> brain changes.

---

## 0. Decide the shape

| Shape | When | Raw tier | Source tokens |
|---|---|---|---|
| **notes-first** | No offline corpus to harvest — you author the ground truth (Active Directory, Windows Server, SCCM) | `_sources/<domain>/*.md` (immutable once written) | `note:` + `web:` |
| **corpus-backed** | You have a harvestable doc corpus to freeze | `reference/<domain>/*.md` (folded in by `corpus_to_vault.py`) | `kb:`/`guide:`/`ref:` + `web:` |

Active Directory → **notes-first** (no Red Hat-style support corpus; the authority
is Microsoft Learn + lab/operational knowledge, which we paraphrase into notes).

---

## 1. Register the domain (the load-bearing step)

Edit `_meta/taxonomy.md`. Copy the `<!-- Template -->` block under `## Domains` and
fill it in. What we added for AD:

```markdown
### active-directory
- domain: active-directory
- areas: [directory-services, replication, group-policy, ad-dns, fsmo, trusts, sites-topology, ad-certificate-services, ad-authn, users, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/active-directory/]
- review-moc: active-directory-implementation-review
```

Why this matters: `lint.py` validates every page's `domain:` against the
`- domain:` lines here (an undeclared domain is a warning), and `index.py` builds
`index.<domain>.md` only for declared domains. The kebab-only parser ignores the
`<placeholder>` tokens, so the commented template never registers as a real domain.

## 2. Add new areas to the shared vocabulary

`## Areas` is a **flat union** across all domains; a domain's `areas:` must be a
subset of it. A new technology almost always contributes new area tokens. We added
nine AD-specific areas (`directory-services`, `replication`, `group-policy`,
`ad-dns`, `fsmo`, `trusts`, `sites-topology`, `ad-certificate-services`,
`ad-authn`) and reused the generic ones (`users`, `security`, `troubleshooting`,
`migration`). Keep each as a backticked token with a one-line gloss so `tags.py` /
`lint.py` accept it.

## 3. Create the raw tier

**Notes-first** (AD):

```bash
mkdir -p _sources/active-directory
```

Add a `README.md` declaring these notes ARE the immutable ground truth (copy
`_sources/active-directory/README.md`), then write notes — **one file per concept**,
each recording its source (Microsoft Learn URL + fetch date, or a lab/ticket
observation) and the load-bearing facts, paraphrased (no long verbatim excerpts).
Our seed: `_sources/active-directory/fsmo-roles.md`.

**Corpus-backed from a docs repo** (the "give me *all* the docs" path — what we
wired for AD against Microsoft Learn). The Windows Server / AD docs are open-source
Markdown in `MicrosoftDocs/windowsserverdocs` (AD under `WindowsServerDocs/identity/`).
Clone on a networked machine, drop the `identity/` tree into
`_sources/active-directory/_raw/`, then run two stdlib commands offline:

```bash
# docs tree -> corpus (index.jsonl + body files) — derives the learn.microsoft URLs
python3 _meta/bin/docs_to_corpus.py \
    --src _sources/active-directory/_raw/identity \
    --domain active-directory --apply

# corpus -> immutable in-vault reference notes (existing tool, unchanged)
python3 _meta/bin/corpus_to_vault.py --domain active-directory --apply
```

`docs_to_corpus.py` turns each DocFX `.md` into a corpus record (frontmatter
`title`/`description` → note title/abstract, body stripped of frontmatter, live URL
derived from the path); `includes/` partials and non-Markdown assets are skipped.
After folding in, **flip the domain's `shape:` to `corpus-backed`** in
`_meta/taxonomy.md` (and add `corpora/active-directory/` to its `sources:`), then
re-run `index.py` → `crosslink.py --apply` → `lint.py`. The retrieval contract
becomes grep over `reference/active-directory/` (+ optional `kb.py --domain
active-directory search`), exactly like keycloak.

For a non-DocFX bulk source (a CIS/STIG PDF, a vendor guide), drop it in `_raw/` and
distill it into paraphrased `_sources/<domain>/` notes instead — no long verbatim
(copyright + the "provenance, not transcripts" rule).

## 4. Seed the synthesis (minimum viable brain)

Write three pages so the brain is navigable and lintable:

1. **Overview topic** — the spine. `topics/active-directory-overview.md`.
2. **First entity** it links — `entities/fsmo-roles.md`.
3. **The review MOC** named in step 1's `review-moc:` —
   `topics/active-directory-implementation-review.md` — with a rule→anti-pattern→
   symptom checklist and a symptom→cause reverse index. Copy the shape from
   `topics/sso-implementation-review.md`.

Every page carries the full frontmatter contract: `title / type / domain / slug /
summary / sources / provenance / tags / status / updated`. For notes-first, cite
`note:_sources/<domain>/<file>.md` and carry the upstream `web:` URL. Assign
`provenance:` by reading each claim against its note — don't count bullets. Tag
`(inferred)` inline for cross-source synthesis. Slugs are globally unique across
`topics/` + `entities/`.

## 5. Generate indexes and lint

```bash
python3 _meta/bin/index.py     # writes index.<domain>.md + adds the domain to the global router
python3 _meta/bin/lint.py      # health check
```

A healthy new brain looks like our AD run:

- `wrote index.active-directory.md (3 pages)` and the global `index.md` router gains
  `- [active-directory](index.active-directory.md) — 3 pages · review lens [[active-directory-implementation-review]]`.
- The only AD findings are **intentional `[[wanted]]` TODO markers** (we left
  `[[group-policy]]` as the next page to write) and the review-MOC's
  `inferred>=extracted` drift warning — expected, because a MOC is pure synthesis
  (the sibling `sso-implementation-review` shows the same).
- **No AD orphans, no broken links, no missing-frontmatter errors.**

## 6. Grow it, and record what you ingest

From here the brain grows through the normal **INGEST** / **QUERY** ops in
`../CLAUDE.md`. As you fold in real sources, record them:

```bash
python3 _meta/bin/manifest.py record note:_sources/active-directory/<file>.md --pages <slug,...>
```

---

## Per-tech quick checklist

- [ ] Shape chosen (notes-first vs corpus-backed)
- [ ] `### <domain>` block added under `## Domains` in `_meta/taxonomy.md`
- [ ] New `areas:` added to `## Areas`
- [ ] Raw tier created (`_sources/<domain>/` + README, or `reference/<domain>/`)
- [ ] Overview topic + first entity + `<domain>-implementation-review` MOC written
- [ ] `index.py` run → `index.<domain>.md` + router updated
- [ ] `lint.py` clean (only intentional wanted-pages / MOC drift)
- [ ] Sources recorded in the manifest as they're ingested
