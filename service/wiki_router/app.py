"""app.py — T4. FastAPI serving layer: /route /get /reload /healthz /metrics.

Atomic index swap (NFR-1), admin-gated reload (FR-6), provenance everywhere (FR-5),
path safety (NFR-4). Prometheus text is hand-rolled to keep deps minimal & offline.
"""
from __future__ import annotations

import logging
import time

from fastapi import FastAPI, Header, Query, Request, Response
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel

from .config import Config
from .index import build_index, is_source_only, posix, resolve_safe, _split_frontmatter
from .ranking import Hit, candidates_for_query, make_ranker

log = logging.getLogger("wiki_router.app")


class RouteRequest(BaseModel):
    query: str
    k: int | None = None
    version: str | None = None
    domain: str | None = None
    type: str | None = None


class _State:
    """Mutable holder; attribute assignment is the atomic swap (NFR-1)."""
    def __init__(self, config: Config):
        self.config = config
        self.index = build_index(config.repo_root, built_at=time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        self.ranker = make_ranker(config, self.index)
        self.metrics = {"route": 0, "get": 0, "reload": 0}

    def reload(self):
        idx = build_index(self.config.repo_root, built_at=time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        ranker = make_ranker(self.config, idx)
        self.index, self.ranker = idx, ranker      # atomic swap (readers see old or new, never partial)


def create_app(config: Config | None = None) -> FastAPI:
    cfg = config or Config.from_env()
    app = FastAPI(title="LLM-Wiki Serving Layer", version="1.0")
    st = _State(cfg)
    app.state.st = st

    @app.post("/route")
    def route(req: RouteRequest):                                  # FR-2
        st.metrics["route"] += 1
        k = req.k or cfg.default_k
        k = max(1, min(50, k))
        cands = candidates_for_query(st.index, req.query)
        hits = st.ranker.rank(req.query, cands, version=req.version,
                              domain=req.domain, type=req.type, k=k)  # FR-3 inside
        return [h.to_dict() for h in hits]                          # FR-5 provenance in each

    @app.get("/get")
    def get(path: str = Query(...), section: str | None = Query(None)):   # FR-4, NFR-4
        st.metrics["get"] += 1
        rel = posix(path)
        safe = resolve_safe(cfg.repo_root, rel)
        if safe is None:
            return JSONResponse({"reason": "unsafe-path"}, status_code=400)   # AC-NFR4
        if is_source_only(rel):
            return JSONResponse({"reason": "source-only"}, status_code=404)   # AC-4.3
        entry = next((e for e in st.index.entries if e.path == rel), None)
        if entry is None:
            if not safe.exists():
                return JSONResponse({"reason": "not-found"}, status_code=404)
            fm, _ = _split_frontmatter(safe.read_text(encoding="utf-8"))
            if not isinstance(fm, dict) or fm.get("routable") is not True:
                return JSONResponse({"reason": "not-routable"}, status_code=404)  # AC-4.4
            return JSONResponse({"reason": "not-found"}, status_code=404)
        prov = list(entry.frontmatter.get("source_provenance") or [])           # FR-5
        if entry.inject == "full":                                              # AC-4.2
            body = "\n".join(s.text for s in entry.sections)
            return {"path": entry.path, "section": None, "inject": "full",
                    "frontmatter": dict(entry.frontmatter), "body": body,
                    "source_provenance": prov}
        anchor = section or entry.sections[0].anchor                            # AC-4.1
        sec = next((s for s in entry.sections if s.anchor == anchor), None)
        if sec is None:
            return JSONResponse({"reason": "no-section"}, status_code=404)
        return {"path": entry.path, "section": sec.anchor, "inject": "section",
                "frontmatter": dict(entry.frontmatter), "body": sec.text,
                "source_provenance": prov}

    @app.post("/reload")
    def reload(x_admin_token: str | None = Header(None)):                       # FR-6
        if not cfg.admin_token or x_admin_token != cfg.admin_token:
            return JSONResponse({"reason": "unauthorized"}, status_code=401)    # AC-6.1
        st.reload()
        st.metrics["reload"] += 1
        n_sec = sum(len(e.sections) for e in st.index.entries)
        return {"reloaded": True, "files": len(st.index.entries), "sections": n_sec}

    @app.get("/healthz")
    def healthz():                                                             # FR-7
        n_sec = sum(len(e.sections) for e in st.index.entries)
        return {"status": "ok", "files": len(st.index.entries), "sections": n_sec,
                "ranker": st.ranker.name, "version_filter": True}

    @app.get("/metrics")
    def metrics():                                                             # FR-7
        n_sec = sum(len(e.sections) for e in st.index.entries)
        lines = [
            "# TYPE wiki_route_requests_total counter",
            f"wiki_route_requests_total {st.metrics['route']}",
            "# TYPE wiki_get_requests_total counter",
            f"wiki_get_requests_total {st.metrics['get']}",
            "# TYPE wiki_reload_total counter",
            f"wiki_reload_total {st.metrics['reload']}",
            "# TYPE wiki_index_files gauge",
            f"wiki_index_files {len(st.index.entries)}",
            "# TYPE wiki_index_sections gauge",
            f"wiki_index_sections {n_sec}",
        ]
        return PlainTextResponse("\n".join(lines) + "\n")

    return app


# uvicorn entrypoint (factory — avoids an import-time repo scan):
#   uvicorn wiki_router.app:create_app --factory
