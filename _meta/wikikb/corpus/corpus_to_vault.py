#!/usr/bin/env python3
"""corpus_to_vault.py — fold a raw corpus into the Obsidian vault. stdlib only, no network.

"Obsidian rules all the KBs and the data": instead of querying a corpus through a
bespoke tool (kb.py), the raw documents become first-class Obsidian reference notes
inside the vault. After migration the vault physically contains all the data and
retrieval is plain tiered reads + grep over Markdown — no corpus query tool.

For each record in corpora/<domain>/index.jsonl:
  - body present (body_status == fetched) -> wiki/reference/<domain>/<slug>.md
        frontmatter (title, type: reference, domain, source url, guide, version,
        family, primary) + the body text.
  - body absent (subscriber-gated) -> one pointer row in
        wiki/reference/<domain>/_gated-kb-index.md (title + url + abstract), so the
        pointers live in the vault too without thousands of stub files.

Reference notes are a distinct tier: linkable + greppable, but NOT synthesized
pages — lint.py does not scan them for page discipline and index.py does not list
them in the routing index (it only counts them).

Usage:
    python3 -m wikikb corpus_to_vault --domain keycloak            # dry-run + sample
    python3 -m wikikb corpus_to_vault --domain keycloak --apply    # write the notes
"""
import argparse
import hashlib
import json
import os
import re
import sys

from wikikb import paths
ROOT = str(paths.ROOT)
CORPORA = str(paths.CORPORA)
WIKI = str(paths.WIKI)
REF = str(paths.REFERENCE)
# The lock hashes reference/<domain>/ — it is VAULT DATA, so it must follow WIKI (which
# WIKIKB_VAULT_ROOT redirects), NOT META (which it does not). Pointing it at META made a
# sandboxed run write its lock into the LIVE repo while its notes went to the sandbox.
# The original crash under the override was a missing parent dir, not the wrong root.
LOCK = os.path.join(WIKI, "_meta", "reference.lock.json")


