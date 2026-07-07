---
title: Token Introspection
type: entity
domain: keycloak
slug: token-introspection
summary: "RFC 7662 defines a protected POST endpoint that lets a resource server ask the authorization server whether a token is currently active; misuse of the `active` flag or weak caching is the primary cause of revoked tokens remaining valid."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection, fetched 2026-06-17)
provenance_extracted: 14
provenance_inferred: 3
provenance_ambiguous: 0
tags: [tokens, security, endpoint]
symptoms:
  - "\"active\": false"
  - "invalid_token"
  - "400 Bad Request"
  - "415 Unsupported Media Type"
status: reviewed
updated: 2026-07-02
---

# Token Introspection

**A protected HTTP POST endpoint exposed by the authorization server that returns `{"active": true|false}` — and optionally token metadata — so a resource server can determine a token's current validity without maintaining local revocation state.**

## Rule

**Request format (RFC 7662 §2.1).** The request MUST be `HTTP POST` with an `application/x-www-form-urlencoded` body. The `token` parameter is REQUIRED; `token_type_hint` is OPTIONAL. JSON bodies and GET requests are not supported.

**Endpoint authentication (RFC 7662 §2.1, §4).** The introspection endpoint MUST require the caller to authenticate — typically via client credentials. The AS SHOULD restrict which resource servers are permitted to call it. An open endpoint lets any party probe token validity.

**The `active` flag is gate zero (RFC 7662 §2.2).** The response MUST include `active` (boolean). `active: true` means: issued by this AS, not revoked, and within its validity window. When `active` is `false` the AS SHOULD NOT return any other claims. Resource servers MUST check `active` first before reading any other claim.

**Optional claims (RFC 7662 §2.2).** The response MAY include `scope`, `client_id`, `username`, `token_type`, `exp`, `iat`, `nbf`, `sub`, `aud`, `iss`, `jti`. None are guaranteed; resource servers must treat each as optional.

**HTTP status semantics (RFC 7662 §2.3).** Bad caller credentials return `401`. A valid request for an unknown or inactive token returns `200 {"active": false}` — not a 4xx. The error code `invalid_token` (RFC 6750) is the correct bearer error for a rejected token at the resource server.

**Transport (RFC 7662 §4).** TLS 1.2 is the minimum. The resource server MUST validate the AS server certificate on every introspection call.

**Caching (RFC 7662 §4).** Cached `active: true` responses MUST NOT outlive the token's `exp`. Caching is permissible to reduce latency, but the TTL must be bounded by the token lifetime (inferred).

**Complete state checks (RFC 7662 §4).** Even when the AS returns `active: true`, it MUST have checked expiry, not-before, revocation status, and signature (if signed). The resource server should not skip its own local checks on the assumption that introspection did them (inferred).

**Relationship to JWT access tokens (inferred).** When access tokens are structured JWTs per RFC 9068 (`typ: at+jwt`), a resource server can validate most claims locally without calling introspection. Introspection remains necessary for revocation checking because a valid JWT signature does not imply the token has not been revoked since issuance. See [[access-token-validation-resource-server]] and [[oidc-token-validation]].

## Anti-pattern

1. **GET or JSON body.** Calling introspection over GET or sending a JSON body — the endpoint returns `400`/`415`.
2. **Unauthenticated endpoint.** Exposing introspection without requiring caller credentials enables token-scanning: an attacker iterates candidate tokens to discover valid ones.
3. **Skipping `active` and reading other claims directly.** Resource servers that read `exp` or `scope` without first asserting `active: true` will accept expired or revoked tokens whose metadata happens to look valid.
4. **Assuming optional claims are present.** Hard-failing when `aud`, `scope`, or another optional claim is absent breaks against a spec-compliant AS that omits them.
5. **Conflating 401 (caller auth failure) with "token invalid".** A `401` means the resource server's own credential is wrong, not that the user's token is bad.
6. **Long-TTL caching ignoring `exp`.** Caching `active: true` with a fixed multi-minute window means revoked tokens pass until the cache entry expires.
7. **Disabled TLS certificate validation.** Allows a MITM to forge `active: true` responses for arbitrary tokens.

## Symptom

| Fault | Observable behaviour |
|---|---|
| GET / JSON body | `400 Bad Request` or `415 Unsupported Media Type` from the introspection endpoint; "invalid request" error |
| Open endpoint | Token-scanning in access logs; no `client_id` on introspection hits |
| Skip `active` check | Revoked or expired token still authorises API calls; tickets: "user still has access after logout" |
| Optional claim assumption | `NullPointerException` / "missing claim" crashes in resource server code against spec-compliant AS |
| Conflate 401 with bad token | Valid users denied while the RS credential is misconfigured; RS logs a non-JSON parse error on the `401` body |
| Long-TTL cache | "Revocation doesn't take effect immediately"; revoked-but-cached access window |
| No cert validation | MITM forges `active: true`; tokens validated against spoofed endpoint — silent |
| `active: true` but no revocation check | `invalid_grant` or "logged-out user still has API access" persisting until token natural expiry |

## Surface (client vs backend)

**Browser/SPA client — none.** Clients never call the introspection endpoint directly. Token introspection is a server-to-server protocol. A public client has no safe way to authenticate itself to the endpoint. See [[token-storage-browser]] and [[bff-token-handler]] for how SPAs should handle token state.

**Backend / resource server.** All introspection work lives here:
- Authenticate to the introspection endpoint using client credentials (e.g. `client_id` + `client_secret`, or mTLS — see [[client-authentication-methods]] and [[mtls-bound-tokens]]).
- POST `token=<opaque_or_jwt>&token_type_hint=access_token`.
- Assert `active: true` before reading any other claim.
- Cache the response up to but not beyond `exp`.
- Validate the AS server certificate; use TLS 1.2+.
- Return `WWW-Authenticate: Bearer error="invalid_token"` (HTTP 401) to the caller when introspection returns `active: false`.

For confidential back-end services calling each other, introspection integrates naturally with the [[service-to-service-client-credentials]] pattern. For BFF architectures, the BFF layer calls introspection and the browser never sees the raw token. See [[bff-token-handler]].

## See also

- [[token-revocation]] — RFC 7009; the complementary endpoint to revoke tokens; introspection and revocation are the two-sided real-time token-state protocol
- [[access-token-validation-resource-server]] — full RFC 9068 JWT validation sequence that supplements or replaces introspection for structured tokens
- [[oidc-token-validation]] — RHBK-specific token validation and the local JWT fast path
- [[tokens-and-sessions]] — how Keycloak models token lifetimes and session state
- [[audience-and-scope-checks]] — `aud` and `scope` claims the introspection response may carry
- [[jwt-validation-pitfalls]] — `typ: at+jwt` confusion and why signature validity alone is not sufficient
- [[client-authentication-methods]] — how the resource server authenticates to the introspection endpoint
- [[mtls-bound-tokens]] — sender-constraining that supplements introspection for proof-of-possession
- [[dpop]] — DPoP as an alternative sender-constraint mechanism
- [[oidc-endpoints]] — where the introspection endpoint appears in discovery metadata
- [[authorization-server-metadata-discovery]] — `introspection_endpoint` field in AS metadata
- [[back-channel-logout]] — back-channel logout drives revocations that introspection must reflect
- [[oidc-logout]] — session termination flows that trigger revocation
- [[bff-token-handler]] — BFF pattern where introspection stays server-side, invisible to the browser
- [[service-to-service-client-credentials]] — M2M flows where introspection is the primary validation path
- [[cors-for-spa]] — introspection is NOT a cross-origin browser call; CORS does not apply here
- [[sso-implementation-review]] — MOC
