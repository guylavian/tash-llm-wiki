#!/usr/bin/env python3
"""serve.py — stateless JSON API over the wiki, for SRE/agent consumption. stdlib only, no network deps.

Why: an SRE-facing agent shouldn't have to shell out to `python3 -m wikikb <tool>` per lookup. This
wraps the SAME functions the CLI tools call — route.route, kb.load/score/snippet, expand.graph_notes,
ask.ask — behind a small HTTP surface and returns their result as JSON. Nothing is re-implemented (the
faithfulness invariant the rest of the toolchain follows): a handler is a thin translation from query
params to a function call to a JSON body.

stdlib only: http.server.ThreadingHTTPServer + urllib.parse + json. No socket opens at import time —
the listener binds inside main(). Default bind is 127.0.0.1 (loopback only); binding a real interface
(--bind 0.0.0.0/<lan-ip>) is the operator's explicit choice, not this module's default.

Usage:
    python3 -m wikikb serve                             # http://127.0.0.1:8642
    python3 -m wikikb serve --port 9000 --bind 0.0.0.0   # operator's explicit non-loopback choice

Endpoints (all GET, all JSON; errors are {"error": "..."} with a non-2xx status):
    GET /health                                    -> {"status","domains","pages"}
    GET /route?q=...                               -> {"domains":[...],"confident":bool}
    GET /search?domain=D&q=...&k=5                  -> [{"id","title","score","snippet"}, ...]
    GET /ask?q=...&domain=D&k=5&tier=conceptual     -> same shape as `wikikb ask --json`
    GET /page/<slug>                                -> {"slug","path","frontmatter","body"}
    GET /expand?domain=D&q=...                      -> {"notes":[...]}
"""
import argparse
import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

from wikikb import paths
WIKI = str(paths.WIKI)
sys.dont_write_bytecode = True

from wikikb.build import tags                  # tags.load_domains() — the SAME loader lint.py validates against
from wikikb.quality import lint as lintmod      # lint.page_files() — page count, no re-parsing
from wikikb.retrieval import route as routemod
from wikikb.retrieval import kb
from wikikb.retrieval import expand as expandmod
from wikikb.graph import ask as askmod

