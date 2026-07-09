#!/usr/bin/env python3
"""gate_page_probe.py — verify the PAGE-LEVEL arm of the Confidence gate. stdlib only.

FAITHFUL: imports lint.py and calls lint.page_gate_verdict() — the SAME rule lint
enforces — so the probe can NOT drift from enforcement (as eval.py imports kb.py).

Tests GATE BEHAVIOUR (does the provenance arm flag a page), NOT answer-correctness — so
it is O(1) per page and never needs to know the "right answer" to a question. The
negative (clean) case is the calibration proof: without it the probe only shows
over-eager firing, not correctness.

Cases: _meta/eval/gate_page_cases.jsonl  {page, expect ∈ {flag, clean}, why}

Also probes the B1 fix (PLAN-graphify-pdf-upload.md Phase 3 item 1): that the PUBLIC
`ask()`/`run_query` path actually THREADS a candidate page's real frontmatter into
gate_node, instead of the pre-fix docstring's `page_fm={}` placeholder under which only
H1 could ever fire. See probe_wiring_reads_real_pages() / probe_run_query_gate() below.

Exit: 0 all pass · 1 a case failed (CI gate) · 2 bad input.

Usage:
    python3 wiki/_meta/tests/gate_page_probe.py
    python3 wiki/_meta/tests/gate_page_probe.py --cases _meta/eval/gate_page_cases.jsonl
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
WIKI = os.path.dirname(META)                            # wiki
sys.dont_write_bytecode = True
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable
from wikikb.quality import lint  # faithful: reuse the real frontmatter parser AND the gate rule


def verdict(page_path):
    """('flag'|'clean', reasons) for a page, via the exact rule lint enforces."""
    with open(page_path, encoding="utf-8") as fh:
        fm = lint.parse_frontmatter(fh.read())
    if fm is None:
        return "flag", ["no frontmatter"]
    reasons = lint.page_gate_verdict(fm)
    return ("flag" if reasons else "clean"), reasons


def probe_wiring_reads_real_pages():
    """B1 sanity: nodes.expand_node (UNPATCHED) actually reads real on-disk page frontmatter for a
    real query into state['page_fm'] — proves the file-reading wiring, not just gate_node's math."""
    from wikikb.graph import nodes
    st = {"domain": "keycloak", "query": "ldap user federation truststore", "k": 5}
    st.update(nodes.route_node(st))
    st.update(nodes.retrieve_node(st))
    st.update(nodes.expand_node(st))
    fms = st.get("page_fm")
    ok = isinstance(fms, list) and len(fms) > 0 and all(isinstance(fm, dict) and fm.get("slug") for fm in fms)
    reasons = ["slugs=%s" % [fm.get("slug") for fm in fms]] if isinstance(fms, list) else ["page_fm=%r" % (fms,)]
    return ok, reasons


def _fixture_fm(status=None, extracted=None, inferred=0, slug="probe-fixture"):
    """Fabricate an in-memory fm dict in the SAME flat-key shape lint.parse_frontmatter produces —
    no file write, mirroring how selftest.py's BF-4 check (#27) fabricates page_fm dicts directly
    for lint.gate_banner. Used to force H4 (no real needs-review page exists in the wiki today)."""
    fm = {"slug": slug, "domain": "keycloak"}
    if status is not None:
        fm["status"] = status
    if extracted is not None:
        fm["provenance_extracted"] = str(extracted)
        fm["provenance_inferred"] = str(inferred)
    return fm


def probe_run_query_gate():
    """B1 regression guard: the PUBLIC ask() path (== run_query when langgraph is installed; the
    same linear node sequence when it's absent, as it is here) now yields H2 AND H4 banner lines for
    pages with extracted==0 / status: needs-review — not just H1. `nodes.expand_node` is monkeypatched
    to hand back one REAL on-disk fixture (extracted==0 via the reviewed-no-provenance gate-hole
    fixture already used by the JSONL cases above) plus one FABRICATED needs-review fm (no real page
    like that exists yet) — proving gate_node's per-page union fires BOTH without a clean page in the
    same list masking either (the approved multi-page decision)."""
    from wikikb.graph import nodes
    from wikikb.graph import ask as ask_mod

    fixture_path = os.path.join(WIKI, "_meta", "eval", "fixtures", "reviewed-no-provenance.md")
    with open(fixture_path, encoding="utf-8") as fh:
        h2_fm = lint.parse_frontmatter(fh.read())
    h4_fm = _fixture_fm(status="needs-review", extracted=5, slug="probe-fixture-h4")

    real_expand_node = nodes.expand_node

    def _fake_expand_node(state):
        out = real_expand_node(state)          # still exercises the real retrieval/expand plumbing
        out["page_fm"] = [h2_fm, h4_fm]         # override with the fixtures under test (no content write)
        return out

    nodes.expand_node = _fake_expand_node
    try:
        st = ask_mod.ask("ldap user federation truststore", domain="keycloak")
    finally:
        nodes.expand_node = real_expand_node    # always restore, even on assertion/exception

    banner = st.get("banner") or []
    has_h2 = any("extracted==0" in b for b in banner)
    has_h4 = any("(H4)" in b for b in banner)
    ok = has_h2 and has_h4
    return ok, ["orchestrator=%s" % st.get("orchestrator"), "banner=%s" % banner]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default=os.path.join(WIKI, "_meta", "eval", "gate_page_cases.jsonl"))
    args = ap.parse_args()

    path = args.cases if os.path.isabs(args.cases) else os.path.join(WIKI, args.cases)
    if not os.path.isfile(path):
        print("cases file not found: %s" % path)
        sys.exit(2)

    cases = []
    with open(path, encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as e:
                print("bad JSON at line %d: %s" % (ln, e))
                sys.exit(2)

    print("=" * 82)
    print("CONFIDENCE-GATE PROBE — page-level (provenance) arm  (%d cases)" % len(cases))
    print("rule: lint.page_gate_verdict() — H2 extracted==0, H3 reviewed AND inferred>=extracted")
    print("=" * 82)

    fails = []
    for c in cases:
        pg = os.path.join(WIKI, c["page"])
        if not os.path.isfile(pg):
            fails.append(c)
            print("  FAIL  %-48s — page not found" % c["page"])
            continue
        v, reasons = verdict(pg)
        ok = (v == c["expect"])
        if not ok:
            fails.append(c)
        print("  %s  %-48s => %-6s (expect %-6s)" % ("PASS" if ok else "FAIL", c["page"], v, c["expect"]))
        if reasons:
            print("          fired: %s" % "; ".join(reasons))
    print("-" * 82)
    print("%d/%d passed%s" % (len(cases) - len(fails), len(cases),
                              "" if not fails else "  — FAILURES ABOVE"))

    print("=" * 82)
    print("B1 WIRING PROBE — page_fm threaded into the live ask()/run_query path")
    print("=" * 82)
    wiring_fails = 0
    for name, fn in (("wiring reads real seed-page frontmatter", probe_wiring_reads_real_pages),
                     ("run_query/ask() yields H2+H4 (multi-page union)", probe_run_query_gate)):
        try:
            ok, reasons = fn()
        except Exception as e:                          # noqa: BLE001 — a probe crash is still a FAIL, not a hang
            ok, reasons = False, ["raised %r" % e]
        if not ok:
            wiring_fails += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        for r in reasons:
            print("          %s" % r)
    print("-" * 82)
    print("%d/2 passed%s" % (2 - wiring_fails, "" if not wiring_fails else "  — FAILURES ABOVE"))

    sys.exit(1 if (fails or wiring_fails) else 0)


if __name__ == "__main__":
    main()
