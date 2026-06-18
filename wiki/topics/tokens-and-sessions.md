---
title: Tokens & Sessions
type: topic
domain: keycloak
slug: tokens-and-sessions
summary: "How RHBK issues, scopes, and expires access/refresh tokens, and how user sessions and their timeouts are governed"
sources:
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - ref:server-administration.md
provenance: needs-review
tags: [tokens, concept]
status: draft
updated: 2026-06-16
---

# Tokens & Sessions

**How RHBK issues, scopes, and expires access/refresh tokens, and how user
sessions and their timeouts are governed.**

## Body
- **Access token** — short-lived bearer token (JWT) presented to APIs. Lifespan
  is set per-realm (Realm Settings → Tokens) and can be overridden per client.
- **Refresh token** — used to obtain new access tokens; bounded by session
  idle/max lifespans.
- **Sessions** — SSO session idle and max lifespans cap how long a refresh chain
  survives. Validate tokens by **JWKS** (offline signature) or **introspection**
  (online, lets revocation take effect immediately) — see
  [[oidc-token-validation]].
- **Token exchange** (`urn:ietf:params:oauth:grant-type:token-exchange`) swaps a
  subject token for another token type/audience (Securing Apps Guide Ch. 13).
- **Holder-of-key** (DPoP / mTLS-bound) tokens bind a refresh/access token to the
  client, checked on refresh, UserInfo, and logout requests.

## Contradictions / caveats
- Token-exchange capabilities and their support/preview status vary by RHBK
  version — confirm in `ref:rhbk-platform-support.md` before relying on it in
  production.
- Lifespan defaults differ between realm-level and client-level overrides; the
  most specific (client) wins.

## See also
- [[oidc-token-validation]]
- [[token-exchange]]
- [[dpop]]
- [[oidc-grant-types]]
- [[securing-apps-oidc-saml]]
