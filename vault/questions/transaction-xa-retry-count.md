---
origin: eval-cohort
title: KC_TRANSACTION_XA_RETRY_COUNT environment variable
type: question
question_tier: conceptual
domain: keycloak
slug: transaction-xa-retry-count
summary: "KC_TRANSACTION_XA_RETRY_COUNT does not exist in the Keycloak/RHBK corpus; the real XA-transaction option is KC_TRANSACTION_XA_ENABLED (build-time, enables or disables XA datasources)."
sources:
  - ref:rhbk-26-0-migration-changes.md
  - ref:rhbk-26-2-db.md
  - guide:server_configuration
provenance:
  extracted: 3
  inferred: 0
  ambiguous: 0
tags: [server-config, transaction, database]
status: draft
updated: 2026-07-12
graph_community: "RHBK Server Configuration — sources, build vs runtime, precedence"
---

# What does the `KC_TRANSACTION_XA_RETRY_COUNT` environment variable configure?

**`KC_TRANSACTION_XA_RETRY_COUNT` does not exist.** No such environment variable is defined in any RHBK 26.x or upstream Keycloak release. It is a fabrication.

## The real XA-transaction configuration

The correct environment variable is **`KC_TRANSACTION_XA_ENABLED`** (CLI: `--transaction-xa-enabled`), a **build-time** option that controls whether the datasource uses XA transactions:

- **`KC_TRANSACTION_XA_ENABLED=true`** — the default datasource uses an XA-compliant JDBC driver. Required when configuring additional datasources (more than one datasource), as XA ensures distributed transaction coordination across them (`reference/keycloak/rhbk-26-0-migration-changes.md:196-200`).
- **`KC_TRANSACTION_XA_ENABLED=false`** — disables XA. Recommended with AWS Aurora (`entities/rhbk-db-connection-pool.md:57`) and in certain HA deployments where the Aurora JDBC driver does not support XA.

Because it is a build-time option, changing it requires `kc.sh build` to persist the value. Attempting to set it at runtime (e.g. `KC_TRANSACTION_XA_ENABLED=false` on `kc.sh start` without a preceding build) produces the error:

> "The following build time options have values that differ from what is persisted — the new values will NOT be used until another build is run: kc.transaction-xa-enabled"

(`reference/keycloak/_gated-kb-index.md:3102-3104`)

## References

### RH ground-truth
- `ref:rhbk-26-0-migration-changes.md:196-200` — XA datasources now required for multiple datasources
- `ref:rhbk-26-2-db.md:201` — `--transaction-xa-enabled` build-time option
- `ref:rhbk-gated-kb-index` — runtime-only error when build step is skipped (kb:KTRIAGE-2193)
- `entities/rhbk-db-connection-pool.md:57` — XA off with Aurora

### Wiki
- [[rhbk-db-connection-pool]] — connection pooling and XA-off guidance
- [[database-configuration]] — database configuration overview
