---
name: wiki-query
description: Answer ANY question against the multi-domain LLM-maintained Obsidian wiki/ — every domain declared in wiki/_meta/taxonomy.md (currently keycloak/RHBK, openshift/kubernetes, active-directory, cisco-ios-xe) and any future domain added via add-domain — using a tiered read (index.<domain>.md + summaries first, page bodies only when needed), falling back to grepping the in-vault reference tier (wiki/reference/<domain>/), then filing the answer back as a durable questions/ page. Use for ANY question a wiki domain covers — Kubernetes/OpenShift, AD, and IOS-XE questions route here exactly like Keycloak ones, even when another domain-specific skill also matches; wiki-query is what keeps the wiki richer and the answer under the query protocol.
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
   (notes-first). `python3 -m wikikb kb --domain <d> search "..."` is an
   optional ranked search over that same reference tier.
4. Synthesize, then end the answer with the **two-group References section**
   (RH ground-truth `kb:`/`guide:`/`ref:` *and* Wiki `[[slug]]` + `web:`) — the
   contract (resolve each used page's `sources:` to id + title; surface kb even
   when the wiki already synthesizes; flag tier disagreements) is defined in
   **"Operation: QUERY" in `wiki/CLAUDE.md`** (single source of truth). Don't
   restate it here.
5. **File the answer back:** write `wiki/questions/<slug>.md`; if a reusable fact
   surfaced, run a mini-INGEST (see the `wiki-ingest` skill).
6. **Every answer follows the "Query answering protocol" in `wiki/CLAUDE.md`**
   (Operation: QUERY → "Query answering protocol"): search-first (absence in corpus
   is a valid answer), reasoning not just facts, false-premise correction, **line-level
   citations** (`file.md:XXX-YYY`), inline provenance tags, file-back as `status: draft`,
   and a closing 1–2 line chat summary. Mandatory regardless of confidence **and
   regardless of domain** — defined there, not restated here.
7. **Final gate (blocking):** before presenting ANY answer as complete, run the
   **"Final self-check"** checklist at the end of the protocol section in
   `wiki/CLAUDE.md`. If any box fails, the answer is NOT final — complete the missing
   step first, then respond.
8. **Subagent-mediated research / multi-skill matches:** if the search runs inside a
   subagent (Explore/general-purpose) or the question also matched another skill, the
   layer that writes the user-facing answer STILL owns steps 6-7. Instruct research
   subagents to return per-claim `file.md:line` citations + extracted/`(inferred)`
   tags, and preserve them verbatim in the final synthesis — never compress to
   file-level citations, never drop tags (rule defined in `wiki/CLAUDE.md`, "The
   answer-producing layer owns this gate").

## Hard rule
Reads of `kb/` and `references/` are fine; **writes go only to `wiki/`**. No
network beyond the offline corpus; stdlib only.

> **Optional online tier:** an off-by-default LangGraph runner
> (`wiki/_meta/wikikb/graph/query_graph.py`, enabled with `WIKI_LLM=local` + the vendored deps) can
> mechanize this QUERY flow against a **local loopback** model, and `eval.py --measure-llm` reports
> real token/$/latency. It is an *alternative* to the host-runtime loop, not a replacement, and stays
> fully offline by default. See `wiki/CLAUDE.md` → "Optional online tier".
