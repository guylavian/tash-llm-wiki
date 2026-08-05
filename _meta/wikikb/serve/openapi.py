#!/usr/bin/env python3
"""openapi.py — the OpenAPI 3.1 description of serve.py's HTTP surface, plus a dependency-free
docs page. stdlib only, no network, no vendored assets.

WHY NOT STOCK SWAGGER UI: the usual `<script src="https://unpkg.com/swagger-ui-dist/...">` page
renders BLANK on an air-gapped box — which is this project's actual deployment target (CLAUDE.md:
"stdlib only, air-gapped", and serve.py opens no socket it wasn't told to). Vendoring swagger-ui-dist
would add ~1 MB of third-party JS into a repo whose whole thesis is copy-and-run with zero deps.

So the split is:
  GET /openapi.json — the REAL, portable artifact. Point stock Swagger UI, Postman, Insogmnia, n8n,
                      or an SDK generator at it and you get the full interactive experience, with the
                      third-party tooling living on the operator's workstation instead of in the image.
  GET /docs         — a self-contained HTML rendering (inline CSS, one small inline script, zero
                      external requests) so an operator on the sealed box still gets a readable,
                      try-it-out reference with nothing to install.

The spec is BUILT FROM the live server config (the MCP mount point moves with WIKIKB_MCP_PATH, the
security scheme appears only when WIKIKB_API_TOKEN is set), so it cannot drift from what is actually
being served the way a hand-maintained YAML file would.
"""
import json
import os

from wikikb import modes

# One schema per response shape serve.py actually returns. Kept inline (not $ref-heavy) because the
# surface is small and a flat spec is far easier to eyeball against the handlers it documents.
_ERROR = {
    "type": "object",
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}


def _q(name, desc, required=False, schema=None, example=None):
    p = {"name": name, "in": "query", "description": desc, "required": required,
         "schema": schema or {"type": "string"}}
    if example is not None:
        p["example"] = example
    return p


def _json_response(desc, schema):
    return {"description": desc, "content": {"application/json": {"schema": schema}}}


def _errors(*codes):
    out = {}
    for code, desc in codes:
        out[str(code)] = _json_response(desc, _ERROR)
    return out


