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

OPERATION MODES (WIKIKB_MODE — see wikikb/modes.py for the full contract):
    airgapped (default)  everything below EXCEPT the /scrape surface, which answers exactly like an
                         unknown path — so an online-only endpoint is not fingerprintable on a
                         sealed box. No outbound connection is ever opened.
    online               the same surface PLUS the web-harvest endpoints: /scrape, /scrape/sources,
                         /scrape/cron, and the scheduled harvest that drives them.
The modes are additive: `online` is a strict superset, so a client written against an airgapped
instance keeps working verbatim against an online one. An unknown WIKIKB_MODE value REFUSES TO
START (exit 2) rather than falling back to a default — a mode is a posture, and silently getting
the wrong one in either direction is the failure that check exists for.

Usage:
    python3 -m wikikb serve                             # http://127.0.0.1:8642
    python3 -m wikikb serve --port 9000 --bind 0.0.0.0   # operator's explicit non-loopback choice
    python3 -m wikikb serve --allow-upload               # opt in to PUT /upload (see below); off by default
    WIKIKB_MODE=online python3 -m wikikb serve           # + the web-scraper surface

Endpoints (all JSON; errors are {"error": "..."} with a non-2xx status):
    GET /health                                    -> {"status","mode","capabilities","domains","pages"}
    GET /route?q=...                               -> {"domains":[...],"confident":bool}
    GET /search?domain=D&q=...&k=5                  -> [{"id","title","score","snippet"}, ...]
    GET /ask?q=...&domain=D&k=5&tier=conceptual     -> same shape as `wikikb ask --json`
    GET /page/<slug>                                -> {"slug","path","frontmatter","body",
                                                        "body_total_chars"[,"truncated","next_offset"]}
    GET /expand?domain=D&q=...                      -> {"notes":[...],"previews":[{"id","snippet"}]}
    GET /openapi.json                               -> OpenAPI 3.1 document, built from the LIVE
                                                        config (MCP mount point, auth posture,
                                                        resolved vault) so it can't drift
    GET /docs                                       -> self-contained HTML API reference; no CDN,
                                                        no vendored JS, renders air-gapped. Documents
                                                        each endpoint's INPUT and OUTPUT structure and
                                                        carries a per-operation "Try it" panel that
                                                        calls this instance same-origin (Postman /
                                                        Swagger UI still work off /openapi.json)
    PUT /upload/<domain>/<filename>.pdf             -> {"stored","job_id","status_url"}  (raw body, e.g.
                                                        `curl -T x.pdf`; opt-in via --allow-upload, default
                                                        OFF; see do_PUT for the trust boundary). Storing the
                                                        file also QUEUES the conversion chain — pdf→corpus→
                                                        immutable reference notes→crosslink — as a background
                                                        job; poll it at /jobs/<id>. WIKIKB_AUTO_INGEST=0
                                                        keeps the old store-only behaviour.
    POST /ingest/<domain>                           -> {"job_id","status_url"}  (queue the same chain by
                                                        hand: the batch path — drop several PDFs, ingest
                                                        once. Same opt-in as /upload.)
    GET /jobs                                       -> {"jobs":[...],"stats":{...}}
    GET /jobs/<id>                                  -> {"id","state","steps","results",...}
    GET    /domains                                 -> The full CRUD for the DOMAIN DECLARATIONS in
    POST   /domains                                    vault/taxonomy.md (what /health lists, what every
    GET    /domains/<name>                             page's `domain:` is validated against, what the
    PATCH  /domains/<name>                             router routes to and the Confidence gate reads
    DELETE /domains/<name>[?force=true]                tiers-covered from). GET lists / reads one (+ what
                                                        depends on it); POST declares one — ADD-DOMAIN
                                                        steps 2-4: the block, any new `areas:`, and the
                                                        _sources/<name>/ raw tier; PATCH is partial (the
                                                        NAME is identity and is NOT patchable — it is
                                                        every page's `domain:` and the reference/<name>/
                                                        directory); DELETE undeclares it and answers 409
                                                        while pages still use it. Removal NEVER deletes a
                                                        page or the immutable tiers — that is RETRACT.
                                                        BOTH modes (vault config opens no socket); the
                                                        writes share --allow-upload.
    GET   /scrape/sources                           -> ONLINE MODE ONLY. The full CRUD for the watchlist of
    POST  /scrape/sources                              websites this vault harvests. GET lists them (+ the
    PATCH /scrape/sources                              cron status); POST adds {"url","domain",...}; PATCH
    DELETE /scrape/sources?url=…                       updates one by url (partial — only the fields you
                                                        send; the url itself is identity and is NOT
                                                        patchable, rename = DELETE + POST); DELETE removes
                                                        it (harvested notes are KEPT — the raw tier is
                                                        immutable; withdrawing knowledge is RETRACT).
    POST /scrape                                    -> ONLINE MODE ONLY. Harvest now: {} = every enabled
                                                        watchlist source (one job per domain); {"url","domain"}
                                                        = one URL, watchlist or not. Queued on the SAME
                                                        serialized runner as /ingest -> {"queued":[{job_id}]}.
    GET  /scrape/cron                               -> ONLINE MODE ONLY. Scheduled-harvest status:
    POST /scrape/cron {"enabled":bool}                 schedule, next/last run, live vs boot-default
                                                        enabled. POST toggles it at runtime (default ON,
                                                        env WIKIKB_SCRAPE_CRON / _CRON_ENABLED).
                                                        In airgapped mode ALL of the above are
                                                        indistinguishable from an unknown path; the
                                                        writing ones also require --allow-upload.
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

