---
title: SPI provider/factory model & extension deployment
type: topic
domain: keycloak
slug: spi-provider-model
summary: "Red Hat build of Keycloak (RHBK) is customized by implementing Service Provider Interfaces (SPIs): each extension supplies a `Provider` plus a `ProviderFactory`, registered through a `META-INF/services` file, packaged in a JAR dropped into `providers/`, and activated by running `kc.sh build`."
sources:
  - guide:server_developer_guide
  - kb:https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/server_developer_guide/providers
  - kb:https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/server_developer_guide/user-storage-spi
provenance: needs-review
tags: [spi, concept]
status: draft
updated: 2026-06-16
---

# SPI provider/factory model & extension deployment

**Red Hat build of Keycloak (RHBK) is customized by implementing Service Provider Interfaces (SPIs): each extension supplies a `Provider` plus a `ProviderFactory`, registered through a `META-INF/services` file, packaged in a JAR dropped into `providers/`, and activated by running `kc.sh build`.**

## The provider/factory contract

To implement any SPI you implement two interfaces and register them:

1. **`ProviderFactory`** — a single instance is created once and lives for the server lifetime, so it can hold state across requests. Its lifecycle methods are `init(Config.Scope)`, `postInit(KeycloakSessionFactory)`, `close()`, and `getId()` (the provider id shown in the admin console / used in config keys).
2. **`Provider`** — created per request (or per transaction) by the factory's `create(KeycloakSession ...)`. Provider instances should be light-weight; they are garbage-collected after `close()`.
3. **A service file** `META-INF/services/<fully-qualified-factory-interface>` whose body lists the fully qualified factory class names (line-separated). Example: a Theme Selector extension provides `META-INF/services/org.keycloak.theme.ThemeSelectorProviderFactory`.

A factory can obtain other providers through the `KeycloakSession` passed to `create()`, e.g. `session.getProvider(HostnameProvider.class)`. See [[keycloak-session-spi]] for the two retrieval styles.

Build dependencies: the extension `pom.xml` needs a `dependencyManagement` import of `org.keycloak:keycloak-parent` pinned to the exact RHBK version (e.g. `26.6.2.redhat-00001`), then declares Keycloak artifacts with `scope=provided`.

## Single vs. multiple implementations

RHBK distinguishes two provider-type kinds:

- **Single-implementation** types (e.g. `HostnameProvider`) — only one active implementation per server. If several are on the classpath, pick the default at build time: `kc.sh build --spi-hostname--provider=default`, where `default` is the factory's `getId()`.
- **Multiple-implementation** types (e.g. `EventListener`) — many co-exist; you fetch a specific one by id: `session.getProvider(EventListener.class, "jboss-logging")`.

## Overriding built-in providers

Normally use a unique `getId()`. To override a built-in (e.g. customize `OIDCLoginProtocolFactory`, whose id must stay `openid-connect` because the admin console and well-known endpoint depend on it), keep the same provider id and implement `order()` to return a value higher than the built-in. The highest-order implementation for a given id wins. See [[override-built-in-providers]].

## Registering & building

Providers are registered by copying the JAR (and any extra dependencies not already shipped) into the server's `providers/` directory. After adding/removing JARs, RHBK must be **re-built**: either run `kc.sh build` explicitly, or do a non-optimized start. This is the same build step that [[kc-bootstrap-admin]]-era operators run as an init container.

Classloading caveats (RHBK 26.x):
- Provider JARs are **not** isolated classloaders. Do not bundle resources/classes that collide with built-in ones (notably an `application.properties`, or an overriding `commons-lang3`) — this causes auto-build to fail when the provider JAR is later removed, and produces "split package" warnings at start.
- Not all built-in `lib` JARs are checked by the split-package logic; inspect `<install>/lib/lib/main` JARs before bundling transitive deps.
- A removed provider JAR can leave a `NoSuchFileException`; force a Quarkus index rebuild with `./kc.sh -Dquarkus.launch.rebuild=true --help`, then build/start normally.

## Admin Console integration

Implement `ServerInfoAwareProviderFactory` on your factory to surface build-time, configuration, or operational info (versions, remote URLs, latencies) on the admin **Server Info** page. The full list of runtime SPIs is also visible on that page.

## Key SPIs covered by the dev guide

- [[user-storage-spi]] — bridge external user/credential stores into RHBK's user metamodel.
- [[vault-spi]] — connect to an arbitrary secrets vault.
- Theme Selector / Theme Resource SPIs — see [[keycloak-themes]].
- Multiple-implementation runtime SPIs include `EventListener`, `Authenticator`, OIDC/SAML protocol mappers — these can also be implemented as [[javascript-providers-scripts]] when packaged correctly.

## Contradictions / caveats

- The provider/factory model and `META-INF/services` registration are stable across RHBK 26.0 / 26.2 / 26.4 / 26.6. The pinned parent-POM version string differs per release (e.g. `26.6.2.redhat-00001`).
- JavaScript/script providers are **Technology Preview**, disabled by default — see [[javascript-providers-scripts]].
- This is the RHBK (Quarkus) build/registration flow. Legacy RH-SSO 7.x used a WildFly module/deployment model and `jboss-cli`; do not carry RH-SSO deployment steps into RHBK. See [[rhsso-to-rhbk-migration]].

## See also
- [[user-storage-spi]]
- [[javascript-providers-scripts]]
- [[keycloak-themes]]
- [[vault-spi]]
- [[override-built-in-providers]]
- [[keycloak-session-spi]]
- [[rhsso-to-rhbk-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-providers|Chapter 4. Service Provider Interfaces (SPI)]]
- [[rhbk-26-6-user-storage-spi|Chapter 5. User Storage SPI]]
<!-- crosslink:end -->
