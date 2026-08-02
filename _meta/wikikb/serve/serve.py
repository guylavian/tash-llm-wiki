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
    python3 -m wikikb serve --allow-upload               # opt in to PUT /upload (see below); off by default

Endpoints (all JSON; errors are {"error": "..."} with a non-2xx status):
    GET /health                                    -> {"status","domains","pages"}
    GET /route?q=...                               -> {"domains":[...],"confident":bool}
    GET /search?domain=D&q=...&k=5                  -> [{"id","title","score","snippet"}, ...]
    GET /ask?q=...&domain=D&k=5&tier=conceptual     -> same shape as `wikikb ask --json`
    GET /page/<slug>                                -> {"slug","path","frontmatter","body"}
    GET /expand?domain=D&q=...                      -> {"notes":[...]}
    PUT /upload/<domain>/<filename>.pdf             -> {"stored","next"}  (raw body, e.g. `curl -T x.pdf`;
                                                        the ONLY write surface, opt-in via --allow-upload,
                                                        default OFF; see do_PUT for the trust boundary)
    POST /mcp                                       -> MCP Streamable HTTP transport (JSON-RPC 2.0,
                                                        one message per call; no SSE, no sessions — see
                                                        do_mcp_post). DUAL-ERA: serves both the legacy
                                                        `initialize` handshake (2025-11-25 and earlier —
                                                        what n8n and Claude Code speak today) and the
                                                        modern per-request-`_meta` era (2026-07-28+),
                                                        picked per request. GET/DELETE /mcp reply 405 —
                                                        as of 2026-07-28 that is what the spec TELLS a
                                                        server to answer (the GET stream and protocol
                                                        sessions were both removed), and the reference
                                                        TS client already treated it as a non-error.

