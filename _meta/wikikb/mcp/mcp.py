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
"""
import json
import sys

sys.dont_write_bytecode = True
from wikikb.graph import ask as askmod
from wikikb.serve.serve import do_page, do_route, do_search

PROTOCOL_VERSION = "2025-03-26"

TOOLS = [
    {
        "name": "ask",
        "description": "Ask the wiki a question; returns a gated, cited answer",
        "inputSchema": {
            "type": "object",
            "properties": {
                "question": {"type": "string"},
                "domain": {"type": "string"},
                "tier": {"type": "string", "enum": ["conceptual", "support-kb", "scenarios"]},
                "k": {"type": "integer"},
            },
            "required": ["question"],
        },
    },
    {
        "name": "search",
        "description": "Top-k reference-note hits (id/title/score/snippet) for a domain",
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
        "name": "route",
        "description": "Route a query to its likely domain(s)",
        "inputSchema": {
            "type": "object",
            "properties": {"q": {"type": "string"}},
            "required": ["q"],
        },
    },
    {
        "name": "read_page",
        "description": "Read a wiki page's frontmatter + body by slug (topics/entities/questions). Long bodies are served in ~8k-char slices; pass offset=next_offset for more.",
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
    # same shape as `wikikb ask --json` (ask.py main()) — a host consuming this tool sees the
    # identical answer a human running the CLI would.
    return {
        "query": q, "orchestrator": st.get("orchestrator"), "domain": st.get("domain"), "confident": st.get("confident"),
        "thin": st.get("thin"), "banner": st.get("banner") or [], "answer": st.get("answer", ""),
        "cited": st.get("used", []), "grounding_fail": st.get("grounding_fail", False),
        "references": refs,
    }


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


DISPATCH = {"ask": _tool_ask, "search": _tool_search, "route": _tool_route, "read_page": _tool_read_page}


def _respond(msg_id, result=None, error=None):
    """Write ONE JSON-RPC 2.0 response line to stdout and flush. Notifications never reach here
    (callers only invoke this for requests, which carry an id — possibly None for parse errors,
    which the spec requires)."""
    obj = {"jsonrpc": "2.0", "id": msg_id}
    obj["error" if error is not None else "result"] = error if error is not None else result
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


# F2 (100k-budget plan): session-cumulative accounting. Per-call caps (F1) bound one result; this
# counter bounds the SESSION — every tool result the host retains adds up in the model's window.
# Advisory, not a refusal: past the stop-line the result carries a directive the agent protocol
# card tells the model to obey (answer from what it has; stop reading).
_SESSION_CHARS = 0
SESSION_STOP_TOKENS = 60_000


def _call_tool(msg_id, params):
    global _SESSION_CHARS
    name = params.get("name")
    fn = DISPATCH.get(name)
    if fn is None:
        _respond(msg_id, result={"content": [{"type": "text", "text": "unknown tool: %s" % name}],
                                  "isError": True})
        return
    try:
        out = fn(params.get("arguments") or {})
        text = json.dumps(out, ensure_ascii=False)
        _SESSION_CHARS += len(text)
        tokens = _SESSION_CHARS // 4
        if isinstance(out, dict):
            out["session_tokens_served"] = tokens
            if tokens > SESSION_STOP_TOKENS:
                out["budget_directive"] = ("session tool-result budget exceeded (%dk tokens served) — "
                                           "STOP retrieving; answer from the evidence already read."
                                           % (tokens // 1000))
            text = json.dumps(out, ensure_ascii=False)
        _respond(msg_id, result={"content": [{"type": "text", "text": text}]})
    except Exception as e:                            # noqa: BLE001 — a bad tool call must never kill the loop
        _respond(msg_id, result={"content": [{"type": "text", "text": str(e)}], "isError": True})


def _handle(req):
    """Dispatch one parsed JSON-RPC message. A request (has "id") always gets exactly one
    response; a notification (no "id" key) gets none, per spec."""
    method, params = req.get("method"), req.get("params") or {}
    has_id = "id" in req
    msg_id = req.get("id")

    if method == "initialize":
        _respond(msg_id, result={
            "protocolVersion": params.get("protocolVersion") or PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "wikikb", "version": "1.0"},
        })
    elif method == "notifications/initialized":
        pass                                           # notification: nothing to do, no response
    elif method == "tools/list":
        _respond(msg_id, result={"tools": TOOLS})
    elif method == "tools/call":
        _call_tool(msg_id, params)
    elif has_id:
        _respond(msg_id, error={"code": -32601, "message": "method not found: %s" % method})
    # else: unknown notification — ignore, no response for a message with no id


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
            _respond(None, error={"code": -32700, "message": "parse error"})
            continue
        try:
            _handle(req)
        except Exception as e:                        # noqa: BLE001 — one bad line must never kill the loop
            _respond(req.get("id"), error={"code": -32603, "message": str(e)})


if __name__ == "__main__":
    main()
