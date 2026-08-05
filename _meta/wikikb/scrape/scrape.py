#!/usr/bin/env python3
"""scrape.py — web harvest into the raw tier. ONLINE MODE ONLY. **Not implemented yet.**

This is the seam, committed ahead of the implementation so the mode split is complete and testable:
`WIKIKB_MODE=online` mounts POST /scrape and GET /scrape/sources, and both answer 501 pointing here.
In airgapped mode those paths are indistinguishable from any unknown path (serve.py reuses the same
`_no_such_endpoint()` the disabled upload surface uses), so the online-only surface is not
fingerprintable on a sealed box.

WHERE A SCRAPE MUST LAND (the contract the implementation has to honour — it is the same one the
PDF path already follows, and the reason this is a seam rather than a free-form fetcher):

    fetch(url) -> raw bytes/text
      ↓ writes ONLY into  vault/_sources/<domain>/_raw/web/
      ↓ then the SAME chain the upload path runs (wikikb/serve/jobs.py):
        <html-to-corpus> → corpus_to_vault --apply → build

  * The raw tier is IMMUTABLE ground truth. A scrape adds files to it; it never edits an existing
    one, never touches vault/reference/<domain>/ directly, and never writes a synthesis page.
  * Provenance is `web:<url> (label, fetched YYYY-MM-DD)` per CLAUDE.md's source tiers, and the
    body must be marked as upstream/community material so it is never mistaken for a vendor
    support statement.
  * Run it through `jobs.RUNNER`, not inline in a request handler — same reason the PDF chain does:
    one serialized worker, because `build` regenerates whole-vault artifacts.

Deliberately NOT decided here (they are implementation choices, and guessing them now would bake in
the wrong seam): the fetcher (stdlib urllib vs a vendored client), HTML→Markdown extraction, robots
/ rate-limit policy, and whether a scrape is one URL or a crawl frontier.
"""
import argparse
import sys

from wikikb import modes

sys.dont_write_bytecode = True


def fetch(url, domain=None):
    """Fetch one URL into the raw tier. ONLINE MODE ONLY.

    `require_online()` is called HERE — at the socket, not at the router — so no future caller can
    reach the network from an airgapped deployment by wiring up a new path (modes.py, property 2).
    """
    modes.require_online("web scraping")
    raise NotImplementedError(
        "wikikb.scrape.fetch() is not implemented yet — this module is the declared seam for the "
        "online-mode web scraper. See the module docstring for the raw-tier contract it must honour.")


def sources():
    """Configured scrape sources (feeds/URL sets). ONLINE MODE ONLY. Not implemented yet."""
    modes.require_online("web scraping")
    raise NotImplementedError("wikikb.scrape.sources() is not implemented yet.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="URL to harvest into vault/_sources/<domain>/_raw/web/")
    ap.add_argument("--domain", help="target domain (must be declared in vault/taxonomy.md)")
    args = ap.parse_args()
    try:
        # Mode is checked before anything else so the airgapped refusal is the FIRST thing an
        # operator sees, rather than a NotImplementedError that hides which of the two is the
        # real blocker on their box.
        modes.require_online("web scraping")
    except modes.ModeError as e:
        raise SystemExit("scrape ▸ REFUSED: %s" % e)
    if not args.url:
        raise SystemExit("scrape ▸ usage: python3 -m wikikb scrape <url> --domain <d>")
    try:
        fetch(args.url, args.domain)
    except NotImplementedError as e:
        raise SystemExit("scrape ▸ %s" % e)


if __name__ == "__main__":
    main()
