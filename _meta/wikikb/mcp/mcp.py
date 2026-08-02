#!/usr/bin/env python3
"""mcp.py — `python3 -m wikikb mcp`: an MCP (Model Context Protocol) server over stdio.

Why: MCP hosts (Claude Code, Claude Desktop, etc.) speak newline-delimited JSON-RPC 2.0 over a
child process's stdin/stdout, not HTTP. This is the stdio sibling of serve.py's loopback HTTP
API — same underlying calls (route.route, kb-backed search, ask.ask/references, page read),
different transport. Nothing is re-implemented: `search`/`route`/`read_page` reuse serve.py's
do_search/do_route/do_page verbatim; `ask` calls graph/ask.py's ask()+references() directly so
its result matches `wikikb ask --json` byte-for-byte in shape.

Register with an MCP host:
    claude mcp add wikikb -- python3 -m wikikb mcp
(cwd must be wiki/_meta/, or set PYTHONPATH=<repo>/wiki/_meta, so `import wikikb` resolves with
no install — same constraint every other tool in this package has.)

Protocol: one JSON-RPC 2.0 message per line, UTF-8, stdin in / stdout out. stdout is reserved
EXCLUSIVELY for protocol messages — every response is flushed immediately and nothing else ever
writes there; all diagnostics go to stderr. Pure stdlib (sys, json only). No sockets, ever.
Exits cleanly (0) when stdin closes (EOF) — the host's normal child-process teardown.

Transport-agnostic core: `handle(req) -> dict | None` is a PURE function (dispatch one parsed
JSON-RPC message, return the response object, touch no I/O). This file's own main() loop below is
just one caller of it — it does the stdout writing itself. serve.py's `POST /mcp` (Streamable HTTP
transport, for remote callers like n8n that can't spawn a stdio child process) is the other caller:
same dispatch table, same tools, byte-identical results, different plumbing around it.

DUAL-ERA (see the two-eras block further down): `handle()` serves BOTH the legacy `initialize`
handshake (protocol 2025-11-25 and earlier — every client in the field today) and the modern
per-request-`_meta` era introduced by revision 2026-07-28, choosing per message from the request
itself. The legacy path is unchanged code on an unchanged wire; modern support is purely additive.
The HTTP-specific half of the modern era (required `MCP-Protocol-Version`/`Mcp-Method`/`Mcp-Name`
headers, and mapping protocol errors onto HTTP status) lives in serve.py, where the transport is.
"""
import json
import sys

sys.dont_write_bytecode = True
from wikikb.graph import ask as askmod
from wikikb.serve.serve import do_page, do_route, do_search

# ---------------------------------------------------------------------------------------------
# TOOL ANNOTATIONS (spec: server/tools #toolannotations). Hints, never a security boundary — the
# write gate is `file_back`'s own guard chain in fileback.file_answer, not this metadata. But a host
# CANNOT auto-approve a read tool it has no way to recognise, so omitting these costs twice: the
# three genuinely read-only tools don't get credit, and the one that can WRITE isn't flagged.
#
# `openWorldHint: False` on all four is the honest reading of this server: every tool answers from
# the local vault. The optional LLM tier is loopback-only and refuses non-loopback without a double
# opt-in (see _meta/CLAUDE.md), so no tool here reaches an open-ended external system.
_READ = {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True,
         "openWorldHint": False}
# ask is CONDITIONALLY mutating: with file_back=true it persists questions/<slug>.md into the vault.
# Not destructive — fileback refuses an existing slug rather than overwriting it — but not read-only
# either, so readOnlyHint must be False. Not idempotent: the first call files the page, the second
# returns filed=False ("already exists"), so repeat calls differ.
_ASK = {"readOnlyHint": False, "destructiveHint": False, "idempotentHint": False,
        "openWorldHint": False}

