---
title: How do you secure an application using RHBK's OIDC or SAML support?
type: question
question_tier: conceptual
domain: keycloak
slug: securing-an-app-with-oidc-saml
summary: "Register the app as a *client* in an RHBK realm and have it speak OpenID Connect (preferred for new apps) or SAML 2.0, using the framework's native OIDC/SAML library — not a Keycloak adapter."
sources:
  - guide:securing_applications_and_services_guide
  - ref:securing-apps-oidc-saml.md
  - ref:oidc-client-best-practices.md
  - ref:oidc-grant-types.md
  - ref:saml-clients-and-migration.md
  - kb:oidc-layers-
provenance:
  extracted: 14
  inferred: 2
  ambiguous: 0
tags: [clients]
status: draft
updated: 2026-07-07
graph_community: "Tokens & Sessions"
---

# How do you secure an application using RHBK's OIDC or SAML support?

You secure an application with RHBK by registering it as a **client** in a realm and having it speak **OpenID Connect (OIDC)** or **SAML 2.0** to RHBK as the authorization server / identity provider.

## Pick a protocol

- **OpenID Connect** — token-based (JWT), JSON over REST, lightweight. Recommended for new apps of any type: web, SPA, mobile, native, service-to-service. OIDC is the default choice ([[securing-apps-oidc-saml]]).
- **SAML 2.0** — XML-based, browser-redirect/POST assertions. Choose it to integrate with existing enterprise SAML service providers, e.g. via `mod_auth_mellon` or the SAML Galleon feature pack for EAP ([[saml-clients-and-migration]]).

## Register the client

Create a client in the realm via the Admin Console, [[client-registration-service]] (REST API), or [[client-registration-cli]] (`kcreg.sh`). Decide whether it is:

- **Confidential** — server-side app that can safely hold a secret or signed-JWT credential. Required for token introspection, CIBA, and the JWT-authorization grant ([[client-authentication-methods]]).
- **Public** — SPA or native/mobile app that cannot hold a secret. Must use PKCE and preferably DPoP sender-constrained tokens ([[dpop]]).
- **Service account** — a client that authenticates on its own behalf for machine-to-machine work using the Client Credentials grant.

## Choose the right OIDC flow

From [[oidc-grant-types]]:

- **Authorization Code + PKCE** — the standard for web apps, SPAs, and native/mobile. The app redirects the user to RHBK, gets a code, and exchanges it for tokens. PKCE is mandatory per OAuth 2.0 BCP (RFC 9700).
- **Client Credentials** — for service-to-service (no user).
- **Device Authorization Grant** — for input-constrained devices.
- **CIBA** — for decoupled/backchannel auth (confidential clients only).
- Discouraged (removed in OAuth 2.1): Implicit, Hybrid, Direct Grant (ROPC).

## Authenticate the client

From [[oidc-client-best-practices]]:
- **Confidential client:** prefer `private_key_jwt` (client-authenticated signed JWT) over a shared secret.
- **Public client:** no secret — identify by `client_id` only. Require PKCE (S256) and enable DPoP to sender-constrain tokens.

## Validate tokens on the resource server

From [[oidc-token-validation]]:
- **Offline (JWKS):** fetch the realm's `jwks_uri` from the OIDC discovery document, cache the keys, verify the JWT signature, and check `iss`, `aud`, `exp`, `nbf` on every request. Handle key rotation by refetching on an unknown `kid`.
- **Online (Introspection):** call RHBK's introspection endpoint (`/protocol/openid-connect/token/introspect`). Confidential client required. Use when you need immediate revocation feedback or the token is opaque.

## Discover endpoints from the well-known URL

From [[oidc-endpoints]]:

```
GET /realms/{realm}/.well-known/openid-configuration
→ authorization_endpoint, token_endpoint, jwks_uri, end_session_endpoint,
  revocation_endpoint, introspection_endpoint ...
```

Never hardcode endpoint URLs.

