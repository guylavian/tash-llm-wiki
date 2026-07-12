"""paths.py — the single home for project paths, resolved from the package location.

Replaces the per-module `BIN = dirname(abspath(__file__)); WIKI = dirname(dirname(BIN))` math that
was duplicated across ~20 scripts. Everything is derived once from this file's location:
`_meta/wikikb/paths.py` -> WIKI is parents[2]. Values are pathlib.Path (os.path.join / open / f-strings
all accept them); call str() if a plain string is needed. stdlib only.
"""
import os as _env
from pathlib import Path

PKG = Path(__file__).resolve().parent     # .../wiki/_meta/wikikb
META = PKG.parent                          # .../wiki/_meta
WIKI = META.parent                         # .../wiki
# Eval isolation override: run300 sets WIKIKB_VAULT_ROOT=<case-snapshot> in the examinee
# env; every opencode-spawned wikikb MCP inherits it, so all VAULT READS scope to the
# snapshot even though the global opencode config points PYTHONPATH at the live package
# (opencode ignores per-project MCP overrides — verified empirically 2026-07-12).
# Code comes from the live tree; data comes from the snapshot. Unset ⇒ identical to before.
if _env.environ.get("WIKIKB_VAULT_ROOT"):
    WIKI = Path(_env.environ["WIKIKB_VAULT_ROOT"]).resolve()
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


# --- eval-freeze lock (the 15:09 rule) -------------------------------------
# run300 writes .eval-lock at cohort start ({"run_id":…, "pid":…}) and removes
# it at exit; build/crosslink --apply refuse while the holder pid is alive.
import json as _json
import os as _os

EVAL_LOCK = WIKI / ".eval-lock"


def eval_lock_error():
    """Return a refusal message while a live eval cohort holds the vault lock,
    else None. A stale lock (holder pid dead) is ignored, not an error."""
    try:
        info = _json.loads(EVAL_LOCK.read_text(encoding="utf-8"))
        pid = int(info.get("pid", 0))
    except (OSError, ValueError):
        return None
    try:
        _os.kill(pid, 0)
    except OSError:
        return None                      # stale — holder is dead
    return ("vault is FROZEN: live eval cohort %s (pid %d) holds %s — no build or "
            "crosslink --apply while a run is live (the 15:09 rule)"
            % (info.get("run_id", "?"), pid, EVAL_LOCK))