# OUTPUT SCHEMAS. Following keycloak-mcp-server/app/core/envelope.py's measured trade-off: name every
# field, type only the ones a client branches on, and leave enumerations to the documentation — a
# fully-typed schema costs more `tools/list` tokens per conversation than it buys.
# additionalProperties stays open: _call_tool appends session_tokens_served/budget_directive, and ask
# gains `filed` and `judge_verdict` conditionally.
_ASK_OUT = {
    "type": "object", "additionalProperties": True,
    "properties": {
        "query": {"type": "string"}, "domain": {"type": ["string", "null"]},
        "answer": {"type": "string"},
        "confident": {"type": "boolean"}, "thin": {"type": "boolean"},
        "withheld": {"type": "boolean"}, "grounding_fail": {"type": "boolean"},
        "banner": {"type": "array"}, "guard": {"type": "array"},
        "cited": {"type": "array"}, "ungrounded_identifiers": {"type": "array"},
        "premise_flags": {"type": "array"}, "references": {"type": "array"},
        "grounding_basis": {}, "reference_groups": {}, "orchestrator": {"type": "string"},
        "filed": {"type": "object", "description": "present only when file_back=true"},
        "session_tokens_served": {"type": "integer"},
    },
}
# do_search returns a bare LIST. structuredContent MUST be an object (spec: server/tools
# #structured-content), so the object form lives in structuredContent while `content` keeps the
# verbatim list — byte-identical to serve /search, so no existing consumer sees a shape change.
_SEARCH_OUT = {
    "type": "object", "additionalProperties": True,
    "properties": {"hits": {"type": "array"}, "count": {"type": "integer"}},
}
_ROUTE_OUT = {
    "type": "object", "additionalProperties": True,
    "properties": {"domains": {"type": "array"}, "confident": {"type": "boolean"}},
}
_PAGE_OUT = {
    "type": "object", "additionalProperties": True,
    "properties": {
        "slug": {"type": "string"}, "path": {"type": "string"},
        "frontmatter": {"type": "object"}, "body": {"type": "string"},
        "body_total_chars": {"type": "integer"},
        "truncated": {"type": "boolean"}, "next_offset": {"type": "integer"},
    },
}

TOOLS = [
    {
        "name": "wiki_ask",
        "description": ("Ask the wiki a question; returns a gated, cited answer. "
                        "WRITES when file_back=true: persists the answer as a questions/<slug>.md "
                        "draft page in the vault."),
        "annotations": _ASK,
        "outputSchema": _ASK_OUT,
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string"},
                "domain": {"type": "string"},
                "tier": {"type": "string", "enum": ["conceptual", "support-kb", "scenarios"]},
                "k": {"type": "integer"},
                "strict": {"type": "boolean",
                           "description": "withhold the answer prose when ungrounded (recommended "
                                          "for unattended consumers; WIKI_STRICT_GROUNDING=1 sets "
                                          "this default globally)"},
                "file_back": {"type": "boolean",
                              "description": "persist the answer as a questions/<slug>.md DRAFT "
                                             "page in the vault (skipped for withheld answers and "
                                             "existing slugs); result gains a `filed` object"},
            },
            "required": ["question"],
        },
    },
    {
        "name": "wiki_search",
        "description": "Top-k reference-note hits (id/title/score/snippet) for a domain",
        "annotations": _READ,
        "outputSchema": _SEARCH_OUT,
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string"},
                "q": {"type": "string"},
                "k": {"type": "integer"},
            },
            "required": ["domain", "q"],
        },
    },
    {
        "name": "wiki_route",
        "description": "Route a query to its likely domain(s)",
        "annotations": _READ,
        "outputSchema": _ROUTE_OUT,
        "inputSchema": {
            "type": "object",
            "properties": {"q": {"type": "string"}},
            "required": ["q"],
        },
    },
    {
        "name": "wiki_read_page",
        "description": "Read a wiki page's frontmatter + body by slug (topics/entities/questions). Long bodies are served in ~8k-char slices; pass offset=next_offset for more.",
        "annotations": _READ,
        "outputSchema": _PAGE_OUT,
        "inputSchema": {
            "type": "object",
            "properties": {"slug": {"type": "string"},
                           "offset": {"type": "integer", "description": "char offset for the next slice of a long body (see next_offset)"}},
            "required": ["slug"],
        },
    },
]


