---
title: mTLS Certificate-Bound Access Tokens
type: entity
domain: keycloak
slug: mtls-bound-tokens
summary: "mTLS certificate binding sender-constrains OAuth2 access (and optionally refresh) tokens to the client's TLS certificate thumbprint, making a stolen token useless without the matching private key. RFC 8705 defines the mechanism; FAPI 2.0 mandates it (alongside DPoP) for all access tokens."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc8705 (RFC 8705, fetched 2026-06-17)
  - web:https://openid.net/specs/fapi-security-profile-2_0-final.html (FAPI 2.0 Security Profile, fetched 2026-06-17)
provenance:
  extracted: 28
  inferred: 5
  ambiguous: 0
tags: [tokens, security, concept]
status: reviewed
updated: 2026-06-17
---

# mTLS Certificate-Bound Access Tokens

**RFC 8705 mechanism that binds an OAuth2 access token to the SHA-256 thumbprint of the client's TLS certificate, so the token is only usable by the holder of the matching private key.**

## Rule

### Two independent features in RFC 8705

RFC 8705 (§1) separates two orthogonal capabilities: (1) **mTLS client authentication** at the token endpoint (`tls_client_auth` PKI mode or `self_signed_tls_client_auth`), and (2) **certificate-bound token issuance**. These are independent — a public client that does not use mTLS client-auth can still receive a cert-bound token (§3, §1).

### Client authentication methods

**PKI mode (`tls_client_auth`):** the AS validates the cert chain to a trusted CA, then matches exactly one registered subject attribute — `tls_client_auth_subject_dn` or one SAN variant (`_san_dns`, `_san_uri`, `_san_ip`, `_san_email`). Only one such field may be registered per client (§2.1, §2.1.2). Every mTLS-authenticated request must include `client_id`; failed cert auth returns `invalid_client` (§2, §2.3).

**Self-signed mode (`self_signed_tls_client_auth`):** the AS does NOT validate the chain. It matches the presented cert against the client's registered certs in `jwks`/`jwks_uri` (via JWK `x5c`) and confirms private-key possession via the TLS handshake (§2.2, §2.2.2). The cert need not come from a trusted CA.

### Certificate binding

The binding is carried in the access token's `cnf` claim as member `x5t#S256` = base64url(SHA-256(DER-encoded cert)), with trailing `=` padding omitted (§3.1; RFC 4648 §5). For JWT introspection responses the same `cnf` object appears at the top level (§3.2, §9.1).

The AS MUST only bind a token to a cert whose private-key possession the client proved in the TLS handshake (§6.1). Binding applies to authorization_code and refresh_token flows; the implicit grant is explicitly out of scope (§6.4).

Clients MUST use the `mtls_endpoint_aliases` URL when the AS publishes one; hitting the conventional token endpoint may result in a silently unbound token (§3.4, §5).

**Cert rotation:** a cert-bound token becomes invalid when the client rotates its cert — treat it like expiry and obtain a fresh token via refresh (§6.3).

**Refresh tokens:** for public clients the AS SHOULD bind the refresh token to the cert and re-validate on each use (§7.1, §4). For confidential `tls_client_auth`/`self_signed` clients the binding is implicit via the authentication requirement.

### Resource server validation

The RS MUST obtain the client cert from the mutually authenticated TLS layer, compute SHA-256 of the DER encoding, and require an exact match against `cnf.x5t#S256`; on mismatch respond HTTP 401 `invalid_token` (§3.4, §3.2). The RS MUST NOT validate the cert's trust chain — an expired or self-signed cert is acceptable as long as the thumbprint matches (§6.2). This is a proof-of-possession check, not a PKI check (inferred).

### FAPI 2.0 mandate

FAPI 2.0 (§5.3.2.1 AS / §5.3.3.1 client / §5.3.4 RS) requires that all access tokens be sender-constrained using either mTLS (RFC 8705) or DPoP (RFC 9449). Plain bearer access tokens do not satisfy the profile. Tokens must be presented only in HTTP headers (RFC 6750 §2.1 bearer header or DPoP RFC 9449 §7.1) — never in query parameters (§5.3.4 RS).

FAPI 2.0 also requires mTLS client auth or `private_key_jwt` as the only allowed client authentication methods; `client_secret_*` methods are not permitted (§5.3.2.1).

### Metadata and registration

AS capability is advertised via `tls_client_certificate_bound_access_tokens: true` in its metadata (§3.3, §9.3). Clients must also set this flag in their registration to opt in (§3.4). `mtls_endpoint_aliases` in AS metadata provides the mTLS-specific endpoint URLs so conventional clients are not prompted for client certs (§5).

### TLS termination

TLS may terminate at a reverse proxy. Securely conveying the client cert (or its thumbprint) from the proxy to the app server is out of scope in RFC 8705 (§6.5), but getting it wrong makes the PoP check unverifiable. Prefer TLS 1.3 — pre-1.3 sends the client cert in cleartext, enabling third-party correlation (§7.5, §8). Use a vetted X.509 library; do not hand-roll cert parsing (§7.3).

**PKI spoofing:** in `tls_client_auth` mode, a cert with the same subject DN/SAN issued by a different trusted CA can impersonate the client. The AS SHOULD restrict its truststore to an agreed anchor CA rather than trusting the OS/default bundle (§7.4) (inferred: this is a deployment policy decision not always surfaced in client documentation).