from wikikb import bootstrap             # vault skeleton creation — called from main(), not at import
from wikikb import modes
from wikikb import paths
WIKI = str(paths.WIKI)
sys.dont_write_bytecode = True

from wikikb.build import tags                  # tags.load_domains() — the SAME loader lint.py validates against
from wikikb.build import domains as domainsmod  # CRUD over the domain declarations in vault/taxonomy.md
from wikikb.quality import lint as lintmod      # lint.page_files() — page count, no re-parsing
from wikikb.retrieval import route as routemod
from wikikb.retrieval import kb
from wikikb.retrieval import expand as expandmod
from wikikb.graph import ask as askmod
from wikikb.serve import openapi        # OpenAPI 3.1 description + the offline /docs page
from wikikb.serve import jobs as jobsmod  # background runner for the ingest chain (no thread at import)
# The scrape surface. Imported UNCONDITIONALLY, in BOTH modes, and that is safe by construction: the
# package opens no socket at import and every fetch path calls modes.require_online() at the socket
# itself (modes.py, property 2). Importing it only in online mode would make the module graph differ
# between postures — which is exactly the kind of difference that makes an airgapped bug reproduce
# only in production.
from wikikb.scrape import scrape as scrapemod
from wikikb.scrape import sources as srcmod
from wikikb.scrape import cron as cronmod

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
# POST /ingest/<domain> — the batch trigger for the same chain an upload queues automatically.
INGEST_RE = re.compile(r"^/ingest/([a-z0-9][a-z0-9-]*)$")
# /domains/<name> — GET/PATCH/DELETE one declaration. Same traversal-safe-by-construction shape as
# SLUG_RE and UPLOAD_RE: the group excludes "/" and ".", so a path that isn't a bare kebab name never
# reaches a handler. The name's SEMANTIC rules (2+ chars, declared or not) live in domains.py, which
# is where the readers that impose them are documented.
DOMAIN_PATH_RE = re.compile(r"^/domains/([a-z0-9][a-z0-9-]*)$")
# GET /jobs/<id> — job ids are uuid4 hex prefixes (jobs.Job.id), so the shape check is exact.
JOB_ID_RE = re.compile(r"^[0-9a-f]{12}$")


# --- runtime configuration (env defaults; an explicit CLI flag still wins) ----------------
# Added 2026-08-05 so a container is configured by .env alone and the image's CMD can stay a
# static exec-form array (exec form does no shell variable expansion, so `--port $PORT` in CMD
# would be passed through as the literal string "$PORT").
def _env_route(name, default):
    """Normalize an env-supplied URL path: exactly one leading '/', no trailing '/'.
    Empty/whitespace falls back to `default` rather than mounting the endpoint at '/', which
    would shadow every other route."""
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    if not raw.startswith("/"):
        raw = "/" + raw
    return raw.rstrip("/") or default


# The MCP-over-HTTP mount point. Relocating it does NOT widen the surface: the old path falls
# through to the same _no_such_endpoint() any unknown path gets, so a moved endpoint is
# indistinguishable from an absent one (the same unfingerprintable property do_PUT relies on).
MCP_PATH = _env_route("WIKIKB_MCP_PATH", "/mcp")
DEFAULT_PORT = int(os.environ.get("WIKIKB_PORT") or 8642)
DEFAULT_BIND = os.environ.get("WIKIKB_BIND") or "127.0.0.1"

# The operation mode. Resolved at import with current_safe() rather than current(): mcp.py imports
# THIS module, so a bad WIKIKB_MODE must not become an import-time traceback inside an unrelated
# tool. On an unresolvable value MODE is the fail-closed default and MODE_ERROR carries the message;
# main() refuses to start the listener, which is where "fail loud on a typo" is actually enforced.
MODE, MODE_ERROR = modes.current_safe()

# Whether storing a PDF also QUEUES the conversion chain. Default ON (that is the point of the
# write surface: an upload should produce linked Markdown, not a file someone must remember to
# process). Set 0/false to keep the pre-2026-08-05 store-only behaviour and drive ingest by hand
# via POST /ingest/<domain> — the batch path, one build for several drops.
AUTO_INGEST = (os.environ.get("WIKIKB_AUTO_INGEST") or "1").strip().lower() not in ("0", "false", "no", "off")

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