def _tool_ask(args):
    q = args.get("question")
    if not q:
        raise ValueError("question is required")
    st = askmod.ask(q, domain=args.get("domain"), k=int(args.get("k") or 5), question_tier=args.get("tier"))
    refs = askmod.references(st.get("domain"), st.get("used", []))
    # WI-7: the shared serializer — byte-same shape as `wikikb ask --json` and serve /ask; a host
    # consuming this tool sees the identical answer a human running the CLI would, with grounding
    # status always structured (withheld / ungrounded_identifiers / grounding_basis).
    # strict tri-state: an absent arg defers to WIKI_STRICT_GROUNDING; an explicit false beats it.
    out = askmod.public_result(q, st, refs, strict=askmod.resolve_strict(args.get("strict")))
    if args.get("file_back"):
        from wikikb.graph import fileback
        out["filed"] = fileback.file_answer(out, question_tier=args.get("tier"))
    return out


def _tool_search(args):
    domain, q = args.get("domain"), args.get("q")
    if not domain or not q:
        raise ValueError("domain and q are required")
    status, obj = do_search(domain, q, int(args.get("k") or 5))
    if status != 200:
        raise ValueError(obj.get("error", "search failed"))
    return obj


def _tool_route(args):
    q = args.get("q")
    if not q:
        raise ValueError("q is required")
    status, obj = do_route(q)
    if status != 200:
        raise ValueError(obj.get("error", "route failed"))
    return obj


def _tool_read_page(args):
    slug = args.get("slug")
    if not slug:
        raise ValueError("slug is required")
    status, obj = do_page(slug, int(args.get("offset") or 0))
    if status != 200:
        raise ValueError(obj.get("error", "no such page"))
    return obj


# The ADVERTISED names carry the `wiki_` prefix: an MCP host may load this server alongside others,
# and bare `ask`/`search`/`route` are the most collision-prone names available (server/tools
# #tool-name). Claude Code namespaces to mcp__wikikb__*, but a host that flattens names does not.
#
# The legacy bare names stay dispatchable but UNADVERTISED — tools/list offers only `wiki_*`, while
# an in-flight caller pinned to the old name (selftest #50, an n8n workflow, a saved agent card)
# keeps working. A rename nobody can act on yet is a breakage, not a fix; drop the aliases once the
# consumers are moved.
_TOOL_FNS = {"ask": _tool_ask, "search": _tool_search, "route": _tool_route,
             "read_page": _tool_read_page}
DISPATCH = dict(_TOOL_FNS)
DISPATCH.update({"wiki_" + n: fn for n, fn in _TOOL_FNS.items()})

# Which advertised tool a result belongs to, for structuredContent shaping (search returns a list).
_LIST_RESULT_TOOLS = {"search", "wiki_search"}


# F2 (100k-budget plan): session-cumulative accounting. Per-call caps (F1) bound one result; this
# counter bounds the SESSION — every tool result the host retains adds up in the model's window.
# Advisory, not a refusal: past the stop-line the result carries a directive the agent protocol
# card tells the model to obey (answer from what it has; stop reading).
#
# Per-session, not per-process: stdio's one process IS one session, so a bare module-global counter
# was correct there. Over HTTP, one process serves MANY callers (n8n's domain agents, concurrently),
# so the same global would leak one caller's budget into another's — keyed by session instead.
# ponytail: a plain dict that never evicts. Fine at the scale this actually runs at (stdio has
# exactly one entry; HTTP sees one entry per DISTINCT Mcp-Session-Id a caller sends us — and this
# server never ISSUES one, see do_POST, so in practice no compliant client ever sends one and this
# stays empty over HTTP). Add a TTL/LRU only if a real deployment starts minting many distinct ids.
_SESSION_CHARS = {}
SESSION_STOP_TOKENS = 60_000
STDIO_SESSION = "stdio"          # the stdio transport's one implicit session (whole process lifetime)


