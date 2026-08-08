#!/usr/bin/env python3
"""adoc_to_corpus.py — turn a Red Hat AsciiDoc docs repo (openshift/openshift-docs) into a corpus.

The Markdown sibling `docs_to_corpus.py` handles DocFX/Hugo Markdown (MS Learn, kubernetes.io).
Red Hat product docs are **AsciiDoc** assemblies: a top-level `<book>/<assembly>.adoc` carries the
page (`= Title`, prose) and `include::modules/*.adoc[]` directives that splice in reusable modules.
This harvester walks the book dirs, treats each **assembly** as one record, **resolves its includes
inline** (so the body is the complete published page, not a fragment), lightly de-AsciiDocs the text,
derives the docs.redhat.com URL, and emits the SAME `corpora/<domain>/index.jsonl` + body files that
the proven `corpus_to_vault.py` consumes. So onboarding an OCP-style domain is, like the Markdown path,
two stdlib commands and no bespoke fold-in code.

    # 1. adoc tree -> corpus (this script); --append keeps an existing (e.g. kubernetes) index
    python3 -m wikikb adoc_to_corpus --src <clone>/openshift-docs --domain openshift \\
        --version 4.22 --append --apply
    # 2. corpus -> immutable in-vault reference notes (existing tool, unchanged)
    python3 -m wikikb corpus_to_vault --domain openshift --apply

stdlib only, no network. Clone the repo (per version branch) on a networked box, then run this offline.
Lexical/grep retrieval tolerates residual markup, so the cleanup is deliberately light (provenance, not
a renderer). Re-run per branch (enterprise-4.8 … enterprise-4.22) with a distinct --version to layer
versions, exactly as the keycloak corpus carries 26.0/26.2/26.4/26.6.
"""
import argparse
import json
import os
import re
import sys

from wikikb import paths
ROOT = str(paths.ROOT)

# Book dirs are the published topic groups; skip tooling/asset/include-only trees.
SKIP_DIR = {"modules", "_attributes", "_images", "_javascripts", "_stylesheets", "_templates",
            "_topic_maps", "_converters", "_gemfiles", "_unused_topics", "images", "media",
            ".git", "contributing_to_docs", "rest_api", "snippets", "_custom-overrides"}
INCLUDE_RE = re.compile(r"^include::([^\[\]]+)\[[^\]]*\]\s*$")
URL_BASE = "https://docs.redhat.com/en/documentation/openshift_container_platform"


def resolve_includes(path, seen=None, depth=0):
    """Read an .adoc file, splicing in `include::...[]` targets recursively (depth-capped, cycle-safe)."""
    seen = seen if seen is not None else set()
    rp = os.path.abspath(path)
    if rp in seen or depth > 8 or not os.path.isfile(rp):
        return ""
    seen.add(rp)
    out = []
    for line in open(rp, encoding="utf-8", errors="replace").read().splitlines():
        m = INCLUDE_RE.match(line.strip())
        if m:
            target = m.group(1).strip()
            if target.startswith("_attributes") or target.startswith("snippets"):
                continue                                # boilerplate attribute/snippet partials
            inc = os.path.normpath(os.path.join(os.path.dirname(rp), target))
            out.append(resolve_includes(inc, seen, depth + 1))
        else:
            out.append(line)
    return "\n".join(out)


def clean_adoc(text, product="OpenShift Container Platform"):
    """Light de-AsciiDoc for a lexical corpus: drop conditionals/attr-entries/toc, flatten xref/link text,
    substitute the common product attributes. NOT a renderer — residual markup is fine for grep/lexical."""
    lines = []
    for ln in text.splitlines():
        s = ln.rstrip()
        if re.match(r"^(ifdef|ifndef|endif|ifeval)::", s):       # conditional directives
            continue
        if re.match(r"^:[\w!-]+:.*$", s) and not s.startswith("::"):  # attribute entries (:context:, …)
            continue
        if s in ("toc::[]",) or s.startswith("////"):
            continue
        lines.append(s)
    body = "\n".join(lines)
    body = re.sub(r"\{product-title\}", product, body)
    body = re.sub(r"\{product-version\}", "", body)
    body = re.sub(r"xref:[^\[]*\[([^\]]*)\]", r"\1", body)        # xref:...[text] -> text
    body = re.sub(r"link:[^\[]*\[([^\]]*)\]", r"\1", body)        # link:...[text] -> text
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def title_of(text, fallback):
    for ln in text.splitlines():
        m = re.match(r"^=\s+(.+)$", ln.strip())
        if m:
            return m.group(1).strip()
    return fallback


