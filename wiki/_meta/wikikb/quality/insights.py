#!/usr/bin/env python3
"""insights.py — graph insights over the wiki's link graph (the offline, stdlib transfer of
nashsu/llm_wiki's "4-signal graph + Louvain communities + knowledge-gap insights").

Karpathy-pattern wikis compile a *graph* (pages cross-linked with [[wikilinks]] + `## Sources`
citations). This tool reads that graph straight from the vault — no LLM, no network, no third-party
dep — and surfaces three things a flat page list can't:

  1. COMMUNITIES   — clusters of tightly-linked pages (deterministic label propagation), each tagged
                     with its dominant domain. Shows how the knowledge self-organizes.
  2. KNOWLEDGE GAPS— under-connected pages (degree ≤1), and per-domain UNCITED reference-corpus
                     (notes no synthesis page links) — e.g. openshift's harvested corpus that the
                     6 synthesis pages barely touch. This is the "what to write next" list.
  3. SUGGESTED LINKS — non-adjacent page pairs with high Adamic-Adar score (shared neighbors): pages
                     the graph thinks SHOULD be linked but aren't (nashsu's "surprising connections").

Deterministic (sorted iteration, no randomness — the wiki bans Math.random for golden-stability) so
the output is stable run-to-run. Reads only `topics/ entities/ questions/` + `reference/<domain>/`.

    python3 -m wikikb insights                 # full report
    python3 -m wikikb insights --domain openshift
    python3 -m wikikb insights --json
"""
import argparse
import json
import math
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
sys.dont_write_bytecode = True

PAGE_DIRS = ("topics", "entities", "questions")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")


def _fm(text):
    m = FM_RE.match(text)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
            if mm:
                out.setdefault(mm.group(1), mm.group(2).strip().strip("\"'"))
    return out


def load_pages():
    """slug -> {domain, type, links:set, cites:set} from the synthesis tier."""
    pages = {}
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if not fn.endswith(".md"):
                continue
            slug = fn[:-3]
            text = open(os.path.join(full, fn), encoding="utf-8", errors="replace").read()
            fm = _fm(text)
            body = FM_RE.sub("", text, count=1)
            links = set(t.strip() for t in WIKILINK_RE.findall(body))
            pages[slug] = {"domain": fm.get("domain") or "?", "type": fm.get("type") or d[:-1],
                           "targets": links}
    return pages


def reference_slugs():
    """domain -> set(reference-note slugs) (the corpus tier; excludes generated _* hubs)."""
    out = {}
    refroot = os.path.join(WIKI, "reference")
    if not os.path.isdir(refroot):
        return out
    for dom in sorted(os.listdir(refroot)):
        dd = os.path.join(refroot, dom)
        if os.path.isdir(dd):
            out[dom] = set(f[:-3] for f in os.listdir(dd)
                           if f.endswith(".md") and not f.startswith("_"))
    return out


def build_graph(pages):
    """Undirected page↔page adjacency over [[wikilinks]] that resolve to another page (the synthesis
    graph used for communities + suggestions). Citations to reference notes are tracked separately."""
    slugs = set(pages)
    adj = {s: set() for s in slugs}
    for s, p in pages.items():
        for t in p["targets"]:
            if t in slugs and t != s:
                adj[s].add(t)
                adj[t].add(s)
    return adj


def communities(adj):
    """Deterministic async label-propagation. Each node starts in its own community; in sorted order
    each node adopts the most common label among its neighbors (ties broken by smallest label). Repeat
    until stable. Returns label -> sorted[members]."""
    label = {n: n for n in adj}
    for _ in range(50):
        changed = False
        for n in sorted(adj):
            if not adj[n]:
                continue
            counts = {}
            for m in adj[n]:
                counts[label[m]] = counts.get(label[m], 0) + 1
            best = min(sorted(counts), key=lambda lbl: (-counts[lbl], lbl))
            if label[n] != best:
                label[n] = best
                changed = True
        if not changed:
            break
    comm = {}
    for n, lbl in label.items():
        comm.setdefault(lbl, []).append(n)
    return {lbl: sorted(members) for lbl, members in comm.items()}