def do_health(allow_upload=False):
    """Liveness + what this instance actually IS.

    `capabilities` is MODE-derived (what the posture permits); `uploads`/`auto_ingest` are
    PROCESS-derived (what this run switched on). Reporting them separately is deliberate — an
    operator debugging "why did my PUT 404" needs to tell "wrong mode" apart from "forgot
    --allow-upload", and a single merged flag would hide exactly that distinction.
    """
    domains = sorted(tags.load_domains())
    pages = sum(1 for _ in lintmod.page_files())
    return 200, {"status": "ok", "mode": MODE, "capabilities": modes.capabilities(MODE),
                 "uploads": bool(allow_upload),
                 "auto_ingest": bool(allow_upload and AUTO_INGEST),
                 "domains": domains, "pages": pages}


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

    out = {"stored": os.path.relpath(target, WIKI)}
    # 201 Created, not 202: the resource named in the request-target IS created and durable by the
    # time we answer. The queued conversion is reported as an ADDITIONAL field rather than by
    # downgrading the status, so a client that only cares about the file keeps its old contract.
    if AUTO_INGEST:
        try:
            job, coalesced = jobsmod.submit_ingest(domain, detail={"uploaded": out["stored"]})
        except RuntimeError as e:                       # queue full — the file is stored regardless,
            out["ingest"] = "not queued: %s" % e         # so say so instead of failing the upload
            out["next"] = "POST /ingest/%s once the backlog drains" % domain
            return 201, out
        out["job_id"] = job.id
        out["status_url"] = "/jobs/%s" % job.id
        # `coalesced` is not a degraded outcome: the chain reads the WHOLE _raw/pdfs/ directory, so
        # the pending job it folded into will see this file too (see jobs.Runner.submit).
        out["ingest"] = "coalesced into pending job" if coalesced else "queued"
        out["next"] = "GET /jobs/%s" % job.id
    else:
        out["ingest"] = "disabled (WIKIKB_AUTO_INGEST=0)"
        out["next"] = ("POST /ingest/%s   (or: python3 -m wikikb pdf_to_corpus --src "
                       "_sources/%s/_raw/pdfs --domain %s --append --apply)" % (domain, domain, domain))
    return 201, out


def do_ingest(domain):
    """POST /ingest/<domain> — queue the conversion chain by hand.

    The batch path: drop several PDFs with WIKIKB_AUTO_INGEST=0, then run ONE chain over all of
    them. Also the retry path when an upload's job failed and the cause has been fixed.
    """
    if domain not in tags.load_domains():
        return 400, {"error": "unknown domain: %s (see GET /health)" % domain}
    try:
        job, coalesced = jobsmod.submit_ingest(domain, detail={"trigger": "POST /ingest"})
    except RuntimeError as e:
        return 429, {"error": str(e)}
    return 202, {"job_id": job.id, "status_url": "/jobs/%s" % job.id,
                 "state": job.state, "coalesced": coalesced,
                 "steps": [name for name, _ in job.steps]}


def do_job(job_id):
    if not JOB_ID_RE.match(job_id or ""):
        return 400, {"error": "invalid job id"}
    job = jobsmod.RUNNER.get(job_id)
    if job is None:
        # Also the answer for a job that has been evicted after MAX_RETAINED — indistinguishable on
        # purpose: "we no longer hold a record" and "no such id" are the same fact to a client.
        return 404, {"error": "no such job: %s" % job_id}
    return 200, job.to_dict()


def do_jobs():
    return 200, {"jobs": [j.to_dict() for j in jobsmod.RUNNER.list()],
                 "stats": jobsmod.RUNNER.stats()}


# --- the domain declarations (BOTH MODES) -------------------------------------------------------
# CRUD over `vault/taxonomy.md`'s `## Domains` blocks — the file `/health`'s `domains` list, every
# page's `domain:`, the router's vocabulary and the Confidence gate's coverage arm all come from.
# NOT mode-gated: editing the vault's own configuration opens no socket, so refusing it on a sealed
# box would be a posture check applied to something that has no posture (the same reasoning that
# keeps the scrape watchlist's CLI verbs mode-independent). The WRITES share `--allow-upload` with
# /upload, /ingest and /scrape: declaring a domain decides what a later upload is allowed to write
# into the vault, so it belongs to the one write surface, and with uploads off it answers the same
# unfingerprintable 404, never a 403.

def do_domains_list():
    """GET /domains — every declared domain, plus what a POST is allowed to reference.

    The `areas` vocabulary ships with the listing on purpose: a domain's `areas:` must be a subset
    of the flat union, so a client composing a POST needs it, and a second round trip to discover
    the legal values would be a needless one.
    """
    items = domainsmod.list_domains()
    return 200, {"domains": items, "count": len(items),
                 "areas": domainsmod.known_areas(),
                 "shapes": list(domainsmod.SHAPES), "tiers": list(domainsmod.TIERS),
                 "file": str(paths.TAXONOMY)}


def do_domain_get(name):
    """GET /domains/<name> — one declaration + what currently depends on it.

    `usage` is served on the plain read, not only on a refused DELETE: the blast radius of
    undeclaring a domain (pages that would start failing lint, immutable notes that would be
    stranded) is exactly what someone asks for before they decide, not after.
    """
    entry = domainsmod.get(name)
    if entry is None:
        return 404, {"error": "no such domain: %s (see GET /domains)" % name}
    entry["usage"] = domainsmod.usage(name)
    entry["file"] = str(paths.TAXONOMY)
    return 200, entry


def do_domains_add(body):
    """POST /domains — declare a new technology domain.

    This is ADD-DOMAIN steps 2–4 (declare it, extend the area vocabulary, create the raw tier) as
    one call. It deliberately stops there: seeding the synthesis (step 5) is an authored act, and
    the generated indexes are `wikikb index`'s output — so the response says what to do next instead
    of inventing pages nobody wrote.
    """
    name = body.get("domain") or body.get("name")
    if not body.get("areas"):
        return 400, {"error": "areas is required — a domain with no areas routes nothing "
                              "(GET /domains lists the vocabulary; send unknown ones in new_areas)"}
    try:
        entry = domainsmod.add(name, areas=body.get("areas"),
                               shape=(body.get("shape") or "notes-first"),
                               sources=body.get("sources"),
                               review_moc=body.get("review-moc") or body.get("review_moc"),
                               tiers_covered=(body.get("tiers-covered") or body.get("tiers_covered")),
                               new_areas=body.get("new_areas"))
    except domainsmod.DomainError as e:
        return (409 if "already declared" in str(e) else 400), {"error": str(e)}
    return 201, {"added": entry, "file": entry["file"],
                 "next": "write the overview topic, its first entity and %s, then run "
                         "`python3 -m wikikb build` (or POST /ingest/%s after dropping sources)"
                         % (entry["review-moc"], entry["domain"])}


