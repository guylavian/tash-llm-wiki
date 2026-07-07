---
title: What are the best practices for OIDC client integration with RHBK?
type: question
domain: keycloak
slug: oidc-client-best-practices-rhbk
summary: "Comprehensive answer covering flow selection, client auth, token refresh, validation, logout, DPoP, BFF pattern, and session-loss tolerance for OIDC client code integrating with Red Hat Build of Keycloak."
sources:
  - guide:securing_applications_and_services_guide
  - ref:securing-apps-oidc-saml.md
  - kb:oidc-layers-
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
provenance:
  extracted: 14
  inferred: 4
  ambiguous: 0
tags: [clients]
status: reviewed
updated: 2026-07-07
---

# What are the best practices for OIDC client integration with RHBK?

## 1. Flow selection

- **Interactive (web/mobile/native) → Authorization Code + PKCE (S256)**. Never use Implicit, Hybrid, or ROPC — these are leak-prone and removed in OAuth 2.1.
- **Machine-to-machine → Client Credentials** grant, with `private_key_jwt` or mTLS client auth.
- **Browserless devices → Device Grant or CIBA**.
- Enforce these with [[fapi-oauth21-profiles]] client policies to block deprecated flows server-side.

## 2. Discovery, never hardcode endpoints

Pull every endpoint from `/.well-known/openid-configuration` so paths and keys survive realm/version changes ([[oidc-endpoints]]). Validate the `issuer` field exactly to prevent mix-up attacks ([[issuer-identification-mixup]]).

## 3. Client authentication

- **Confidential clients** (server-side): prefer `private_key_jwt` (signed-JWT) over shared secret; secret via Basic auth or form params is acceptable.
- **Public clients** (SPA, native): **no secret** — identify by `client_id`, **require PKCE**, and sender-constrain tokens with [[dpop]].
- Confidential client is required for introspection and CIBA ([[client-authentication-methods]]).

## 4. Token refresh — where most bugs live

Correct refresh:
```
POST /realms/<realm>/protocol/openid-connect/token
grant_type=refresh_token
&refresh_token=<token>
&client_id=<id>
&client_secret=<secret>   # confidential only
```

Five rules to prevent `invalid_grant`:
1. **Refresh is single-use when rotation is on** — always replace stored token atomically with the one from the response.
2. **Never refresh concurrently** — serialize behind a single-flight lock/mutex; parallel refreshes race and the second gets `invalid_grant`.
3. **Refresh proactively before `exp`** — schedule at ~80% of `expires_in` with a safety margin for clock skew.
4. **`invalid_grant` / "Session not active" = re-authenticate the user** — the SSO session expired. Never retry forever.
5. **Store refresh tokens server-side / secure keychain** — never in `localStorage`. For public clients, sender-constrain with DPoP ([[dpop]]).

## 5. Offline tokens for background jobs

Request `scope=offline_access` to get an offline token that survives beyond the normal SSO idle timeout (bounded by *Offline Session Idle*, default 30 days). Revoke when done.

## 6. Validate access tokens on the resource server

- **Default to JWKS (offline):** fetch `jwks_uri`, cache the keys, verify JWT signature locally. Check `iss`, `aud` (exact match to this resource server), `exp`, `nbf`, `scope`/roles ([[oidc-token-validation]], [[access-token-validation-resource-server]]).
- **Reject `alg: none`** and enforce a fixed algorithm allowlist ([[jwt-validation-pitfalls]]).
- Handle key rotation: refetch on unknown `kid`.
- **Use Introspection only when you need immediate revocation** or the token is opaque; confidential-client only.

## 7. Logout and revocation

- **Redirect logout:** send user agent to `end_session_endpoint` with `id_token_hint` + `post_logout_redirect_uri` ([[rp-initiated-logout]]).
- **Back-channel logout:** expose `backchannel_logout_uri`, validate Logout Token (signature, `iss`, `aud`, `jti`, `events`), immediately invalidate local session ([[back-channel-logout]]).
- **Revocation:** call `/revoke` on sign-out to invalidate the token at the AS ([[token-revocation]]).

## 8. SPA token safety — BFF pattern

The strongest recommendation per RFC 9700 and the OAuth Browser-Based Apps draft: use a **Backend-for-Frontend / Token Handler pattern**. A confidential server-side BFF runs the Authorization Code + PKCE flow, holds all tokens server-side, and issues only encrypted HttpOnly session cookies to the browser ([[bff-token-handler]]). This eliminates token theft via XSS entirely.

If a BFF is not feasible, the public-client SPA must use:
- PKCE + DPoP (sender-constrained tokens)
- Tokens in-memory only, never `localStorage`
- Scoped CORS to the app origin ([[cors-for-spa]])

## 9. Session-loss tolerance

- **Volatile (cache-only) sessions:** a pod restart drops every session → every refresh fails. Code must degrade to a clean re-login, not crash-loop ([[session-persistence-volatile]]).
- **Cluster deployments:** prefer sticky sessions/affinity; a request hitting a node without the session returns "Session not active" ([[ha-cross-site]]).

## Quick checklist

- [ ] Auth Code + PKCE (or Client Credentials for M2M); no implicit/ROPC.
- [ ] Endpoints from discovery; JWKS cached + rotation-aware.
- [ ] Refresh is single-flight, proactive, and persists the rotated token.
- [ ] `invalid_grant` → re-auth, not infinite retry.
- [ ] Refresh tokens stored securely; public clients use PKCE + DPoP.
- [ ] Logout via `end_session_endpoint`; revoke on sign-out.
- [ ] App tolerant of session loss on restart / wrong-node routing.

## References

### RH ground-truth
- **`guide:securing_applications_and_services_guide`** — Red Hat securing-apps guide (Ch. 2 OIDC flow, client auth, token validation)
- **`ref:securing-apps-oidc-saml.md`** — wiki reference for OIDC/SAML endpoints
- **`kb:oidc-layers-`** — RHBK OIDC protocol layer reference

### Wiki pages
- [[oidc-client-best-practices]] — main synthesis page this answer builds on
- [[sso-implementation-review]] — evaluation-lens MOC with client + backend checklists
- [[bff-token-handler]] — BFF/Token Handler pattern for SPAs
- [[access-token-validation-resource-server]] — per-token validation sequence
- [[tokens-and-sessions]] — token lifespans, refresh, rotation
- [[oidc-grant-types]] — authorization code, client credentials, device, CIBA
- [[client-authentication-methods]] — secret, signed-JWT, public vs confidential
- [[oidc-token-validation]] — JWKS vs introspection
- [[oidc-endpoints]] — well-known discovery and endpoint URLs
- [[oidc-logout]] — RP-initiated logout, back-channel logout
- [[dpop]] — sender-constrained tokens
- [[session-persistence-volatile]] — volatile vs DB-backed sessions
- [[fapi-oauth21-profiles]] — FAPI/OAuth 2.1 client policy profiles

### Upstream / web
- `web:https://datatracker.ietf.org/doc/rfc9700/` — RFC 9700 OAuth 2.0 Security Best Current Practice (Jan 2025)
- `web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.txt` — OAuth 2.0 for Browser-Based Apps

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
<!-- crosslink:end -->
