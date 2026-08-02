#!/usr/bin/env python3
"""Tag taxonomy tool for the Keycloak/RHBK LLM Wiki — stdlib only, no network.

The controlled vocabulary lives in `wiki/_meta/taxonomy.md` (the single source of
truth; this script parses it). Tags are navigation/faceting aids — never a
substitute for `sources:` or `provenance:`.

  validate   (default) report tags not in the vocabulary + untagged pages
  normalize  rewrite synonym tags to their canonical form   (--apply to write)
  backfill   add heuristic `area` tags (+ `concept` for topics) to pages that
             have none, by matching slug keywords                (--apply to write)

Only edits files under wiki/{topics,entities,questions}/ — never kb/ or references/.
`wiki/_meta/` is never scanned. lint.py imports load_taxonomy()/parse_tags() here.

Usage:
    python3 -m wikikb tags validate
    python3 -m wikikb tags normalize --apply
    python3 -m wikikb tags backfill            # dry-run
    python3 -m wikikb tags backfill --apply
"""
import argparse
import os
import re

from wikikb import paths
META = str(paths.META)
WIKI = str(paths.WIKI)
TAXONOMY = str(paths.TAXONOMY)
PAGE_DIRS = paths.PAGE_DIRS
FM_RE = re.compile(r"^(---\n)(.*?)(\n---)", re.DOTALL)
BACKTICK_RE = re.compile(r"`([a-z0-9][a-z0-9.\-]*)`")

# slug-keyword -> area (accumulated; multiple may apply). Order is not significant.
AREA_KEYWORDS = [
    ("tf-", "iac"), ("terraform", "iac"),
    ("operator", "operator"), ("keycloak-cr", "operator"), ("realm-import", "operator"),
    ("olm", "operator"), ("pod-template", "operator"),
    ("ldap", "federation"), ("user-storage", "federation"), ("kerberos", "federation"),
    ("idp", "brokering"), ("identity-provider", "brokering"), ("brokering", "brokering"),
    ("mellon", "brokering"),
    ("authorization", "authz"), ("policy", "authz"), ("permission", "authz"),
    ("protection", "authz"), ("rpt", "authz"), ("uma", "authz"),
    ("requesting-party", "authz"), ("decision-strateg", "authz"), ("enforc", "authz"),
    ("oidc", "clients"), ("saml", "clients"), ("client", "clients"), ("dpop", "clients"),
    ("fapi", "clients"), ("oauth21", "clients"), ("mapper", "clients"),
    ("registration", "clients"),
    ("token", "tokens"), ("session", "tokens"),
    ("ha-", "ha"), ("infinispan", "ha"), ("cache", "ha"), ("multi-site", "ha"),
    ("site-synchron", "ha"), ("load-balancer", "ha"), ("failover", "ha"),
    ("data-grid", "ha"), ("distributed-cache", "ha"),
    ("metric", "observability"), ("trac", "observability"), ("telemetry", "observability"),
    ("health", "observability"), ("sli", "observability"), ("grafana", "observability"),
    ("observability", "observability"), ("otlp", "observability"), ("exemplar", "observability"),
    ("opentelemetry", "observability"),
    ("hostname", "server-config"), ("tls", "server-config"), ("proxy", "server-config"),
    ("database", "server-config"), ("config-source", "server-config"),
    ("build-vs-runtime", "server-config"), ("management", "server-config"),
    ("feature-flag", "server-config"), ("vault", "server-config"),
    ("truststore", "server-config"), ("server-config", "server-config"),
    ("bootstrap-admin", "server-config"),
    ("migration", "migration"), ("rhsso", "migration"), ("rh-sso", "migration"),
    ("adapter", "migration"), ("quarkus-config", "migration"), ("upgrad", "migration"),
    ("spi", "spi"), ("provider-model", "spi"), ("theme", "spi"),
    ("javascript-provider", "spi"), ("override-built", "spi"),
    ("realm-keys", "realm"), ("realm-import-export", "realm"), ("realm-administration", "realm"),
    ("otp", "authn"), ("password", "authn"), ("brute-force", "authn"),
    ("step-up", "authn"), ("authentication-flow", "authn"), ("webauthn", "authn"),
    ("role", "users"), ("group", "users"), ("credential", "users"), ("managing-users", "users"),
    ("security", "security"), ("hardening", "security"), ("threat", "security"),
]


def load_taxonomy(path=TAXONOMY):
    """Return (vocab:set, synonyms:dict). vocab = all backticked tokens under the
    Areas/Kinds/Versions headings; synonyms parsed from `a` -> `b` lines."""
    vocab, synonyms = set(), {}
    if not os.path.isfile(path):
        return vocab, synonyms
    section = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            h = re.match(r"^##\s+(.*)", line)
            if h:
                section = h.group(1).strip().lower()
                continue
            if section and section.startswith("synonyms"):
                m = re.search(r"`([^`]+)`\s*->\s*`([^`]+)`", line)
                if m:
                    synonyms[m.group(1)] = m.group(2)
            elif section in ("areas", "kinds", "versions"):
                m = BACKTICK_RE.search(line)
                if m:
                    vocab.add(m.group(1))
    return vocab, synonyms


