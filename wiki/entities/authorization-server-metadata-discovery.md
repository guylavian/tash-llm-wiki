---
title: Authorization Server Metadata Discovery
type: entity
domain: keycloak
slug: authorization-server-metadata-discovery
summary: "The mechanism by which OAuth 2.0 / OIDC clients locate an authorization server's endpoints and capabilities via a well-known URL, with strict issuer validation required to prevent mix-up and impersonation attacks."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc8414 (RFC 8414 — OAuth 2.0 AS Metadata, fetched 2026-06-17)
  - web:https://openid.net/specs/openid-connect-discovery-1_0.html (OpenID Connect Discovery 1.0, fetched 2026-06-17)
provenance_extracted: 28
provenance_inferred: 4
provenance_ambiguous: 0
tags: [security, clients, endpoint]
status: reviewed
updated: 2026-06-17
---

# Authorization Server Metadata Discovery

**A standardized self-description document published at a well-known HTTPS URL that lets clients bootstrap all endpoint and capability information without hardcoding it.**

## Rule

### Well-known URL construction

RFC 8414 (§3) and OIDC Discovery (§4/§4.1) define two slightly different conventions that clients must handle:

- **RFC 8414 (OAuth 2.0 / pure OAuth clients):** Insert `/.well-known/oauth-authorization-server` *between* the issuer host and its path. Issuer `https://as.example.com` → `https://as.example.com/.well-known/oauth-authorization-server`. Issuer `https://as.example.com/issuer1` → `https://as.example.com/.well-known/oauth-authorization-server/issuer1`.
- **OIDC Discovery:** Append `/.well-known/openid-configuration` *after* the issuer path. Issuer `https://as.example.com/realms/foo` → `https://as.example.com/realms/foo/.well-known/openid-configuration`. Strip any trailing slash before appending.

These are structurally different constructions (inferred); a client that treats them as equivalent will build the wrong URL when the issuer has a path component.

### Required metadata fields

RFC 8414 (§2) mandates `issuer` (HTTPS, no query/fragment) and `response_types_supported`; `authorization_endpoint` and `token_endpoint` are required unless the grant type mix renders them unnecessary. OIDC Discovery (§3) adds `jwks_uri`, `subject_types_supported`, and `id_token_signing_alg_values_supported` as required fields; `token_endpoint` is required except in implicit-only deployments, `RS256` must appear in the signing-alg list, and `openid` must appear in `scopes_supported`.

### Issuer exact-match validation

RFC 8414 (§3.3, §6.2) and OIDC Discovery (§4.3, §7.2) both require the `issuer` value in the returned document to be byte-for-byte identical to the issuer URL used to construct the discovery request. Any mismatch — trailing slash, scheme case, proxy-rewritten hostname — means the document MUST NOT be used. In OIDC the `issuer` must also match the `iss` claim in every issued ID Token.

### jwks_uri and key refresh

The `jwks_uri` REQUIRED field (OIDC Discovery §3) is an HTTPS URL pointing to the AS's public JWK Set. Clients must fetch and refresh from this URI at runtime, honoring the `kid` header in tokens, rather than caching keys at deploy time. This is the only safe path through AS key rotations (inferred).

### HTTP method and response format

Metadata is fetched with HTTP GET. A successful response is `200 OK` with `Content-Type: application/json`. Unknown extra fields must be tolerated. Empty arrays must be omitted rather than sent as `[]`. CORS should be supported so that browser-based relying parties can fetch the document directly (OIDC Discovery §4).

### Signed metadata (RFC 8414 §2.1)

The AS may include a `signed_metadata` member — a JWS-signed JWT. When present and supported by the client, its values override the corresponding plain-JSON fields. The `signed_metadata` key must not appear as a claim inside the JWT itself.

### TLS requirements

Both specs (RFC 8414 §6.1; OIDC Discovery §4.1, §7.1) require the metadata endpoint and every endpoint URL it advertises to use HTTPS. Clients must validate server certificates per RFC 6125 and support TLS 1.2+ with an integrity/confidentiality-providing cipher suite. BCP 195 applies.

### Issuer as AS mix-up defense (RFC 8414 §2)

The issuer identifier is the binding anchor for multi-AS deployments. Each discovered document must be tied back to its issuer at every subsequent step — token redemption, token validation, and resource-server association — to prevent authorization-server mix-up attacks.

## Anti-pattern

