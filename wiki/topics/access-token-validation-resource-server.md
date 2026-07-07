---
title: Access Token Validation at the Resource Server
type: topic
domain: keycloak
slug: access-token-validation-resource-server
summary: "A resource server must cryptographically verify every inbound access token — signature, expiry, issuer, audience, and scope — before granting any access; skipping or weakening any of these checks is the most common single point of privilege-escalation in OAuth2 APIs."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth2 Access Tokens, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc6749 (RFC 6749 OAuth2 core + RFC 6750 Bearer usage, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection + RFC 7009 Token Revocation, fetched 2026-06-17)
  - web:https://owasp.org/API-Security/editions/2023/en/0x11-t10/ (OWASP API Security Top 10 2023, fetched 2026-06-17)
provenance_extracted: 28
provenance_inferred: 5
provenance_ambiguous: 0
tags: [tokens, security, procedure]
symptoms:
  - "invalid_token"
  - "insufficient_scope"
  - "alg:none"
  - "WWW-Authenticate: Bearer error=\"invalid_token\""
  - "HTTP 401"
  - "HTTP 403"
status: reviewed
updated: 2026-07-02
---

# Access Token Validation at the Resource Server

**Every endpoint that accepts an OAuth2 access token must execute a complete, ordered validation sequence before treating the caller as authenticated and authorized.**

## Rule

The normative validation sequence for a JWT access token at a resource server (RS) is defined across RFC 9068 §4, RFC 6750 §3, and RFC 6749 §1.4. Each step is mandatory; no step may be skipped on the assumption another will catch it.

### 1. Transport — TLS before anything else
The token must arrive over an authenticated TLS connection. RS must validate the server certificate on every upstream call (introspection, JWKS fetch). Plaintext transmission voids all other guarantees (RFC 6750 §5.2).

### 2. Extract via Authorization header
The RS MUST support `Authorization: Bearer <token>` as the primary (and only mandatory) extraction method. Query-string extraction (`?access_token=`) SHOULD NOT be used; if unavoidable, the response must include `Cache-Control: no-store` (RFC 6750 §2.1, §2.3).

### 3. Header `typ` — reject non-access tokens
JWT access tokens profiled under RFC 9068 carry `typ: at+jwt` (or `application/at+jwt`). The RS MUST reject any token whose `typ` is absent, wrong, or `JWT` — this prevents ID Tokens from being replayed as access tokens (RFC 9068 §2.1, §4). Key separation between ID Token and access-token signing keys is NOT a substitute (inferred from RFC 9068 §5 and RFC 8725 §2.8): the RS accepts all keys published in AS discovery metadata, so key diversity does not achieve isolation.

### 4. Signature — algorithm must not be `none`
The RS MUST verify the signature per RFC 7515 using the `alg` declared in the header. `alg: none` MUST be rejected. The AS MUST support at minimum RS256 as a signing algorithm (RFC 9068 §2.1).

### 5. Issuer — exact match only
`iss` MUST be compared against the RS's configured, trusted issuer list using exact string equality. Prefix matching, substring checks, or "any issuer signed by my AS" logic must be rejected (RFC 9068 §4; also the issuer-confusion attack surface documented in [[issuer-identification-mixup]]).

### 6. Audience — this RS must be listed
`aud` MUST contain a resource indicator that identifies this specific RS. The RS MUST reject tokens where `aud` does not include it. A valid signature from a trusted issuer for a different audience is still an invalid token here (RFC 9068 §4; RFC 6750 §5.2). Distinct `aud` per resource also prevents cross-JWT confusion between resources sharing the same issuer (RFC 9068 §5; inferred link to [[audience-and-scope-checks]]).

### 7. Expiry — reject with minimal clock-skew leeway
Current time MUST be before `exp`. A small, bounded clock-skew tolerance (a few minutes maximum) is acceptable; unlimited leeway or disabled expiry checking is not (RFC 9068 §4; OWASP API2:2023).

### 8. Required claims — reject if any are absent
Profile access tokens MUST carry: `iss`, `exp`, `aud`, `sub`, `client_id`, `iat`, `jti` (RFC 9068 §2.2). The RS must not tolerate absent required claims. For client-credentials flows (no resource owner), `sub` identifies the client application, not a human — the RS must not assume `sub` is always an end-user (RFC 9068 §2.2).

### 9. Scope — enforce before granting access
Scope is space-delimited and case-sensitive. The RS must verify the token carries the required scope for the requested operation, and return `insufficient_scope` (HTTP 403) when it does not (RFC 6749 §3.3; RFC 6750 §3.1). Authorization on scope presence must be combined with `aud` — a scope valid for one API does not authorize another (inferred from RFC 9068 §2.2.3 and §4).

### 10. Object-level authorization — derive identity from the token
The acting identity MUST be derived from the validated token's `sub` and authorization claims. The RS MUST NOT use an ID supplied in the path, query string, header, or request body to decide who the caller is (OWASP API1:2023, BOLA). Any high-impact action (security-critical account mutations) requires re-authentication or step-up, not merely a valid access token (OWASP API2:2023).

### 11. Error responses — use the correct codes
On any validation failure the RS MUST respond with `WWW-Authenticate: Bearer` and the appropriate error code (RFC 6750 §3, §3.1):

| Condition | HTTP status | `error` value |
|---|---|---|
| Missing token | 401 | (omit error field) |
| Expired / revoked / malformed | 401 | `invalid_token` |
| Token lacks required scope | 403 | `insufficient_scope` |
| Malformed request | 400 | `invalid_request` |