def _call_tool(session, msg_id, params):
    """Pure — returns the JSON-RPC response dict for a tools/call message, no I/O."""
    name = params.get("name")
    fn = DISPATCH.get(name)
    if fn is None:
        return {"jsonrpc": "2.0", "id": msg_id,
                "result": {"content": [{"type": "text", "text": "unknown tool: %s" % name}], "isError": True}}
    try:
        out = fn(params.get("arguments") or {})
        text = json.dumps(out, ensure_ascii=False)
        # session=None -> an HTTP caller with nothing to accumulate against (see handle()'s docstring):
        # charge this call's own size only, and don't touch the dict at all (no entry to ever grow).
        if session is None:
            chars = len(text)
        else:
            chars = _SESSION_CHARS.get(session, 0) + len(text)
            _SESSION_CHARS[session] = chars
        tokens = chars // 4
        if isinstance(out, dict):
            out["session_tokens_served"] = tokens
            if tokens > SESSION_STOP_TOKENS:
                out["budget_directive"] = ("session tool-result budget exceeded (%dk tokens served) — "
                                           "STOP retrieving; answer from the evidence already read."
                                           % (tokens // 1000))
            text = json.dumps(out, ensure_ascii=False)
        # `content` stays EXACTLY what it has always been (the verbatim serializer output), so no
        # existing consumer sees a shape change. structuredContent is additive and must be an object:
        # search's bare list is wrapped, every other tool already returns one.
        if name in _LIST_RESULT_TOOLS:
            structured = {"hits": out, "count": len(out) if isinstance(out, list) else 0,
                          "session_tokens_served": tokens}
        else:
            structured = out if isinstance(out, dict) else {"result": out}
        return {"jsonrpc": "2.0", "id": msg_id,
                "result": {"content": [{"type": "text", "text": text}],
                           "structuredContent": structured}}
    except ValueError as e:
        # Author-written argument errors (`domain and q are required`, `no such page: x`) — these are
        # the actionable ones, so the message goes to the caller verbatim.
        return {"jsonrpc": "2.0", "id": msg_id,
                "result": {"content": [{"type": "text", "text": str(e)}], "isError": True}}
    except Exception as e:                            # noqa: BLE001 — a bad tool call must never kill the loop
        # Anything else is an INTERNAL failure: its text can carry vault paths, stack context or
        # third-party detail the caller has no business seeing (best practice: don't expose internal
        # errors). Full detail goes to stderr for the operator; the caller gets the tool name, the
        # exception class, and what to do next.
        print("wikikb mcp: %s failed: %r" % (name, e), file=sys.stderr)
        return {"jsonrpc": "2.0", "id": msg_id,
                "result": {"content": [{"type": "text", "text":
                                        "%s failed internally (%s). The server log has the detail; "
                                        "retry with narrower arguments or check the wiki build."
                                        % (name, type(e).__name__)}], "isError": True}}


# ---------------------------------------------------------------------------------------------
# TWO ERAS. Revision 2026-07-28 split MCP in half, and the spec names the halves (basic/versioning
# #terminology): LEGACY versions establish a session with an `initialize` handshake (2025-11-25 and
# earlier); MODERN versions carry version/identity/capabilities as per-request `_meta` and have no
# handshake at all. They are not compatible — the spec's own matrix says "Modern client / Legacy
# server: Fails". A server that implements both is DUAL-ERA, which the spec explicitly permits on a
# single endpoint, and which is what this module is.
#
# The discriminator is the request itself, never connection state: a request carrying
# `params._meta["io.modelcontextprotocol/protocolVersion"]` is modern; anything else is legacy and
# takes the ORIGINAL code path below, byte-for-byte unchanged. That asymmetry is deliberate — every
# client that works today (n8n's bundled TS SDK negotiates 2025-11-25; Claude Code sends 2025-03-26)
# keeps working with zero behavior change, and modern support is purely additive.
# ---------------------------------------------------------------------------------------------

# LEGACY set, for the `initialize` handshake ONLY. 2026-07-28 deliberately does NOT belong here:
# initialize does not exist in the modern era, so answering "2026-07-28" to a legacy handshake would
# promise a protocol whose very next message shape we'd reject. Newest-first: index 0 is what we
# answer with when a legacy client asks for something we don't know.
SUPPORTED_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26")
MODERN_VERSIONS = ("2026-07-28",)
# What we advertise in `server/discover` and in an UnsupportedProtocolVersion error's `data.supported`
# — the honest full set for a dual-era server, so a client can pick any era we actually speak.
ALL_SUPPORTED_VERSIONS = MODERN_VERSIONS + SUPPORTED_VERSIONS

# Reserved `_meta` keys (basic/index #_meta). `protocolVersion` and `clientCapabilities` are REQUIRED
# on every modern request; `clientInfo` is SHOULD. `serverInfo` is the response-side counterpart.
META_VERSION = "io.modelcontextprotocol/protocolVersion"
META_CLIENT_CAPS = "io.modelcontextprotocol/clientCapabilities"
META_SERVER_INFO = "io.modelcontextprotocol/serverInfo"
SERVER_INFO = {"name": "wikikb", "version": "1.0"}

# MCP-specification error codes (basic/index #error-codes). The -32020..-32099 sub-range is reserved
# for the spec, and we MUST NOT emit anything in it that the spec hasn't defined.
ERR_HEADER_MISMATCH = -32020
ERR_MISSING_CLIENT_CAPABILITY = -32021
ERR_UNSUPPORTED_VERSION = -32022
ERR_INVALID_PARAMS = -32602
ERR_METHOD_NOT_FOUND = -32601


def request_meta(req):
    """The request's `params._meta` as a dict — {} when absent or malformed. Total on any input."""
    params = req.get("params")
    meta = params.get("_meta") if isinstance(params, dict) else None
    return meta if isinstance(meta, dict) else {}


def is_modern(req):
    """True when this request uses the per-request-metadata (2026-07-28+) era.

    Presence of the reserved protocolVersion `_meta` key IS the era signal — the spec makes that
    field REQUIRED on every modern request, so its absence unambiguously means legacy. Deliberately
    NOT keyed on the method name: a modern client's very first message may be any RPC (there is no
    handshake to look for), and `tools/list` exists in both eras."""
    return META_VERSION in request_meta(req)


def _err(msg_id, code, message, data=None):
    e = {"code": code, "message": message}
    if data is not None:
        e["data"] = data
    return {"jsonrpc": "2.0", "id": msg_id, "error": e}


def _modern_result(msg_id, result):
    """Wrap a result in the modern envelope: `resultType` is REQUIRED on every modern result, and
    servers SHOULD identify themselves via `_meta.serverInfo` on each one (there is no handshake
    where that could otherwise be stated)."""
    out = dict(result)
    out["resultType"] = "complete"
    out["_meta"] = dict(out.get("_meta") or {}, **{META_SERVER_INFO: SERVER_INFO})
    return {"jsonrpc": "2.0", "id": msg_id, "result": out}


def _handle_modern(req, session):
    """Dispatch ONE modern (2026-07-28+) message. Pure, same contract as handle()."""
    meta = request_meta(req)
    msg_id = req.get("id")
    has_id = "id" in req
    method = req.get("method")

    requested = meta.get(META_VERSION)
    if requested not in MODERN_VERSIONS:
        # Includes a client asking for a LEGACY version via modern `_meta` — a genuinely confused
        # mix we must not silently serve. `supported` lists both eras so it can pick again.
        return _err(msg_id, ERR_UNSUPPORTED_VERSION, "Unsupported protocol version",
                    {"supported": list(ALL_SUPPORTED_VERSIONS), "requested": requested})
    if META_CLIENT_CAPS not in meta:
        # "A request missing any required field is malformed; the server MUST reject it with -32602."
        return _err(msg_id, ERR_INVALID_PARAMS,
                    "Invalid params: missing required _meta field %s" % META_CLIENT_CAPS)

    if method == "server/discover":
        # MUST be implemented by every modern server (server/discover). Advertises BOTH eras.
        return _modern_result(msg_id, {
            "supportedVersions": list(ALL_SUPPORTED_VERSIONS),
            "capabilities": {"tools": {}},
            "instructions": "Offline Keycloak/OpenShift/Windows knowledge wiki. Use `route` to pick a "
                            "domain, `search` for reference-note hits, `ask` for a gated cited answer, "
                            "`read_page` to read a wiki page. Answers may carry a confidence banner — "
                            "preserve it verbatim; it marks synthesis that is not ground truth.",
        })
    if method == "tools/list":
        return _modern_result(msg_id, {"tools": TOOLS})
    if method == "tools/call":
        # Same DISPATCH, same tool bodies, same F1/F2 budget counters as the legacy path — only the
        # result envelope differs. Nothing about a tool is era-specific.
        resp = _call_tool(session, msg_id, req.get("params") or {})
        if "result" in resp:
            return _modern_result(msg_id, resp["result"])
        return resp
    if has_id:
        return _err(msg_id, ERR_METHOD_NOT_FOUND, "method not found: %s" % method)
    return None                                         # modern notification — nothing to send back


def _negotiate_version(requested):
    """Return the version to report at `initialize`.

    Previously this echoed `params.protocolVersion` back verbatim, so a client asking for
    'not-a-real-version-99' got that string returned as the NEGOTIATED version — the server
    effectively claiming support for a protocol it has never heard of, which is the one thing
    initialize exists to prevent. Per spec the server replies with the requested version only if it
    supports it, otherwise with a version it does support and lets the client decide whether to
    continue. Non-string junk (a dict, a number, None) falls through the same path."""
    if isinstance(requested, str) and requested in SUPPORTED_VERSIONS:
        return requested
    return SUPPORTED_VERSIONS[0]


def handle(req, session=STDIO_SESSION):
    """Dispatch ONE parsed JSON-RPC message and RETURN the response object — pure, no I/O, so it's
    the transport-agnostic core both transports share. A request (has "id") always returns exactly
    one response dict; a notification (no "id" key) returns None, per spec — the CALLER must then
    send nothing back (stdio's main() below skips the write; serve.py's do_POST replies 202 with no
    body). Nothing here ever touches stdout/a socket directly, which is what makes it reusable.

    `session` scopes the F2 budget counter above to the caller. Default STDIO_SESSION reproduces the
    ORIGINAL stdio behavior byte-for-byte (one accumulating counter for the process's whole life —
    stdio IS a single long-lived session, so this is the same number under a different name, not a
    behavior change). serve.py passes the caller's `Mcp-Session-Id` header, or None when the caller
    sent none — the common case, since this server follows the spec's documented "stateless mode"
    and never ISSUES a session id at `initialize`, so a spec-compliant HTTP client has none to send
    back either (see do_POST's comment for why that's the deliberate, research-backed design here).

    DUAL-ERA: a request carrying modern per-request `_meta` is served statelessly per 2026-07-28;
    everything else falls through to the ORIGINAL legacy handshake path below, unchanged. The era is
    read from the message, never remembered — which is exactly what the modern spec demands
    ("Servers MUST NOT rely on prior requests over the same connection to establish context") and
    what this server already did anyway."""
    if is_modern(req):
        return _handle_modern(req, session)

    method, params = req.get("method"), req.get("params") or {}
    has_id = "id" in req
    msg_id = req.get("id")

    if method == "initialize":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {
            "protocolVersion": _negotiate_version(params.get("protocolVersion")),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "wikikb", "version": "1.0"},
        }}
    if method == "notifications/initialized":
        return None                                     # notification: nothing to do, no response
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        return _call_tool(session, msg_id, params)
    if has_id:
        return {"jsonrpc": "2.0", "id": msg_id,
                "error": {"code": -32601, "message": "method not found: %s" % method}}
    return None                                         # unknown notification — ignore, no response


def _write(obj):
    """stdio's OWN sink: one JSON-RPC line to stdout, flushed immediately. Only main() below calls
    this — handle() itself never writes anything, by design (see its docstring)."""
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main():
    # Reconfigure explicitly to UTF-8 regardless of host locale — the protocol is UTF-8 no matter
    # what environment this child process inherits.
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print("wikikb mcp: serving over stdio (EOF to exit)", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            _write({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}})
            continue
        try:
            resp = handle(req)
        except Exception as e:                        # noqa: BLE001 — one bad line must never kill the loop
            resp = {"jsonrpc": "2.0", "id": req.get("id"), "error": {"code": -32603, "message": str(e)}}
        if resp is not None:                          # None = notification; spec says send nothing back
            _write(resp)


if __name__ == "__main__":
    main()