def do_domains_update(name, body):
    """PATCH /domains/<name> — change a declaration without retyping the rest of it.

    Partial: the path selects, only the fields in the body are touched, and `changed` reports what
    actually moved so a no-op is distinguishable from an update (and does not rewrite the file).
    The NAME is not patchable — it is the value of every page's `domain:`, the `reference/<domain>/`
    directory and the `index.<domain>.md` stem; see domains.update() for the full reasoning.
    """
    if not body:
        return 400, {"error": "nothing to update — send at least one of: %s, new_areas"
                              % ", ".join(domainsmod.PATCHABLE)}
    if "path" in body:
        # domains.update(name, path=…, **fields) takes the TAXONOMY FILE as `path`, so splatting a
        # request body straight in would let a caller redirect the write to any file the process can
        # open. The body names FIELDS; `path` is not one, and it is refused by name rather than
        # silently dropped.
        return 400, {"error": "not updatable: path (allowed: %s, new_areas)"
                              % ", ".join(domainsmod.PATCHABLE)}
    try:
        entry, changed = domainsmod.update(name, **body)
    except domainsmod.DomainError as e:
        return (404 if str(e).startswith("no such domain") else 400), {"error": str(e)}
    out = {"updated": entry, "changed": changed, "file": entry["file"]}
    if not changed:
        out["note"] = "no change — the declaration already held these values (file not rewritten)"
    elif "areas" in changed or "new_areas" in changed:
        out["note"] = ("the router's keyword profiles are built from areas — run "
                       "`python3 -m wikikb build` (or restart serve) for this to take effect")
    return 200, out


def do_domains_remove(name, force=False):
    """DELETE /domains/<name> — undeclare a domain.

    Removes the DECLARATION and the generated `index.<domain>.md`; it never deletes a page or a
    line of the immutable reference/_sources tiers — withdrawing knowledge is Operation: RETRACT.
    It answers 409 while pages still declare the domain, because silently undeclaring it makes
    every one of those pages fail lint as "unknown domain" with nothing pointing back here.
    `?force=true` is the operator taking that on.
    """
    try:
        entry = domainsmod.remove(name, force=force)
    except domainsmod.DomainError as e:
        msg = str(e)
        if msg.startswith("no such domain"):
            return 404, {"error": msg}
        return (409 if "still in use" in msg else 400), {"error": msg}
    return 200, {"removed": entry, "file": entry["file"], "kept": entry["kept"],
                 "removed_generated": entry["removed_generated"],
                 "note": "the immutable reference/ and _sources/ tiers and every page are KEPT — to "
                         "withdraw what this domain knows, retract the pages (CLAUDE.md, Operation: "
                         "RETRACT). Run `python3 -m wikikb build` to regenerate the router index."}


# --- the scrape surface (ONLINE MODE ONLY) ------------------------------------------------------
# Every handler below is reached only after do_GET/do_POST/do_DELETE has confirmed online mode;
# in airgapped mode the same paths fall through to _no_such_endpoint() and are byte-identical to an
# unknown path, so a sealed instance does not advertise what it refuses to do.