DOMAIN_RE = re.compile(r"^\s*-\s*domain:\s*([a-z][a-z0-9-]*)\s*$", re.MULTILINE)


def load_domains(path=TAXONOMY):
    """Set of declared domain names, parsed from `- domain: <name>` lines under the
    `## Domains` section of taxonomy.md. The kebab-only pattern skips template
    placeholders like `<domain>`, so commented examples don't register as domains.
    lint.py uses this to validate each page's `domain:`; index.py uses it to know
    which `index.<domain>.md` files to build."""
    if not os.path.isfile(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        return set(DOMAIN_RE.findall(fh.read()))


def page_files():
    for d in PAGE_DIRS:
        full = os.path.join(WIKI, d)
        if not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.endswith(".md") and fn != "README.md":
                yield d, fn[:-3], os.path.join(full, fn)


def parse_tags(fm_block):
    """Extract the tags list from a frontmatter block (inline [a, b] form)."""
    m = re.search(r"^tags:\s*\[(.*?)\]\s*$", fm_block, re.MULTILINE)
    if not m:
        return None
    return [t.strip() for t in m.group(1).split(",") if t.strip()]


def heuristic_tags(slug, page_dir):
    areas = []
    for kw, area in AREA_KEYWORDS:
        if kw in slug and area not in areas:
            areas.append(area)
    tags = sorted(areas)[:4]
    if page_dir == "topics":
        tags.append("concept")
    return tags


def cmd_validate(args, vocab, synonyms):
    unknown, untagged = [], []
    for d, slug, path in page_files():
        with open(path, encoding="utf-8") as fh:
            m = FM_RE.match(fh.read())
        block = m.group(2) if m else ""
        tags = parse_tags(block)
        if not tags:
            untagged.append(f"{d}/{slug}")
            continue
        for t in tags:
            if t not in vocab:
                hint = f" (synonym of `{synonyms[t]}`)" if t in synonyms else ""
                unknown.append(f"{d}/{slug}: unknown tag `{t}`{hint}")
    print(f"Taxonomy: {len(vocab)} legal tags, {len(synonyms)} synonyms")
    if unknown:
        print(f"\nUNKNOWN TAGS ({len(unknown)})")
        for u in unknown:
            print("  - " + u)
    print(f"\nUNTAGGED PAGES: {len(untagged)} (run `tags.py backfill --apply`)")
    if args.strict and unknown:
        raise SystemExit(1)


def edit_frontmatter(text, transform):
    m = FM_RE.match(text)
    if not m:
        return text, False
    new_block, changed = transform(m.group(2))
    if not changed:
        return text, False
    return text[:m.start()] + m.group(1) + new_block + m.group(3) + text[m.end():], True


def cmd_normalize(args, vocab, synonyms):
    n = 0
    for d, slug, path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        def tf(block):
            tags = parse_tags(block)
            if not tags:
                return block, False
            new = []
            for t in tags:
                c = synonyms.get(t, t)
                if c not in new:
                    new.append(c)
            if new == tags:
                return block, False
            line = "tags: [" + ", ".join(new) + "]"
            return re.sub(r"^tags:.*$", line, block, count=1, flags=re.MULTILINE), True

        new_text, changed = edit_frontmatter(text, tf)
        if changed:
            n += 1
            print(f"{'WROTE' if args.apply else 'would normalize'} {d}/{slug}")
            if args.apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
    print(f"\n{n} pages {'normalized' if args.apply else 'pending'}")


def cmd_backfill(args, vocab, synonyms):
    n = 0
    for d, slug, path in page_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        def tf(block):
            if parse_tags(block) is not None:
                return block, False  # already tagged — idempotent
            tags = heuristic_tags(slug, d)
            if not tags:
                return block, False
            line = "tags: [" + ", ".join(tags) + "]"
            lines = block.splitlines()
            idx = next((i for i, ln in enumerate(lines) if ln.startswith("status:")), len(lines))
            lines.insert(idx, line)
            return "\n".join(lines), True

        new_text, changed = edit_frontmatter(text, tf)
        if changed:
            n += 1
            print(f"{'WROTE' if args.apply else 'would tag'} {d}/{slug}: "
                  f"{heuristic_tags(slug, d)}")
            if args.apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
    print(f"\n{n} pages {'tagged' if args.apply else 'pending'} "
          f"({'apply' if args.apply else 'dry-run'})")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd")
    pv = sub.add_parser("validate"); pv.add_argument("--strict", action="store_true")
    pv.set_defaults(fn=cmd_validate)
    pn = sub.add_parser("normalize"); pn.add_argument("--apply", action="store_true")
    pn.set_defaults(fn=cmd_normalize)
    pb = sub.add_parser("backfill"); pb.add_argument("--apply", action="store_true")
    pb.set_defaults(fn=cmd_backfill)
    args = ap.parse_args()
    if not getattr(args, "fn", None):
        args = ap.parse_args(["validate"])
    vocab, synonyms = load_taxonomy()
    args.fn(args, vocab, synonyms)


if __name__ == "__main__":
    main()
