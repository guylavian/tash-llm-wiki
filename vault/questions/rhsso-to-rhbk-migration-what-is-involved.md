---
origin: eval-cohort
title: What is involved in migrating from RH-SSO 7.6 to RHBK?
type: question
domain: keycloak
slug: rhsso-to-rhbk-migration-what-is-involved
summary: Migration from RH-SSO 7.6 (JBoss EAP-based) to RHBK (Quarkus-based) spans six surfaces: server config, database, Operator/OpenShift, application adapters, custom providers, and custom themes.
sources:
  - ref:migration-upgrading.md
  - kb:rhbk-26-6-migrating-server
  - kb:rhbk-26-6-migrating-operator
  - kb:rhbk-26-6-migrating-applications
  - kb:rhbk-26-6-migrating-providers
  - kb:rhbk-26-6-migrating-themes
  - kb:rhbk-26-6-other-changes
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 0
question_tier: conceptual
tags: [migration]
status: draft
updated: 2026-07-12
graph_community: "RH-SSO 7.x → Red Hat Build of Keycloak Migration"
---

# What is involved in migrating from RH-SSO 7.6 to RHBK?

Migrating from RH-SSO 7.6 (the last of the legacy JBoss EAP-based line) to Red Hat Build of Keycloak (RHBK, the Quarkus-based successor) is a **non-trivial, multi-surface effort**. The single biggest architectural change is the runtime — RH-SSO 7.6 ran on **JBoss EAP** with `standalone.xml` configuration; RHBK runs on **Quarkus** with a flat `kc.sh` option model (`ref:migration-upgrading.md:8`). There are **six migration surfaces**:

## 1. Server configuration (`standalone.xml` → `kc.sh`)

The entire config model is different. `standalone.xml`, `jboss-cli`, and EAP operating modes no longer apply (`ref:migration-upgrading.md:19`). Every option is now a flat `kc.sh` parameter, sourced (in order of precedence) from CLI args, environment variables (`KC_*`), `conf/keycloak.conf`, or a Java KeyStore (`ref:migration-upgrading.md:19-26`). Key mappings:

| Area | RH-SSO 7.6 | RHBK |
|---|---|---|
| Datasource | `KeycloakDS` datasource subsystem | `--db postgres --db-url-host ... --db-username ... --db-password ...` |
| HTTP/TLS | EAP `<tls>` subsystem | `--https-key-store-file/--https-certificate-file`; HTTP off by default in `start` mode |
| Cache/cluster | Infinispan subsystem in `standalone-ha.xml` | `--cache=ispn`; JGroups default is now `jdbc-ping` (DB-based discovery) |
| Hostname | Hostname SPI (recommended) | `--hostname` is **required** in `start` mode |
| Truststore | File truststore SPI (JKS) | PEM or unencrypted PKCS12 via `--truststore-paths` |
| Vault | Elytron Credential Store | `--vault keystore --vault-file ...` |
| JVM | `standalone.conf` | `JAVA_OPTS` / `JAVA_OPTS_APPEND` |

(`ref:migration-upgrading.md:32-44`)

**Prerequisites:** shut down old RH-SSO 7.6 (never share DB across versions), back up the database, install OpenJDK 21, review release notes (`ref:migration-upgrading.md:12`).

## 2. Database (auto-migration)

RHBK can **reuse the same database instance** as RH-SSO 7.6 (`ref:migration-upgrading.md:57`). The schema is auto-migrated on first start (automatic mode). For air-gapped or DBA-controlled environments, use manual mode:
```
kc.sh start --spi-connections-jpa-quarkus-migration-strategy=manual
```
which writes the DDL to `bin/keycloak-database-update.sql` and exits (`ref:migration-upgrading.md:62`). Always back up before migration — auto-migration is one-way (`(inferred)`).

## 3. Operator / OpenShift (complete rewrite)

The RHBK Operator is a **complete rewrite** — not backward compatible with the RH-SSO 7.6 Operator (`ref:migration-upgrading.md:68`). You must install the new Operator and author fresh `Keycloak` CRs (apiVersion `k8s.keycloak.org/v2alpha1`, kind `Keycloak`). Key differences:
- DB: any supported vendor (not just PostgreSQL)
- TLS: user must supply `tlsSecret`; default Route is **passthrough** (was reencrypt)
- Extensions in CR: **removed** — build an optimized custom image instead
- Upgrade strategy: default is **recreate** (single-version-against-DB guarantee)
- `KeycloakRealm` CR → `KeycloakRealmImport` CR (import-only, no update/delete)
- **Client and User CRs removed**