def _json_body(raw):
    """Parse a request body as a JSON object, or raise ValueError. An EMPTY body is `{}` — `POST
    /scrape` with no body means "harvest the whole watchlist", and requiring `{}` on the wire for
    that would be a needless trap for `curl -X POST`."""
    if not raw or not raw.strip():
        return {}
    obj = json.loads(raw.decode("utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("expected a JSON object")
    return obj


def do_scrape_sources_get():
    """GET /scrape/sources — the watchlist plus what a harvest would actually use.

    A READ, so it is not behind --allow-upload: seeing the configured sources changes nothing, and
    an operator debugging "why did nothing get harvested" needs it before they need anything else.
    """
    info = scrapemod.sources()
    info["cron"] = cronmod.SCHEDULER.status()
    return 200, info


def do_scrape_sources_add(body):
    """POST /scrape/sources — add a website to the watchlist.

    The domain is validated against vault/taxonomy.md here (in sources.add), not at harvest time:
    an entry naming a domain that does not exist would sit on the list and fail every cron tick
    from then on, with nobody watching. 201 with the stored entry, which is the CANONICAL form —
    the caller can see that `HTTPS://Example.com/a#top` was stored as `https://example.com/a`.
    """
    try:
        entry = srcmod.add(url=body.get("url"), domain=body.get("domain"),
                           label=body.get("label"), match=(body.get("match") or "exact"),
                           enabled=body.get("enabled", True), direct=bool(body.get("direct")))
    except srcmod.SourceError as e:
        return 400, {"error": str(e)}
    return 201, {"added": entry, "file": str(paths.SCRAPE_SOURCES),
                 "next": "POST /scrape  (harvest now) — or wait for the cron: GET /scrape/cron"}


def do_scrape_sources_update(body):
    """PATCH /scrape/sources — change an existing source without losing the rest of its entry.

    `url` selects the entry; every other field is optional and only what you send is touched. The
    URL itself is NOT patchable — it is the entry's identity (it names the harvested note and the
    `kb:` token citing pages use), so a rename is DELETE + POST, two explicit acts. See
    sources.update() for the full reasoning.

    The response reports `changed` — the fields that actually moved — so "updated" is
    distinguishable from "you sent the values it already had", which is also why a no-op patch does
    not rewrite the file.
    """
    if not body.get("url"):
        return 400, {"error": 'url is required — it selects which source to update'}
    fields = {k: v for k, v in body.items() if k != "url"}
    if not fields:
        return 400, {"error": "nothing to update — send at least one of: domain, label, match, "
                              "enabled, direct"}
    try:
        entry, changed = srcmod.update(body["url"], **fields)
    except srcmod.SourceError as e:
        return (404 if "not on the watchlist" in str(e) else 400), {"error": str(e)}
    out = {"updated": entry, "changed": changed, "file": str(paths.SCRAPE_SOURCES)}
    if not changed:
        out["note"] = "no change — the entry already held these values (file not rewritten)"
    if "domain" in changed:
        out["note"] = ("domain changed; anything ALREADY harvested stays under the old domain's "
                       "_raw/web/ and the reference notes it produced are unchanged — this only "
                       "redirects future runs")
    return 200, out


def do_scrape_sources_remove(url):
    """DELETE /scrape/sources?url=… — stop watching a website.

    It does NOT delete what that source already harvested. The raw tier is immutable ground truth
    and synthesis pages cite it, so un-watching a site must not silently invalidate every page that
    cites what it produced; withdrawing the KNOWLEDGE is Operation: RETRACT, an explicitly authored
    act. The response says so rather than leaving the caller to assume either behaviour.
    """
    try:
        entry = srcmod.remove(url)
    except srcmod.SourceError as e:
        return (404 if "not on the watchlist" in str(e) else 400), {"error": str(e)}
    return 200, {"removed": entry, "file": str(paths.SCRAPE_SOURCES),
                 "note": "already-harvested notes are kept (the raw tier is immutable); to withdraw "
                         "the knowledge, retract the pages that cite it — CLAUDE.md, Operation: RETRACT"}


def do_scrape_run(body):
    """POST /scrape — harvest now.

    Two shapes, both queued on the SAME serialized runner the upload path uses (never run inline: a
    harvest plus a full `build` is minutes, far past Handler.timeout, and two concurrent builds
    would interleave writes to the generated artifacts):

        {}                            every enabled watchlist source — one job PER DOMAIN, because
                                      the fold-in chain after the fetch is per-domain.
        {"url": …, "domain": …}       one URL, which NEED NOT be on the watchlist. `urls: [...]`
                                      takes several. `direct: true` permits a live origin fetch
                                      when Common Crawl has no capture (address-guarded in
                                      scrape.py); `match: "prefix"` harvests everything indexed
                                      under the URL, up to WIKIKB_SCRAPE_PREFIX_LIMIT.
    """
    urls = body.get("urls") or ([body["url"]] if body.get("url") else [])
    match = (body.get("match") or "exact").strip()
    if match not in srcmod.MATCH_MODES:
        return 400, {"error": "match must be one of %s" % ", ".join(srcmod.MATCH_MODES)}
    direct = bool(body.get("direct"))
    try:
        max_indexes = int(body["max_indexes"]) if body.get("max_indexes") is not None else None
    except (TypeError, ValueError):
        return 400, {"error": "max_indexes must be an integer"}
    known = tags.load_domains()

    if urls:
        domain = body.get("domain")
        if not domain:
            return 400, {"error": "domain is required when scraping a specific url"}
        if domain not in known:
            return 400, {"error": "unknown domain: %s (see GET /health)" % domain}
        canon = []
        for u in urls:
            try:
                canon.append(srcmod.normalize(u))
            except srcmod.SourceError as e:
                return 400, {"error": str(e)}
        try:
            job, coalesced = jobsmod.submit_scrape(domain, urls=canon, match=match, direct=direct,
                                                   detail={"trigger": "POST /scrape",
                                                           "urls": canon})
        except RuntimeError as e:
            return 429, {"error": str(e)}
        return 202, {"queued": [{"domain": domain, "job_id": job.id, "coalesced": coalesced,
                                 "status_url": "/jobs/%s" % job.id}],
                     "urls": canon, "steps": [n for n, _ in job.steps]}

    try:
        doms = srcmod.domains(enabled_only=True)
    except srcmod.SourceError as e:
        return 400, {"error": str(e)}
    if not doms:
        # Not an error: an empty watchlist is a normal state. 200 with an explicit note beats a 202
        # for a job that would do nothing, which reads as "started" in every dashboard.
        return 200, {"queued": [], "note": "watchlist is empty — add one with POST /scrape/sources",
                     "file": str(paths.SCRAPE_SOURCES)}
    queued = []
    for d in doms:
        if d not in known:
            queued.append({"domain": d, "error": "domain is on the watchlist but not in taxonomy.md"})
            continue
        try:
            job, coalesced = jobsmod.submit_scrape(d, detail={"trigger": "POST /scrape"},
                                                   max_indexes=max_indexes)
            queued.append({"domain": d, "job_id": job.id, "coalesced": coalesced,
                           "status_url": "/jobs/%s" % job.id})
        except RuntimeError as e:
            queued.append({"domain": d, "error": str(e)})
    return 202, {"queued": queued}


def do_scrape_cron_get():
    return 200, cronmod.SCHEDULER.status()


def do_scrape_cron_set(body):
    """POST /scrape/cron {"enabled": bool} — flip the scheduled harvest at runtime.

    Runtime-only by design: it does NOT rewrite .env. A process that edits its own configuration
    makes "what will this container do when it restarts?" unanswerable from the config, so the env
    var stays the boot default and this is the live override — the status reports both, side by
    side, so a divergence is never invisible.
    """
    if "enabled" not in body:
        return 400, {"error": 'body must be {"enabled": true|false}'}
    want = body["enabled"]
    if isinstance(want, str):
        want = want.strip().lower() in ("1", "true", "yes", "on")
    return 200, cronmod.SCHEDULER.set_enabled(bool(want))


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

    def _reply_raw(self, status, content_type, body):
        """Serve pre-encoded bytes at an explicit Content-Type. _reply is JSON-only (it json.dumps
        whatever it is handed), which is right for the API surface but cannot emit the HTML docs
        page or a pre-serialized spec without double-encoding it into a JSON string."""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
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
                status, obj = do_health(getattr(self.server, "allow_upload", False))
            elif path == "/jobs":
                status, obj = do_jobs()
            elif path.startswith("/jobs/"):
                status, obj = do_job(path[len("/jobs/"):])
            elif path == "/domains":
                status, obj = do_domains_list()
            elif DOMAIN_PATH_RE.match(path):
                status, obj = do_domain_get(DOMAIN_PATH_RE.match(path).group(1))
            elif path == "/scrape/sources":
                # Online-only. In airgapped mode this falls through to the SAME
                # _no_such_endpoint() an unknown path gets — the disabled-upload posture applied to
                # the mode split, so a sealed instance does not advertise what it refuses to do.
                status, obj = do_scrape_sources_get() if MODE == modes.ONLINE else _no_such_endpoint()
            elif path == "/scrape/cron":
                status, obj = do_scrape_cron_get() if MODE == modes.ONLINE else _no_such_endpoint()
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
            elif path == "/openapi.json":
                # Built from the LIVE config (MCP mount, auth posture, resolved vault) so the
                # description cannot drift from what is actually being served.
                self._reply_raw(200, "application/json; charset=utf-8",
                                openapi.spec_json(MCP_PATH, bool(os.environ.get("WIKIKB_API_TOKEN")),
                                                  str(paths.WIKI), mode=MODE).encode("utf-8"))
                return
            elif path == "/docs":
                self._reply_raw(200, "text/html; charset=utf-8", openapi.docs_html().encode("utf-8"))
                return
            elif path == MCP_PATH:
                # Declining the optional standalone SSE stream is spec-legal (transports#GET item 3);
                # the reference TS SDK client treats 405 here as an expected non-error (RESEARCH 2).
                status, obj = 405, {"error": "GET not supported at %s (no standalone SSE stream; "
                                             "use POST %s)" % (MCP_PATH, MCP_PATH)}
            else:
                status, obj = _no_such_endpoint()
        except Exception as e:                              # noqa: BLE001 — a bad request must never kill the thread
            status, obj = 500, {"error": str(e)}
        self._reply(status, obj)
        # one line per request to stderr; BaseHTTPRequestHandler's default log_message already
        # does this via send_response() -> log_request(), so nothing further is needed here.

    def _drain_body(self, cap):
        """Read and return at most `cap` bytes of body, or None after replying with the error.

        Every POST path must consume its declared body even when it ignores the content: leaving
        unread bytes in the socket desynchronizes a keep-alive connection, so the NEXT request on it
        is parsed starting mid-body. Same required/numeric/bounded shape as do_upload's
        Content-Length handling — a missing length is 411, an oversized one is 413 off the header
        alone, never by reading it first.
        """
        length_header = self.headers.get("Content-Length")
        if length_header is None:
            self._reply(411, {"error": "Content-Length required"})
            return None
        try:
            length = int(length_header)
        except ValueError:
            self._reply(400, {"error": "invalid Content-Length"})
            return None
        if length < 0 or length > cap:
            self._reply(413, {"error": "payload too large (max %d bytes)" % cap})
            return None
        raw = self.rfile.read(length)
        if len(raw) != length:
            self._reply(400, {"error": "short read: expected %d bytes, got %d" % (length, len(raw))})
            return None
        return raw

    def do_POST(self):
        path = urlsplit(self.path).path.rstrip("/") or "/"
        if path != MCP_PATH:
            # Auth FIRST on the non-MCP write paths, matching do_GET (which gates everything except
            # /health before dispatch). The MCP branch below keeps its existing order untouched.
            err = _check_auth(self.headers)
            if err:
                self._reply(*err)
                return
            m = INGEST_RE.match(path)
            if m:
                # Same opt-in as /upload, and the same unfingerprintable refusal when it is off:
                # /ingest triggers writes to the vault, so it is part of the write surface, not a
                # separate one that could be left open after uploads were deliberately disabled.
                if not getattr(self.server, "allow_upload", False):
                    self._reply(*_no_such_endpoint())
                    return
                if self._drain_body(MCP_MAX_BYTES) is None:
                    return
                try:
                    status, obj = do_ingest(m.group(1))
                except Exception as e:                  # noqa: BLE001 — never kill the thread
                    status, obj = 500, {"error": str(e)}
                self._reply(status, obj)
                return
            if path == "/domains":
                # Both modes: a declaration is vault configuration, not a network act. The gate is
                # the write surface's, same as every other writing path.
                ok, body = self._write_body()
                if not ok:
                    return
                try:
                    status, obj = do_domains_add(body)
                except Exception as e:                  # noqa: BLE001 — never kill the thread
                    status, obj = 500, {"error": str(e)}
                self._reply(status, obj)
                return
            if path in ("/scrape", "/scrape/sources", "/scrape/cron") and MODE == modes.ONLINE:
                ok, body = self._write_body()
                if not ok:
                    return
                try:
                    if path == "/scrape":
                        status, obj = do_scrape_run(body)
                    elif path == "/scrape/sources":
                        status, obj = do_scrape_sources_add(body)
                    else:
                        status, obj = do_scrape_cron_set(body)
                except Exception as e:                  # noqa: BLE001 — never kill the thread
                    status, obj = 500, {"error": str(e)}
                self._reply(status, obj)
                return
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

    def _write_body(self):
        """Gate + parsed JSON body shared by EVERY writing request with a JSON body (POST + PATCH,
        scrape and domains alike).

        THE GATE: all of these are part of the ONE write surface and share --allow-upload with
        /upload and /ingest. A scrape writes into the vault; adding or updating a source decides
        what a later scrape writes; toggling the cron decides whether it writes unattended;
        declaring a domain decides which of those an upload is allowed to target at all. An
        instance whose operator deliberately disabled uploads must not be writable through a side
        door — and the refusal is the same unfingerprintable 404, not a 403.

        Returns (True, body) or (False, None) having ALREADY replied. Factored out so POST and PATCH
        cannot drift apart on the gate, the Content-Length handling, or the parse error shape —
        three things that must be identical on every write path or the surface is inconsistent.
        """
        if not getattr(self.server, "allow_upload", False):
            self._reply(*_no_such_endpoint())
            return False, None
        raw = self._drain_body(MCP_MAX_BYTES)
        if raw is None:
            return False, None
        try:
            return True, _json_body(raw)
        except ValueError as e:
            self._reply(400, {"error": "invalid JSON body: %s" % e})
            return False, None

    def do_PATCH(self):
        # Defined UNCONDITIONALLY, exactly like do_PUT and for the same reason: a conditional
        # do_PATCH would leak the stdlib's 501 "Unsupported method" and thereby confirm the method
        # exists on instances that hide it. Airgapped, uploads-off, and "no such path" all end at
        # the SAME _no_such_endpoint().
        path = urlsplit(self.path).path.rstrip("/") or "/"
        err = _check_auth(self.headers)
        if err:
            self._reply(*err)
            return
        dm = DOMAIN_PATH_RE.match(path)
        if not dm and (path != "/scrape/sources" or MODE != modes.ONLINE):
            self._reply(*_no_such_endpoint())
            return
        ok, body = self._write_body()
        if not ok:
            return
        try:
            status, obj = (do_domains_update(dm.group(1), body) if dm
                           else do_scrape_sources_update(body))
        except Exception as e:                          # noqa: BLE001 — never kill the thread
            status, obj = 500, {"error": str(e)}
        self._reply(status, obj)
        return

    def do_DELETE(self):
        # No stateful sessions (serve.py issues no Mcp-Session-Id — RESEARCH 2's recommended, spec-
        # legal design), so explicit session termination is declined via 405, same as GET's SSE decline.
        parts = urlsplit(self.path)
        path = parts.path.rstrip("/") or "/"
        if path == MCP_PATH:
            err = _check_auth(self.headers)
            self._reply(*(err or (405, {"error": "session termination not supported"})))
            return
        dm = DOMAIN_PATH_RE.match(path)
        if dm:
            err = _check_auth(self.headers)
            if err:
                self._reply(*err)
                return
            if not getattr(self.server, "allow_upload", False):
                self._reply(*_no_such_endpoint())
                return
            # `force` from the query string or a JSON body, same dual shape /scrape/sources uses —
            # and a declared body is DRAINED either way, or the next request on a keep-alive
            # connection is parsed starting mid-body.
            qs = {k: v[0] for k, v in parse_qs(parts.query).items()}
            force = qs.get("force") in ("1", "true")
            if self.headers.get("Content-Length") is not None:
                raw = self._drain_body(MCP_MAX_BYTES)
                if raw is None:
                    return
                try:
                    force = bool(_json_body(raw).get("force", force))
                except ValueError as e:
                    self._reply(400, {"error": "invalid JSON body: %s" % e})
                    return
            try:
                status, obj = do_domains_remove(dm.group(1), force=bool(force))
            except Exception as e:                      # noqa: BLE001 — never kill the thread
                status, obj = 500, {"error": str(e)}
            self._reply(status, obj)
            return
        if path == "/scrape/sources" and MODE == modes.ONLINE:
            err = _check_auth(self.headers)
            if err:
                self._reply(*err)
                return
            if not getattr(self.server, "allow_upload", False):
                self._reply(*_no_such_endpoint())
                return
            # The URL comes from the query string OR a JSON body — `curl -X DELETE ".../scrape/
            # sources?url=…"` is what an operator reaches for, while an API client sends a body.
            # A declared body must still be DRAINED either way, or the next request on a keep-alive
            # connection is parsed starting mid-body.
            url = {k: v[0] for k, v in parse_qs(parts.query).items()}.get("url")
            if self.headers.get("Content-Length") is not None:
                raw = self._drain_body(MCP_MAX_BYTES)
                if raw is None:
                    return
                try:
                    url = _json_body(raw).get("url") or url
                except ValueError as e:
                    self._reply(400, {"error": "invalid JSON body: %s" % e})
                    return
            if not url:
                self._reply(400, {"error": "url is required (?url=… or a JSON body {\"url\": …})"})
                return
            try:
                status, obj = do_scrape_sources_remove(url)
            except Exception as e:                      # noqa: BLE001 — never kill the thread
                status, obj = 500, {"error": str(e)}
            self._reply(status, obj)
            return
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
    ap.add_argument("--port", type=int, default=DEFAULT_PORT,
                    help="listen port (default %(default)s; env WIKIKB_PORT)")
    ap.add_argument("--bind", default=DEFAULT_BIND,
                    help="loopback by default (127.0.0.1); binding a real interface is the operator's "
                         "explicit choice (env WIKIKB_BIND)")
    ap.add_argument("--allow-upload", action="store_true",
                    default=os.environ.get("WIKIKB_ALLOW_UPLOAD", "").strip().lower() in ("1", "true", "yes", "on"),
                    help="enable PUT /upload/<domain>/<file>.pdf (default OFF; writes only into "
                         "vault/_sources/<domain>/_raw/pdfs/, never the immutable reference tier; "
                         "env WIKIKB_ALLOW_UPLOAD=1)")
    args = ap.parse_args()
    # REFUSE TO START on an unresolvable WIKIKB_MODE. Falling back to a default here would mean a
    # typo silently changes the deployment's posture — either quietly disabling the scraper an
    # operator believes is running, or (the direction that actually matters) leaving them believing
    # a box is sealed. Exit 2 is the same "misconfiguration, not a runtime error" code build.py uses.
    if MODE_ERROR:
        print("wikikb serve: REFUSED — " + MODE_ERROR, file=sys.stderr)
        sys.exit(2)
    # Create the vault skeleton if it isn't there yet (wikikb/bootstrap.py). Called here as well as
    # in the `python3 -m wikikb` dispatcher because this main() is also reachable directly
    # (`python3 -m wikikb.serve.serve`, the container CMD) — and it MUST precede the cache pre-warm
    # below, which is what would otherwise freeze "zero pages" into a long-lived process. A fresh
    # bind mount at /data/vault is the case this turns from "serves an empty wiki" into a working,
    # writable vault; it prints one stderr line naming the path, so a typo'd mount is visible in the
    # first lines of `docker logs` rather than showing up later as mysteriously empty results.
    bootstrap.ensure_startup(label="wikikb serve")
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
    uploads = ""
    if args.allow_upload:
        uploads = "  [uploads ENABLED%s]" % ("" if AUTO_INGEST else ", auto-ingest OFF")
    print("wikikb serve: http://%s:%d  (Ctrl-C to stop)%s  [%s]" % (
        args.bind, args.port, uploads, auth_mode), file=sys.stderr)
    # The mode decides whether an outbound-capable surface exists at all, so it belongs in the first
    # lines of `docker logs` next to the vault path — the two settings an operator most often gets
    # wrong and cannot otherwise see without making a request.
    # The scheduled harvest starts HERE, not at import: it submits jobs that write to the vault, so
    # it must not exist in a process that is only importing this module (mcp.py does), and it must
    # not exist in a process whose operator did not enable the write surface. Both conditions are
    # reported below rather than silently applied — "my cron never runs" is otherwise an
    # unanswerable question.
    cron_note = ""
    if MODE == modes.ONLINE:
        if not args.allow_upload:
            cron_note = "  [scrape cron INERT — needs --allow-upload]"
        elif cronmod.SCHEDULER.error:
            cron_note = "  [scrape cron DISABLED — bad WIKIKB_SCRAPE_CRON: %s]" % cronmod.SCHEDULER.error
        else:
            cronmod.SCHEDULER.start()
            st = cronmod.SCHEDULER.status()
            cron_note = ("  [scrape cron %s: %s, next %s]"
                         % ("ON" if st["enabled"] else "OFF (WIKIKB_SCRAPE_CRON_ENABLED=0)",
                            st["schedule"], st["next_run_iso"] or "n/a"))
    print("wikikb serve: mode=%s%s" % (
        MODE, "  [web scraper mounted]" + cron_note if MODE == modes.ONLINE else
              "  (no outbound network)"), file=sys.stderr)
    # The vault and MCP mount are both relocatable now, and getting either wrong produces a server
    # that starts cleanly and then answers every query from the wrong (or an empty) corpus. Print
    # them so a misconfigured mount is visible in the first lines of `docker logs`, not later as
    # mysteriously empty results.
    print("wikikb serve: vault=%s  mcp=POST %s  openapi=/openapi.json  docs=/docs" % (
        paths.WIKI, MCP_PATH), file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
