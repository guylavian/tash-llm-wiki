---
name: wiki-query
description: Answer an RHBK/Keycloak question from the LLM-maintained Obsidian wiki/ using a tiered read (index.<domain>.md + summaries first, page bodies only when needed), falling back to grepping the in-vault reference tier (wiki/reference/<domain>/), then filing the answer back as a durable questions/ page. Use to answer Keycloak/RHBK questions while leaving the wiki richer.
---

# wiki-query

Packages the **QUERY** operation. Behavior is defined in **`wiki/CLAUDE.md`**
(single source of truth); this is a thin pointer.

## Do this
1. **Read `wiki/CLAUDE.md`** — follow "Operation: QUERY".
2. **Tiered (cheap) pass first:** read `wiki/index.md`, route to the domain, read
   `wiki/index.<domain>.md` + candidate pages' `title:` + `summary:`. Open page
   **bodies only** when the cheap pass can't answer — this keeps query cost flat.
3. If the synthesized pages are thin, fall back to the in-vault raw tier (read-only):
   grep `wiki/reference/<domain>/` (corpus-backed) or `wiki/_sources/<domain>/`
   (notes-first). `python3 wiki/_meta/bin/kb.py --domain <d> search "..."` is an
   optional ranked search over that same reference tier.
4. Synthesize, then end the answer with the **two-group References section**
   (RH ground-truth `kb:`/`guide:`/`ref:` *and* Wiki `[[slug]]` + `web:`) — the
   contract (resolve each used page's `sources:` to id + title; surface kb even
   when the wiki already synthesizes; flag tier disagreements) is defined in
   **"Operation: QUERY" in `wiki/CLAUDE.md`** (single source of truth). Don't
   restate it here.
5. **File the answer back:** write `wiki/questions/<slug>.md`; if a reusable fact
   surfaced, run a mini-INGEST (see the `wiki-ingest` skill).

## Hard rule
Reads of `kb/` and `references/` are fine; **writes go only to `wiki/`**. No
network beyond the offline corpus; stdlib only.
