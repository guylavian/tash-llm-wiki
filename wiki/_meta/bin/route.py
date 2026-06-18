#!/usr/bin/env python3
"""route.py — cheap query->domain router. stdlib only, no network.

Phase-1 of the tiered QUERY path. Today every QUERY reads the global index.md
(~4.3k tok) PLUS index.<domain>.md before answering. This router picks the
domain(s) a query belongs to by keyword overlap with each domain's vocabulary
(taxonomy.md `## Areas` descriptions + each domain's `areas:` list + tags.py's
AREA_KEYWORDS + synonyms). A CONFIDENT single-domain match lets QUERY skip the
global index.md and read only index.<domain>.md. Ambiguous / zero-signal ->
return all domains (graceful: behave exactly as before, read the global router).

Derived + regenerable: the profiles are built from taxonomy.md at call time; there
is no stored artifact. If taxonomy.md is missing, route() returns all domains
(degrades to the old behaviour, never errors).

Usage:
    python3 route.py "active directory replication tombstone usn"   # -> active-directory
    python3 route.py --explain "rp-initiated logout id_token_hint"
    python3 route.py --eval _meta/eval/cases.jsonl                  # routing accuracy
"""
import argparse
import os
import re
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))
TAXONOMY = os.path.join(WIKI, "_meta", "taxonomy.md")
sys.dont_write_bytecode = True
sys.path.insert(0, BIN)
import kb       # reuse the exact tokenizer so routing tokens == search tokens
import tags     # AREA_KEYWORDS + load_taxonomy/load_domains (single source: taxonomy.md)

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with", "by", "per",
    "its", "via", "into", "over", "that", "this", "is", "are", "be", "as", "at", "from",
    "not", "use", "used", "using", "etc", "e.g", "i.e", "one", "two", "all", "any", "how",
}

# Domain-discriminating jargon the high-level `## Areas` descriptions omit. The taxonomy
# descriptions are intentionally coarse (forests/replication/FSMO/DNS for AD; flows/clients
# /tokens for keycloak), so product-specific tokens like gMSA/dMSA/KDS or DPoP/kcadm don't
# appear there and a description-only router mis-scores them. These are GENERAL domain
# vocabulary (not tuned to the eval cases): any AD/keycloak query using them should lean
# that way. Kept here, not in taxonomy.md, so the schema stays a tag vocabulary.
ROUTER_HINTS = {
    "active-directory": {
        "gmsa", "dmsa", "kds", "msds", "krbtgt", "ntds", "sysvol", "netlogon", "dcpromo",
        "adprep", "rodc", "kcc", "fsmo", "rid", "pdc", "tombstone", "usn", "sddl", "dfsr",
        "laps", "s4u2self", "s4u2proxy", "spn", "gpo", "admx", "managed", "delegated",
        "ticket", "tickets", "forest", "windows", "dc", "ntlm", "sid",
    },
    "keycloak": {
        "rhbk", "keycloak", "kcadm", "kcreg", "quarkus", "infinispan", "openshift",
        "operator", "dpop", "pkce", "oidc", "saml", "realm", "kc.sh", "spi", "rh-sso",
    },
}

_profiles = None


def _area_descriptions(path=TAXONOMY):
    """area-slug -> description words, parsed from the `## Areas` bullet lines
    (each is: dash, backticked area slug, em-dash, free-text description)."""
    out = {}
    if not os.path.isfile(path):
        return out
    section = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            h = re.match(r"^##\s+(.*)", line)
            if h:
                section = h.group(1).strip().lower()
                continue
            if section == "areas":
                m = re.match(r"^\s*-\s*`([a-z0-9][a-z0-9-]*)`\s*(.*)$", line)
                if m:
                    slug, desc = m.group(1), m.group(2)
                    words = set(slug.split("-")) | set(kb.toks(desc))
                    out[slug] = {w for w in words if len(w) >= 3 and w not in STOPWORDS}
    return out


def _domain_areas(path=TAXONOMY):
    """domain -> list of area slugs (from `### name` blocks under `## Domains`)."""
    out, cur = {}, None
    if not os.path.isfile(path):
        return out
    in_domains = False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            h = re.match(r"^##\s+(.*)", line)
            if h:
                in_domains = h.group(1).strip().lower().startswith("domains")
                continue
            if not in_domains:
                continue
            dm = re.match(r"^\s*-\s*domain:\s*([a-z][a-z0-9-]*)\s*$", line)
            if dm:
                cur = dm.group(1)
                out.setdefault(cur, [])
                continue
            am = re.match(r"^\s*-\s*areas:\s*\[(.*)\]\s*$", line)
            if am and cur:
                out[cur] = [a.strip() for a in am.group(1).split(",") if a.strip()]
    return out


