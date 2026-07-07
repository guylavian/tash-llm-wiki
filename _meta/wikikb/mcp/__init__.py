"""wikikb.mcp — the OPTIONAL MCP (Model Context Protocol) stdio surface over the wiki.

Isolated in its own subpackage like serve/ and graph/: it owns a request/response protocol, so it
earns its own boundary. stdlib only (sys, json); no sockets, ever — the transport is stdin/stdout
pipes, not a network listener. Never imported at module scope by anything outside this package.
"""
