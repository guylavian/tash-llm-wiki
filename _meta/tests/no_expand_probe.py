#!/usr/bin/env python3
"""Causal-ablation checks: disabling expansion preserves lexical candidates byte-for-byte."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from wikikb.graph import nodes
from wikikb.retrieval import expand


def main():
    state = {"query": "realm token session", "domain": "keycloak", "k": 5}
    state.update(nodes.retrieve_node(state))
    before = json.dumps(state["candidates"], ensure_ascii=False, separators=(",", ":"))
    real = expand.expand
    try:
        expand.expand = lambda *a, **k: (_ for _ in ()).throw(AssertionError("expand called"))
        result = nodes.expand_node({**state, "no_expand": True})
    finally:
        expand.expand = real
    after = json.dumps(result["candidates"], ensure_ascii=False, separators=(",", ":"))
    assert before == after
    assert result["graph_notes"] == []
    assert result["graph_pages"] == []
    assert result["page_fm"] == []
    print("PASS --no-expand preserves lexical candidates byte-identically")


if __name__ == "__main__":
    main()
