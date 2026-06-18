#!/usr/bin/env python3
"""kb.py — ranked search over the Obsidian vault's reference tier. stdlib only, no network.

**Obsidian rules all the data.** There is no separate corpus or `index.jsonl`: the
imported doc bodies live in the vault as Markdown reference notes under
`wiki/reference/<domain>/` (one note per source) plus a `_gated-kb-index.md` of
body-less pointers. This tool just reads those notes and ranks them — it is a
convenience over the vault, not a separate store. Plain `grep`/`ripgrep` over
`wiki/reference/<domain>/` does the same job; the wiki QUERY path uses grep directly.

USAGE
  python3 kb.py domains                                  # domains with a reference tier
  python3 kb.py --domain keycloak search "ldap truststore operator"
  python3 kb.py --domain keycloak search "fips bcfips" --kind doc
  python3 kb.py --domain keycloak search "proxy headers" --gated   # include gated pointers
  python3 kb.py --all-domains search "tls handshake"
  python3 kb.py --domain keycloak show <slug|url-substr>
  python3 kb.py --domain keycloak guides | stats

Flags for `search`: --kind {doc,solution,article,discussion} --guide <slug>
  --version <v> --family <f> --gated --primary --limit N --full
"""
import argparse, os, re, sys
from collections import Counter

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))      # wiki/_meta/bin -> wiki/
REF = os.path.join(WIKI, "reference")
GATED_FILE = "_gated-kb-index.md"
FM_RE = re.compile(r"^---\n(.*?)\n---\s*(.*)$", re.DOTALL)

KIND = {"doc": "Documentation", "documentation": "Documentation", "solution": "Solution",
        "kb": "Solution", "article": "Article", "discussion": "Discussion"}


def reference_dir(domain):
    return os.path.join(REF, domain)


