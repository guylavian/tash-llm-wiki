#!/usr/bin/env python3
"""pdf_to_corpus.py — turn a folder of PDFs into a corpus.

The Markdown/AsciiDoc siblings (`docs_to_corpus.py`, `adoc_to_corpus.py`) harvest docs
repos; this one harvests **PDF document sets** (vendor guides, CIS/STIG benchmarks,
product manuals). It extracts each PDF's text page-by-page, keeps `<!-- p.N -->` page
markers so wiki pages can cite page numbers, and emits the SAME
`corpora/<domain>/index.jsonl` + body files that the proven `corpus_to_vault.py`
consumes — so a PDF-backed domain is the usual three commands and no bespoke code:

    # 1. pdf folder -> corpus (this script)
    python3 -m wikikb pdf_to_corpus --src _sources/<domain>/_raw/pdfs \\
        --domain <domain> --url-base https://vendor.example/docs --apply
    # 2. corpus -> immutable in-vault reference notes (existing tool, unchanged)
    python3 -m wikikb corpus_to_vault --domain <domain> --apply
    # 3. synthesize pages citing kb:<pdf-stem>, then regen the link graph
    python3 -m wikikb build

Extraction ladder (text PDFs only — scanned/image PDFs are reported and skipped, never
silently emitted empty):
  1. a pre-extracted `<name>.txt` beside/instead of `<name>.pdf` in --src (pure-stdlib
     path for a sealed box: run `pdftotext` on a tooled machine, ship the .txt tree);
  2. `pdftotext -layout -enc UTF-8` (poppler) when the binary is on PATH.
There is deliberately NO pure-Python PDF parser: a half-working extractor that emits
mojibake into the immutable ground-truth tier is worse than a loud skip.
# ponytail: whole-PDF (or fixed-page-chunk) records; splitting on the PDF outline
# (per-chapter notes) is the upgrade path if grep-retrieval on big books gets noisy.

Citation contract: the record's URL **tail** becomes the `kb:` token wiki pages cite
(crosslink.py resolves `kb:<tail>` -> the reference note). Tails here are the slugified
PDF stem, plus `-pNNNN-NNNN` when --chunk-pages splits a big book. Pass a real
--url-base when the PDFs have canonical URLs; the default `pdf://<domain>` marks a
local-file provenance.

stdlib only, no network. Dry-run by default; --apply writes corpora/<domain>/.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

from wikikb import paths
ROOT = str(paths.ROOT)

_slug_bad = re.compile(r"[^a-z0-9]+")


def slugify(s):
    return _slug_bad.sub("-", (s or "").lower()).strip("-") or "doc"


# ---------- title: PDF Info-dict /Title, else first text line, else the filename ----------

def _decode_pdf_string(b):
    try:
        if b.startswith(b"\xfe\xff"):
            return b[2:].decode("utf-16-be").strip() or None
        return b.decode("latin-1").strip() or None      # PDFDocEncoding ~ latin-1 for common text
    except (UnicodeDecodeError, ValueError):
        return None


def pdf_title(raw):
    """Best-effort /Title from the raw bytes (uncompressed Info dicts only — a title
    inside an object stream is invisible here, and we then fall back, never guess)."""
    m = re.search(rb"/Title\s*\(((?:\\.|[^\\()])*)\)", raw)
    if m:
        s = re.sub(rb"\\([()\\])", rb"\1", m.group(1))
        s = re.sub(rb"\\[nrtbf]", b" ", s)
        return _decode_pdf_string(s)
    m = re.search(rb"/Title\s*<([0-9A-Fa-f\s]*)>", raw)
    if m:
        hx = re.sub(rb"\s", b"", m.group(1))
        if hx:
            try:
                return _decode_pdf_string(bytes.fromhex(hx.decode("ascii")))
            except ValueError:
                return None
    return None


def first_line_title(pages):
    for pg in pages:
        for ln in pg.splitlines():
            t = re.sub(r"\s+", " ", ln).strip()
            if len(t) >= 4:
                return t[:120]
    return None


# ---------- extraction ----------

def extract_pdftotext(path):
    """PDF -> page-separated text via poppler's pdftotext, or None if unavailable/failed."""
    if not shutil.which("pdftotext"):
        return None
    try:
        p = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", path, "-"],
                           capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        return None
    return p.stdout if p.returncode == 0 else None


