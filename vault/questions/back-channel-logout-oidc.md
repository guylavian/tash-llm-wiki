---
origin: eval-cohort
title: What is back-channel logout in OpenID Connect?
type: question
domain: keycloak
slug: back-channel-logout-oidc
summary: "Back-Channel Logout is an OIDC mechanism where the OpenID Provider sends a signed Logout Token via server-to-server HTTP POST to registered RPs, bypassing the browser entirely — making it the reliable alternative to front-channel/iframe logout."
sources:
  - web:https://openid.net/specs/openid-connect-rpinitiated-1_0.html (OIDF Back-Channel Logout 1.0, fetched 2026-06-17)
  - ref:server-administration.md
provenance:
  extracted: 8
  inferred: 1
  ambiguous: 0
question_tier: conceptual
tags: [clients]
status: draft
updated: 2026-07-12
graph_community: "Tokens & Sessions"
---

# What is back-channel logout in OpenID Connect?

**Back-Channel Logout is a server-to-server OIDC logout mechanism: when a user's session is terminated at the OpenID Provider (OP), the OP sends a signed Logout Token via HTTP POST directly to each Relying Party's (RP) registered `backchannel_logout_uri`, with no browser involvement.** ([[back-channel-logout]]:22)

## How it works

1. **Registration (BCL §2.2):** The RP registers a `backchannel_logout_uri` with the OP. If the RP needs the `sid` claim to target individual sessions, it sets `backchannel_logout_session_required: true`. ([[back-channel-logout]]:38)

2. **Logout Token structure (BCL §2.4):** The OP issues a signed JWT with:
   - Required claims: `iss`, `aud`, `iat`, `exp`, `jti`
   - An `events` object containing `http://schemas.openid.net/event/backchannel-logout`
   - `sub` and/or `sid` identifying the session to terminate
   - `nonce` MUST NOT be present (BCL §2.4)
   - RECOMMENDED `typ: logout+jwt` header prevents cross-JWT confusion (BCL §4.1) ([[back-channel-logout]]:26)

3. **Delivery (BCL §2.5):** HTTP POST with `Content-Type: application/x-www-form-urlencoded` and a single `logout_token` form parameter. GET, JSON body, and query-string delivery are all non-conformant. ([[back-channel-logout]]:28)

4. **RP validation (BCL §2.6):** Same as ID Token validation: verify signature (reject `alg: none`), confirm `iss`/`aud`/`iat`/`exp`, check `sub` and/or `sid` are present, confirm the `events` member, assert `nonce` is absent. ([[back-channel-logout]]:30)

5. **Session teardown (BCL §2.7):** Locate sessions by `iss`+`sub` and/or `sid`, clear all associated state. Refresh tokens for that session (excluding `offline_access`) SHOULD also be revoked. ([[back-channel-logout]]:32)

6. **Response (BCL §2.8):** Return HTTP 200 or 204 on success, HTTP 400 on bad token. SHOULD set `Cache-Control: no-store`. ([[back-channel-logout]]:34)

7. **Token lifetime (BCL §4):** OPs SHOULD issue short-lived tokens — `exp` no more than ~2 minutes from `iat` — to limit replay exposure. ([[back-channel-logout]]:36)

## Why it matters — resilience advantage

Front-channel logout (iframe-based) is unreliable in modern browsers that block third-party cookies and CSP-restricted iframes (`reference/keycloak/rhbk-26-4-sso-protocols.md:216`). Back-channel logout is the durable alternative ([[back-channel-logout]]:40). It also handles logout triggers that front-channel cannot: admin-initiated logout from the Admin Console or Account Console does not have a browser session to mediate through, so only back-channel can propagate that logout to client applications (`reference/keycloak/rhbk-26-4-sso-protocols.md:222`). (extracted)

## RHBK implementation

Available since RH-SSO 7.5 (`reference/keycloak/rhsso-7-5-red-hat-single-sign-on-7-5-0-ga.md:44`). The endpoint is `/realms/{realm-name}/protocol/openid-connect/logout/backchannel-logout` (`reference/keycloak/rhbk-26-4-sso-protocols.md:242-243`). (extracted)

RHBK tries back-channel logout first when a client has no front-channel logout enabled. If `backchannel_logout_uri` is not defined, it falls back to the Admin URL, and if neither is set, logout is not propagated to the client (`reference/keycloak/rhbk-26-4-sso-protocols.md:218-219`). (extracted)

The `ref:server-administration.md` notes that when signing out all active sessions (Actions → Sign out all active sessions), SAML clients do NOT receive a back-channel logout request (`references/server-administration.md:296`). (extracted)

## Anti-patterns

From [[back-channel-logout]]:43-50: reusing an ID Token as Logout Token (has `nonce`, lacks `events`), accepting unsigned `alg: none` tokens, not revoking refresh tokens, using GET/JSON body delivery, issuing long-lived tokens (>~2 min), and relying solely on front-channel logout.

## See also

- [[back-channel-logout]] — detailed entity page
- [[rp-initiated-logout]] — browser-initiated logout that typically triggers back-channel delivery
- [[oidc-logout]] — parent page covering the full OIDC logout family
- [[token-revocation]] — explicit token revocation as a complement to session teardown
- [[token-introspection]] — for resource servers that cannot receive back-channel signals

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[references/server-administration|RHBK 26.6 — Server Administration]]
<!-- crosslink:end -->
