"""wikikb — the Keycloak/RHBK LLM-wiki toolchain (stdlib-only, air-gapped).

The importable package for the wiki's maintenance + retrieval + (optional) cost/LLM tooling. It
replaces the former flat `_meta/bin/` scripts: modules are imported via the package namespace
(`from wikikb.retrieval import kb`) instead of `sys.path.insert` sibling hacks, and run via the
dispatcher `python -m wikikb <tool>` (from `wiki/_meta/`, or with `PYTHONPATH=<repo>/wiki/_meta`) —
or directly as `python -m wikikb.<group>.<tool>` (e.g. `wikikb.retrieval.kb`). No `pip install` required
(the air-gap "copy-and-run" model is preserved). Project paths are resolved once in `wikikb.paths`.
Modules are grouped into concern-subpackages (retrieval/build/corpus/quality/online/graph); the
probes/selftest live under `_meta/tests/`.
"""
