---
title: Native App OAuth 2.0 (RFC 8252 / OAuth 2.1)
type: entity
domain: keycloak
slug: native-app-oauth
summary: "Rules and failure modes for OAuth 2.0 flows in mobile and desktop apps: use the system browser, PKCE mandatory, public-client registration, verified redirect URIs, and multi-AS mix-up defense."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc8252 (RFC 8252 — OAuth 2.0 for Native Apps, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 — OAuth 2.0 Security BCP, fetched 2026-06-17)
provenance_extracted: 28
provenance_inferred: 5
provenance_ambiguous: 0
tags: [clients, security, profile]
symptoms:
  - "disallowed_useragent"
  - "invalid_request"
  - "invalid_client"
  - "invalid_redirect_uri"
status: reviewed
updated: 2026-07-02
---

# Native App OAuth 2.0 (RFC 8252 / OAuth 2.1)

**OAuth 2.0 for native (mobile/desktop) apps: a profile that mandates an external user agent, PKCE, public-client registration, and verified redirect URI patterns to prevent credential theft and authorization-code interception.**

## Rule

### User-agent: system browser, not webview
RFC 8252 §4/§6 and OAuth 2.1 §8.5.1 require using an external user agent — the platform system browser or an in-app browser tab (ASWebAuthenticationSession, Chrome Custom Tab). Embedded webviews (`WKWebView`, Android `WebView`) are explicitly NOT RECOMMENDED. The host app can read keystrokes and cookies inside a webview; federated IdPs actively block the embedded user agent string.

### Auth code + PKCE — mandatory
Native apps MUST use the authorization code grant with PKCE (RFC 8252 §6/§8.1; OAuth 2.1 §4.1.1; RFC 9700 §2.1.1). Because the app is a public client, any embedded secret is extractable, so PKCE replaces the secret as the code-binding mechanism. Use `S256`; `plain` exposes the verifier and MUST NOT be used as the default (RFC 9700 §2.1.1; OAuth 2.1 §4.1.1).

### Public-client registration — no shipped secret
Native apps MUST be registered as public clients (RFC 8252 §8.4/§8.5; OAuth 2.1 §2.1). Any `client_secret` baked into the binary is extractable and MUST NOT be treated as proof of client identity by the AS. If strong client authentication is required, use a BFF or Dynamic Client Registration at runtime (inferred).

### Redirect URI patterns
RFC 8252 §7–§8.4 and OAuth 2.1 §2.3.1/§8.4.1–8.4.3 define three acceptable redirect types:

| Type | Form | Notes |
|---|---|---|
| Claimed https (App Link / Universal Link) | `https://app.example.com/oauth2callback` | SHOULD be preferred — OS verifies destination app identity |
| Private-use URI scheme | `com.example.app:/oauth2redirect` | MUST be reverse-DNS; AS SHOULD reject schemes without a "." |
| Loopback | `http://127.0.0.1:{port}/...` or `http://[::1]:{port}/...` | AS MUST allow any port; use literal IP, not `localhost` |

The AS MUST compare redirect URIs with exact string matching (RFC 9700 §2.1; OAuth 2.1 §4.1.1); no wildcards, no prefix matching. The only exception: the port component of loopback URIs (RFC 9700 §4.1.3).

### State / CSRF
RFC 8252 §8.9 requires a high-entropy random `state` bound to the pending request. RFC 9700 §2.1/§4.7.1 allows PKCE to serve as CSRF protection when the AS is confirmed to support it; if PKCE support cannot be confirmed, `state` MUST still be used. Validate the returned `state` before proceeding; do not trust unsigned `state` contents.

### Distinct redirect URI per authorization server (mix-up defense)
When a native app talks to more than one AS, RFC 8252 §8.10 and RFC 9700 §4.4.2.2 require a distinct redirect URI per issuer (or use of the `iss` parameter per RFC 9207) so the app can detect a mix-up attack. The client MUST compare the received issuer to the stored expected issuer and abort on mismatch.

### Implicit flow — removed
`response_type=token` is NOT RECOMMENDED for native apps (RFC 8252 §8.2) and effectively removed in OAuth 2.1 §10.1. There is no refresh token; the token is exposed in the redirect URI; and PKCE cannot protect it.

