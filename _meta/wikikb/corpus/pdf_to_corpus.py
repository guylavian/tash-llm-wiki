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
  2. `pdftotext -layout -enc UTF-8` (poppler), found on PATH, at `WIKIKB_PDFTOTEXT`, or in the
     usual install dirs (a service's PATH is narrower than the operator's shell — see
     `pdftotext_path`). A run that extracts nothing exits non-zero rather than writing a
     green, empty corpus.
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

# `shutil.which` alone is NOT enough to decide poppler is absent. A server process inherits
# the PATH of whatever launched it, which is routinely narrower than the operator's shell —
# most sharply on Windows, where Git-for-Windows ships `pdftotext` inside its MSYS tree
# (`C:\Program Files\Git\mingw64\bin`) that a native Python's PATH never contains. The binary
# is then present on the box and invisible to this process, and every PDF is reported as
# "no extractable text" — indistinguishable, in the log, from a genuinely scanned PDF.
# So: probe the usual install locations too, and let an operator pin it outright.
_PDFTOTEXT_DIRS = (
    r"C:\Program Files\Git\mingw64\bin",          # Git for Windows (MSYS) — ships poppler
    r"C:\Program Files (x86)\Git\mingw64\bin",
    r"C:\Program Files\poppler\bin",              # standalone poppler-windows release
    r"C:\ProgramData\chocolatey\bin",             # choco install poppler
    "/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", "/bin",   # brew (arm64/x86) + POSIX
)
_PDFTOTEXT_UNSET = object()
_pdftotext_cached = _PDFTOTEXT_UNSET


def pdftotext_path():
    """Absolute path to poppler's `pdftotext`, or None if it is genuinely not installed.
    Cached — the answer cannot change inside one run, and build() asks once per document.
    `WIKIKB_PDFTOTEXT` pins an explicit binary and wins over every probe."""
    global _pdftotext_cached
    if _pdftotext_cached is not _PDFTOTEXT_UNSET:
        return _pdftotext_cached
    found = None
    pinned = os.environ.get("WIKIKB_PDFTOTEXT")
    if pinned:                                    # an explicit pin is honoured or reported,
        found = shutil.which(pinned)              # never silently downgraded to a PATH lookup
        if not found:
            print("WARNING: WIKIKB_PDFTOTEXT=%r is not an executable — ignoring it" % pinned,
                  file=sys.stderr)
    if not found:
        found = shutil.which("pdftotext")
    if not found:
        for d in _PDFTOTEXT_DIRS:
            cand = shutil.which("pdftotext", path=d)
            if cand:
                found = cand
                break
    _pdftotext_cached = found
    return found


