#!/usr/bin/env python3
"""embed.py — local, offline dense-embedding index over the reference tier. Phase 3.

The semantic-recall layer that kills the lexical miss-cascade (paraphrases like "proof of
possession" -> the DPoP note; "operations master role permanently offline" -> the seize-FSMO
note). It is the ONLY component permitted a third-party dependency, and only a LOCAL one:

  - sentence-transformers + a model VENDORED at `_meta/models/<name>/` (default
    bge-small-en-v1.5), loaded BY PATH, no network — ever. See `_meta/models/README.md`
    for the offline vendoring step.
  - numpy for vector storage/cosine.

Both are imported LAZILY (inside functions), so `import embed` stays stdlib-safe: kb.py and
eval.py import this module and call into it guarded by try/except, degrading to LEXICAL when
the library, model, or index is absent (graceful, not a hard dep — the air-gap invariant).

The index is a DERIVED, REGENERABLE artifact under `_meta/embeddings/` (like the routing
indexes and the reference lock), never a source of truth. It is DELTA-AWARE: a note is
re-embedded only when its content hash changes (same sha256 scheme manifest.py uses).

Usage (once the model + libs are vendored):
    python3 embed.py --domain keycloak --build            # build/update the index (delta)
    python3 embed.py --domain keycloak --status           # index freshness vs the notes
    python3 embed.py --domain keycloak --query "proof of possession token binding"
    python3 embed.py --domains                            # list domains + index state
"""
import argparse
import hashlib
import json
import os
import re
import sys

from wikikb import paths
WIKI = str(paths.WIKI)
META = str(paths.META)
EMB_DIR = str(paths.EMBEDDINGS)
MODELS_DIR = str(paths.MODELS)
DEFAULT_MODEL = "bge-small-en-v1.5"
# bge-* retrieval wants this instruction on the QUERY side only (passages stay raw).
DEFAULT_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
MAX_CHUNK_CHARS = 1800        # ~roughly a section; long sections are windowed
CHARS_PER_TOKEN = 4

sys.dont_write_bytecode = True
from wikikb.retrieval import kb                     # stdlib: reuse the reference-tier loader (slug + body + title)


# ---------- availability (never raises on import) -------------------------------------

def model_path(model=DEFAULT_MODEL):
    return os.path.join(MODELS_DIR, model)


def have_library():
    try:
        import sentence_transformers  # noqa: F401
        import numpy  # noqa: F401
        return True
    except Exception:
        return False


def have_model(model=DEFAULT_MODEL):
    p = model_path(model)
    return os.path.isdir(p) and bool(os.listdir(p))


def available(model=DEFAULT_MODEL):
    """True iff the dense path can run: library importable AND model vendored on disk."""
    return have_library() and have_model(model)


def status_str(model=DEFAULT_MODEL):
    return "library=%s model[%s]=%s" % (
        "yes" if have_library() else "NO (install sentence-transformers + numpy, offline)",
        model, "yes" if have_model(model) else "NO (vendor to %s/)" % os.path.relpath(model_path(model), WIKI))


# ---------- chunking (stdlib) ---------------------------------------------------------

_HEAD = re.compile(r"^#{2,3}\s+\S", re.MULTILINE)


def chunk_note(title, body):
    """Split a reference note into heading-bounded chunks. The title is prepended to the
    first chunk so title/slug-overlap queries match it. Long sections are windowed."""
    text = ("TITLE: %s\n%s" % (title, body)).strip()
    # split at ## / ### headings, keeping each heading with its section
    idxs = [m.start() for m in _HEAD.finditer(text)]
    spans = []
    bounds = [0] + idxs + [len(text)]
    # the lead (before first heading) is its own chunk; then each heading-section
    seen = set()
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        if a in seen:
            continue
        seen.add(a)
        seg = text[a:b].strip()
        if seg:
            spans.append(seg)
    # window any oversized section
    chunks = []
    for seg in spans:
        if len(seg) <= MAX_CHUNK_CHARS:
            chunks.append(seg)
        else:
            for j in range(0, len(seg), MAX_CHUNK_CHARS):
                chunks.append(seg[j:j + MAX_CHUNK_CHARS])
    return chunks or [text[:MAX_CHUNK_CHARS]]


def note_hash(body):
    """Same sha256[:16] scheme manifest.py uses, applied to a reference note body."""
    return "sha256:" + hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


# ---------- index paths ---------------------------------------------------------------

def vec_path(domain):
    return os.path.join(EMB_DIR, "%s.npz" % domain)


def meta_path(domain):
    return os.path.join(EMB_DIR, "%s.json" % domain)


def index_exists(domain):
    return os.path.isfile(vec_path(domain)) and os.path.isfile(meta_path(domain))


def load_meta(domain):
    if not os.path.isfile(meta_path(domain)):
        return None
    with open(meta_path(domain), encoding="utf-8") as fh:
        return json.load(fh)


# ---------- build (delta-aware; needs the library + model) ----------------------------

def _encoder(model=DEFAULT_MODEL):
    from sentence_transformers import SentenceTransformer  # lazy
    return SentenceTransformer(model_path(model))          # load BY PATH — no network


