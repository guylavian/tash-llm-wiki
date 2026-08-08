"""modes.py — the ONE definition of the runtime OPERATION MODE. stdlib only, no network.

The application runs in exactly one of two modes, selected by the `WIKIKB_MODE` env var:

    airgapped (DEFAULT)  vault + MCP + the PDF upload/ingest write surface. Opens no outbound
                         connection, ever. This is the sealed-box posture the rest of CLAUDE.md
                         assumes ("stdlib only, air-gapped"), so it is what you get when nothing
                         is configured.
    online               EVERYTHING airgapped serves — same endpoints, same MCP tools, same
                         upload/ingest chain — PLUS the web-scraper surface (`wikikb/scrape/`).

The modes are ADDITIVE, not alternative: `online` is a strict superset. That is deliberate — an
operator switching modes must never lose an endpoint, and a client written against an airgapped
instance keeps working verbatim against an online one.

WHY "airgapped" AND NOT "offline": `offline` is already load-bearing vocabulary in this project
for a DIFFERENT axis — whether `ask` synthesizes prose through the local LLM gateway or falls back
to extractive answers (`WIKI_LLM`, `wikikb/online/` — the LiteLLM subpackage, which has nothing to
do with scraping). Reusing it here would make "offline mode" ambiguous in every future bug report.
`offline` is still accepted as an INPUT alias below, since it is the obvious synonym to reach for.

TWO PROPERTIES THIS MODULE EXISTS TO GUARANTEE:

  1. FAIL LOUD ON A TYPO. `WIKIKB_MODE=onlien` must not silently resolve to the default. A mode is
     a security posture; silently getting the wrong one — in either direction — is the failure this
     raises on. `serve.main()` turns the raise into a clean exit-2 with the message below.
  2. FAIL CLOSED ON A BUG. Anything that cannot resolve a mode gets `airgapped`, the mode that can
     do strictly less. `require_online()` is the guard every egress path must call at CALL time
     (not just at registration time), so "airgapped" is an enforced property rather than a label on
     a container that could still open a socket.
"""
import os

AIRGAPPED = "airgapped"
ONLINE = "online"
MODES = (AIRGAPPED, ONLINE)

ENV_VAR = "WIKIKB_MODE"
DEFAULT = AIRGAPPED                     # unset ⇒ the mode that can do less (fail closed)

# Input spellings accepted for a canonical mode. `offline` is here because it is what an operator
# will type first; it resolves to airgapped rather than erroring, but the CANONICAL name — what
# /health reports, what the logs print — is always one of MODES.
_ALIASES = {
    "offline": AIRGAPPED,
    "air-gapped": AIRGAPPED,
    "airgap": AIRGAPPED,
    "sealed": AIRGAPPED,
    "connected": ONLINE,
}


class ModeError(ValueError):
    """Raised for an unresolvable mode, or for an online-only feature reached in airgapped mode.

    Two distinct causes, one exception type on purpose: both mean "the configured posture forbids
    what was just asked for", and both are reported to the operator as text, never handled
    differently in code.
    """


def resolve(value):
    """Canonicalize one mode spelling. None/empty ⇒ DEFAULT. Unknown ⇒ ModeError (never DEFAULT)."""
    raw = (value or "").strip().lower()
    if not raw:
        return DEFAULT
    if raw in MODES:
        return raw
    if raw in _ALIASES:
        return _ALIASES[raw]
    raise ModeError(
        "%s=%r is not a known operation mode. Use one of: %s (aliases: %s). "
        "Unset ⇒ %s." % (ENV_VAR, value, ", ".join(MODES), ", ".join(sorted(_ALIASES)), DEFAULT))


def current():
    """The live mode from the environment. Raises ModeError on an unknown value — callers that
    must not crash on import use `current_safe()` and report the error separately."""
    return resolve(os.environ.get(ENV_VAR))


def current_safe():
    """(mode, error_message_or_None) — never raises.

    For module-scope use: `serve.py` is imported by `mcp.py` (and by the probes), so a bad env var
    must not turn into an import-time traceback in an unrelated tool. The mode returned alongside
    an error is DEFAULT (fail closed); the caller's `main()` is responsible for refusing to START
    when the error is non-None, which is what keeps property 1 above true.
    """
    try:
        return current(), None
    except ModeError as e:
        return DEFAULT, str(e)


def is_online(mode=None):
    return (mode or current()) == ONLINE


def capabilities(mode=None):
    """Mode-derived feature flags, as served by GET /health.

    MODE-DERIVED ONLY — these say what the MODE permits, not what this particular process has
    switched on. Upload, for instance, is permitted in both modes but still requires
    `--allow-upload`; /health reports that separately so the two are never conflated.
    """
    m = mode or current()
    return {
        "vault": True,          # the read surface: route/search/ask/expand/page
        "mcp": True,            # MCP over stdio and over HTTP
        "ingest": True,         # PDF upload -> md conversion -> crosslink (both modes)
        "scrape": m == ONLINE,  # the ONLY mode-gated capability
    }


def require_online(feature="this feature"):
    """Guard for every egress path. Call at CALL time, not only at registration time.

    Registration-time gating alone would mean a mis-wired route, a stale import, or a future
    refactor could still reach the network from an airgapped deployment. This is the check that
    makes the posture real, so it lives next to the socket, not next to the router.
    """
    mode = current()
    if mode != ONLINE:
        raise ModeError(
            "%s requires %s=%s; this instance runs in %s mode (no outbound network)."
            % (feature, ENV_VAR, ONLINE, mode))
    return mode
