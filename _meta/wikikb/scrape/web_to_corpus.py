#!/usr/bin/env python3
"""web_to_corpus.py — turn harvested web notes into corpus records. stdlib only, NO network.

The web sibling of `pdf_to_corpus.py` / `docs_to_corpus.py`, and deliberately the same shape: it
reads what `scrape.py` wrote into `vault/_sources/<domain>/_raw/web/` (a `<slug>.md` body plus its
`<slug>.json` sidecar) and emits the SAME `corpora/<domain>/index.jsonl` + body files that the
proven `corpus_to_vault.py` consumes. So a web-harvested domain is the usual three commands and no
bespoke code:

    python3 -m wikikb scrape --domain <d> --all                       # 1. web  -> raw tier
    python3 -m wikikb web_to_corpus --domain <d> --append --apply     # 2. raw  -> corpus
    python3 -m wikikb corpus_to_vault --domain <d> --apply            # 3. corpus -> reference notes
    python3 -m wikikb build                                           # 4. crosslink/index/lint/verify

NO NETWORK HERE, ON PURPOSE. Fetching and folding-in are separate steps so a failed extraction can
be re-run without re-fetching, several harvests can share one `build`, and this half of the chain
stays runnable (and testable) on an airgapped box against an already-harvested raw tier.

`--append` IS NOT OPTIONAL IN PRACTICE — same trap as the PDF path. Without it the tool truncates
`corpora/<domain>/index.jsonl` and rewrites it from just what is under `--src`; the next
`corpus_to_vault --apply` would then regenerate `reference/<domain>/` from that truncated index. On
a corpus-backed domain (keycloak has 800 harvested reference notes) one scraped page would silently
destroy the ground-truth tier. The serve-side job chain always passes it.

THE CITATION TOKEN. Each record's reference note gets the slug `web-<host>-<url-tail>` (family
`web-<host>`, no version), and `crosslink.py` indexes a note by BOTH its source-URL tail and its own
slug — so the stable, collision-free token to put in a page's `sources:` is `kb:web-<host>-<tail>`,
which this tool prints for every record. The page ALSO carries the `web:<url> (label, fetched DATE)`
token that CLAUDE.md's source tiers require for upstream material; the two are complementary, not
alternatives: `web:` states the provenance and the fetch date, `kb:` is what puts the note into the
link graph.

UPSTREAM MARKING IS APPLIED HERE, NOT LEFT TO THE PAGE AUTHOR. Every body written from a web
harvest is prefixed with an explicit "Upstream / community source" banner carrying the URL and the
capture date, because the note is immutable once written and a reader who greps into the middle of
it must still be able to tell that it is not a vendor support statement.
"""
import argparse
import json
import os
import re
import sys
from urllib.parse import urlsplit

from wikikb import paths
from wikikb.corpus import corpus_to_vault as c2v      # base_slug/url_tail — reuse, never re-derive

sys.dont_write_bytecode = True

_slug_bad = re.compile(r"[^a-z0-9]+")


def slugify(s):
    return _slug_bad.sub("-", (s or "").lower()).strip("-") or "web"


def family_for(url):
    """`web-<host>` — the family prefix that scopes a harvested note's slug to its site.

    Without the host in the family, two sites' `/index.html` would produce the same base slug and
    corpus_to_vault would silently disambiguate them with a `-2` suffix — making the citation token
    depend on the order records happen to be written in.
    """
    host = (urlsplit(url).hostname or "web").lower()
    if host.startswith("www."):
        host = host[4:]
    return "web-" + slugify(host)


def _drop_leading_h1(body, title):
    """Remove a leading `# …` when it is the document's own title.

    Only the FIRST line, and only when it is an H1: a document whose body genuinely starts with a
    section heading keeps it. The title match is loose (case/whitespace) because an extractor's
    `<title>` and the page's `<h1>` routinely differ by a site-name suffix.
    """
    lines = body.split("\n", 1)
    first = lines[0].strip()
    if not first.startswith("# "):
        return body
    head = first[2:].strip().lower()
    want = (title or "").strip().lower()
    if want and (head == want or head in want or want in head):
        return (lines[1] if len(lines) > 1 else "").lstrip("\n")
    return body


def banner(sidecar):
    """The upstream/community marker prepended to every web-derived body."""
    url = sidecar.get("url", "")
    return ("> **Upstream / community source — not a vendor support statement.**\n"
            "> Harvested from %s (capture: %s, via %s).\n"
            "> Cite as `web:%s (%s, fetched %s)`. Prefer a vendor/RH ground-truth source for\n"
            "> support questions and note any difference.\n"
            % (url, sidecar.get("captured") or "unknown",
               sidecar.get("source") or "commoncrawl", url,
               sidecar.get("label") or sidecar.get("title") or "upstream",
               sidecar.get("captured") or "unknown"))


