---
source: draft-ietf-oauth-v2-1-15 (OAuth 2.1)
url: https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html
fetched: 2026-06-17
status: Internet-Draft rev-15 (2 Mar 2026, Std Track intended), work-in-progress; obsoletes RFC 6749/6750 only when published
feeds: [pkce, redirect-uri-validation, refresh-token-rotation, native-app-oauth, bearer-token-usage, service-to-service-client-credentials]
---

# OAuth 2.1 (draft-15) — load-bearing requirements

Notes distilled per concept slug. Section anchors cite the OAuth 2.1 draft unless tagged otherwise.
RULE / ANTI-PATTERN / SYMPTOM per bullet. Paraphrased tightly (copyright).

## pkce

- RULE: PKCE REQUIRED for the authorization code flow (§4.1.1); AS MUST enforce `code_challenge`/`code_verifier`. Only exception: confidential client talking directly to token endpoint over a secure channel (§7.5.1). Public clients always PKCE.
  - ANTI-PATTERN: SPA/native app runs bare auth-code flow with no `code_challenge`; or AS configured to make PKCE optional.
  - SYMPTOM: stolen/intercepted `code` is redeemable by an attacker; pen-test flags "authorization code injection"; Keycloak client with "Proof Key for Code Exchange Code Challenge Method" left blank.
- RULE: If the client can do `S256` it MUST use `S256` (Mandatory-To-Implement); `plain` only when `S256` is technically impossible and the server is known to support `plain` (§4.1.1). `S256` is the only method that does not expose the verifier.
  - ANTI-PATTERN: sending `code_challenge_method=plain` (verifier == challenge) by default.
  - SYMPTOM: verifier leaks in logs/referrer; AS rejects with `invalid_request` ("plain not supported"); audit finding "weak PKCE method".
- RULE: `code_verifier` = 43–128 chars from unreserved set `[A-Z]/[a-z]/[0-9]/-/./_/~`; RECOMMENDED 32 random octets base64url-encoded → 43 chars (§4.1.1). AS MUST validate the verifier at the token endpoint.
  - ANTI-PATTERN: short/low-entropy or static verifier; reusing one verifier across requests.
  - SYMPTOM: token endpoint returns `invalid_grant` (PKCE verification failed); brute-forceable challenge.

## redirect-uri-validation

- RULE: AS MUST reject any `redirect_uri` that is not an exact string match (RFC 3986 §6.2.1 Simple String Comparison) to a registered URI (§4.1.1, §2.3.1). Full URI incl. path MUST be pre-registered. No wildcards / no prefix / no substring matching.
  - ANTI-PATTERN: registering `https://app.example.com/*` or relying on host-only / prefix matching; per-request varying redirect URIs.
  - SYMPTOM: open-redirect / code-exfiltration to attacker host; Keycloak "Invalid redirect uri" (`invalid_redirect_uri`) when a real exact URI was expected; CVE-style auth-code theft.
- RULE: redirect URI MUST be absolute, MAY have a query component, MUST NOT have a fragment (§2.3). Use `state` for per-request data rather than mutating the redirect URI (§2.3.1).
  - ANTI-PATTERN: stuffing dynamic data into the redirect path/query and registering loose patterns to allow it.
  - SYMPTOM: mismatch rejections; or loosened registration that reopens open-redirect.
- RULE: On missing/invalid/mismatched redirect URI the AS MUST NOT auto-redirect to the bad URI; SHOULD show the error to the user instead (§2.3.5). Clients MUST NOT operate open redirectors (§2.3.1, §7.12).
  - ANTI-PATTERN: bouncing the browser to an unverified `redirect_uri` to "show" the error; an app endpoint that forwards to an arbitrary `?url=` param.
  - SYMPTOM: token/code exfiltration via chained open redirect; security scanner flags open redirector.

## refresh-token-rotation

- RULE: Refresh tokens for public clients MUST be sender-constrained OR use refresh-token rotation (one-time use). OAuth 2.1 carries this from the Security BCP — see RFC 9700 §2.2.2 (the MUST) + §4.14.2 (rotation mechanism); OAuth 2.1 §1.4.3 recommends sender-constraining (DPoP RFC 9449 / mTLS RFC 8705). Note: precise in-draft anchor for the rotation MUST is in the §4.3 "Refresh Token" subsection (text tail truncated on fetch; verify exact §4.3.x number against the draft).
  - ANTI-PATTERN: public client (SPA/native) issued a long-lived, non-rotating, non-sender-constrained refresh token.
  - SYMPTOM: a stolen refresh token mints access tokens indefinitely; no replay detection; incident "refresh token replay".
- RULE: On rotation, the new refresh token MUST NOT extend the lifetime beyond the original refresh token's expiry (per RFC 9700 §4.14.2 / Browser-Based Apps BCP). If a rotated (consumed) refresh token is replayed, the AS SHOULD treat it as compromise and revoke the whole token chain (RFC 9700 §4.14.2).
  - ANTI-PATTERN: rotation that resets/extends expiry each cycle; ignoring reuse of an already-redeemed refresh token.
  - SYMPTOM: effectively immortal sessions; or attacker + legitimate client both refreshing undetected.