def build_profiles():
    """domain -> set(keywords). Built from taxonomy areas + AREA_KEYWORDS + synonyms."""
    global _profiles
    if _profiles is not None:
        return _profiles
    area_words = _area_descriptions()
    dom_areas = _domain_areas()
    _, synonyms = tags.load_taxonomy()

    # area -> domains that declare it (shared areas like users/security stay neutral)
    area_to_domains = {}
    for dom, areas in dom_areas.items():
        for a in areas:
            area_to_domains.setdefault(a, set()).add(dom)

    prof = {dom: set() for dom in dom_areas}
    for dom, areas in dom_areas.items():
        prof[dom] |= set(dom.split("-"))                 # the domain name itself
        for a in areas:
            prof[dom] |= {a} | area_words.get(a, set())  # area slug + its description words
    # AREA_KEYWORDS (kw -> area): add kw to every domain that declares that area
    for kw, area in tags.AREA_KEYWORDS:
        for dom in area_to_domains.get(area, ()):
            prof[dom].add(kw)
    # synonyms (syn -> canonical area): add syn to domains declaring the canonical area
    for syn, canon in synonyms.items():
        for dom in area_to_domains.get(canon, ()):
            prof[dom].add(syn)
    # domain-discriminating jargon the coarse area descriptions omit
    for dom, hints in ROUTER_HINTS.items():
        if dom in prof:
            prof[dom] |= hints
    _profiles = prof
    return prof


def score_domains(query):
    """domain -> count of distinct query tokens present in that domain's profile."""
    prof = build_profiles()
    qtok = set(kb.toks(query))
    return {dom: len(qtok & kws) for dom, kws in prof.items()}


CONF_MIN = 2     # winner must have >= this many signal hits
CONF_MARGIN = 2  # ...and beat the runner-up by >= this, i.e. DOMINATE — so a query whose
                 # tokens are shared across domains stays ambiguous and reads the global
                 # index rather than confidently guessing wrong (precision over coverage:
                 # a CONFIDENT route is never wrong -> Phase-1 skip never regresses recall).


def route(query):
    """Return (domains, confident). `confident` => one domain DOMINATES (>=CONF_MIN hits and
    >=CONF_MARGIN ahead), so QUERY may skip the global index.md and read only that domain's
    index. Otherwise -> ranked domains with signal (or all), confident=False: read the
    global router as before. Conservative by design: misroutes degrade to a cheap fallback,
    never to a wrong-tier search."""
    scores = score_domains(query)
    if not scores:
        return [], False
    ranked = sorted(scores, key=lambda d: -scores[d])
    top = scores[ranked[0]]
    second = scores[ranked[1]] if len(ranked) > 1 else 0
    if top == 0:
        return ranked, False                                  # no signal: read the global router
    if top >= CONF_MIN and (top - second) >= CONF_MARGIN:
        return [ranked[0]], True                              # one domain dominates: confident
    return [d for d in ranked if scores[d] > 0] or ranked, False


def cmd_eval(path):
    """Report the property that matters for Phase 1: a CONFIDENT route (the one that lets
    QUERY skip the global index) must never be wrong. Non-confident = graceful abstention
    (read the global router as before) — a coverage gap, NOT a recall risk."""
    import json
    n = 0
    conf_ok, conf_wrong, abstained = [], [], []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            c = json.loads(line)
            n += 1
            doms, conf = route(c["query"])
            want = c.get("domain")
            if conf:
                (conf_ok if doms and doms[0] == want else conf_wrong).append((want, doms, c["query"][:52]))
            else:
                abstained.append((want, doms, c["query"][:52]))
    nc = len(conf_ok) + len(conf_wrong)
    prec = 100.0 * len(conf_ok) / nc if nc else 0.0
    print("Routing over %d cases:" % n)
    print("  confident      : %d/%d  (precision %.0f%%, CONFIDENT-WRONG=%d  <- must be 0)"
          % (nc, n, prec, len(conf_wrong)))
    print("  abstained      : %d/%d  (read global index — graceful, no recall risk)"
          % (len(abstained), n))
    for want, got, q in conf_wrong:
        print("  !! CONFIDENT-WRONG want=%s got=%s  %s…" % (want, got, q))
    for want, got, q in abstained:
        print("  .. abstain want=%s got=%s  %s…" % (want, ",".join(got), q))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="*")
    ap.add_argument("--explain", action="store_true")
    ap.add_argument("--eval", metavar="CASES")
    args = ap.parse_args()
    if args.eval:
        cmd_eval(args.eval if os.path.isabs(args.eval) else os.path.join(WIKI, args.eval))
        return
    q = " ".join(args.query)
    if not q:
        print("usage: route.py \"<query>\"  |  --eval <cases.jsonl>"); sys.exit(2)
    doms, conf = route(q)
    print("%s   (confident=%s)" % (", ".join(doms) or "(none)", conf))
    if args.explain:
        sc = score_domains(q)
        for d in sorted(sc, key=lambda x: -sc[x]):
            qtok = set(kb.toks(q))
            hits = sorted(qtok & build_profiles()[d])
            print("  %-18s score=%d  matched: %s" % (d, sc[d], ", ".join(hits) or "(none)"))


if __name__ == "__main__":
    main()
