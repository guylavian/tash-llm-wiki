---
title: How RHBK issues, scopes, and expires tokens and sessions
type: question
question_tier: conceptual
domain: keycloak
slug: how-does-rhbk-issue-scope-and-expire-tokens-and-sessions
summary: "RHBK issues tokens via OIDC/OAuth2 grant types on the token endpoint; scopes them with the scope parameter, client scopes, protocol mappers, and client policies; and expires them with layered session/token lifespans (SSO Session, Client Session, Offline Session, Access Token, Refresh Token) configured per-realm and per-client."
sources:
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - ref:rhbk-26-4-managing-user-sessions
  - ref:rhbk-26-6-oidc-layers
provenance:
  extracted: 3
  inferred: 1
  ambiguous: 0
tags: [tokens]
status: draft
updated: 2026-07-07
graph_community: "Tokens & Sessions"
---

# How RHBK issues, scopes, and expires tokens and sessions

## Issuance

RHBK issues tokens at the **token endpoint** (`/realms/{realm}/protocol/openid-connect/token`) using these grant types ([[oidc-grant-types]]):

| Grant | Use case | Tokens issued | Recommended |
|---|---|---|---|
| Authorization Code | Web apps, native/mobile (harden with PKCE) | access + refresh + ID | Yes (OAuth 2.1) |
| Client Credentials | Machine-to-machine, no user | access only (no refresh) | Yes (OAuth2-only) |
| Device Authorization Grant | Limited-input devices | access + refresh + ID | Yes (RFC 8628) |
| CIBA | Decoupled auth (phone approval, etc.) | access + refresh + ID | Yes, confidential only |
| Implicit | No code exchange, token in URL | access + ID (no refresh) | **Discouraged** — removed in OAuth 2.1 |
| Direct Grant (password) | Raw credentials to tokens | access + refresh + ID | **Discouraged** — removed in OAuth 2.1 |

The authorization endpoint (`/realms/{realm}/protocol/openid-connect/auth`) initiates authentication for redirect-based flows. Server-to-server session-less auth uses **transient sessions** (no user session created) for service accounts with token refresh disabled (`rhbk-26-4-managing-user-sessions.md:112-117`).

## Scoping

Tokens carry claims and access boundaries shaped by four layers:

1. **`scope` parameter** — the OAuth scope parameter in the auth/token request (`openid`, `profile`, `email`, `offline_access`, custom scopes). `offline_access` grants an **offline token** (never expires by lifespan, only by idle/max if `Offline Session Max Limited` is enabled) (`rhbk-26-4-managing-user-sessions.md:93-110`).

2. **Client scopes** — default client scopes (always included) and optional client scopes (included when the client requests them). Attached to each client in the Admin Console.

3. **Protocol mappers** — rules on a client or client scope that shape what claims go into access tokens, ID tokens, UserInfo responses, and SAML assertions.

4. **Client policies** — built-in profiles ([[fapi-oauth21-profiles]]) enforce FAPI 1/2, OAuth 2.1, DPoP, PKCE S256, and other constraints automatically based on the client's metadata.

Token **audience** is controlled via the `audience` parameter or client settings; scope claims in the token must be enforced by the resource server ([[audience-and-scope-checks]]).

## Expiration — Session timeouts

Configured in **Realm Settings → Sessions tab** (`rhbk-26-4-managing-user-sessions.md:54-91`):

| Setting | What it governs |
|---|---|
| **SSO Session Idle** | OIDC user session inactivity timeout. Resets on client auth or refresh token. +2 min grace window if persistent user sessions are off (for cluster ISPN replication lag). |
| **SSO Session Max** | Absolute max lifespan of a user session. |
| **SSO Session Idle/Max Remember Me** | Longer timeouts when user checked "Remember Me". Falls back to SSO Session Idle/Max if 0. |
| **Client Session Idle** | Per-client idle timeout (child of SSO session). Overrideable per client. Typically shorter than SSO. 0 = use SSO Session Idle. |
| **Client Session Max** | Per-client max timeout. Overrideable per client. 0 = use SSO Session Max. |
| **Offline Session Idle** | Idle timeout for offline tokens. Must be used at least once per this interval or revoked. +2 min grace window (see above). |
| **Offline Session Max Limited** | Off/On. If Off, offline sessions never expire by lifespan. If On, **Offline Session Max** caps them (default 60 days). |
| **Client Offline Session Max** | Per-client max offline timeout. Evaluated only if Offline Session Max Limited is On. |
| **Login timeout** | Total time allowed for authentication. |
| **Login action timeout** | Max time per page during authentication. |

