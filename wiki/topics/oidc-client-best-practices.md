---
title: OIDC Client Best Practices — Writing the Integration Code Correctly
type: topic
domain: keycloak
slug: oidc-client-best-practices
summary: How to write app code that talks to RHBK/Keycloak so flow choice, client auth, token refresh, validation, logout, and session loss behave correctly — RHBK-grounded rules plus RFC 9700 upstream best practice.
sources:
  - guide:securing_applications_and_services_guide
  - ref:securing-apps-oidc-saml.md
  - kb:oidc-layers-
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
source_notes:
  - "[[rhbk-26-6-oidc-layers]]"
provenance_extracted: 14
provenance_inferred: 6
provenance_ambiguous: 0
tags: [clients, concept]
status: reviewed
updated: 2026-06-16
---

# OIDC Client Best Practices — Writing the Integration Code Correctly

**How to write an app that talks to RHBK/Keycloak so tokens, refresh, validation,
and logout behave correctly and securely.** Every rule below is grounded in a
linked wiki page.

## 1. Pick the right flow ([[oidc-grant-types]])
- **Web / mobile / native → Authorization Code + PKCE.** Never roll your own.
- **Machine-to-machine (no user) → Client Credentials.**
- **Browserless devices → Device Grant or CIBA.**
- **Do NOT use** Implicit, Hybrid, or Direct Grant (ROPC) — leak-prone and
  removed in OAuth 2.1. Enforce their absence with [[fapi-oauth21-profiles]].

## 2. Bootstrap from discovery, never hardcode URLs ([[oidc-endpoints]])
Pull every endpoint from `/.well-known/openid-configuration` so paths and keys
survive realm/version changes:
```
GET https://<host>/realms/<realm>/.well-known/openid-configuration
→ authorization_endpoint, token_endpoint, jwks_uri, end_session_endpoint,
  revocation_endpoint, introspection_endpoint ...
```

## 3. Authenticate the client correctly ([[client-authentication-methods]])
- **Confidential client** (server-side, has a secret store): prefer
  **`private_key_jwt`** (signed-JWT) over a shared secret; secret is fine if you
  must, via Basic auth or form params.
- **Public client** (SPA, native): **no secret** — identify by `client_id`,
  **require PKCE**, and sender-constrain tokens with **[[dpop]]**.
- Confidential client is **required** for introspection and CIBA.

## 4. The refresh code — where most bugs live ([[tokens-and-sessions]])
Correct refresh request to the token endpoint:
```http
POST /realms/<realm>/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=<the_refresh_token>
&client_id=<id>
&client_secret=<secret>        # confidential only; public clients omit (use PKCE/DPoP)
```
Rules that prevent `invalid_grant`:
1. **Refresh is single-use when rotation is on.** If the realm has *Revoke
   Refresh Token* enabled, every refresh returns a **new** refresh token and
   invalidates the old one. **Always replace your stored token with the one from
   the response**, atomically.
2. **Never refresh the same token concurrently.** Two parallel calls / retries /
   browser tabs racing the same refresh token → the second gets `invalid_grant`.
   Serialize refresh behind a single-flight lock/mutex.
3. **Refresh proactively, before `exp`** — schedule on `expires_in`, don't wait
   for a 401. Leave a safety margin (e.g. refresh at 80% of lifetime) for clock
   skew.
4. **A refresh token only lives as long as the SSO session.** It dies at *SSO
   Session Idle* / *Max* (or *Offline Session Idle* for `offline_access`). Treat
   `invalid_grant` / `Session not active` as "**re-authenticate the user**", not
   as a bug to retry forever.
5. **Store refresh tokens securely** — server-side / secure keychain, never in
   `localStorage`. For browser/native, sender-constrain with [[dpop]].

## 5. Long-lived background access → `offline_access`
Request `scope=offline_access` to get an **offline token** that survives idle
beyond the normal SSO idle (bounded by *Offline Session Idle*, default 30 days).
Use only for true background jobs; revoke when done.

## 6. Validate access tokens on the resource server ([[oidc-token-validation]])
- **Default to JWKS (offline):** fetch `jwks_uri`, **cache the keys**, verify the
  JWT signature locally, and check `iss`, `aud`, `exp`, `nbf`. Fast, no round-trip.
- **Use Introspection (online)** only when you need **immediate revocation** or
  the token is opaque. Confidential-client only.
- Don't fetch JWKS per request, and **do** handle key rotation (refetch on
  unknown `kid`).

## 7. Log out properly ([[oidc-logout]] · [[oidc-endpoints]])
- **Redirect logout:** send the user agent to `end_session_endpoint` (with
  `id_token_hint` + `post_logout_redirect_uri`).
