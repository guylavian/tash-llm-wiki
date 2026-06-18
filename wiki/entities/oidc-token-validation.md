---
title: OIDC Token Validation — JWKS vs. Introspection
type: entity
domain: keycloak
slug: oidc-token-validation
summary: "The two ways a resource server checks an RHBK access token: offline signature verification via JWKS, or an online call to the token introspection endpoint"
sources:
  - guide:securing_applications_and_services_guide
  - guide:server_administration_guide
  - ref:securing-apps-oidc-saml.md
provenance: needs-review
tags: [clients, tokens]
status: draft
updated: 2026-06-16
---

# OIDC Token Validation — JWKS vs. Introspection

**The two ways a resource server checks an RHBK access token: offline signature
verification via JWKS, or an online call to the token introspection endpoint.**

## JWKS (offline / local)
- Fetch RHBK's public signing keys from the realm JWKS URI (advertised in the
  OIDC discovery document) and verify the JWT signature locally.
- Fast, no per-request round-trip. Validate `iss`, `aud`, `exp`, `nbf` too.
- **Tradeoff:** revocation isn't immediate — a token stays "valid" until `exp`
  even if the session was killed server-side.

## Introspection (online)
- POST the token to the **token introspection endpoint**; RHBK returns
  `active: true/false` plus claims.
- Reflects revocation/logout immediately; can surface extra claims (a protocol
  mapper can be set to add a claim *only* to introspection responses).
- **Tradeoff:** a network round-trip per validation.

## Guidance
- Use **JWKS** for high-throughput APIs with short token lifespans (pair with
  [[tokens-and-sessions]] lifespan tuning).
- Use **introspection** when immediate revocation matters or for opaque tokens.

## See also
- [[tokens-and-sessions]]
- [[oidc-endpoints]]
- [[dpop]]
- [[securing-apps-oidc-saml]]
