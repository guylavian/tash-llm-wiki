---
origin: eval-cohort
title: What rules define how access tokens must be transmitted and handled?
type: question
domain: keycloak
slug: access-token-transmission-handling-rules
summary: RFC 6750 and the OAuth 2.0 Security BCP (RFC 9700) define strict rules for bearer-token transmission and storage — Authorization header only, TLS mandatory, no tokens in URLs/logs/cookies, short lifetimes, and sender-constraining (DPoP/mTLS) for high-value deployments.
sources:
  - kb:rhbk-26-6-securing-apps
  - kb:rhbk-26-4-securing-apps
  - kb:rhbk-26-2-securing-apps
  - kb:rhbk-26-0-securing-apps
provenance_extracted: 22
provenance_inferred: 3
provenance_ambiguous: 0
tags: "[tokens, security, bearer-token, oauth2, rfc-6750]"
question_tier: conceptual
tags: [tokens]
status: reviewed
updated: 2026-07-12
---

# What rules define how access tokens must be transmitted and handled?

Access token transmission and handling is governed by **RFC 6750** (The OAuth 2.0 Authorization Framework: Bearer Token Usage) and the **OAuth 2.0 Security Best Current Practice (RFC 9700)**. Violations cause token leakage, replay attacks, and silent access-control bypasses.

## Transmission rules

- **`Authorization: Bearer` header is mandatory** (RFC 6750 §2.1). Clients SHOULD send `Authorization: Bearer <token>`; resource servers MUST support this method ([[bearer-token-usage]]).
- **URI query parameters are forbidden** (RFC 6750 §2.3; RFC 9700 §4.3.2). The `?access_token=` method MUST NOT be used. Tokens MUST NOT appear in page URLs ([[bearer-token-usage]]).
- **Form-body parameter is tightly conditioned** (RFC 6750 §2.2). Allowed only with `Content-Type: application/x-www-form-urlencoded`, single-part ASCII body, and a non-GET HTTP method ([[bearer-token-usage]]).
- **TLS is mandatory end-to-end** (RFC 6750 §5.2; RFC 9700 §2.6). Clients MUST use HTTPS and MUST validate the certificate chain. The AS MUST NOT allow `http`-scheme redirect URIs except loopback native clients ([[bearer-token-usage]]).
- **Error responses use `WWW-Authenticate: Bearer`** with correct error codes: `invalid_token` → 401, `insufficient_scope` → 403, `invalid_request` → 400 (RFC 6750 §3.1; [[bearer-token-usage]]).

## Storage and handling rules

- **Access tokens must be short-lived** (RFC 6750 §5.3). At or below one hour; minimum necessary lifetime limits the blast radius of a leak ([[bearer-token-usage]]).
- **Bearer semantics: possession equals authorization** (RFC 6750 §1, §5.2). Any leak is equivalent to handing over the session ([[bearer-token-usage]]).
- **No browser storage is XSS-safe**. `localStorage`/`sessionStorage` are readable by any JS; the only opaque store is an HttpOnly cookie set by a server. The BFF / Token Handler pattern removes tokens from the browser entirely ([[token-storage-browser]]; [[bff-token-handler]]).
- **Referrer leakage must be suppressed**. Set `Referrer-Policy: no-referrer` (or `strict-origin-when-cross-origin`) on pages processing redirect callbacks (RFC 9700 §4.2.4; [[bearer-token-usage]]).
- **Do not log the `Authorization` header** or raw token values ([[bearer-token-usage]]).
- **Sender-constraining** upgrades bearer tokens to proof-of-possession tokens: [[dpop]] (RFC 9449) and [[mtls-bound-tokens]] (RFC 8705).

## Resource-server validation rules

- MUST validate signature, `exp`, `aud`, issuer, and required scopes before granting access ([[access-token-validation-resource-server]]).
- MUST reject tokens with a mismatched `aud` even when the signature is valid — prevents token-redirect / confused-deputy (RFC 9700 §4.10.2; [[bearer-token-usage]]).
- MUST enforce TLS all the way to the backend; cleartext internal hops leak tokens ([[bearer-token-usage]]).

## References

**RH ground-truth:**
- `kb:rhbk-26-6-securing-apps` — Red Hat build of Keycloak 26.6 Securing Applications and Services Guide (RFC 6750 compliance)
- `kb:rhbk-26-4-securing-apps` — Same, 26.4 guide
- `kb:rhbk-26-2-securing-apps` — Same, 26.2 guide (UserInfo error responses now RFC 6750 compliant)
- `kb:rhbk-26-0-securing-apps` — Same, 26.0 guide

**Wiki pages:**
- [[bearer-token-usage]] — RFC 6750 and RFC 9700 rules, anti-patterns, symptoms, client vs backend surface
- [[token-storage-browser]] — No safe browser store; BFF as the only architecture removing tokens from JS
- [[bff-token-handler]] — BFF pattern: confidential server, encrypted HttpOnly cookies, allowlisted proxies
- [[access-token-validation-resource-server]] — Cryptographic token validation by resource servers
- [[dpop]] — RFC 9449 sender-constraining (key-bound tokens)
- [[mtls-bound-tokens]] — RFC 8705 certificate-bound tokens
