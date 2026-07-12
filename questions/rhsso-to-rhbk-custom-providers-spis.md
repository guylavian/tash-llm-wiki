---
title: "RH-SSO 7.6 → RHBK 26 — what happens to custom providers/SPIs, rebuild vs. carry over"
type: question
question_tier: conceptual
domain: keycloak
slug: rhsso-to-rhbk-custom-providers-spis
summary: "Custom SPI providers always require a recompile+rebuild for RHBK 26 (Jakarta EE 10, consolidated KeycloakSession, removed deps, new JAR-in-providers/ deployment with kc.sh build); the SPI/factory contract and most provider logic carry over unchanged, but EAR/WAR packaging, hot-deploy, the AngularJS Admin/Account console themes, and several APIs do not."
sources:
  - guide:migration_guide
  - kb:migrating-providers
  - kb:migrating-themes
  - kb:other-changes
  - guide:server_developer_guide
source_notes:
  - "[[rhbk-26-6-migrating-providers]]"
  - "[[rhbk-26-6-migrating-themes]]"
  - "[[rhbk-26-6-other-changes]]"
provenance_extracted: 10
provenance_inferred: 2
provenance_ambiguous: 0
tags: [migration, spi]
status: reviewed
updated: 2026-06-17
---

# RH-SSO 7.6 → RHBK 26 — custom providers & SPIs: rebuild vs. carry over

**Every custom SPI provider must be recompiled and re-deployed for RHBK 26 — the
runtime moved from JBoss EAP to Quarkus and the platform jumped to Jakarta EE 10.
The *SPI/factory programming model* and most of your provider logic carry over;
the *packaging, deployment, and a set of removed APIs* do not.** ([[custom-provider-migration]], [[spi-provider-model]])

## What carries over (unchanged)
- **The SPI/factory contract itself.** `ProviderFactory` + `Provider` +
  `META-INF/services/<factory-interface>` registration is stable across RHBK
  26.0/26.2/26.4/26.6 and is the same model RH-SSO used. Your `getId()`,
  lifecycle methods, and override-by-`order()` semantics still apply
  ([[spi-provider-model]], [[override-built-in-providers]]).
- **Provider business logic that only calls surviving APIs.** Most providers need
  *no code change* — the removed-method migrations below apply only if you hit
  them (inferred from the guide's "most providers need no change" note).
- **The database.** Point RHBK at the existing DB; it auto-migrates the schema on
  first start ([[database-auto-migration]]) — your User Storage SPI keeps reading
  the same external store ([[user-storage-spi]]).

## What must be rebuilt / changed
**1. Recompile for Jakarta EE 10.**
`javax.*` → `jakarta.*` (except JDK-provided `javax.security`/`.net`/`.crypto`).
Session/stateless EJBs are dropped.

**2. Drop removed third-party deps / bundle what you still need.**
`openshift-rest-client`, `okio-jvm`, `okhttp`, `commons-lang`,
`commons-compress`, `jboss-dmr`, `kotlin-stdlib`, and most EAP libraries are gone
— bundle any you still need into the JAR (mind the non-isolated classloader and
split-package warnings — [[spi-provider-model]]).

**3. Adapt to the consolidated `KeycloakSession`.**
`userLocalStorage()`, `userCache()`, `userStorageManager()`,
`userFederatedStorage()` and the `*StorageManager()`/`*LocalStorage()` family are
removed — use `users()` (now cache-aware). For true local-storage access, cast
via `LegacyDatastoreProvider`; storage-provider `RealmModel` code should implement
`LegacyRealmModel` — both require the new `keycloak-model-legacy*` modules on the
deployment. Parameter ordering normalized (`RealmModel` first).

**4. Replace `@Context` injection.**
JAX-RS resources no longer get `@Context` injection — obtain request/response via
`session.getContext().getHttpRequest()/getHttpResponse()`, other objects via
`context.getContextObject(...)`.

**5. Change how you deploy — and run a build.**
Copy provider JARs (plus extra dependency JARs) into `${KC_HOME}/providers`, **not**
the removed `standalone/deployments`. **`EAR`/`WAR` packaging and
`jboss-deployment-structure.xml` are no longer supported.** Hot-deploy and
auto-discovery are gone: after changing providers you must run **`kc.sh build`**
(or a non-optimized start / operator init-container build) ([[spi-provider-model]]).

## SPI-type specifics
- **User Storage SPI** — logic survives; adapt to the `users()`/legacy-cast API
  changes above ([[user-storage-spi]]).
- **JavaScript/script providers** — package as a JAR (scripts-must-be-a-JAR);
  Nashorn is on the classpath by default, so do **not** bundle a JS engine. Script
  providers are Technology Preview, disabled by default ([[javascript-providers-scripts]]).
- **Themes** — **Login themes migrate**; the **AngularJS Admin Console and
  server-side-templated Account Console (and themes extending them) have no
  migration path** — the v2 React consoles replace them ([[keycloak-themes]]).
- **Admin client artifact renamed** — `keycloak-admin-client-jakarta` →
  `keycloak-admin-client` (Jakarta default since 26.2.0); Java EE variant is now
  `keycloak-admin-client-jee`.

## Caveats
- Legacy-module casts (`LegacyDatastoreProvider`, `LegacyRealmModel`) only work
  when the `keycloak-model-legacy*` modules are part of the deployment.
- Pin the extension `pom.xml` `dependencyManagement` to the exact RHBK version
  (e.g. `26.6.2.redhat-00001`) with Keycloak artifacts `scope=provided`.
- Do **not** carry RH-SSO 7.x WildFly module / `jboss-cli` deployment steps into
  RHBK — the Quarkus build/registration flow replaces them entirely.

## See also
- [[custom-provider-migration]]
- [[spi-provider-model]]
- [[rhsso-to-rhbk-migration]]
- [[user-storage-spi]]
- [[keycloak-themes]]
- [[javascript-providers-scripts]]
- [[override-built-in-providers]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-migration_guide|keycloak reference — migration_guide]]
- [[rhbk-26-6-migrating-providers|Chapter 6. Migrating custom providers]]
- [[rhbk-26-6-migrating-themes|Chapter 7. Migrating custom themes]]
- [[rhbk-26-6-other-changes|Chapter 9. Other notable changes]]
- [[_ref-keycloak-server_developer_guide|keycloak reference — server_developer_guide]]
<!-- crosslink:end -->