def read_harvest(src):
    """(sidecar, body) pairs for every complete harvest under `src`.

    A `.md` without its `.json`, or vice versa, is SKIPPED and reported rather than guessed at: the
    sidecar is where the URL and the capture date live, and inventing either would put a wrong
    `fetched` date on an immutable note.
    """
    pairs, orphans = [], []
    if not os.path.isdir(src):
        return pairs, orphans
    for fn in sorted(os.listdir(src)):
        if not fn.endswith(".md"):
            continue
        stem = fn[:-3]
        side = os.path.join(src, stem + ".json")
        if not os.path.isfile(side):
            orphans.append((fn, "no .json sidecar"))
            continue
        try:
            with open(side, encoding="utf-8") as fh:
                sidecar = json.load(fh)
        except (OSError, ValueError) as e:
            orphans.append((fn, "unreadable sidecar: %s" % e))
            continue
        if not sidecar.get("url"):
            orphans.append((fn, "sidecar has no url"))
            continue
        with open(os.path.join(src, fn), encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        if not body.strip():
            orphans.append((fn, "empty body"))
            continue
        pairs.append((sidecar, body))
    return pairs, orphans


def build(src, domain):
    recs, bodies, orphans_out = [], {}, []
    pairs, orphans = read_harvest(src)
    orphans_out.extend(orphans)
    seen_urls = {}
    for sidecar, body in pairs:
        url = sidecar["url"]
        if url in seen_urls:
            orphans_out.append((sidecar.get("body_file") or url, "duplicate url"))
            continue
        seen_urls[url] = True
        fam = family_for(url)
        # Drop the page's own leading H1: `corpus_to_vault.render_note` prepends `# <title>`, so
        # keeping it would give every web-derived reference note two identical top-level headings.
        stripped = _drop_leading_h1(body.strip(), sidecar.get("title"))
        text = banner(sidecar) + "\n" + stripped + "\n"
        body_file = "bodies/" + slugify(url.split("//", 1)[-1])[:150] + ".md"
        rec = {
            "title": sidecar.get("title") or url,
            "url": url,
            "family": fam,
            "documentKind": "Web",
            # Markdown syntax stripped: the abstract is a ranking/preview signal (kb.py scores it,
            # the gated index prints it), and a leading "#" in it is noise in every one of those uses.
            "abstract": re.sub(r"\s+", " ", re.sub(r"^#{1,6}\s*", "", stripped, flags=re.M))[:280].strip(),
            "body_status": "fetched",
            "body_file": body_file,
        }
        recs.append(rec)
        bodies[body_file] = text
    return recs, bodies, orphans_out


def predicted_slug(rec):
    """What `corpus_to_vault` will name this record's reference note — i.e. the `kb:` token.

    Computed by calling ITS `base_slug`, not by re-deriving the rule here: a second copy of the
    naming logic would drift, and the whole value of printing the token is that it is the one a
    page can actually cite.
    """
    return c2v.base_slug(rec)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", required=True)
    ap.add_argument("--src", default=None,
                    help="harvest dir (default: vault/_sources/<domain>/_raw/web)")
    ap.add_argument("--append", action="store_true",
                    help="merge into an existing corpora/<domain>/index.jsonl (dedup by url; the "
                         "new harvest wins). REQUIRED on a domain that already has a corpus.")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    src = args.src or os.path.join(str(paths.WIKI), "_sources", args.domain, "_raw", "web")
    recs, bodies, orphans = build(src, args.domain)

    outdir = os.path.join(str(paths.CORPORA), args.domain)
    rel = os.path.relpath(outdir, str(paths.ROOT))
    print("domain=%s  src=%s" % (args.domain, src))
    print("harvested documents=%d  records=%d" % (len(recs), len(recs)))
    if orphans:
        print("SKIPPED %d: %s" % (len(orphans), ", ".join("%s [%s]" % o for o in orphans)))
    for r in recs[:5]:
        print("  %s\n      -> cite as kb:%s   (and web:%s)" % (r["url"], predicted_slug(r), r["url"]))
    if len(recs) > 5:
        print("  … and %d more" % (len(recs) - 5))
    if not recs:
        # Not an error: an empty harvest dir is the normal state of a domain nobody has scraped
        # yet, and the job chain runs this step unconditionally after a scrape that may have found
        # nothing new. Exiting non-zero would fail the whole chain over a no-op.
        print("nothing to do (no complete <slug>.md + <slug>.json pairs under --src)")
        return

    if not args.apply:
        print("\n--- DRY RUN (no files written). Re-run with --append --apply, then: "
              "python3 -m wikikb corpus_to_vault --domain %s --apply ---" % args.domain)
        return

    os.makedirs(os.path.join(outdir, "bodies"), exist_ok=True)
    idx = os.path.join(outdir, "index.jsonl")
    existing = []
    if args.append and os.path.isfile(idx):
        urls = {r["url"] for r in recs}
        with open(idx, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("url") not in urls:               # the new harvest wins on a collision
                    existing.append(rec)
    allrecs = existing + recs
    with open(idx, "w", encoding="utf-8") as fh:
        for r in allrecs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for bf, text in bodies.items():
        with open(os.path.join(outdir, bf), "w", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
    print("\nWROTE %s/index.jsonl (%d records%s) + %d body files" % (
        rel, len(allrecs), ", %d kept from --append" % len(existing) if existing else "",
        len(bodies)))
    print("NEXT: python3 -m wikikb corpus_to_vault --domain %s --apply   "
          "(then: python3 -m wikikb build)" % args.domain)


if __name__ == "__main__":
    main()
