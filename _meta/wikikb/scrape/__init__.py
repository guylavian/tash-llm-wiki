"""wikikb.scrape — the ONLINE-mode web-harvest surface.

Isolated in its own subpackage like serve/ and online/: it is the only part of the toolchain
permitted to open an OUTBOUND connection, so it earns its own boundary. Every entry point calls
`modes.require_online()` before touching the network, so importing this package on an airgapped
instance is harmless — it is the CALL that is refused, not the import (see modes.py, property 2).

NOT IMPLEMENTED YET. This package is the declared seam: `serve.py` mounts the endpoints in online
mode and they answer 501 until `fetch()` below is written.
"""
