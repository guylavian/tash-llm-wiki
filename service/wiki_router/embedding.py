"""embedding.py — T5/T6. Local-only embedding source + metadata-only numpy-flat store.

FR-9: source is a loopback /embeddings endpoint OR a staged model path; absent -> (None,None)
      so the factory falls back to lexical.
FR-10: the embedded corpus is frontmatter + headings + section summaries ONLY — never bodies.
numpy is imported lazily inside functions so the lexical core stays zero-ML (ADR-2/ADR-4).
"""
from __future__ import annotations

import json
import logging
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

log = logging.getLogger("wiki_router.embedding")

_LOOPBACK = ("127.0.0.1", "localhost", "::1")


def meta_text(entry, section) -> str:
    """Metadata-only text for one section (FR-10). NEVER includes section.text (full body)."""
    kw = " ".join(str(x) for x in (entry.frontmatter.get("keywords") or []))
    return f"{entry.domain} | {entry.title} | {section.title} | {kw} | {section.summary}"


class EmbeddingStore:
    """Single-file numpy-flat cosine store. Keeps source texts for FR-10 verification."""

    def __init__(self, ids=None, matrix=None, texts=None):
        self.ids = list(ids or [])
        self._matrix = matrix            # numpy 2D float32 or None
        self.texts = list(texts or [])
        self._pos = {i: n for n, i in enumerate(self.ids)}

    def empty(self) -> bool:
        return self._matrix is None or len(self.ids) == 0

    def get(self, key):
        n = self._pos.get(key)
        return None if n is None else self._matrix[n]

    @staticmethod
    def cosine(a, b) -> float:
        import numpy as np
        a = np.asarray(a, dtype="float32"); b = np.asarray(b, dtype="float32")
        na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
        if na == 0.0 or nb == 0.0:
            return 0.0
        return float(np.dot(a, b) / (na * nb))

    @classmethod
    def build(cls, index, embedder) -> "EmbeddingStore":
        import numpy as np
        ids, texts = [], []
        for e in index.entries:
            for s in e.sections:
                ids.append(f"{e.path}#{s.anchor}")
                texts.append(meta_text(e, s))            # FR-10 metadata only
        if not ids:
            return cls()
        vecs = embedder(texts)
        return cls(ids=ids, matrix=np.asarray(vecs, dtype="float32"), texts=texts)

    def save(self, path: str) -> None:
        import numpy as np
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        np.savez(path, ids=np.array(self.ids, dtype=object),
                 matrix=self._matrix, texts=np.array(self.texts, dtype=object))

    @classmethod
    def load(cls, path: str) -> "EmbeddingStore | None":
        if not Path(path).exists():
            return None
        import numpy as np
        d = np.load(path, allow_pickle=True)
        return cls(ids=list(d["ids"]), matrix=d["matrix"], texts=list(d["texts"]))


class EndpointEmbedder:
    """POST to a LOOPBACK OpenAI-compatible /embeddings endpoint (AC-9.2: loopback only)."""

    def __init__(self, url: str, model: str = "local"):
        self.url, self.model = url, model

    def __call__(self, texts):
        payload = json.dumps({"model": self.model, "input": list(texts)}).encode("utf-8")
        req = urllib.request.Request(self.url, data=payload,
                                     headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:    # loopback only (validated in resolve)
            data = json.loads(resp.read().decode("utf-8"))
        return [row["embedding"] for row in data["data"]]


class LocalModelEmbedder:
    """Staged sentence-transformers model loaded BY PATH. Lazy import; no network."""

    def __init__(self, model_path: str):
        from sentence_transformers import SentenceTransformer  # lazy (ADR-4)
        self._m = SentenceTransformer(model_path)

    def __call__(self, texts):
        return self._m.encode(list(texts), normalize_embeddings=False).tolist()


def _is_loopback(url: str) -> bool:
    try:
        host = urlparse(url).hostname or ""
    except ValueError:
        return False
    return host in _LOOPBACK


def resolve(config, index):
    """Return (embedder, store) or (None, None). Never a non-loopback call (FR-9/AC-9.2)."""
    embedder = None
    if config.embed_endpoint:
        if not _is_loopback(config.embed_endpoint):
            log.warning("WIKI_EMBED_ENDPOINT %s is not loopback — refusing (AC-9.2).",
                        config.embed_endpoint)
            return None, None
        embedder = EndpointEmbedder(config.embed_endpoint, config.embed_model_path or "local")
    elif config.embed_model_path and Path(config.embed_model_path).exists():
        try:
            embedder = LocalModelEmbedder(config.embed_model_path)
        except Exception as ex:                       # noqa: BLE001 — degrade, never crash (FR-9)
            log.warning("staged model load failed (%s); embedding disabled.", ex)
            return None, None
    if embedder is None:
        return None, None
    store = EmbeddingStore.load(config.embed_store)
    if store is None or store.empty():
        try:
            store = EmbeddingStore.build(index, embedder)
        except Exception as ex:                       # noqa: BLE001
            log.warning("embedding corpus build failed (%s); embedding disabled.", ex)
            return None, None
    return embedder, store
