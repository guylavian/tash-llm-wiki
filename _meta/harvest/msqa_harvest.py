#!/usr/bin/env python3
"""msqa_harvest.py — harvest Microsoft Q&A threads into the `_sources/<domain>/qa/` raw tier.

DELIBERATELY OUTSIDE the `wikikb` package. Every wikikb tool is stdlib-only AND offline (selftest
carries a network/DNS tripwire); this one opens sockets, so it lives here instead — the same shape
as the original doc harvests that produced `_sources/<domain>/_raw/`. Harvest happens externally,
then the wiki folds the result in. Nothing here is imported by the air-gapped toolchain.

WHAT IT WRITES
  `_sources/<domain>/qa/<id>-<slug>.md` — one note per thread, the `web:` provenance tier.
  These become the IMMUTABLE raw material an INGEST pass synthesizes from; they are NOT wiki pages.

WHY IT IS SAFE TO RUN
  * Enumeration comes from Microsoft's OWN published sitemap, which robots.txt advertises
    (`Sitemap: https://learn.microsoft.com/answers/sitemaps/sitemap.xml`).
  * It fetches ONLY `/en-us/answers/questions/<id>/<slug>` pages, which robots.txt does not
    disallow. It never touches the disallowed surfaces: /answers/search, /answers/users/,
    /answers/revisions/, /answers/comments, or any `?sort= ?filterby= ?orderby= ?pagesize= ?topics=`
    browse URL.
  * Content is read from the page's `schema.org/QAPage` JSON-LD block — structured data the site
    publishes for machines. No HTML scraping, no login, no cookies, no token.
  * Rate-limited and backs off on 429/5xx. Resumable: an existing output file is skipped, so an
    interrupted run costs nothing.

PROVENANCE HONESTY — the reason each note records authorRole/affiliations
  A Q&A answer is COMMUNITY content, not a vendor support statement, and accepted answers are
  routinely wrong or version-stale. Every note therefore carries `tier: community-qa`, the fetch
  date, and per-answer author role/affiliation so a later INGEST can weight a Microsoft employee's
  answer differently from an anonymous one. Pages synthesized from these MUST cite them as
  `web:<url> (fetched DATE)` under an explicit community/upstream heading — never as `kb:`.

    python3 _meta/harvest/msqa_harvest.py --domain sccm --limit 20        # validate the shape
    python3 _meta/harvest/msqa_harvest.py --domain sccm                   # whole domain, resumable
    python3 _meta/harvest/msqa_harvest.py --all --delay 0.5
"""
import argparse
import concurrent.futures as cf
import html
import json
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)                       # _meta/ -> vault root is one up
VAULT = os.path.dirname(HERE) if os.path.basename(HERE) != "harvest" else os.path.dirname(os.path.dirname(HERE))
SOURCES = os.path.join(VAULT, "_sources")
UA = "llm-wiki-harvest/1.0 (personal offline knowledge base; contact via repo owner)"
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

_print_lock = threading.Lock()


def log(msg):
    with _print_lock:
        print(msg, flush=True)


# ---------- html -> text ------------------------------------------------------------------

def detag(s):
    """JSON-LD `text` fields carry HTML. Reduce to readable markdown-ish plain text.
    Code blocks are preserved as fences because half the value of a Q&A answer is the command."""
    if not s:
        return ""
    s = re.sub(r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>",
               lambda m: "\n```\n" + html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() + "\n```\n",
               s, flags=re.S)
    s = re.sub(r"<code[^>]*>(.*?)</code>", lambda m: "`" + re.sub(r"<[^>]+>", "", m.group(1)) + "`", s, flags=re.S)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"</(p|div|li|ul|ol|h[1-6]|blockquote)>", "\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:80] or "q"


# ---------- fetch -------------------------------------------------------------------------

def fetch(url, tries=4, timeout=30):
    """GET with backoff. Returns text, or None when the page is genuinely unavailable."""
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None                                   # thread deleted — not an error
            if e.code in (429, 500, 502, 503, 504):
                wait = (2 ** attempt) + random.random()        # back off, be a good citizen
                log(f"    HTTP {e.code} on {url.rsplit('/',1)[-1][:40]} — sleeping {wait:.1f}s")
                time.sleep(wait)
                continue
            return None
        except Exception:                                     # noqa: BLE001 — transient network
            time.sleep((2 ** attempt) + random.random())
    return None