### Opaque tokens — use introspection instead of local decode
When the token is opaque (not a JWT), the RS must call the AS introspection endpoint (RFC 7662 §2.1): HTTP POST with `application/x-www-form-urlencoded`, presenting its own client credentials. The RS MUST check `active: true` before consuming any other claim in the response. Introspection must be called over TLS with certificate validation (RFC 7662 §4). Cached introspection results MUST NOT outlive the token's `exp` (inferred constraint from RFC 7662 §4 — aggressive fixed-TTL caching widens the revocation window). See [[token-introspection]] for the full introspection protocol.

### Revocation and near-real-time invalidation
JWT validation is inherently point-in-time; a token valid at decode time may have been revoked seconds later. For sensitive flows, supplement local JWT validation with introspection or pair with [[back-channel-logout]] / [[token-revocation]]. Revoking a refresh token SHOULD invalidate derived access tokens, but if the AS does not propagate revocation to access tokens, existing access tokens remain valid until their natural `exp` (RFC 7009 §2.1). Account for this gap in risk analysis.

## Anti-pattern

The most prevalent failure pattern is **partial validation** — teams implement some checks but not others. Common omissions (inferred from aggregating the spec anti-patterns):

- Decoding the JWT payload without verifying the signature ("if it decodes, it's fine").
- Accepting `alg: none` because a library defaults to permissive mode.
- Skipping the `typ` check, allowing ID Tokens to be replayed at API endpoints.
- Trusting any token signed by the AS regardless of `aud` — "if it's from our issuer, accept it."
- Ignoring `exp` or setting an unbounded clock-skew leeway to suppress clock-mismatch complaints.
- Authorizing on token validity alone, without checking scope or per-object ownership.
- Using a client-supplied `user_id` in the URL/body as the acting identity instead of the token `sub`.
- Caching introspection results with a long fixed TTL, leaving revoked tokens effective for the cache window.

## Symptom

Observable faults a misconfigured RS produces — concrete enough to recognize in a ticket or security finding:

- **Unsigned/forged token accepted** — pentest finding "API accepts `alg:none` token"; attacker-crafted JWT with arbitrary claims grants access.
- **ID Token used as bearer token and honored** — `typ` check missing; audit log shows wrong token class.
- **Token from a foreign realm/AS accepted** — `iss` checked by prefix; cross-realm token confusion.
- **Expired token still works** — `exp` leeway too wide or check disabled; `WWW-Authenticate: Bearer error="invalid_token"` never reached.
- **Token minted for API-A replayed against API-B and accepted** — `aud` unchecked; token substitution / privilege crossing.
- **Any valid token can reach any endpoint** — scope not enforced; over-privileged access in pen-test findings.
- **IDOR / "I see someone else's record by editing the URL"** — RS trusted a param-supplied ID instead of token `sub` (BOLA).
- **"Logged-out user still has API access"** — revocation propagation gap; access token not invalidated after refresh-token revoke.
- **Opaque 500 on bad token** — RS returns a generic server error instead of `WWW-Authenticate: Bearer error="invalid_token"` with HTTP 401; clients cannot distinguish "refresh the token" from a server bug.
- **Client can't auto-refresh on expiry** — RS returns 403 (scope error status) for an expired token instead of 401; SDK refresh logic never triggers.

## Surface (client vs backend)

**Backend (resource server) only.** All validation steps described in this page run in the RS on every inbound request. The RS is the enforcement point.

**Client/SPA responsibilities** are complementary but distinct:
- Request the token with the minimum necessary scope.
- Send it exclusively via `Authorization: Bearer` (never in the URL).
- Discard it over plaintext channels.
- Retry with a fresh token on `invalid_token` (401); escalate to re-authorization on `insufficient_scope` (403).
- Never perform RS-side validation logic (signature verify, audience check) in browser JavaScript — the SPA does not hold the resource server's private context. See [[token-storage-browser]] and [[bff-token-handler]] for browser-side concerns.

For service-to-service flows, both the calling service (as client) and the receiving service (as RS) execute their respective sides. See [[service-to-service-client-credentials]].

## See also

- [[audience-and-scope-checks]] — deep dive on `aud` + `scope` enforcement rules
- [[jwt-validation-pitfalls]] — algorithm confusion, key-confusion, cross-JWT attacks
- [[token-introspection]] — opaque token validation via RFC 7662
- [[token-revocation]] — RFC 7009 revocation and the near-real-time invalidation gap
- [[bearer-token-usage]] — how clients must transmit tokens (RFC 6750 mechanics)
- [[oidc-token-validation]] — OIDC ID Token validation (distinct from access-token validation)
- [[issuer-identification-mixup]] — iss confusion across realms and multi-tenant AS
- [[dpop]] — sender-constraining access tokens beyond bearer
- [[mtls-bound-tokens]] — mTLS certificate-bound tokens as an alternative to plain bearer
- [[back-channel-logout]] — pushing logout events to the RS for near-real-time revocation
- [[rp-initiated-logout]] — front-channel logout complement
- [[cors-for-spa]] — CORS pre-flight on protected endpoints (403 on preflight)
- [[bff-token-handler]] — BFF pattern keeping tokens server-side, out of browser
- [[token-storage-browser]] — why SPAs must not hold access tokens in localStorage
- [[refresh-token-rotation]] — refresh strategy when access tokens expire
- [[service-to-service-client-credentials]] — machine-to-machine token flows
- [[fapi2-security-profile]] — high-security profile layering on top of these baseline rules
- [[authorization-server-metadata-discovery]] — how RS discovers the JWKS / issuer metadata
- [[oidc-client-best-practices]] — client-side complement (RHBK-specific)
- [[tokens-and-sessions]] — RHBK token and session lifecycle
- [[securing-apps-oidc-saml]] — RHBK adapter / library integration
- [[sso-implementation-review]] — MOC: SSO implementation review
