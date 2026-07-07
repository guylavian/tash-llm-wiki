"""Render the TKG JSON store into a self-contained interactive graph.html.

Usage:  python3 -m wikikb.tkg.viewer          (after `wikikb tkg ingest`)
Output: _meta/tkg/graph.html — open in a browser. Graph data is embedded;
the only external fetch is the vis-network library from a CDN (view needs
a browser with internet; the wiki toolchain itself stays offline).
"""
import json

from wikikb.paths import META

STORE = META / "tkg" / "graph.json"
OUT = META / "tkg" / "graph.html"

DOMAIN_COLORS = {
    "keycloak": "#c0392b", "active-directory": "#2c5fb3",
    "cisco-ios-xe": "#3a8c2c", "openshift": "#7d3ac0",
}
REL_COLORS = {"LINKS_TO": "#888", "CITES": "#c9a227", "IN_DOMAIN": "#ddd"}

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Wiki TKG — %(counts)s</title>
<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
 body{margin:0;font:13px sans-serif} #net{width:100vw;height:100vh}
 #bar{position:fixed;top:8px;left:8px;background:#fffd;padding:8px 12px;border-radius:6px;
      box-shadow:0 1px 4px #0003;z-index:9}
 #bar label{margin-right:10px} input[type=search]{width:220px}
</style></head><body>
<div id="bar">
 <b>Wiki TKG</b> · %(counts)s ·
 <label><input type="checkbox" id="cites" checked> CITES (KB)</label>
 <label><input type="checkbox" id="links" checked> LINKS_TO</label>
 <label><input type="checkbox" id="src" checked> Source nodes</label>
 <input type="search" id="q" placeholder="find node…">
</div>
<div id="net"></div>
<script>
const NODES=%(nodes)s, EDGES=%(edges)s;
const nodes=new vis.DataSet(NODES), edges=new vis.DataSet(EDGES);
const net=new vis.Network(document.getElementById('net'),{nodes,edges},{
 physics:{solver:'forceAtlas2Based',stabilization:{iterations:120}},
 nodes:{shape:'dot',font:{size:11}}, edges:{smooth:false,color:{inherit:false}},
 interaction:{hover:true}});
function refilter(){
 const c=document.getElementById('cites').checked, l=document.getElementById('links').checked,
       s=document.getElementById('src').checked;
 nodes.update(NODES.map(n=>({id:n.id,hidden:n.group==='Source'&&!s})));
 edges.update(EDGES.map(e=>({id:e.id,hidden:(e.rel==='CITES'&&(!c||!s))||(e.rel==='LINKS_TO'&&!l)})));
}
['cites','links','src'].forEach(id=>document.getElementById(id).onchange=refilter);
document.getElementById('q').onchange=ev=>{
 const hit=NODES.find(n=>n.id.includes(ev.target.value));
 if(hit){net.focus(hit.id,{scale:1.5,animation:true});net.selectNodes([hit.id]);}
};
</script></body></html>
"""


def main():
    d = json.loads(STORE.read_text(encoding="utf-8"))
    nodes, edges = [], []
    for n in d["nodes"]:
        color = DOMAIN_COLORS.get(n.get("domain"), "#555")
        size = {"Domain": 30, "Topic": 16, "Source": 6}.get(n["label"], 10)
        nodes.append({
            "id": n["id"], "label": "" if n["label"] == "Source" else n["id"],
            "group": n["label"], "size": size,
            "color": "#bbb" if n["label"] == "Source" else color,
            "title": "%s · %s · %s" % (n["label"], n.get("domain", ""), n.get("title", n["id"])),
        })
    for i, e in enumerate(d["edges"]):
        edges.append({
            "id": i, "from": e["src"], "to": e["dst"], "rel": e["rel"],
            "color": REL_COLORS.get(e["rel"], "#888"),
            "dashes": e["kind"] == "version-temporal",
            "title": e["rel"] + (" · from %s (%s)" % (e["valid_from"], e["valid_from_precision"])
                                 if e["valid_from"] else ""),
        })
    counts = "%d nodes / %d edges" % (len(nodes), len(edges))
    OUT.write_text(TEMPLATE % {"counts": counts,
                               "nodes": json.dumps(nodes), "edges": json.dumps(edges)},
                   encoding="utf-8")
    print("WROTE %s  (%s) — open it in a browser" % (OUT, counts))


if __name__ == "__main__":
    main()