def page_tags(page_html):
    """The thread's OWN tags, as Microsoft classifies it — NOT my slug guess.

    The question's tags render near the top of the document; the sidebar's generic "popular tags"
    block renders much later. Taking only anchors from the leading fraction separates them (verified:
    an Exchange thread yields exactly `office-exchange-online`, while a whole-page scan yields 17
    unrelated windows-home tags). This is what makes routing precise — a slug containing "pxe" or
    "wsus" is frequently a consumer Surface question, and the tag says so."""
    head = page_html[:int(len(page_html) * 0.4)]
    return sorted({slug for _id, slug in re.findall(r"/en-us/answers/tags/(\d+)/([a-z0-9-]+)", head)})


# tag-substring -> wiki domain. First match wins; a thread whose tags map nowhere is DROPPED
# rather than filed under a guess (an unrouted note is corpus noise the INGEST pass would have
# to re-filter). Extend as the sample surfaces new tag families.
TAG_ROUTES = [
    ("configuration-manager", "sccm"), ("configmgr", "sccm"), ("mecm", "sccm"), ("intune-configmgr", "sccm"),
    ("exchange", "exchange"),
    ("sharepoint", "sharepoint"),
    ("powershell", "powershell"),
    ("windows-server", "windows-server"),
    ("active-directory", "active-directory"),
]

# Hard drop, checked BEFORE routing: Entra ID / Entra Connect is CLOUD identity, and this vault's
# active-directory domain is on-prem AD DS. Entra threads were 350+33 of the first 992 harvested and
# would have swamped the domain with out-of-scope cloud content. ADFS is NOT dropped — it is an
# on-prem role and matches "active-directory" below.
TAG_DROP = ("entra",)


def route(tags, fallback):
    if any(d in t for t in tags for d in TAG_DROP):
        return None
    for t in tags:
        for frag, dom in TAG_ROUTES:
            if frag in t:
                return dom
    return fallback if not tags else None      # tagged but unmapped -> drop; untagged -> keyword guess


def parse_qa(page_html):
    """Pull the schema.org QAPage payload. None when the page carries no Q&A structured data."""
    for block in LD_RE.findall(page_html):
        try:
            d = json.loads(block)
        except ValueError:
            continue
        if d.get("@type") == "QAPage" and isinstance(d.get("mainEntity"), dict):
            return d["mainEntity"]
    return None


def answers_of(mn):
    """[(kind, answer_dict)] — accepted first, then moderator-recommended, then the rest."""
    out = []
    if isinstance(mn.get("acceptedAnswer"), dict):
        out.append(("accepted", mn["acceptedAnswer"]))
    for a in mn.get("moderatorRecommendedAnswers") or []:
        if isinstance(a, dict):
            out.append(("recommended", a))
    sa = mn.get("suggestedAnswer")
    for a in (sa if isinstance(sa, list) else [sa] if isinstance(sa, dict) else []):
        if isinstance(a, dict):
            out.append(("community", a))
    return out


def yaml_q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip() + '"'


def render(url, qid, mn, fetched, tags):
    ans = answers_of(mn)
    has_accepted = any(k == "accepted" for k, _ in ans)
    roles = sorted({(a.get("authorRole") or "").strip() for _, a in ans if a.get("authorRole")})
    affil = sorted({x for _, a in ans for x in (a.get("authorAffiliations") or []) if x})

    fm = [
        "---",
        f"title: {yaml_q(mn.get('name') or 'Untitled')}",
        "type: source",
        "tier: community-qa",
        f"source: {url}",
        f"question_id: {qid}",
        f"fetched: {fetched}",
        f"answer_count: {mn.get('answerCount') or len(ans)}",
        f"has_accepted_answer: {'true' if has_accepted else 'false'}",
        f"upvotes: {mn.get('upvoteCount') or 0}",
        ("qa_tags: [" + ", ".join(yaml_q(x) for x in tags) + "]") if tags else "qa_tags: []",
    ]
    if roles:
        fm.append("answer_author_roles: [" + ", ".join(yaml_q(r) for r in roles) + "]")
    if affil:
        fm.append("answer_author_affiliations: [" + ", ".join(yaml_q(a) for a in affil) + "]")
    fm.append("---")

    body = [
        "",
        f"# {mn.get('name') or 'Untitled'}",
        "",
        "> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.",
        "> Accepted answers are frequently version-stale or wrong. Cite as",
        f"> `web:{url} (fetched {fetched})` and verify against vendor documentation before relying on it.",
        "",
        "## Question",
        "",
        detag(mn.get("text")),
        "",
    ]
    for kind, a in ans:
        role = a.get("authorRole") or "community member"
        aff = ", ".join(a.get("authorAffiliations") or [])
        head = f"## Answer ({kind}) — {role}" + (f" [{aff}]" if aff else "")
        body += [head, "", f"*upvotes: {a.get('upvoteCount') or 0}"
                          + (f" · updated: {a['updatedAt'][:10]}" if a.get("updatedAt") else "") + "*", "",
                 detag(a.get("text")), ""]
    if not ans:
        body += ["## Answers", "", "_No answers on this thread._", ""]
    return "\n".join(fm) + "\n".join(body).rstrip() + "\n"