- RULE: If issued, refresh tokens MUST be bound to the scope and resource servers consented by the resource owner (§3.2.3) — prevents privilege escalation. Issuing a refresh token is OPTIONAL / at AS discretion (§1.3.2, §3.2.3). Clients MUST tolerate refresh tokens expiring/being revoked at any time (§1.3.2).
  - ANTI-PATTERN: refresh exchange that broadens scope or hits unintended resource servers; client assuming a fixed refresh-token lifetime.
  - SYMPTOM: scope creep on refresh; `invalid_scope`/`invalid_grant`; client breaks when AS revokes early.

## native-app-oauth

- RULE: Native apps are public clients — any embedded secret is extractable, so do NOT ship client secrets (§2.1). If credentials are needed, use Backend-For-Frontend or runtime Dynamic Client Registration (§2.1). PKCE mandatory (see pkce).
  - ANTI-PATTERN: client secret baked into the mobile/desktop binary; treating a native app as confidential.
  - SYMPTOM: secret extracted via decompile; "client_secret in APK" finding; impersonation.
- RULE: Use an external user agent (system browser / in-app browser tab), NOT an embedded webview (§8.5.1, NOT RECOMMENDED). Native redirect options: claimed `https` (§8.4.1), loopback `http://127.0.0.1`/`localhost` with variable port (§8.4.2, RFC 8252 §7.3), or private-use reverse-domain scheme e.g. `com.example.app:/cb` (§8.4.3). AS SHOULD enforce reverse-domain naming for private-use schemes (§2.3.1).
  - ANTI-PATTERN: embedded WebView capturing credentials/code; non-reverse-domain custom scheme; fixed loopback port required.
  - SYMPTOM: phishing/credential capture in webview; scheme-hijack by another app intercepting the code; "redirect_uri did not match" on loopback when AS won't allow variable port.
- RULE: Loopback is the only redirect where the AS MUST allow a variable port (exact match on everything except the port component) (§4.1.1, §2.3.1).
  - ANTI-PATTERN: registering a single hardcoded localhost port and rejecting others.
  - SYMPTOM: intermittent `invalid_redirect_uri` because the app picked an ephemeral port.

## bearer-token-usage

- RULE: Send bearer tokens in the HTTP `Authorization: Bearer <token>` header (§5.1.1) or, only if needed, form-encoded body (§5.1.2). Query-string transmission is NOT a defined method — effectively disallowed (§5.1).
  - ANTI-PATTERN: `?access_token=...` in the URL.
  - SYMPTOM: token leaks via server logs, referrer headers, browser history, proxies; "access token in URL" audit hit.
- RULE: All OAuth URLs (AS/RS/client) MUST use `https`, except loopback redirect which MAY use `http` (§1.5). Client↔RS exchange MUST have TLS confidentiality+integrity (§1.4.2). Tokens MUST be kept confidential in transit and storage (§1.4).
  - ANTI-PATTERN: token sent over plain HTTP / TLS-terminating proxy that re-emits cleartext internally.
  - SYMPTOM: token sniffed on the wire; mixed-content; downgrade.
- RULE: Bearer = pure possession (no key proof) (§1.4.2); SHOULD sender-constrain via DPoP/mTLS for high value (§1.4.3). RS signals auth errors via `WWW-Authenticate` (§5.3.1, RFC 9110).
  - ANTI-PATTERN: relying on bearer alone for sensitive APIs; no `WWW-Authenticate` on 401.
  - SYMPTOM: stolen token replayable anywhere (no binding); clients can't tell why 401 (missing/invalid/expired).

## service-to-service-client-credentials

- RULE: Client Credentials grant is for confidential clients only, no resource owner / no user context; access limited to resources owned by or pre-arranged for the client (§1.3.3, §4.2). No public-client variant exists.
  - ANTI-PATTERN: using client_credentials from a public/native/browser app; expecting user-scoped data back.
  - SYMPTOM: `invalid_client` / `unauthorized_client`; or a service account leaking through a public app's extractable secret.
- RULE: Confidential clients MUST authenticate at the token endpoint (§3.2.1) via one method (§2.4): client_secret (§2.4.1), mTLS RFC 8705, or private_key_jwt RFC 7523. Asymmetric methods preferred to resist impersonation (§7.3).
  - ANTI-PATTERN: weak/shared client secret; secret in source control; no client auth.
  - SYMPTOM: `invalid_client` (bad/missing auth); leaked secret = full service impersonation.
- RULE: A refresh token MUST NOT be issued for the client credentials grant (client can just re-request with its own credentials). Scopes requested via `scope` param, constrained per §1.4.1.
  - ANTI-PATTERN: storing/relying on a refresh token from client_credentials; over-broad scopes.
  - SYMPTOM: unexpected/ignored refresh token; over-privileged service token.

## removals vs RFC 6749/6750 (context)

- Implicit grant removed (§10.1) — use auth code + PKCE. SYMPTOM: `response_type=token` rejected (`unsupported_response_type`); legacy SPA breaks.
- Resource Owner Password Credentials (ROPC) grant removed — not defined in 2.1. SYMPTOM: `grant_type=password` → `unsupported_grant_type`.
- Bearer Token Usage (was RFC 6750) folded into §5; updated by RFC 9700 (§1.10).
- `redirect_uri` echoed in token request and re-validated for exact match (§10.2).
