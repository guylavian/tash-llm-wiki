---
source: FAPI 2.0 Security Profile + Attacker Model
url: https://openid.net/specs/fapi-security-profile-2_0-final.html
fetched: 2026-06-17
status: OIDF FAPI 2.0
feeds: [fapi2-security-profile, mtls-bound-tokens]
---

# FAPI 2.0 Security Profile + Attacker Model — raw harvest

Second URL: https://openid.net/specs/fapi-2_0-attacker-model.html
Tier: web (upstream OIDF spec) — NOT RHBK ground truth.

## fapi2-security-profile

- **RULE** (§5.3.2.1): AS shall support only confidential clients; reject ROPC (password grant).
  - **ANTI-PATTERN**: public client / SPA without backend; enabling Direct Access Grants on a FAPI client.
  - **SYMPTOM**: conformance suite flags "public client not allowed"; ROPC token request unexpectedly succeeds, failing the profile.

- **RULE** (§5.3.2.2): `response_type` shall be `code` only (authorization code grant; no implicit/hybrid).
  - **ANTI-PATTERN**: legacy `response_type=id_token`/`token`/`code id_token` hybrid flows.
  - **SYMPTOM**: AS returns `unsupported_response_type` / `invalid_request`; tokens never appear in the redirect fragment.

- **RULE** (§5.3.2.2 + client §5.3.3.2): PAR (RFC 9126) is mandatory — AS shall support client-authenticated pushed authorization requests and reject authorization requests sent without PAR; client sends only `client_id` + `request_uri` to the authorization endpoint.
  - **ANTI-PATTERN**: pushing full params (scope, redirect_uri, state) on the front-channel `/authorize` GET; PAR left optional/disabled.
  - **SYMPTOM**: `/authorize` returns `invalid_request` ("PAR required" / "request_uri required"); front-channel params silently ignored.

- **RULE** (§5.3.2.2): PKCE (RFC 7636) required with `S256` as the code challenge method; client (§5.3.3.2) generates a fresh challenge per request, bound to client + user agent.
  - **ANTI-PATTERN**: `plain` challenge method; reused/static verifier; no PKCE.
  - **SYMPTOM**: AS rejects `code_challenge_method=plain` or missing challenge; token exchange fails with `invalid_grant` on verifier mismatch.

- **RULE** (§5.3.2.2): `request_uri` from PAR shall expire in < 600 seconds (`expires_in`).
  - **ANTI-PATTERN**: long-lived / reusable `request_uri`.
  - **SYMPTOM**: stale `request_uri` accepted long after issuance; conformance flags excessive lifetime.

- **RULE** (§5.3.2.1): authorization codes shall have max lifetime of 60 seconds.
  - **ANTI-PATTERN**: minutes-long code lifetime carried over from non-FAPI config.
  - **SYMPTOM**: code still redeemable after 60s; conformance flags lifetime > 60s.

- **RULE** (§5.3.2.2): authorization code shall be rejected if previously used (single-use, no replay).
  - **ANTI-PATTERN**: idempotent/reusable code redemption.
  - **SYMPTOM**: replayed code yields a second token instead of `invalid_grant`.

- **RULE** (§5.3.2.2): AS shall return the `iss` parameter (RFC 9207) in the authorization response; client (§5.3.3.2) shall check it to prevent mix-up.
  - **ANTI-PATTERN**: omitting `iss` in the response; client not validating issuer.
  - **SYMPTOM**: mix-up attack feasible; conformance flags missing/unverified `iss`.

- **RULE** (§5.3.2.1 / §5.3.3.1): client authentication via mTLS (RFC 8705) or `private_key_jwt` only; the `aud` claim shall be the AS issuer identifier as a string (not array); `client_secret`-based methods not allowed.
  - **ANTI-PATTERN**: `client_secret_basic` / `client_secret_post`; `aud` as token-endpoint URL or JSON array.
  - **SYMPTOM**: AS returns `invalid_client`; assertion rejected for wrong/array `aud`.

- **RULE** (§5.3.2.1): refresh token rotation shall NOT be used except in extraordinary circumstances; if rotated, offer a time-limited retry honoring the old token. (Client §5.3.3.1 must still support refresh tokens and rotation.)
  - **ANTI-PATTERN**: aggressive rotate-on-every-use with immediate hard revoke of prior token.
  - **SYMPTOM**: concurrent/retried refresh causes `invalid_grant` and forced re-login (race under network retry).

- **RULE** (§5.3.2.1 timestamps): accept JWTs with `iat`/`nbf` up to ~10s in the future; reject if > 60s future. Nonce values up to 64 chars supported (client §5.3.3.2 should not exceed 64).
  - **ANTI-PATTERN**: no clock-skew tolerance, or unbounded future timestamps; oversized nonce.
  - **SYMPTOM**: valid assertions rejected on minor skew; or far-future-dated tokens accepted; nonce > 64 chars rejected.

- **RULE** (§5.3.2.1 / §5.3.3.1): AS shall publish discovery metadata; client shall use only metadata retrieved from the metadata document (RFC 8414 / OpenID Discovery), verify `issuer` matches, and obtain the URL via an authoritative secure channel.
  - **ANTI-PATTERN**: hardcoded endpoints; trusting issuer/endpoints from an untrusted channel.
  - **SYMPTOM**: endpoint mismatch vs metadata; opens mix-up / token-endpoint substitution.

