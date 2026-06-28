"""config.py — T1. Frozen runtime config from env. No IO on import (NFR-5)."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _repo_root_default() -> str:
    # Walk up from this file to the repo root (contains tools/wikidoc.py). Pure path math.
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "tools" / "wikidoc.py").exists():
            return str(p)
    return str(here.parents[2])  # service/wiki_router/ -> repo


@dataclass(frozen=True)
class Config:
    repo_root: str
    ranker: str                 # lexical | embedding | hybrid
    embed_endpoint: str | None
    embed_model_path: str | None
    embed_store: str
    admin_token: str | None
    default_k: int

    @staticmethod
    def from_env(env=None) -> "Config":
        e = env if env is not None else os.environ
        root = e.get("WIKI_REPO_ROOT") or _repo_root_default()
        ranker = (e.get("WIKI_RANKER") or "lexical").strip().lower()
        if ranker not in ("lexical", "embedding", "hybrid"):
            ranker = "lexical"
        store = e.get("WIKI_EMBED_STORE") or str(Path(root) / "service" / "embeddings.npz")
        try:
            k = int(e.get("WIKI_DEFAULT_K", "5"))
        except ValueError:
            k = 5
        return Config(
            repo_root=str(root),
            ranker=ranker,
            embed_endpoint=(e.get("WIKI_EMBED_ENDPOINT") or None),
            embed_model_path=(e.get("WIKI_EMBED_MODEL_PATH") or None),
            embed_store=store,
            admin_token=(e.get("WIKI_ADMIN_TOKEN") or None),
            default_k=max(1, min(50, k)),
        )
