---
title: OIDC Client Libraries by Stack (Java / Node / SPA)
type: entity
domain: keycloak
slug: client-libraries-by-stack
summary: "Which library to use to authenticate an app against RHBK/Keycloak, by stack — and what the RH-SSO→RHBK move means for each"
sources:
  - guide:securing_applications_and_services_guide
  - kb:migrating-applications
  - web:https://developers.redhat.com/articles/2024/04/23/migrate-sso-red-hat-build-keycloak (RHBK migration, fetched 2026-06-16)
  - web:https://www.angulararchitects.io/blog/oauth2-with-spring-angular-keycloak-spring-for-resource-server/ (fetched 2026-06-16)
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
  - web:https://github.com/spring-projects/spring-security/wiki/OAuth-2.0-Migration-Guide (Spring Security OAuth EOL/migration, fetched 2026-06-16)
  - web:https://github.com/authts/react-oidc-context (fetched 2026-06-16)
source_notes:
  - "[[rhbk-26-6-migrating-applications]]"
provenance_extracted: 5
provenance_inferred: 9
provenance_ambiguous: 0
tags: [clients]
status: draft
updated: 2026-07-02
---

# OIDC Client Libraries by Stack (Java / Node / SPA)

**Which library to use to authenticate an app against RHBK/Keycloak, by stack —
and what the RH-SSO→RHBK move means for each.** The frozen RHBK corpus names two
categories ("keycloak-js JavaScript adapter" and "generic OIDC RP library"); the
concrete library names below the line are **upstream/community (web-sourced)** and
should be version-checked against each library's own docs.

## The rule that spans all stacks
Use **Authorization Code + PKCE** with the right client type; **no Implicit / no
Direct Grant** (RFC 9700, removed in OAuth 2.1). Server-side apps =
**confidential** client; browser/native = **public** client. See
[[oidc-grant-types]], [[client-authentication-methods]], [[oidc-client-best-practices]].

## Java (server-side, confidential client)
The RH-SSO Java adapters (EAP 6/7 OIDC, **Spring Boot adapter**, Fuse) are
**removed** from RHBK — do **not** carry them forward ([[adapter-migration]]).
Use the platform's native OIDC instead:
| Framework | Use |
|---|---|
| JBoss EAP 8.x | **EAP-native OIDC** client (config mirrors old `keycloak.json`) |
| Spring Boot | **Spring Security** `oauth2-client` (login) / `oauth2-resource-server` (API) |
| Quarkus | **`quarkus-oidc`** extension |
| Plain Java / JAX-RS resource server | validate JWT via JWKS ([[oidc-token-validation]]) |
Tokens stay server-side — the safest pattern; no token-in-browser exposure.

## Node
- **Server-side / API:** a certified OIDC RP library such as **`openid-client`**,
  or framework middleware (Passport OIDC strategy, NestJS OIDC). Confidential
  client; validate access tokens by JWKS ([[oidc-token-validation]]).
- **SPA backend:** run a **BFF / Token Handler** (Node confidential client holds
  the tokens, browser gets only a cookie) — the strongest SPA pattern per RFC 9700.

## SPA (Angular / React / Vue — public client)
- **`keycloak-js`** — the official Keycloak JavaScript adapter (the one corpus-named
  browser option; *not* among the removed adapters). Best loaded from the server so
  it tracks the server version. Framework-agnostic; you wrap it.
- **`keycloak-angular`** — Angular-idiomatic wrapper over keycloak-js: ready-made
  `AuthGuard` and an `HttpClient` interceptor that attaches the bearer token.
  Recommended when the app is Keycloak-committed.
- **`angular-auth-oidc-client`** / **`angular-oauth2-oidc`** — provider-agnostic,
  standards-based, favored for modern Angular + PKCE setups and avoiding IdP
  lock-in.
All require: public client (client authentication **off**), PKCE on, Implicit off.
For token safety prefer **DPoP** ([[dpop]]) or a **BFF**.