1. **Wrong URL construction:** Appending `/.well-known/oauth-authorization-server` to the end of a path-bearing issuer (RFC 8414 anti-pattern), or hardcoding `https://host/.well-known/openid-configuration` and ignoring a realm path like `/realms/foo` (OIDC anti-pattern).
2. **Skipping issuer validation:** Accepting a metadata document without verifying its `issuer` field byte-for-byte against the requested issuer. Trailing-slash and scheme-case drifts are the most common silent failures.
3. **Hardcoding endpoints or keys:** Configuring `token_endpoint`, `authorization_endpoint`, or JWK material at deploy time instead of reading them from discovery. This breaks silently after any AS reconfiguration or key rotation.
4. **Disabling TLS verification:** Using `--insecure` / `verify=false` to work around cert errors during development, then deploying without fixing the root cause.
5. **Omitting required fields:** Emitting a partial metadata document (missing `jwks_uri`, `subject_types_supported`, or RS256 in the alg list); or emitting `[]` for unsupported optional fields instead of omitting the key entirely.
6. **Ignoring `signed_metadata`:** Reading plain-JSON values when a `signed_metadata` JWT is present and the client claims to support it.
7. **Unpaired resource–AS association:** Pairing a protected resource with an AS without an independent trust anchor — discovery alone does not establish that pairing (RFC 8414 §6.3, §6.4).

## Symptom

- **404 / "discovery failed"** — wrong well-known URL path; client falls back to hardcoded endpoints and silently bypasses discovery.
- **`Failed to load OpenID provider metadata` / `unable to resolve well-known endpoint`** — issuer path ignored or double-slash introduced.
- **`Invalid issuer` / `iss claim mismatch` / `Token issuer does not match expected issuer`** — issuer value in metadata or ID Token does not byte-match the configured issuer.
- **Authorization-server mix-up / confused deputy** — code or token redeemed at the wrong AS; accepted tokens minted by an unintended issuer.
- **`Unable to find a signing key` / `kid not found` / intermittent `invalid_signature`** — keys were hardcoded rather than fetched from `jwks_uri`; post-rotation the cached key is stale.
- **`No 'Access-Control-Allow-Origin'` on discovery fetch** — metadata endpoint missing CORS header; SPA client cannot fetch it in-browser.
- **`Unexpected token < in JSON` / parse failures** — server returned HTML or wrong content type (e.g., an error page or auth-redirect).
- **PKCE silently skipped** — `code_challenge_methods_supported` absent from metadata; client does not enable PKCE even though the AS supports it (inferred).
- **MITM / token interception** — TLS not enforced on metadata or advertised endpoint URLs; attacker-controlled endpoints substituted.
- **Attacker-tampered endpoints used** — client reads plain-JSON values while a `signed_metadata` JWT is present; unsigned values override the signed ones.

## Surface (client vs backend)

**Browser / SPA client:**
- Fetch the discovery document at startup via GET, with CORS support required.
- Validate `issuer` byte-for-byte before reading any other field.
- Drive all endpoint URLs (`authorization_endpoint`, `token_endpoint`, `end_session_endpoint`) from the discovery document — never hardcode them.
- Respect `code_challenge_methods_supported` to determine PKCE support.

**Backend (confidential client, resource server, BFF, service-to-service):**
- On startup (or lazily with a circuit-breaker), fetch and cache the metadata document.
- Enforce `issuer` validation; reject any document with a mismatched `issuer`.
- Fetch the JWK Set from `jwks_uri` and refresh on `kid` miss rather than at a fixed interval.
- In multi-AS environments, maintain a per-issuer metadata cache and bind every inbound token to the correct issuer before validating.
- Never disable TLS verification, even in staging. Fix the cert instead (inferred).
- When `signed_metadata` is present and the client supports it, verify the JWT signature and use its claims in preference to the unsigned values.

## See also

- [[oidc-endpoints]]
- [[oidc-token-validation]]
- [[oidc-grant-types]]
- [[pkce]]
- [[issuer-identification-mixup]]
- [[jwt-validation-pitfalls]]
- [[redirect-uri-validation]]
- [[state-and-nonce]]
- [[oidc-client-best-practices]]
- [[client-authentication-methods]]
- [[client-libraries-by-stack]]
- [[dpop]]
- [[fapi-oauth21-profiles]]
- [[fapi2-security-profile]]
- [[oidc-logout]]
- [[rp-initiated-logout]]
- [[back-channel-logout]]
- [[token-storage-browser]]
- [[bff-token-handler]]
- [[refresh-token-rotation]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[dpop-sender-constraining]]
- [[mtls-bound-tokens]]
- [[cors-for-spa]]
- [[service-to-service-client-credentials]]
- [[token-revocation]]
- [[token-introspection]]
- [[native-app-oauth]]
- [[bearer-token-usage]]
- [[tokens-and-sessions]]
- [[token-exchange]]
- [[securing-apps-oidc-saml]]
- [[sso-implementation-review]]
