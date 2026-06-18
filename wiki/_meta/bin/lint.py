#!/usr/bin/env python3
"""Health-check the Keycloak/RHBK LLM Wiki — stdlib only, no network.

Reports broken links, wanted (not-yet-written) pages, orphans, missing
provenance/summary, provenance drift, link hubs, and stale pages. With --status
it also prints the delta-manifest audit (ingested-vs-pending). See wiki/CLAUDE.md
for the schema this enforces.

Only the content dirs (topics/ entities/ questions/) are scanned; `_meta/` (this
script's home + the manifest) is tooling, not content, and is never scanned.

Usage:
    python3 wiki/_meta/bin/lint.py            # health check
    python3 wiki/_meta/bin/lint.py --status   # + delta-manifest audit
    python3 wiki/_meta/bin/lint.py --strict   # exit 1 on any *error*
    python3 wiki/_meta/bin/lint.py --stale-days 365   # stale threshold (default 365)
"""
import argparse
import datetime
import os
import re
import sys

BIN = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(os.path.dirname(BIN))   # _meta/bin -> _meta -> wiki
PAGE_DIRS = ("topics", "entities", "questions")
LINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)\]\]")
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def page_files():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield d, fn[:-3], os.path.join(full, fn)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    fm = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "-", "\t")):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    fm["_has_sources"] = "sources:" in block
    fm["_provenance"] = parse_provenance(block)
    fm["_block"] = block
    return fm