## Anti-pattern

1. Treating `cnf.x5t#S256` tokens as plain bearer tokens — skipping the thumbprint check at the RS entirely.
2. Hashing the PEM/base64 text or the public key (SPKI) instead of the raw DER-encoded full certificate, or leaving `=` padding, or using SHA-1 `x5t` instead of `x5t#S256`.
3. Hitting the plain token endpoint instead of `mtls_endpoint_aliases` when the AS publishes one, resulting in a silently unbound token.
4. Assuming cert binding requires `tls_client_auth` — public clients can also receive cert-bound tokens (inferred: commonly misunderstood).
5. Trusting an unauthenticated client-cert header (e.g. `X-SSL-Client-Cert`) injected past a reverse proxy — allows header spoofing to bypass PoP.
6. Registering multiple subject matchers for `tls_client_auth` or matching on a partial/normalized DN.
7. Running full PKIX validation (chain, expiry) at the RS during the PoP check — valid thumbprint matches after cert expiry are rejected unnecessarily.
8. Issuing long-lived cert-bound tokens with no refresh-on-rotation path.
9. Trusting the OS/default CA bundle as the truststore for PKI-mode mTLS client auth.

## Symptom

- `invalid_token` (HTTP 401) from the RS: cert thumbprint never matches — usually caused by hashing PEM text instead of DER bytes, or the client cert not reaching the RS through TLS termination.
- Token silently issued with no `cnf` claim: client hit the plain token endpoint instead of `mtls_endpoint_aliases`, or neither AS nor client had `tls_client_certificate_bound_access_tokens: true`.
- `invalid_client` at the token endpoint: `client_id` omitted, DN-normalization mismatch across vendors, or multiple subject matchers registered.
- `invalid_token` storm after cert rotation: long-lived bound tokens that outlive the cert with no refresh-on-rotation logic.
- Token replayable from any host with no cert: RS is accepting the token as a plain bearer token, ignoring the `cnf` binding — sender-constraining bypassed.
- `invalid_grant` on refresh after cert rotation: public client refresh token was not bound, or was bound to the old cert.
- Valid bound requests rejected after cert expiry: RS performing full PKIX validation instead of pure thumbprint match.
- Browser cert-selection prompts for non-mTLS clients: conventional clients hitting an mTLS-only endpoint because `mtls_endpoint_aliases` is being ignored.
- FAPI conformance failure "token not sender-constrained": plain bearer token issued, no `cnf` claim.

## Surface (client vs backend)

**Confidential client / backend (BFF, service-to-service):**
- Holds the TLS client certificate and its private key.
- Must use the `mtls_endpoint_aliases` token endpoint URL when the AS publishes one.
- Must include `client_id` on every mTLS-authenticated request.
- Must present the client cert on every call to the resource server so the RS can extract and match the thumbprint.
- Must refresh the access token when the cert is rotated (treating rotation as expiry).
- Should register `tls_client_certificate_bound_access_tokens: true` in dynamic registration.
- Should use `tls_client_auth` or `self_signed_tls_client_auth` as `token_endpoint_auth_method` when applicable.

**Resource server (backend):**
- Must extract the client cert from the mutually authenticated TLS layer.
- Must compute SHA-256 of the DER-encoded cert and compare it exactly to `cnf.x5t#S256` in the access token.
- Must NOT validate the cert's trust chain during the PoP check.
- Must reject mismatches with HTTP 401 `invalid_token`.
- Must never accept a cert-bound token as a plain bearer token.
- Must not trust spoofable proxy headers for the client cert without authentication of the header source (inferred).

**SPA / browser client:**
mTLS client-cert flows are not practical in browsers — browser cert selection is user-visible and cert management is uncontrollable. Use DPoP (see [[dpop-sender-constraining]]) for browser-side sender-constraining. FAPI 2.0 allows DPoP as the alternative to mTLS for this reason (inferred).

## See also

- [[dpop-sender-constraining]] — DPoP is the browser-viable alternative to mTLS binding; FAPI 2.0 mandates one or the other
- [[fapi2-security-profile]] — mandates sender-constrained tokens; restricts client auth to mTLS or `private_key_jwt`
- [[client-authentication-methods]] — covers `tls_client_auth` and `self_signed_tls_client_auth` in the RHBK context
- [[access-token-validation-resource-server]] — RS-side validation flow where the thumbprint check fits
- [[tokens-and-sessions]] — token lifecycle; cert rotation interacts with token expiry
- [[service-to-service-client-credentials]] — primary flow for mTLS-authenticated confidential clients
- [[bff-token-handler]] — BFF pattern that holds the cert and shields SPAs from mTLS complexity
- [[token-introspection]] — introspection responses carry `cnf` at the top level for bound tokens
- [[token-revocation]] — revocation is listed as one of the `mtls_endpoint_aliases` endpoints
- [[jwt-validation-pitfalls]] — DER-vs-PEM hashing mistake sits in the same class of JWT/crypto pitfalls
- [[bearer-token-usage]] — contrast with plain bearer usage; FAPI 2.0 disallows query-param token passing
- [[oidc-token-validation]] — broader token validation context
- [[securing-apps-oidc-saml]] — RHBK-specific client securing guide
- [[sso-implementation-review]] — MOC
