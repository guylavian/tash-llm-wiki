#!/usr/bin/env python3
"""Backward-compat shim — the Keycloak KB now lives in the Obsidian vault.

The harvested corpus was folded into the vault as reference notes under
`wiki/reference/keycloak/`, and the query tool is now `wiki/_meta/bin/kb.py`, which
reads that reference tier (Obsidian rules all the data). Prefer calling it directly:

    python3 wiki/_meta/bin/kb.py --domain keycloak search "..."

This shim forwards every argument with `--domain keycloak` prepended, so existing
callers (`python3 kb/rhbk_kb.py search ...`) keep working.
"""
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.normpath(os.path.join(HERE, "..", "wiki", "_meta", "bin", "kb.py"))

if not os.path.isfile(KB):
    sys.exit("rhbk_kb.py shim: cannot find generic tool at %s" % KB)

# Inject the domain ahead of the subcommand; `domains` needs no domain.
forwarded = sys.argv[1:]
if forwarded and forwarded[0] != "domains":
    forwarded = ["--domain", "keycloak"] + forwarded
sys.argv = [KB] + forwarded
runpy.run_path(KB, run_name="__main__")
