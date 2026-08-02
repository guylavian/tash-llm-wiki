"""Export the curated TKG into Graphify's graph.json schema.

Bridges Obsidian → Graphify: instead of Graphify re-extracting markdown
headings (structural noise), its query/path/explain CLI and graph.html run
over the wiki's *curated* semantic graph — [[wikilink]] edges (LINKS_TO)
and provenance edges (CITES) built by crosslink/tkg ingest.

Deliberately excluded: IN_DOMAIN edges and Domain nodes (god-nodes with
degree 69–178 that flood any traversal — `domain` stays as a node
attribute for filtering), and heading/section nodes (pages are the unit
of retrieval, matching the wiki's page-per-concept contract).

Usage:  python3 -m wikikb.tkg.graphify_export   (after `wikikb tkg ingest`)
Output: <wiki>/graphify-out/graph.json — then optionally
        `graphify cluster-only <wiki> --no-label` for communities/report/viz.
"""
import json

from wikikb.paths import META, WIKI

STORE = META / "tkg" / "graph.json"
OUT = WIKI / "graphify-out" / "graph.json"

PAGE_DIR = {"topic": "topics", "entity": "entities", "question": "questions"}


def main():
    d = json.loads(STORE.read_text(encoding="utf-8"))
    nodes, links = [], []
    for n in d["nodes"]:
        if n["label"] == "Domain":
            continue
        a = n.get("attrs", {})
        if n["label"] == "Source":
            path = "reference/%s/%s.md" % (n["domain"], n["id"])
        elif a.get("type") in PAGE_DIR:
            path = "%s/%s.md" % (PAGE_DIR[a["type"]], n["id"])
        else:
            # ponytail: malformed page missing type:/domain: frontmatter (schema
            # violation upstream, e.g. questions/kubernetes-preferred-zone-...) —
            # skip rather than crash the whole export; fix the page's frontmatter
            # to recover it.
            print("SKIP node with missing/unknown type: %s" % n["id"])
            continue
        node = {
            "id": n["id"], "label": n.get("title") or n["id"],
            "norm_label": n["id"], "file_type": "document",
            "source_file": path, "source_location": "L1", "_origin": "wikikb-tkg",
            "kind": n["label"].lower(), "domain": n.get("domain"),
        }
        if a.get("summary"):
            node["summary"] = a["summary"]
        if a.get("version"):
            node["version"] = a["version"]
        nodes.append(node)
    kept = {n["id"] for n in nodes}
    for e in d["edges"]:
        if e["rel"] == "IN_DOMAIN" or e["src"] not in kept or e["dst"] not in kept:
            continue
        link = {
            "relation": "cites" if e["rel"] == "CITES" else "references",
            "confidence": "EXTRACTED", "confidence_score": 1.0, "weight": 1.0,
            "source": e["src"], "target": e["dst"],
            "source_file": "", "source_location": "",
        }
        if e.get("valid_from"):
            link["valid_from"] = e["valid_from"]
        links.append(link)
    out = {
        "directed": True, "multigraph": False,
        "graph": {"name": "wiki-tkg", "schema": d.get("schema")},
        "nodes": nodes, "links": links, "hyperedges": [],
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print("WROTE %s — %d nodes / %d links (curated: references+cites only)"
          % (OUT, len(nodes), len(links)))


if __name__ == "__main__":
    main()
