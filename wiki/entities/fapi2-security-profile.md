---
title: FAPI 2.0 Security Profile
type: entity
domain: keycloak
slug: fapi2-security-profile
summary: "The OpenID Foundation FAPI 2.0 Security Profile is a hardened OAuth 2.0 / OIDC profile for high-value APIs, mandating PAR, PKCE S256, sender-constrained tokens, and strong client authentication; deviations surface as conformance failures, invalid_grant errors, or stolen-token reuse."
sources:
  - web:https://openid.net/specs/fapi-security-profile-2_0-final.html (OIDF FAPI 2.0 Security Profile final, fetched 2026-06-17)
  - web:https://openid.net/specs/fapi-2_0-attacker-model.html (OIDF FAPI 2.0 Attacker Model, fetched 2026-06-17)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [security, profile]
status: reviewed
updated: 2026-06-17
---

# FAPI 2.0 Security Profile

**A hardened OAuth 2.0 / OIDC profile that closes every major front-channel and bearer-token attack surface, used as a conformance baseline for financial-grade and high-assurance APIs.**

## Rule

The profile imposes a layered set of mandatory controls across the AS, client, and resource server. Key requirements by spec section:

**Grant and response type (§5.3.2.2)**
- `response_type=code` only; implicit, hybrid, and ROPC grants are rejected.
- PAR (RFC 9126) is mandatory: clients push all authorization parameters to `/par` first, then send only `client_id` + `request_uri` on the front-channel `/authorize`. The AS must reject any authorization request that lacks a `request_uri`.
- The `request_uri` must expire within 600 seconds.
- PKCE with `code_challenge_method=S256` is required; `plain` is forbidden.

**Authorization code (§5.3.2.1)**
- Max lifetime 60 seconds; single-use only — a replayed code must return `invalid_grant`.

**Client authentication (§5.3.2.1 / §5.3.3.1)**
- Only mTLS (RFC 8705) or `private_key_jwt` are allowed. `client_secret_*` methods are forbidden.
- For `private_key_jwt`, the `aud` claim must be the AS issuer identifier as a string scalar — not the token-endpoint URL, not a JSON array.
- Signing algorithms: `PS256`, `ES256`, or `EdDSA` (`Ed25519`). `RS256`, `HS256`, and `alg:none` are all forbidden. RSA keys must be ≥ 2048 bits, EC keys ≥ 224 bits.

**Token sender-constraining (§5.3.2.1 / §5.3.3.1 / §5.3.4)**
- Every access token must be sender-constrained via mTLS certificate binding (RFC 8705) **or** DPoP (RFC 9449). Plain bearer tokens are not acceptable.
- When using DPoP, the AS must support the server-provided nonce (`DPoP-Nonce`, RFC 9449 §8) and must bind the authorization code to the DPoP key (RFC 9449 §10.1).
- When using mTLS, the client must use `mtls_endpoint_aliases` (RFC 8705) for token requests.
- The resource server must present tokens only in HTTP headers (Authorization or DPoP), and must verify binding, expiry, and revocation. Query-parameter token delivery is forbidden.

**Issuer and metadata (§5.3.2.2 / §5.3.3.1)**
- The AS must include the `iss` parameter (RFC 9207) in authorization responses; the client must validate it to prevent mix-up attacks.
- Clients must derive all endpoints from the AS discovery document (RFC 8414 / OpenID Discovery) retrieved via a secure channel, and must verify `issuer` matches. Hardcoded endpoint URLs are not allowed.

**Miscellaneous (§5.2.1 / §5.3.2.1)**
- TLS 1.2+ required (BCP 195); server certificate validation per RFC 9525 mandatory. HTTP redirect URIs are forbidden except for loopback.
- `jwks_uri` must be served over TLS; `jku`/`x5u` JOSE headers should not be used.
- Clock-skew tolerance: accept JWTs up to ~10 s in the future; reject if > 60 s.
- Nonces: client must not exceed 64 characters.
- Refresh-token rotation should NOT be aggressive; if rotated, retain a grace window honoring the prior token to survive network retries (inferred: this is to prevent forced re-login on concurrent requests).
- Authorization flow initiation must require end-user consent and be CSRF-protected.

## Anti-pattern

Teams commonly violate FAPI 2.0 in these ways (in rough order of frequency, inferred from the attacker model threat list):

1. **Public client / SPA without a backend** — FAPI requires confidential clients only.
2. **PAR left optional or disabled** — parameters pushed directly on the front-channel `/authorize` GET, leaving them visible to A3a (authorization request reader) attackers.
3. **No PKCE or `plain` method** — the `S256` method is mandatory; a `plain` verifier or absent challenge degrades security.
4. **`client_secret_basic` / `client_secret_post`** — symmetric secrets are explicitly forbidden.
5. **Plain bearer access tokens** — no `cnf` claim and no binding check at the RS.
6. **`jku`/`x5u` in JWTs** — allows key injection by an attacker who can redirect the key fetch.
7. **`aud` claim as array or as token-endpoint URL** — `private_key_jwt` assertions will be rejected.
8. **Hardcoded token/auth endpoints** — bypasses discovery, opens mix-up / substitution.
9. **Long-lived or reusable codes** — code lifetime > 60 s or replayed code accepted.
10. **`RS256` or `HS256` signing** — only `PS256`, `ES256`, `EdDSA` are allowed.

