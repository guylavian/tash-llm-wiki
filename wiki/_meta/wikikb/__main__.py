"""python -m wikikb <tool> [args...] — dispatch to a tool module's main().

`python -m wikikb kb --domain keycloak search "..."` works in addition to the direct
`python -m wikikb.<group>.<tool> ...`. Run from wiki/_meta/ (or PYTHONPATH=<repo>/wiki/_meta); no install.
The dispatcher maps each tool name to its subpackage, so the public CLI is STABLE even if a tool's
group changes — callers never need to know the internal layout.
"""
import importlib
import sys

# tool name -> subpackage
TOOLS = {
    "backfill": "build",
    "crosslink": "build",
    "index": "build",
    "manifest": "build",
    "tags": "build",
    "corpus_to_vault": "corpus",
    "docs_to_corpus": "corpus",
    "adoc_to_corpus": "corpus",
    "migrate_native": "corpus",
    "cost": "online",
    "llm": "online",
    "evaluate": "quality",
    "faithfulness": "quality",
    "lint": "quality",
    "embed": "retrieval",
    "expand": "retrieval",
    "kb": "retrieval",
    "route": "retrieval",
    "insights": "quality",
    "ask": "graph",        # QUERY pipeline -> one cited, gated answer (offline extractive / local LLM)
    "tkg": "tkg",          # the temporal-knowledge-graph CLI lives at wikikb/tkg/tkg.py
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in TOOLS:
        print("usage: python -m wikikb <tool> [args]\n  tools: " + ", ".join(sorted(TOOLS)))
        print("  (or run a tool directly: python -m wikikb.<group>.<tool> ...)")
        sys.exit(2)
    tool, sys.argv = sys.argv[1], [sys.argv[1]] + sys.argv[2:]
    importlib.import_module("wikikb.%s.%s" % (TOOLS[tool], tool)).main()


if __name__ == "__main__":
    main()
