#!/usr/bin/env python3
"""expand.py — graph expansion over the synthesized-page link graph. stdlib only, no network.

crosslink.py already writes a `## Sources` block of `[[reference-note]]` links and the body
already carries `[[page]]` wikilinks into every synthesized page — but no *retrieval* code
consumed those edges. This does: given a query, it ranks the synthesized pages lexically
(the cheap first-hit pass), takes the top-k as SEEDS, and returns their 1-hop neighborhood
with NO new corpus search:
  - neighbor PAGES   reached via the seeds' `[[page]]` wikilinks
  - reference NOTES  reached via the seeds' (and their neighbors') `## Sources` blocks

Those reference notes are the extra retrieval candidates. On a multi-hop query whose answer
note shares little surface vocabulary with the query (so lexical ranks it deep), the query
still matches a *synthesized page* that cites it — and the graph hands you the note directly,
at near-zero added cost. The eval imports this module so the scoreboard measures the real
tool (as it imports kb.py for lexical), not a re-implementation.

Derived + regenerable: edges are read live from the page files crosslink.py maintains; there
is no stored artifact. With no pages / no ## Sources, expansion is simply empty (graceful).

Usage:
    python3 expand.py --domain keycloak "active passive cross-site session failover"
    python3 expand.py --domain keycloak -k 5 "rp-initiated logout relying parties"
"""
import argparse
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
sys.dont_write_bytecode = True
from wikikb.retrieval import kb       # reuse the exact tokenizer + scorer so page ranking matches search ranking

PAGE_DIRS = paths.PAGE_DIRS
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
PAGELINK_RE = paths.PAGELINK_RE   # shared grammar: bare slug + optional |display
SOURCES_BLOCK_RE = re.compile(r"## Sources\n<!-- crosslink:begin.*?-->(.*?)<!-- crosslink:end -->",
                              re.DOTALL)
SOURCES_NOTE_RE = re.compile(r"\[\[([^\]|#]+)")                     # [[note-slug|Title]] inside it

_pages_cache = None


def load_pages():
    """slug -> {domain, title, summary, body, note_sources:set, page_links:set}."""
    global _pages_cache
    if _pages_cache is not None:
        return _pages_cache
    G = {}
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            text = open(os.path.join(full, fn), encoding="utf-8").read()
            m = FM_RE.match(text)
            fm = {}
            if m:
                for line in m.group(1).splitlines():
                    if line and not line[0].isspace() and ":" in line and not line.startswith(("-", "#")):
                        k, _, v = line.partition(":")
                        fm[k.strip()] = v.strip().strip('"\'')
            sb = SOURCES_BLOCK_RE.search(text)
            note_sources = set(SOURCES_NOTE_RE.findall(sb.group(1))) if sb else set()
            body_wo_sources = SOURCES_BLOCK_RE.sub("", text)
            page_links = set(PAGELINK_RE.findall(body_wo_sources))
            G[fn[:-3]] = {
                "domain": fm.get("domain"), "title": fm.get("title") or fn[:-3],
                "summary": fm.get("summary") or "", "body": body_wo_sources,
                "note_sources": note_sources, "page_links": page_links,
            }
    _pages_cache = G
    return G


def rank_pages(domain, query):
    """Lexical rank of synthesized pages in this domain (reusing kb.score/build_idf/avg_dl — pages
    ARE their own corpus here, so idf/dl stats are computed over just this domain's page texts,
    not the reference-note corpus kb.py ranks)."""
    terms = kb.toks(query)
    G = load_pages()
    pseudos = []
    for slug, p in G.items():
        if p["domain"] != domain:
            continue
        pseudo = {"title": p["title"], "abstract": p["summary"], "body_status": "fetched",
                  "primary": False, "family": None, "version": None, "_body": p["body"]}
        pseudos.append((slug, pseudo))
    if not pseudos:
        return []
    pool = [ps for _, ps in pseudos]
    idf, avgdl = kb.build_idf(pool), kb.avg_dl(pool)   # once per query, over this domain's pages
    scored = []
    for slug, pseudo in pseudos:
        sc = kb.score(pseudo, terms, pseudo["_body"], idf, avgdl)
        if sc > 0:
            scored.append((sc, slug))
    scored.sort(key=lambda x: -x[0])
    return [slug for _, slug in scored]