def extract_pdftotext(path):
    """PDF -> (page-separated text, None), or (None, reason). The reason distinguishes
    'poppler is not installed' from 'poppler ran and refused this file' — collapsing the two
    is what makes a PATH problem look like a scanned PDF."""
    exe = pdftotext_path()
    if not exe:
        return None, "pdftotext-not-installed"
    try:
        # `encoding=` is NOT optional here: bare text=True decodes with the LOCALE codepage,
        # so on any non-UTF-8 console (cp1255/cp1251/cp936/…) the UTF-8 bytes we just asked
        # for blow up mid-stream and the document is misreported as having no text. We pin the
        # decoder to the -enc we requested; errors="replace" matches the .txt path above.
        p = subprocess.run([exe, "-layout", "-enc", "UTF-8", path, "-"],
                           capture_output=True, timeout=300,
                           encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return None, "pdftotext-timeout-300s"
    except OSError as e:                          # unreadable/quarantined binary
        return None, "pdftotext-unrunnable: %s" % e
    if p.returncode != 0:
        err = re.sub(r"\s+", " ", (p.stderr or "")).strip()[:160] or "no stderr"
        return None, "pdftotext-failed(rc=%d): %s" % (p.returncode, err)
    if not p.stdout:                              # rc=0 but nothing captured — never return a
        return None, "pdftotext-empty-stdout"     # bare None, which reads as a missing reason
    return p.stdout, None


def doc_pages(src, stem, have_txt):
    """(pages, method) for one document; pages split on the \\f page breaks pdftotext emits.
    A pre-extracted .txt wins over the .pdf (the sealed-box path)."""
    if have_txt:
        with open(os.path.join(src, stem + ".txt"), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        method = "txt"
    else:
        text, reason = extract_pdftotext(os.path.join(src, stem + ".pdf"))
        if text is None:
            return None, reason
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


# ---------- section splitting (the "per-chapter notes" upgrade path) ----------
#
# Splits a big document on its RUNNING HEADER — the line a publisher repeats at the top of
# every page of a chapter — because that is the one structural signal present in a flat text
# extraction. It is a HEURISTIC over layout, not a parsed outline (poppler's `pdftotext` emits
# no bookmark tree), so the contract is deliberately conservative:
#   * a section boundary only ever splits a document into MORE notes of the SAME text — no
#     page is dropped, reordered or rewritten, and absolute page markers are preserved, so a
#     mis-placed boundary costs retrieval precision, never ground-truth fidelity;
#   * a document whose headers yield one section falls back to exactly today's whole-PDF note.
# Titles are compared by TOKEN PREFIX because a two-up scan puts two column headers on one
# line ("Cisco 850 Series Cisco 850 Series"), which exact-matching would split into confetti.

_MIN_PREFIX_TOKENS = 3          # shared leading tokens required to stay in the same section
_MAX_TITLE_TOKENS = 8


def page_header(pg):
    """The page's running header: its first substantial line, normalized."""
    for ln in pg.splitlines():
        t = re.sub(r"\s+", " ", ln).strip()
        t = re.sub(r"^Notes\s+", "", t)                  # a Notes page carries the next header
        t = re.sub(r"\bcontinued\b", " ", t, flags=re.I)  # "... continued" is the same section
        t = re.sub(r"\s+", " ", t).strip()
        if len(t) >= 4:
            return t
    return ""


def _common_prefix(a_tokens, b_tokens):
    out = []
    for x, y in zip(a_tokens, b_tokens):
        if x.lower() != y.lower():
            break
        out.append(x)
    return out


def _undouble(tokens):
    """'Cisco 7600 Series Cisco 7600 Series' -> 'Cisco 7600 Series' (two-up header echo)."""
    n = len(tokens)
    if n >= 2 and n % 2 == 0:
        half = n // 2
        if [t.lower() for t in tokens[:half]] == [t.lower() for t in tokens[half:]]:
            return tokens[:half]
    return tokens


def sections(pages, min_pages=2):
    """[(start_page_1based, pages_slice, title)] grouped by running header.

    Runs shorter than `min_pages` are folded into the PREVIOUS section: covers, dividers and
    stray one-page interludes are not their own chapter, and emitting them as standalone notes
    is the failure mode that makes a split corpus noisier than the single note it replaced."""
    heads = [page_header(pg) for pg in pages]
    runs = []                                    # [start_idx, end_idx, title_tokens]
    for i, h in enumerate(heads):
        if runs:
            cp = _common_prefix(runs[-1][2], h.split())
            if len(cp) >= _MIN_PREFIX_TOKENS:
                runs[-1][1], runs[-1][2] = i, cp
                continue
        runs.append([i, i, h.split()])
    merged = []
    for r in runs:
        if merged and (r[1] - r[0] + 1) < min_pages:
            merged[-1][1] = r[1]                 # absorb the short run, keep the earlier title
        else:
            merged.append(r)
    out = []
    for a, b, toks in merged:
        title = " ".join(_undouble(toks)[:_MAX_TITLE_TOKENS]).strip()
        out.append((a + 1, pages[a:b + 1], title or None))
    return out


def build(src, domain, url_base, family, version, guide, kind, chunk_pages,
          split_sections=False, min_section_pages=2):
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
        if split_sections:
            parts = sections(pages, min_section_pages)
        else:
            n_chunks = 1 if chunk_pages <= 0 else -(-len(pages) // chunk_pages)
            parts = [(s, sl, None) for s, sl in chunks(pages, chunk_pages)]
        if split_sections:
            n_chunks = len(parts)
        seen_tails = set()
        for start, sl, label in parts:
            end = start + len(sl) - 1
            if label:
                # Subject tails read as citations ("kb:19293-cisco-routers-cisco-2800-series").
                # A repeated running header (a chapter resumed later in the book) would collide,
                # and a silent overwrite would drop pages — so disambiguate with the page range.
                tail = "%s-%s" % (stem_slug, slugify(label))
                if tail in seen_tails:
                    tail = "%s-p%04d-%04d" % (tail, start, end)
                seen_tails.add(tail)
                title = "%s — %s" % (doc_title, label)
            elif n_chunks == 1:
                tail, title = stem_slug, doc_title
            else:
                tail = "%s-p%04d-%04d" % (stem_slug, start, end)
                title = "%s — pages %d-%d" % (doc_title, start, end)
            url = url_base.rstrip("/") + "/" + tail
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
    ap.add_argument("--split-sections", action="store_true",
                    help="one record per DOCUMENT SECTION (grouped by running header) instead "
                         "of one per PDF — see sections(); mutually exclusive with --chunk-pages")
    ap.add_argument("--min-section-pages", type=int, default=2,
                    help="runs shorter than this fold into the previous section (default: 2)")
    ap.add_argument("--append", action="store_true",
                    help="merge into an existing corpora/<domain>/index.jsonl (dedup by url; "
                         "new harvest wins)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    if args.split_sections and args.chunk_pages > 0:
        raise SystemExit("--split-sections and --chunk-pages are mutually exclusive: pick either the document's own sections or fixed-size windows")
    if not os.path.isdir(args.src):
        raise SystemExit("--src not found: %s" % args.src)
    url_base = args.url_base or ("pdf://" + args.domain)
    recs, bodies, skipped, methods = build(
        args.src, args.domain, url_base, args.family or args.domain,
        args.version, args.guide, args.kind, args.chunk_pages,
        args.split_sections, args.min_section_pages)

    outdir = os.path.join(str(paths.CORPORA), args.domain)
    rel = os.path.relpath(outdir, ROOT)
    n_docs = len(methods)
    print("domain=%s  src=%s" % (args.domain, args.src))
    print("pdf docs extracted=%d (%s)  records=%d" % (
        n_docs, ", ".join(sorted(set(methods.values()))) or "none", len(recs)))
    if skipped:  # never a silent cap: name what was dropped and why
        print("SKIPPED %d: %s" % (len(skipped), ", ".join("%s [%s]" % s for s in skipped)))
        if any("not-installed" in r for _, r in skipped):
            print("  -> poppler's pdftotext was not found. Install it, pin it with "
                  "WIKIKB_PDFTOTEXT=/path/to/pdftotext, or ship a pre-extracted <name>.txt "
                  "beside the .pdf (the sealed-box path).")
    print("target: %s/index.jsonl + %s/bodies/*.md" % (rel, rel))
    if recs:
        print("sample url: %s  (cite it as kb:%s)" % (recs[0]["url"],
                                                      recs[0]["url"].rsplit("/", 1)[-1]))
    if not recs and not skipped:
        raise SystemExit("no .pdf/.txt documents found in --src")
    # Converting NOTHING while holding documents is a failure, not a clean no-op. Exiting 0 here
    # let the upload job report `state: done` with every step green while zero notes reached the
    # vault — the caller had uploaded a PDF and been told it worked. The job runner stops the
    # chain on a non-zero exit, so this is also what keeps corpus_to_vault from running against
    # an index this run contributed nothing to.
    if not recs:
        raise SystemExit("extracted 0 of %d document(s) — nothing to write (see SKIPPED above)"
                         % len(skipped))

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
