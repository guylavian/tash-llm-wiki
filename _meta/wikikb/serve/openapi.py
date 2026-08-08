#!/usr/bin/env python3
"""openapi.py — the OpenAPI 3.1 description of serve.py's HTTP surface, plus a dependency-free
docs page WITH try-it-out. stdlib only, no network, no vendored assets.

WHY NOT STOCK SWAGGER UI: the usual `<script src="https://unpkg.com/swagger-ui-dist/...">` page
renders BLANK on an air-gapped box — which is this project's actual deployment target (CLAUDE.md:
"stdlib only, air-gapped", and serve.py opens no socket it wasn't told to). Vendoring swagger-ui-dist
would add ~1 MB of third-party JS into a repo whose whole thesis is copy-and-run with zero deps.

So the split is:
  GET /openapi.json — the REAL, portable artifact. Point stock Swagger UI, Postman, Insomnia, n8n,
                      or an SDK generator at it and you get the full third-party experience, with the
                      tooling living on the operator's workstation instead of in the image.
  GET /docs         — a self-contained HTML rendering (inline CSS, one small inline script, zero
                      external requests) that documents the INPUT and OUTPUT structure of every
                      endpoint and can CALL it: each operation carries a "Try it" panel that builds
                      the request from the spec's own parameters/requestBody and fetches it
                      same-origin. ~500 lines of vanilla JS, no dependency, renders identically on a
                      sealed box.

The spec is BUILT FROM the live server config (the MCP mount point moves with WIKIKB_MCP_PATH, the
security scheme appears only when WIKIKB_API_TOKEN is set), so it cannot drift from what is actually
being served the way a hand-maintained YAML file would. The response schemas below are written
against serve.py's handlers field-by-field — a documented field a handler doesn't return is the same
class of lie as a documented endpoint that answers 404.
"""
import json
import os

from wikikb import modes

# One schema per response shape serve.py actually returns. Kept inline (not $ref-heavy) because the
# surface is small and a flat spec is far easier to eyeball against the handlers it documents.
_ERROR = {
    "type": "object",
    "properties": {"error": {"type": "string", "description": "Human-readable failure reason."}},
    "required": ["error"],
    "example": {"error": "domain and q are required"},
}


def _q(name, desc, required=False, schema=None, example=None):
    p = {"name": name, "in": "query", "description": desc, "required": required,
         "schema": schema or {"type": "string"}}
    if example is not None:
        p["example"] = example
    return p


def _path_param(name, desc, pattern="^[a-z0-9][a-z0-9-]*$", example=None):
    p = {"name": name, "in": "path", "required": True, "description": desc,
         "schema": {"type": "string", "pattern": pattern}}
    if example is not None:
        p["example"] = example
    return p


def _json_response(desc, schema, example=None):
    """One response entry. `example` is attached to the MEDIA TYPE (not the schema) so the docs page
    can show a real payload without the generated-from-schema placeholder guesswork, and so a
    generator that ignores examples still sees a clean schema."""
    media = {"schema": schema}
    if example is not None:
        media["example"] = example
    return {"description": desc, "content": {"application/json": media}}


def _errors(*codes):
    out = {}
    for code, desc in codes:
        out[str(code)] = _json_response(desc, _ERROR)
    return out


def _json_body(schema, example=None, required=True, desc=None):
    media = {"schema": schema}
    if example is not None:
        media["example"] = example
    body = {"required": required, "content": {"application/json": media}}
    if desc:
        body["description"] = desc
    return body


