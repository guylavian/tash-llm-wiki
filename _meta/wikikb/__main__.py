"""python -m wikikb <tool> [args...] — dispatch to a tool module's main().

`python -m wikikb kb --domain keycloak search "..."` works in addition to the direct
`python -m wikikb.<group>.<tool> ...`. Run from wiki/_meta/ (or PYTHONPATH=<repo>/wiki/_meta); no install.
The dispatcher maps each tool name to its subpackage, so the public CLI is STABLE even if a tool's
group changes — callers never need to know the internal layout.

Every dispatch first runs the VAULT BOOTSTRAP (wikikb/bootstrap.py): a missing or incomplete vault
skeleton is created here, once, before the tool imports and starts scanning it. This is the seam
because it is the ONE place every tool is entered from — putting the call in each tool's main()
would mean remembering it 25 times, and putting it at package-import time would give a bare
`import wikikb` filesystem side effects. It is idempotent, silent when there is nothing to do, and
skipped entirely under WIKIKB_BOOTSTRAP=0.
"""
import importlib
import sys

# tool name -> subpackage ("" = the module lives at the top of the package, next to paths.py)
TOOLS = {
    "bootstrap": "",       # create/repair the vault skeleton (also runs automatically, see above)
    "backfill": "build",
    "build": "build",      # the whole regen chain: tags -> crosslink -> index -> tkg -> lint
    "crosslink": "build",
    "domains": "build",    # CRUD over the domain declarations in vault/taxonomy.md (mirrors /domains)
    "graphlinks": "build",  # writes Graphify's computed communities back as graph_community: frontmatter
    "index": "build",
    "card": "build",         # QUERY protocol card generator (F4, 100k-budget plan)
    "manifest": "build",
    "tags": "build",
    "corpus_to_vault": "corpus",
    "docs_to_corpus": "corpus",
    "adoc_to_corpus": "corpus",
    "pdf_to_corpus": "corpus",
    "migrate_native": "corpus",
    "cost": "online",
    "llm": "online",
    "evaluate": "quality",
    "verify": "quality",   # answer-time source verification: numeric claims vs cited kb: notes
    "faithfulness": "quality",
    "lint": "quality",
    "livebank": "quality",  # live-query bank: realistic SRE queries through the FULL serve path
    "embed": "retrieval",
    "expand": "retrieval",
    "kb": "retrieval",
    "route": "retrieval",
    "insights": "quality",
    "ask": "graph",        # QUERY pipeline -> one cited, gated answer (offline extractive / local LLM)
    "tkg": "tkg",          # the temporal-knowledge-graph CLI lives at wikikb/tkg/tkg.py
    "serve": "serve",      # stateless JSON API over the wiki for SRE/agent consumption (loopback default)
    "mcp": "mcp",          # MCP (Model Context Protocol) stdio server for MCP-host consumption
    "scrape": "scrape",         # ONLINE-mode web harvest (WIKIKB_MODE=online) via the Common Crawl index
    "web_to_corpus": "scrape",  # harvested web notes -> corpus records (stdlib, NO network)
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in TOOLS:
        print("usage: python -m wikikb <tool> [args]\n  tools: " + ", ".join(sorted(TOOLS)))
        print("  (or run a tool directly: python -m wikikb.<group>.<tool> ...)")
        sys.exit(2)
    tool, sys.argv = sys.argv[1], [sys.argv[1]] + sys.argv[2:]
    if tool != "bootstrap":                       # `bootstrap` does its own, with a full report
        from wikikb import bootstrap
        bootstrap.ensure_startup(label="wikikb " + tool)
    group = TOOLS[tool]
    importlib.import_module("wikikb.%s.%s" % (group, tool) if group else "wikikb." + tool).main()


if __name__ == "__main__":
    main()
