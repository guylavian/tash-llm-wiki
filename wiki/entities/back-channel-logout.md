---
title: Back-Channel Logout
type: entity
domain: keycloak
slug: back-channel-logout
summary: "A server-to-server logout mechanism in which the OpenID Provider POSTs a signed Logout Token directly to a registered RP endpoint, bypassing the browser entirely and making it the resilient alternative to front-channel/iframe logout in modern browsers."
sources:
  - web:https://openid.net/specs/openid-connect-rpinitiated-1_0.html (OIDF Back-Channel Logout 1.0, fetched 2026-06-17)
provenance:
  extracted: 9
  inferred: 2
  ambiguous: 0
tags: [tokens, security, profile]
status: reviewed
updated: 2026-06-17
---

# Back-Channel Logout

**A server-to-server OIDC logout mechanism: the OP sends a signed Logout Token via HTTP POST directly to the RP's registered `backchannel_logout_uri`, with no browser involvement.**

## Rule

**Logout Token structure (BCL §2.4):** The OP issues a signed JWT with required claims `iss`, `aud`, `iat`, `exp`, `jti`, and an `events` object containing the member `http://schemas.openid.net/event/backchannel-logout`. The token MUST contain `sub` and/or `sid` to identify which session to terminate. The claim `nonce` MUST NOT be present (BCL §2.4), and the RECOMMENDED `typ: logout+jwt` header prevents cross-JWT confusion (BCL §4.1).

**Delivery (BCL §2.5):** The OP sends an HTTP POST with `Content-Type: application/x-www-form-urlencoded` and a single `logout_token` form parameter to the registered URI. GET requests, JSON bodies, and query-string delivery are all non-conformant.

**RP validation (BCL §2.6):** The RP MUST validate the Logout Token the same way it validates an ID Token: verify the signature (`alg: none` MUST NOT be accepted), confirm `iss`/`aud`/`iat`/`exp`, check that `sub` and/or `sid` are present, confirm the `events` member is present, and assert that `nonce` is absent.

**Session teardown (BCL §2.7):** On a valid token, the RP locates sessions by `iss`+`sub` and/or `sid` and clears all associated state. Refresh tokens for that session (excluding `offline_access` tokens) SHOULD also be revoked.

**Response codes (BCL §2.8):** The RP MUST return HTTP 200 or 204 on success and HTTP 400 on a bad token. The response SHOULD set `Cache-Control: no-store`.

**Token lifetime (BCL §4):** OPs SHOULD issue short-lived Logout Tokens, preferably with `exp` no more than ~2 minutes from `iat`, to limit replay exposure.

**Registration (BCL §2.2):** The RP registers `backchannel_logout_uri` with the OP. If the RP requires a `sid` claim to target individual sessions, it sets `backchannel_logout_session_required: true`. (inferred) This makes back-channel logout the preferred logout mechanism when browser-mediated iframe approaches are blocked by third-party cookie restrictions.

**Resilience advantage (FCL §4.1, SM §5.1):** Front-channel/iframe logout is unreliable in modern browsers that block third-party content. Back-channel logout is the durable alternative and deployments relying solely on front-channel are exposed to intermittent logout failures. (inferred)

## Anti-pattern

- Reusing a plain ID Token as the Logout Token (carries `nonce`, lacks the `events` member, wrong `typ`).
- Accepting unsigned or `alg: none` Logout Tokens.
- Not revoking the associated refresh tokens after session teardown, leaving the user re-authenticatable immediately.
- Using HTTP GET or a JSON body for token delivery instead of form-encoded POST.
- Issuing long-lived Logout Tokens (hours rather than ~2 minutes).
- Registering a `backchannel_logout_uri` but not honoring the `sid` requirement when `backchannel_logout_session_required: true`.
- Relying solely on front-channel/iframe logout and omitting back-channel registration entirely.

## Symptom

- **"logout_token missing events/sub/sid"** — RP rejects the token because the OP constructed it from the ID Token code path.
- **Token accepted with `alg: none`** — forged Logout Tokens can log out arbitrary users (DoS); no error surfaced until a security audit.
- **User re-authenticates immediately after logout** — refresh token was not revoked; cookie cleared but token still valid.
- **OP receives no callback / 400** — delivery over GET or JSON body fails parsing at the RP.
- **Logout replay accepted hours later** — long `exp` allows a captured token to be reused.
- **"still logged in elsewhere" reports** — front-channel only; back-channel not registered so server-side session survives browser iframe blocking.
- **`sid required` rejection** — OP omits `sid` but RP declared `backchannel_logout_session_required: true`; logout can't target the right session.

## Surface (client vs backend)

**Backend (RP server / confidential client / BFF):**
All the load-bearing work is server-side. The RP must expose an HTTPS endpoint at the registered `backchannel_logout_uri`, validate the Logout Token fully (signature, claims, `nonce` absent), resolve the session via `iss`+`sub`/`sid`, invalidate the server session, revoke related refresh tokens, and return the correct HTTP status. The endpoint must be reachable by the OP without browser mediation.

**Browser / SPA client:**
The browser is not involved in back-channel logout delivery at all. The SPA may receive a downstream signal (e.g., the BFF invalidates the session cookie, or a WebSocket push) and then clear local state (in-memory tokens, UI state). SPAs that store access tokens locally must rely on short token lifetimes or [[token-introspection]] since the browser gets no direct notification from the OP. (inferred)

## See also

- [[oidc-logout]] — parent page covering the full OIDC logout family
- [[rp-initiated-logout]] — browser-initiated logout that typically triggers back-channel delivery
- [[token-revocation]] — explicit token revocation as a complement to session teardown
- [[token-introspection]] — for resource servers that cannot receive back-channel signals
- [[tokens-and-sessions]] — session model that back-channel logout targets
- [[refresh-token-rotation]] — why leaving refresh tokens live after logout is dangerous
- [[token-storage-browser]] — SPA token storage patterns affected by back-channel gaps
- [[bff-token-handler]] — BFF pattern that centralizes back-channel receipt for SPAs
- [[oidc-token-validation]] — validation rules shared between ID Tokens and Logout Tokens
- [[jwt-validation-pitfalls]] — `alg: none` and cross-JWT confusion attacks
- [[securing-apps-oidc-saml]] — integration-level guidance for configuring logout
- [[cors-for-spa]] — not applicable to back-channel (server-to-server), but relevant for the SPA side receiving downstream signals
- [[sso-implementation-review]] — MOC: evaluating SSO implementations end to end