def build_spec(mcp_path="/mcp", auth_required=False, vault=None, version="1.2.0",
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
            {"name": "taxonomy", "description": "The domain declarations in vault/taxonomy.md — what "
                                                "every page's `domain:` is validated against."},
            {"name": "scrape", "description": "Web harvest — ONLINE MODE ONLY."},
            {"name": "meta", "description": "Health and machine-readable description."},
        ],
        "paths": {},
    }

    spec["paths"]["/health"] = {
        "get": {
            "tags": ["meta"], "operationId": "getHealth",
            "summary": "Liveness + corpus fingerprint",
            "description": ("Intentionally UNAUTHENTICATED even when a bearer token is configured, so "
                            "kubelet-style probes (which cannot attach custom headers) still work. "
                            "Returns the declared domains and total page count — useful for confirming "
                            "a bind-mounted vault actually landed.\n\n"
                            "`capabilities` is what the MODE permits; `uploads`/`auto_ingest` are what "
                            "THIS process switched on. They are reported separately so 'wrong mode' and "
                            "'forgot --allow-upload' are distinguishable.\n\n"
                            "Takes no input."),
            "security": [],
            "responses": {"200": _json_response("Server is up.", {
                "type": "object",
                "required": ["status", "mode", "capabilities", "domains", "pages"],
                "properties": {
                    "status": {"type": "string", "const": "ok"},
                    "mode": {"type": "string", "enum": list(modes.MODES),
                             "description": "the live WIKIKB_MODE"},
                    "capabilities": {"type": "object", "description": "what the MODE permits",
                                     "properties": {
                                         "vault": {"type": "boolean"}, "mcp": {"type": "boolean"},
                                         "ingest": {"type": "boolean"},
                                         "scrape": {"type": "boolean",
                                                    "description": "true only in online mode"}}},
                    "uploads": {"type": "boolean",
                                "description": "PUT /upload enabled on this process (--allow-upload)"},
                    "auto_ingest": {"type": "boolean",
                                    "description": "an upload also queues the conversion chain"},
                    "domains": {"type": "array", "items": {"type": "string"},
                                "description": "domains declared in vault/taxonomy.md"},
                    "pages": {"type": "integer", "description": "synthesis pages discovered in the vault"},
                },
            }, example={
                "status": "ok", "mode": "airgapped",
                "capabilities": {"vault": True, "mcp": True, "ingest": True, "scrape": False},
                "uploads": False, "auto_ingest": False,
                "domains": ["active-directory", "cisco-ios-xe", "keycloak", "openshift"],
                "pages": 214,
            })},
        }
    }

    spec["paths"]["/route"] = {
        "get": {
            "tags": ["retrieval"], "operationId": "getRoute",
            "summary": "Route a question to its domain(s)",
            "description": ("Keyword match against each domain's `areas:` vocabulary. Conservative by "
                            "design: `confident: true` is never wrong, so a confident route lets a "
                            "client skip the cross-domain index entirely. `confident: false` means "
                            "the router abstained — disambiguate before searching."),
            "parameters": [_q("q", "The natural-language question.", True, example="keycloak ldap federation")],
            "responses": {
                "200": _json_response("Routing decision.", {
                    "type": "object",
                    "required": ["domains", "confident"],
                    "properties": {
                        "domains": {"type": "array", "items": {"type": "string"},
                                    "description": "candidate domains, best first; [] when nothing matched"},
                        "confident": {"type": "boolean",
                                      "description": "true ⇒ a single-domain route the client may trust "
                                                     "outright; false ⇒ the router abstained"},
                    },
                }, example={"domains": ["keycloak"], "confident": True}),
                **_errors((400, "Missing `q`.")),
            },
        }
    }

    spec["paths"]["/search"] = {
        "get": {
            "tags": ["retrieval"], "operationId": "getSearch",
            "summary": "Lexical search over a domain's reference tier",
            "description": ("Ranks the immutable reference notes (`vault/reference/<domain>/`) with the "
                            "SAME `kb.lexical_rank` the CLI and the eval harness use — corpus IDF, "
                            "average-length normalisation and alias expansion included — so this "
                            "endpoint cannot disagree with `python3 -m wikikb kb search`.\n\n"
                            "Returns a bare JSON ARRAY, not an envelope."),
            "parameters": [
                _q("domain", "Domain slug, e.g. `keycloak`. Must be declared in the vault taxonomy.",
                   True, example="keycloak"),
                _q("q", "Search terms.", True, example="jdbc-ping"),
                _q("k", "Max hits.", False, {"type": "integer", "default": 5, "minimum": 1}),
            ],
            "responses": {
                "200": _json_response("Ranked hits, best first.", {
                    "type": "array",
                    "items": {"type": "object", "properties": {
                        "id": {"type": "string", "description": "reference-note id — the `kb:` token to cite"},
                        "title": {"type": "string"},
                        "score": {"type": "number", "description": "lexical rank score (not normalised)"},
                        "snippet": {"type": "string",
                                    "description": "term-centred excerpt, or the note's abstract when "
                                                   "the body is absent"},
                    }},
                }, example=[
                    {"id": "kc-cluster-jdbc-ping-26-6", "title": "Configuring distributed caches",
                     "score": 18.42,
                     "snippet": "…use the `jdbc-ping` stack for discovery when multicast is unavailable…"},
                ]),
                **_errors((400, "Missing `domain` or `q`."),
                          (404, "No reference tier for that domain (see GET /health for the list).")),
            },
        }
    }

    spec["paths"]["/ask"] = {
        "get": {
            "tags": ["answers"], "operationId": "getAsk",
            "summary": "Gated, cited answer",
            "description": ("Runs retrieval → graph expansion → synthesis → the Confidence gate, and "
                            "returns the SAME serialized shape as `wikikb ask --json` and the "
                            "`wiki_ask` MCP tool (one serializer, no per-surface drift).\n\n"
                            "Read the structured fields, not the prose: `banner` (the fired "
                            "Confidence-gate arms), `grounding_fail` / `ungrounded_identifiers` "
                            "(always present, never omitted), `cited` (the reference notes the answer "
                            "actually rests on) and `reference_groups` (the two-group RH/Wiki "
                            "citation contract).\n\n"
                            "With `strict=true` an ungrounded answer is WITHHELD — `withheld: true` "
                            "and `answer` replaced by a deterministic line — rather than served with a "
                            "warning. Prefer strict for unattended/automated callers."),
            "parameters": [
                _q("q", "The question.", True, example="how do I configure jdbc-ping discovery?"),
                _q("domain", "Restrict to one domain. Omitted ⇒ the router decides.", False, example="keycloak"),
                _q("k", "Retrieval depth (lexical candidates).", False,
                   {"type": "integer", "default": 5, "minimum": 1}),
                _q("tier", "Question tier for the gate's H1 coverage arm.",
                   False, {"type": "string", "enum": ["conceptual", "support-kb", "scenarios"]}),
                _q("strict", "Withhold instead of flagging when grounding fails. Absent ⇒ the "
                             "WIKI_STRICT_GROUNDING env default decides; an explicit `0` overrides it.",
                   False, {"type": "boolean", "default": False}),
            ],
            "responses": {
                "200": _json_response("Answer plus its grounding/provenance envelope.", {
                    "type": "object",
                    "required": ["query", "domain", "answer", "banner", "cited", "grounding_fail",
                                 "ungrounded_identifiers", "withheld", "references", "reference_groups"],
                    "properties": {
                        "query": {"type": "string", "description": "echoed back verbatim"},
                        "orchestrator": {"type": "string", "enum": ["langgraph", "linear"],
                                         "description": "which path ran; `linear` = langgraph absent"},
                        "domain": {"type": ["string", "null"], "description": "the domain answered from"},
                        "confident": {"type": "boolean", "description": "was the route confident"},
                        "thin": {"type": "boolean",
                                 "description": "true when retrieval found little to stand on"},
                        "banner": {"type": "array", "items": {"type": "string"},
                                   "description": "Confidence-gate banners that fired (H1/H2/H3/H4/"
                                                  "Provisional); [] when none did. Already prefixed "
                                                  "onto `answer` too."},
                        "guard": {"type": "array", "items": {"type": "string"},
                                  "description": "guard notes raised during synthesis"},
                        "answer": {"type": "string",
                                   "description": "Markdown prose, banner-prefixed, ending with the "
                                                  "canonical two-group References section"},
                        "cited": {"type": "array", "items": {"type": "string"},
                                  "description": "reference-note ids the synthesis actually used"},
                        "grounding_fail": {"type": "boolean",
                                           "description": "the answer could not be grounded in its cited notes"},
                        "ungrounded_identifiers": {"type": "array", "items": {"type": "string"},
                                                   "description": "distinctive identifiers asserted but "
                                                                  "absent from every cited note — the "
                                                                  "fabricated-citation tripwire. Always "
                                                                  "a list."},
                        "grounding_basis": {"type": ["string", "null"],
                                            "description": "what the grounding check was computed over"},
                        "premise_flags": {"type": "array", "description": "false-premise findings; always a list",
                                          "items": {"type": "object", "properties": {
                                              "flag": {"type": "string",
                                                       "example": "premise_unaddressed"},
                                              "detail": {"type": "string"}}}},
                        "withheld": {"type": "boolean",
                                     "description": "true when strict mode suppressed the prose"},
                        "references": {"type": "array", "description": "resolved cited notes",
                                       "items": {"type": "object", "properties": {
                                           "id": {"type": "string"},
                                           "source": {"type": "string",
                                                      "description": "the note's `source:`/`url:` frontmatter"}}}},
                        "reference_groups": {
                            "type": "object",
                            "description": "the two-group citation contract, machine-readable",
                            "properties": {
                                "rh_ground_truth": {"type": "array", "items": {"type": "object", "properties": {
                                    "token": {"type": "string", "example": "ref:kc-cluster-jdbc-ping-26-6"},
                                    "id": {"type": "string"}, "source": {"type": "string"}}}},
                                "wiki": {"type": "array", "items": {"type": "object", "properties": {
                                    "slug": {"type": "string"},
                                    "wikilink": {"type": "string", "example": "[[jdbc-ping]]"}}}}}},
                        "judge_verdict": {"type": ["object", "null"],
                                          "description": "present ONLY when the advisory judge ran"},
                    },
                }, example={
                    "query": "how do I configure jdbc-ping discovery?",
                    "orchestrator": "langgraph", "domain": "keycloak", "confident": True, "thin": False,
                    "banner": [], "guard": [],
                    "answer": "**jdbc-ping** discovers cluster members through the database …\n\n"
                              "## References (canonical)\n\n### RH ground-truth\n"
                              "- `ref:kc-cluster-jdbc-ping-26-6` — Configuring distributed caches\n\n"
                              "### Wiki\n- [[jdbc-ping]]",
                    "cited": ["kc-cluster-jdbc-ping-26-6"],
                    "grounding_fail": False, "ungrounded_identifiers": [],
                    "grounding_basis": "cited-notes", "premise_flags": [], "withheld": False,
                    "references": [{"id": "kc-cluster-jdbc-ping-26-6",
                                    "source": "Configuring distributed caches"}],
                    "reference_groups": {
                        "rh_ground_truth": [{"token": "ref:kc-cluster-jdbc-ping-26-6",
                                             "id": "kc-cluster-jdbc-ping-26-6",
                                             "source": "Configuring distributed caches"}],
                        "wiki": [{"slug": "jdbc-ping", "wikilink": "[[jdbc-ping]]"}]},
                }),
                **_errors((400, "Missing `q`.")),
            },
        }
    }

    spec["paths"]["/expand"] = {
        "get": {
            "tags": ["retrieval"], "operationId": "getExpand",
            "summary": "1-hop graph neighbourhood for a query",
            "description": ("Returns the reference notes cited by the query's seed pages and by their "
                            "immediate `[[wikilink]]` neighbours — WITHOUT running a second search. "
                            "This is the multi-hop entry point: a paraphrased query that lexical "
                            "ranks deep often still matches a page that CITES the right note.\n\n"
                            "`previews` carries a snippet per note so triage costs no full-body read."),
            "parameters": [
                _q("domain", "Domain slug.", True, example="keycloak"),
                _q("q", "The query.", True, example="cluster discovery in air-gapped kubernetes"),
            ],
            "responses": {
                "200": _json_response("Cited-note neighbourhood.", {
                    "type": "object",
                    "required": ["notes", "previews"],
                    "properties": {
                        "notes": {"type": "array", "items": {"type": "string"},
                                  "description": "reference-note ids, sorted"},
                        "previews": {"type": "array", "description": "one entry per id, same order",
                                     "items": {"type": "object", "properties": {
                                         "id": {"type": "string"},
                                         "snippet": {"type": "string",
                                                     "description": "term-centred excerpt; \"\" when the "
                                                                    "note carries no body"}}}},
                    },
                }, example={
                    "notes": ["kc-cluster-jdbc-ping-26-6", "kc-operator-cache-26-6"],
                    "previews": [
                        {"id": "kc-cluster-jdbc-ping-26-6",
                         "snippet": "…`jdbc-ping` needs no multicast, which is why it is the air-gapped default…"},
                        {"id": "kc-operator-cache-26-6", "snippet": "…cache configuration in the Operator…"}],
                }),
                **_errors((400, "Missing `domain` or `q`.")),
            },
        }
    }

    spec["paths"]["/page/{slug}"] = {
        "get": {
            "tags": ["retrieval"], "operationId": "getPage",
            "summary": "Read one synthesis page",
            "description": ("Bodies are served in bounded slices (8000 chars max, cut back to a whole "
                            "line so a slice never ends mid-table-row); when more remains the response "
                            "carries `truncated: true` and `next_offset` — feed it back as `offset` to "
                            "page through rather than demanding the file whole."),
            "parameters": [
                _path_param("slug", "Kebab-case page slug. Anything else fails the shape check before a "
                                    "filesystem path is built — which is what makes this traversal-safe.",
                            example="jdbc-ping"),
                _q("offset", "Character offset into the body.", False,
                   {"type": "integer", "default": 0, "minimum": 0}),
                _q("max_chars", "Max characters in this slice (capped at 8000).", False,
                   {"type": "integer", "minimum": 1, "maximum": 8000}),
            ],
            "responses": {
                "200": _json_response("The page (or one slice of it).", {
                    "type": "object",
                    "required": ["slug", "path", "frontmatter", "body", "body_total_chars"],
                    "properties": {
                        "slug": {"type": "string"},
                        "path": {"type": "string", "description": "vault-relative, e.g. `entities/jdbc-ping.md`"},
                        "frontmatter": {"type": "object", "additionalProperties": {"type": "string"},
                                        "description": "top-level scalar frontmatter keys (title, domain, "
                                                       "summary, status, updated, provenance_*, …)"},
                        "body": {"type": "string", "description": "this slice of the Markdown body"},
                        "body_total_chars": {"type": "integer", "description": "full body length"},
                        "truncated": {"type": "boolean", "description": "present only when more remains"},
                        "next_offset": {"type": "integer",
                                        "description": "present only when truncated — pass as `offset`"},
                    },
                }, example={
                    "slug": "jdbc-ping", "path": "entities/jdbc-ping.md",
                    "frontmatter": {"title": "jdbc-ping", "type": "entity", "domain": "keycloak",
                                    "status": "reviewed", "updated": "2026-06-16"},
                    "body": "# jdbc-ping\n\n**Database-backed JGroups discovery.**\n…",
                    "body_total_chars": 3182,
                }),
                **_errors((400, "Malformed slug."), (404, "No such page.")),
            },
        }
    }

    spec["paths"]["/upload/{domain}/{filename}"] = {
        "put": {
            "tags": ["ingest"], "operationId": "putUpload",
            "summary": "Upload a PDF into the raw tier (opt-in)",
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
                _path_param("domain", "Target domain; must be declared in vault/taxonomy.md.",
                            example="keycloak"),
                _path_param("filename", "Destination filename. Must end in `.pdf`.",
                            pattern=r"^[A-Za-z0-9][A-Za-z0-9._-]*\.pdf$", example="server-guide.pdf"),
            ],
            "requestBody": {
                "required": True,
                "description": "The raw PDF bytes (max 50 MB; the %PDF magic bytes are checked).",
                "content": {"application/pdf": {"schema": {"type": "string", "format": "binary"}}},
            },
            "responses": {
                "201": _json_response("Stored (and, unless auto-ingest is off, conversion queued).", {
                    "type": "object",
                    "required": ["stored", "ingest"],
                    "properties": {
                        "stored": {"type": "string", "description": "path relative to the vault root"},
                        "ingest": {"type": "string",
                                   "description": "queued | coalesced into pending job | disabled | not queued"},
                        "job_id": {"type": "string", "description": "present when a job was queued"},
                        "status_url": {"type": "string", "example": "/jobs/9f2c1a0b4d7e"},
                        "next": {"type": "string", "description": "what to do next, in words"}},
                }, example={
                    "stored": "_sources/keycloak/_raw/pdfs/server-guide.pdf",
                    "ingest": "queued", "job_id": "9f2c1a0b4d7e", "status_url": "/jobs/9f2c1a0b4d7e",
                    "next": "poll GET /jobs/9f2c1a0b4d7e until state=done",
                }),
                **_errors(
                    (404, "Uploads disabled, or path shape not matched (deliberately indistinguishable)."),
                    (400, "Unknown domain, bad Content-Length, or a short read."),
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
            "tags": ["ingest"], "operationId": "postIngest",
            "summary": "Queue the conversion chain for a domain (opt-in)",
            "description": (
                "Runs the same three steps an upload queues — `pdf_to_corpus --append` → "
                "`corpus_to_vault` → `build` — over everything currently in "
                "`vault/_sources/{domain}/_raw/pdfs/`. Use it to batch several drops into one "
                "`build`, or to retry after a failed job.\n\n"
                "Gated by the SAME `--allow-upload` opt-in as `/upload`: it writes to the vault, so "
                "it is part of the one write surface, not a second one that could stay open after "
                "uploads were deliberately disabled. Disabled ⇒ indistinguishable from an unknown path.\n\n"
                "Takes no request body. A submission for a domain that already has a QUEUED job "
                "returns that job (`coalesced: true`) instead of a duplicate — the chain reads the "
                "whole directory, so the pending job will see the new files anyway."),
            "parameters": [_path_param("domain", "Domain to ingest; must be declared in vault/taxonomy.md.",
                                       example="keycloak")],
            "responses": {
                "202": _json_response("Job queued.", {
                    "type": "object",
                    "required": ["job_id", "status_url", "state", "coalesced", "steps"],
                    "properties": {"job_id": {"type": "string"},
                                   "status_url": {"type": "string", "example": "/jobs/9f2c1a0b4d7e"},
                                   "state": {"type": "string", "enum": ["queued", "running"]},
                                   "coalesced": {"type": "boolean",
                                                 "description": "true ⇒ this returned an ALREADY-pending "
                                                                "job rather than queueing a second one"},
                                   "steps": {"type": "array", "items": {"type": "string"},
                                             "description": "the chain, in order"}},
                }, example={"job_id": "9f2c1a0b4d7e", "status_url": "/jobs/9f2c1a0b4d7e",
                            "state": "queued", "coalesced": False,
                            "steps": ["pdf_to_corpus", "corpus_to_vault", "build"]}),
                **_errors((400, "Domain not declared in the vault taxonomy."),
                          (404, "Write surface disabled (indistinguishable from an unknown path)."),
                          (429, "Job queue full — retry once the backlog drains.")),
            },
        }
    }

    _JOB = {
        "type": "object",
        "required": ["id", "kind", "state", "created", "steps", "results"],
        "properties": {
            "id": {"type": "string", "description": "12 hex chars"},
            "kind": {"type": "string", "enum": ["ingest", "scrape"]},
            "state": {"type": "string", "enum": ["queued", "running", "done", "failed"]},
            "domain": {"type": "string", "description": "present when the job is domain-scoped"},
            "detail": {"type": "object", "additionalProperties": True,
                       "description": "what triggered it (and, for a scrape, the URLs)"},
            "created": {"type": "number", "description": "unix epoch seconds"},
            "started": {"type": ["number", "null"]},
            "finished": {"type": ["number", "null"]},
            "steps": {"type": "array", "items": {"type": "string"},
                      "description": "step names in execution order"},
            "current_step": {"type": ["string", "null"],
                             "description": "present only while queued/running"},
            "results": {"type": "array", "description": "one entry per COMPLETED step",
                        "items": {"type": "object", "properties": {
                            "step": {"type": "string"}, "exit": {"type": "integer"},
                            "seconds": {"type": "number"},
                            "log": {"type": "array", "items": {"type": "string"},
                                    "description": "tail of the step's combined output, capped"}}}},
            "error": {"type": "string", "description": "present only on `failed`"},
        },
    }
    _JOB_EXAMPLE = {
        "id": "9f2c1a0b4d7e", "kind": "ingest", "state": "done", "domain": "keycloak",
        "detail": {"trigger": "PUT /upload"},
        "created": 1786100000.4, "started": 1786100000.6, "finished": 1786100061.2,
        "steps": ["pdf_to_corpus", "corpus_to_vault", "build"],
        "results": [
            {"step": "pdf_to_corpus", "exit": 0, "seconds": 4.1, "log": ["1 PDF appended"]},
            {"step": "corpus_to_vault", "exit": 0, "seconds": 2.7, "log": ["wrote 1 reference note"]},
            {"step": "build", "exit": 0, "seconds": 53.8, "log": ["lint: 0 errors"]},
        ],
    }

    spec["paths"]["/jobs"] = {
        "get": {
            "tags": ["jobs"], "operationId": "getJobs",
            "summary": "Recent jobs (newest first)",
            "description": ("Job state is IN-MEMORY and lost on restart: it is progress reporting, not "
                            "provenance. The durable record of what was ingested is the vault plus "
                            "`.manifest.json`.\n\nTakes no input."),
            "responses": {"200": _json_response("Recent jobs plus runner stats.", {
                "type": "object",
                "required": ["jobs", "stats"],
                "properties": {"jobs": {"type": "array", "items": _JOB},
                               "stats": {"type": "object", "properties": {
                                   "pending": {"type": "integer", "description": "queued, not yet started"},
                                   "retained": {"type": "integer",
                                                "description": "records held in memory (oldest finished "
                                                               "ones are evicted)"},
                                   "worker": {"type": "boolean", "description": "the single worker is alive"}}}},
            }, example={"jobs": [_JOB_EXAMPLE],
                        "stats": {"pending": 0, "retained": 1, "worker": True}})},
        }
    }

    spec["paths"]["/jobs/{id}"] = {
        "get": {
            "tags": ["jobs"], "operationId": "getJob",
            "summary": "One job's state and step log",
            "description": ("Steps run in order and STOP at the first failure — continuing past a "
                            "failed extraction would fold a stale corpus into the reference tier. On "
                            "`failed`, the last entry in `results` carries the exit code and the tail "
                            "of that step's output."),
            "parameters": [{"name": "id", "in": "path", "required": True,
                            "description": "The 12-hex-char job id returned by /upload, /ingest or /scrape.",
                            "schema": {"type": "string", "pattern": "^[0-9a-f]{12}$"},
                            "example": "9f2c1a0b4d7e"}],
            "responses": {"200": _json_response("The job.", _JOB, example=_JOB_EXAMPLE),
                          **_errors((400, "Malformed job id."),
                                    (404, "No such job, or its record has been evicted."))},
        }
    }

    # --- the domain declarations (BOTH modes) ---------------------------------------------------
    # Emitted unconditionally, unlike the scrape block below: editing the vault's own taxonomy opens
    # no socket, so an airgapped instance serves this surface too and a spec that hid it would lie
    # in the other direction.
    spec.setdefault("components", {}).setdefault("schemas", {})["Domain"] = {
        "type": "object", "required": ["domain", "areas", "shape", "sources", "tiers-covered"],
        "description": "One `### <name>` block under `## Domains` in vault/taxonomy.md.",
        "properties": {
            "domain": {"type": "string", "pattern": "^[a-z][a-z0-9-]+$",
                       "description": "kebab-case, 2+ chars. This is the value every page's "
                                      "`domain:` frontmatter must equal, the name of the immutable "
                                      "`reference/<domain>/` tier, and the `index.<domain>.md` "
                                      "stem — i.e. the domain's IDENTITY. Not patchable."},
            "areas": {"type": "array", "items": {"type": "string"},
                      "description": "Subset of the flat `## Areas` union (GET /domains returns it). "
                                     "These ARE the router's vocabulary: the area slug plus the "
                                     "words of its description become this domain's keyword profile."},
            "shape": {"type": "string", "enum": ["notes-first", "corpus-backed"],
                      "description": "notes-first = you hand-author the raw tier under "
                                     "`_sources/<domain>/`; corpus-backed = a harvested doc corpus "
                                     "is folded in as immutable `reference/<domain>/` notes."},
            "sources": {"type": "array", "items": {"type": "string"},
                        "description": "Raw-tier paths this domain reads. Defaulted from `shape`."},
            "review-moc": {"type": "string",
                           "description": "Slug of the domain's evaluation-lens Map of Content "
                                          "(symptom → likely-cause). Defaults to "
                                          "`<domain>-implementation-review`."},
            "tiers-covered": {"type": "array",
                              "items": {"type": "string",
                                        "enum": ["conceptual", "support-kb", "scenarios"]},
                              "description": "The coarse knowledge tiers ACTUALLY ingested. This "
                                             "drives the Confidence gate's H1 arm: a question whose "
                                             "tier is not covered gets an out-of-coverage banner "
                                             "instead of a confident answer. Declaring a tier you "
                                             "have not ingested silently disables that protection."},
            "comments": {"type": "object", "additionalProperties": {"type": "string"},
                         "description": "Trailing `# …` notes preserved from the file, keyed by "
                                        "field — usually the reason a coverage tier is what it is."},
            "header_mismatch": {"type": "string",
                                "description": "Present only on a hand-edited block whose `### "
                                               "heading` disagrees with its `- domain:` line — a "
                                               "domain lint can see but the gate cannot."}}}
    _DOMAIN_EXAMPLE = {"domain": "checkpoint",
                       "areas": ["cp-gateway", "cp-management", "cp-policy", "security"],
                       "shape": "notes-first", "sources": ["_sources/checkpoint/"],
                       "review-moc": "checkpoint-implementation-review",
                       "tiers-covered": ["conceptual"]}
    _domain_write_note = (
        "Part of the **write surface**, so it shares `--allow-upload` (`WIKIKB_ALLOW_UPLOAD=1`) with "
        "`/upload` and `/ingest`: declaring a domain decides what a later upload is allowed to write "
        "into the vault. With uploads off it answers the same unfingerprintable 404, not a 403.\n\n"
        "Served in **both** operation modes — a taxonomy edit opens no socket.")

    spec["paths"]["/domains"] = {
        "get": {
            "tags": ["taxonomy"], "operationId": "listDomains",
            "summary": "List the declared domains",
            "description": (
                "Every `### <name>` block in `vault/taxonomy.md`, plus the flat `## Areas` "
                "vocabulary and the legal `shape`/`tiers-covered` values — everything needed to "
                "compose a POST, so discovering the legal values costs no second round trip.\n\n"
                "A **read**: open even when the write surface is disabled. Takes no input."),
            "responses": {"200": _json_response("The declarations.", {
                "type": "object",
                "properties": {
                    "domains": {"type": "array", "items": {"$ref": "#/components/schemas/Domain"}},
                    "count": {"type": "integer"},
                    "areas": {"type": "object", "additionalProperties": {"type": "string"},
                              "description": "the flat union: area slug -> its description"},
                    "shapes": {"type": "array", "items": {"type": "string"}},
                    "tiers": {"type": "array", "items": {"type": "string"}},
                    "file": {"type": "string", "description": "resolved path of taxonomy.md"}}},
                example={"domains": [_DOMAIN_EXAMPLE], "count": 1,
                         "areas": {"cp-gateway": "Security Gateway: inspection, blades, NAT"},
                         "shapes": ["notes-first", "corpus-backed"],
                         "tiers": ["conceptual", "support-kb", "scenarios"],
                         "file": "/data/vault/taxonomy.md"})},
        },
        "post": {
            "tags": ["taxonomy"], "operationId": "addDomain",
            "summary": "Declare a new domain",
            "description": (
                f"{_domain_write_note}\n\n"
                "This is **ADD-DOMAIN steps 2–4** in one call: it writes the `### <name>` block, "
                "appends any `new_areas` to the flat `## Areas` union first, and creates the raw "
                "tier `vault/_sources/<name>/` (with a README) that uploads and scrapes land in.\n\n"
                "It deliberately stops there. It writes **no pages** — seeding the synthesis (the "
                "overview topic, its first entity, the review MOC) is an authored act under the "
                "citation contract — and **no index**, which is `wikikb index`'s output. The "
                "response's `next` says exactly what is left.\n\n"
                "`areas` must be a subset of the existing vocabulary; an unknown one is **refused, "
                "not invented**, because an area with no description contributes nothing to the "
                "router and is indistinguishable from a typo of a real one. Send genuinely new "
                "areas as `new_areas` **with a description**.\n\n"
                "Defaults: `shape` = `notes-first`, `sources` from the shape, `review-moc` = "
                "`<name>-implementation-review`, `tiers-covered` = `[conceptual]`."),
            "requestBody": _json_body({
                "type": "object", "required": ["domain", "areas"],
                "properties": {
                    "domain": {"type": "string", "pattern": "^[a-z][a-z0-9-]+$"},
                    "areas": {"type": "array", "items": {"type": "string"}},
                    "shape": {"type": "string", "enum": ["notes-first", "corpus-backed"],
                              "default": "notes-first"},
                    "sources": {"type": "array", "items": {"type": "string"}},
                    "review-moc": {"type": "string"},
                    "tiers-covered": {"type": "array", "items": {"type": "string"},
                                      "default": ["conceptual"]},
                    "new_areas": {"type": "object", "additionalProperties": {"type": "string"},
                                  "description": "area slug -> description; appended to `## Areas` "
                                                 "BEFORE the domain block that references them"}}},
                example={"domain": "nginx", "areas": ["web-serving", "security", "troubleshooting"],
                         "shape": "notes-first", "tiers-covered": ["conceptual"],
                         "new_areas": {"web-serving": "reverse proxy, virtual hosts, TLS "
                                                      "termination, upstreams, rate limiting"}}),
            "responses": {
                "201": _json_response("Declared.", {
                    "type": "object",
                    "properties": {"added": {"$ref": "#/components/schemas/Domain"},
                                   "file": {"type": "string"},
                                   "next": {"type": "string",
                                            "description": "the ADD-DOMAIN steps this call did NOT do"}}},
                    example={"added": dict(_DOMAIN_EXAMPLE, created=["_sources/checkpoint",
                                                                     "_sources/checkpoint/README.md"]),
                             "file": "/data/vault/taxonomy.md",
                             "next": "write the overview topic, its first entity and "
                                     "checkpoint-implementation-review, then run "
                                     "`python3 -m wikikb build`"}),
                **_errors((400, "Missing/invalid areas, an unknown area or tier, a bad shape, or a "
                                "name that is not kebab-case 2+ chars."),
                          (404, "The write surface is disabled (indistinguishable from an unknown path)."),
                          (409, "That domain is already declared — PATCH it instead.")),
            },
        },
    }

    spec["paths"]["/domains/{domain}"] = {
        "get": {
            "tags": ["taxonomy"], "operationId": "getDomain",
            "summary": "One declaration + what depends on it",
            "description": (
                "The block as stored, plus a `usage` block: how many synthesis pages declare this "
                "domain, how many immutable reference/source notes it owns, and how many scrape "
                "sources target it.\n\n"
                "`usage` is on the plain GET, not only on a refused DELETE, because the blast radius "
                "of undeclaring a domain is what you want *before* deciding, not after."),
            "parameters": [_path_param("domain", "The declared domain name.", example="keycloak")],
            "responses": {
                "200": _json_response("The declaration.", {
                    "allOf": [{"$ref": "#/components/schemas/Domain"},
                              {"type": "object", "properties": {
                                  "usage": {"type": "object", "properties": {
                                      "pages": {"type": "integer"},
                                      "page_slugs": {"type": "array", "items": {"type": "string"},
                                                     "description": "first 20, sorted"},
                                      "reference_notes": {"type": "integer"},
                                      "source_notes": {"type": "integer"},
                                      "scrape_sources": {"type": "integer"},
                                      "index": {"type": "string"}}},
                                  "file": {"type": "string"}}}]},
                    example=dict(_DOMAIN_EXAMPLE,
                                 usage={"pages": 3, "page_slugs": ["checkpoint-clusterxl-sync"],
                                        "reference_notes": 12, "source_notes": 1,
                                        "scrape_sources": 1,
                                        "index": "/data/vault/index.checkpoint.md"},
                                 file="/data/vault/taxonomy.md")),
                **_errors((404, "No such domain.")),
            },
        },
        "patch": {
            "tags": ["taxonomy"], "operationId": "updateDomain",
            "summary": "Update a declaration (partial)",
            "description": (
                f"{_domain_write_note}\n\n"
                "**Partial.** The path selects; only the fields you send are touched, so widening "
                "coverage is `{\"tiers-covered\":[\"conceptual\",\"support-kb\"]}` and nothing else "
                "moves. Trailing `# …` comments on untouched fields are preserved — several of them "
                "record *why* a domain covers only `conceptual`, and dropping that on an unrelated "
                "patch would delete the justification for a gate decision.\n\n"
                "**The name is NOT patchable.** It is every page's `domain:` frontmatter, the "
                "`reference/<domain>/` directory and the `index.<domain>.md` stem; patching it here "
                "would leave all of them addressed under the old name while the taxonomy claims the "
                "new one. A rename is DELETE + POST plus a deliberate pass over the pages.\n\n"
                "The response carries `changed` — the fields that actually moved. A no-op reports "
                "`changed: []` and does **not** rewrite the file, so the taxonomy's mtime keeps "
                "meaning 'when it last really changed'.\n\n"
                "Widening `tiers-covered` is the one change to make deliberately: it *disables* the "
                "Confidence gate's out-of-coverage banner for that tier, so declare a tier only once "
                "it is genuinely ingested."),
            "parameters": [_path_param("domain", "The domain to patch (selector; not itself patchable).",
                                       example="checkpoint")],
            "requestBody": _json_body({
                "type": "object",
                "properties": {
                    "areas": {"type": "array", "items": {"type": "string"}},
                    "shape": {"type": "string", "enum": ["notes-first", "corpus-backed"]},
                    "sources": {"type": "array", "items": {"type": "string"}},
                    "review-moc": {"type": "string"},
                    "tiers-covered": {"type": "array", "items": {"type": "string"}},
                    "new_areas": {"type": "object", "additionalProperties": {"type": "string"}}}},
                example={"tiers-covered": ["conceptual", "support-kb"]}),
            "responses": {
                "200": _json_response("Updated (or already up to date).", {
                    "type": "object",
                    "properties": {"updated": {"$ref": "#/components/schemas/Domain"},
                                   "changed": {"type": "array", "items": {"type": "string"},
                                               "description": "field names that actually moved; [] = no-op"},
                                   "file": {"type": "string"}, "note": {"type": "string"}}},
                    example={"updated": dict(_DOMAIN_EXAMPLE,
                                             **{"tiers-covered": ["conceptual", "support-kb"]}),
                             "changed": ["tiers-covered"], "file": "/data/vault/taxonomy.md"}),
                **_errors((400, "Nothing to update, an attempt to rename, an unknown field, or an "
                                "invalid area/tier/shape value."),
                          (404, "No such domain — or the write surface is disabled.")),
            },
        },
        "delete": {
            "tags": ["taxonomy"], "operationId": "removeDomain",
            "summary": "Undeclare a domain",
            "description": (
                f"{_domain_write_note}\n\n"
                "**It deletes no knowledge.** The declaration goes, and so does the generated "
                "`index.<domain>.md` (a derived artifact that would otherwise describe a domain "
                "nothing can validate). Every synthesis page and every line of the immutable "
                "`reference/`/`_sources/` tiers is KEPT — withdrawing what a domain knows is "
                "Operation: RETRACT, an explicitly authored act, and doing it as a side effect of a "
                "config edit would destroy ground truth over a typo.\n\n"
                "It answers **409** while pages still declare the domain (or a scrape source still "
                "targets it), because undeclaring it silently makes every one of those pages fail "
                "lint as 'unknown domain' with nothing pointing back here. `?force=true` (or "
                "`{\"force\":true}`) is the operator taking that on."),
            "parameters": [
                _path_param("domain", "The domain to undeclare.", example="checkpoint"),
                _q("force", "Undeclare even while pages still use it.",
                   False, {"type": "boolean", "default": False}),
            ],
            "responses": {
                "200": _json_response("Undeclared.", {
                    "type": "object",
                    "properties": {"removed": {"$ref": "#/components/schemas/Domain"},
                                   "kept": {"type": "array", "items": {"type": "string"},
                                            "description": "immutable tiers left untouched"},
                                   "removed_generated": {"type": "array", "items": {"type": "string"},
                                                         "description": "derived artifacts deleted"},
                                   "file": {"type": "string"}, "note": {"type": "string"}}},
                    example={"removed": _DOMAIN_EXAMPLE,
                             "kept": ["/data/vault/reference/checkpoint",
                                      "/data/vault/_sources/checkpoint"],
                             "removed_generated": ["index.checkpoint.md"],
                             "file": "/data/vault/taxonomy.md",
                             "note": "the immutable reference/ and _sources/ tiers and every page are "
                                     "KEPT — to withdraw what this domain knows, retract the pages"}),
                **_errors((400, "Malformed request."),
                          (404, "No such domain — or the write surface is disabled."),
                          (409, "Still in use: pages declare it (or scrape sources target it). "
                                "Repoint or retract them, or pass ?force=true.")),
            },
        },
    }

    if mode == modes.ONLINE:
        # The watchlist entry shape, shared by the GET listing and the POST body. Emitted only in
        # online mode, alongside the paths that reference it — an airgapped spec must not carry a
        # schema for a surface it does not serve.
        spec.setdefault("components", {}).setdefault("schemas", {})["ScrapeSource"] = {
            "type": "object", "required": ["url", "domain"],
            "properties": {
                "url": {"type": "string", "description": "http(s) only; stored canonicalized "
                                                         "(lowercased host, no fragment)"},
                "domain": {"type": "string", "description": "must be declared in vault/taxonomy.md"},
                "label": {"type": ["string", "null"],
                          "description": "human label used in the web: provenance token"},
                "match": {"type": "string", "enum": ["exact", "prefix"], "default": "exact"},
                "enabled": {"type": "boolean", "default": True},
                "direct": {"type": "boolean", "default": False,
                           "description": "permit a live origin fetch when Common Crawl has no capture"},
                "added": {"type": "string", "format": "date"},
                "state": {"type": "object", "readOnly": True,
                          "description": "harvest PROGRESS for this source (read-only; from the "
                                         "ledger, not the watchlist file)",
                          "properties": {
                              "indexes_done": {"type": "integer",
                                               "description": "crawls already harvested against"},
                              "documents": {"type": "integer"},
                              "last_index": {"type": ["string", "null"]},
                              "last_harvested": {"type": ["string", "null"], "format": "date"}}}}}
        _SOURCE_EXAMPLE = {"url": "https://www.keycloak.org/docs/latest/server_admin/",
                           "domain": "keycloak",
                           "label": "Keycloak Server Administration Guide (upstream)",
                           "match": "exact", "enabled": True, "direct": False, "added": "2026-08-07"}
        _CRON_STATUS = {
            "type": "object",
            "properties": {
                "enabled": {"type": "boolean", "description": "the LIVE flag (runtime override)"},
                "env_default": {"type": "boolean",
                                "description": "what WIKIKB_SCRAPE_CRON_ENABLED booted with — a "
                                               "divergence from `enabled` is deliberate and visible"},
                "schedule": {"type": "string", "description": "raw WIKIKB_SCRAPE_CRON spec",
                             "example": "0 3 * * *"},
                "kind": {"type": "string", "enum": ["cron", "interval", "invalid"]},
                "error": {"type": ["string", "null"], "description": "why a malformed schedule was refused"},
                "running": {"type": "boolean", "description": "the timer thread is alive"},
                "next_run": {"type": ["number", "null"], "description": "unix epoch seconds"},
                "next_run_iso": {"type": ["string", "null"]},
                "last_run": {"type": ["number", "null"]},
                "last_run_iso": {"type": ["string", "null"]},
                "last_result": {"description": "what the last tick queued (or the error it hit)"},
                "runs": {"type": "integer", "description": "ticks since boot"}}}
        _CRON_EXAMPLE = {"enabled": True, "env_default": True, "schedule": "0 3 * * *", "kind": "cron",
                         "error": None, "running": True, "next_run": 1786190400.0,
                         "next_run_iso": "2026-08-08T03:00:00", "last_run": 1786104000.0,
                         "last_run_iso": "2026-08-07T03:00:00",
                         "last_result": {"queued": [{"domain": "keycloak", "job_id": "3b71c0de19aa"}]},
                         "runs": 1}
        _online_note = ("Mounted only when `WIKIKB_MODE=online`; in airgapped mode this path answers "
                        "exactly like an unknown path and is absent from this document.")
        _write_note = ("Part of the **write surface**, so it shares `--allow-upload` "
                       "(`WIKIKB_ALLOW_UPLOAD=1`) with `/upload` and `/ingest` — with uploads off it "
                       "answers the same unfingerprintable 404, not a 403.")
        spec["paths"]["/scrape"] = {
            "post": {
                "tags": ["scrape"], "operationId": "postScrape",
                "summary": "Harvest now (ONLINE MODE ONLY)",
                "description": (
                    f"{_online_note}\n\n{_write_note}\n\n"
                    "Two body shapes:\n\n"
                    "* `{}` (or no body) — harvest **every enabled watchlist source**, as one job "
                    "per domain.\n"
                    "* `{\"url\": …, \"domain\": …}` — harvest **one URL, which need not be on the "
                    "watchlist**. `urls: [...]` takes several.\n\n"
                    "**A watchlist run walks the crawl HISTORY, not just the newest index.** Common "
                    "Crawl samples the web rather than exhaustively recrawling it, so which pages of "
                    "a site appear varies enormously per crawl — measured on `support.checkpoint.com`, "
                    "3 of 4 pages appear in only the newest crawl, and four crawls yielded 81 "
                    "documents where one yielded 21. Each source is therefore harvested against every "
                    "crawl it has not been processed against yet, newest first, and the results "
                    "accumulate.\n\n"
                    "A **ledger** in `vault/.scrape-state.json` records every (source, crawl) pair — "
                    "including crawls that held nothing, since a published crawl is immutable and "
                    "will never hold anything later. So the first runs walk the history and every "
                    "later run touches only the crawls published since (about one a month). Each run "
                    "is bounded by `max_indexes` (default `WIKIKB_SCRAPE_MAX_INDEXES_PER_RUN`, 12) so "
                    "it finishes inside the job step timeout; the ledger makes the next run resume.\n\n"
                    "Each URL found in a crawl has its archived WARC record range-fetched, extracted "
                    "to Markdown and written to `vault/_sources/{domain}/_raw/web/`. An older capture "
                    "never overwrites a newer note. When a URL is **not** in a crawl the run reports "
                    "`not-indexed` and fetches nothing — unless `direct: true`, the opt-in live fetch "
                    "(which refuses any host resolving to a non-public address).\n\n"
                    "Queued on the SAME serialized runner as `/ingest`, never run inline: the chain "
                    "is `scrape → web_to_corpus → corpus_to_vault → build`, i.e. minutes of work, "
                    "and two concurrent `build`s would interleave writes to the generated artifacts. "
                    "Poll each returned `job_id` at `/jobs/{id}`."),
                "requestBody": _json_body({
                    "type": "object",
                    "properties": {
                        "url": {"type": "string", "description": "one URL to harvest"},
                        "urls": {"type": "array", "items": {"type": "string"},
                                 "description": "several URLs, all into the same domain"},
                        "domain": {"type": "string", "description": "REQUIRED with url/urls"},
                        "match": {"type": "string", "enum": ["exact", "prefix"], "default": "exact",
                                  "description": "prefix harvests every indexed page under the URL, "
                                                 "up to WIKIKB_SCRAPE_PREFIX_LIMIT"},
                        "direct": {"type": "boolean", "default": False,
                                   "description": "permit a live origin fetch when Common Crawl has "
                                                  "no capture"},
                        "max_indexes": {"type": "integer",
                                        "description": "cap how many not-yet-harvested crawls this "
                                                       "run walks (watchlist runs only; default "
                                                       "WIKIKB_SCRAPE_MAX_INDEXES_PER_RUN=12). The "
                                                       "ledger makes the next run continue where "
                                                       "this one stopped."}},
                }, example={"url": "https://www.keycloak.org/docs/latest/server_admin/",
                            "domain": "keycloak"},
                    required=False,
                    desc="Omit entirely (or send `{}`) to harvest the whole watchlist."),
                "responses": {
                    "202": _json_response("Queued — one job per domain.", {
                        "type": "object", "required": ["queued"],
                        "properties": {
                            "queued": {"type": "array", "items": {"type": "object", "properties": {
                                "domain": {"type": "string"}, "job_id": {"type": "string"},
                                "coalesced": {"type": "boolean"},
                                "status_url": {"type": "string"},
                                "error": {"type": "string",
                                          "description": "present instead of job_id when THIS domain "
                                                         "could not be queued"}}}},
                            "urls": {"type": "array", "items": {"type": "string"},
                                     "description": "canonicalized URLs (single/multi-URL form only)"},
                            "steps": {"type": "array", "items": {"type": "string"}}}},
                        example={"queued": [{"domain": "keycloak", "job_id": "3b71c0de19aa",
                                             "coalesced": False, "status_url": "/jobs/3b71c0de19aa"}],
                                 "urls": ["https://www.keycloak.org/docs/latest/server_admin/"],
                                 "steps": ["scrape", "web_to_corpus", "corpus_to_vault", "build"]}),
                    "200": _json_response("Nothing to do — the watchlist is empty (not an error).", {
                        "type": "object",
                        "properties": {"queued": {"type": "array", "items": {"type": "object"}},
                                       "note": {"type": "string"}, "file": {"type": "string"}}},
                        example={"queued": [],
                                 "note": "watchlist is empty — add one with POST /scrape/sources",
                                 "file": "/data/vault/scrape-sources.json"}),
                    **_errors((400, "Unknown domain, bad URL, bad match, or invalid JSON body."),
                              (404, "Uploads are disabled, or this instance is airgapped."),
                              (429, "Job queue full."))},
            }
        }
        spec["paths"]["/scrape/sources"] = {
            "get": {"tags": ["scrape"], "operationId": "getScrapeSources",
                    "summary": "The scrape watchlist (ONLINE MODE ONLY)",
                    "description": (f"{_online_note}\n\nThe configured websites (`vault/scrape-"
                                    "sources.json`), which HTML extractor this instance would "
                                    "actually use, which index-lookup backend is configured, and the "
                                    "cron status. A **read** — not behind `--allow-upload`. Takes no "
                                    "input."),
                    "responses": {"200": _json_response("The watchlist.", {
                        "type": "object",
                        "required": ["file", "exists", "sources", "extractor", "lookup_backend"],
                        "properties": {
                            "file": {"type": "string", "description": "absolute path to the watchlist"},
                            "exists": {"type": "boolean", "description": "false ⇒ nothing configured yet"},
                            "extractor": {"type": "string", "enum": ["trafilatura", "stdlib"],
                                          "description": "which extractor a harvest would really use"},
                            "lookup_backend": {"type": "string", "enum": ["auto", "api", "cluster"]},
                            "index_pin": {"type": ["string", "null"],
                                          "description": "pinned Common Crawl index, if any"},
                            "state_file": {"type": "string",
                                           "description": "the vault-resident harvest ledger "
                                                          "(vault/.scrape-state.json)"},
                            "crawls_published": {"type": ["integer", "null"],
                                                 "description": "Common Crawl crawls known to this "
                                                                "vault — the denominator for each "
                                                                "source's harvest progress"},
                            "ledger_error": {"type": ["string", "null"],
                                             "description": "set when the ledger is unreadable; the "
                                                            "watchlist is still listed"},
                            "sources": {"type": "array",
                                        "items": {"$ref": "#/components/schemas/ScrapeSource"}},
                            "cron": _CRON_STATUS}},
                        example={"file": "/data/vault/scrape-sources.json", "exists": True,
                                 "extractor": "stdlib", "lookup_backend": "auto", "index_pin": None,
                                 "state_file": "/data/vault/.scrape-state.json",
                                 "crawls_published": 126, "ledger_error": None,
                                 "sources": [_SOURCE_EXAMPLE], "cron": _CRON_EXAMPLE}),
                        **_errors((404, "This instance is airgapped."))}},
            "post": {"tags": ["scrape"], "operationId": "addScrapeSource",
                     "summary": "Add a website to the watchlist (ONLINE MODE ONLY)",
                     "description": (f"{_online_note}\n\n{_write_note}\n\nThe `domain` is validated "
                                     "against `vault/taxonomy.md` HERE rather than at harvest time — "
                                     "an entry naming a domain that does not exist would otherwise "
                                     "sit on the list and fail every cron tick unattended. The "
                                     "response echoes the **canonical** stored URL, so you can see "
                                     "that `HTTPS://Example.com/a#top` was stored as "
                                     "`https://example.com/a`."),
                     "requestBody": _json_body({"$ref": "#/components/schemas/ScrapeSource"},
                                               example={"url": "https://www.keycloak.org/docs/latest/server_admin/",
                                                        "domain": "keycloak",
                                                        "label": "Keycloak Server Administration Guide (upstream)",
                                                        "match": "exact", "enabled": True, "direct": False}),
                     "responses": {"201": _json_response("Added.", {
                         "type": "object", "required": ["added", "file"],
                         "properties": {"added": {"$ref": "#/components/schemas/ScrapeSource"},
                                        "file": {"type": "string"},
                                        "next": {"type": "string"}}},
                         example={"added": _SOURCE_EXAMPLE, "file": "/data/vault/scrape-sources.json",
                                  "next": "POST /scrape  (harvest now) — or wait for the cron: GET /scrape/cron"}),
                         **_errors((400, "Bad URL, unknown domain, duplicate, or list full."),
                                   (404, "Uploads are disabled, or this instance is airgapped."))}},
            "patch": {"tags": ["scrape"], "operationId": "updateScrapeSource",
                      "summary": "Update a watchlist source (ONLINE MODE ONLY)",
                      "description": (
                          f"{_online_note}\n\n{_write_note}\n\n"
                          "**Partial update.** `url` selects the entry; only the fields you send are "
                          "touched, so pausing a source is `{\"url\":…,\"enabled\":false}` and nothing "
                          "else is disturbed.\n\n"
                          "**The `url` itself is NOT patchable.** It is the entry's identity — it is "
                          "what the watchlist is keyed by, what the Common Crawl lookup is built from, "
                          "and what names the harvested note and therefore the `kb:` token every citing "
                          "page uses. Patching it would strand the already-harvested file under the old "
                          "slug. A rename is `DELETE` + `POST`, two explicit acts.\n\n"
                          "`domain` **is** patchable (picking the wrong one at add time is an ordinary "
                          "mistake), but it only redirects FUTURE runs — anything already harvested "
                          "stays under the old domain, and the response says so.\n\n"
                          "The response carries `changed`, the fields that actually moved: a no-op "
                          "patch reports `changed: []` and does **not** rewrite the file, so the "
                          "watchlist's mtime keeps meaning 'when it last really changed'."),
                      "requestBody": _json_body({
                          "type": "object", "required": ["url"],
                          "properties": {
                              "url": {"type": "string",
                                      "description": "selects the entry; not itself patchable"},
                              "domain": {"type": "string",
                                         "description": "must be declared in vault/taxonomy.md"},
                              "label": {"type": ["string", "null"]},
                              "match": {"type": "string", "enum": ["exact", "prefix"]},
                              "enabled": {"type": "boolean"},
                              "direct": {"type": "boolean"}}},
                          example={"url": "https://www.keycloak.org/docs/latest/server_admin/",
                                   "enabled": False}),
                      "responses": {
                          "200": _json_response("Updated (or already up to date).", {
                              "type": "object", "required": ["updated", "changed", "file"],
                              "properties": {
                                  "updated": {"$ref": "#/components/schemas/ScrapeSource"},
                                  "changed": {"type": "array", "items": {"type": "string"},
                                              "description": "field names that actually moved; [] = no-op"},
                                  "file": {"type": "string"},
                                  "note": {"type": "string",
                                           "description": "present on a no-op, and when `domain` moved"}}},
                              example={"updated": dict(_SOURCE_EXAMPLE, enabled=False),
                                       "changed": ["enabled"],
                                       "file": "/data/vault/scrape-sources.json"}),
                          **_errors((400, "No url, nothing to update, an unpatchable/unknown field, "
                                          "a bad match value, or an undeclared domain."),
                                    (404, "Not on the watchlist, uploads disabled, or airgapped."))}},
            "delete": {"tags": ["scrape"], "operationId": "removeScrapeSource",
                       "summary": "Remove a website from the watchlist (ONLINE MODE ONLY)",
                       "description": (f"{_online_note}\n\n{_write_note}\n\n**Already-harvested notes "
                                       "are kept.** The raw tier is immutable ground truth and "
                                       "synthesis pages cite it, so un-watching a site must not "
                                       "silently invalidate every page citing what it produced; "
                                       "withdrawing the knowledge is Operation: RETRACT."),
                       "parameters": [_q("url", "The source URL to remove (or send it in a JSON body).",
                                         True, example="https://www.keycloak.org/docs/latest/server_admin/")],
                       "responses": {"200": _json_response("Removed from the watchlist.", {
                           "type": "object", "required": ["removed", "file"],
                           "properties": {"removed": {"$ref": "#/components/schemas/ScrapeSource"},
                                          "file": {"type": "string"},
                                          "note": {"type": "string",
                                                   "description": "restates that harvested notes are kept"}}},
                           example={"removed": _SOURCE_EXAMPLE, "file": "/data/vault/scrape-sources.json",
                                    "note": "already-harvested notes are kept (the raw tier is immutable); "
                                            "to withdraw the knowledge, retract the pages that cite it "
                                            "— CLAUDE.md, Operation: RETRACT"}),
                                     **_errors((400, "Missing or invalid url."),
                                               (404, "Not on the watchlist, uploads disabled, or airgapped."))}},
        }
        spec["paths"]["/scrape/cron"] = {
            "get": {"tags": ["scrape"], "operationId": "getScrapeCron",
                    "summary": "Scheduled-harvest status (ONLINE MODE ONLY)",
                    "description": (f"{_online_note}\n\nThe schedule (`WIKIKB_SCRAPE_CRON` — 5-field "
                                    "cron, an `@macro`, or an interval like `6h`), when it next "
                                    "fires, when it last did, and **both** the live `enabled` flag "
                                    "and the `env_default` it booted with — the runtime toggle "
                                    "deliberately does not rewrite the env, so a divergence between "
                                    "them must stay visible. Takes no input."),
                    "responses": {"200": _json_response("Cron status.", _CRON_STATUS,
                                                        example=_CRON_EXAMPLE),
                                  **_errors((404, "This instance is airgapped."))}},
            "post": {"tags": ["scrape"], "operationId": "setScrapeCron",
                     "summary": "Toggle the scheduled harvest (ONLINE MODE ONLY)",
                     "description": (f"{_online_note}\n\n{_write_note}\n\nRuntime-only: it does not "
                                     "rewrite `.env`. Default is **on**. Returns the same status "
                                     "object `GET /scrape/cron` does, already reflecting the change."),
                     "requestBody": _json_body({
                         "type": "object", "required": ["enabled"],
                         "properties": {"enabled": {"type": "boolean",
                                                    "description": "a string \"1\"/\"true\"/\"yes\"/\"on\" "
                                                                   "is accepted too"}}},
                         example={"enabled": False}),
                     "responses": {"200": _json_response("The new cron status.", _CRON_STATUS,
                                                         example=dict(_CRON_EXAMPLE, enabled=False,
                                                                      running=False, next_run=None,
                                                                      next_run_iso=None)),
                                   **_errors((400, "Body must be {\"enabled\": true|false}."),
                                             (404, "Uploads are disabled, or this instance is airgapped."))}},
        }

    spec["paths"][mcp_path] = {
        "post": {
            "tags": ["meta"], "operationId": "postMcp",
            "summary": "MCP over HTTP (JSON-RPC 2.0)",
            "description": (
                "Streamable-HTTP MCP transport — one JSON-RPC message per call, no SSE, no sessions. "
                "Dual-era: serves both the legacy `initialize` handshake and the 2026-07-28+ "
                "per-request `_meta` era, chosen per request.\n\n"
                "Tools: `wiki_ask` (the only non-read-only one), `wiki_search`, `wiki_route`, "
                "`wiki_read_page`. Try `{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/list\"}` "
                "first — it needs no arguments and lists the current input schemas.\n\n"
                f"Mount point is configurable via `WIKIKB_MCP_PATH` (currently `{mcp_path}`). "
                "`Origin` is validated when present — a browser-based DNS-rebinding attempt gets 403, "
                "while a backend client sending no `Origin` is unaffected. (That also means the /docs "
                "try-it panel, which is a browser and DOES send `Origin`, gets 403 here unless this "
                "instance's origin is in `WIKIKB_MCP_ALLOWED_ORIGINS` — use curl or an MCP client.)"),
            "requestBody": _json_body({
                "type": "object", "required": ["jsonrpc", "method"],
                "properties": {
                    "jsonrpc": {"type": "string", "const": "2.0"},
                    "id": {"type": ["string", "integer", "null"],
                           "description": "omit for a notification (answered 202, no body)"},
                    "method": {"type": "string",
                               "description": "e.g. initialize | tools/list | tools/call"},
                    "params": {"type": "object", "additionalProperties": True},
                }}, example={"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                             "params": {"name": "wiki_search",
                                        "arguments": {"domain": "keycloak", "query": "jdbc-ping", "k": 3}}}),
            "responses": {
                "200": _json_response("JSON-RPC result (or a JSON-RPC error object — still 200).", {
                    "type": "object",
                    "required": ["jsonrpc"],
                    "properties": {
                        "jsonrpc": {"type": "string", "const": "2.0"},
                        "id": {"type": ["string", "integer", "null"]},
                        "result": {"type": "object", "additionalProperties": True,
                                   "description": "present on success"},
                        "error": {"type": "object", "description": "present on failure",
                                  "properties": {"code": {"type": "integer"},
                                                 "message": {"type": "string"}}}},
                }, example={"jsonrpc": "2.0", "id": 1,
                            "result": {"content": [{"type": "text", "text": "…"}], "isError": False}}),
                "202": {"description": "Notification accepted (no body)."},
                **_errors((403, "Origin present but not allowlisted."),
                          (413, "Body exceeds the 2 MB cap.")),
            },
        },
        "get": {"tags": ["meta"], "operationId": "getMcp",
                "summary": "Not supported (no SSE stream)",
                "responses": _errors((405, "Spec-legal decline of the optional standalone SSE stream."))},
        "delete": {"tags": ["meta"], "operationId": "deleteMcp",
                   "summary": "Not supported (stateless — no sessions)",
                   "responses": _errors((405, "No session to terminate."))},
    }

    # NOT security-exempt when a token is configured. /health is exempt for a concrete reason
    # (kubelet-style probes cannot attach headers); no such reason applies to a full map of the
    # API, and serving one to an unauthenticated caller would contradict the same posture that
    # makes a disabled upload surface unfingerprintable. Swagger UI/Postman send bearer tokens fine.
    spec["paths"]["/openapi.json"] = {
        "get": {"tags": ["meta"], "operationId": "getOpenapi",
                "summary": "This document",
                "description": "The OpenAPI 3.1 document, built from the live config. Takes no input.",
                "responses": {"200": _json_response("OpenAPI 3.1 document.",
                                                    {"type": "object", "additionalProperties": True})}}
    }
    spec["paths"]["/docs"] = {
        "get": {"tags": ["meta"], "operationId": "getDocs",
                "summary": "Human-readable API reference with try-it-out (self-contained HTML)",
                "description": ("Renders this document — input structure, output structure and a live "
                                "request panel per endpoint — with zero external requests. Takes no "
                                "input."),
                "responses": {"200": {"description": "HTML page.",
                                      "content": {"text/html": {"schema": {"type": "string"}}}}}}
    }

    if auth_required:
        # setdefault, not assignment: the online branch above may already have put the ScrapeSource
        # schema in components, and overwriting it here would leave dangling $refs in the spec.
        spec.setdefault("components", {})["securitySchemes"] = {"bearerAuth": {
            "type": "http", "scheme": "bearer",
            "description": "Set `WIKIKB_API_TOKEN` on the server; send `Authorization: Bearer <token>`. "
                           "Only `/health` is exempt (unauthenticated probes)."}}
        spec["security"] = [{"bearerAuth": []}]
    return spec


