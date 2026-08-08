"""bootstrap.py — the vault is SELF-CREATING: ensure its skeleton exists before any tool reads it.
stdlib only, no network.

THE FAILURE THIS EXISTS FOR. Every tool here resolves content through `paths.WIKI`, which is
`<repo>/vault` or whatever `WIKIKB_VAULT_ROOT` points at — and until now *nothing* created that
tree. Point the code at a fresh directory (a brand-new clone of the toolchain, an empty bind mount
at `/data/vault`, a `WIKIKB_VAULT_ROOT` on a new host) and the tools do not fail loudly: they scan
a directory that isn't there, find zero pages, and serve an EMPTY WIKI that looks healthy. That is
exactly the trap docker-compose.yml warns about in prose ("seed the host directory FIRST or you
will serve an empty wiki") — a warning in a comment is not a mechanism.

WHAT IT CREATES — the minimum a vault needs to be lintable, indexable, and writable:
  * the vault root itself,
  * the four synthesis page tiers (`paths.PAGE_DIRS`) — the dirs every scanner walks,
  * the raw tiers `reference/` + `references/` + `_sources/` — where INGEST lands notes,
  * `taxonomy.md`, the LOAD-BEARING file: with no domains declared, `lint` rejects every page and
    `index` builds nothing, so a vault without it is not merely empty but unusable. The seed
    carries the section headings the parsers read plus the inert ADD-DOMAIN template, and NO
    declared domain — a domain is a human decision (ADD DOMAIN step 2), never bootstrapped.
  * `.manifest.json`, seeded byte-equivalent to `manifest.load()`'s in-memory default.

WHAT IT WILL NOT DO:
  * **Never touch an existing file.** Every action is create-if-absent. A vault that already has
    `taxonomy.md` keeps its own, whatever state it is in — repair is INGEST/LINT's job, not this
    module's, and silently rewriting a hand-authored taxonomy would destroy the domain declarations
    the whole wiki validates against.
  * **Never invent content.** No pages, no domains, no generated indexes (`index.md` /
    `index.<domain>.md` are `wikikb index`'s output — hand-seeding them would create the exact
    stale-generated-index state lint warns about).
  * **Never mask a bad path by failing.** A read-only or unwritable vault yields a warning and the
    tool runs on; only a NON-DIRECTORY at the vault path raises, because that is a
    misconfiguration no amount of retrying fixes.

VISIBILITY IS THE SAFETY VALVE. Auto-creation is one typo away from silently serving a fresh empty
vault out of `WIKIKB_VAULT_ROOT=/data/valut` — so anything created prints one line to STDERR naming
the resolved path (the same reason `serve.main()` prints `vault=…` at startup). `WIKIKB_BOOTSTRAP=0`
turns the automatic hook off entirely for operators who want the old "missing means missing".
"""
import json
import os
import sys
from pathlib import Path

from wikikb import paths

ENV_VAR = "WIKIKB_BOOTSTRAP"          # =0 disables the automatic startup hook (explicit CLI still works)

# The dirs a vault must have. PAGE_DIRS is imported, not re-listed — adding a fifth page tier there
# must not require remembering to add it here too (the copy-paste bug paths.py's comment describes).
RAW_DIRS = ("reference", "references", "_sources")
REQUIRED_DIRS = tuple(paths.PAGE_DIRS) + RAW_DIRS

# Seeded byte-equivalent to manifest.load()'s default so `manifest status` on a fresh vault behaves
# identically whether or not the file is on disk.
MANIFEST_SEED = {"generated": None, "sources": {}}

# NOTE on the Areas/Kinds/Versions sections below: tags.load_taxonomy() harvests EVERY backticked
# lowercase token under those three headings into the tag vocabulary, and it does not skip HTML
# comments. So the prose here deliberately carries no backticks — a helpful `like-this` example
# would silently become a legal tag. The Domains template is safe as-is: its `<domain>` placeholders
# fail the kebab-only pattern DOMAIN_RE requires, which is why it can ship inert.
TAXONOMY_SEED = """# Wiki tag taxonomy — controlled vocabulary

Seeded by `wikikb bootstrap`. This is the **only** source of legal `tags:` values and the
**only** place domains are declared: `tags.py` / `lint.py` / `index.py` parse this file, so
until a domain is declared under `## Domains`, lint rejects every page's `domain:` and
`index` builds nothing. Fill it in per CLAUDE.md, Operation: ADD DOMAIN.

A page's `tags:` should carry **one or more `area`**, optionally **one `kind`**, and
optionally **version** tags when the page is version-specific. Example:

```yaml
tags: [federation, concept, v26.6]
```

## Areas
<!-- One token per line, kebab-case, in the same shape as the Kinds entries below:
     a dash, the token in backticks, an em-dash, then what it covers.
     Areas are a FLAT UNION across every domain; each domain's areas: must be a subset. -->

## Kinds
- `concept` — broad synthesis / how-something-works (usually topics/)
- `config-option` — a single config key / flag / setting
- `cli` — a command-line tool or command
- `endpoint` — an HTTP endpoint or protocol surface
- `procedure` — a step-by-step task
- `troubleshooting` — a diagnosis/fix page
- `anti-pattern` — a page centered on a common wrong implementation (paired with the rule it violates)
- `failure-mode` — a page centered on the observable fault/symptom a wrong implementation produces

## Versions
<!-- One product version per line as a backticked token, e.g. a dash then v1.2 in backticks.
     Only add versions this vault actually distinguishes between. -->

## Domains
The `domain:` **frontmatter facet** (required on every page) partitions the wiki by
technology. It is *not* a tag — `lint.py` validates each page's `domain:` against the
`- domain: <name>` lines below, and `index.py` reads each block to build that domain's
`index.<domain>.md`.

Each domain also declares `- tiers-covered:` — the coarse knowledge tiers actually
ingested, from this fixed, deliberately tiny set (do **not** grow it into an ontology):
conceptual (how it works: product docs/guides), support-kb (break-fix / known-issue /
patch knowledge), scenarios (end-to-end deployment & operations playbooks). A QUERY
classifies the question's tier; if the routed domain does not cover it, the **Confidence
gate** fires `Out of corpus coverage`.

<!-- Template — copy per new technology (placeholders are ignored by lint/index):
### <domain>
- domain: <domain>
- areas: [...]                       # also add any NEW area to ## Areas above
- shape: notes-first | corpus-backed
- sources: [_sources/<domain>/]      # + corpora/<domain>/ if corpus-backed
- review-moc: <domain>-implementation-review
- tiers-covered: [conceptual]        # coarse tiers ingested: conceptual | support-kb | scenarios
-->

## Synonyms (normalized away by `tags.py --normalize`)
<!-- One rewrite per line: a dash, the alias in backticks, an arrow, the canonical area in backticks. -->
"""


