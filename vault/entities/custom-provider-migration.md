---
title: Migrating custom providers, themes & admin-client artifacts to RHBK
type: entity
domain: keycloak
slug: custom-provider-migration
summary: "Custom SPI providers must be recompiled for Jakarta EE 10 and the consolidated KeycloakSession API, deployed as plain JARs in `providers/` with a build step — and the AngularJS Admin/Account consoles have no theme migration path"
sources:
  - guide:migration_guide
  - kb:migrating-providers
  - kb:migrating-themes
  - kb:other-changes
source_notes:
  - "[[rhbk-26-6-migrating-providers]]"
  - "[[rhbk-26-6-migrating-themes]]"
  - "[[rhbk-26-6-other-changes]]"
provenance_extracted: 12
provenance_inferred: 0
provenance_ambiguous: 2
tags: [migration]
status: draft
updated: 2026-07-02
graph_community: "RH-SSO 7.x → Red Hat Build of Keycloak Migration"
---

# Migrating custom providers, themes & admin-client artifacts to RHBK

**Custom SPI providers must be recompiled for Jakarta EE 10 and the
consolidated KeycloakSession API, deployed as plain JARs in `providers/` with a
build step — and the AngularJS Admin/Account consoles have no theme migration
path.**

## Body

### Deploying providers
Copy providers (and their extra dependency JARs) to `${KC_HOME}/providers`, not
the removed `standalone/deployments`. RHBK has **no separate classpath** for
providers, so be careful with transitive deps. **`EAR`/`WAR` packaging and
`jboss-deployment-structure.xml` are no longer supported.** Hot-deploy and
auto-discovery are gone — after changing providers you must run a **build** (or
restart with the auto-build feature). See [[spi-provider-model]].

### Code changes
- **Java EE → Jakarta EE 10:** `javax.*` → `jakarta.*` (except JDK-provided
  `javax.security`/`javax.net`/`javax.crypto`). Session/stateless beans dropped.
- **Removed 3rd-party deps:** `openshift-rest-client`, `okio-jvm`, `okhttp`,
  `commons-lang`, `commons-compress`, `jboss-dmr`, `kotlin-stdlib`, plus most EAP
  libraries — bundle any you still need into `providers/`.
- **No `@Context` injection on JAX-RS resources:** obtain request/response from
  `session.getContext().getHttpRequest()/getHttpResponse()`; other contextual
  objects via `context.getContextObject(...)`.
- **Consolidated `KeycloakSession`:** `userLocalStorage()`, `userCache()`,
  `userStorageManager()`, `userFederatedStorage()` and the `*StorageManager()` /
  `*LocalStorage()` family are removed — use `users()` (note: now cache-aware).
  For genuine local-storage access, cast via `LegacyDatastoreProvider` (ambiguous —
  see caveats: the 26.6 migration-guide note this page cites shows the cast target
  as plain `DatastoreProvider`, not `LegacyDatastoreProvider`). Several
  deprecated stream/model methods removed and parameter ordering normalized
  (`RealmModel` first). See [[user-storage-spi]].
- **New legacy modules:** data-store code moved to
  `keycloak-model-legacy`, `keycloak-model-legacy-private`,
  `keycloak-model-legacy-services`; add them as deps if you used moved classes.
  Code implementing `RealmModel` storage-provider methods should implement
  `LegacyRealmModel` and cast accordingly.

### Themes
- **New Admin Console** (`keycloak.v2`, React) and **new Account Console**
  (`keycloak.v2`, React): there is **no migration path** from the old AngularJS
  Admin Console / server-side-templated Account Console or themes extending them.
- **Login themes** do migrate. Reference built-in templates inside
  `${KC_HOME}/lib/lib/main/org.keycloak.keycloak-themes-${KC_VERSION}.jar`.
  Deploy as a JAR in `providers/` or copy into `${KC_HOME}/themes`. `start-dev`
  disables theme caching for live editing. See [[keycloak-themes]].

### Admin client & other notable changes
- **Admin client artifact renamed:** `keycloak-admin-client-jakarta` →
  `keycloak-admin-client` (Jakarta default since 26.2.0 — ambiguous, see caveats);
  Java EE variant is now `keycloak-admin-client-jee`.
- **Nashorn JS engine** is on the classpath by default — do **not** copy a JS
  engine when deploying [[javascript-providers-scripts]].
- **"Never expires"** removed from client advanced-settings combos (was `-1`).
- **Email validation:** new ASCII rules + 64-char local-part limit; raise with
  `--spi-user-profile-declarative-user-profile-max-email-local-part-length`.

## Contradictions / caveats
- Most providers that only call surviving APIs need **no** code change; the
  removed-method migrations above apply only if you hit them.
- Legacy-module casts (`LegacyDatastoreProvider`, `LegacyRealmModel`) work only
  when the legacy modules are part of the deployment.
- **Ambiguous — `LegacyDatastoreProvider` vs `DatastoreProvider`:** the RHBK 26.0 and
  26.2 migrating-providers notes show the cast as
  `((LegacyDatastoreProvider) session.getProvider(DatastoreProvider.class))`, but the
  26.4 and 26.6 notes (incl. the one cited on this page) show
  `((DatastoreProvider) session.getProvider(DatastoreProvider.class))` — i.e. the
  interface name in the cast itself appears to have been simplified/corrected
  starting 26.4. Verify against the exact target version before copying the snippet.
- **Ambiguous — Jakarta-default version number:** each per-version migration-guide
  note self-referentially states the `keycloak-admin-client` rename "since version
  X.Y.0" using its own version number (26.2 note says 26.2.0, 26.4 note says 26.4.0,
  26.6 note says 26.6.0) — almost certainly an un-updated template string in the
  docs rather than three separate renames. Treat 26.2.0 as the more credible
  original date and re-verify against the actual 26.2 release notes if precision
  matters.

## See also
- [[spi-provider-model]]
- [[user-storage-spi]]
- [[keycloak-themes]]
- [[javascript-providers-scripts]]
- [[rhsso-to-rhbk-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-migration_guide|keycloak reference — migration_guide]]
- [[rhbk-26-6-migrating-providers|Chapter 6. Migrating custom providers]]
- [[rhbk-26-6-migrating-themes|Chapter 7. Migrating custom themes]]
- [[rhbk-26-6-other-changes|Chapter 9. Other notable changes]]
<!-- crosslink:end -->