# --- the offline docs page -------------------------------------------------------------------
# Inline CSS + one inline script, zero external requests (a CSP-tight, air-gapped box renders this
# identically to a networked one). Theme-aware so it isn't blinding in a dark terminal-adjacent setup.
#
# It does three things stock Swagger UI does and the previous version of this page did not:
#   1. INPUT structure  — path/query parameters AND the request-body schema, rendered field by field.
#   2. OUTPUT structure — the response schema per status code, rendered field by field, with the
#                         spec's example payload alongside it.
#   3. TRY ME           — a per-operation form built from those same parameters, which issues the
#                         real request same-origin and shows status, latency, headers and body, plus
#                         the equivalent curl line to paste into a terminal.
# $ref is resolved against components/schemas; there is no cycle in this spec, and depth is capped
# anyway so a future one degrades to a "…" row rather than hanging the page.
_DOCS_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>wikikb API</title>
<style>
:root{--bg:#fff;--fg:#1a1a1a;--mut:#5a5f66;--line:#e3e6ea;--card:#fafbfc;--acc:#0b6bcb;
      --get:#0b6bcb;--post:#1a7f4b;--put:#a15c00;--patch:#6b3fa0;--del:#b3261e;--code:#f3f5f7;
      --ok:#1a7f4b;--warn:#a15c00;--err:#b3261e}
@media(prefers-color-scheme:dark){:root{--bg:#14171a;--fg:#e8eaed;--mut:#9aa3ad;--line:#2a2f35;
      --card:#1b1f24;--acc:#5ea9ff;--get:#5ea9ff;--post:#5fd39b;--put:#e0a458;--patch:#c9a2ff;
      --del:#ff8a80;--code:#1f242a;--ok:#5fd39b;--warn:#e0a458;--err:#ff8a80}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:32px 20px 80px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:15px;text-transform:uppercase;letter-spacing:.08em;
   color:var(--mut);margin:36px 0 12px;font-weight:600}
h3{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--mut);margin:18px 0 6px;font-weight:600}
.sub{color:var(--mut);margin:0 0 8px}
.op{border:1px solid var(--line);border-radius:8px;margin:10px 0;overflow:hidden;background:var(--card)}
.op>summary{cursor:pointer;padding:12px 14px;display:flex;gap:10px;align-items:center;list-style:none}
.op>summary::-webkit-details-marker{display:none}
.m{font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;padding:5px 8px;border-radius:4px;
   color:#fff;flex:none;letter-spacing:.05em}
.GET{background:var(--get)}.POST{background:var(--post)}.PUT{background:var(--put)}
.PATCH{background:var(--patch)}.DELETE{background:var(--del)}
.p{font:13px/1 ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:600}
.s{color:var(--mut);font-size:13px;margin-left:auto;text-align:right}
.wr{font:600 10px/1 ui-sans-serif,system-ui;color:var(--warn);border:1px solid var(--warn);
    border-radius:4px;padding:3px 5px;flex:none}
.body{padding:0 14px 16px;border-top:1px solid var(--line)}
.desc{white-space:pre-wrap;margin:12px 0}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:13px;display:block;overflow-x:auto}
th,td{text-align:left;padding:6px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--mut);font-weight:600;white-space:nowrap}
code{background:var(--code);padding:1px 5px;border-radius:3px;
     font:13px ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--code);padding:10px 12px;border-radius:6px;overflow-x:auto;margin:6px 0;
    font:12.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}
