"""wikikb.scrape — the ONLINE-mode web-harvest surface.

Isolated in its own subpackage like serve/ and online/: it is the only part of the toolchain
permitted to open an OUTBOUND connection, so it earns its own boundary. Every entry point calls
`modes.require_online()` before touching the network, so importing this package on an airgapped
instance is harmless — it is the CALL that is refused, not the import (see modes.py, property 2).

Six modules, split along the line between "decides what to fetch" and "fetches":

    sources.py       the watchlist (vault/scrape-sources.json): add/remove/list, URL
                     canonicalization, SURT keys. No network.
    commoncrawl.py   collinfo.json -> the newest crawl; the CDX index lookup (HTTP API, falling back
                     to a range-searched cluster.idx on data.commoncrawl.org); the ranged WARC fetch.
    extract.py       archived HTML -> Markdown. trafilatura when installed, stdlib otherwise.
    scrape.py        the orchestrator + CLI: watchlist or ad-hoc URL -> notes under
                     vault/_sources/<domain>/_raw/web/.
    web_to_corpus.py raw web notes -> corpora/<domain>/index.jsonl, so the rest of the chain
                     (corpus_to_vault -> build) is the SAME one the PDF upload path runs. No network.
    cron.py          the scheduled-harvest timer. Decides *when*; fetches nothing itself.
"""