def doc_pages(src, stem, have_txt):
    """(pages, method) for one document; pages split on the \\f page breaks pdftotext emits.
    A pre-extracted .txt wins over the .pdf (the sealed-box path)."""
    if have_txt:
        with open(os.path.join(src, stem + ".txt"), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        method = "txt"
    else:
        text = extract_pdftotext(os.path.join(src, stem + ".pdf"))
        if text is None:
            return None, "pdftotext-unavailable-or-failed"
        method = "pdftotext"
    pages = [p for p in text.split("\f")]
    while pages and not pages[-1].strip():
        pages.pop()
    return (pages if any(p.strip() for p in pages) else None), method


def render_body(pages, start_page):
    """Markdown-ish body: absolute page markers (the citation anchor) + light cleanup."""
    out = []
    for i, pg in enumerate(pages):
        out.append("<!-- p.%d -->" % (start_page + i))
        out.append(pg.rstrip())
    body = "\n\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


# ---------- build ----------

def chunks(pages, n):
    """Yield (start_page_1based, pages_slice). n<=0 -> one chunk with everything."""
    if n <= 0 or len(pages) <= n:
        yield 1, pages
        return
    for i in range(0, len(pages), n):
        yield i + 1, pages[i:i + n]


def build(src, domain, url_base, family, version, guide, kind, chunk_pages):
    stems = {}                                    # stem -> has_txt
    for fn in sorted(os.listdir(src)):
        stem, ext = os.path.splitext(fn)
        if ext.lower() == ".pdf":
            stems.setdefault(stem, False)
        elif ext.lower() == ".txt":
            stems[stem] = True
    recs, bodies, skipped, methods = [], {}, [], {}
    used = {}                       # stem_slug -> stem: two files slugifying identically would share a
    for stem in sorted(stems):      # url + body_file (silent overwrite) — skip loudly, never renumber
        stem_slug = slugify(stem)   # (a suffixed token would silently change what pages must cite)
        if stem_slug in used:
            skipped.append((stem, "stem slug '%s' collides with '%s' — rename one file"
                            % (stem_slug, used[stem_slug])))
            continue
        used[stem_slug] = stem
        pages, method = doc_pages(src, stem, stems[stem])
        if pages is None:
            skipped.append((stem, "empty-text" if method in ("txt", "pdftotext") else method))
            continue
        methods[stem] = method
        raw = b""
        if not stems[stem]:
            with open(os.path.join(src, stem + ".pdf"), "rb") as fh:
                raw = fh.read()
        doc_title = pdf_title(raw) or first_line_title(pages) or stem
        n_chunks = 1 if chunk_pages <= 0 else -(-len(pages) // chunk_pages)
        for start, sl in chunks(pages, chunk_pages):
            end = start + len(sl) - 1
            tail = stem_slug if n_chunks == 1 else "%s-p%04d-%04d" % (stem_slug, start, end)
            url = url_base.rstrip("/") + "/" + tail
            title = doc_title if n_chunks == 1 else "%s — pages %d-%d" % (doc_title, start, end)
            body = render_body(sl, start)
            body_file = "bodies/" + slugify(url.split("//", 1)[-1]) + ".md"
            rec = {
                "title": title,
                "url": url,
                "family": family,
                "documentKind": kind,
                "abstract": re.sub(r"\s+", " ",
                                   re.sub(r"<!-- p\.\d+ -->", " ", body))[:280].strip(),
                "body_status": "fetched",
                "body_file": body_file,
            }
            if version:
                rec["version"] = version
            if guide:
                rec["guide"] = guide
            recs.append(rec)
            bodies[body_file] = body
    return recs, bodies, skipped, methods


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True,
                    help="folder of .pdf files (and/or pre-extracted .txt siblings, which win)")
    ap.add_argument("--domain", required=True)
    ap.add_argument("--url-base", default=None,
                    help="canonical URL base for the docs; the URL TAIL is the kb: citation "
                         "token (default: pdf://<domain>, i.e. local-file provenance)")
    ap.add_argument("--family", default=None,
                    help="slug family prefix for the reference notes (default: the domain)")
    ap.add_argument("--version", default=None, help="doc-set version, e.g. 8 or 2025.1")
    ap.add_argument("--guide", default=None, help="optional guide grouping token")
    ap.add_argument("--kind", default="doc", help="documentKind frontmatter (default: doc)")
    ap.add_argument("--chunk-pages", type=int, default=0,
                    help="split each PDF into records of N pages (0 = one record per PDF)")
    ap.add_argument("--append", action="store_true",
                    help="merge into an existing corpora/<domain>/index.jsonl (dedup by url; "
                         "new harvest wins)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        raise SystemExit("--src not found: %s" % args.src)
    url_base = args.url_base or ("pdf://" + args.domain)
    recs, bodies, skipped, methods = build(
        args.src, args.domain, url_base, args.family or args.domain,
        args.version, args.guide, args.kind, args.chunk_pages)

    outdir = os.path.join(str(paths.CORPORA), args.domain)
    rel = os.path.relpath(outdir, ROOT)
    n_docs = len(methods)
    print("domain=%s  src=%s" % (args.domain, args.src))
    print("pdf docs extracted=%d (%s)  records=%d" % (
        n_docs, ", ".join(sorted(set(methods.values()))) or "none", len(recs)))
    if skipped:  # never a silent cap: name what was dropped and why
        print("SKIPPED %d (no extractable text — scanned/image PDF, or install poppler / "
              "ship .txt): %s" % (len(skipped), ", ".join("%s [%s]" % s for s in skipped)))
    print("target: %s/index.jsonl + %s/bodies/*.md" % (rel, rel))
    if recs:
        print("sample url: %s  (cite it as kb:%s)" % (recs[0]["url"],
                                                      recs[0]["url"].rsplit("/", 1)[-1]))
    if not recs and not skipped:
        raise SystemExit("no .pdf/.txt documents found in --src")

    if not args.apply:
        print("\n--- DRY RUN (no files written). Re-run with --apply, then: "
              "python3 -m wikikb corpus_to_vault --domain %s --apply ---" % args.domain)
        return

    os.makedirs(os.path.join(outdir, "bodies"), exist_ok=True)
    idx = os.path.join(outdir, "index.jsonl")
    existing = []
    if args.append and os.path.isfile(idx):
        urls = {r["url"] for r in recs}
        for line in open(idx, encoding="utf-8"):
            line = line.strip()
            if line:
                rec = json.loads(line)
                if rec.get("url") not in urls:            # new harvest wins on url collision
                    existing.append(rec)
    allrecs = existing + recs
    with open(idx, "w", encoding="utf-8") as fh:
        for r in allrecs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for bf, text in bodies.items():
        with open(os.path.join(outdir, bf), "w", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
    print("\nWROTE %s/index.jsonl (%d records%s) + %d body files" % (
        rel, len(allrecs), ", %d kept from --append" % len(existing) if existing else "",
        len(bodies)))
    print("NEXT: python3 -m wikikb corpus_to_vault --domain %s --apply   "
          "(then: python3 -m wikikb build)" % args.domain)


if __name__ == "__main__":
    main()
