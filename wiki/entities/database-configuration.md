---
title: Database configuration
type: entity
domain: keycloak
slug: database-configuration
summary: "RHBK stores realm/user/client data in a relational database selected by the build-time `db` option, with connection details (`db-url-host`, `db-username`, `db-password`) set at runtime."
sources:
  - guide:server_configuration_guide
provenance: needs-review
tags: [server-config]
status: draft
updated: 2026-06-16
---

# Database configuration

**RHBK stores realm/user/client data in a relational database selected by the build-time `db` option, with connection details (`db-url-host`, `db-username`, `db-password`) set at runtime.**

## Supported vendors (`db` values)

`mariadb`, `mssql`, `mysql`, `oracle`, `postgres`, `dev-mem`, `dev-file`. Hosted variants are also supported: EnterpriseDB Advanced, Amazon Aurora PostgreSQL, Azure SQL Database, Azure SQL Managed Instance. The default is **`dev-file`** — development only, **not** supported for production and must be replaced before deploying.

Tested versions (26.4): PostgreSQL 17 (14–17 supported), MySQL 8.4, MariaDB 11.8, Oracle 23.5/19c, MS SQL 2022. Using a DB version outside the documented range is unsupported even if the Hibernate dialect allows it.

## Drivers

All drivers ship with RHBK **except Oracle and Microsoft SQL Server**, which you install manually by dropping the JARs (`ojdbc17` + `orai18n`, or `mssql-jdbc`) into the `providers/` folder — or `ADD`-ing them into a custom container image. Overriding or supplying other drivers is unsupported.

## Configuring (build + runtime)

`db` is a **build option**; connection settings are runtime options. Recommended optimized flow — put the minimum in `conf/keycloak.conf`:

```
db=postgres
db-username=keycloak
db-password=change_me
db-url-host=keycloak-postgres
```

then `kc.sh build` and `kc.sh start --optimized`. The non-optimized one-shot form is `kc.sh start --db postgres --db-url-host ... --db-username ... --db-password ...`, but it exposes the password on the command line and is not recommended — use `keycloak.conf`, env vars, or the KeyStore/vault for the password. Default schema is `keycloak` (override with `db-schema`).

## Contradictions / caveats
- Supported-version tables drift per release — the list above is from **26.4**; check the matching guide for 26.0/26.2/26.6.
- For Operator-built custom images that add a driver, the image must be an optimized image with build options set (`ENV KC_DB`, then `RUN kc.sh build`). See [[build-vs-runtime-options]] and [[rhbk-operator]].
- The database is also central to clustering/persistence — see [[distributed-caches]] and [[ha-cross-site]].

## See also
- [[server-configuration]]
- [[build-vs-runtime-options]]
- [[production-checklist]]
- [[distributed-caches]]
- [[rhbk-operator]]
- [[keycloak-vault]]
