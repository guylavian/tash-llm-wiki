---
origin: eval-cohort
title: What must a resource server cryptographically verify on inbound access tokens?
type: question
domain: keycloak
slug: access-token-cryptographic-verification
tags: [tokens]
status: draft
summary: "A resource server must verify signature, typ, iss, aud, exp, required claims, scope, and derive identity from the token — in that order — before granting access."
question_tier: conceptual
provenance_extracted: 10
provenance_inferred: 1
provenance_ambiguous: 0
updated: 2026-07-12
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth2 Access Tokens)
  - web:https://www.rfc-editor.org/rfc/rfc6749 (RFC 6749 OAuth2 core)
  - web:https://www.rfc-editor.org/rfc/rfc6750 (RFC 6750 Bearer Token Usage)
  - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection)
  - web:https://www.rfc-editor.org/rfc/rfc7515 (RFC 7515 JWS)
  - web:https://www.rfc-editor.org/rfc/rfc7009 (RFC 7009 Token Revocation)
tags:
  - tokens
  - security
  - resource-server
  - oauth2
graph_community: "Tokens & Sessions"
---

# What must a resource server cryptographically verify on inbound access tokens?

A resource server **must execute a complete, ordered validation sequence** on every inbound access token before treating the caller as authenticated and authorized (`access-token-validation-resource-server.md:29-33`). No step may be skipped.

### 1. Transport — TLS
The token must arrive over an authenticated TLS connection. Plaintext voids all other guarantees. (extracted, `access-token-validation-resource-server.md:35-36`, citing RFC 6750 §5.2)

### 2. Extract via `Authorization: Bearer`
The RS must support `Authorization: Bearer <token>`. Query-string extraction SHOULD NOT be used. (extracted, `access-token-validation-resource-server.md:38-39`, citing RFC 6750 §2.1, §2.3)

### 3. `typ` — reject non-access tokens
RFC 9068 access tokens carry `typ: at+jwt`. The RS **must** reject tokens with absent, wrong, or `JWT` typ — this prevents ID Tokens from being replayed as access tokens. (extracted, `access-token-validation-resource-server.md:41-43`, RFC 9068 §2.1, §4)

### 4. Signature — algorithm must not be `none`
The RS must verify the signature per RFC 7515 using the `alg` in the header. `alg: none` must be rejected. (extracted, `access-token-validation-resource-server.md:44-45`, RFC 9068 §2.1)

### 5. Issuer — exact match only
`iss` must match the RS's configured trusted issuer list with **exact string equality**. No prefix or substring matching. (extracted, `access-token-validation-resource-server.md:47-48`, RFC 9068 §4)

### 6. Audience — this RS must be listed
`aud` must contain a resource indicator identifying this specific RS. A valid signature for a different audience is still an invalid token here. (extracted, `access-token-validation-resource-server.md:50-51`, RFC 9068 §4, RFC 6750 §5.2)

### 7. Expiry — reject with minimal clock-skew leeway
Current time must be before `exp`. A bounded tolerance of a few minutes maximum is acceptable; unlimited leeway or disabled expiry is not. (extracted, `access-token-validation-resource-server.md:53-54`, RFC 9068 §4, OWASP API2:2023)

### 8. Required claims — reject if absent
Profile access tokens must carry: `iss`, `exp`, `aud`, `sub`, `client_id`, `iat`, `jti`. (extracted, `access-token-validation-resource-server.md:56-57`, RFC 9068 §2.2)

### 9. Scope — enforce before granting access
Scope is space-delimited and case-sensitive. Return `insufficient_scope` (HTTP 403) when the token lacks required scope for the operation. (extracted, `access-token-validation-resource-server.md:59-60`, RFC 6749 §3.3, RFC 6750 §3.1)

### 10. Object-level authorization — derive identity from the token
The acting identity must be derived from the validated token's `sub`. The RS must **not** use a client-supplied ID from path/query/header/body. (extracted, `access-token-validation-resource-server.md:62-63`, OWASP API1:2023)

### 11. Error responses — use correct codes
Use `WWW-Authenticate: Bearer` with the appropriate error: missing token → 401 (omit error), expired/revoked → 401 `invalid_token`, insufficient scope → 403 `insufficient_scope`, malformed → 400 `invalid_request`. (extracted, `access-token-validation-resource-server.md:65-73`, RFC 6750 §3, §3.1)

### Opaque tokens
When the token is opaque (not a JWT), the RS must call the AS introspection endpoint (RFC 7662 §2.1) and check `active: true`. (extracted, `access-token-validation-resource-server.md:75-76`)

### Revocation gap
JWT validation is point-in-time; a token valid at decode may be revoked seconds later. Supplement with introspection or back-channel logout for sensitive flows. (extracted, `access-token-validation-resource-server.md:78-79`, RFC 7009 §2.1)

## References

### RH ground-truth (wiki sources)
- RFC 9068 — JWT Profile for OAuth2 Access Tokens (§2.1, §2.2, §4, §5)
- RFC 6749 — OAuth 2.0 Authorization Framework (§1.4, §3.3)
- RFC 6750 — Bearer Token Usage (§2.1, §2.3, §3, §3.1, §5.2)
- RFC 7662 — Token Introspection (§2.1, §4)
- RFC 7515 — JWS (signature verification)
- RFC 7009 — Token Revocation (§2.1)
- OWASP API Security Top 10 2023 — API1:2023 (BOLA), API2:2023 (Broken Auth)

### Wiki
- [[access-token-validation-resource-server]] — the full validation sequence
- [[audience-and-scope-checks]] — deep dive on `aud` + `scope`
- [[jwt-validation-pitfalls]] — algorithm confusion, key confusion
- [[token-introspection]] — opaque token introspection protocol
- [[token-revocation]] — RFC 7009 and the near-real-time gap
- [[bearer-token-usage]] — token transmission best practices
- [[oidc-token-validation]] — ID Token validation (distinct)
- [[dpop]] — sender-constrained tokens
- [[mtls-bound-tokens]] — mTLS-bound tokens
