"""paths.py — the single home for project paths, resolved from the package location.

Replaces the per-module `BIN = dirname(abspath(__file__)); WIKI = dirname(dirname(BIN))` math that
was duplicated across ~20 scripts. Everything is derived once from this file's location:
`_meta/wikikb/paths.py` -> WIKI is parents[2]. Values are pathlib.Path (os.path.join / open / f-strings
all accept them); call str() if a plain string is needed. stdlib only.
"""
from pathlib import Path

PKG = Path(__file__).resolve().parent     # .../wiki/_meta/wikikb
META = PKG.parent                          # .../wiki/_meta
WIKI = META.parent                         # .../wiki
ROOT = WIKI.parent                         # repo root

REFERENCE = WIKI / "reference"             # in-vault corpus tier (reference/<domain>/)
REFERENCES = WIKI / "references"           # curated reference guides (ref: tier — folded into the vault 2026-07-07)
EVAL = META / "eval"                       # eval + gate cases + committed goldens
TAXONOMY = META / "taxonomy.md"
MODELS = META / "models"                   # vendored embedding model(s) / tokenizers
EMBEDDINGS = META / "embeddings"           # built dense index (derived)
TKG = META / "tkg"                         # built temporal-knowledge-graph store (derived; gitignored)
MANIFEST = META / ".manifest.json"
COST_REPORT = EVAL / "cost_report.json"    # regenerable LLM-spend ledger
LLM_CONFIG = META / "llm.config.yaml"
