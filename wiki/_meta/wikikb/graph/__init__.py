"""graph/ — the OPTIONAL LangGraph orchestration tier for the wiki's QUERY/INGEST operations.

This package mechanizes the prose operations in wiki/CLAUDE.md as LangGraph StateGraphs. It is the
optional online tier (Phase 4-5): with langgraph absent the modules still IMPORT (the langgraph
import lives INSIDE each build_*_graph() factory, never at module scope), so `import graph.query_graph`
is stdlib-safe and the host runtime remains the default agent loop. The nodes WRAP the existing
deterministic tools (kb/route/expand) and the real Confidence gate (lint.gate_banner) — they never
re-implement them — and the only LLM call is the synthesize node via the local-loopback llm.py gateway.
No LangChain / LCEL / SqliteSaver (COUNCIL-DIRECTIVES.md §5).
"""