PAGE_DIRS = ("topics", "entities", "questions")
# Same slug shape lint.py's LINK_RE / expand.py's PAGELINK_RE use: kebab-case only. This is what makes
# /page/<slug> traversal-safe — a slug containing "." or "/" (e.g. "../CLAUDE") fails the regex before
# any filesystem path is ever built, so there's no path to sanitize.
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def _frontmatter_and_body(text):
    """The same tiny top-level-scalar frontmatter split index.py/lint.py/expand.py each carry
    locally — not centralized there, so not centralized here either."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if line and not line[0].isspace() and ":" in line and not line.startswith(("-", "#")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip("\"'")
    return fm, text[m.end():].lstrip("\n")


def find_page(slug):
    """slug -> (dir, path) inside topics/entities/questions ONLY, or (None, None)."""
    for d in PAGE_DIRS:
        p = os.path.join(WIKI, d, slug + ".md")
        if os.path.isfile(p):
            return d, p
    return None, None


# ---------- endpoint handlers: (status, json-able-object) --------------------------------------

def do_health():
    domains = sorted(tags.load_domains())
    pages = sum(1 for _ in lintmod.page_files())
    return 200, {"status": "ok", "domains": domains, "pages": pages}


def do_route(q):
    if not q:
        return 400, {"error": "missing q"}
    domains, confident = routemod.route(q)
    return 200, {"domains": domains, "confident": confident}


def do_search(domain, q, k):
    if not domain or not q:
        return 400, {"error": "domain and q are required"}
    recs = kb.load(domain)
    if recs is None:
        return 404, {"error": "no reference tier for domain %r (see GET /health for available domains)" % domain}
    pool = [r for r in recs if r.get("body_status") == "fetched"]
    terms = kb.toks(q)
    scored = []
    for r in pool:
        bt = kb.body_text(r)
        sc = kb.score(r, terms, bt)              # same call kb.cmd_search makes per candidate
        if sc > 0:
            scored.append((sc, r, bt))
    scored.sort(key=lambda x: (-x[0], -kb.vkey(x[1].get("version"))[0] if x[1].get("version") else 0))
    hits = [{"id": r.get("id"), "title": r.get("title"), "score": sc,
             "snippet": kb.snippet(bt, terms) if bt else (r.get("abstract") or "")}
            for sc, r, bt in scored[:k]]
    return 200, hits


def do_ask(q, domain, k, tier):
    if not q:
        return 400, {"error": "missing q"}
    st = askmod.ask(q, domain=domain, k=k, question_tier=tier)
    refs = askmod.references(st.get("domain"), st.get("used", []))
    return 200, {
        "query": q, "domain": st.get("domain"), "confident": st.get("confident"),
        "thin": st.get("thin"), "banner": st.get("banner") or [],
        "answer": st.get("answer", ""), "references": refs,
    }


# F1 (100k-budget plan): a page/note body is served in bounded slices, never whole-file. 8k chars
# (~2k tok) bounds the per-call cost; `offset` keeps every byte reachable for the caller that
# genuinely needs more. Whole-line cut so a slice never ends mid-sentence/mid-table-row.
PAGE_MAX_CHARS = 8000


def _slice_body(body, offset, max_chars):
    total = len(body)
    offset = max(0, min(offset, total))
    end = min(offset + max_chars, total)
    if end < total:                                  # cut back to the last whole line
        nl = body.rfind("\n", offset, end)
        if nl > offset:
            end = nl
    return body[offset:end], total, (end if end < total else None)


def do_page(slug, offset=0, max_chars=PAGE_MAX_CHARS):
    if not SLUG_RE.match(slug or ""):
        return 400, {"error": "invalid slug"}
    d, path = find_page(slug)
    if not path:
        return 404, {"error": "no such page: %s" % slug}
    fm, body = _frontmatter_and_body(open(path, encoding="utf-8").read())
    max_chars = max(1, min(int(max_chars or PAGE_MAX_CHARS), PAGE_MAX_CHARS))
    piece, total, nxt = _slice_body(body, int(offset or 0), max_chars)
    out = {"slug": slug, "path": "%s/%s.md" % (d, slug), "frontmatter": fm, "body": piece,
           "body_total_chars": total}
    if nxt is not None:
        out["truncated"] = True
        out["next_offset"] = nxt
    return 200, out


def do_expand(domain, q):
    if not domain or not q:
        return 400, {"error": "domain and q are required"}
    notes = sorted(expandmod.graph_notes(domain, q) or set())
    # F3: snippets alongside ids — multi-hop triage must not cost one full-body read per note.
    terms = kb.toks(q)
    by_id = {r.get("id"): r for r in (kb.load(domain) or [])}
    out = []
    for nid in notes:
        r = by_id.get(nid)
        bt = kb.body_text(r) if r else ""
        out.append({"id": nid, "snippet": kb.snippet(bt, terms) if bt else ""})
    return 200, {"notes": notes, "previews": out}


class Handler(BaseHTTPRequestHandler):
    server_version = "wikikb-serve/1.0"

    def _reply(self, status, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parts = urlsplit(self.path)
        qs = {k: v[0] for k, v in parse_qs(parts.query).items()}
        path = parts.path.rstrip("/") or "/"
        try:
            if path == "/health":
                status, obj = do_health()
            elif path == "/route":
                status, obj = do_route(qs.get("q", ""))
            elif path == "/search":
                status, obj = do_search(qs.get("domain"), qs.get("q", ""), int(qs.get("k", 5)))
            elif path == "/ask":
                status, obj = do_ask(qs.get("q", ""), qs.get("domain"), int(qs.get("k", 5)), qs.get("tier"))
            elif path == "/expand":
                status, obj = do_expand(qs.get("domain"), qs.get("q", ""))
            elif path.startswith("/page/"):
                status, obj = do_page(path[len("/page/"):], int(qs.get("offset", 0)),
                                      int(qs.get("max_chars", PAGE_MAX_CHARS)))
            else:
                status, obj = 404, {"error": "no such endpoint: %s" % path}
        except Exception as e:                              # noqa: BLE001 — a bad request must never kill the thread
            status, obj = 500, {"error": str(e)}
        self._reply(status, obj)
        # one line per request to stderr; BaseHTTPRequestHandler's default log_message already
        # does this via send_response() -> log_request(), so nothing further is needed here.


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8642)
    ap.add_argument("--bind", default="127.0.0.1",
                    help="loopback by default (127.0.0.1); binding a real interface is the operator's "
                         "explicit choice")
    args = ap.parse_args()
    # Pre-warm the two module-level read caches (route.py's domain profiles, expand.py's page graph)
    # ONCE here, single-threaded, before ThreadingHTTPServer starts handing requests to worker threads.
    # After this point every request only READS them — no locking needed (ponytail: a shared mutable
    # cache would need one; a pre-warmed read-only one doesn't).
    routemod.build_profiles()
    expandmod.load_pages()
    httpd = ThreadingHTTPServer((args.bind, args.port), Handler)
    print("wikikb serve: http://%s:%d  (Ctrl-C to stop)" % (args.bind, args.port), file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
