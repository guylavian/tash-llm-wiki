"""paths.py — the single home for project paths, resolved from the package location.

Replaces the per-module `BIN = dirname(abspath(__file__)); WIKI = dirname(dirname(BIN))` math that
was duplicated across ~20 scripts. Everything is derived once from this file's location:
`_meta/wikikb/paths.py` -> WIKI is parents[2]. Values are pathlib.Path (os.path.join / open / f-strings
all accept them); call str() if a plain string is needed. stdlib only.
"""
import os as _env
from pathlib import Path

PKG = Path(__file__).resolve().parent     # <repo>/_meta/wikikb
META = PKG.parent                          # <repo>/_meta
ROOT = META.parent                         # <repo> — the code/repo root
#
# CONTENT LIVES UNDER `<repo>/vault/` (moved there 2026-08-05). The vault is the ONE
# directory that holds every non-regenerable piece of data — the page tiers, the immutable
# reference/_sources tiers, the generated indexes, AND `taxonomy.md` + `.manifest.json`
# (both formerly under `_meta/`, which stranded them when the vault was copied elsewhere).
# The invariant that buys portability: **copying `vault/` to another machine carries the
# whole knowledge base**; everything left behind under `_meta/` is either code or is
# regenerable from the vault (`embeddings/`, `tkg/`, `eval/` goldens).
#
# ROOT is derived from META (the CODE location), NOT from WIKI — so redirecting the vault
# never drags the repo-relative staging dirs along with it. It was `WIKI.parent` before the
# move, which in the old flat layout resolved to the directory ABOVE the repo, quietly
# putting `corpora/` outside the project.
WIKI = ROOT / "vault"                      # <repo>/vault — the portable content root
# Eval isolation override: run300 sets WIKIKB_VAULT_ROOT=<case-snapshot> in the examinee
# env; every opencode-spawned wikikb MCP inherits it, so all VAULT READS scope to the
# snapshot even though the global opencode config points PYTHONPATH at the live package
# (opencode ignores per-project MCP overrides — verified empirically 2026-07-12).
# Code comes from the live tree; data comes from the snapshot. Unset ⇒ identical to before.
# This is ALSO the container seam: `-e WIKIKB_VAULT_ROOT=/data/vault` with the host dir
# bind-mounted there (see .env.example / docker-compose.yml).
if _env.environ.get("WIKIKB_VAULT_ROOT"):
    WIKI = Path(_env.environ["WIKIKB_VAULT_ROOT"]).resolve()

# The synthesis-layer page dirs — the ONE definition (was copy-pasted in 13 modules, so adding a
# tier meant 13 edits and one of them would be forgotten). `outputs/` is the derived-artifact tier
# (runbooks, cheat sheets, comparisons): a real page like any other — full frontmatter, linted,
# indexed, crosslinked — that cites the topics/entities it was compiled from, so the next artifact
# builds on every previous one instead of being re-derived outside the vault.
PAGE_DIRS = ("topics", "entities", "questions", "outputs")

# The page↔page wikilink grammar — the ONE definition (was byte-identical in lint.py, expand.py and
# tkg/model.py, the three tools that build the link graph, with tkg's comment literally saying "Mirror
# expand.py exactly"). Bare kebab slug per CLAUDE.md ("no directory, no .md"), with an OPTIONAL
# `|display text` — Obsidian's alias form, which the vault already uses on 67 hand-authored page links
# across 25 pages that every one of those tools silently dropped. The pipe was originally excluded to
# keep crosslink's generated `## Sources` links (`[[note|Title]]`) out of the page graph; that job
# belongs to excising the Sources block (which all three now do), not to the link grammar.
import re as _re

PAGELINK_RE = _re.compile(r"\[\[([a-z0-9][a-z0-9-]*)(?:\|[^\]\n]*)?\]\]")

REFERENCE = WIKI / "reference"             # in-vault corpus tier (reference/<domain>/)
REFERENCES = WIKI / "references"           # curated reference guides (ref: tier — folded into the vault 2026-07-07)
# --- vault-resident DATA (travels with a `vault/` copy) --------------------
# taxonomy.md and .manifest.json moved out of `_meta/` on 2026-08-05. Both describe the
# CONTENT, not the toolchain: taxonomy declares the domains every page's `domain:` is
# validated against (without it lint rejects every page and index builds nothing), and the
# manifest is the ingest ledger for the notes in this vault. Under `_meta/` they were left
# behind whenever the vault moved — the exact failure that makes a "just copy the folder"
# migration silently produce an unlintable, unindexable wiki on the far end.
TAXONOMY = WIKI / "taxonomy.md"
MANIFEST = WIKI / ".manifest.json"
# The ONLINE-mode scrape watchlist: which websites get harvested into which domain. Vault-resident
# for the same reason taxonomy.md is — it describes the CONTENT ("this vault tracks these upstream
# pages"), not the toolchain, so a copied vault must carry it or the far end silently stops
# refreshing sources it believes it is watching. Hand-editable AND API-managed (POST/DELETE
# /scrape/sources); it holds CONFIG ONLY. Per-URL fetch STATE (last digest, last fetch date) lives
# in the raw-tier sidecars next to the harvested Markdown, so the scraper never rewrites a file a
# human may be editing.
SCRAPE_SOURCES = (Path(_env.environ["WIKIKB_SCRAPE_SOURCES"]).resolve()
                  if _env.environ.get("WIKIKB_SCRAPE_SOURCES") else WIKI / "scrape-sources.json")
# Regenerable cache for the Common Crawl collection list (collinfo.json). Code-resident, not
# vault-resident: it is a copy of a public file that is refetched on TTL expiry, so leaving it
# behind on a vault copy costs one HTTP request, not data.
SCRAPE_CACHE = META / ".scrape-cache"
# --- code-resident / REGENERABLE (safe to leave behind) --------------------
EVAL = META / "eval"                       # eval + gate cases + committed goldens
MODELS = META / "models"                   # vendored embedding model(s) / tokenizers
EMBEDDINGS = META / "embeddings"           # built dense index (derived — rebuild with `wikikb embed`)
TKG = META / "tkg"                         # built temporal-knowledge-graph store (derived; gitignored)
# Staging for a harvest in flight (pdf/docs/adoc_to_corpus -> corpus_to_vault). Repo-relative
# by default; override so a container can persist it on the mounted volume.
CORPORA = Path(_env.environ["WIKIKB_CORPORA_DIR"]).resolve() if _env.environ.get("WIKIKB_CORPORA_DIR") else ROOT / "corpora"
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
