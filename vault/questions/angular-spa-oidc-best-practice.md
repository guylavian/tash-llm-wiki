---
title: "OAuth/OIDC best practice for an Angular SPA against RHBK — code+PKCE vs BFF, tokens, public-client settings, logout"
type: question
question_tier: conceptual
domain: keycloak
slug: angular-spa-oidc-best-practice
summary: "An Angular SPA must use a public client with Authorization Code + PKCE (S256), client authentication OFF, implicit/direct-grant OFF, exact redirect URIs, and logout via end_session_endpoint; tokens should be sender-constrained with DPoP or, for the strongest XSS posture, moved server-side behind a BFF. keycloak-angular (Keycloak-committed) or angular-auth-oidc-client (provider-agnostic) are the library choices."
sources:
  - guide:securing_applications_and_services_guide
  - kb:oidc-layers-
  - kb:migrating-applications
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
source_notes:
  - "[[rhbk-26-6-oidc-layers]]"
  - "[[rhbk-26-6-migrating-applications]]"
provenance_extracted: 8
provenance_inferred: 5
provenance_ambiguous: 0
tags: [clients]
status: reviewed
updated: 2026-06-17
graph_community: "Tokens & Sessions"
---

# Angular SPA against RHBK — OIDC best practice

**An Angular SPA is a browser app that cannot keep a secret, so it is a public
client using Authorization Code + PKCE. The strongest posture moves tokens
server-side behind a BFF; if tokens stay in the browser, sender-constrain them
with DPoP.** Grounded in [[securing-apps-oidc-saml]], [[oidc-client-best-practices]],
[[client-libraries-by-stack]], [[fapi-oauth21-profiles]].

## Code + PKCE vs BFF — the decision
- **Authorization Code + PKCE (public client, tokens in the browser).** The
  baseline supported SPA pattern: `keycloak-js`/`keycloak-angular` runs the redirect
  flow, PKCE (`S256`) protects the code, tokens live in JS memory. Simplest to ship.
  Residual risk: any XSS can read the in-memory tokens. Harden with **[[dpop]]** so a
  stolen token is useless without the browser-held private key
  ([[oidc-client-best-practices]] §9).
- **BFF / Token Handler (server-side confidential client, browser holds only a
  cookie).** RFC 9700's strongest current SPA recommendation: a server-side
  confidential client holds the tokens; the browser gets an `HttpOnly`/`Secure`
  session cookie and never sees a token, sidestepping XSS token theft entirely
  ([[oidc-client-best-practices]] §"Upstream / RFC 9700"). Cost: you run and operate
  a backend (a Node/Java confidential client — [[client-libraries-by-stack]]).
- **Recommendation (inferred):** use PKCE-public-client + DPoP for a pure SPA with
  no backend; choose the BFF when you already have a server tier or handle
  high-value data — it is the safer long-term target.

## Public-client settings on the RHBK realm
Create the client as **OpenID Connect**, then ([[securing-apps-oidc-saml]],
[[client-authentication-methods]]):
- **Client authentication = OFF** (this is what makes it *public*; no secret).
- **Standard flow = ON** (Authorization Code); **Implicit = OFF**, **Direct access
  grants = OFF** (both discouraged by RFC 9700 / removed in OAuth 2.1).
- **PKCE required**: set *Proof Key for Code Exchange Code Challenge Method =
  `S256`* on the client's Advanced settings (or enforce realm-wide via the
  `fapi-1-baseline` `pkce-enforcer` executor — [[fapi-oauth21-profiles]]).
- **Valid redirect URIs**: exact match, no broad wildcards (e.g.
  `https://app.example.com/*` only if necessary; prefer the exact callback path).
- **Valid post logout redirect URIs** + **Web origins** (CORS) set to the app origin.
- Optional hardening: enable **`dpop_bound_access_tokens`** on the client to require
  DPoP ([[dpop]]); apply an **OAuth 2.1 public-client** policy profile.

## Token handling (where SPA bugs live — [[oidc-client-best-practices]] §4)
- Endpoints come from **discovery** (`/.well-known/openid-configuration`), never
  hardcoded.
- **Refresh is single-flight + proactive**: serialize refresh behind one lock,
  refresh before `exp` (~80% of lifetime), and — if the realm has *Revoke Refresh
  Token* on — **persist the rotated refresh token** from each response. (`keycloak-js`
  `updateToken(minValidity)` does this for you; don't fire it from many tabs racing.)
- Treat `invalid_grant` / "Session not active" as **re-authenticate**, not retry.
- **Never put tokens in `localStorage`** — keep them in memory; for durable browser
  storage you want a BFF cookie instead.
- Resource servers validate the access token by **JWKS (cached, rotation-aware)**,
  not per-request introspection ([[oidc-token-validation]]).

## Logout ([[oidc-logout]])
- **Redirect logout** to the `end_session_endpoint` with `id_token_hint` +
  `post_logout_redirect_uri` (the post-logout URI must be registered on the client).
  `keycloak-js` `logout({ redirectUri })` wraps this.
- Hit the **revocation endpoint** to kill a specific token immediately; revoking a
  refresh token also clears the user's consent.
- With DPoP-bound tokens, RHBK enforces a DPoP proof on the logout endpoint too.

## Library choice (Angular — [[client-libraries-by-stack]])
- **`keycloak-angular`** (wraps official `keycloak-js`) — Keycloak-idiomatic
  `AuthGuard` + bearer-token `HttpClient` interceptor; best when the app is
  Keycloak-committed. Keep the `keycloak-js` version aligned with the server.
- **`angular-auth-oidc-client` / `angular-oauth2-oidc`** — provider-agnostic,
  standards-based, avoids IdP lock-in. Avoid `angular-oauth2-oidc`'s old
  implicit-flow samples.
- All require: public client, client-auth **off**, PKCE **on**, implicit **off**.

## Caveats
- DPoP is a full feature in **RHBK 26.6**, preview in earlier 26.x — check the flag
  ([[dpop]]).
- OAuth 2.1 profiles track a **draft** spec and may change between RHBK versions
  ([[fapi-oauth21-profiles]]).
- Realm token lifespans / *Revoke Refresh Token* / offline idle are server-side and
  govern much of the client behavior — confirm them per realm.
- On an air-gapped network, resolve npm packages from an internal mirror and prefer
  loading `keycloak-js` from the internal RHBK server ([[client-libraries-by-stack]]).

## Scaffold
A runnable Angular 17+ standalone scaffold built on this guidance lives at
`examples/angular-rhbk-spa/` (keycloak-angular, public client + PKCE, functional
auth guard, bearer interceptor, login/logout) with a README mapping each file back
to the rules above.

## See also
- [[oidc-client-best-practices]]
- [[securing-apps-oidc-saml]]
- [[client-libraries-by-stack]]
- [[fapi-oauth21-profiles]]
- [[dpop]]
- [[oidc-logout]]
- [[client-authentication-methods]]
- [[oidc-token-validation]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
<!-- crosslink:end -->
