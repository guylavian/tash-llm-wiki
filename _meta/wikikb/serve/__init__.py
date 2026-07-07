"""wikikb.serve — the OPTIONAL stateless HTTP surface over the wiki, for SRE/agent consumption.

Isolated in its own subpackage like online/ and graph/: it opens a real socket, so it earns its own
boundary. stdlib only (http.server); never imported at module scope by anything outside this package,
so `import wikikb` elsewhere never binds a port.
"""
