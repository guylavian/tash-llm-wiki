---
title: How to migrate RH-SSO 7.6 Java client adapters
type: question
domain: keycloak
slug: migrate-rhsso-76-java-client-adapters
summary: "Several RH-SSO 7.6 Java OIDC and SAML client adapters are no longer released with RHBK; re-platform onto standards-based OIDC/SAML support in the app's own stack, with an adapter bridge available during transition"
sources:
  - guide:migration_guide
  - kb:migrating-applications
  - ref:rhbk-platform-support.md
provenance:
  extracted: 10
  inferred: 2
  ambiguous: 0
tags: [clients, migration]
status: draft
updated: 2026-07-07
---

# How to migrate RH-SSO 7.6 Java client adapters

**RHBK no longer ships several RH-SSO 7.6 Java adapters. Re-platform applications onto the standards-based OIDC/SAML support built into their own framework — EAP-native OIDC for EAP 8.x, Spring Security for Spring Boot, Quarkus OIDC for Quarkus — using the RH-SSO 7.6 adapters as a temporary bridge against the RHBK 26.x server.**

## Dropped adapters (no longer released with RHBK)

| Adapter | Recommended replacement |
|---|---|
| JBoss EAP 6.x OIDC | End of maintenance; unsupported by both products |
| JBoss EAP 7.x OIDC | No RHBK support; existing apps keep RH-SSO 7.6 adapters under maintenance |
| Spring Boot OIDC | Spring Security `oauth2-client` / `oauth2-resource-server` |
| Red Hat Fuse OIDC | End of full support; adapters via RH-SSO 7.6 maintenance only |
| JBoss EAP 6.x/7.x SAML | Keycloak SAML Adapter feature pack / RPM for JBoss EAP 8.x |

## JBoss EAP migration

- **EAP 8.x:** use the EAP-native OpenID Connect client. Remove `EAP_HOME/modules/system/add-ons/keycloak/` and configure the native client — its config schema mirrors the old `keycloak.json`. For SAML, use the Keycloak SAML Adapter feature pack or RPM for JBoss EAP 8.x. (`rhbk-26-6-migrating-applications.md:31-35`)
- **EAP 7.x:** no RHBK support. Existing apps keep the RH-SSO 7.6 adapter (maintenance support). The adapter is supported against an RHBK 26.x server. (`rhbk-26-6-migrating-applications.md:125-127`)
- **EAP 6.x:** end of maintenance; unsupported by both products. (`rhbk-26-6-migrating-applications.md:128-129`)

## Spring Boot migration

Replace the RH-SSO Spring Boot adapter with Spring Security's built-in OAuth2/OIDC support (`spring-boot-starter-oauth2-client` for login, `-resource-server` for APIs). The adapters from RH-SSO 7.6 remain under maintenance support and work against RHBK 26.x as a bridge. (`rhbk-26-6-migrating-applications.md:130-137`)

## Red Hat Fuse migration

Red Hat Fuse is end of full support; RHBK provides no adapter for it. The RH-SSO 7.6 Fuse adapter remains under maintenance support and works against RHBK 26.x as a bridge. (`rhbk-26-6-migrating-applications.md:138-140`)

## Policy Enforcer (Authorization Services)

The policy enforcer is **decoupled** from the Java client adapters and available as a separate Maven dependency (`keycloak-policy-enforcer`). It works with any Java framework that has built-in OAuth2/OIDC support, including Servlet apps and Spring Boot. (`rhbk-26-6-migrating-applications.md:141-153`)

## Node.js and SPA adapters (not dropped)

These adapters **are** still shipped with RHBK (though the SPA adapter has changes):
- **Node.js (`keycloak-connect`):** upgrade to `@redhat/keycloak-connect@latest` (26.1.1). (`rhbk-26-6-migrating-applications.md:168-177`)
- **SPA (`keycloak-js`):** upgrade to `@redhat/keycloak-js@latest` (26.2.x). Breaking changes: legacy Promise API (`.success()`/`.error()`) removed; `new` operator required. (`rhbk-26-6-migrating-applications.md:154-167`)

## Protocol / client-setting changes (apply to all migrated OIDC clients)

- **Access Type removed** from Admin Console v2. Reproduce: Bearer-only = no flow enabled; Public = client auth disabled + ≥1 flow; Confidential = client auth enabled + ≥1 flow. The `bearerOnly`/`publicClient` JSON flags still work via REST/import. (`rhbk-26-6-migrating-applications.md:37-42`)
- **Custom-scheme redirect URIs** must be explicitly matched (`custom:/test*`); bare `*` no longer covers non-http(s) schemes. (`rhbk-26-6-migrating-applications.md:43-44`)
- **`client_id` param** supported on OIDC RP-Initiated Logout endpoint. (`rhbk-26-6-migrating-applications.md:45-54`)
- **Valid Post Logout Redirect URIs** added; `+` reuses the Valid Redirect URIs set (default on migration for BC). (`rhbk-26-6-migrating-applications.md:55-60`)
- **UserInfo endpoint:** RFC 6750-compliant errors (`WWW-Authenticate` instead of JSON); access token must carry `openid` scope (else 403); disabled users return `invalid_token`. (`rhbk-26-6-migrating-applications.md:61-85`)
- **Service Account Client ID mapper:** claim renamed `clientId` → `client_id` (OAuth2-compliant); `clientId` userSession note still exists. (`rhbk-26-6-migrating-applications.md:86-97`)
- **`iss` auth-response param** (RFC 9207) added by default. Older adapters may choke on it — disable per client via *OpenID Connect Compatibility Modes → Exclude Issuer From Authentication Response*. (`rhbk-26-6-migrating-applications.md:98-107`)

## SAML-specific changes

- RSA_SHA1 and DSA_SHA1 signature algorithms deprecated; use SHA256/SHA512 alternatives. These algorithms do not work on Java 17+. (`rhbk-26-6-migrating-applications.md:197-212`)
- SAML SP metadata now includes only encryption-intended realm keys (per algorithm). (`rhbk-26-6-migrating-applications.md:191-196`)

## Bridge strategy

RH-SSO 7.6 adapters are **supported in combination with an RHBK 26.x server** ([`adapter-migration.md`]). Migrate the server first, re-platform apps afterward.

## See also
- [[adapter-migration]]
- [[rhsso-to-rhbk-migration]]
- [[client-libraries-by-stack]]
- [[saml-clients-and-migration]]
- [[air-gapped-client-integration]]
- [[custom-provider-migration]]
- [[oidc-client-best-practices]]
- [[quarkus-config-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
<!-- crosslink:end -->
