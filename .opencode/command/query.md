---
description: Answer an RHBK/Keycloak question from the wiki (tiered), then file it back
agent: wiki
---

Answer this Keycloak/RHBK question: **$ARGUMENTS**

Follow the `wiki-query` skill and "Operation: QUERY" in `wiki/CLAUDE.md`. Do the
tiered cheap pass first (read `wiki/index.md`, route to the relevant domain, then
read `wiki/index.<domain>.md` + candidate pages' `title:`/`summary:`), open page
bodies only when needed, fall back — when the synthesized pages are thin — to
grepping the in-vault raw tier (`wiki/reference/<domain>/` for a corpus-backed
domain, `wiki/_sources/<domain>/` for a notes-first one); `wiki/_meta/wikikb/kb.py
--domain <d> search "..."` is an optional ranked search over that same reference
tier. Then **end the answer with the two-group References section (RH ground-truth
+ Wiki/`web:`) mandated by "Operation: QUERY" in `wiki/CLAUDE.md`**, and file the
answer back as `wiki/questions/<slug>.md`.

Never edit the immutable `wiki/reference/`, `wiki/_sources/`, or `references/`. Offline only.

> Optional: an off-by-default LangGraph runner (`wiki/_meta/wikikb/graph/query_graph.py`, `WIKI_LLM=local`
> + vendored deps) can mechanize this flow against a **local loopback** model — an alternative to the
> host loop, not a replacement; fully offline by default. See `wiki/CLAUDE.md` → "Optional online tier".
