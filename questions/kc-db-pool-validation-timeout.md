---
origin: eval-cohort
title: KC_DB_POOL_VALIDATION_TIMEOUT does not exist in RHBK
type: question
domain: keycloak
slug: kc-db-pool-validation-timeout
status: draft
summary: KC_DB_POOL_VALIDATION_TIMEOUT is not a recognized RHBK/Keycloak environment variable; the real db-pool options are db-pool-initial-size, db-pool-min-size, db-pool-max-size, and db-pool-max-lifetime.
sources:
  - id: rhbk-26-4-db
    type: guide
    title: "Chapter 9. Configuring the database - Red Hat build of Keycloak 26.4 Server Configuration Guide"
  - id: rhbk-26-0-concepts-threads
    type: guide
    title: "Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.0 High Availability Guide"
  - id: rhbk-26-4-migration-changes
    type: guide
    title: "Chapter 2. Migration changes - Red Hat build of Keycloak 26.4 Server Configuration Guide"
provenance:
  extracted: 1
  inferred: 0
  ambiguous: 0
updated: 2026-07-12
---

# KC_DB_POOL_VALIDATION_TIMEOUT does not exist in RHBK

`KC_DB_POOL_VALIDATION_TIMEOUT` is **not a recognized environment variable** in Red Hat Build of Keycloak (RHBK). It does not appear in the RHBK reference corpus — not in the database configuration guide, not in the thread/concepts guides, and not in migration notes. The variable is silently ignored if set; no deprecation warning or error is emitted (inferred from the absence of any reference).

## Actual database pool options

RHBK exposes four `db-pool-*` config options, each also available as an env var with the `KC_DB_POOL_*` prefix:

| CLI / config key         | Environment variable            | Purpose                                                    |
|--------------------------|---------------------------------|------------------------------------------------------------|
| `db-pool-initial-size`   | `KC_DB_POOL_INITIAL_SIZE`       | Initial number of connections in the pool                  |
| `db-pool-min-size`       | `KC_DB_POOL_MIN_SIZE`           | Minimum number of connections kept in the pool             |
| `db-pool-max-size`       | `KC_DB_POOL_MAX_SIZE`           | Maximum number of connections the pool can hold            |
| `db-pool-max-lifetime`   | `KC_DB_POOL_MAX_LIFETIME`       | Maximum lifetime of a connection (must be < DB `wait_timeout`) |

These are documented in:
- RHBK 26.4 Server Configuration Guide — "Configuring the database" chapter (`reference/keycloak/rhbk-26-4-db.md:249-258`): lists `db-pool-max-lifetime` and its relationship with the database's `wait_timeout`.
- RHBK 26.0/26.2 HA Guide — "Concepts for configuring thread pools" (`reference/keycloak/rhbk-26-0-concepts-threads.md:27-29`, `reference/keycloak/rhbk-26-2-concepts-threads.md:31-33`): lists `db-pool-initial-size`, `db-pool-min-size`, and `db-pool-max-size` as the connection pool sizing options.
- RHBK 26.4 Migration changes (`reference/keycloak/rhbk-26-4-migration-changes.md:303-307`): documents the introduction of a default `db-pool-max-lifetime`.

No `db-pool-validation-timeout` or related validation-timeout option exists in the RHBK configuration surface. If a connection-validation timeout is needed, it would be a JDBC driver-level property on the URL, not an RHBK server option.

## See also
- [[rhbk-db-connection-pool]] — HA connection pool sizing guidance (equal initial/min/max sizes)
- [[database-configuration]] — general database setup