def build_spec(mcp_path="/mcp", auth_required=False, vault=None, version="1.1.0",
               mode=modes.AIRGAPPED):
    """Return the OpenAPI 3.1 document as a dict.

    mcp_path      — live value of serve.MCP_PATH, so relocating the MCP mount is reflected here.
    auth_required — True when WIKIKB_API_TOKEN is set; adds the bearer scheme AND the global
                    `security` requirement. When unset we deliberately emit NO security block:
                    advertising auth that isn't enforced is worse than advertising none.
    vault         — the resolved vault path, surfaced in the description so an operator reading
                    /docs can confirm which corpus this instance is actually serving.
    mode          — the live WIKIKB_MODE. The scrape paths are emitted ONLY in online mode, for the
                    same reason serve.py hides them there: a spec that documents an endpoint this
                    instance answers as "unknown path" is a spec that lies, and it would also hand a
                    reader of an airgapped /docs a map of a surface that does not exist here.
    """
    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": "wikikb — llm-wiki JSON API",
            "version": version,
            "description": (
                "Stateless JSON API over the LLM-maintained knowledge wiki. Every handler is a thin "
                "translation to the same functions the `python3 -m wikikb <tool>` CLI calls — nothing "
                "is re-implemented.\n\n"
                + (f"**Vault served by this instance:** `{vault}`\n\n" if vault else "")
                + f"**Operation mode:** `{mode}`. "
                + ("Airgapped — vault, MCP and the PDF ingest chain; no outbound network, and the "
                   "web-scraper paths are absent (they answer exactly like an unknown path).\n\n"
                   if mode != modes.ONLINE else
                   "Online — everything airgapped serves, plus the web-scraper surface. The modes "
                   "are additive, so a client written against an airgapped instance works here "
                   "unchanged.\n\n")
                + "**Answers are gated.** `/ask` applies the Confidence gate before returning: a "
                "response resting on synthesis rather than extracted sources carries a `⚠️` banner. "
                "Treat a banner as 'verify before acting', not as prose decoration."
            ),
        },
        "servers": [{"url": "/", "description": "this instance"}],
        "tags": [
            {"name": "retrieval", "description": "Route, search, expand, and read pages."},
            {"name": "answers", "description": "Gated, cited synthesis."},
            {"name": "ingest", "description": "Write surface — opt-in, off by default."},
            {"name": "jobs", "description": "Background conversion jobs queued by the write surface."},
            {"name": "scrape", "description": "Web harvest — ONLINE MODE ONLY."},
            {"name": "meta", "description": "Health and machine-readable description."},
        ],
        "paths": {},
    }

    spec["paths"]["/health"] = {
        "get": {
            "tags": ["meta"], "summary": "Liveness + corpus fingerprint",
            "description": ("Intentionally UNAUTHENTICATED even when a bearer token is configured, so "
                            "kubelet-style probes (which cannot attach custom headers) still work. "
                            "Returns the declared domains and total page count — useful for confirming "
                            "a bind-mounted vault actually landed.\n\n"
                            "`capabilities` is what the MODE permits; `uploads`/`auto_ingest` are what "
                            "THIS process switched on. They are reported separately so 'wrong mode' and "
                            "'forgot --allow-upload' are distinguishable."),
            "security": [],
            "responses": {"200": _json_response("Server is up.", {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "ok"},
                    "mode": {"type": "string", "enum": list(modes.MODES)},
                    "capabilities": {"type": "object", "properties": {
                        "vault": {"type": "boolean"}, "mcp": {"type": "boolean"},
                        "ingest": {"type": "boolean"},
                        "scrape": {"type": "boolean", "description": "true only in online mode"}}},
                    "uploads": {"type": "boolean", "description": "PUT /upload enabled on this process"},
                    "auto_ingest": {"type": "boolean",
                                    "description": "an upload also queues the conversion chain"},
                    "domains": {"type": "array", "items": {"type": "string"}},
                    "pages": {"type": "integer", "description": "synthesis pages discovered in the vault"},
                },
            })},
        }
    }

    spec["paths"]["/route"] = {
        "get": {
            "tags": ["retrieval"], "summary": "Route a question to its domain(s)",
            "description": ("Keyword match against each domain's `areas:` vocabulary. Conservative by "
                            "design: `confident: true` is never wrong, so a confident route lets a "
                            "client skip the cross-domain index entirely. `confident: false` means "
                            "the router abstained — disambiguate before searching."),
            "parameters": [_q("q", "The natural-language question.", True, example="keycloak ldap federation")],
            "responses": {"200": _json_response("Routing decision.", {
                "type": "object",
                "properties": {
                    "domains": {"type": "array", "items": {"type": "string"}},
                    "confident": {"type": "boolean"},
                },
            })},
        }
    }

    spec["paths"]["/search"] = {
        "get": {
            "tags": ["retrieval"], "summary": "Lexical search over a domain's reference tier",
            "parameters": [
                _q("domain", "Domain slug, e.g. `keycloak`. Must be declared in the vault taxonomy.",
                   True, example="keycloak"),
                _q("q", "Search terms.", True, example="jdbc-ping"),
                _q("k", "Max hits.", False, {"type": "integer", "default": 5, "minimum": 1}),
            ],
            "responses": {
                "200": _json_response("Ranked hits.", {
                    "type": "array",
                    "items": {"type": "object", "properties": {
                        "id": {"type": "string"}, "title": {"type": "string"},
                        "score": {"type": "number"}, "snippet": {"type": "string"},
                    }},
                }),
                **_errors((400, "Missing/unknown domain or empty query.")),
            },
        }
    }

    spec["paths"]["/ask"] = {
        "get": {
            "tags": ["answers"], "summary": "Gated, cited answer",
            "description": ("Runs retrieval → synthesis → the Confidence gate. The returned answer may "
                            "carry a `⚠️` banner (out-of-coverage, ungrounded provenance, or "
                            "provisional). With `strict=true`, an answer whose citations cannot be "
                            "grounded is WITHHELD rather than served with a warning — prefer strict "
                            "for unattended/automated callers."),
            "parameters": [
                _q("q", "The question.", True, example="how do I configure jdbc-ping discovery?"),
                _q("domain", "Restrict to one domain. Omitted ⇒ the router decides.", False, example="keycloak"),
                _q("k", "Retrieval depth.", False, {"type": "integer", "default": 5, "minimum": 1}),
                _q("tier", "Question tier for the gate's coverage arm.",
                   False, {"type": "string", "enum": ["conceptual", "support-kb", "scenarios"]}),
                _q("strict", "Withhold instead of flagging when grounding fails.",
                   False, {"type": "boolean", "default": False}),
            ],
            "responses": {
                "200": _json_response("Answer, plus grounding/provenance fields.", {
                    "type": "object",
                    "properties": {
                        "answer": {"type": "string"},
                        "domain": {"type": "string"},
                        "banner": {"type": ["string", "null"],
                                   "description": "Confidence-gate banner; null when no arm fired."},
                        "citations": {"type": "array", "items": {"type": "string"}},
                        "withheld": {"type": "boolean",
                                     "description": "True when strict mode suppressed an ungrounded answer."},
                    },
                }),
                **_errors((400, "Empty query or unknown domain.")),
            },
        }
    }

    spec["paths"]["/expand"] = {
        "get": {
            "tags": ["retrieval"], "summary": "1-hop graph neighbourhood for a query",
            "description": ("Returns the reference notes cited by the query's seed pages and by their "
                            "immediate `[[wikilink]]` neighbours — WITHOUT running a second search. "
                            "This is the multi-hop entry point: a paraphrased query that lexical "
                            "ranks deep often still matches a page that CITES the right note."),
            "parameters": [
                _q("domain", "Domain slug.", True, example="keycloak"),
                _q("q", "The query.", True, example="cluster discovery in air-gapped kubernetes"),
            ],
            "responses": {
                "200": _json_response("Cited-note neighbourhood.", {
                    "type": "object",
                    "properties": {"notes": {"type": "array", "items": {"type": "string"}}},
                }),
                **_errors((400, "Missing/unknown domain.")),
            },
        }
    }

    spec["paths"]["/page/{slug}"] = {
        "get": {
            "tags": ["retrieval"], "summary": "Read one synthesis page",
            "description": ("Bodies are served in bounded slices; use `offset` with the returned "
                            "`next_offset` to page through a long note rather than demanding it whole."),
            "parameters": [
                {"name": "slug", "in": "path", "required": True,
                 "description": "Kebab-case page slug. Anything else fails the shape check before a "
                                "filesystem path is built — which is what makes this traversal-safe.",
                 "schema": {"type": "string", "pattern": "^[a-z0-9][a-z0-9-]*$"},
                 "example": "jdbc-ping"},
                _q("offset", "Byte offset into the body.", False, {"type": "integer", "default": 0, "minimum": 0}),
                _q("max_chars", "Max characters in this slice.", False, {"type": "integer", "minimum": 1}),
            ],
            "responses": {
                "200": _json_response("The page.", {
                    "type": "object",
                    "properties": {
                        "slug": {"type": "string"}, "path": {"type": "string"},
                        "frontmatter": {"type": "object", "additionalProperties": True},
                        "body": {"type": "string"},
                        "next_offset": {"type": ["integer", "null"]},
                    },
                }),
                **_errors((400, "Malformed slug."), (404, "No such page.")),
            },
        }
    }

    spec["paths"]["/upload/{domain}/{filename}"] = {
        "put": {
            "tags": ["ingest"], "summary": "Upload a PDF into the raw tier (opt-in)",
            "description": (
                "**Disabled by default.** Enable with `--allow-upload` / `WIKIKB_ALLOW_UPLOAD=1`. When "
                "disabled the response is byte-identical to an unknown path, so the surface is not "
                "fingerprintable.\n\n"
                "Body is the RAW file (`curl -T file.pdf ...`), not multipart. Stores only under "
                "`vault/_sources/<domain>/_raw/pdfs/` — never the immutable reference tier.\n\n"
                "Storing the file also QUEUES the conversion chain in the background — "
                "`pdf_to_corpus --append` → `corpus_to_vault` → `build` (whose crosslink step is what "
                "links the new document to the other Markdown files) — and returns a `job_id`; poll "
                "`GET /jobs/{id}`. The response is 201, not 202, because the file itself is durable "
                "by the time it answers; the job is reported alongside.\n\n"
                "Set `WIKIKB_AUTO_INGEST=0` for the old store-only behaviour and drive the chain with "
                "`POST /ingest/{domain}` instead — the batch path when several PDFs should share one "
                "`build`. Note that synthesis pages are NOT written by the chain: it lands the "
                "document as an immutable reference note, and the citation contract is applied when a "
                "page is authored against it."),
            "parameters": [
                {"name": "domain", "in": "path", "required": True,
                 "schema": {"type": "string", "pattern": "^[a-z0-9][a-z0-9-]*$"}, "example": "keycloak"},
                {"name": "filename", "in": "path", "required": True,
                 "schema": {"type": "string", "pattern": r"^[A-Za-z0-9][A-Za-z0-9._-]*\.pdf$"},
                 "example": "server-guide.pdf"},
            ],
            "requestBody": {"required": True, "content": {"application/pdf": {
                "schema": {"type": "string", "format": "binary"}}}},
            "responses": {
                "201": _json_response("Stored (and, unless auto-ingest is off, conversion queued).", {
                    "type": "object",
                    "properties": {
                        "stored": {"type": "string", "description": "path relative to the vault root"},
                        "ingest": {"type": "string",
                                   "description": "queued | coalesced into pending job | disabled | not queued"},
                        "job_id": {"type": "string"},
                        "status_url": {"type": "string", "example": "/jobs/9f2c1a0b4d7e"},
                        "next": {"type": "string", "description": "what to do next, in words"}},
                }),
                **_errors(
                    (404, "Uploads disabled, or path shape not matched (deliberately indistinguishable)."),
                    (409, "A file of that name already exists — the raw tier is immutable."),
                    (411, "Content-Length required."),
                    (413, "Body exceeds the 50 MB cap."),
                    (415, "Body is not a PDF (magic-byte check)."),
                ),
            },
        }
    }

    spec["paths"]["/ingest/{domain}"] = {
        "post": {
            "tags": ["ingest"], "summary": "Queue the conversion chain for a domain (opt-in)",
            "description": (
                "Runs the same three steps an upload queues — `pdf_to_corpus --append` → "
                "`corpus_to_vault` → `build` — over everything currently in "
                "`vault/_sources/{domain}/_raw/pdfs/`. Use it to batch several drops into one "
                "`build`, or to retry after a failed job.\n\n"
                "Gated by the SAME `--allow-upload` opt-in as `/upload`: it writes to the vault, so "
                "it is part of the one write surface, not a second one that could stay open after "
                "uploads were deliberately disabled. Disabled ⇒ indistinguishable from an unknown path.\n\n"
                "A submission for a domain that already has a QUEUED job returns that job "
                "(`coalesced: true`) instead of a duplicate — the chain reads the whole directory, so "
                "the pending job will see the new files anyway."),
            "parameters": [{"name": "domain", "in": "path", "required": True,
                            "schema": {"type": "string", "pattern": "^[a-z0-9][a-z0-9-]*$"},
                            "example": "keycloak"}],
            "responses": {
                "202": _json_response("Job queued.", {
                    "type": "object",
                    "properties": {"job_id": {"type": "string"}, "status_url": {"type": "string"},
                                   "state": {"type": "string"}, "coalesced": {"type": "boolean"},
                                   "steps": {"type": "array", "items": {"type": "string"}}},
                }),
                **_errors((400, "Domain not declared in the vault taxonomy."),
                          (404, "Write surface disabled (indistinguishable from an unknown path)."),
                          (429, "Job queue full — retry once the backlog drains.")),
            },
        }
    }

    _JOB = {
        "type": "object",
        "properties": {
            "id": {"type": "string"}, "kind": {"type": "string", "example": "ingest"},
            "state": {"type": "string", "enum": ["queued", "running", "done", "failed"]},
            "domain": {"type": "string"},
            "created": {"type": "number"}, "started": {"type": ["number", "null"]},
            "finished": {"type": ["number", "null"]},
            "steps": {"type": "array", "items": {"type": "string"}},
            "current_step": {"type": ["string", "null"]},
            "results": {"type": "array", "items": {"type": "object", "properties": {
                "step": {"type": "string"}, "exit": {"type": "integer"},
                "seconds": {"type": "number"},
                "log": {"type": "array", "items": {"type": "string"},
                        "description": "tail of the step's combined output, capped"}}}},
            "error": {"type": "string"},
        },
    }

    spec["paths"]["/jobs"] = {
        "get": {
            "tags": ["jobs"], "summary": "Recent jobs (newest first)",
            "description": ("Job state is IN-MEMORY and lost on restart: it is progress reporting, not "
                            "provenance. The durable record of what was ingested is the vault plus "
                            "`.manifest.json`."),
            "responses": {"200": _json_response("Recent jobs plus runner stats.", {
                "type": "object",
                "properties": {"jobs": {"type": "array", "items": _JOB},
                               "stats": {"type": "object", "properties": {
                                   "pending": {"type": "integer"}, "retained": {"type": "integer"},
                                   "worker": {"type": "boolean"}}}}})},
        }
    }

    spec["paths"]["/jobs/{id}"] = {
        "get": {
            "tags": ["jobs"], "summary": "One job's state and step log",
            "description": ("Steps run in order and STOP at the first failure — continuing past a "
                            "failed extraction would fold a stale corpus into the reference tier. On "
                            "`failed`, the last entry in `results` carries the exit code and the tail "
                            "of that step's output."),
            "parameters": [{"name": "id", "in": "path", "required": True,
                            "schema": {"type": "string", "pattern": "^[0-9a-f]{12}$"}}],
            "responses": {"200": _json_response("The job.", _JOB),
                          **_errors((400, "Malformed job id."),
                                    (404, "No such job, or its record has been evicted."))},
        }
    }

    if mode == modes.ONLINE:
        spec["paths"]["/scrape"] = {
            "post": {
                "tags": ["scrape"], "summary": "Harvest a web source (ONLINE MODE ONLY)",
                "description": ("Mounted only when `WIKIKB_MODE=online`; in airgapped mode this path "
                                "answers exactly like an unknown path and is absent from this "
                                "document.\n\n**Not implemented yet** — `wikikb/scrape/scrape.py` is "
                                "the declared seam and currently answers 501. When written, a scrape "
                                "lands in `vault/_sources/{domain}/_raw/web/` and runs through the "
                                "same job runner as the PDF chain."),
                "responses": {**_errors((501, "Not implemented yet — see wikikb/scrape/scrape.py."))},
            }
        }
        spec["paths"]["/scrape/sources"] = {
            "get": {"tags": ["scrape"], "summary": "Configured scrape sources (ONLINE MODE ONLY)",
                    "description": "**Not implemented yet** — answers 501.",
                    "responses": {**_errors((501, "Not implemented yet."))}}
        }

    spec["paths"][mcp_path] = {
        "post": {
            "tags": ["meta"], "summary": "MCP over HTTP (JSON-RPC 2.0)",
            "description": (
                "Streamable-HTTP MCP transport — one JSON-RPC message per call, no SSE, no sessions. "
                "Dual-era: serves both the legacy `initialize` handshake and the 2026-07-28+ "
                "per-request `_meta` era, chosen per request.\n\n"
                "Tools: `wiki_ask` (the only non-read-only one), `wiki_search`, `wiki_route`, "
                "`wiki_read_page`.\n\n"
                f"Mount point is configurable via `WIKIKB_MCP_PATH` (currently `{mcp_path}`). "
                "`Origin` is validated when present — a browser-based DNS-rebinding attempt gets 403, "
                "while a backend client sending no `Origin` is unaffected."),
            "requestBody": {"required": True, "content": {"application/json": {
                "schema": {"type": "object", "properties": {
                    "jsonrpc": {"type": "string", "const": "2.0"},
                    "id": {"type": ["string", "integer", "null"]},
                    "method": {"type": "string", "example": "tools/list"},
                    "params": {"type": "object", "additionalProperties": True},
                }, "required": ["jsonrpc", "method"]}}}},
            "responses": {
                "200": _json_response("JSON-RPC result.", {"type": "object", "additionalProperties": True}),
                "202": {"description": "Notification accepted (no body)."},
                **_errors((403, "Origin present but not allowlisted."),
                          (413, "Body exceeds the 2 MB cap.")),
            },
        },
        "get": {"tags": ["meta"], "summary": "Not supported (no SSE stream)",
                "responses": _errors((405, "Spec-legal decline of the optional standalone SSE stream."))},
        "delete": {"tags": ["meta"], "summary": "Not supported (stateless — no sessions)",
                   "responses": _errors((405, "No session to terminate."))},
    }

    # NOT security-exempt when a token is configured. /health is exempt for a concrete reason
    # (kubelet-style probes cannot attach headers); no such reason applies to a full map of the
    # API, and serving one to an unauthenticated caller would contradict the same posture that
    # makes a disabled upload surface unfingerprintable. Swagger UI/Postman send bearer tokens fine.
    spec["paths"]["/openapi.json"] = {
        "get": {"tags": ["meta"], "summary": "This document",
                "responses": {"200": _json_response("OpenAPI 3.1 document.",
                                                    {"type": "object", "additionalProperties": True})}}
    }
    spec["paths"]["/docs"] = {
        "get": {"tags": ["meta"], "summary": "Human-readable API reference (self-contained HTML)",
                "responses": {"200": {"description": "HTML page.",
                                      "content": {"text/html": {"schema": {"type": "string"}}}}}}
    }

    if auth_required:
        spec["components"] = {"securitySchemes": {"bearerAuth": {
            "type": "http", "scheme": "bearer",
            "description": "Set `WIKIKB_API_TOKEN` on the server; send `Authorization: Bearer <token>`. "
                           "Only `/health` is exempt (unauthenticated probes)."}}}
        spec["security"] = [{"bearerAuth": []}]
    return spec