.req{color:var(--del);font-size:11px}
.ind{color:var(--mut)}
a{color:var(--acc)}
.note{border-left:3px solid var(--acc);padding:10px 14px;background:var(--card);margin:14px 0;font-size:14px}
.tok{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:14px 0}
input,textarea,select{background:var(--bg);color:var(--fg);border:1px solid var(--line);
  border-radius:5px;padding:6px 8px;font:13px ui-monospace,SFMono-Regular,Menlo,monospace;width:100%}
textarea{min-height:96px;resize:vertical}
button{background:var(--acc);color:#fff;border:0;border-radius:5px;padding:7px 14px;cursor:pointer;
  font:600 13px ui-sans-serif,system-ui;width:auto}
button.ghost{background:transparent;color:var(--acc);border:1px solid var(--line)}
button:disabled{opacity:.55;cursor:default}
.try{border:1px dashed var(--line);border-radius:6px;padding:12px;margin-top:10px}
.f{display:grid;grid-template-columns:170px 1fr;gap:8px 10px;align-items:center;margin-bottom:10px}
.f label{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut);word-break:break-all}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.st{font:600 12px ui-monospace,SFMono-Regular,Menlo,monospace;padding:3px 7px;border-radius:4px;
    border:1px solid var(--line)}
.st.ok{color:var(--ok);border-color:var(--ok)}.st.err{color:var(--err);border-color:var(--err)}
.st.warn{color:var(--warn);border-color:var(--warn)}
.tabs{display:flex;gap:6px;margin:8px 0 2px;flex-wrap:wrap}
.tab{font:600 11px ui-sans-serif,system-ui;padding:4px 9px;border-radius:999px;border:1px solid var(--line);
     background:transparent;color:var(--mut);cursor:pointer;width:auto}