- **Back-channel logout:** call the endpoint directly with the **refresh token +
  client credentials**.
- To kill a specific token now, hit the **revocation endpoint** (`/revoke`) —
  revoking a refresh token also clears the user's consent.

## 8. Don't assume sessions survive everything ([[session-persistence-volatile]] · [[ha-cross-site]])
- If the deployment uses **volatile (cache-only) sessions**, a full pod restart
  drops every session → every refresh fails. Your code must degrade to a clean
  re-login, not crash-loop on retries.
- In a cluster, prefer **sticky sessions/affinity**; a request hitting a node
  without the session returns `Session not active`.

## 9. DPoP for public clients ([[dpop]])
For SPAs/native, enable `dpop_bound_access_tokens`: generate a key pair, send a
fresh single-use **DPoP proof JWT** (`htm`/`htu`/`jti`/`iat`, plus `ath` to
resources) per request. A stolen token is then useless without the private key.
Note RHBK enforces the DPoP proof on **refresh, UserInfo, and logout** for public
clients.

## Upstream / OSS best practice — RFC 9700 (upstream)
RHBK is downstream of OSS Keycloak; the current authority for client security is
**IETF RFC 9700 — Best Current Practice for OAuth 2.0 Security (Jan 2025)**. Key
rules, applicable to every stack:
- **PKCE is mandatory** for the authorization code flow — *all* public clients,
  and recommended for confidential ones. **Implicit flow must not be used.**
- **Refresh-token rotation** for public clients: each refresh issues a new refresh
  token and invalidates the old; the server **revokes the whole chain on replay
  detection** (your client must then re-authenticate). Maps directly to RHBK's
  *Revoke Refresh Token* setting — turn it on.
- **Minimal token lifetimes:** sensitive APIs ~5–15 min access tokens, refresh
  7–30 days; general-purpose 30–60 min access. Shorten in Realm → Tokens.
- **Exact redirect-URI matching** + `state` for CSRF; bind tokens with **DPoP or
  mTLS** for high-security ([[dpop]]).
- **SPAs: keep tokens out of the browser where you can** — prefer a **BFF
  (Backend-For-Frontend) / Token Handler** pattern (a server-side confidential
  client holds the tokens, the browser holds only a session cookie). This sidesteps
  XSS token theft entirely and is the strongest current SPA recommendation.
_Source: web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16). Upstream/IETF guidance — directionally authoritative; confirm RHBK feature/flag support per version in the Red Hat sources._

## Per-stack guidance (which library) ([[client-libraries-by-stack]])
- **Java server-side (confidential client):** native platform OIDC — **EAP 8
  native OIDC**, **Spring Security**, or **Quarkus OIDC** — *not* the removed
  Keycloak Java adapters ([[adapter-migration]]). Tokens live server-side; this is
  the safest pattern.
- **Node:** a certified OIDC RP library (e.g. `openid-client`) or your framework's
  OIDC middleware; confidential client if server-side, BFF for SPA backends.
- **SPA (Angular/React/etc.):** public client + PKCE via **keycloak-js**
  (official) / **keycloak-angular** wrapper, or a provider-agnostic lib
  (`angular-auth-oidc-client`). Add DPoP or move to a BFF for token safety.
See [[client-libraries-by-stack]] for the full comparison and citations.

## Quick checklist
- [ ] Auth Code + PKCE (or Client Credentials for M2M); no implicit/ROPC.
- [ ] Endpoints from discovery; JWKS cached + rotation-aware.
- [ ] Refresh is single-flight, proactive, and **persists the rotated token**.
- [ ] `invalid_grant` → re-auth, not infinite retry.
- [ ] Refresh tokens stored securely; public clients use PKCE + DPoP.
- [ ] Logout via `end_session_endpoint`; revoke on sign-out.
- [ ] App tolerant of session loss on restart / wrong-node routing.

## Contradictions / caveats
- Realm token settings (lifespans, *Revoke Refresh Token*, offline idle) control
  much of this behavior server-side — confirm them per realm; client overrides
  win over realm defaults ([[tokens-and-sessions]]).
- DPoP is a full feature in RHBK 26.6, preview in earlier 26.x — check the flag
  ([[dpop]]). Token-exchange support status also varies by version.

## See also
- [[securing-apps-oidc-saml]] — the RHBK adapter/endpoint reference these practices apply to
- [[tokens-and-sessions]]
- [[oidc-grant-types]]
- [[client-authentication-methods]]
- [[oidc-token-validation]]
- [[oidc-endpoints]]
- [[oidc-logout]]
- [[dpop]]
- [[session-persistence-volatile]]
- [[fapi-oauth21-profiles]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
<!-- crosslink:end -->