def corpus_records(domain):
    index = os.path.join(CORPORA, domain, "index.jsonl")
    if not os.path.isfile(index):
        return None
    out = []
    with open(index, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def body_text(domain, r):
    bf = r.get("body_file")
    if not bf:
        return ""
    p = os.path.join(CORPORA, domain, bf)
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


_slug_bad = re.compile(r"[^a-z0-9]+")


def url_tail(url):
    tail = (url or "").rstrip("/").rsplit("/", 1)[-1]
    return tail or "doc"


def base_slug(r):
    """Human-ish, stable slug from family-version-urltail (unique-ish; deduped below)."""
    fam = (r.get("family") or "doc")
    ver = (r.get("version") or "").replace(".", "-")
    tail = url_tail(r.get("url"))
    raw = "-".join(p for p in (fam, ver, tail) if p)
    s = _slug_bad.sub("-", raw.lower()).strip("-")
    return s or "doc"


def yaml_q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_note(domain, r, slug):
    fm = ["---",
          f"title: {yaml_q(r.get('title') or slug)}",
          "type: reference",
          f"domain: {domain}",
          f"slug: {slug}",
          "tier: reference"]
    if r.get("url"):
        fm.append(f"source: {r['url']}")
    for k in ("guide", "version", "family", "documentKind"):
        if r.get(k):
            fm.append(f"{k}: {yaml_q(r[k])}" if k == "documentKind" else f"{k}: {r[k]}")
    if r.get("primary"):
        fm.append("primary: true")
    ab = re.sub(r"\s+", " ", (r.get("abstract") or "")).strip()
    if ab:
        fm.append(f"abstract: {yaml_q(ab)}")  # restores kb.py's abstract ranking signal
    fm.append("---")
    body = body_text(domain, r).strip()
    title = r.get("title") or slug
    return "\n".join(fm) + f"\n\n# {title}\n\n{body}\n"


def render_gated_index(domain, gated):
    lines = ["---", f"title: {yaml_q(domain + ' — gated KB pointers')}",
             "type: reference", f"domain: {domain}", "slug: _gated-kb-index",
             "tier: reference", "---", "",
             f"# {domain} — gated KB pointers ({len(gated)})", "",
             "_Subscriber-gated records (no public body in the harvest). Title + URL +",
             "abstract only; open the URL with a login for the full text._", ""]
    for r in sorted(gated, key=lambda x: (x.get("title") or "")):
        lines.append(f"## {r.get('title') or '(untitled)'}")
        if r.get("url"):
            lines.append(f"- {r['url']}")
        ab = (r.get("abstract") or "").strip()
        if ab:
            lines.append(f"- {re.sub(chr(92)+'s+', ' ', ab)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def plan(domain):
    recs = corpus_records(domain)
    if recs is None:
        return None
    fetched = [r for r in recs if r.get("body_status") == "fetched" and r.get("body_file")]
    gated = [r for r in recs if not (r.get("body_status") == "fetched" and r.get("body_file"))]
    # assign unique slugs
    seen, assigned = {}, []
    for r in fetched:
        b = base_slug(r)
        n = seen.get(b, 0)
        seen[b] = n + 1
        slug = b if n == 0 else f"{b}-{n+1}"
        assigned.append((slug, r))
    return {"recs": recs, "fetched": assigned, "gated": gated}


# ---------- integrity lock (FIX 2) ----------
# "Immutable" reference notes are only a convention now that they're editable Markdown.
# The lock stores a sha256 per *managed* reference note (the body notes + the gated index
# this tool writes) so a bare hand-edit in Obsidian is detectable; the regenerated
# `_ref-*` group/hub indexes (index.py's) are excluded — they legitimately change.

def _sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def reference_domains():
    if not os.path.isdir(REF):
        return []
    return sorted(d for d in os.listdir(REF) if os.path.isdir(os.path.join(REF, d)))


def managed_notes(domain):
    """Corpus-managed reference notes: body notes + `_gated-kb-index.md`; excludes the
    `_ref-*` indexes that index.py regenerates."""
    d = os.path.join(REF, domain)
    if not os.path.isdir(d):
        return []
    return sorted(fn for fn in os.listdir(d) if fn.endswith(".md") and not fn.startswith("_ref-"))


def _load_lock():
    if os.path.isfile(LOCK):
        with open(LOCK, encoding="utf-8") as fh:
            return json.load(fh)
    return {"algo": "sha256", "notes": {}}


def write_lock(domain):
    lock = _load_lock()
    d = os.path.join(REF, domain)
    lock.setdefault("notes", {})[domain] = {fn: _sha256(os.path.join(d, fn))
                                            for fn in managed_notes(domain)}
    os.makedirs(os.path.dirname(LOCK), exist_ok=True)   # sandboxed vault (WIKIKB_VAULT_ROOT) has no _meta/ yet
    with open(LOCK, "w", encoding="utf-8") as fh:
        json.dump(lock, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return len(lock["notes"][domain])


def cmd_lock():
    doms = reference_domains()
    total = 0
    for dom in doms:
        n = write_lock(dom)
        total += n
        print(f"locked {dom}: {n} reference notes")
    print(f"baseline -> {os.path.relpath(LOCK, ROOT)} ({total} notes, {len(doms)} domain(s))")


def cmd_verify():
    """Read-only. Recompute hashes, report added/removed/modified. Returns True on drift.
    Never writes a reference note (or the lock)."""
    if not os.path.isfile(LOCK):
        print("reference.lock.json not found — run `corpus_to_vault.py --lock` to baseline (skipping)")
        return False
    locked = _load_lock().get("notes", {})
    drift = False
    for dom in sorted(set(locked) | set(reference_domains())):
        want = locked.get(dom, {})
        d = os.path.join(REF, dom)
        have = {fn: _sha256(os.path.join(d, fn)) for fn in managed_notes(dom)}
        modified = sorted(fn for fn in want if fn in have and have[fn] != want[fn])
        removed = sorted(fn for fn in want if fn not in have)
        added = sorted(fn for fn in have if fn not in want)
        if modified or removed or added:
            drift = True
            print(f"DRIFT reference/{dom}/:")
            for fn in modified:
                print(f"  modified: {fn}")
            for fn in removed:
                print(f"  removed:  {fn}")
            for fn in added:
                print(f"  added:    {fn}")
    if not drift:
        print(f"reference tier intact — {sum(len(v) for v in locked.values())} notes match the lock")
    return drift


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domain", default="keycloak")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--lock", action="store_true",
                    help="(re)baseline _meta/reference.lock.json from the current reference notes")
    ap.add_argument("--verify", action="store_true",
                    help="read-only: report reference-tier drift (added/removed/modified); exit 1 on drift")
    args = ap.parse_args()

    if args.verify:
        sys.exit(1 if cmd_verify() else 0)
    if args.lock:
        cmd_lock()
        return

    p = plan(args.domain)
    if p is None:
        raise SystemExit(f"no corpus at corpora/{args.domain}/index.jsonl")
    outdir = os.path.join(WIKI, "reference", args.domain)
    rel = os.path.relpath(outdir, ROOT)

    print(f"domain={args.domain}  total={len(p['recs'])}  "
          f"body-notes={len(p['fetched'])}  gated-pointers={len(p['gated'])}")
    print(f"target: {rel}/<slug>.md  + {rel}/_gated-kb-index.md")
    print("sample slugs: " + ", ".join(s for s, _ in p["fetched"][:5]))

    if not args.apply:
        print("\n--- DRY RUN (no files written). Sample note below: ---\n")
        if p["fetched"]:
            slug, r = p["fetched"][0]
            note = render_note(args.domain, r, slug)
            print(note[:1400] + ("\n…(truncated)" if len(note) > 1400 else ""))
        print("\nRe-run with --apply to write.")
        return

    os.makedirs(outdir, exist_ok=True)
    for slug, r in p["fetched"]:
        with open(os.path.join(outdir, slug + ".md"), "w", encoding="utf-8") as fh:
            fh.write(render_note(args.domain, r, slug))
    if p["gated"]:
        with open(os.path.join(outdir, "_gated-kb-index.md"), "w", encoding="utf-8") as fh:
            fh.write(render_gated_index(args.domain, p["gated"]))
    n = write_lock(args.domain)
    print(f"\nWROTE {len(p['fetched'])} reference notes + "
          f"{'1 gated index' if p['gated'] else 'no gated index'} to {rel}/ "
          f"(integrity lock refreshed: {n} notes)")


if __name__ == "__main__":
    main()
