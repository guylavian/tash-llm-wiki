#!/usr/bin/env python3
"""tkg.py — the temporal + cross-domain knowledge-graph CLI. stdlib only, no network.

    python3 -m wikikb tkg ingest                          # build the graph from the vault → JSON store
    python3 -m wikikb tkg graph-status                    # node/edge/domain health snapshot
    python3 -m wikikb tkg cross-domain-query [--from D --to D] [--version V]
    python3 -m wikikb tkg provenance-trace <slug>         # what a page rests on / what rests on a source
    python3 -m wikikb tkg temporal-query [--as-of V] [--domain D]

The store is canonical and stdlib-built; the optional Graphiti/Kuzu backend (Phase 5) never enters this
path. Phase 3 ships structural ingest + cross-domain + provenance; the temporal verbs report honestly
that the temporal layer (tkg/versions.py) is a Phase 4 feature rather than fabricating dates.
"""
import argparse
import sys

from wikikb.tkg import model, store


def _load_or_build():
    """Load the JSON store, or build it on the fly if it hasn't been ingested yet (graceful)."""
    if store.store_exists():
        return store.load_store()
    sys.stderr.write("note: no store at %s — building in-memory (run `tkg ingest` to persist)\n"
                     % store.DEFAULT_PATH)
    return model.build_graph()


def _hist(d):
    return ", ".join("%s=%d" % (k, d[k]) for k in sorted(d))