## Symptom

Concrete observable failures when the above anti-patterns are deployed:

| Anti-pattern | Observed symptom |
|---|---|
| Public client | Conformance suite: "public client not allowed"; ROPC request unexpectedly succeeds |
| PAR skipped | `/authorize` returns `invalid_request` ("PAR required" / "request_uri required") |
| PKCE `plain` or missing | AS rejects `code_challenge_method=plain`; token exchange fails `invalid_grant` on verifier mismatch |
| Auth code replayed | Second token issued instead of `invalid_grant` |
| Auth code lifetime > 60 s | Conformance flags lifetime; code redeemable minutes later |
| Wrong `aud` in `private_key_jwt` | AS returns `invalid_client` |
| Bearer token (no binding) | Stolen token usable from any client; RS conformance: "token not sender-constrained" |
| Token in query param | Token leaks in proxy/server logs and `Referer` headers; revoked token still grants access |
| DPoP without `DPoP-Nonce` | AS responds `use_dpop_nonce`; client loops or errors |
| mTLS without `mtls_endpoint_aliases` | Cert thumbprint not captured; RS rejects with `invalid_token` (cert mismatch) |
| `jku`/`x5u` in JWT headers | Key injection possible; conformance flags the header |
| Hardcoded endpoints | Mix-up / token-endpoint substitution attack feasible |
| `http://` redirect URI (non-loopback) | AS rejects redirect_uri; conformance flags weak TLS |
| No CSRF on login initiation | Session fixation / forced-login; session-integrity conformance fails |
| Missing `iss` in auth response | Mix-up attack feasible; conformance flags missing/unverified `iss` |

## Surface (client vs backend)

**Client (browser SPA must use a confidential backend; native apps see [[native-app-oauth]])**

The profile prohibits pure public clients, so a browser SPA must operate through a BFF (see [[bff-token-handler]]). What the client-side layer must do:

- Initiate the flow only on user action, with CSRF protection.
- Generate a fresh PKCE S256 verifier per request and store it bound to the session.
- Send only `client_id` + `request_uri` on the front-channel `/authorize` — never full params.
- Check the `iss` parameter in the authorization response before exchanging the code.
- Not exceed 64-character nonces.
- Fetch all endpoints from the discovery document, never hardcode them.

**Backend (AS / confidential client / BFF / resource server)**

The AS side:

- Enforce confidential-client-only; reject public clients and ROPC.
- Mandate PAR; reject authorization requests without `request_uri`.
- Issue authorization codes valid ≤ 60 s, single-use.
- Accept only `PS256`/`ES256`/`EdDSA` for client assertions.
- Issue only sender-constrained tokens (mTLS or DPoP); include `cnf` claim.
- Support DPoP server nonce and authorization-code-to-DPoP-key binding.
- Publish valid discovery metadata and include `iss` in authorization responses.

The resource server side:

- Accept tokens only in HTTP headers.
- Verify `cnf` binding on every request (cert thumbprint or DPoP proof).
- Check token expiry and revocation status.

(inferred) A BFF acting as the confidential client concentrates all AS-facing secrets and `cnf` verification on the server side, making it the natural FAPI 2.0 deployment pattern for SPAs.

## Attacker model summary

The profile explicitly models five attacker classes and states which controls defeat each (inferred synthesis from the attacker-model spec):

- **A1 / A1a (web attacker / malicious AS)** — defeated by `iss` (RFC 9207) and PAR/PKCE binding.
- **A2 (network attacker)** — defeated by mandatory TLS + sender-constrained tokens.
- **A3a (authorization-request reader)** — defeated by PAR (params off the front channel) and per-request PKCE bound to client + user agent.
- **A7 (resource-request reader)** — defeated by sender-constrained tokens (a leaked token is unusable without the bound key/cert).

Out of scope: TLS breakage, compromised device/browser, weak RNG, implementation bugs, phishing.

## See also

- [[fapi-oauth21-profiles]]
- [[dpop-sender-constraining]]
- [[mtls-bound-tokens]]
- [[pkce]]
- [[bff-token-handler]]
- [[client-authentication-methods]]
- [[oidc-client-best-practices]]
- [[redirect-uri-validation]]
- [[state-and-nonce]]
- [[token-storage-browser]]
- [[refresh-token-rotation]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[rp-initiated-logout]]
- [[back-channel-logout]]
- [[cors-for-spa]]
- [[service-to-service-client-credentials]]
- [[jwt-validation-pitfalls]]
- [[authorization-server-metadata-discovery]]
- [[issuer-identification-mixup]]
- [[token-revocation]]
- [[bearer-token-usage]]
- [[oidc-grant-types]]
- [[oidc-endpoints]]
- [[oidc-token-validation]]
- [[tokens-and-sessions]]
- [[securing-apps-oidc-saml]]
- [[native-app-oauth]]
- [[dpop]]
- [[sso-implementation-review]]