.tab[aria-selected=true]{color:var(--acc);border-color:var(--acc)}
</style></head><body><div class="wrap">
<h1>wikikb — llm-wiki JSON API</h1>
<p class="sub" id="ver"></p>
<div class="desc" id="info"></div>
<div class="note"><strong>Try it right here.</strong> Every operation below documents its input and
output structure and carries a <em>Try it</em> panel that calls this instance directly — no CDN, no
install, works on a sealed box. For codegen or a shared collection, point Postman / Insomnia /
Swagger UI at <a href="openapi.json"><code>/openapi.json</code></a>.</div>
<div class="tok" id="tokrow" hidden>
  <label for="tok" style="width:auto;white-space:nowrap">Bearer token</label>
  <input id="tok" type="password" placeholder="WIKIKB_API_TOKEN" style="max-width:340px" autocomplete="off">
  <button class="ghost" id="reload">Reload spec</button>
  <span class="sub" id="tokhint" style="margin:0"></span>
</div>
<div id="ops"></div>
</div><script>
(function(){
"use strict";
var SPEC = null;
var el = function(id){ return document.getElementById(id); };
function esc(s){ return String(s == null ? "" : s)
  .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }
function token(){ var t = el("tok"); return t ? t.value.trim() : ""; }

// ---- schema helpers -------------------------------------------------------------------------
function deref(sch){
  var seen = 0;
  while (sch && sch.$ref && seen++ < 8){
    var parts = sch.$ref.replace(/^#\\//,"").split("/");
    var node = SPEC;
    for (var i=0;i<parts.length && node;i++) node = node[parts[i]];
    sch = node;
  }
  return sch || {};
}
function typeName(sch){
  sch = deref(sch);
  if (!sch) return "any";
  if (sch.const !== undefined) return JSON.stringify(sch.const);
  if (sch.enum) return sch.enum.join(" | ");
  var t = sch.type;
  if (Array.isArray(t)) t = t.join(" | ");
  if (t === "array"){
    var it = deref(sch.items || {});
    return "array<" + (it.type === "object" ? "object" : typeName(it)) + ">";
  }
  return t || "any";
}
// Flatten a schema into {path, type, required, desc} rows, nested objects/arrays indented.
function rows(sch, out, prefix, depth, required){
  sch = deref(sch);
  out = out || []; prefix = prefix || ""; depth = depth || 0;
  if (depth > 4){ out.push({path: prefix + "…", type: "", desc: "(nested further — see openapi.json)"}); return out; }
  if (sch.type === "array" || sch.items){
    var items = deref(sch.items || {});
    if (items.type === "object" || items.properties){
      // Top level: the caller's heading already says "each element", so don't prefix every row
      // with a redundant "[]." — nested arrays DO get the marker (see the property loop below).
      return rows(items, out, prefix, depth, null);
    }
    return out;
  }
  var props = sch.properties || {};
  var req = required || sch.required || [];
  for (var k in props){
    var p = deref(props[k]);
    var path = prefix ? prefix + "." + k : k;
    out.push({path: path, type: typeName(props[k]), required: req.indexOf(k) >= 0,
              desc: p.description || "", depth: depth,
              extra: (p.default !== undefined ? "default " + JSON.stringify(p.default) : "")});
    if (p.type === "object" && p.properties) rows(p, out, path, depth + 1, p.required);
    else if (p.type === "array" && deref(p.items || {}).properties) rows(deref(p.items), out, path + "[]", depth + 1, deref(p.items).required);
  }
  return out;
}
function schemaTable(sch, title){
  sch = deref(sch);
  if (!sch || (!sch.properties && !sch.items && !sch.type)) return "";
  var rs = rows(sch, [], "", 0, null);
  if (!rs.length){
    return "<h3>" + esc(title) + "</h3><p class=\\"sub\\">" + esc(typeName(sch))
         + (sch.description ? " — " + esc(sch.description) : "") + "</p>";
  }
  var head = "<h3>" + esc(title) + "</h3>";
  if (sch.type === "array") head += "<p class=\\"sub\\">A JSON array; each element:</p>";
  var body = "";
  for (var i=0;i<rs.length;i++){
    var r = rs[i], pad = "&nbsp;".repeat((r.depth||0) * 3);
    body += "<tr><td>" + pad + "<code>" + esc(r.path) + "</code>"
          + (r.required ? " <span class=\\"req\\">required</span>" : "")
          + "</td><td><code>" + esc(r.type) + "</code>"
          + (r.extra ? " <span class=\\"ind\\">" + esc(r.extra) + "</span>" : "")
          + "</td><td>" + esc(r.desc) + "</td></tr>";
  }
  return head + "<table><tr><th>Field</th><th>Type</th><th>Description</th></tr>" + body + "</table>";
}
// A concrete payload: the spec's example when it has one, else synthesized from the schema.
function sample(sch, depth){
  sch = deref(sch); depth = depth || 0;
  if (!sch || depth > 5) return null;
  if (sch.example !== undefined) return sch.example;
  if (sch.const !== undefined) return sch.const;
  if (sch.default !== undefined) return sch.default;
  if (sch.enum) return sch.enum[0];
  var t = Array.isArray(sch.type) ? sch.type[0] : sch.type;
  if (t === "object" || sch.properties){
    var o = {};
    for (var k in (sch.properties || {})) o[k] = sample(sch.properties[k], depth + 1);
    return o;
  }
  if (t === "array") return [sample(sch.items || {}, depth + 1)];
  if (t === "integer" || t === "number") return 0;
  if (t === "boolean") return false;
  if (t === "null") return null;
  return "string";
}
function mediaOf(container){
  if (!container || !container.content) return null;
  var c = container.content;
  var key = c["application/json"] ? "application/json" : Object.keys(c)[0];
  return key ? {type: key, media: c[key]} : null;
}

// ---- try-it ---------------------------------------------------------------------------------
function buildTry(path, method, op){
  var wrap = document.createElement("div"); wrap.className = "try";
  var params = op.parameters || [];
  var rb = mediaOf(op.requestBody);
  var isJson = rb && rb.type === "application/json";
  var isBin = rb && !isJson;
  var form = document.createElement("div"); form.className = "f";
  var inputs = {};
  params.forEach(function(p){
    var lab = document.createElement("label");
    lab.textContent = p.name + (p.in === "path" ? " (path)" : "");
    if (p.required) lab.innerHTML += " <span class='req'>*</span>";
    var inp;
    var sch = p.schema || {};
    if (sch.enum){
      inp = document.createElement("select");
      if (!p.required) inp.appendChild(new Option("(omit)", ""));
      sch.enum.forEach(function(v){ inp.appendChild(new Option(v, v)); });
    } else {
      inp = document.createElement("input");
      inp.type = (sch.type === "integer" || sch.type === "number") ? "number" : "text";
      if (p.example !== undefined) inp.value = p.example;
      else if (sch.default !== undefined) inp.value = sch.default;
      inp.placeholder = typeName(sch);
    }
    inputs[p.name] = {el: inp, def: p};
    form.appendChild(lab); form.appendChild(inp);
  });
  wrap.appendChild(form);

  var bodyEl = null;
  if (isJson){
    var h = document.createElement("h3"); h.textContent = "Request body (JSON)"; wrap.appendChild(h);
    bodyEl = document.createElement("textarea");
    var ex = rb.media.example !== undefined ? rb.media.example : sample(rb.media.schema);
    bodyEl.value = ex === undefined || ex === null ? "{}" : JSON.stringify(ex, null, 2);
    wrap.appendChild(bodyEl);
  } else if (isBin){
    var h2 = document.createElement("h3"); h2.textContent = "Request body (" + rb.type + ")";
    wrap.appendChild(h2);
    bodyEl = document.createElement("input"); bodyEl.type = "file";
    if (rb.type === "application/pdf") bodyEl.accept = ".pdf,application/pdf";
    wrap.appendChild(bodyEl);
  }

  var row = document.createElement("div"); row.className = "row"; row.style.marginTop = "10px";
  var go = document.createElement("button"); go.textContent = "Execute " + method.toUpperCase();
  var curlBtn = document.createElement("button"); curlBtn.className = "ghost"; curlBtn.textContent = "Copy as curl";
  var stat = document.createElement("span"); stat.className = "sub";
  row.appendChild(go); row.appendChild(curlBtn); row.appendChild(stat);
  wrap.appendChild(row);
  var outWrap = document.createElement("div"); wrap.appendChild(outWrap);

  function buildUrl(){
    var url = path, qs = [];
    for (var name in inputs){
      var v = String(inputs[name].el.value || "").trim();
      var where = inputs[name].def.in;
      if (where === "path"){
        url = url.replace("{" + name + "}", encodeURIComponent(v));
      } else if (v !== ""){
        qs.push(encodeURIComponent(name) + "=" + encodeURIComponent(v));
      }
    }
    return url + (qs.length ? "?" + qs.join("&") : "");
  }
  function curlOf(){
    var url = buildUrl(), c = ["curl -i"];
    if (method !== "get") c.push("-X " + method.toUpperCase());
    if (token()) c.push("-H 'Authorization: Bearer <token>'");
    if (isJson && bodyEl && bodyEl.value.trim()){
      c.push("-H 'Content-Type: application/json'");
      c.push("--data '" + bodyEl.value.replace(/\\n\\s*/g, " ").replace(/'/g, "'\\\\''") + "'");
    } else if (isBin){
      c.push("-T <file>");
    }
    c.push("'" + location.origin + url + "'");
    return c.join(" ");
  }
  curlBtn.onclick = function(){
    var text = curlOf();
    outWrap.innerHTML = "<h3>curl</h3><pre>" + esc(text) + "</pre>";
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(
      function(){ stat.textContent = "curl copied"; },
      function(){ stat.textContent = "copy blocked — select the text above"; });
    else stat.textContent = "select the text above to copy";
  };
  go.onclick = function(){
    var missing = [];
    for (var n in inputs)
      if (inputs[n].def.required && !String(inputs[n].el.value || "").trim()) missing.push(n);
    if (missing.length){ stat.textContent = "missing required: " + missing.join(", "); return; }
    var init = {method: method.toUpperCase(), headers: {}};
    if (token()) init.headers["Authorization"] = "Bearer " + token();
    if (isJson && bodyEl && bodyEl.value.trim()){
      try { JSON.parse(bodyEl.value); }
      catch(e){ stat.textContent = "body is not valid JSON: " + e.message; return; }
      init.headers["Content-Type"] = "application/json";
      init.body = bodyEl.value;
    } else if (isBin){
      if (!bodyEl.files || !bodyEl.files[0]){ stat.textContent = "choose a file first"; return; }
      init.headers["Content-Type"] = rb.type;
      init.body = bodyEl.files[0];
    }
    go.disabled = true; stat.textContent = "requesting…";
    var url = buildUrl(), t0 = performance.now();
    fetch(url, init).then(function(res){
      return res.text().then(function(text){ return {res: res, text: text}; });
    }).then(function(r){
      var ms = Math.round(performance.now() - t0);
      var cls = r.res.status < 300 ? "ok" : (r.res.status < 500 ? "warn" : "err");
      var pretty = r.text;
      try { pretty = JSON.stringify(JSON.parse(r.text), null, 2); } catch(e){}
      var hdrs = [];
      r.res.headers.forEach(function(v, k){ hdrs.push(k + ": " + v); });
      outWrap.innerHTML =
        "<h3>Response</h3><div class=\\"row\\"><span class=\\"st " + cls + "\\">"
        + r.res.status + " " + esc(r.res.statusText || "") + "</span>"
        + "<span class=\\"sub\\">" + ms + " ms · " + (r.text.length) + " bytes · "
        + esc(url) + "</span></div>"
        + "<pre>" + esc(pretty || "(empty body)") + "</pre>"
        + "<details><summary class=\\"sub\\">response headers</summary><pre>"
        + esc(hdrs.join("\\n")) + "</pre></details>";
      stat.textContent = "";
    }).catch(function(e){
      outWrap.innerHTML = "<h3>Response</h3><pre>request failed: " + esc(e.message) + "</pre>";
      stat.textContent = "";
    }).then(function(){ go.disabled = false; });
  };
  return wrap;
}

// ---- rendering ------------------------------------------------------------------------------
function renderOp(path, method, op){
  var d = document.createElement("details"); d.className = "op";
  var M = method.toUpperCase();
  var writes = (M !== "GET");
  var params = op.parameters || [];
  var prows = "";
  params.forEach(function(p){
    var sch = p.schema || {};
    var def = sch.default !== undefined ? " <span class='ind'>default " + esc(JSON.stringify(sch.default)) + "</span>" : "";
    var ex = p.example !== undefined ? " <span class='ind'>e.g. " + esc(p.example) + "</span>" : "";
    prows += "<tr><td><code>" + esc(p.name) + "</code>"
           + (p.required ? " <span class='req'>required</span>" : "")
           + "</td><td><code>" + esc(p.in) + "</code></td><td><code>" + esc(typeName(sch)) + "</code>"
           + def + "</td><td>" + esc(p.description || "") + ex + "</td></tr>";
  });
  var inputHtml = prows
    ? "<h3>Input — parameters</h3><table><tr><th>Name</th><th>In</th><th>Type</th><th>Description</th></tr>"
      + prows + "</table>"
    : "";
  var rb = mediaOf(op.requestBody);
  if (rb){
    var reqd = op.requestBody.required ? "required" : "optional";
    inputHtml += "<h3>Input — request body (" + esc(rb.type) + ", " + reqd + ")</h3>";
    if (op.requestBody.description) inputHtml += "<p class='sub'>" + esc(op.requestBody.description) + "</p>";
    if (rb.type === "application/json"){
      inputHtml += schemaTable(rb.media.schema, "Body fields");
      var bex = rb.media.example !== undefined ? rb.media.example : sample(rb.media.schema);
      if (bex !== undefined && bex !== null)
        inputHtml += "<pre>" + esc(JSON.stringify(bex, null, 2)) + "</pre>";
    } else {
      inputHtml += "<p class='sub'>Raw body of type <code>" + esc(rb.type) + "</code>.</p>";
    }
  }
  if (!inputHtml) inputHtml = "<h3>Input</h3><p class='sub'>No parameters and no request body.</p>";

  var outHtml = "<h3>Output — responses</h3><table><tr><th>Status</th><th>Meaning</th></tr>";
  var codes = Object.keys(op.responses || {});
  codes.forEach(function(code){
    var r = op.responses[code];
    outHtml += "<tr><td><code>" + esc(code) + "</code></td><td>" + esc(r.description || "") + "</td></tr>";
  });
  outHtml += "</table>";
  codes.forEach(function(code){
    if (!/^2/.test(code)) return;                       // structure shown for the success shapes
    var m = mediaOf(op.responses[code]);
    if (!m || m.type !== "application/json") return;
    outHtml += schemaTable(m.media.schema, code + " response body");
    var rex = m.media.example !== undefined ? m.media.example : sample(m.media.schema);
    if (rex !== undefined && rex !== null)
      outHtml += "<p class='sub'>Example</p><pre>" + esc(JSON.stringify(rex, null, 2)) + "</pre>";
  });
  var errShape = null;
  codes.forEach(function(code){
    if (/^2/.test(code)) return;
    var m = mediaOf(op.responses[code]);
    if (m && m.type === "application/json") errShape = m.media.schema;
  });
  if (errShape) outHtml += "<p class='sub'>Every non-2xx body is <code>{\\"error\\": string}</code>.</p>";

  d.innerHTML = "<summary><span class=\\"m " + M + "\\">" + M + "</span>"
              + "<span class=\\"p\\">" + esc(path) + "</span>"
              + (writes ? "<span class=\\"wr\\">writes</span>" : "")
              + "<span class=\\"s\\">" + esc(op.summary || "") + "</span></summary>"
              + "<div class=\\"body\\"><div class=\\"desc\\">" + esc(op.description || "") + "</div>"
              + inputHtml + outHtml + "<h3>Try it</h3></div>";
  var body = d.querySelector(".body");
  body.appendChild(buildTry(path, method, op));
  return d;
}

function render(spec){
  SPEC = spec;
  el("ver").textContent = spec.info.title + " · v" + spec.info.version;
  el("info").textContent = spec.info.description || "";
  var order = {get:0, post:1, put:2, patch:3, delete:4}, out = el("ops");
  out.innerHTML = "";
  var groups = {};
  for (var path in spec.paths){
    var item = spec.paths[path];
    for (var method in item){
      var op = item[method];
      var tag = (op.tags && op.tags[0]) || "other";
      (groups[tag] = groups[tag] || []).push({path: path, method: method, op: op});
    }
  }
  var names = (spec.tags || []).map(function(t){ return t.name; });
  for (var g in groups) if (names.indexOf(g) < 0) names.push(g);
  names.forEach(function(tag){
    if (!groups[tag]) return;
    var h = document.createElement("h2"); h.textContent = tag; out.appendChild(h);
    groups[tag].sort(function(a, b){
      return a.path.localeCompare(b.path) || (order[a.method] - order[b.method]); });
    groups[tag].forEach(function(o){ out.appendChild(renderOp(o.path, o.method, o.op)); });
    delete groups[tag];
  });
}

function load(){
  var init = {headers: {}};
  if (token()) init.headers["Authorization"] = "Bearer " + token();
  fetch("openapi.json", init).then(function(res){
    if (res.status === 401){
      el("tokrow").hidden = false;
      el("tokhint").textContent = "this instance requires a bearer token";
      throw new Error("401 unauthorized — enter the bearer token above and press Reload spec");
    }
    if (!res.ok) throw new Error("HTTP " + res.status);
    return res.json();
  }).then(function(spec){
    render(spec);
    // Show the token row when the spec says auth is enforced, so try-it can attach it.
    if (spec.security || (spec.components && spec.components.securitySchemes)){
      el("tokrow").hidden = false;
      if (!el("tokhint").textContent)
        el("tokhint").textContent = "sent as Authorization: Bearer … by Try it";
    }
  }).catch(function(e){
    el("ops").textContent = "Could not load openapi.json: " + e.message;
  });
}
el("reload").onclick = load;
load();
})();
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