## Migration-readiness signal (use in the repo audit)
- 🟢 **Easy:** already on keycloak-js / a generic OIDC lib / Spring Security /
  Quarkus OIDC / EAP-8 native OIDC — mostly config (issuer/realm/client URL) +
  the protocol-change checklist in [[adapter-migration]].
- 🔴 **Heavy:** uses a **removed** RH-SSO Java adapter (EAP 6/7, Spring Boot
  adapter, Fuse) → must re-platform onto native OIDC before/with the move (the
  RH-SSO adapter still works against an RHBK 26.x server as a temporary bridge).

## Named libraries — status & caveats (upstream / web-sourced)
Specific libraries people ask about. **This whole section is upstream/community,
not Red Hat ground-truth** — verify versions against each project.

| Library | Layer | Status (2025/26) | Verdict |
|---|---|---|---|
| **`spring-security-oauth2`** (legacy `org.springframework.security.oauth`) | Java | **EOL — moved to `spring-attic`, docs 404, deprecated Apr 2022.** `@EnableResourceServer`/`@EnableAuthorizationServer`, `OAuth2RestTemplate`, `ClientCredentialsResourceDetails` all dead | ❌ **Do not use.** A repo on this is a 🔴 finding regardless of RHBK |
| **Spring Security 5/6 built-in** (`oauth2Client` / `oauth2ResourceServer` DSL) | Java | Current, in core | ✅ The migration target. Client + Resource Server only — Authorization Server role → **Spring Authorization Server** (separate project) |
| **`angular-oauth2-oidc`** (manfredsteyer) | SPA | Active, most-starred Angular OIDC lib | ✅ Provider-agnostic, PKCE. Avoid its old **implicit-flow** samples |
| **`react-oidc-context`** (on **`oidc-client-ts`**) | SPA | Actively maintained | ✅ Recommended React path (PKCE + silent renew). ⚠️ Known **"No matching state found in storage"** callback bug under React 18 StrictMode double-mount — handle the callback/clear URL params correctly |
| **`oidc-client-ts`** | SPA | Active (successor to dead `oidc-client`) | ✅ The engine under react-oidc-context; use directly for non-React |
| **`passport-openidconnect`** | Node | Maintained, generic | ✅ Standards-based server-side login strategy for Passport/Express |
| **`openid-client`** | Node | Maintained, certified | ✅ Preferred low-level Node RP (use directly or behind Passport) |
| **`passport-keycloak-oauth2-oidc`** | Node | **Stale — last publish ~5 yrs ago** | ❌ Avoid for new/prod; prefer `passport-openidconnect`/`openid-client` |

**Dominant 2025 pattern (inferred — synthesis across the web-sourced library survey
above, not a single source):** SPA does the OIDC login (PKCE, public client); the
Node/Java backend is a **resource server that only validates Bearer JWTs**
([[oidc-token-validation]]) — not its own redirect login. Extract client roles
from `resource_access[clientId].roles`.

## Contradictions / caveats
- Library names/versions here are **upstream/community (web-sourced)**, not Red Hat
  ground-truth — pin versions against each library's docs and the support story in
  `ref:rhbk-platform-support.md`.
- keycloak-js: keep the adapter version aligned with the server; upgrade the
  server first.
- **`spring-security-oauth2` is the highest-value red flag** in a Java repo audit —
  it's EOL independent of the RHBK move and must be rewritten to Spring Security
  5/6 native OAuth2.

## Air-gap note
On a disconnected network you **cannot install these from public registries** —
resolve every package from an internal Nexus/Artifactory/Verdaccio mirror, vendor
SPA bundles into the image, and prefer loading **keycloak-js from the internal
RHBK server**. SAML integrates via local metadata files. Full detail:
[[air-gapped-client-integration]]. SAML SP options: [[saml-clients-and-migration]].

## See also
- [[adapter-migration]]
- [[saml-clients-and-migration]]
- [[air-gapped-client-integration]]
- [[oidc-client-best-practices]]
- [[oidc-grant-types]]
- [[client-authentication-methods]]
- [[oidc-token-validation]]
- [[dpop]]
- [[rhsso-to-rhbk-migration]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
<!-- crosslink:end -->
