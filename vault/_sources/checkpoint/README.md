# `_sources/checkpoint/` — the Check Point raw tier

**IMMUTABLE.** Nothing under here is edited once written. It is ground truth; the synthesis
layer (`topics/`, `entities/`, `questions/`) is what gets maintained, and it cites this.

## Where the material comes from

This domain is **notes-first with a scraper-fed raw tier**: it has no harvested offline docset
like `keycloak` or `openshift`. Two inputs:

- **`_raw/web/`** — written by the ONLINE-mode harvester. `support.checkpoint.com` is on
  `vault/scrape-sources.json` with `match: prefix`, so each run pulls the pages under it that
  the newest Common Crawl index has captured. Each document lands as `<slug>.md` plus a
  `<slug>.json` sidecar carrying the URL, the **capture date**, the WARC digest and which
  extractor produced it. `web_to_corpus → corpus_to_vault → build` then folds those into
  `vault/reference/checkpoint/` as immutable reference notes and links them into the graph.
- **hand notes** — drop Markdown directly in this directory for anything you know that no
  public page states, and cite it as `note:_sources/checkpoint/<file>.md`.

## Citing it

A scraped document carries **both** tokens, and they are complementary, not alternatives:

```yaml
sources:
  - kb:web-support-checkpoint-com-<url-tail>     # the reference note — puts it in the link graph
  - web:https://support.checkpoint.com/… (label, fetched YYYY-MM-DD)   # the provenance + date
```

`web_to_corpus` prints the exact `kb:` token for every record it writes.

## Two things to be careful about

1. **This is a vendor SUPPORT PORTAL, and most of it is behind a login.** Common Crawl only ever
   holds what was served to an anonymous crawler, so what lands here is the public surface —
   product/download landing pages and public SK articles, not the gated knowledge base. Treat a
   thin or navigational note as exactly that; do not synthesize a break-fix claim out of a
   product listing page.
2. **`tiers-covered:` is `conceptual` only** (`vault/taxonomy.md`). Until a real support-kb tier
   is ingested, a `support-kb`/`scenarios` question routed here MUST fire the Confidence gate's
   **H1 out-of-coverage banner** (CLAUDE.md, Operation: QUERY) and be filed `status: draft`.
   Raising `tiers-covered:` without the content behind it is precisely how that gate is defeated.

## Still outstanding for this domain (ADD DOMAIN, steps 5–7)

Registered in `taxonomy.md` and wired to the scraper, but **not yet seeded**: it has no overview
topic, no first entity, and no `checkpoint-implementation-review` MOC. Write those against real
harvested notes — see `_meta/ADD-DOMAIN.md`.