(`ref:migration-upgrading.md:95-106`)

## 4. Application adapters (dropped Java adapters)

Several RH-SSO 7.6 Java client adapters are **no longer released** with RHBK:
- JBoss EAP 6.x/7.x OIDC adapters
- Spring Boot adapter
- Red Hat Fuse adapter

Replacements (`ref:migration-upgrading.md:130-141`):
- **EAP 8.x** → native OpenID Connect client (no extra dependency)
- **Spring Boot** → Spring Security OAuth2/OIDC
- **EAP 7.x** → keep RH-SSO 7.6 adapters (maintenance support; supported against RHBK 26.x server as a bridge)
- **SPA** → `@redhat/keycloak-js` 26.2.x (legacy `.success()/.error()` removed)
- **Node.js** → `@redhat/keycloak-connect` 26.1.1

OIDC protocol changes: `Access Type` removed from UI; custom-scheme redirect URIs need explicit patterns; `iss` auth-response param (RFC 9207) added by default; UserInfo now RFC 6750-compliant (`ref:migration-upgrading.md:145`).

## 5. Custom providers (Jakarta EE 10 + consolidated API)

Custom providers require recompilation (`ref:migration-upgrading.md:151`):
- **Java EE → Jakarta EE 10**: `javax.*` → `jakarta.*`
- **Deployment**: JARs in `providers/` (not `standalone/deployments/`); no EAR/WAR, no `jboss-deployment-structure.xml`
- **No hot-deploy**: run a build or restart after changes
- **Consolidated `KeycloakSession`**: `users()` replaces `*LocalStorage()`/`*StorageManager()` family
- Several 3rd-party deps removed (`openshift-rest-client`, `okhttp`, `commons-lang`, etc.)
- `@Context` injection on JAX-RS removed — use `session.getContext()`

## 6. Custom themes (console themes don't migrate)

- **New Admin & Account Consoles** (React, `keycloak.v2`): **no migration path** from old AngularJS/themed versions (`ref:migration-upgrading.md:155`)
- **Login themes do migrate**: reference built-in templates from `keycloak-themes-${KC_VERSION}.jar`; deploy as JAR in `providers/` or files in `themes/`

## Other notable changes
- RPM distribution is **no longer available** — ZIP or container only (`ref:migration-upgrading.md:8`)
- Domain clustered mode **not supported** in RHBK (`ref:migration-upgrading.md:38`)
- Nashorn JS engine bundled by default
- Admin client artifact: `keycloak-admin-client` (Jakarta default)
- "Never expires" (`-1`) removed from client Advanced Settings

## References

**RH ground-truth (`ref:` / `kb:`):**
- `ref:migration-upgrading.md` — Migration & Upgrading — RH-SSO 7.6 → RHBK and RHBK version upgrades (26.6 Offline Reference)
- `kb:rhbk-26-6-migrating-server` — Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server
- `kb:rhbk-26-6-migrating-operator` — Chapter 3. Migrating Operator deployments on OpenShift
- `kb:rhbk-26-6-migrating-applications` — Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6
- `kb:rhbk-26-6-migrating-providers` — Chapter 6. Migrating custom providers
- `kb:rhbk-26-6-migrating-themes` — Chapter 7. Migrating custom themes
- `kb:rhbk-26-6-other-changes` — Chapter 9. Other notable changes

**Wiki pages:**
- [[rhsso-to-rhbk-migration]] — master topic page
- [[server-config-migration]] — detailed `standalone.xml` → `kc.sh` mapping
- [[quarkus-config-migration]] — EAP → Quarkus config model
- [[database-auto-migration]] — auto/manual schema migration
- [[operator-cr-migration]] — Operator CR rewrite details
- [[adapter-migration]] — dropped adapters and replacements
- [[custom-provider-migration]] — Jakarta EE 10 and API consolidation
- [[keycloak-themes]] — theme migration

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/migration-upgrading|Migration & Upgrading — RH-SSO 7.6 → RHBK and RHBK version upgrades — 26.6 (Offline Reference)]]
- [[rhbk-26-6-migrating-server|Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server]]
- [[rhbk-26-6-migrating-operator|Chapter 3. Migrating Operator deployments on Openshift]]
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
- [[rhbk-26-6-migrating-providers|Chapter 6. Migrating custom providers]]
- [[rhbk-26-6-migrating-themes|Chapter 7. Migrating custom themes]]
- [[rhbk-26-6-other-changes|Chapter 9. Other notable changes]]
<!-- crosslink:end -->