def build(domain, model=DEFAULT_MODEL, query_prefix=DEFAULT_QUERY_PREFIX, apply=True):
    """(Re)build the dense index for a domain, re-embedding only changed notes."""
    if not have_library():
        raise SystemExit("dense layer unavailable: %s" % status_str(model))
    if not have_model(model):
        raise SystemExit("model not vendored: %s  (see _meta/models/README.md)" % status_str(model))
    import numpy as np  # lazy

    recs = kb.load(domain) or []
    recs = [r for r in recs if r.get("body_status") == "fetched"]
    cur_hash = {r["id"]: note_hash(kb.body_text(r)) for r in recs}

    old = load_meta(domain) or {}
    old_hash = old.get("note_hash", {})
    reuse = {s for s in cur_hash if old_hash.get(s) == cur_hash[s]}
    changed = [r for r in recs if r["id"] not in reuse]

    # carry over unchanged vectors
    rows, vecs = [], []
    if reuse and index_exists(domain):
        oldvecs = np.load(vec_path(domain))["vectors"]
        for i, row in enumerate(old.get("rows", [])):
            if row["slug"] in reuse:
                rows.append(row)
                vecs.append(oldvecs[i])

    # embed changed/new notes
    if changed:
        enc = _encoder(model)
        texts, newrows = [], []
        for r in changed:
            for ci, ch in enumerate(chunk_note(r.get("title", r["id"]), kb.body_text(r))):
                texts.append(ch)
                newrows.append({"slug": r["id"], "chunk": ci,
                                "heading": ch.split("\n", 1)[0][:80]})
        embs = enc.encode(texts, normalize_embeddings=True, batch_size=64,
                          show_progress_bar=False)
        for row, v in zip(newrows, embs):
            rows.append(row)
            vecs.append(np.asarray(v, dtype="float32"))

    vectors = np.vstack(vecs).astype("float32") if vecs else np.zeros((0, 0), dtype="float32")
    meta = {"model": model, "query_prefix": query_prefix,
            "dim": int(vectors.shape[1]) if vectors.size else 0,
            "rows": rows, "note_hash": cur_hash}

    print("domain=%s notes=%d  reused=%d  re-embedded=%d  chunks=%d  dim=%d"
          % (domain, len(recs), len(reuse), len(changed), len(rows), meta["dim"]))
    if apply:
        os.makedirs(EMB_DIR, exist_ok=True)
        np.savez_compressed(vec_path(domain), vectors=vectors)
        with open(meta_path(domain), "w", encoding="utf-8") as fh:
            json.dump(meta, fh)
        print("wrote %s + %s" % (os.path.relpath(vec_path(domain), WIKI),
                                 os.path.relpath(meta_path(domain), WIKI)))
    return meta


def build_status(domain, model=DEFAULT_MODEL):
    """Report delta state without building (stdlib only — no library needed)."""
    recs = [r for r in (kb.load(domain) or []) if r.get("body_status") == "fetched"]
    cur = {r["id"]: note_hash(kb.body_text(r)) for r in recs}
    old = (load_meta(domain) or {}).get("note_hash", {})
    new = [s for s in cur if s not in old]
    changed = [s for s in cur if s in old and old[s] != cur[s]]
    gone = [s for s in old if s not in cur]
    fresh = index_exists(domain) and not new and not changed and not gone
    print("domain=%s  index=%s  notes=%d  new=%d changed=%d gone=%d  -> %s"
          % (domain, "present" if index_exists(domain) else "ABSENT", len(cur),
             len(new), len(changed), len(gone), "fresh" if fresh else "STALE (run --build)"))
    return fresh


# ---------- dense query (needs the library + model + index) ---------------------------

def dense_rank(domain, query, topn=50):
    """Return [(note_slug, dense_score)] best-first, or None if the dense path is
    unavailable (library/model/index absent) — callers fall back to lexical."""
    if not available() or not index_exists(domain):
        return None
    import numpy as np  # lazy
    meta = load_meta(domain)
    if not meta or not meta.get("rows"):
        return None
    vectors = np.load(vec_path(domain))["vectors"]
    if vectors.size == 0:
        return None
    enc = _encoder(meta.get("model", DEFAULT_MODEL))
    qv = enc.encode([meta.get("query_prefix", "") + query], normalize_embeddings=True)[0]
    sims = vectors @ np.asarray(qv, dtype="float32")        # cosine (rows are normalized)
    best = {}
    for row, s in zip(meta["rows"], sims):                   # max sim over a note's chunks
        slug = row["slug"]
        if slug not in best or s > best[slug]:
            best[slug] = float(s)
    ranked = sorted(best.items(), key=lambda kv: -kv[1])
    return ranked[:topn]


# ---------- RRF fusion (pure stdlib — shared by kb.py / eval.py) -----------------------

def rrf_fuse(lex_ids, dense_ids, k=60):
    """Reciprocal Rank Fusion of two best-first id lists. Either may be empty/None."""
    score = {}
    for lst in (lex_ids or [], [s for s, _ in (dense_ids or [])]):
        for rank, sid in enumerate(lst, 1):
            score[sid] = score.get(sid, 0.0) + 1.0 / (k + rank)
    return [s for s, _ in sorted(score.items(), key=lambda kv: -kv[1])]


# ---------- CLI -----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain")
    ap.add_argument("--domains", action="store_true", help="list domains + index/library state")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--query")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--dry-run", action="store_true", help="with --build: don't write")
    args = ap.parse_args()

    if args.domains:
        print("dense layer: %s" % status_str(args.model))
        for d in kb.available_domains():
            build_status(d, args.model)
        return
    if not args.domain:
        print("need --domain <name> (or --domains). dense layer: %s" % status_str(args.model))
        sys.exit(2)
    if args.build:
        build(args.domain, args.model, apply=not args.dry_run)
    elif args.status:
        build_status(args.domain, args.model)
    elif args.query:
        r = dense_rank(args.domain, args.query)
        if r is None:
            print("dense unavailable (%s) — lexical only." % status_str(args.model))
            sys.exit(0)
        for i, (slug, sc) in enumerate(r[:10], 1):
            print("%2d. %.4f  %s" % (i, sc, slug))
    else:
        build_status(args.domain, args.model)


if __name__ == "__main__":
    main()
