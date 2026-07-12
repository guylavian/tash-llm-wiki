---
title: How are Service Provider Interfaces (SPIs) used to customize RHBK?
type: question
question_tier: conceptual
domain: keycloak
slug: spi-customization-rhbk
summary: "RHBK is customized by implementing SPIs: write a `Provider` + `ProviderFactory`, register via `META-INF/services/`, JAR goes in `providers/`, then `kc.sh build`. Two provider-type kinds (single vs multiple implementations), plus JavaScript script providers (Technology Preview) for lighter customization."
sources:
  - guide:server_developer_guide
source_notes:
  - "[[rhbk-26-6-providers]]"
  - "[[spi-provider-model]]"
provenance_extracted: 12
provenance_inferred: 0
provenance_ambiguous: 0
tags: [spi, customization, extension]
status: draft
updated: 2026-07-07
---

# How are Service Provider Interfaces (SPIs) used to customize RHBK?

Red Hat Build of Keycloak (RHBK) exposes a large set of **Service Provider Interfaces (SPIs)** that let you plug in custom behavior without forking the server. The extension model has three parts:

## 1. The provider/factory contract (Java SPI)

Every SPI extension implements two interfaces (`rhbk-26-6-providers.md:21-22`):

- **`ProviderFactory`** — a singleton, created once and lives for the server lifetime. Lifecycle: `init(Config.Scope)`, `postInit(KeycloakSessionFactory)`, `close()`, `getId()`.
- **`Provider`** — created per-request by the factory's `create(KeycloakSession ...)`. Should be light-weight.

Registration: a file `META-INF/services/<fully-qualified-factory-interface>` listing the factory FQCNs (one per line) (`rhbk-26-6-providers.md:22-23`).

Example for a custom Theme Selector: implement `ThemeSelectorProviderFactory` + `ThemeSelectorProvider`, provide `META-INF/services/org.keycloak.theme.ThemeSelectorProviderFactory` (`rhbk-26-6-providers.md:24-65`).

## 2. Packaging and build step

- **`pom.xml`** needs a `dependencyManagement` import of `org.keycloak:keycloak-parent` pinned to the exact RHBK version (e.g. `26.6.2.redhat-00001`), Keycloak artifacts with `scope=provided` (`rhbk-26-6-providers.md:85-114`).
- Copy the JAR (and extra dependencies) to the server's `providers/` directory (`rhbk-26-6-providers.md:179-182`).
- **Rebuild**: `kc.sh build` (or non-optimized start) (`rhbk-26-6-providers.md:183-184`).
- Classloading caveat: provider JARs are **not** isolated — avoid bundling conflicting resources like `application.properties` or `commons-lang3` (`rhbk-26-6-providers.md:185-193`).

### Configuration

Pass options at build or start time: `--spi-<spi-name>-<provider-id>-<option>=<value>`, or via environment variable `KC_SPI_<SPI-NAME>__<PROVIDER-ID>__<OPTION>` (`rhbk-26-6-providers.md:67-73`).

## 3. Single vs. multiple implementation provider types

RHBK distinguishes two kinds (`rhbk-26-6-providers.md:156-177`):

| Kind | Example | Lookup | Behaviour |
|---|---|---|---|
| **Single-implementation** | `HostnameProvider` | `session.getProvider(HostnameProvider.class)` | Only one active; pick the default with `kc.sh build --spi-hostname--provider=default` |
| **Multiple-implementation** | `EventListener` | `session.getProvider(EventListener.class, "jboss-logging")` | Many co-exist; fetch by provider id |

## 4. Overriding built-in providers

To replace a built-in whose id must stay fixed (e.g. `OIDCLoginProtocolFactory` must keep id `openid-connect`), use the same `getId()` and implement `order()` with a higher value than the built-in. The highest-order implementation for that id wins at runtime (`rhbk-26-6-providers.md:119-134`).

## 5. Admin Console integration

Implement `ServerInfoAwareProviderFactory` on your factory to surface build-time, configuration, or operational info (versions, remote URLs, latencies) on the **Server Info** page (`rhbk-26-6-providers.md:135-152`).

## 6. Key SPIs you can implement

| SPI | What it customizes |
|---|---|
| **User Storage SPI** | Bridge external user/credential stores into RHBK's user model (the engine behind LDAP/AD federation). See [[user-storage-spi]] |
| **Vault SPI** | Connect to an arbitrary secrets vault. See [[vault-spi]] |
| **Theme Selector / Theme Resource SPIs** | Control how themes are selected and loaded. See [[keycloak-themes]] |
| **EventListener SPI** | React to login, logout, admin events |
| **Authenticator SPI** | Add custom authentication steps to a flow |
| **Protocol Mapper SPIs** (OIDC/SAML) | Shape claims/tokens/assertions |
| **Hostname SPI** | Control frontend/backchannel URL formation |
| **Policy SPI** | Custom authorization policy provider |

## 7. JavaScript (script) providers — Technology Preview

For lighter customization without compiling Java, RHBK supports **script-based providers** for: Authenticator, JavaScript Policy, OIDC Protocol Mapper, SAML Protocol Mapper (`rhbk-26-6-providers.md:197-205`). Scripts are JavaScript files packaged in a JAR with a `META-INF/keycloak-scripts.json` descriptor (`rhbk-26-6-providers.md:305-367`). Disabled by default; enable with `--features=preview` or `--features=scripts` (`rhbk-26-6-providers.md:199-201`).

## Summary

To customize RHBK via SPI: **(1)** implement `ProviderFactory` + `Provider`, **(2)** add a `META-INF/services/` file, **(3)** build a JAR with the RHBK parent POM, **(4)** drop it in `providers/`, **(5)** run `kc.sh build`. For single-implementation types, use `--spi-<name>--provider=<id>` to select which implementation is active. The full list of available SPIs is visible in the Admin Console at **Server Info → Provider Info**.

## References

**RH ground-truth:**
- `kb:rhbk-26-6-providers` — Chapter 4. Service Provider Interfaces (SPI), RHBK 26.6 Server Developer Guide
- `kb:rhbk-26-6-user-storage-spi` — Chapter 5. User Storage SPI, RHBK 26.6 Server Developer Guide

**Wiki pages:**
- [[spi-provider-model]] — SPI provider/factory model & extension deployment
- [[user-storage-spi]] — User Storage SPI
- [[vault-spi]] — Vault SPI
- [[keycloak-themes]] — Theme customization (Theme Selector/Resource SPIs)
- [[javascript-providers-scripts]] — JavaScript script providers
- [[override-built-in-providers]] — Overriding a built-in provider
- [[keycloak-session-spi]] — KeycloakSession SPI
- [[rhsso-to-rhbk-custom-providers-spis]] — RH-SSO 7.6 → RHBK migration for custom SPIs

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-server_developer_guide|keycloak reference — server_developer_guide]]
<!-- crosslink:end -->