## Write correct refresh logic

From [[oidc-client-best-practices]]:
- Refresh tokens are **single-use** when *Revoke Refresh Token* is on. Always persist the new refresh token from the response atomically.
- Never refresh the same token concurrently (race → `invalid_grant`). Serialize behind a single-flight lock.
- Refresh proactively (e.g. at 80% of `expires_in`) — don't wait for a 401.
- `invalid_grant` means "re-authenticate the user" — the SSO session expired. Don't retry forever.
- DPoP-bound public clients need a valid DPoP proof on refresh requests as well.

## Log out and revoke

From [[oidc-logout]]:
- **Redirect logout:** send the user agent to RHBK's `end_session_endpoint` with `id_token_hint` and `post_logout_redirect_uri`.
- **Back-channel logout:** call the endpoint directly with the refresh token and client credentials.
- **Revocation:** POST to `/revoke` with the token to invalidate it immediately. Revoking a refresh token clears the user's consent.

## Stronger: sender-constrained tokens and compliance profiles

- **DPoP (RFC 9449):** bind tokens to a client-held key pair. Stolen tokens are useless without the private key. Full support in RHBK 26.4+ ([[dpop]]).
- **FAPI / OAuth 2.1 profiles:** built-in client-policy profiles (`fapi-1-baseline`, `fapi-2-security-profile`, `oauth-2-1-for-public-client`, etc.) enforce PKCE, sender-constrained tokens, PAR, and exact redirect URIs ([[fapi-oauth21-profiles]]).
- **BFF pattern:** for SPAs, the strongest protection is a Backend-for-Frontend (confidential server-side client) that holds all tokens and issues only encrypted HttpOnly session cookies to the browser ([[bff-token-handler]]).

## SAML specifics

From [[saml-clients-and-migration]]:
- RHBK is a full SAML 2.0 IdP. Integration is via metadata-file exchange: export RHBK's IdP descriptor and import the SP's entity descriptor.
- **Supported SAML adapters:** EAP 8 SAML Galleon feature pack / RPM, `mod_auth_mellon` (Apache HTTPD module), framework-native SAML SP (e.g. Spring Security SAML).
- **Not supported:** RH-SSO 7.6 SAML adapters for non-EAP containers (Tomcat, older JBoss).
- SAML Single Logout in a cluster requires correct cache configuration — remote nodes may lack the session-index mapping (inferred).
- SAML is air-gap friendly: metadata exchange via static files, no internet needed.

## References

### RH ground-truth
- `guide:securing_applications_and_services_guide` — Securing Applications and Services Guide (RHBK 26.x)
- `guide:migration_guide` — Migration Guide (RHBK 26.x)
- `guide:server_administration_guide` — Server Administration Guide (RHBK 26.x)
- `kb:oidc-layers-` — reference note harvested from the OIDC layers chapter

### Wiki
- [[securing-apps-oidc-saml]] — OIDC vs SAML, client types & protocol flows
- [[oidc-client-best-practices]] — writing the integration code correctly
- [[oidc-grant-types]] — recommended vs discouraged flows
- [[client-authentication-methods]] — secret, signed-JWT, public client auth
- [[oidc-token-validation]] — JWKS vs introspection token validation
- [[oidc-endpoints]] — the standard OIDC endpoint set
- [[oidc-logout]] — logout and revocation
- [[dpop]] — RFC 9449 sender-constrained tokens
- [[fapi-oauth21-profiles]] — built-in FAPI 1/2 and OAuth 2.1 profiles
- [[saml-clients-and-migration]] — SAML SP integration and adapter migration
- [[bff-token-handler]] — Backend-for-Frontend / Token Handler pattern
- [[client-libraries-by-stack]] — which OIDC library per stack

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
- [[references/securing-apps-oidc-saml|Securing Applications & Services with RHBK 26.6 (OIDC & SAML)]]
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
<!-- crosslink:end -->