def harvest_one(url, outdir, fetched, fallback):
    m = re.search(r"/questions/(\d+)/([a-z0-9-]*)", url)
    if not m:
        return "skip"
    qid, slug = m.group(1), m.group(2)
    out = os.path.join(outdir, f"{qid}-{slugify(slug)}.md")
    if os.path.exists(out):
        return "cached"
    page = fetch(url)
    if page is None:
        return "gone"
    mn = parse_qa(page)
    if not mn:
        return "nold"
    tags = page_tags(page)
    dom = route(tags, fallback)
    if dom is None:
        return "offtopic"                                  # tagged, but not one of our domains
    if dom != fallback:                                    # Microsoft's taxonomy overrules the slug guess
        outdir = os.path.join(SOURCES, dom, "qa")
        os.makedirs(outdir, exist_ok=True)
        out = os.path.join(outdir, f"{qid}-{slugify(slug)}.md")
        if os.path.exists(out):
            return "cached"
    text = render(url, qid, mn, fetched, tags)
    tmp = out + ".part"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, out)                                   # atomic: no half-written note on Ctrl-C
    return "wrote"


def run_domain(domain, urls, delay, workers, limit):
    outdir = os.path.join(SOURCES, domain, "qa")
    os.makedirs(outdir, exist_ok=True)
    fetched = date.today().isoformat()
    if limit:
        urls = urls[:limit]
    counts = {}
    lock = threading.Lock()
    done = [0]

    def work(u):
        time.sleep(delay * random.uniform(0.7, 1.3))       # jitter: don't hammer in lockstep
        r = harvest_one(u, outdir, fetched, domain)
        with lock:
            counts[r] = counts.get(r, 0) + 1
            done[0] += 1
            if done[0] % 100 == 0:
                log(f"  [{domain}] {done[0]}/{len(urls)}  {counts}")
        return r

    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(work, urls))
    log(f"[{domain}] DONE {done[0]} urls -> {counts}  ({outdir})")
    return counts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--urls-dir", default="/tmp/msqa", help="dir holding urls-<domain>.txt from the sitemap pass")
    ap.add_argument("--domain", action="append", help="repeatable; default = every urls-*.txt present")
    ap.add_argument("--limit", type=int, help="stop after N urls per domain (validation runs)")
    ap.add_argument("--delay", type=float, default=0.5, help="per-worker sleep between requests")
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()

    doms = args.domain
    if not doms:
        doms = sorted(f[5:-4] for f in os.listdir(args.urls_dir)
                      if f.startswith("urls-") and f.endswith(".txt") and f != "urls-relevant.txt")
    total = {}
    for d in doms:
        p = os.path.join(args.urls_dir, f"urls-{d}.txt")
        if not os.path.isfile(p):
            log(f"[{d}] no {p} — skipping")
            continue
        urls = [l.strip() for l in open(p, encoding="utf-8") if l.strip()]
        log(f"[{d}] {len(urls)} urls  (delay={args.delay}s workers={args.workers})")
        for k, v in run_domain(d, urls, args.delay, args.workers, args.limit).items():
            total[k] = total.get(k, 0) + v
    log(f"TOTAL {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
