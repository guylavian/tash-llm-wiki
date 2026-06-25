"""wikikb.online — the OPTIONAL online tier: token/$/latency cost accounting + the local-first LiteLLM gateway.

Isolated in its own subpackage so the air-gap auditing rule is structurally enforced: any module that
can make a network call or incur $ lives here and ONLY here. Callers lazy-import or check `available()`
at call time, never at module scope — so importing the rest of the toolchain stays stdlib-safe and
opens no socket. (Keep this boundary: do not merge these into graph/ or a general util package.)
"""