## Expiration — Token timeouts

Configured in **Realm Settings → Tokens tab**:

| Setting | What it governs |
|---|---|
| **Access Token Lifespan** | Lifetime of access tokens (JWT, short-lived). |
| **Access Token Lifespan For Implicit Flow** | Separate lifespan for tokens issued via implicit flow (no refresh token available). |
| **Revoke Refresh Token** | Enables **refresh token rotation** — each refresh consumes the current refresh token and issues a new one. On replay of an already-consumed refresh token, the entire grant family is revoked (`invalid_grant`). See [[refresh-token-rotation]]. |
| **Client login timeout** | Max time to complete Authorization Code flow. |
| User-Initiated Action Lifespan | Max time for user action permissions. |
| Default Admin-Initiated Action Lifespan | Max time for admin-sent action permissions. |
| Email Verification / Forgot Password / Execute Actions | Independent timeouts for each action type. |

## Token validation & revocation

- **JWKS (offline)** — fetch public keys from `/certs` and verify JWT signature locally. Fast. Revocation isn't immediate — token valid until `exp` (`rhbk-26-6-oidc-layers.md:203-204`). See [[oidc-token-validation]].
- **Introspection (online)** — POST token to `/token/introspect`, returns `active: true/false`. Reflects revocation immediately. Required for opaque/lightweight access tokens (`rhbk-26-6-oidc-layers.md:52-63`).
- **Token revocation endpoint** (`/revoke`) — RFC 7009. Revokes both access and refresh tokens; revoking the refresh token also revokes user consent for the client (`rhbk-26-6-oidc-layers.md:67-70`).
- **Admin "Sign out all active sessions"** — invalidates all SSO cookies but does **not** revoke outstanding access tokens (they expire naturally). See [[token-revocation]].
- **Revocation policy** — administratively set a cutoff timestamp; push to OIDC adapters. Tokens issued before that date are rejected.

## Session persistence

- **DB-backed (default)** — sessions persisted in the relational database, cached in Infinispan. Survives full cluster restarts. Load cost: ~1400 write IOPS + 0.35–0.7 vCPU per 100 login/logout/refresh ops/s (`rhbk-26-4-managing-user-sessions.md:88-91` for grace window logic; [[session-persistence-volatile]] for sizing).
- **Volatile** — cache is source of truth. All sessions lost if every pod restarts. Reduced DB load.
- **Transient sessions** — no user session stored at all; `sid`/`session_state` are empty; no token refresh. Used automatically for service-account auth with refresh disabled (`rhbk-26-4-managing-user-sessions.md:112-118`).

## Holder-of-key binding

Tokens can be **sender-constrained** so a stolen token is useless without the client's private key:
- **DPoP** (RFC 9449) — client proves possession of a key at token request; the thumbprint is embedded in the access token (`cnf.jkt`). See [[dpop]].
- **mTLS-bound tokens** (RFC 8705) — binds token to client TLS certificate thumbprint (`cnf.x5t#S256`). See [[mtls-bound-tokens]].

Both are supported (not preview) in RHBK 26.6. DPoP can be enforced via the `dpop-bind-enforcer` client policy executor or the per-client `dpop_bound_access_tokens` switch.

## References

### RH ground-truth
- `guide:server_administration_guide` — Server Administration Guide (Ch. 6 Managing User Sessions)
- `guide:securing_applications_and_services_guide` — Securing Applications and Services Guide (Ch. 2 OpenID Connect)
- `kb:rhbk-26-4-managing-user-sessions` — "Chapter 6. Managing user sessions" (26.4)
- `kb:rhbk-26-6-oidc-layers` — "Chapter 2. Securing applications and services with OpenID Connect" (26.6)

### Wiki
- [[tokens-and-sessions]] — topic page
- [[oidc-grant-types]] — supported flows
- [[oidc-token-validation]] — JWKS vs introspection
- [[refresh-token-rotation]] — per-use refresh token policy
- [[session-persistence-volatile]] — DB-backed vs volatile sessions
- [[dpop]] — DPoP sender-constraining
- [[mtls-bound-tokens]] — mTLS-bound tokens
- [[token-revocation]] — RFC 7009 revoke endpoint
- [[fapi-oauth21-profiles]] — client policy profiles for FAPI/OAuth 2.1
- [[securing-apps-oidc-saml]] — OIDC vs SAML client types

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-server_administration_guide|keycloak reference — server_administration_guide]]
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
<!-- crosslink:end -->
