---
title: SSO / OIDC Implementation Review — Evaluation-Lens MOC
type: topic
domain: keycloak
slug: sso-implementation-review
summary: An evaluation lens for reviewing whether an SSO/OIDC integration meets current best-practice standards; maps every security concept to a best-practice rule, its anti-pattern, and the observable symptom (ticket) that anti-pattern produces — enabling both proactive checklists and fault-first root-cause lookup.
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security Best Current Practice, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.txt (draft-ietf-oauth-browser-based-apps-26 OAuth 2.0 for Browser-Based Apps, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.txt (draft-ietf-oauth-v2-1-15 OAuth 2.1, fetched 2026-06-17)
  - web:https://owasp.org/www-project-application-security-verification-standard/ (OWASP ASVS, fetched 2026-06-17)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html (OWASP OAuth2 Cheat Sheet, fetched 2026-06-17)
provenance_extracted: 0
provenance_inferred: 62
provenance_ambiguous: 0
tags: [security, clients, concept]
status: draft
updated: 2026-06-17
---

# SSO / OIDC Implementation Review — Evaluation-Lens MOC

**This page is the upstream-standards evaluation lens for reviewing an SSO/OIDC implementation.** It indexes every security concept page in this wiki into two actionable checklists — one for the browser-side client/SPA and one for the backend — and provides a reverse index mapping observable faults directly to the most likely root-cause concept page.

This is the upstream/standards complement to [[oidc-client-best-practices]], which covers the same ground grounded in RHBK/Keycloak specifics. The two pages reinforce each other; do not duplicate content between them.

---

## How to use this page

Read each checklist row left to right: the **Best-practice rule** column states what the implementation must do; the **Anti-pattern** column states the most common wrong variation; the **Symptom** column names the concrete, observable ticket or fault that gap produces in production. The **Page** column links to the concept page that explains the rule in full, with normative references.

To evaluate an implementation: step through the checklist, test each rule against the code or configuration, and treat any hit in the Symptom column as confirmation of the gap. To diagnose a reported fault: jump to the [Reverse index](#reverse-index--symptom--likely-cause) and follow the concept links back to the corrective rule.

---

## Client / SPA checklist (browser Relying Party)

| Best-practice rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use Authorization Code + PKCE for every interactive flow; generate a fresh `code_verifier` per request and send `code_challenge` (S256) in the authorization request | Implicit grant; Authorization Code without PKCE; reusing a verifier across requests | Authorization code can be replayed from the browser history or network log; token endpoint rejects with `invalid_grant` after code interception | [[pkce]] |
| Register every `redirect_uri` exactly and require exact-string matching on the authorization server; treat any redirect outside registered values as fatal | Wildcard, prefix, regex, or subdomain-match in redirect validation | Authorization code or token silently redirected to an attacker-controlled URI; account takeover through open redirect | [[redirect-uri-validation]] |
| Generate a cryptographically random `state` parameter per authorization request and validate it exactly on callback; use OIDC `nonce` (random, bound to session, validated in ID Token) for every OIDC flow | Omitting `state` or `nonce`; using a predictable value; skipping validation on return | Login CSRF — attacker forces victim into attacker's session; token replay across sessions | [[state-and-nonce]] |
| Do not store access tokens or refresh tokens in `localStorage`, `sessionStorage`, or browser globals; adopt the BFF / Token Handler pattern for SPAs that need persistence | Tokens in `localStorage` "because it's easy"; tokens in `sessionStorage` "because it's not persistent" | Any XSS payload can exfiltrate tokens; attacker silently reuses stolen tokens from a different origin | [[token-storage-browser]] |
| Implement a BFF as a confidential OAuth client; let the BFF hold all tokens server-side and issue only encrypted HttpOnly cookies to the SPA | SPA acting as a public client holding tokens directly in the browser | XSS compromises token material; token theft is exploitable without any CSRF risk | [[bff-token-handler]] |
| Use the system browser (ASWebAuthenticationSession / Custom Tabs) for the authorization redirect; register a verified HTTPS redirect URI or PKCE-protected private-use URI scheme | Embedded webview; custom URI schemes without PKCE; `localhost` redirect on non-localhost port | Authorization code interceptable by another app; in-app browser used for phishing | [[native-app-oauth]] |
| Request only the scopes the operation actually needs; validate that the returned ID Token contains all expected claims before acting on them | Requesting `*` or overly broad scopes at login; trusting ID Token claims without validating `aud`, `nonce`, `iat`, `exp` | Over-privileged sessions; stale or replayed ID Tokens accepted | [[audience-and-scope-checks]] |
| Discover all authorization server endpoints at startup via the `.well-known/openid-configuration` URL; treat the `issuer` value as the canonical identifier | Hardcoding endpoint URLs; skipping issuer validation | Endpoints break silently on AS reconfiguration; issuer mismatch lets mix-up attacks succeed | [[authorization-server-metadata-discovery]] |
| When the client interacts with more than one AS, bind each authorization request to its AS and verify that the authorization response came back from the same AS | Single shared client config across multiple AS instances; no `iss` parameter or `iss` response validation | OAuth mix-up attack: honest AS issues a code that is redeemed at a malicious AS | [[issuer-identification-mixup]] |
| Validate `state` and `nonce` on every callback; additionally verify the `iss` response parameter (RFC 9207) when talking to multiple AS instances | Treating the callback URL as trusted without checking `state`; skipping `iss` response validation | Login CSRF; cross-AS code injection | [[issuer-identification-mixup]], [[state-and-nonce]] |
| Include a signed DPoP proof JWT on every token endpoint request and every API call when the AS supports DPoP | Bearer-only token usage for public clients; not binding tokens to a client key | A stolen access or refresh token can be replayed from any origin without the private key | [[dpop-sender-constraining]] |
| Implement logout via the OIDC RP-Initiated Logout endpoint (`end_session_endpoint`); send `id_token_hint`, validate `post_logout_redirect_uri` against registered values, use `state` to detect response tampering | Clearing the local cookie without telling the AS; open `post_logout_redirect_uri`; no `state` | Session survives at the AS after client logs out; open redirect in the logout response; DoS via crafted logout URL | [[rp-initiated-logout]] |
| Handle back-channel logout tokens: expose a `backchannel_logout_uri`, validate the incoming Logout Token (signature, `iss`, `aud`, `iat`, `jti`, `events`, no `nonce`), and immediately invalidate the local session | No back-channel logout endpoint; accepting unsigned or replayed Logout Tokens | Remote logout (admin revoke, IdP session end) does not propagate to the app | [[back-channel-logout]] |
| Set CORS policy on the BFF and the token endpoint to allow only the known SPA origins; reject `Origin: null` | `Access-Control-Allow-Origin: *` on the BFF or token endpoint | Any malicious page can send credentialed requests to the BFF and harvest session data | [[cors-for-spa]] |
| Send tokens exclusively in `Authorization: Bearer` headers; never in query strings, form bodies, or custom headers | `?access_token=...` query parameter; tokens in `Referer`-leakable headers | Token appears in server logs, CDN access logs, or browser history; leaks through `Referer` | [[bearer-token-usage]] |
| Call the revocation endpoint (`token_revocation_endpoint`) when the user logs out or a token is no longer needed | Never revoking tokens; treating logout as only a local cookie clear | Stolen or leaked tokens remain valid indefinitely after the user believes they have logged out | [[token-revocation]] |

---

## Backend checklist (resource server / confidential client / BFF / service-to-service)

| Best-practice rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Validate every inbound access token: signature → `typ` → `alg` ≠ `none` → `exp` → `nbf` → `iss` (exact) → `aud` (exact) → `scope`/roles → binding proof (DPoP/mTLS) | Skipping any step; trusting the token payload without signature verification; accepting `alg: none` | Unsigned or expired tokens accepted; privilege escalation; replayed tokens work after expiry | [[access-token-validation-resource-server]] |
| Reject any token whose `aud` claim does not include this resource server's identifier; enforce scope/role claims before granting access to each operation | Accepting tokens with any `aud` value; checking scope only at the gateway but not per-operation | Token issued to service A accepted by service B (confused-deputy); overprivileged calls succeed silently | [[audience-and-scope-checks]] |
| Treat JWT header parameters as untrusted input: reject `alg: none`, reject JWK/`jku`/`x5u` header injection, enforce a fixed algorithm allowlist | Accepting the algorithm from the token header; allowing embedded JWK | An attacker crafts a valid-looking token by injecting a key they control; `alg: none` bypasses signature check entirely | [[jwt-validation-pitfalls]] |
| Bind access tokens to the client's DPoP key; verify the DPoP proof JWT (fresh `iat`, matching `htm`/`htu`, matching `jkt` thumbprint) on every request | Accepting the access token without checking the DPoP proof; ignoring `jkt` in the token | A stolen access token is replayed from a different host or client | [[dpop-sender-constraining]] |
| Where the deployment mandates FAPI 2.0 or high-value APIs: require mTLS, verify the `cnf.x5t#S256` thumbprint in the access token against the presented client certificate on every request | Accepting mTLS-bound tokens without verifying the certificate thumbprint | A stolen token is replayed from a different TLS client; mTLS tunnel provides authentication but token binding is ignored | [[mtls-bound-tokens]] |
| Use the Client Credentials grant for M2M calls; authenticate the client with a private key JWT or mTLS (not a shared secret) and request a minimal-scope token | Using ROPC or Authorization Code for automated services; using a long-lived static secret | A compromised secret grants full client impersonation; no per-request accountability | [[service-to-service-client-credentials]] |
| Keep access token lifetimes short (minutes, not hours); rotate refresh tokens on every use; detect and revoke the grant chain on refresh-token replay | Long-lived access tokens; non-rotating refresh tokens; ignoring replayed refresh tokens | A stolen access token is usable for its full (long) lifetime; a stolen refresh token is silently reused | [[refresh-token-rotation]] |
| Verify JWT access tokens locally (via JWKS); use token introspection only as a fallback or for opaque tokens; never cache an active introspection response beyond the token's `exp` | Trusting the `active` field without checking claims; caching introspection results without respecting `exp`; querying the AS on every request (latency) | Revoked tokens continue to be accepted until the cache TTL expires; or the AS becomes a latency bottleneck | [[token-introspection]] |
| Call the token revocation endpoint when a client secret is rotated, a user session ends, or a service account is decommissioned; confirm cascade revocation of all sibling tokens in the grant | Deleting tokens only from local state; not calling the revocation endpoint | Tokens remain valid at the AS; old access tokens continue to authorize requests | [[token-revocation]] |
| Maintain a JWKS cache with a reasonable TTL; re-fetch on unknown `kid`; set a minimum re-fetch interval to prevent key-confusion DoS | Fetching JWKS on every request; never rotating keys; accepting a `kid` not in the published JWKS | Key-rotation event invalidates all in-flight tokens (if never re-fetched); DoS via crafted unknown-kid tokens | [[access-token-validation-resource-server]] |
| Discover authorization server metadata at startup via the `.well-known/oauth-authorization-server` or `.well-known/openid-configuration` URL; validate the `issuer` field exactly | Hardcoded AS URLs; accepting any `iss` value in tokens | Mix-up attack succeeds; AS reconfiguration silently breaks token validation | [[authorization-server-metadata-discovery]] |
| Configure the CORS policy on the resource server / BFF to allow only known SPA origins; reflect `Vary: Origin`; do not allow credentials with wildcard origin | `Access-Control-Allow-Origin: *` with `Access-Control-Allow-Credentials: true` | Cross-origin malicious page can make credentialed API calls with the victim's session cookie | [[cors-for-spa]] |
| Accept bearer tokens only via `Authorization: Bearer`; if `POST` body or query-string extraction is needed, enforce `Cache-Control: no-store` and audit log the access | Query-string token parameters left in logs and CDN caches | Token material leaks into access logs, browser history, or shared CDN caches | [[bearer-token-usage]] |
| Reject ID Tokens presented to a resource-server endpoint; enforce `typ: at+jwt` for access tokens | Accepting any JWT without checking `typ`; sharing signing keys between ID Token and access token | An ID Token replayed as an access token is accepted; claims from the wrong token type drive authorization | [[jwt-validation-pitfalls]], [[access-token-validation-resource-server]] |
| Require PAR, PKCE S256, sender-constrained tokens, and `private_key_jwt` or mTLS client authentication when operating under FAPI 2.0 | Missing PAR; plain PKCE without sender-constraining; shared-secret client authentication | FAPI conformance suite reports profile violations; authorization server rejects requests with `invalid_request`; stolen tokens are replayable | [[fapi2-security-profile]] |

---

## Reverse index — symptom → likely cause

| Observable fault / ticket | Most likely root-cause concept(s) |
|---|---|
| Tokens readable via XSS (token exfiltration from browser storage) | [[token-storage-browser]], [[bff-token-handler]] |
| "Logged out but token still works" / session continues after logout | [[rp-initiated-logout]], [[back-channel-logout]], [[token-revocation]], [[token-introspection]] |
| `invalid_grant` on refresh / refresh races / second use of a refresh token fails | [[refresh-token-rotation]] |
| `alg=none` accepted, wrong-key JWT accepted, or embedded-JWK injection succeeds | [[jwt-validation-pitfalls]], [[access-token-validation-resource-server]] |
| Access token accepted by the wrong API (audience mismatch silently permitted) | [[audience-and-scope-checks]], [[access-token-validation-resource-server]] |
| CORS preflight failure on token endpoint or resource server (SPA blocked) | [[cors-for-spa]] |
| Authorization code interception / code replayed from history or network capture | [[pkce]], [[redirect-uri-validation]] |
| Open redirect in authorization response or logout response; OAuth mix-up attack | [[redirect-uri-validation]], [[rp-initiated-logout]], [[issuer-identification-mixup]], [[state-and-nonce]] |
| Refresh token never expires / stolen refresh token reused indefinitely | [[refresh-token-rotation]], [[token-revocation]] |
| Login CSRF — user logged in as wrong account without action | [[state-and-nonce]] |
| ID Token replayed as access token at resource server | [[jwt-validation-pitfalls]], [[access-token-validation-resource-server]] |
| Revoked token still accepted (time window beyond revocation) | [[token-introspection]], [[token-revocation]], [[access-token-validation-resource-server]] |
| Stolen access token reused from a different client or host | [[dpop-sender-constraining]], [[mtls-bound-tokens]], [[bearer-token-usage]] |
| M2M service authenticated with a long-lived shared secret that rotates infrequently | [[service-to-service-client-credentials]] |
| Native-app authorization code intercepted by another app on the same device | [[native-app-oauth]], [[pkce]] |
| FAPI 2.0 conformance test failures (`invalid_request`, `invalid_grant`, missing PAR) | [[fapi2-security-profile]], [[pkce]], [[dpop-sender-constraining]], [[mtls-bound-tokens]] |

---

## See also

- [[oidc-client-best-practices]] — the RHBK-grounded sibling to this page; covers the same implementation concerns but with RHBK/Keycloak-specific configuration details and version references. This page (sso-implementation-review) is the upstream/standards layer; consult both when reviewing an implementation against a running RHBK deployment.
- [[security-hardening-checklist]] — server-side hardening of the RHBK instance itself (realm settings, TLS, brute-force protection).
- [[fapi2-security-profile]] — detailed treatment of the OpenID Foundation FAPI 2.0 Security Profile, which mandates a strict subset of the rules above.