- **RULE** (§5.3.3.1): client shall initiate the authorization flow only with end-user consent and protect initiation against CSRF.
  - **ANTI-PATTERN**: auto-initiating login on arbitrary GET; no CSRF token on the initiation endpoint.
  - **SYMPTOM**: forced-login / session-fixation; session-integrity conformance fails.

- **RULE** (§5.2.1): only TLS-protected endpoints, TLS 1.2+, follow BCP 195, perform server cert check (RFC 9525); authorization responses shall not traverse unencrypted connections; no `http` scheme redirect except loopback. (§5.3.2.2)
  - **ANTI-PATTERN**: `http://` redirect URIs (non-loopback); TLS < 1.2 / weak ciphers.
  - **SYMPTOM**: AS rejects `http` redirect_uri; conformance flags weak TLS.

- **RULE** (§5.4.1 / §5.4.2): signing algs limited to `PS256`, `ES256`, or `EdDSA`(`Ed25519`); `none` forbidden; RSA ≥ 2048 bits, EC ≥ 224 bits, credentials ≥ 128 bits entropy; `jwks_uri` served only over TLS; should not use `x5u`/`jku` JOSE headers.
  - **ANTI-PATTERN**: `RS256`/`HS256` or `alg:none`; attacker-supplied `jku`/`x5u`; under-sized keys.
  - **SYMPTOM**: signature verification rejects disallowed alg; key-injection via `jku` blocked; conformance flags weak key sizes.

## mtls-bound-tokens

- **RULE** (§5.3.2.1 AS / §5.3.3.1 client / §5.3.4 RS): all access tokens shall be sender-constrained, using mTLS (RFC 8705) OR DPoP (RFC 9449); AS issues only sender-constrained tokens, client and RS must support and verify the binding.
  - **ANTI-PATTERN**: plain bearer access tokens with no `cnf` binding; RS that ignores the binding.
  - **SYMPTOM**: a stolen/replayed token works from any client → conformance "token not sender-constrained"; RS accepts token presented without the bound cert/key.

- **RULE** (§5.3.4 RS): tokens accepted only in HTTP headers (RFC 6750 §2.1 bearer header, or DPoP RFC 9449 §7.1); never in query parameters; RS shall verify validity, integrity, expiration, and revocation status.
  - **ANTI-PATTERN**: `?access_token=...` in the URL; RS skips revocation/expiry checks.
  - **SYMPTOM**: token leaks in proxy/server logs and referrers; revoked token still grants access.

- **RULE** (§5.3.3.1, mTLS path): client shall support `mtls_endpoint_aliases` (RFC 8705) when using mTLS client auth or mTLS-bound tokens; binding is the client's TLS client-cert thumbprint in the token `cnf` claim.
  - **ANTI-PATTERN**: hitting the standard token endpoint (not the mTLS alias) for cert-bound flows; missing client cert on the TLS connection.
  - **SYMPTOM**: cert thumbprint not captured → token issued unbound, or RS rejects with `invalid_token` (cert mismatch) on resource calls.

- **RULE** (§5.3.2.1, DPoP path): if DPoP is used, AS shall support the server-provided nonce mechanism (RFC 9449 §8) and Authorization Code Binding to DPoP Key (RFC 9449 §10.1); client (§5.3.3.1) shall support the nonce mechanism.
  - **ANTI-PATTERN**: DPoP proof without honoring `DPoP-Nonce`; code not bound to the DPoP key.
  - **SYMPTOM**: AS responds `use_dpop_nonce` and client loops/fails; pre-auth DPoP-key swap / code-injection feasible.

## attacker model — threats the profile defends (attacker-model spec)

- **A1 Web Attacker** (§4.1): can drive arbitrary browser requests / run own endpoints but cannot intercept others' messages or break crypto. **A1a** (§4.2) can act as a malicious AS and replay honest-AS messages. → motivates `iss` (RFC 9207) and PAR/PKCE binding.
- **A2 Network Attacker** (§4.3): controls the whole network (intercept/block/tamper) but not crypto without keys. → motivates mandatory TLS + sender-constrained tokens.
- **A3a Authorization Request Reader** (§4.4.1): reads authorization requests from browser→AS (mobile URL handlers, history, XSS, proxies). → motivates PAR (params off the front channel) + per-request PKCE bound to client/UA.
- **A5 Token Endpoint Tamperer** (§4.5.1): tampers when client is redirected to an attacker token endpoint — **stated NOT relevant in FAPI 2.0** because endpoints come from honest-AS metadata over a protected channel. → motivates metadata-only endpoint discovery.
- **A7 Resource Request Reader** (§4.6.1): reads requests to the RS (e.g., RS-side proxy logs). → motivates sender-constrained tokens so a leaked token is unusable by the reader.
- **Security goals**: Authorization (§2.1) "no attacker accesses resources other than their own" — anti-pattern: plain bearer tokens; symptom: token usable anywhere. Authentication (§2.2) "no attacker logs in as another user" — ID-token theft/replay. Session Integrity (§2.3) — defends forced-login-as-attacker and forced-access-to-attacker-resources (CSRF / session swap); anti-pattern: no CSRF protection on initiation.
- **Out of scope** (§5): TLS breakage, compromised device/browser, weak RNG, implementation bugs, phishing — these are explicitly NOT covered by the profile's guarantees.