# --- the offline docs page -------------------------------------------------------------------
# Inline CSS + one inline script, zero external requests (a CSP-tight, air-gapped box renders this
# identically to a networked one). Theme-aware so it isn't blinding in a dark terminal-adjacent setup.
_DOCS_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>wikikb API</title>
<style>
:root{--bg:#fff;--fg:#1a1a1a;--mut:#5a5f66;--line:#e3e6ea;--card:#fafbfc;--acc:#0b6bcb;
      --get:#0b6bcb;--post:#1a7f4b;--put:#a15c00;--del:#b3261e;--code:#f3f5f7}
@media(prefers-color-scheme:dark){:root{--bg:#14171a;--fg:#e8eaed;--mut:#9aa3ad;--line:#2a2f35;
      --card:#1b1f24;--acc:#5ea9ff;--get:#5ea9ff;--post:#5fd39b;--put:#e0a458;--del:#ff8a80;--code:#1f242a}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:32px 20px 80px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:15px;text-transform:uppercase;letter-spacing:.08em;
   color:var(--mut);margin:36px 0 12px;font-weight:600}
.sub{color:var(--mut);margin:0 0 8px}
.op{border:1px solid var(--line);border-radius:8px;margin:10px 0;overflow:hidden;background:var(--card)}
.op>summary{cursor:pointer;padding:12px 14px;display:flex;gap:10px;align-items:center;list-style:none}
.op>summary::-webkit-details-marker{display:none}
.m{font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;padding:5px 8px;border-radius:4px;
   color:#fff;flex:none;letter-spacing:.05em}
.GET{background:var(--get)}.POST{background:var(--post)}.PUT{background:var(--put)}.DELETE{background:var(--del)}
.p{font:13px/1 ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:600}
.s{color:var(--mut);font-size:13px;margin-left:auto;text-align:right}
.body{padding:0 14px 14px;border-top:1px solid var(--line)}
.desc{white-space:pre-wrap;margin:12px 0}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13px;display:block;overflow-x:auto}
th,td{text-align:left;padding:6px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--mut);font-weight:600;white-space:nowrap}
code{background:var(--code);padding:1px 5px;border-radius:3px;
     font:13px ui-monospace,SFMono-Regular,Menlo,monospace}
.req{color:var(--del);font-size:11px}
a{color:var(--acc)}
.note{border-left:3px solid var(--acc);padding:10px 14px;background:var(--card);margin:14px 0;font-size:14px}
</style></head><body><div class="wrap">
<h1>wikikb — llm-wiki JSON API</h1>
<p class="sub" id="ver"></p>
<div class="desc" id="info"></div>
<div class="note"><strong>Interactive UI:</strong> this page is deliberately dependency-free so it
renders on an air-gapped host. For try-it-out, point Swagger UI / Postman / Insomnia at
<a href="openapi.json"><code>/openapi.json</code></a>.</div>
<div id="ops"></div>
</div><script>
fetch("openapi.json").then(r=>r.json()).then(spec=>{
  document.getElementById("ver").textContent = spec.info.title + " · v" + spec.info.version;
  document.getElementById("info").textContent = spec.info.description || "";
  const order = {get:0,post:1,put:2,delete:3}, out = document.getElementById("ops");
  const groups = {};
  for (const [path, item] of Object.entries(spec.paths)) {
    for (const [method, op] of Object.entries(item)) {
      const tag = (op.tags && op.tags[0]) || "other";
      (groups[tag] = groups[tag] || []).push({path, method, op});
    }
  }
  for (const tag of (spec.tags || []).map(t => t.name).concat(Object.keys(groups))) {
    if (!groups[tag]) continue;
    const h = document.createElement("h2"); h.textContent = tag; out.appendChild(h);
    groups[tag].sort((a,b)=> a.path.localeCompare(b.path) || order[a.method]-order[b.method]);
    for (const {path, method, op} of groups[tag]) {
      const d = document.createElement("details"); d.className = "op";
      const M = method.toUpperCase();
      const params = op.parameters || [];
      let rows = "";
      for (const p of params) {
        const sch = p.schema || {};
        const type = sch.enum ? sch.enum.join(" | ") : (sch.type || "string");
        const def = sch.default !== undefined ? ` <code>default ${sch.default}</code>` : "";
        rows += `<tr><td><code>${p.name}</code>${p.required?' <span class="req">required</span>':''}</td>`
              + `<td><code>${type}</code>${def}</td><td>${p.description||""}</td></tr>`;
      }
      const ptable = rows ? `<table><tr><th>Parameter</th><th>Type</th><th>Description</th></tr>${rows}</table>` : "";
      let rrows = "";
      for (const [code, r] of Object.entries(op.responses || {}))
        rrows += `<tr><td><code>${code}</code></td><td>${r.description||""}</td></tr>`;
      const rtable = rrows ? `<table><tr><th>Status</th><th>Meaning</th></tr>${rrows}</table>` : "";
      d.innerHTML = `<summary><span class="m ${M}">${M}</span><span class="p">${path}</span>`
                  + `<span class="s">${op.summary||""}</span></summary>`
                  + `<div class="body"><div class="desc">${(op.description||"").replace(/</g,"&lt;")}</div>`
                  + ptable + rtable + `</div>`;
      out.appendChild(d);
    }
  }
}).catch(e => { document.getElementById("ops").textContent = "Could not load openapi.json: " + e; });
</script></body></html>
"""


def docs_html():
    """The self-contained docs page (bytes-ready str). Fetches only same-origin openapi.json."""
    return _DOCS_HTML


def spec_json(mcp_path="/mcp", auth_required=False, vault=None, mode=modes.AIRGAPPED):
    return json.dumps(build_spec(mcp_path, auth_required, vault, mode=mode),
                      indent=2, ensure_ascii=False)


if __name__ == "__main__":                      # `python3 -m wikikb.serve.openapi > openapi.json`
    # current_safe(), not current(): dumping the spec must not die on a bad WIKIKB_MODE — that is
    # serve.main()'s refusal to make, and an operator generating a client is often not on the box
    # whose env is misconfigured.
    print(spec_json(os.environ.get("WIKIKB_MCP_PATH", "/mcp"),
                    bool(os.environ.get("WIKIKB_API_TOKEN")),
                    mode=modes.current_safe()[0]))