def available_domains():
    """Domains with a reference tier on disk (wiki/reference/<d>/*.md)."""
    if not os.path.isdir(REF):
        return []
    out = []
    for d in sorted(os.listdir(REF)):
        dd = os.path.join(REF, d)
        if os.path.isdir(dd) and any(f.endswith(".md") and f != GATED_FILE for f in os.listdir(dd)):
            out.append(d)
    return out


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _split(text):
    """(frontmatter dict, body) for a reference note."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if line and not line[0].isspace() and ":" in line and not line.startswith(("-", "#")):
            k, _, v = line.partition(":")
            fm[k.strip()] = _unquote(v)
    return fm, m.group(2)


def _parse_gated(path, domain):
    """Recreate pointer records from reference/<domain>/_gated-kb-index.md."""
    recs, cur = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            h = re.match(r"^##\s+(.*)", line)
            if h:
                if cur:
                    recs.append(cur)
                cur = {"title": h.group(1).strip(), "url": "", "abstract": "",
                       "body_status": "subscriber_only", "_body": "", "_domain": domain,
                       "documentKind": "Solution", "primary": False}
                continue
            if cur and line.strip().startswith("- "):
                val = line.strip()[2:].strip()
                if val.startswith("http") and not cur["url"]:
                    cur["url"] = val
                else:
                    cur["abstract"] = (cur["abstract"] + " " + val).strip()
    if cur:
        recs.append(cur)
    return recs


def load(domain):
    d = reference_dir(domain)
    if not os.path.isdir(d):
        return None
    recs = []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(d, fn)
        if fn == GATED_FILE:
            recs.extend(_parse_gated(path, domain))
            continue
        with open(path, encoding="utf-8") as fh:
            fm, body = _split(fh.read())
        recs.append({
            "id": fm.get("slug") or fn[:-3],
            "title": fm.get("title") or fn[:-3],
            "url": fm.get("source") or "",
            "guide": fm.get("guide"),
            "version": fm.get("version"),
            "family": fm.get("family"),
            "documentKind": fm.get("documentKind"),
            "primary": str(fm.get("primary")).lower() == "true",
            "abstract": fm.get("abstract") or "",
            "body_status": "fetched",
            "_body": body,
            "_domain": domain,
        })
    return recs


def load_many(domains):
    recs = []
    for d in domains:
        r = load(d)
        if r:
            recs.extend(r)
    return recs


def body_text(r):
    return r.get("_body", "")


_word = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9+_.-]*")
def toks(s):
    return [w.lower() for w in _word.findall(s or "")]


def vkey(v):
    try:
        return tuple(int(x) for x in (v or "0").split("."))
    except ValueError:
        return (0,)


def score(r, terms, bt):
    title = (r.get("title") or "").lower()
    abs   = (r.get("abstract") or "").lower()
    tc, ac, bc = Counter(toks(title)), Counter(toks(abs)), Counter(toks(bt))
    s, hit_terms = 0.0, 0
    for t in terms:
        h = tc.get(t, 0) * 6 + ac.get(t, 0) * 3 + bc.get(t, 0)
        if h:
            hit_terms += 1
        s += h
    if hit_terms == 0:
        return 0.0
    if len(terms) >= 2 and hit_terms < max(1, (len(terms) + 1) // 2):
        s *= 0.25
    phrase = " ".join(terms)
    if len(terms) >= 2:
        if phrase in title: s += 40
        elif phrase in abs: s += 15
        elif phrase in (bt or "").lower(): s += 8
    if r.get("primary"): s *= 1.30
    if r.get("family") == "rhsso": s *= 0.80
    if r.get("body_status") != "fetched": s *= 0.85
    s += hit_terms * 2
    return s


def snippet(bt, terms, width=260):
    if not bt:
        return ""
    low = bt.lower()
    best_i, best_n = 0, -1
    for i in range(0, max(1, len(low) - width), 60):
        n = sum(low[i:i + width].count(t) for t in terms)
        if n > best_n:
            best_n, best_i = n, i
    seg = bt[best_i:best_i + width].replace("\n", " ").strip()
    return ("…" if best_i else "") + re.sub(r"\s+", " ", seg) + "…"


def ref(r):
    u = r.get("url", "") or ""
    m = re.search(r"/solutions/(\d+)", u)
    if m: return "KB " + m.group(1)
    m = re.search(r"/articles/([0-9A-Za-z_]+)", u)
    if m: return "Article " + m.group(1)
    if r.get("guide"):
        return "%s %s · %s" % ((r.get("family") or "").upper(), r.get("version", "?"), r.get("guide"))
    return r.get("documentKind", "?")


def cmd_search(recs, a):
    terms = toks(" ".join(a.query))
    if not terms:
        print("no query terms"); return
    pool = recs
    if a.kind:
        want = KIND.get(a.kind.lower())
        pool = [r for r in pool if r.get("documentKind") == want]
    if a.guide:
        pool = [r for r in pool if r.get("guide") == a.guide]
    if a.version:
        pool = [r for r in pool if r.get("version") == a.version]
    if a.family:
        pool = [r for r in pool if r.get("family") == a.family]
    if a.primary:
        pool = [r for r in pool if r.get("primary")]
    if not a.gated:
        pool = [r for r in pool if r.get("body_status") == "fetched"]
    scored = []
    for r in pool:
        bt = body_text(r)
        sc = score(r, terms, bt)
        if sc > 0:
            scored.append((sc, r, bt))
    scored.sort(key=lambda x: (-x[0], -vkey(x[1].get("version"))[0] if x[1].get("version") else 0))

    # --hybrid: fuse the lexical ranking with the dense (embedding) ranking via RRF.
    # The dense path lives in embed.py (the one place a local model dep is allowed) and is
    # imported lazily + guarded, so kb.py stays stdlib-only and DEGRADES TO LEXICAL when the
    # library / vendored model / index is absent (the air-gap invariant).
    if getattr(a, "hybrid", False) and not a.all_domains and a.domain:
        embed = dense = None
        try:
            import embed
            dense = embed.dense_rank(a.domain, " ".join(a.query))
        except Exception:
            dense = None
        if dense:
            lex_ids = [r.get("id") for _, r, _ in scored]
            by_id = {r.get("id"): (sc, r, bt) for sc, r, bt in scored}
            rec_by_id = {r.get("id"): r for r in pool}
            fused = []
            for sid in embed.rrf_fuse(lex_ids, dense):
                if sid in by_id:
                    fused.append(by_id[sid])
                elif sid in rec_by_id:                 # dense-only note (lexical score 0)
                    r = rec_by_id[sid]
                    fused.append((0.0, r, body_text(r)))
            scored = fused
        else:
            why = embed.status_str() if embed is not None else "embed.py import failed"
            print("(hybrid unavailable — %s; lexical only)" % why, file=sys.stderr)

    if not scored:
        print("No matches. Try fewer terms, or --gated to include subscriber-only pointers.")
        return
    multi = a.all_domains or len({r.get("_domain") for _, r, _ in scored}) > 1
    print("%d hit(s) for: %s\n" % (len(scored), " ".join(terms)))
    for i, (sc, r, bt) in enumerate(scored[:a.limit], 1):
        gate = "" if r.get("body_status") == "fetched" else "  [GATED — title/abstract only]"
        dom = ("{%s} " % r.get("_domain")) if multi else ""
        print("%2d. %s[%-12s] %s%s" % (i, dom, ref(r), r.get("title", ""), gate))
        if r.get("url"):
            print("    %s" % r["url"])
        sn = snippet(bt, terms) if bt else (r.get("abstract") or "")
        if sn:
            print("    %s" % sn)
        print()
    if a.full and scored:
        top, bt = scored[0][1], scored[0][2]
        print("=" * 78)
        print("FULL BODY of top hit: %s\n%s\n%s" % (top.get("title"), top.get("url"), "=" * 78))
        print(bt or "(no public body — subscriber-gated)")


def cmd_show(recs, a):
    q = a.target.lower()
    for r in recs:
        if (q == str(r.get("id")) or (r.get("url") and q in r["url"].lower())):
            print(r.get("title")); print(r.get("url"))
            print("domain=%s kind=%s family=%s version=%s guide=%s status=%s\n" % (
                r.get("_domain"), r.get("documentKind"), r.get("family"), r.get("version"),
                r.get("guide"), r.get("body_status")))
            print(body_text(r) or "(no public body — subscriber-gated; open the URL with a login)")
            return
    print("not found:", a.target)


def cmd_guides(recs, a):
    g = Counter()
    for r in recs:
        if r.get("documentKind") == "Documentation" and r.get("guide"):
            g[(r.get("family"), r.get("guide"))] += 1
    for (fam, guide), c in sorted(g.items(), key=lambda x: (-x[1], str(x[0][0]), str(x[0][1]))):
        print("%4d  %-6s %s" % (c, fam or "?", guide))


def cmd_stats(recs, a):
    print("Reference notes:", len(recs))
    print("By kind:", dict(Counter(r.get("documentKind") for r in recs)))
    print("By status:", dict(Counter(r.get("body_status") for r in recs)))
    print("By family:", dict(Counter(r.get("family") for r in recs)))
    print("Primary (newest) doc chapters:", sum(1 for r in recs if r.get("primary")))


def cmd_domains(_recs, _a):
    found = available_domains()
    if not found:
        print("No reference tier found under %s/ (run corpus_to_vault.py to fold a corpus in)."
              % os.path.relpath(REF, os.path.dirname(WIKI)))
        return
    print("Domains with a reference tier (wiki/reference/<domain>/):")
    for d in found:
        print("  %-16s %5d notes" % (d, len(load(d) or [])))


def resolve_records(a):
    if a.all_domains:
        return load_many(available_domains()), None
    if not a.domain:
        return None, ("--domain <name> is required (or --all-domains). "
                      "Available: " + (", ".join(available_domains()) or "none"))
    recs = load(a.domain)
    if recs is None:
        return None, ("no reference tier for domain '%s' at wiki/reference/%s/. It may be a "
                      "notes-first domain — grep wiki/_sources/%s/ instead. With a reference "
                      "tier: %s" % (a.domain, a.domain, a.domain, ", ".join(available_domains()) or "none"))
    return recs, None


def main():
    p = argparse.ArgumentParser(prog="kb.py", description="Ranked search over the vault reference tier")
    p.add_argument("--domain", help="which reference tier to search (wiki/reference/<domain>/)")
    p.add_argument("--all-domains", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query", nargs="+")
    s.add_argument("--kind"); s.add_argument("--guide"); s.add_argument("--version")
    s.add_argument("--family"); s.add_argument("--gated", action="store_true")
    s.add_argument("--primary", action="store_true")
    s.add_argument("--hybrid", action="store_true",
                   help="fuse lexical with dense embeddings (RRF); needs embed.py index — falls back to lexical")
    s.add_argument("--limit", type=int, default=10); s.add_argument("--full", action="store_true")
    s.set_defaults(fn=cmd_search)
    sh = sub.add_parser("show"); sh.add_argument("target"); sh.set_defaults(fn=cmd_show)
    sub.add_parser("guides").set_defaults(fn=cmd_guides)
    sub.add_parser("stats").set_defaults(fn=cmd_stats)
    sub.add_parser("domains").set_defaults(fn=cmd_domains)
    a = p.parse_args()
    if a.cmd == "domains":
        cmd_domains(None, a); return
    recs, err = resolve_records(a)
    if err:
        print(err); sys.exit(2)
    a.fn(recs, a)


if __name__ == "__main__":
    main()
