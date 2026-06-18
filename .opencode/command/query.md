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
domain, `wiki/_sources/<domain>/` for a notes-first one); `wiki/_meta/bin/kb.py
--domain <d> search "..."` is an optional ranked search over that same reference
tier. Then **end the answer with the two-group References section (RH ground-truth
+ Wiki/`web:`) mandated by "Operation: QUERY" in `wiki/CLAUDE.md`**, and file the
answer back as `wiki/questions/<slug>.md`.

Never edit the immutable `wiki/reference/`, `wiki/_sources/`, or `references/`. Offline only.
