---
description: Answer a wiki question (any domain) via wikikb ask — graph-by-default — then file it back
agent: wiki
---

Answer this question from the wiki: **$ARGUMENTS**

Run the mechanized QUERY pipeline first — it routes, retrieves, graph-expands,
gates, and synthesizes in one shot (orchestrated through the LangGraph StateGraph
by default; degrades to the same nodes linearly when langgraph is absent):

- Preferred: call the `wikikb` MCP tool `ask` with the question (add `domain`
  and `tier` when known).
- CLI equivalent: `PYTHONPATH=_meta _meta/.venv-online/bin/python -m wikikb ask
  "$ARGUMENTS" --json` (plain `python3` also works — linear fallback; check the
  `orchestrator` field).

If the returned answer is thin or extractive, deepen it per "Operation: QUERY"
in `CLAUDE.md` (repo root = vault root): read `index.<domain>.md` + candidate
pages' `title:`/`summary:`, open page bodies only when needed, then grep the
in-vault raw tier (`vault/reference/<domain>/` for corpus-backed domains,
`vault/_sources/<domain>/` for notes-first ones).

Then **end the answer with the two-group References section (RH ground-truth +
Wiki/`web:`) mandated by "Operation: QUERY" in `CLAUDE.md`**, and file the answer
back as `questions/<slug>.md` (full frontmatter, `status: draft`, banner rules).

Never edit the immutable `reference/`, `_sources/`, or `references/`. Offline only.
