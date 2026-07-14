# opencode session ses_0a806152cffewB6VUY6B8X0Rno — 2026-07-12 23:17
model: gemini-flash-latest

## USER
Answer this question from the wiki: **Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? **

Run the mechanized QUERY pipeline first — it routes, retrieves, graph-expands,
gates, and synthesizes in one shot (orchestrated through the LangGraph StateGraph
by default; degrades to the same nodes linearly when langgraph is absent):

- Preferred: call the `wikikb` MCP tool `ask` with the question (add `domain`
  and `tier` when known).
- CLI equivalent: `PYTHONPATH=_meta _meta/.venv-online/bin/python -m wikikb ask
  "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? " --json` (plain `python3` also works — linear fallback; check the
  `orchestrator` field).

If the returned answer is thin or extractive, deepen it per "Operation: QUERY"
in `CLAUDE.md` (repo root = vault root): read `index.<domain>.md` + candidate
pages' `title:`/`summary:`, open page bodies only when needed, then grep the
in-vault raw tier (`reference/<domain>/` for corpus-backed domains,
`_sources/<domain>/` for notes-first ones).

Then **end the answer with the two-group References section (RH ground-truth +
Wiki/`web:`) mandated by "Operation: QUERY" in `CLAUDE.md`**, and file the answer
back as `questions/<slug>.md` (full frontmatter, `status: draft`, banner rules).

Never edit the immutable `reference/`, `_sources/`, or `references/`. Offline only.