class BootstrapError(RuntimeError):
    """A vault path that cannot be a vault (a file / non-directory sits there).

    Distinct from an OSError on creation: that one is transient-ish (permissions, read-only mount)
    and tools continue; this one means the configured path is wrong.
    """


def enabled():
    """False only when WIKIKB_BOOTSTRAP is explicitly off. Absent ⇒ on (a fresh vault should just
    work); the escape hatch is for operators who want a missing vault to stay missing."""
    return os.environ.get(ENV_VAR, "").strip().lower() not in ("0", "false", "no", "off")


def vault_root(root=None):
    return Path(root).expanduser().resolve() if root else paths.WIKI


def plan(root=None):
    """(vault, actions) — what ensure() WOULD create, creating nothing. `actions` is a list of
    (kind, relpath) with kind in {"root", "dir", "file"}, in creation order."""
    vault = vault_root(root)
    actions = []
    if not vault.is_dir():
        if vault.exists():
            raise BootstrapError(
                "vault path %s exists but is not a directory — check WIKIKB_VAULT_ROOT" % vault)
        actions.append(("root", "."))
    for d in REQUIRED_DIRS:
        p = vault / d
        if not p.is_dir():
            if p.exists():
                raise BootstrapError("%s exists but is not a directory" % p)
            actions.append(("dir", d))
    # Files are keyed off the resolved paths module so an override (WIKIKB_VAULT_ROOT,
    # WIKIKB_SCRAPE_SOURCES) can never disagree with what the tools then read.
    for rel in ("taxonomy.md", ".manifest.json"):
        if not (vault / rel).exists():
            actions.append(("file", rel))
    return vault, actions


def _write_seed(path, rel):
    if rel == "taxonomy.md":
        path.write_text(TAXONOMY_SEED, encoding="utf-8")
    else:
        path.write_text(json.dumps(MANIFEST_SEED, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ensure(root=None, dry_run=False):
    """Create the missing pieces of the vault skeleton. Idempotent; returns (vault, created) where
    `created` is the list of relpaths acted on (empty ⇒ the vault was already complete).

    Raises BootstrapError for a non-directory at a required path, OSError if creation fails.
    """
    vault, actions = plan(root)
    created = []
    for kind, rel in actions:
        target = vault if rel == "." else vault / rel
        if not dry_run:
            if kind == "file":
                _write_seed(target, rel)
            else:
                # parents=True so a never-mounted path like /srv/llm-wiki/vault works on a fresh
                # host; the stderr notice is what keeps a typo'd parent chain from being invisible.
                target.mkdir(parents=True, exist_ok=True)
        created.append(rel)
    return vault, created


def ensure_startup(label="wikikb", stream=None):
    """The automatic hook every entry point calls. Never raises, never exits: a tool must not die
    because the vault could not be prepared — it should run and report its own emptiness.

    Prints ONE line to stderr when it created something (or could not), and nothing at all on the
    overwhelmingly common path where the vault is already complete.
    """
    stream = stream or sys.stderr
    if not enabled():
        return []
    try:
        vault, created = ensure()
    except BootstrapError as e:
        print("%s bootstrap: REFUSED — %s" % (label, e), file=stream)
        return []
    except OSError as e:
        print("%s bootstrap: could not prepare vault %s — %s (continuing)"
              % (label, vault_root(), e), file=stream)
        return []
    if created:
        fresh = created[0] == "."
        print("%s bootstrap: %s vault %s (%s)" % (
            label, "created" if fresh else "repaired", vault,
            ", ".join(r for r in created if r != ".") or "root only"), file=stream)
    return created


def main():
    import argparse

    ap = argparse.ArgumentParser(
        prog="python3 -m wikikb bootstrap", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", help="prepare THIS path instead of the resolved vault "
                                   "(default: %s)" % paths.WIKI)
    ap.add_argument("--dry-run", action="store_true", help="report what is missing, create nothing")
    args = ap.parse_args()
    try:
        vault, created = ensure(args.vault, dry_run=args.dry_run)
    except (BootstrapError, OSError) as e:
        print("bootstrap: FAILED: %s" % e)
        sys.exit(2)
    verb = "would create" if args.dry_run else "created"
    print("bootstrap: vault %s" % vault)
    if not created:
        print("bootstrap: complete — nothing to do")
    else:
        for rel in created:
            print("bootstrap: %s %s" % (verb, "the vault root" if rel == "." else rel))
        if not args.dry_run:
            print("bootstrap: next: declare a domain in taxonomy.md (CLAUDE.md, Operation: ADD "
                  "DOMAIN), then `python3 -m wikikb build`")
    sys.exit(0)


if __name__ == "__main__":
    main()
