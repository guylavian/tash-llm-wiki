"""test_router.py — T7. Acceptance tests; each asserts the AC/requirement it proves.

Runnable two ways:
  service/.venv-svc/bin/python -m pytest service/tests/test_router.py   # if pytest present
  service/.venv-svc/bin/python service/tests/test_router.py             # plain runner (no deps)
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SERVICE = HERE.parent
FIX = HERE / "fixtures"
sys.path.insert(0, str(SERVICE))

from fastapi.testclient import TestClient  # noqa: E402

from wiki_router.app import create_app  # noqa: E402
from wiki_router.config import Config  # noqa: E402
from wiki_router import index as idx_mod  # noqa: E402
from wiki_router import embedding as emb_mod  # noqa: E402
from wiki_router import ranking as rk  # noqa: E402


def cfg(root=FIX, ranker="lexical", admin=None, endpoint=None, model=None):
    return Config(repo_root=str(root), ranker=ranker, embed_endpoint=endpoint,
                  embed_model_path=model, embed_store=str(HERE / "_nostore.npz"),
                  admin_token=admin, default_k=5)


def client(c=None):
    return TestClient(create_app(c or cfg()))


class HashingEmbedder:
    """Deterministic, offline bag-of-tokens embedder for FR-8/10 tests (no network/ML)."""
    def __init__(self, dim=64):
        self.dim = dim

    def __call__(self, texts):
        import numpy as np
        out = []
        for t in texts:
            v = np.zeros(self.dim, dtype="float32")
            for tok in re.findall(r"[a-z0-9._-]+", t.lower()):
                v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % self.dim] += 1.0
            out.append(v)
        return out


# ---- FR-1 -----------------------------------------------------------------------------
def test_fr1_excludes_source_and_nonroutable():            # AC-1.1, AC-1.2
    ix = idx_mod.build_index(str(FIX))
    paths = {e.path for e in ix.entries}
    assert "references/observability.md" in paths
    assert "references/high-availability.md" in paths
    assert "wiki/reference/source.md" not in paths, "source-only must be excluded (AC-1.1)"
    assert "references/notroutable.md" not in paths, "routable:false must be excluded (AC-1.2)"


def test_fr1_sections_split():                              # AC-1.3
    ix = idx_mod.build_index(str(FIX))
    obs = next(e for e in ix.entries if e.path == "references/observability.md")
    anchors = [s.anchor for s in obs.sections]
    assert "__intro__" in anchors, "preamble retained as __intro__"
    assert len(anchors) == len(set(anchors)), "anchors distinct"
    assert len(obs.sections) >= 4, "3 H2 + intro"
    # non-overlapping, ascending ranges
    rs = [(s.start_line, s.end_line) for s in obs.sections]
    assert rs == sorted(rs) and all(a[1] <= b[0] for a, b in zip(rs, rs[1:]))


# ---- FR-3 -----------------------------------------------------------------------------
def test_fr3_version_gating():                              # AC-3.1, AC-3.2
    cl = client()
    hits = cl.post("/route", json={"query": "cache cluster infinispan", "version": "26.6"}).json()
    assert all(h["path"] != "references/high-availability.md" for h in hits), "26.2-only dropped"
    hits2 = cl.post("/route", json={"query": "cache cluster infinispan"}).json()
    assert any(h["path"] == "references/high-availability.md" for h in hits2), "no version => eligible"


# ---- FR-2 -----------------------------------------------------------------------------
def test_fr2_route_shape():                                 # AC-2.1, AC-2.2
    cl = client()
    hits = cl.post("/route", json={"query": "metrics"}).json()
    assert isinstance(hits, list) and len(hits) <= 5
    need = {"path", "section", "title", "domain", "type", "inject", "applies_to",
            "score", "source_provenance"}
    assert all(need <= set(h) for h in hits)
    assert len(cl.post("/route", json={"query": "metrics", "k": 999}).json()) <= 50


# ---- FR-4 -----------------------------------------------------------------------------
def test_fr4_get_section():                                 # AC-4.1
    cl = client()
    r = cl.get("/get", params={"path": "references/observability.md",
                               "section": "ispn000541-cache-dns-failure"}).json()
    assert r["inject"] == "section"
    assert "ISPN000541" in r["body"]
    assert "OTLP exporter" not in r["body"], "sibling section not leaked"


def test_fr4_get_full():                                    # AC-4.2
    cl = client()
    r = cl.get("/get", params={"path": "references/high-availability.md"}).json()
    assert r["inject"] == "full"
    assert "Single cluster" in r["body"] and "Cross-site" in r["body"]


def test_fr4_source_only_404():                             # AC-4.3
    r = client().get("/get", params={"path": "wiki/reference/source.md"})
    assert r.status_code == 404 and r.json()["reason"] == "source-only"


def test_fr4_notroutable_404():                             # AC-4.4
    r = client().get("/get", params={"path": "references/notroutable.md"})
    assert r.status_code == 404 and r.json()["reason"] == "not-routable"


# ---- FR-5 -----------------------------------------------------------------------------
def test_fr5_provenance():                                  # AC-5.1
    cl = client()
    for h in cl.post("/route", json={"query": "metrics tracing"}).json():
        assert h["source_provenance"] and all("visibility" in p for p in h["source_provenance"])
    g = cl.get("/get", params={"path": "references/observability.md",
                               "section": "metrics-endpoint"}).json()
    assert g["source_provenance"] and g["source_provenance"][0]["visibility"] == "public"


# ---- NFR-3 / NFR-4 --------------------------------------------------------------------
def test_nfr3_determinism():                                # AC-NFR3
    cl = client()
    a = cl.post("/route", json={"query": "metrics health tracing", "k": 10}).json()
    b = cl.post("/route", json={"query": "metrics health tracing", "k": 10}).json()
    assert [(h["path"], h["section"]) for h in a] == [(h["path"], h["section"]) for h in b]


def test_nfr4_path_safety():                                # AC-NFR4
    r = client().get("/get", params={"path": "../../etc/passwd"})
    assert r.status_code == 400 and r.json()["reason"] == "unsafe-path"


# ---- FR-6 -----------------------------------------------------------------------------
def test_fr6_reload(tmp_path=None):                         # AC-6.1, AC-6.2
    root = Path(tmp_path) if tmp_path else Path(__import__("tempfile").mkdtemp())
    (root / "references").mkdir(parents=True, exist_ok=True)
    shutil.copy(FIX / "references" / "observability.md", root / "references" / "observability.md")
    cl = TestClient(create_app(cfg(root=root, admin="s3cret")))
    assert cl.post("/reload", headers={"X-Admin-Token": "wrong"}).status_code == 401   # AC-6.1
    before = cl.get("/healthz").json()["files"]
    shutil.copy(FIX / "references" / "nearmiss.md", root / "references" / "nearmiss.md")
    ok = cl.post("/reload", headers={"X-Admin-Token": "s3cret"})
    assert ok.status_code == 200 and ok.json()["files"] == before + 1                  # AC-6.2


# ---- FR-7 -----------------------------------------------------------------------------
def test_fr7_health_metrics():                              # AC-7.1, AC-7.2
    cl = client()
    h = cl.get("/healthz").json()
    assert h["status"] == "ok" and {"files", "sections", "ranker"} <= set(h)
    m = cl.get("/metrics").text
    assert "wiki_index_files" in m and "wiki_route_requests_total" in m


# ---- FR-9 -----------------------------------------------------------------------------
def test_fr9_embedding_fallback():                          # AC-9.1
    h = client(cfg(ranker="embedding")).get("/healthz").json()
    assert h["ranker"] == "lexical", "no embed source => lexical fallback"


def test_fr9_loopback_refused():                            # AC-9.2
    ix = idx_mod.build_index(str(FIX))
    e, s = emb_mod.resolve(cfg(ranker="embedding", endpoint="http://evil.example.com/v1/embeddings"), ix)
    assert e is None and s is None, "non-loopback endpoint refused, no call made"


# ---- FR-8 -----------------------------------------------------------------------------
def test_fr8_hybrid_exact_code_wins():                      # AC-8.2
    ix = idx_mod.build_index(str(FIX))
    store = emb_mod.EmbeddingStore.build(ix, HashingEmbedder())
    hybrid = rk.HybridRanker(ix, rk.LexicalRanker(ix), rk.EmbeddingRanker(ix, HashingEmbedder(), store))
    cands = rk.candidates_for_query(ix, "ispn000541")
    hits = hybrid.rank("ispn000541", cands, version="26.6", k=5)
    assert hits, "hybrid returns hits"
    top = hits[0]
    assert top.path == "references/observability.md", "exact error-code doc out-ranks near-miss"
    assert all(h.path != "references/nearmiss.md" or h.score < top.score for h in hits)


# ---- FR-10 ----------------------------------------------------------------------------
def test_fr10_metadata_only():                              # AC-10.1
    ix = idx_mod.build_index(str(FIX))
    store = emb_mod.EmbeddingStore.build(ix, HashingEmbedder())
    by_id = dict(zip(store.ids, store.texts))
    for e in ix.entries:
        for s in e.sections:
            key = f"{e.path}#{s.anchor}"
            assert s.text not in by_id[key], f"full body leaked into embedded corpus: {key}"


def _hit_to_dict(h):  # guard helper kept simple
    return h.to_dict() if isinstance(h, rk.Hit) else h


# --------------------------------------------------------------------------------------
def _run_all():
    import tempfile
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    fails = []
    for t in tests:
        try:
            if t.__name__ == "test_fr6_reload":
                t(tempfile.mkdtemp())
            else:
                t()
            print(f"  PASS  {t.__name__}")
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}"); fails.append(t.__name__)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR {t.__name__}: {type(e).__name__}: {e}"); fails.append(t.__name__)
    # AC-8.1 — lexical core imports zero ML deps (isolated subprocess)
    code = ("import sys; import wiki_router.ranking; "
            "sys.exit(1 if 'numpy' in sys.modules else 0)")
    r = subprocess.run([sys.executable, "-c", code], cwd=str(SERVICE))
    if r.returncode == 0:
        print("  PASS  test_fr8_lexical_zero_ml_import (AC-8.1)")
    else:
        print("  FAIL  test_fr8_lexical_zero_ml_import (AC-8.1): numpy imported by ranking")
        fails.append("AC-8.1")
    print()
    print(f"FAILED: {fails}" if fails else "ALL PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