## Anti-pattern

- Opening the authorization endpoint inside an embedded `WebView` / `WKWebView`.
- Shipping a `client_secret` in the APK/IPA and registering the app as a confidential client.
- Running the authorization code flow without `code_challenge` / `code_verifier`.
- Using `code_challenge_method=plain` instead of `S256`.
- Registering a private-use scheme without a dot in the name (e.g. `myapp://` instead of `com.example.app://`).
- Requiring a fixed loopback port in the registered redirect URI.
- Using a single redirect URI for multiple authorization servers with no `iss` check.
- Omitting `state` or not validating it when PKCE support on the AS is unconfirmed.
- Using `response_type=token` (implicit flow) to get an access token directly.

## Symptom

- **Webview detected:** `"disallowed_useragent"` / HTTP 403 from federated IdPs; no SSO cookie reuse; credential-phishing finding in security review.
- **No PKCE:** `"PKCE code verifier not specified"` / `"Missing parameter: code_challenge"`; authorization code interceptable by co-installed malicious app; pen-test flags "authorization code injection".
- **Weak PKCE (`plain`):** verifier visible in logs/referrer; AS returns `invalid_request ("plain not supported")`; audit finding "weak PKCE method".
- **Embedded secret extracted:** `"client_secret in APK"` finding; `invalid_client` after secret rotation; impersonation by any user who decompiles the binary.
- **Bad redirect URI scheme:** scheme collision — wrong app receives the authorization code; server returns `invalid_request: Invalid parameter: redirect_uri`; open-redirect finding.
- **Fixed loopback port:** intermittent `invalid_redirect_uri` when the OS assigns a different ephemeral port.
- **Mix-up attack:** authorization code delivered to and redeemed at the wrong AS; silent account compromise (inferred).
- **Implicit flow:** access token exposed in URL fragment and browser history; no refresh token; `unsupported_response_type` once the AS enforces OAuth 2.1 (inferred).

## Surface (client vs backend)

**Client (native app) — all of the following:**
- Launch the authorization endpoint in the system browser or an in-app browser tab; never a `WebView`.
- Generate a high-entropy `code_verifier`, compute `S256` challenge, include `code_challenge` and `code_challenge_method=S256` in the authorization request.
- Generate a random `state`; validate it on the redirect callback.
- Register and use the correct redirect URI type for the platform (claimed-https preferred, private-use reverse-DNS, or loopback with ephemeral port).
- Use a distinct redirect URI per AS if the app talks to multiple issuers; validate the `iss` parameter in the response.
- Never embed a `client_secret`; register as a public client.
- Present `code_verifier` at the token endpoint.

**Backend (authorization server) — all of the following:**
- Enforce PKCE for all public-client authorization code requests; reject requests without `code_challenge` (RFC 8252 §8.1; RFC 9700 §2.1.1).
- Validate `code_verifier` at token issuance; reject on mismatch (`invalid_grant`).
- Perform exact-string redirect URI matching; allow variable port for loopback only.
- Reject non-reverse-DNS private-use schemes.
- Reject `http` redirect URIs except for loopback.
- Enforce public-client classification; treat any `client_secret` from a native app as non-binding.
- For public clients, issue rotating (one-time-use) or sender-constrained refresh tokens (RFC 9700 §2.2.2).

The resource server has no special obligations specific to native apps beyond standard [[access-token-validation-resource-server]] and [[bearer-token-usage]] rules (inferred).

## See also

- [[pkce]]
- [[redirect-uri-validation]]
- [[state-and-nonce]]
- [[refresh-token-rotation]]
- [[dpop]]
- [[bearer-token-usage]]
- [[token-storage-browser]]
- [[bff-token-handler]]
- [[issuer-identification-mixup]]
- [[authorization-server-metadata-discovery]]
- [[oidc-grant-types]]
- [[oidc-client-best-practices]]
- [[client-authentication-methods]]
- [[securing-apps-oidc-saml]]
- [[tokens-and-sessions]]
- [[client-libraries-by-stack]]
- [[fapi2-security-profile]]
- [[sso-implementation-review]]