Auth (opt-in): set WIKIKB_API_TOKEN to require `Authorization: Bearer <token>` on every endpoint
except /health (left open for kubelet-style probes, which can't attach custom headers without a
templating layer this project doesn't have). Unset (the default) keeps today's no-auth, loopback-
only posture — PRODUCTION.md already says not to bind a real interface without this.
"""
import argparse
import base64
import hmac
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

PAGE_DIRS = paths.PAGE_DIRS
# Same slug shape lint.py's LINK_RE / expand.py's PAGELINK_RE use: kebab-case only. This is what makes
# /page/<slug> traversal-safe — a slug containing "." or "/" (e.g. "../CLAUDE") fails the regex before
# any filesystem path is ever built, so there's no path to sanitize.
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# PUT /upload/<domain>/<filename> — same traversal-safe-by-construction idea as SLUG_RE: neither
# group's character class contains "/", so a multi-segment or ".."-laden path simply fails to
# MATCH (falls into the disabled/unknown branch) rather than needing separate sanitizing. Domain
# membership in the taxonomy is still checked separately (do_upload) since that's semantic, not shape.
UPLOAD_RE = re.compile(r"^/upload/([a-z0-9][a-z0-9-]*)/([A-Za-z0-9][A-Za-z0-9._-]*\.pdf)$")
UPLOAD_MAX_BYTES = 50 * 1024 * 1024  # 50 MB cap (CLAUDE.md A3 trust-boundary checklist)
MCP_MAX_BYTES = 2 * 1024 * 1024      # 2 MB cap on a single POST /mcp JSON-RPC body — same idea,
                                      # much smaller ceiling (tool-call args are small text, not a PDF)


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
    # WI-5: consume kb.lexical_rank — the single ranking home — instead of re-deriving scoring
    # here (this path previously omitted corpus IDF/avgdl and alias expansion, so /search could
    # disagree with the CLI/eval ordering for the same query).
    terms, _pool, scored = kb.lexical_rank(domain, q, recs)
    hits = [{"id": r.get("id"), "title": r.get("title"), "score": sc,
             "snippet": kb.snippet(bt, terms) if bt else (r.get("abstract") or "")}
            for sc, r, bt in scored[:k]]
    return 200, hits


def _parse_strict(v):
    """?strict= tri-state: absent -> None (env default decides), '1'/'true' -> True,
    anything else explicit ('0'/'false') -> False — an explicit opt-out beats the env."""
    return None if v is None else v in ("1", "true")


def do_ask(q, domain, k, tier, strict=None):
    if not q:
        return 400, {"error": "missing q"}
    st = askmod.ask(q, domain=domain, k=k, question_tier=tier)
    refs = askmod.references(st.get("domain"), st.get("used", []))
    # WI-7: the shared serializer — same shape as `wikikb ask --json` and the mcp ask tool, with
    # grounding status always structured; strict: per-call tri-state over WIKI_STRICT_GROUNDING.
    return 200, askmod.public_result(q, st, refs, strict=askmod.resolve_strict(strict))


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


def _check_auth(headers):
    """Bearer-token gate, opt-in via WIKIKB_API_TOKEN — unset (the loopback-only default) skips the
    check entirely, matching serve.py's existing no-auth posture. n8n's Bearer-Auth credential sends
    exactly this header shape (RESEARCH 1: "Bearer Auth is implemented as Header auth with
    Authorization: Bearer <token>"). Returns a (status, obj) tuple to reply on failure, or None to
    proceed. hmac.compare_digest avoids a timing side-channel on the comparison."""
    token = os.environ.get("WIKIKB_API_TOKEN")
    if not token:
        return None
    got = headers.get("Authorization", "")
    prefix = "Bearer "
    # Compare BYTES, not str: hmac.compare_digest raises TypeError("comparing strings with non-ASCII
    # characters is not supported") on a str containing non-ASCII, and this runs BEFORE the handlers'
    # try/except — so an `Authorization: Bearer tökén` from any unauthenticated caller killed the
    # request thread and returned a dead connection (curl exit 52) plus a stderr traceback instead of
    # a clean 401. Encoding both sides makes the comparison total for arbitrary header bytes while
    # keeping the constant-time property, which is the only reason compare_digest is here.
    if not got.startswith(prefix) or not hmac.compare_digest(
            got[len(prefix):].encode("utf-8"), token.encode("utf-8")):
        return 401, {"error": "unauthorized"}
    return None


def _check_origin(origin):
    """DNS-rebinding guard for /mcp — mandatory since MCP spec 2025-03-26 ("servers MUST validate
    the Origin header on all incoming connections"); the 2025-11-25 revision further requires 403
    specifically when Origin is present-but-invalid (RESEARCH 2). A non-browser client (n8n's
    backend, curl, this repo's own tools) never sends an Origin header, so the default empty
    allowlist only ever blocks a browser page reaching this endpoint cross-origin — the exact
    attack the MUST exists to stop — without touching the real consumer. Widen via
    WIKIKB_MCP_ALLOWED_ORIGINS (comma-separated) if a browser-based caller is ever added."""
    if origin is None:
        return None
    allowed = {o.strip() for o in os.environ.get("WIKIKB_MCP_ALLOWED_ORIGINS", "").split(",") if o.strip()}
    if origin not in allowed:
        return 403, {"error": "origin not allowed"}
    return None


# --- MCP 2026-07-28 (modern era) HTTP bindings -------------------------------------------------
# Everything below applies ONLY to requests carrying modern per-request `_meta` (mcp.is_modern).
# Legacy requests — which is every client working today, n8n included — bypass all of it and keep
# their exact previous behavior. That asymmetry is the whole safety property of the dual-era change.

MCP_B64_PREFIX = "=?base64?"
MCP_B64_SUFFIX = "?="
# Which body field `Mcp-Name` mirrors, per method (transports #standard-request-headers).
MCP_NAME_SOURCE = {"tools/call": "name", "prompts/get": "name", "resources/read": "uri"}
# Modern protocol errors carry an HTTP status; legacy keeps every JSON-RPC error at 200 (in that era
# they're protocol-level, not HTTP-level). Codes are spec literals, not imports — wikikb.mcp.mcp
# imports THIS module, so a module-scope import back would be circular (same reason do_mcp_post
# defers its own import).
MCP_MODERN_ERROR_STATUS = {
    -32020: 400,   # HeaderMismatch
    -32021: 400,   # MissingRequiredClientCapability
    -32022: 400,   # UnsupportedProtocolVersion
    -32602: 400,   # Invalid params — a required `_meta` field was missing
    -32601: 404,   # Method not found: 404, NOT 200. The JSON-RPC error body is what distinguishes
                   # this from the bare 404 a legacy HTTP+SSE server gives (transports, backward-compat)
}


def _decode_header_value(v):
    """Undo the Base64 sentinel encoding `=?base64?...?=` (transports #value-encoding).

    Servers MUST decode an encoded `Mcp-Name` value BEFORE comparing it to the request body, or every
    non-ASCII tool name would false-positive as a mismatch. A value carrying the markers but holding
    invalid base64 is returned AS-IS so it simply loses the comparison and yields a clean 400 — never
    a 500 out of a decoder on attacker-controlled bytes."""
    if isinstance(v, str) and v.startswith(MCP_B64_PREFIX) and v.endswith(MCP_B64_SUFFIX):
        try:
            return base64.b64decode(v[len(MCP_B64_PREFIX):-len(MCP_B64_SUFFIX)],
                                    validate=True).decode("utf-8")
        except (ValueError, UnicodeDecodeError):        # binascii.Error subclasses ValueError
            return v
    return v


def _validate_mcp_headers(req, headers):
    """Modern-era header/body cross-check -> a `-32020` HeaderMismatch error object, or None if OK.

    The transport mirrors selected body fields into HTTP headers so intermediaries (an OpenShift
    Route, a load balancer, a rate limiter) can route and inspect without parsing the body. The
    server MUST reject any request where header and body disagree — otherwise the intermediary
    routing on the header and this server executing on the body are acting on different truths, which
    is the exact vulnerability the requirement exists to close."""
    from wikikb.mcp import mcp as mcpmod
    msg_id = req.get("id")
    # An http.server `headers` is an email.message.Message: .get() is case-INSENSITIVE, which is what
    # the spec requires for field names. A plain dict (direct callers/tests) is not, but is only ever
    # populated by those callers themselves.
    got = {} if headers is None else headers

    def mismatch(msg):
        return {"jsonrpc": "2.0", "id": msg_id,
                "error": {"code": -32020, "message": "Header mismatch: " + msg}}

    checks = [("MCP-Protocol-Version", mcpmod.request_meta(req).get(mcpmod.META_VERSION), True),
              ("Mcp-Method", req.get("method"), True)]
    field = MCP_NAME_SOURCE.get(req.get("method"))
    if field:
        checks.append(("Mcp-Name", (req.get("params") or {}).get(field), True))

    for name, body_value, required in checks:
        hdr = got.get(name)
        if hdr is None:
            if required:
                return mismatch("%s header is required" % name)
            continue
        if _decode_header_value(hdr) != body_value:
            return mismatch("%s header value %r does not match body value %r" % (name, hdr, body_value))
    return None


def do_mcp_post(raw_body, session=None, headers=None):
    """POST /mcp body -> (status, obj-or-None). One JSON-RPC 2.0 message in, one out — batching was
    removed from the spec in 2025-06-18 and stays removed in 2025-11-25 (RESEARCH 2), so no array
    handling is needed. obj is None for a notification, which MUST get 202 Accepted with no body;
    a request always gets a single JSON-RPC response object at 200 (JSON-RPC errors are protocol-
    level, not HTTP-level, per the same research). `session` is the caller's Mcp-Session-Id header
    if it sent one (None otherwise — the common case: this server never issues one, so a spec-
    compliant client has none to send back — see mcp.handle()'s docstring); it only scopes the F2
    tool-result budget counter, nothing else. Deferred import: wikikb.mcp.mcp imports
    do_page/do_route/do_search FROM this module, so importing it back at module load time here
    would be circular; by the time a request lands, both modules are already fully loaded, so a
    call-scoped import breaks the cycle — same TOOLS/DISPATCH/handle() the stdio transport uses,
    nothing re-implemented (CLAUDE.md's faithfulness invariant)."""
    from wikikb.mcp import mcp as mcpmod
    try:
        req = json.loads(raw_body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return 200, {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}
    if not isinstance(req, dict) or "method" not in req:
        return 200, {"jsonrpc": "2.0", "id": req.get("id") if isinstance(req, dict) else None,
                     "error": {"code": -32600, "message": "invalid request"}}
    if mcpmod.is_modern(req):
        # Header validation runs BEFORE dispatch: a header/body disagreement means we cannot trust
        # which of the two the request actually meant, so nothing should execute on either.
        err = _validate_mcp_headers(req, headers)
        if err is not None:
            return 400, err
    resp = mcpmod.handle(req, session=session)
    if resp is None:
        return 202, None                                 # notification: 202 Accepted, no body (both eras)
    if mcpmod.is_modern(req):
        code = (resp.get("error") or {}).get("code")
        return MCP_MODERN_ERROR_STATUS.get(code, 200), resp
    return 200, resp                                     # legacy: unchanged — always 200


def _no_such_endpoint():
    """The exact (status, body) do_GET gives an unknown path. do_PUT reuses this UNCHANGED for both
    "uploads are disabled" and "path doesn't look like /upload/<domain>/<file>.pdf" — deliberately
    NOT echoing the requested path back, so the two cases (and an ordinary unknown GET) are
    byte-identical and a disabled/absent upload surface is unfingerprintable (CLAUDE.md A3)."""
    return 404, {"error": "no such endpoint"}


def do_upload(domain, filename, content_length_header, rfile):
    """PUT /upload/<domain>/<filename> body -> _sources/<domain>/_raw/pdfs/<filename>.
    Called only once do_PUT has confirmed uploads are enabled and the path matched UPLOAD_RE
    (so domain/filename are already shape-clean); this does the remaining trust-boundary checks:
    domain membership, Content-Length presence/cap, %PDF magic, and a realpath containment
    assert before ever touching the filesystem. Returns (status, json-able-object)."""
    if domain not in tags.load_domains():
        return 400, {"error": "unknown domain: %s (see GET /health)" % domain}

    if content_length_header is None:
        return 411, {"error": "Content-Length required"}
    try:
        length = int(content_length_header)
    except ValueError:
        return 400, {"error": "invalid Content-Length"}
    if length < 0:
        return 400, {"error": "invalid Content-Length"}
    if length > UPLOAD_MAX_BYTES:
        return 413, {"error": "payload too large (max %d bytes)" % UPLOAD_MAX_BYTES}

    body = rfile.read(length)               # exactly `length` bytes — never more, never less
    if len(body) != length:
        return 400, {"error": "short read: expected %d bytes, got %d" % (length, len(body))}
    if not body.startswith(b"%PDF"):
        return 415, {"error": "not a PDF (missing %PDF magic bytes)"}

    staging_dir = os.path.join(WIKI, "_sources", domain, "_raw", "pdfs")
    target = os.path.join(staging_dir, filename)
    # Defense-in-depth vs a planted symlink somewhere in the existing path chain: UPLOAD_RE already
    # forbids "/" and ".." inside domain/filename, but realpath containment is the belt-and-braces
    # check CLAUDE.md's checklist calls for before any write. realpath() works fine on paths that
    # don't exist yet (it just normalizes the non-existent tail lexically).
    root_real = os.path.realpath(WIKI) + os.sep
    if not os.path.realpath(staging_dir).startswith(root_real) or not os.path.realpath(target).startswith(root_real):
        return 400, {"error": "invalid target path"}

    os.makedirs(staging_dir, exist_ok=True)
    try:
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except FileExistsError:
        return 409, {"error": "already exists: %s" % filename}
    with os.fdopen(fd, "wb") as fh:
        fh.write(body)

    return 201, {
        "stored": os.path.relpath(target, WIKI),
        "next": ("python3 -m wikikb pdf_to_corpus --src _sources/%s/_raw/pdfs --domain %s --apply"
                 % (domain, domain)),
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "wikikb-serve/1.0"

    # Slowloris guard. Both write-side handlers read EXACTLY Content-Length bytes off the socket
    # (do_POST for /mcp, do_PUT for /upload), so a client that declares 500 bytes, sends 16, and then
    # goes silent parks that worker thread forever — verified: no response after 20s, thread still in
    # rfile.read(). ThreadingHTTPServer spawns a thread per connection with no cap, so a handful of
    # such connections is a cheap resource-exhaustion DoS on anything reachable through a Route.
    # socketserver.StreamRequestHandler.setup() applies this attribute with connection.settimeout(),
    # so setting it here fixes EVERY request path at once (including the pre-existing upload one)
    # rather than bolting a deadline onto each read. A stalled read now raises socket.timeout, the
    # handler thread unwinds, and the connection is closed.
    # ponytail: one blunt per-connection deadline, not a token-bucket/read-loop budget. 30s is far
    # above the slowest measured request (~2.8s /ask on the largest corpus) and far below "forever".
    timeout = 30

    def _reply(self, status, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _reply_no_body(self, status):
        """202 Accepted for an MCP notification — the spec requires no body, so _reply's fixed
        application/json Content-Length:0 body would be wrong here."""
        self.send_response(status)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        parts = urlsplit(self.path)
        qs = {k: v[0] for k, v in parse_qs(parts.query).items()}
        path = parts.path.rstrip("/") or "/"
        if path != "/health":                               # left open for unauthenticated kubelet probes
            err = _check_auth(self.headers)
            if err:
                self._reply(*err)
                return
        try:
            if path == "/health":
                status, obj = do_health()
            elif path == "/route":
                status, obj = do_route(qs.get("q", ""))
            elif path == "/search":
                status, obj = do_search(qs.get("domain"), qs.get("q", ""), int(qs.get("k", 5)))
            elif path == "/ask":
                status, obj = do_ask(qs.get("q", ""), qs.get("domain"), int(qs.get("k", 5)), qs.get("tier"),
                                     strict=_parse_strict(qs.get("strict")))
            elif path == "/expand":
                status, obj = do_expand(qs.get("domain"), qs.get("q", ""))
            elif path.startswith("/page/"):
                status, obj = do_page(path[len("/page/"):], int(qs.get("offset", 0)),
                                      int(qs.get("max_chars", PAGE_MAX_CHARS)))
            elif path == "/mcp":
                # Declining the optional standalone SSE stream is spec-legal (transports#GET item 3);
                # the reference TS SDK client treats 405 here as an expected non-error (RESEARCH 2).
                status, obj = 405, {"error": "GET not supported at /mcp (no standalone SSE stream; "
                                             "use POST /mcp)"}
            else:
                status, obj = _no_such_endpoint()
        except Exception as e:                              # noqa: BLE001 — a bad request must never kill the thread
            status, obj = 500, {"error": str(e)}
        self._reply(status, obj)
        # one line per request to stderr; BaseHTTPRequestHandler's default log_message already
        # does this via send_response() -> log_request(), so nothing further is needed here.

    def do_POST(self):
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if path != "/mcp":
            self._reply(*_no_such_endpoint())
            return
        err = _check_auth(self.headers)
        if err:
            self._reply(*err)
            return
        err = _check_origin(self.headers.get("Origin"))
        if err:
            self._reply(*err)
            return
        # Same cap-and-validate shape as do_upload's Content-Length handling above — required,
        # numeric, bounded — just a much smaller ceiling: a JSON-RPC tool-call body is small text,
        # not a PDF, so MCP_MAX_BYTES only needs to be generous headroom against a hostile/broken
        # body, not a real per-tool budget (that's the F1/F2 counters in mcp.py's own job).
        length_header = self.headers.get("Content-Length")
        if length_header is None:
            self._reply(411, {"error": "Content-Length required"})
            return
        try:
            length = int(length_header)
        except ValueError:
            self._reply(400, {"error": "invalid Content-Length"})
            return
        if length < 0 or length > MCP_MAX_BYTES:
            self._reply(413, {"error": "payload too large (max %d bytes)" % MCP_MAX_BYTES})
            return
        raw = self.rfile.read(length)
        if len(raw) != length:
            self._reply(400, {"error": "short read: expected %d bytes, got %d" % (length, len(raw))})
            return
        try:
            status, obj = do_mcp_post(raw, session=self.headers.get("Mcp-Session-Id"),
                                      headers=self.headers)
        except Exception as e:                              # noqa: BLE001 — a bad request must never kill the thread
            status, obj = 500, {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}
        if obj is None:
            self._reply_no_body(status)
        else:
            self._reply(status, obj)

    def do_DELETE(self):
        # No stateful sessions (serve.py issues no Mcp-Session-Id — RESEARCH 2's recommended, spec-
        # legal design), so explicit session termination is declined via 405, same as GET's SSE decline.
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if path == "/mcp":
            err = _check_auth(self.headers)
            self._reply(*(err or (405, {"error": "session termination not supported"})))
        else:
            self._reply(*_no_such_endpoint())

    def do_PUT(self):
        # Defined UNCONDITIONALLY (not only when --allow-upload) — a conditional do_PUT would leak a
        # stdlib 501 "Unsupported method" for a disabled server, fingerprinting that uploads exist but
        # are off. The allow-flag check lives INSIDE, and both it and "path doesn't match" fall through
        # to the SAME _no_such_endpoint() an unknown GET path gives, so the two are indistinguishable.
        path = urlsplit(self.path).path.rstrip("/") or "/"
        err = _check_auth(self.headers)
        if err:
            self._reply(*err)
            return
        if not getattr(self.server, "allow_upload", False):
            status, obj = _no_such_endpoint()
            self._reply(status, obj)
            return
        m = UPLOAD_RE.match(path)
        if not m:
            status, obj = _no_such_endpoint()
            self._reply(status, obj)
            return
        try:
            status, obj = do_upload(m.group(1), m.group(2), self.headers.get("Content-Length"), self.rfile)
        except Exception as e:                              # noqa: BLE001 — a bad request must never kill the thread
            status, obj = 500, {"error": str(e)}
        self._reply(status, obj)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8642)
    ap.add_argument("--bind", default="127.0.0.1",
                    help="loopback by default (127.0.0.1); binding a real interface is the operator's "
                         "explicit choice")
    ap.add_argument("--allow-upload", action="store_true",
                    help="enable PUT /upload/<domain>/<file>.pdf (default OFF; writes only into "
                         "_sources/<domain>/_raw/pdfs/, never the immutable reference tier)")
    args = ap.parse_args()
    # Pre-warm the two module-level read caches (route.py's domain profiles, expand.py's page graph)
    # ONCE here, single-threaded, before ThreadingHTTPServer starts handing requests to worker threads.
    # After this point every request only READS them — no locking needed (ponytail: a shared mutable
    # cache would need one; a pre-warmed read-only one doesn't).
    routemod.build_profiles()
    expandmod.load_pages()
    httpd = ThreadingHTTPServer((args.bind, args.port), Handler)
    httpd.allow_upload = args.allow_upload    # read-only per-request via self.server; never mutated after this
    # Print which auth posture is live — an operator staring at a fresh container's logs needs to see
    # at a glance whether WIKIKB_API_TOKEN was actually picked up, not just trust that they set it.
    auth_mode = "auth: Bearer token required" if os.environ.get("WIKIKB_API_TOKEN") else "auth: OFF (set WIKIKB_API_TOKEN to require it)"
    print("wikikb serve: http://%s:%d  (Ctrl-C to stop)%s  [%s]" % (
        args.bind, args.port, "  [uploads ENABLED]" if args.allow_upload else "", auth_mode), file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
