#!/usr/bin/env python3
"""model.py — deterministic builder: the Obsidian vault → a normalized temporal knowledge graph.

stdlib only, NO LLM, NO network. Every edge comes from exactly one of two deterministic sources that
already exist in the vault — so the graph is reproducible byte-for-byte from the same vault state:

  * LINKS_TO  — page→page, from `[[wikilinks]]` in page bodies (mirrors `expand.PAGELINK_RE`; the
                crosslink-generated `## Sources` block is stripped first so its `[[note|Title]]` links
                are NOT counted as page links).
  * CITES     — page→Source(reference note), resolved with `crosslink.resolve()` of each `kb:` token —
                the SAME resolver `crosslink.py` uses to write `## Sources` (primary/newest version wins).
                Non-`kb:` tokens (guide:/ref:/web:/note:) don't map 1:1 to a reference note; they are
                recorded on the Page node as `sources_raw` (surfaced by `provenance-trace`) — never
                silently dropped, never turned into an edge.
  * IN_DOMAIN — page→Domain, a straight `domain:` frontmatter read.

TEMPORAL HONESTY (rules R1/R2/R4):
  * A Source node's version metadata (`version` / `primary` / `documentKind`) is read EXCLUSIVELY from
    the immutable `reference/<domain>/` note frontmatter, behind `_ref_frontmatter()` which ASSERTS the
    path is under `reference/`. A synthesis page (the only file carrying `updated:`) is read solely for
    its Page node, its `[[links]]`, and its `sources:` tokens. `valid_from` is therefore structurally
    unreachable from `updated:` — not by convention, by an assertion at build time.
  * In Phase 3 EVERY edge is STRUCTURAL: `valid_from = valid_until = None`. Phase 4 promotes a CITES
    edge to VERSION-TEMPORAL only when ALL hold: `note.version is not None` AND
    `documentKind == 'Documentation'` AND `tkg.versions` returns a *usable* (verified or errata-confirmed)
    release date. Absent any
    of those it stays STRUCTURAL (graceful temporal degradation — never fabricate a date). `valid_until`
    is hardcoded None: supersession is never inferred from version succession.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field, asdict  # noqa: F401  (asdict re-used by store)
from typing import Dict, List, Optional

from wikikb import paths
from wikikb.build import crosslink  # reuse the EXACT kb:→reference-note resolver (R3: no re-implementation)

try:                                # the temporal registry is the ONLY source of valid_from (rule R1).
    from wikikb.tkg import versions  # stdlib-only data module; the builder still works (all edges
except ImportError:                 # STRUCTURAL) if versions.py is ABSENT — graceful degradation. Note we
    versions = None                 # catch ONLY ImportError: a real error INSIDE versions.py (e.g. a typo in
    #                                 RELEASES) must propagate loudly, not silently drop every temporal edge.

WIKI = str(paths.WIKI)
REF = str(paths.REFERENCE)
PAGE_DIRS = ("topics", "entities", "questions")

# Mirror expand.py exactly so LINKS_TO matches the retrieval graph: bare [[page-slug]] only (no pipe).
# The generated `## Sources` block is excised before scanning by reusing crosslink.SECTION_RE — the SAME
# anchored regex crosslink.py writes/strips with (re.escape'd BEGIN/END), so the two can never drift.
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
PAGELINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)\]\]")

TYPE_TO_LABEL = {"entity": "Entity", "topic": "Topic", "question": "Question"}
DOMAIN_PREFIX = "domain::"  # Domain node ids are namespaced so they can't collide with a page/source slug

STRUCTURAL = "structural"
VERSION_TEMPORAL = "version-temporal"


@dataclass
class WikiNode:
    """A single node kind (the user's WikiNode) carrying one of five labels.

    label ∈ {Entity, Topic, Question} for synthesis pages (by frontmatter `type:`),
            Source for a cited reference note, Domain for a `domain:` value.
    """
    id: str
    label: str
    domain: Optional[str]
    title: str
    attrs: Dict = field(default_factory=dict)


@dataclass
class WikiEdge:
    src: str
    dst: str
    rel: str                       # LINKS_TO | CITES | IN_DOMAIN
    kind: str = STRUCTURAL         # structural | version-temporal
    valid_from: Optional[str] = None   # ISO date, ONLY from versions.release_date() (rule R1); else None
    valid_until: Optional[str] = None  # hardcoded None — never inferred from version succession
    valid_from_precision: Optional[str] = None  # verified | errata-confirmed — so approximate≠exact is visible
    provenance: str = ""           # "wikilink" | the kb:/… token | "domain"


@dataclass
class WikiGraph:
    nodes: Dict[str, WikiNode]
    edges: List[WikiEdge]
    meta: Dict = field(default_factory=dict)


def _top_fields(block: str) -> Dict[str, str]:
    """Top-level scalar frontmatter fields (delegates to crosslink's parser for parity)."""
    return crosslink.top_fields(block)


def _successor_slug(cands: List[Dict], family: Optional[str], version: Optional[str]) -> Optional[str]:
    """The highest-version SAME-FAMILY candidate under this url_tail whose version is STRICTLY higher
    than `version`, or None. Same url_tail + same family + strictly higher version identifies the
    successor as FACT (rule R3) — deterministic (sorted by (vkey, slug)), no dates, no inference.
    None means the cited note is current (nothing supersedes it), the common case since crosslink.resolve
    already prefers the primary/newest note — this fires only when `primary` lags a newer harvest."""
    mv = crosslink.vkey(version or "")
    fam = (family or "").strip().lower()
    newer = [c for c in cands
             if (c.get("family") or "").strip().lower() == fam and crosslink.vkey(c["version"]) > mv]
    if not newer:
        return None
    return sorted(newer, key=lambda c: (crosslink.vkey(c["version"]), c["slug"]))[-1]["slug"]


def _ref_frontmatter(domain: str, slug: str, cache: Dict) -> Dict[str, str]:
    """Frontmatter of a reference/<domain>/<slug>.md note — the ONLY sanctioned source of temporal
    metadata (rule R2). Asserts the path is under reference/ so no synthesis page (which carries
    `updated:`) can ever feed this path."""
    key = (domain, slug)
    if key in cache:
        return cache[key]
    path = os.path.join(REF, domain or "", slug + ".md")
    ap, aref = os.path.abspath(path), os.path.abspath(REF)
    if os.path.commonpath([ap, aref]) != aref:   # explicit raise: an `assert` vanishes under `python -O`
        raise AssertionError(
            "R2 violation: temporal metadata must be read from reference/ only, not %r" % path)
    fm: Dict[str, str] = {}
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as fh:
            m = FM_RE.match(fh.read())
        if m:
            fm = _top_fields(m.group(1))
    cache[key] = fm
    return fm


def build_graph() -> WikiGraph:
    """Walk the vault and assemble the structural graph. Deterministic: fixed dir order, sorted listings,
    sorted link targets, stable de-dup."""
    idx = crosslink.build_ref_index()         # domain -> url_tail -> [reference-note candidates]
    refcache: Dict = {}
    nodes: Dict[str, WikiNode] = {}
    edges: List[WikiEdge] = []
    seen_edges = set()                         # (src, dst, rel) — first wins

    def add_edge(src, dst, rel, provenance, kind=STRUCTURAL, valid_from=None, valid_from_precision=None):
        k = (src, dst, rel)
        if k in seen_edges:
            return
        seen_edges.add(k)
        edges.append(WikiEdge(src=src, dst=dst, rel=rel, kind=kind, valid_from=valid_from,
                              valid_until=None,  # valid_until: always None (R4 — no supersession inference)
                              valid_from_precision=valid_from_precision, provenance=provenance))

    # Pass 1 — Page nodes, Domain nodes, IN_DOMAIN edges. Record each page's raw frontmatter block + text.
    pages: Dict[str, Dict] = {}
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if not fn.endswith(".md") or fn == "README.md":
                continue
            slug = fn[:-3]
            with open(os.path.join(full, fn), encoding="utf-8") as fh:
                text = fh.read()
            m = FM_RE.match(text)
            if not m:
                continue
            block = m.group(1)
            fm = _top_fields(block)
            domain = fm.get("domain")
            label = TYPE_TO_LABEL.get((fm.get("type") or "").strip(), "Entity")
            sources_raw = crosslink.source_tokens(block)
            nodes[slug] = WikiNode(
                id=slug, label=label, domain=domain, title=fm.get("title") or slug,
                attrs={"type": fm.get("type"), "status": fm.get("status"),
                       "summary": fm.get("summary") or "", "sources_raw": sources_raw},
            )
            if domain:
                dom_id = DOMAIN_PREFIX + domain
                if dom_id not in nodes:
                    nodes[dom_id] = WikiNode(id=dom_id, label="Domain", domain=domain, title=domain, attrs={})
                add_edge(slug, dom_id, "IN_DOMAIN", "domain")
            # Keep the source tokens parsed here (reused in Pass 2 — no second source_tokens() call).
            pages[slug] = {"domain": domain, "text": text, "tokens": sources_raw}

    known_pages = set(pages)

    # Pass 2 — LINKS_TO (page→page) and CITES (page→Source). Needs the full page set first.
    for slug in sorted(pages):
        info = pages[slug]
        domain, text = info["domain"], info["text"]
        # LINKS_TO: strip the generated ## Sources block AND the frontmatter (so source_notes:/tags: links
        # aren't miscounted), then scan body for bare [[page-slug]] pointing at a KNOWN page.
        body = crosslink.SECTION_RE.sub("", text)
        body = FM_RE.sub("", body, count=1)
        for tgt in sorted(set(PAGELINK_RE.findall(body))):
            if tgt != slug and tgt in known_pages:
                add_edge(slug, tgt, "LINKS_TO", "wikilink")
        # CITES: resolve each kb: token via the canonical crosslink resolver; non-kb tokens stay in
        # sources_raw on the Page node (already recorded) — surfaced by provenance-trace, never an edge.
        for tok in info["tokens"]:
            r = crosslink.resolve(tok, domain, idx)
            if not r:
                continue
            src_slug = r["slug"]
            existing = nodes.get(src_slug)
            if existing is not None and existing.label != "Source":
                # A reference-note slug equals a synthesis-page slug. Slugs are required globally unique
                # across pages + reference notes; silently overwriting one with the other would corrupt the
                # graph. Fail loud (the project's "fail the build, never corrupt" rule) instead of guessing.
                raise SystemExit(
                    "tkg: slug collision — %r is both a %s page and a reference note; "
                    "rename one (slugs must be globally unique across pages and reference notes)"
                    % (src_slug, existing.label))
            if existing is None:                                   # build the Source node once (idempotent)
                fm_ref = _ref_frontmatter(domain, src_slug, refcache)  # reference/ ONLY (R2 asserted)
                # Supersession (rule R3, deterministic): does a same-tail, same-family, strictly-newer
                # reference note exist? tok is a kb: token (non-kb resolve to None → `continue` above).
                tail = crosslink.url_tail(tok[len("kb:"):]).rstrip("-")
                succ = _successor_slug((idx.get(domain) or {}).get(tail) or [],
                                       fm_ref.get("family"), fm_ref.get("version"))
                nodes[src_slug] = WikiNode(
                    id=src_slug, label="Source", domain=domain, title=r.get("title") or src_slug,
                    attrs={
                        "version": fm_ref.get("version") or None,
                        "primary": str(fm_ref.get("primary", "")).lower() == "true",
                        "documentKind": fm_ref.get("documentKind") or None,
                        "family": fm_ref.get("family") or None,
                        "source": fm_ref.get("source") or None,
                        "superseded_by": succ,  # node attr only — NEVER valid_until (R4: no supersession inference on edges)
                    },
                )
            # VERSION-TEMPORAL promotion (rule R4) — a THREE-condition opt-in, every condition a hard gate:
            #   1. the reference note carries a structured `version:` (not None — never body prose),
            #   2. it is documentKind=Documentation (a chapter that DESCRIBES behavior at that version; a
            #      Solution/Article note's version is an applicability tag, not a product-introduction date),
            #   3. versions.release_date() returns a VERIFIED date (else None ⇒ stays structural).
            # Any gate failing ⇒ STRUCTURAL with valid_from=None. valid_until is never set (no supersession
            # inference). `updated:` cannot reach this branch — `vf` comes only from the registry.
            sn = nodes[src_slug]
            vf = vp = None
            if versions is not None and sn.attrs.get("version") is not None \
                    and sn.attrs.get("documentKind") == "Documentation":
                vf, vp = versions.release_info(sn.attrs.get("family"), sn.attrs.get("version"))
            add_edge(slug, src_slug, "CITES", tok,
                     kind=(VERSION_TEMPORAL if vf else STRUCTURAL), valid_from=vf, valid_from_precision=vp)

    label_counts: Dict[str, int] = {}
    for n in nodes.values():
        label_counts[n.label] = label_counts.get(n.label, 0) + 1
    rel_counts: Dict[str, int] = {}
    for e in edges:
        rel_counts[e.rel] = rel_counts.get(e.rel, 0) + 1
    vt = sum(1 for e in edges if e.kind == VERSION_TEMPORAL)
    meta = {
        "schema": "wikikb-tkg/1",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "labels": label_counts,
        "relations": rel_counts,
        "version_temporal_edges": vt,
        "note": ("All edges STRUCTURAL (valid_from=None) — no sourced version dates promoted them."
                 if vt == 0 else
                 "%d CITES edge(s) promoted to VERSION-TEMPORAL from sourced release dates (precision "
                 "tagged per edge — see tkg/versions.py); valid_until is never set (no supersession "
                 "inference)." % vt),
    }
    return WikiGraph(nodes=nodes, edges=edges, meta=meta)


def cross_domain_edges(graph: WikiGraph):
    """LINKS_TO edges whose endpoints are pages in different domains — the cross-domain bridges."""
    out = []
    for e in graph.edges:
        if e.rel != "LINKS_TO":
            continue
        s, d = graph.nodes.get(e.src), graph.nodes.get(e.dst)
        if s and d and s.domain and d.domain and s.domain != d.domain:
            out.append(e)
    return out
