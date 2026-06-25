---
title: Token Revocation
type: entity
domain: keycloak
slug: token-revocation
summary: "RFC 7009 defines how clients signal an authorization server to invalidate a token immediately; correct implementation requires HTTPS-only endpoints, client-authenticated requests, and cascade invalidation of all tokens from the same grant."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection + RFC 7009 Token Revocation, fetched 2026-06-17)
provenance_extracted: 9
provenance_inferred: 3
provenance_ambiguous: 0
tags: [tokens, security, endpoint]
status: reviewed
updated: 2026-06-17
---

# Token Revocation

**The mechanism by which a client tells the authorization server to immediately invalidate a token before its natural expiry.**

## Rule

RFC 7009 §2 requires the revocation endpoint to be HTTPS only; an `http://` variant MUST NOT be advertised as the revocation endpoint.

RFC 7009 §2.1 specifies request shape: `HTTP POST` with `application/x-www-form-urlencoded`, `token` REQUIRED, `token_type_hint` OPTIONAL (`access_token` | `refresh_token`). The client MUST include its own authentication credentials, and the AS MUST verify the token was issued to that client. If the hint is wrong, the AS MUST widen the search rather than failing.

Cascade requirement (RFC 7009 §2.1): implementations MUST support refresh-token revocation; revoking a refresh token SHOULD also invalidate all access tokens derived from the same grant. Revoking an access token MAY also revoke the associated refresh token. Invalidation is immediate — not eventual.

RFC 7009 §2.2: The server MUST return HTTP 200 whether the token was revoked or was already invalid/unknown. The response body MUST NOT distinguish between the two outcomes. A `503` response means the token still exists and the client SHOULD retry.

RFC 7009 §2.2.1: If the AS cannot revoke a given token type it returns `unsupported_token_type`. An unrecognized `token_type_hint` value MUST be ignored, not rejected.

RFC 7009 §5 / §2.3: Rate-limit the endpoint against revocation-flood DoS. Clients MUST validate the server certificate and obtain the endpoint URL from a trustworthy source (e.g., [[authorization-server-metadata-discovery]]). CORS MAY be supported; JSONP MAY be offered but risks code injection (inferred: JSONP should be treated as a security concern and avoided where CORS is viable).

If the AS only supports refresh-token revocation and not access-token revocation, access tokens remain valid until natural expiry after a revocation call — account for this gap in risk analysis (inferred: access-token lifetime should be kept short in deployments lacking access-token revocation support).

## Anti-pattern

1. **Advertising an `http://` revocation URL** — allows the revocation request to be observed or stripped by a network attacker.
2. **Revoking a refresh token but not cascading to derived access tokens** — leaves existing access tokens live after logout.
3. **Returning 404 or 400 for unknown/already-expired tokens** — creates a token-existence oracle. The spec requires 200 in all non-auth-failure cases.
4. **Returning a generic 500 for `unsupported_token_type`** — callers cannot distinguish network failures from a well-defined limitation.
5. **Allowing any authenticated client to revoke another client's token** — enables cross-client DoS.
6. **Assuming access tokens die instantly when only refresh-token revocation is implemented** — produces a live-token window equal to the access-token TTL (inferred).

## Symptom

- **"Logged-out user still has API access"** — refresh token revoked but derived access tokens kept working until natural expiry; cascade invalidation was missing.
- **Token-existence oracle** — AS returns 404 vs 200 on revocation; attacker can probe whether a stolen token is still live.
- **"Wrong hint => token not revoked" bug** — AS hard-failed on a mismatched `token_type_hint` instead of searching all token types.
- **Revocation-flood DoS** — unthrottled endpoint hit by a script iterating over candidate token values.
- **Revocation request stripped on the wire** — `http://` endpoint; attacker intercepts and drops the POST.
- **Spurious 500 errors** — generic error returned for `unsupported_token_type`; client cannot classify the failure.
- **XSS via JSONP callback** — JSONP enabled on revocation endpoint; malicious page injects arbitrary script via the callback parameter.

## Surface (client vs backend)

**Client (SPA / native app / BFF front-channel):**
- On logout, POST to the revocation endpoint (URL from [[authorization-server-metadata-discovery]] `revocation_endpoint`) with the refresh token (preferred) and optionally the access token.
- Include client credentials (public clients use `client_id`; confidential clients use full client auth per [[client-authentication-methods]]).
- Treat any 200 as success regardless of response body; retry on 503; do NOT branch logic on body content.
- Drop tokens from local storage ([[token-storage-browser]]) immediately after sending the request — do not wait for confirmation beyond HTTP 200.

**Backend (confidential client / BFF / service-to-service):**
- Confidential clients MUST authenticate with their client credentials on every revocation call; the AS checks ownership.
- Resource servers relying on [[token-introspection]] should be aware that a successful revocation call does not guarantee instant propagation if introspection responses are cached — cache TTL must not exceed token `exp` (RFC 7662 §4).
- Backends implementing [[refresh-token-rotation]] should revoke the previous refresh token on each rotation rather than only at explicit logout.
- Rate-limit and monitor inbound revocation requests if the AS role is implemented locally.

## See also

- [[token-introspection]] — complementary endpoint; introspection checks whether a token is still active after revocation
- [[oidc-logout]] — coordinates revocation with session termination
- [[rp-initiated-logout]] — front-channel logout flow that typically triggers revocation
- [[back-channel-logout]] — server-driven logout that also terminates token grants
- [[refresh-token-rotation]] — revocation of previous refresh tokens on each rotation
- [[tokens-and-sessions]] — relationship between token grants and session state
- [[access-token-validation-resource-server]] — RS-side checks that must account for revocation lag
- [[token-storage-browser]] — where to store and how to clear tokens on revocation
- [[authorization-server-metadata-discovery]] — how clients locate the `revocation_endpoint`
- [[client-authentication-methods]] — credential formats used in authenticated revocation requests
- [[oidc-endpoints]] — full map of AS endpoints including revocation
- [[cors-for-spa]] — CORS configuration needed for browser-side revocation calls
- [[bff-token-handler]] — BFF pattern that centralises revocation away from the browser
- [[sso-implementation-review]]