def cmd_ingest(args):
    g = model.build_graph()
    if args.stdout:
        import json
        json.dump(store.graph_to_dict(g), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return
    path = store.save_store(g)
    labels = g.meta["labels"]
    rels = g.meta["relations"]
    xdom = model.cross_domain_edges(g)
    print("INGESTED → %s" % path)
    print("  nodes: %d  (%s)" % (g.meta["node_count"], _hist(labels)))
    print("  edges: %d  (%s)" % (g.meta["edge_count"], _hist(rels)))
    print("  version-temporal edges: %d" % g.meta["version_temporal_edges"])
    print("  %s" % g.meta.get("note", ""))
    print("  cross-domain LINKS_TO: %d" % len(xdom))
    if not xdom:
        print("  (no cross-domain wikilinks in the vault yet — sparse by content, not a bug; "
              "write [[links]] across domains to populate cross-domain-query)")
    from wikikb.tkg import graphiti_backend  # lazy: the common path never imports the optional backend
    if args.backend:
        if graphiti_backend.available():
            print("  backend: loaded into Kuzu → %s" % graphiti_backend.load_graph(g))
        else:
            print("  backend: --backend requested but " + graphiti_backend.status_str())
    elif graphiti_backend.available():
        print("  backend: available (WIKI_TKG=%s) — pass --backend to also load into Kuzu"
              % graphiti_backend.mode())


def cmd_status(args):
    g = _load_or_build()
    labels, doms, srcs, rels, kinds = {}, {}, {}, {}, {}
    deg = {}
    for n in g.nodes.values():
        labels[n.label] = labels.get(n.label, 0) + 1
        if n.domain and n.label in ("Entity", "Topic", "Question"):   # pages only — Source nodes counted separately
            doms[n.domain] = doms.get(n.domain, 0) + 1
        elif n.domain and n.label == "Source":
            srcs[n.domain] = srcs.get(n.domain, 0) + 1
    for e in g.edges:
        rels[e.rel] = rels.get(e.rel, 0) + 1
        kinds[e.kind] = kinds.get(e.kind, 0) + 1
        deg[e.src] = deg.get(e.src, 0) + 1
        deg[e.dst] = deg.get(e.dst, 0) + 1
    linked = set(deg)
    orphans = [nid for nid, n in g.nodes.items() if nid not in linked]
    hubs = sorted(deg.items(), key=lambda kv: (-kv[1], kv[0]))[:8]
    xdom = model.cross_domain_edges(g)
    print("GRAPH STATUS  (schema %s)" % g.meta.get("schema", "?"))
    print("  nodes: %d  (%s)" % (len(g.nodes), _hist(labels)))
    print("  pages by domain: %s" % _hist(doms))
    print("  sources by domain: %s" % _hist(srcs))
    print("  edges: %d  (rel: %s | kind: %s)" % (len(g.edges), _hist(rels), _hist(kinds)))
    print("  cross-domain LINKS_TO: %d" % len(xdom))
    print("  orphan nodes (no edges): %d" % len(orphans))
    print("  top hubs (by degree):")
    for nid, dg in hubs:
        n = g.nodes.get(nid)
        print("    %-44s %3d  [%s]" % (nid, dg, n.label if n else "?"))
    from wikikb.tkg import graphiti_backend  # lazy: status only; never pulls kuzu unless installed+enabled
    print("  " + graphiti_backend.status_str())


def cmd_cross_domain(args):
    g = _load_or_build()
    xdom = model.cross_domain_edges(g)
    if args.version:
        # Cross-domain bridges are page↔page [[wikilinks]] — STRUCTURAL by nature (a link carries no
        # product version). Version validity lives on CITES edges, so `--version` can't honestly filter
        # cross-domain links. Say so plainly and point at the right verb, rather than silently no-op.
        print("note: --version does not apply to cross-domain links (page↔page wikilinks are structural, "
              "no version); use `tkg temporal-query --as-of %s` for version-scoped CITES edges. "
              "Showing all cross-domain links." % args.version)
    rows = []
    for e in xdom:
        s, d = g.nodes[e.src], g.nodes[e.dst]
        if args.from_ and s.domain != args.from_:
            continue
        if args.to and d.domain != args.to:
            continue
        rows.append((s.domain, e.src, d.domain, e.dst))
    if not rows:
        print("no cross-domain edges match." + (
            "" if g.edges else " (store is empty — run `tkg ingest`)"))
        print("(cross-domain links are sparse in this vault by content; add [[links]] across domains.)")
        return
    print("CROSS-DOMAIN LINKS_TO  (%d)" % len(rows))
    for sd, ss, dd, ds in sorted(rows):
        print("  [%s] %s  →  [%s] %s" % (sd, ss, dd, ds))


def cmd_provenance(args):
    g = _load_or_build()
    slug = args.slug
    n = g.nodes.get(slug)
    if n is None:
        print("no node %r in the graph. (run `tkg ingest`, or check the slug)" % slug)
        return
    if n.label == "Domain":
        members = sorted(e.src for e in g.edges if e.rel == "IN_DOMAIN" and e.dst == slug)
        print("DOMAIN  %s  (%d pages)" % (n.domain, len(members)))
        print("  (provenance-trace expects a page or reference-note slug, not a domain)")
        return
    if n.label == "Source":
        citers = sorted(e.src for e in g.edges if e.rel == "CITES" and e.dst == slug)
        print("SOURCE  %s" % slug)
        print("  %s" % (n.title or ""))
        print("  version=%s primary=%s documentKind=%s" % (
            n.attrs.get("version"), n.attrs.get("primary"), n.attrs.get("documentKind")))
        if n.attrs.get("superseded_by"):
            print("  superseded by %s (a same-guide, strictly-newer reference note exists)" % n.attrs["superseded_by"])
        if n.attrs.get("source"):
            print("  url: %s" % n.attrs["source"])
        print("  cited by %d page(s):" % len(citers))
        for c in citers:
            print("    ← %s" % c)
        return
    # a synthesis page
    cites = sorted((e.dst, e.provenance, e.valid_from, e.valid_from_precision)
                   for e in g.edges if e.rel == "CITES" and e.src == slug)
    raw = n.attrs.get("sources_raw") or []
    nonkb = [t for t in raw if not t.startswith("kb:")]
    print("PAGE  %s  [%s, domain=%s]" % (slug, n.label, n.domain))
    if n.attrs.get("summary"):
        print("  %s" % n.attrs["summary"])
    print("  CITES → %d reference note(s) (resolved kb: tokens):" % len(cites))
    for dst, tok, vf, vp in cites:
        sn = g.nodes.get(dst)
        ver = sn.attrs.get("version") if sn else None
        dk = sn.attrs.get("documentKind") if sn else None
        temporal = ("  valid_from=%s [%s]" % (vf, vp)) if vf else ""
        sup = ("  superseded by %s" % sn.attrs["superseded_by"]) if sn and sn.attrs.get("superseded_by") else ""
        print("    → %-40s  (version=%s, %s)%s%s  via %s" % (dst, ver, dk, temporal, sup, tok))
    if nonkb:
        print("  unresolved provenance (not a graph edge — guide:/ref:/web:/note:):")
        for t in nonkb:
            print("    · %s" % t)
    # reverse: sibling pages that cite the same sources (reverse CITES index → O(cited) not O(all edges))
    cited = {c[0] for c in cites}
    if cited:
        rev = {}
        for e in g.edges:
            if e.rel == "CITES":
                rev.setdefault(e.dst, []).append(e.src)
        siblings = {}
        for dst in cited:
            for src in rev.get(dst, []):
                if src != slug:
                    siblings.setdefault(src, set()).add(dst)
        if siblings:
            print("  pages sharing a cited source (%d):" % len(siblings))
            for sib in sorted(siblings):
                print("    ~ %s  (shares %d)" % (sib, len(siblings[sib])))


def cmd_temporal(args):
    g = _load_or_build()
    vt = [e for e in g.edges if e.kind == model.VERSION_TEMPORAL]
    if not vt:
        print("TEMPORAL QUERY — no version-temporal edges in the store.")
        print("  No reference note met all three promotion gates (version present + documentKind=Documentation")
        print("  + a usable verified/errata-confirmed date in tkg/versions.py). Every edge is STRUCTURAL —")
        print("  honest, not fabricated. valid_from is None throughout; `updated:` is never a temporal signal.")
        return
    from wikikb.tkg import versions
    asof = None
    if args.as_of:
        asof = versions.resolve_asof(args.as_of)
        if asof is None:
            print("note: could not resolve --as-of %r to a usable (verified/errata-confirmed) date — unknown "
                  "version, ambiguous across families, or no usable date for it; showing all version-temporal "
                  "edges instead of a guessed slice." % args.as_of)
    rows, dropped_superseded = [], 0
    for e in vt:
        s = g.nodes.get(e.src)
        if args.domain and s and s.domain != args.domain:
            continue
        if asof and not (e.valid_from and e.valid_from <= asof):  # cumulative: authoritative by `asof`
            continue
        dn = g.nodes.get(e.dst)
        if args.current_only and dn and dn.attrs.get("superseded_by"):  # deterministic, no dates involved
            dropped_superseded += 1
            continue
        rows.append(e)
    scope = (" valid as of %s (%s)" % (args.as_of, asof)) if asof else ""
    print("TEMPORAL QUERY%s — %d edge(s) of %d version-temporal" % (scope, len(rows), len(vt)))
    print("  (valid_from precision is tagged; 'errata-confirmed' = a conservative lower bound from a public "
          "RHSA/RHEA errata, not an exact GA date — see tkg/versions.py)")
    if args.current_only:
        print("  --current-only: dropped %d edge(s) whose target reference note is superseded by a newer version"
              % dropped_superseded)
    for e in sorted(rows, key=lambda x: (x.valid_from or "", x.src, x.dst)):
        sn = g.nodes.get(e.dst)
        ver = sn.attrs.get("version") if sn else None
        sup = ("  superseded by %s" % sn.attrs["superseded_by"]) if sn and sn.attrs.get("superseded_by") else ""
        print("  %-36s →(CITES)→ %-30s  valid_from=%s [%s] (v%s)%s" % (
            e.src, e.dst, e.valid_from, e.valid_from_precision, ver, sup))


def main():
    ap = argparse.ArgumentParser(prog="wikikb tkg", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("ingest", help="build the graph from the vault → JSON store")
    p.add_argument("--stdout", action="store_true", help="dump JSON to stdout instead of writing the store")
    p.add_argument("--backend", action="store_true",
                   help="also load into the optional Kuzu backend (requires WIKI_TKG set + kuzu installed)")
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("graph-status", help="node/edge/domain health snapshot")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("cross-domain-query", help="LINKS_TO edges spanning two domains")
    p.add_argument("--from", dest="from_", default=None, help="restrict source domain")
    p.add_argument("--to", dest="to", default=None, help="restrict target domain")
    p.add_argument("--version", default=None, help="(Phase 4) filter to edges valid at a version")
    p.set_defaults(func=cmd_cross_domain)

    p = sub.add_parser("provenance-trace", help="what a page rests on / what rests on a source")
    p.add_argument("slug", help="a page slug or a reference-note (Source) slug")
    p.set_defaults(func=cmd_provenance)

    p = sub.add_parser("temporal-query", help="(Phase 4) edges valid as of a version/date")
    p.add_argument("--as-of", dest="as_of", default=None, help="version or ISO date")
    p.add_argument("--domain", default=None, help="restrict to a domain")
    p.add_argument("--current-only", dest="current_only", action="store_true",
                   help="drop edges whose target reference note is superseded by a newer version")
    p.set_defaults(func=cmd_temporal)

    args = ap.parse_args()
    if not getattr(args, "func", None):
        ap.print_help()
        sys.exit(2)
    args.func(args)


if __name__ == "__main__":
    main()