def is_assembly(path, raw):
    """An assembly = a publishable page (has a top-level `= Title`), not a bare module/partial."""
    if "/modules/" in path.replace(os.sep, "/"):
        return False
    return bool(re.search(r"^=\s+\S", raw, re.MULTILINE))


def build(src_root, domain, version):
    recs, bodies = [], {}
    src_root = os.path.abspath(src_root)
    for dirpath, dirnames, filenames in os.walk(src_root):
        dirnames[:] = [d for d in dirnames if d.lower() not in SKIP_DIR and not d.startswith(".")]
        rel_dir = os.path.relpath(dirpath, src_root)
        if rel_dir == "." or rel_dir.split(os.sep)[0] in SKIP_DIR:
            continue
        book = rel_dir.split(os.sep)[0]
        for fn in sorted(filenames):
            if not fn.endswith(".adoc") or fn.startswith("_"):
                continue
            path = os.path.join(dirpath, fn)
            raw = open(path, encoding="utf-8", errors="replace").read()
            if not is_assembly(path, raw):
                continue
            full = resolve_includes(path)
            body = clean_adoc(full)
            if len(body) < 200:                          # skip near-empty stubs/landing pages
                continue
            stem = re.sub(r"\.adoc$", "", fn)
            slug = re.sub(r"[^a-z0-9]+", "-", ("ocp-%s-%s" % (book, stem)).lower()).strip("-")
            url = "%s/%s/html/%s/%s" % (URL_BASE, version, book, stem)
            body_file = "bodies/%s.md" % slug
            recs.append({"id": slug, "title": title_of(full, stem.replace("-", " ")),
                         "abstract": "", "url": url, "documentKind": "Documentation",
                         "version": version, "domain": domain, "family": book,   # book -> reference sub-hub
                         "body_status": "fetched", "body_file": body_file,
                         "source_path": os.path.relpath(path, src_root)})
            bodies[body_file] = body                      # keyed by body_file (corpus_to_vault contract)
    return recs, bodies


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="root of the openshift-docs clone (a version branch)")
    ap.add_argument("--domain", required=True)
    ap.add_argument("--version", required=True, help="OCP version this branch is, e.g. 4.22")
    ap.add_argument("--append", action="store_true",
                    help="merge into an existing corpora/<domain>/index.jsonl (keep other-source records)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    recs, bodies = build(args.src, args.domain, args.version)
    by_book = {}
    for r in recs:
        by_book[r["source_path"].split(os.sep)[0]] = by_book.get(r["source_path"].split(os.sep)[0], 0) + 1
    print("domain=%s  version=%s  src=%s" % (args.domain, args.version, args.src))
    print("assemblies harvested=%d across %d books" % (len(recs), len(by_book)))
    print("sample url: %s" % (recs[0]["url"] if recs else "(none)"))
    if not args.apply:
        print("(dry run — pass --apply to write corpora/%s/)" % args.domain)
        return

    cdir = os.path.join(str(paths.CORPORA), args.domain)
    bdir = os.path.join(cdir, "bodies")
    os.makedirs(bdir, exist_ok=True)
    idx = os.path.join(cdir, "index.jsonl")
    existing = []
    if args.append and os.path.isfile(idx):
        ids = {r["id"] for r in recs}
        for line in open(idx, encoding="utf-8"):
            line = line.strip()
            if line:
                rec = json.loads(line)
                if rec.get("id") not in ids:             # new harvest wins on id collision
                    existing.append(rec)
    allrecs = existing + recs
    with open(idx, "w", encoding="utf-8") as fh:
        for r in allrecs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for body_file, body in bodies.items():               # body_file is "bodies/<slug>.md"
        with open(os.path.join(cdir, body_file), "w", encoding="utf-8") as fh:
            fh.write(body)
    print("WROTE %s (%d records total: %d existing + %d new) + %d body files"
          % (idx, len(allrecs), len(existing), len(recs), len(bodies)))
    print("NEXT: python3 -m wikikb corpus_to_vault --domain %s --apply" % args.domain)


if __name__ == "__main__":
    main()