def expand(domain, query, k=10):
    """Top-k page seeds -> 1-hop neighborhood. Returns
      {seeds, neighbors, notes_seed, notes_closure}
    where
      notes_seed    = the seeds' OWN `## Sources` notes — tight, high-precision (the seed
                      page that the query matched directly cites these), and
      notes_closure = notes_seed PLUS the seeds' [[linked]] same-domain pages' `## Sources`
                      — broader recall, looser precision.
    Retrieval should prefer notes_seed and treat notes_closure as the fallback ceiling."""
    if os.environ.get("WIKIKB_NO_EXPAND") == "1":
        return {"seeds": [], "neighbors": [], "notes_seed": set(), "notes_closure": set()}
    G = load_pages()
    seeds = rank_pages(domain, query)[:k]
    neighbors, notes_seed, notes_closure = [], set(), set()
    for slug in seeds:
        p = G[slug]
        notes_seed |= p["note_sources"]
        notes_closure |= p["note_sources"]
        for lp in p["page_links"]:
            q = G.get(lp)
            if q and q["domain"] == domain:
                if lp not in neighbors and lp not in seeds:
                    neighbors.append(lp)
                notes_closure |= q["note_sources"]
    return {"seeds": seeds, "neighbors": neighbors,
            "notes_seed": notes_seed, "notes_closure": notes_closure}


def graph_notes(domain, query, k=10, closure=False):
    """The reference-note candidate set retrieval consumes — seed-sources by default
    (high precision); pass closure=True for the broader 1-hop ceiling."""
    e = expand(domain, query, k)
    return e["notes_closure"] if closure else e["notes_seed"]


def _asof_filter(r, domain, asof_token):
    """Drop reference notes whose CITES edge is version-temporal with valid_from > asof (the note
    describes behavior introduced AFTER the as-of point). Structural/undated edges are NEVER filtered
    (omit-not-fabricate: an undated note stays visible). Mutates r's note sets, returns a status line —
    or None (no filtering) when the token can't resolve or the tkg layer is unavailable. Lazy imports so
    `expand` stays a stdlib retrieval path when --as-of is absent (the eval golden depends on that)."""
    from wikikb.tkg import versions, model, store
    asof = versions.resolve_asof(asof_token)
    if asof is None:
        sys.stderr.write("note: could not resolve --as-of %r to a usable date; no temporal filtering.\n"
                         % asof_token)
        return None
    try:
        g = store.load_store() if store.store_exists() else model.build_graph()
    except Exception as e:                                              # noqa: BLE001 — degrade, never crash retrieval
        sys.stderr.write("note: tkg store unavailable (%s); no temporal filtering.\n" % e)
        return None
    # note-slug -> valid_from, from any version-temporal CITES edge targeting it (same note => same date).
    src_valid = {e.dst: e.valid_from for e in g.edges
                 if e.rel == "CITES" and e.kind == model.VERSION_TEMPORAL and e.valid_from}
    dropped = {n for n in (r["notes_seed"] | r["notes_closure"])
               if src_valid.get(n) and src_valid[n] > asof}
    r["notes_seed"] -= dropped
    r["notes_closure"] -= dropped
    return ("--as-of %s (%s): filtered %d later-version note(s); structural/undated notes unaffected."
            % (asof_token, asof, len(dropped)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", required=True)
    ap.add_argument("-k", type=int, default=10, help="number of page seeds (default 10)")
    ap.add_argument("--as-of", dest="as_of", default=None,
                    help="version or ISO date — drop reference notes introduced after this point (uses the tkg store)")
    ap.add_argument("query", nargs="+")
    args = ap.parse_args()
    r = expand(args.domain, " ".join(args.query), args.k)
    if args.as_of:
        line = _asof_filter(r, args.domain, args.as_of)
        if line:
            print(line)
    print("seeds (top-%d pages):  %s" % (args.k, ", ".join(r["seeds"][:args.k]) or "(none)"))
    print("1-hop neighbor pages: %s" % (", ".join(r["neighbors"]) or "(none)"))
    print("\nseed-source notes (primary, %d):" % len(r["notes_seed"]))
    for nslug in sorted(r["notes_seed"]):
        print("  - " + nslug)
    extra = r["notes_closure"] - r["notes_seed"]
    print("1-hop closure adds (%d): %s" % (len(extra), ", ".join(sorted(extra)) or "(none)"))


if __name__ == "__main__":
    main()