def adamic_adar(adj, pages, topn=15):
    """Suggest links: for non-adjacent page pairs, AA = Σ 1/log(deg(w)) over shared neighbors w.
    High AA + not linked = the graph expects a link. Cross-domain pairs are highlighted."""
    scores = {}
    nodes = sorted(adj)
    for i, a in enumerate(nodes):
        for w in adj[a]:                       # shared-neighbor pairs only (sparse, cheap)
            dw = len(adj[w])
            if dw < 2:
                continue
            contrib = 1.0 / math.log(dw)
            for b in adj[w]:
                if b <= a or b in adj[a]:       # ordered pairs, skip already-linked
                    continue
                scores[(a, b)] = scores.get((a, b), 0.0) + contrib
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:topn]
    return [{"a": a, "b": b, "score": round(sc, 3),
             "cross_domain": pages[a]["domain"] != pages[b]["domain"]} for (a, b), sc in ranked]


def analyze(domain=None):
    pages = load_pages()
    # NB: we always build the graph over ALL pages so cross-domain signals survive a --domain
    # scope; the scoping is applied per-section below (corpus_gap, thin, communities).
    adj = build_graph(pages)
    comm = communities(adj)
    refs = reference_slugs()

    # citations: which reference notes does any synthesis page link?
    cited = set()
    for p in pages.values():
        cited |= p["targets"]
    corpus_gap = {}
    for dom, slugs in refs.items():
        if domain and dom != domain:
            continue
        uncited = len(slugs - cited)
        corpus_gap[dom] = {"corpus": len(slugs), "cited": len(slugs) - uncited, "uncited": uncited}

    # under-connected synthesis pages
    scope = [s for s in adj if (not domain or pages[s]["domain"] == domain)]
    thin = sorted((s for s in scope if len(adj[s]) <= 1),
                  key=lambda s: (len(adj[s]), s))

    # community summary (dominant domain per cluster, size ≥3)
    csum = []
    for lbl, members in comm.items():
        ms = [m for m in members if not domain or pages[m]["domain"] == domain]
        if len(ms) < 3:
            continue
        doms = {}
        for m in ms:
            doms[pages[m]["domain"]] = doms.get(pages[m]["domain"], 0) + 1
        dom = max(sorted(doms), key=lambda d: doms[d])
        csum.append({"size": len(ms), "domain": dom, "anchor": ms[0], "members": ms})
    csum.sort(key=lambda c: (-c["size"], c["anchor"]))

    return {"pages": len(pages), "edges": sum(len(v) for v in adj.values()) // 2,
            "communities": csum, "corpus_gap": corpus_gap, "thin": thin,
            "suggested_links": adamic_adar(adj, pages)}


def report(r):
    print("=" * 78)
    print("WIKI GRAPH INSIGHTS — %d pages, %d page↔page links" % (r["pages"], r["edges"]))
    print("=" * 78)

    print("\n## COMMUNITIES (clusters of tightly-linked pages)")
    for c in r["communities"][:12]:
        print("  [%2d pages · %-16s] %s%s" % (c["size"], c["domain"], c["anchor"],
              ("  +%d more" % (c["size"] - 1)) if c["size"] > 1 else ""))

    print("\n## KNOWLEDGE GAPS — uncited reference corpus (write synthesis that cites these)")
    for dom, g in sorted(r["corpus_gap"].items(), key=lambda kv: -kv[1]["uncited"]):
        pct = (100.0 * g["cited"] / g["corpus"]) if g["corpus"] else 0
        print("  %-18s %5d notes · %4d cited (%4.1f%%) · %5d UNCITED" %
              (dom, g["corpus"], g["cited"], pct, g["uncited"]))

    print("\n## UNDER-CONNECTED PAGES (degree ≤1 — orphans/stubs to wire in)")
    print("  " + (", ".join(r["thin"][:20]) or "(none)") + (" …" if len(r["thin"]) > 20 else ""))

    print("\n## SUGGESTED LINKS (high shared-neighbor score, not yet linked)")
    for s in r["suggested_links"]:
        tag = " [cross-domain]" if s["cross_domain"] else ""
        print("  %5.2f  [[%s]] ↔ [[%s]]%s" % (s["score"], s["a"], s["b"], tag))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", help="scope gaps/communities to one domain")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    r = analyze(args.domain)
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        report(r)


if __name__ == "__main__":
    main()