def parse_provenance(block):
    """Return ('needs-review'|'unknown'|None) or dict(extracted/inferred/ambiguous)."""
    lines = block.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^provenance:\s*(\S.*)?$", line)
        if not m:
            continue
        inline = (m.group(1) or "").strip()
        if inline:
            return inline  # e.g. "needs-review"
        counts = {}
        for sub in lines[i + 1:]:
            sm = re.match(r"^\s+(\w+):\s*(\d+)", sub)
            if sm:
                counts[sm.group(1)] = int(sm.group(2))
            elif not sub.startswith((" ", "\t")):
                break
        return counts or None
    return None  # provenance: absent


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def bold_definition(text):
    """Leading bold one-line definition, multi-line aware; mirrors backfill.py."""
    body = FM_RE.sub("", text, count=1)
    b = re.sub(r"^\s*#.*\n", "", body.lstrip(), count=1).lstrip()
    if not b.startswith("**"):
        return None
    m = re.match(r"\*\*(.+?)\*\*", b, re.DOTALL)
    if not m:
        return None
    return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--stale-days", type=int, default=365)
    ap.add_argument("--ctx-window", type=int, default=32768,
                    help="local model context window; a per-domain index over ~25%% of it is flagged")
    args = ap.parse_args()

    # shared taxonomy (from tags.py / _meta/taxonomy.md); empty if unavailable
    sys.dont_write_bytecode = True
    sys.path.insert(0, BIN)
    try:
        import tags as tagmod
        vocab, synonyms = tagmod.load_taxonomy()
        declared_domains = tagmod.load_domains()
    except Exception:  # noqa: BLE001
        tagmod, vocab, synonyms = None, set(), {}
        declared_domains = set()

    pages = {}
    for d, slug, path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        pages[slug] = (d, path, text, parse_frontmatter(text))

    slugs = set(pages)
    # reference-tier notes (wiki/reference/<domain>/) are valid [[link]] targets but
    # are NOT synthesized pages — collect their slugs so links to them aren't "wanted"
    ref_slugs = set()
    ref_root = os.path.join(WIKI, "reference")
    if os.path.isdir(ref_root):
        for dom in os.listdir(ref_root):
            dd = os.path.join(ref_root, dom)
            if os.path.isdir(dd):
                for fn in os.listdir(dd):
                    if fn.endswith(".md"):
                        ref_slugs.add(fn[:-3])

    # in-index detection spans the global index.md AND every generated index.<domain>.md
    index_sources = set()
    index_files = ["index.md"] + sorted(
        f for f in os.listdir(WIKI) if re.match(r"^index\.[a-z0-9-]+\.md$", f))

    referenced = {}     # slug -> set of pages (or index files) that link to it
    for slug, (_d, _p, text, _fm) in pages.items():
        for target in LINK_RE.findall(text):
            referenced.setdefault(target, set()).add(slug)
    for fn in index_files:
        p = os.path.join(WIKI, fn)
        if not os.path.exists(p):
            continue
        index_sources.add(fn)
        with open(p, encoding="utf-8") as fh:
            for target in LINK_RE.findall(fh.read()):
                referenced.setdefault(target, set()).add(fn)

    errors, warnings, notes, seeded, hubs = [], [], [], [], []

    wanted = sorted(t for t in referenced if t not in slugs and t not in ref_slugs)
    for t in wanted:
        src = ", ".join(sorted(referenced[t]))
        notes.append(f"wanted page [[{t}]]  (referenced by: {src})")

    today = datetime.date.today()
    for slug, (_d, path, text, fm) in pages.items():
        rel = os.path.relpath(path, WIKI)
        if fm is None:
            errors.append(f"{rel}: missing frontmatter block")
            continue
        if not fm.get("_has_sources"):
            errors.append(f"{rel}: no `sources:` provenance")

        # domain facet (required; validated against taxonomy ## Domains)
        dom = fm.get("domain")
        if not dom:
            warnings.append(f"{rel}: no `domain:` (required — run backfill.py)")
        elif declared_domains and dom not in declared_domains:
            warnings.append(f"{rel}: domain `{dom}` not declared in taxonomy.md ## Domains")

        # summary checks
        summary = fm.get("summary", "")
        if not summary:
            warnings.append(f"{rel}: no `summary:` (tiered query relies on it)")
        else:
            bd = bold_definition(text)
            if bd and unquote(summary).strip().rstrip(".") == bd:
                seeded.append(f"{rel}: summary auto-seeded from bold definition — wants a human summary")

        # provenance checks — and the PROVENANCE GATE (Phase 4): a `status: reviewed`
        # page MUST carry real per-claim provenance — no `needs-review`/`unknown`, and
        # not inferred>=extracted. For reviewed pages these are ERRORS (so `--strict`
        # fails and lists them); for draft/stub pages they remain warnings. The gate only
        # FLAGS — fixing a flagged page is a separate human/LLM content pass, never an
        # auto-edit.
        prov = fm.get("_provenance")
        reviewed = fm.get("status") == "reviewed"
        if prov is None:
            warnings.append(f"{rel}: no `provenance:` block")
        elif isinstance(prov, str):
            if prov in ("needs-review", "unknown"):
                if reviewed:
                    errors.append(f"{rel}: provenance gate — status: reviewed but provenance: {prov} "
                                  f"(assign real per-claim provenance or lower status)")
                else:
                    warnings.append(f"{rel}: provenance: {prov} (assign real per-claim provenance)")
        elif isinstance(prov, dict):
            ext, inf = prov.get("extracted", 0), prov.get("inferred", 0)
            if inf >= ext and (ext or inf):
                if reviewed:
                    errors.append(f"{rel}: provenance gate — status: reviewed but inferred>=extracted "
                                  f"({inf}>={ext}); verify vs raw layer or lower status")
                else:
                    warnings.append(f"{rel}: provenance drifts inferred>=extracted ({inf}>={ext}) — verify vs raw layer")

        # tag checks (Pass 2 — validated against _meta/taxonomy.md)
        if tagmod is not None:
            page_tags = tagmod.parse_tags(fm.get("_block", ""))
            if page_tags is None:
                notes.append(f"{rel}: no `tags:` (run tags.py backfill)")
            else:
                for t in page_tags:
                    if vocab and t not in vocab:
                        hint = f" (synonym of `{synonyms[t]}` — run tags.py normalize)" if t in synonyms else ""
                        warnings.append(f"{rel}: tag `{t}` not in taxonomy{hint}")

        if fm.get("status") == "stub":
            warnings.append(f"{rel}: still status: stub")

        # stale: updated older than threshold
        upd = fm.get("updated", "")
        try:
            d = datetime.date.fromisoformat(upd)
            if (today - d).days > args.stale_days:
                notes.append(f"{rel}: stale (updated {upd}, >{args.stale_days}d)")
        except ValueError:
            pass

        # orphan check (spans index.md + every index.<domain>.md)
        in_index = slug in referenced and bool(referenced[slug] & index_sources)
        linked = slug in referenced and any(s not in index_sources for s in referenced[slug])
        if not in_index and not linked and fm.get("type") != "question":
            warnings.append(f"{rel}: orphan (no inbound [[links]] and not in any index)")

    # hubs: most-linked pages (inbound from other pages, not index files)
    inbound = {s: len([x for x in srcs if x not in index_sources]) for s, srcs in referenced.items() if s in slugs}
    for slug, n in sorted(inbound.items(), key=lambda kv: -kv[1])[:8]:
        if n:
            hubs.append(f"[[{slug}]] — {n} inbound links")

    # cross-domain links: page in one domain linking to a page in another (soft —
    # intentional bridges are fine, but they're the SRE correlation surface, so surface them)
    page_dom = {s: (fm.get("domain") if fm else None) for s, (_d, _p, _t, fm) in pages.items()}
    xdomain = []
    for tgt, srcs in referenced.items():
        if tgt not in pages:
            continue
        for src in sorted(srcs):
            if (src in pages and page_dom.get(src) and page_dom.get(tgt)
                    and page_dom[src] != page_dom[tgt]):
                xdomain.append(f"[[{src}]] ({page_dom[src]}) → [[{tgt}]] ({page_dom[tgt]})")

    # generated-index health: staleness + context-budget (stdlib heuristic, no tokenizer)
    try:
        import index as indexmod
        for d in indexmod.stale_indexes():
            warnings.append(f"index.{d}.md is stale — run `python3 _meta/bin/index.py`")
    except Exception as e:  # noqa: BLE001
        notes.append(f"index staleness check unavailable: {e}")
    budget = int(args.ctx_window * 0.25)
    for fn in index_files:
        if fn == "index.md":
            continue
        p = os.path.join(WIKI, fn)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as fh:
            est_tokens = len(fh.read()) // 4  # ~4 chars/token heuristic (air-gap-safe, no tiktoken)
        if est_tokens > budget:
            warnings.append(f"{fn}: ~{est_tokens} tokens (> 25% of --ctx-window {args.ctx_window}) "
                            "— split the domain or trim summaries to protect the routing context")

    # reference-tier validation (the folded-in corpus). Light checks (warnings, not errors):
    # these are raw imported notes, not synthesized pages, but a malformed one silently
    # breaks retrieval (e.g. an empty gated index drops every gated pointer).
    ref_root = os.path.join(WIKI, "reference")
    if os.path.isdir(ref_root):
        for dom in sorted(os.listdir(ref_root)):
            dd = os.path.join(ref_root, dom)
            if not os.path.isdir(dd):
                continue
            bodies = 0
            for fn in sorted(os.listdir(dd)):
                if not fn.endswith(".md") or fn.startswith("_"):
                    continue
                bodies += 1
                with open(os.path.join(dd, fn), encoding="utf-8") as fh:
                    rfm = parse_frontmatter(fh.read())
                rrel = f"reference/{dom}/{fn}"
                if rfm is None:
                    warnings.append(f"{rrel}: reference note missing frontmatter")
                elif not rfm.get("source"):
                    warnings.append(f"{rrel}: reference note has no `source:`")
            gated = os.path.join(dd, "_gated-kb-index.md")
            if os.path.exists(gated):
                gtext = open(gated, encoding="utf-8").read()
                if gtext.count("\n## ") == 0:
                    warnings.append(f"reference/{dom}/_gated-kb-index.md: present but no pointers parsed (malformed?)")
            if bodies == 0:
                notes.append(f"reference/{dom}/: no body notes (corpus not folded in?)")

    def section(label, items):
        if items:
            print(f"\n{label} ({len(items)})")
            for i in items:
                print(f"  - {i}")

    print(f"Wiki lint — {len(pages)} pages across {', '.join(PAGE_DIRS)}")
    section("ERRORS", errors)
    section("WARNINGS", warnings)
    section("AUTO-SEEDED SUMMARIES (soft — replace with a real summary)", seeded)
    section("CROSS-DOMAIN LINKS (soft — intentional bridges; the SRE correlation surface)", xdomain)
    section("HUBS (most-linked pages)", hubs)
    section("WANTED PAGES (TODO markers, not errors)", notes)
    if not (errors or warnings or notes or seeded):
        print("\nClean. No issues.")

    if args.status:
        print("\n=== STATUS / delta-manifest audit ===")
        sys.dont_write_bytecode = True  # keep _meta/bin/ free of __pycache__
        sys.path.insert(0, BIN)
        try:
            import manifest
            for ln in manifest.status_lines():
                print("  " + ln)
        except Exception as e:  # noqa: BLE001
            print(f"  (manifest audit unavailable: {e})")

    if args.strict and errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
