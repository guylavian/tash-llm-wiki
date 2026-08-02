---
title: Bearer Token Usage
type: entity
domain: keycloak
slug: bearer-token-usage
summary: "RFC 6750 and the OAuth 2.0 Security BCP (RFC 9700) define strict rules for how access tokens are transmitted and handled; violating them causes token leakage, replay attacks, and silent access-control bypasses."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc6749 (RFC 6749 + RFC 6750, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
provenance_extracted: 18
provenance_inferred: 3
provenance_ambiguous: 0
tags: [tokens, security, anti-pattern]
symptoms:
  - "invalid_token"
  - "insufficient_scope"
  - "invalid_request"
status: reviewed
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# Bearer Token Usage

**A bearer token grants access to any party that possesses it, so the entire security model rests on keeping it confidential in transit and at rest.**

## Rule

RFC 6750 and RFC 9700 establish a hierarchy of transmission methods:

- **Authorization header is mandatory** (RFC 6750 §2.1): clients SHOULD send `Authorization: Bearer <token>`; resource servers MUST support this method and MAY support the others.
- **URI query parameters are forbidden** (RFC 6750 §2.3; RFC 9700 §4.3.2): the `?access_token=` method MUST NOT be used. If absolutely unavoidable as a last resort, the request MUST include `Cache-Control: no-store` and the 2xx response MUST include `Cache-Control: private`. Tokens MUST NOT appear in page URLs.
- **Form-body parameter is tightly conditioned** (RFC 6750 §2.2): allowed only when `Content-Type: application/x-www-form-urlencoded`, body is single-part ASCII, and the HTTP method carries a body (not GET).
- **TLS is mandatory end-to-end** (RFC 6750 §5.2; RFC 9700 §2.6): clients MUST use HTTPS and MUST validate the certificate chain. The AS MUST NOT allow `http`-scheme redirect URIs except loopback native clients. Internal TLS termination before the resource server creates a cleartext hop that still leaks tokens (inferred).
- **Access tokens must be short-lived** (RFC 6750 §5.3): issue tokens with the minimum necessary lifetime — guidance is at or below one hour — to limit the blast radius of any leak.
- **Referrer leakage must be suppressed** (RFC 9700 §4.2.4): set `Referrer-Policy` so that authorization-response URLs carrying codes or tokens are not sent to third-party resources.
- **Bearer semantics: possession equals authorization** (RFC 6750 §1, §5.2): the token carries no intrinsic binding to the holder, so any leak is equivalent to handing over the session. Storing a bearer token in cleartext — cookie, log, local storage — is equivalent to storing a password (inferred).

## Anti-pattern

| Pattern | Problem |
|---|---|
| `?access_token=...` appended to GET URLs | Token in query string |
| Logging the `Authorization` header | Persistent token exposure |
| HTTP (non-TLS) to resource server | Wire interception |
| Disabled TLS certificate validation | MITM / DNS hijack |
| Long-lived or never-expiring access tokens | Leaked token valid indefinitely |
| Storing the token in cleartext cookies or `localStorage` | Token readable by XSS or server logs |
| Default `Referrer-Policy` on a page that processed an auth redirect | Code or token in `Referer` header sent to third-party origins |

## Symptom

- **Token stolen from logs / replay incident** — `?access_token=` appears in access logs, browser history, or proxy logs; the same token is replayed from a different IP or user agent with no error.
- **401 on a well-formed request** — resource server only parses the query param; header-using clients are rejected silently.
- **"Token still valid after logout" or long-term unauthorised access** — long-lived access token issued; revocation or short-expiry was not enforced.
- **DNS-hijack or MITM token theft** — plaintext HTTP or disabled certificate validation; bearer token captured on the wire.
- **Code/state leaked to analytics** — `Referer` header carries the authorization-response URL to a third-party script included on the callback page.

## Surface (client vs backend)

**Client (browser SPA / native app / BFF frontend):**
- Always transmit via `Authorization: Bearer` header, never in the URL.
- Set `Referrer-Policy: no-referrer` (or at least `strict-origin-when-cross-origin`) on pages that process redirect callbacks.
- Do not log the Authorization header or the raw token value.
- Store the token in memory where possible; avoid `localStorage` for high-value tokens (see [[token-storage-browser]]).
- Treat the token lifetime as a hard deadline; schedule refresh before `exp`, not after a 401.

**Backend (resource server / confidential client / service-to-service):**
- MUST support `Authorization: Bearer` header extraction; query-param and body-param support is optional.
- On missing or invalid token, return `WWW-Authenticate: Bearer` with the correct error code: `invalid_token` → 401 (client may retry with a fresh token), `insufficient_scope` → 403, `invalid_request` → 400 (RFC 6750 §3.1). Returning 500 or using wrong status codes breaks client auto-refresh logic.
- Validate signature, `exp`, `aud`, and required scopes before granting access (see [[access-token-validation-resource-server]] and [[audience-and-scope-checks]]).
- Reject tokens not addressed to this resource server (`aud` mismatch) even when the signature is valid — token-redirect / confused-deputy (inferred, spanning RFC 6750 §5.2 and RFC 9700 §4.10.2).
- Enforce TLS all the way to the backend; do not accept tokens over a cleartext internal hop.

For sender-constraining (DPoP / mTLS) that upgrades a bearer token to a proof-of-possession token, see [[dpop]] and [[mtls-bound-tokens]].

## See also
- [[pkce]] — public clients obtaining these tokens must use PKCE
- [[oidc-client-best-practices]] — RHBK-specific client guidance for issuing the bearer tokens

- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[token-storage-browser]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[dpop]]
- [[refresh-token-rotation]]
- [[cors-for-spa]]
- [[jwt-validation-pitfalls]]
- [[oidc-token-validation]]
- [[oidc-logout]]
- [[rp-initiated-logout]]
- [[back-channel-logout]]
- [[token-revocation]]
- [[token-introspection]]
- [[tokens-and-sessions]]
- [[oidc-grant-types]]
- [[oidc-endpoints]]
- [[fapi2-security-profile]]
- [[fapi-oauth21-profiles]]
- [[securing-apps-oidc-saml]]
- [[client-authentication-methods]]
- [[service-to-service-client-credentials]]
- [[bff-token-handler]]
- [[sso-implementation-review]]
