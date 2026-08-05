---
source: OpenID Connect Discovery 1.0
url: https://openid.net/specs/openid-connect-discovery-1_0.html
fetched: 2026-06-17
status: OIDF final
feeds: [authorization-server-metadata-discovery]
---

# OpenID Connect Discovery 1.0 — raw staging note

Load-bearing normative requirements distilled for the `authorization-server-metadata-discovery` concept. Each bullet: RULE (+ section), ANTI-PATTERN, SYMPTOM.

## authorization-server-metadata-discovery

### Well-known endpoint construction (§4 / §4.1)
- RULE: Config doc lives at `<issuer>/.well-known/openid-configuration`; if issuer has a path component, strip trailing `/` before appending (§4, §4.1). Request MUST use GET over HTTPS.
  - ANTI-PATTERN: Hardcoding `https://host/.well-known/openid-configuration` and ignoring the issuer path (e.g. realm path `/realms/foo`), or double-slashing when issuer ends in `/`.
  - SYMPTOM: 404 on discovery; `Failed to load OpenID provider metadata` / `unable to resolve well-known endpoint`; client points at wrong realm.

### Issuer exact-match validation (§4.3, §7.2)
- RULE: The `issuer` value in the returned metadata MUST be byte-for-byte identical to the issuer used to build the discovery URL, and MUST equal the `iss` claim in ID Tokens (§4.3).
  - ANTI-PATTERN: Accepting metadata whose `issuer` differs (trailing slash, http vs https, host case, proxy-rewritten hostname) from the configured/expected issuer; trusting endpoints from a mismatched document.
  - SYMPTOM: Mix-up / impersonation risk; runtime `Invalid issuer` / `iss claim mismatch` / `Token issuer does not match expected issuer`; tokens rejected at validation.

### Required metadata fields (§3)
- RULE: Response MUST include `issuer`, `authorization_endpoint`, `jwks_uri`, `response_types_supported`, `subject_types_supported`, `id_token_signing_alg_values_supported` (§3). `token_endpoint` REQUIRED unless only implicit flow. RS256 MUST appear in the signing-alg list; `openid` MUST be in `scopes_supported`; `none` alg only allowed when no ID Token is returned from the authz endpoint.
  - ANTI-PATTERN: Emitting a partial doc (missing `jwks_uri` or `subject_types_supported`), or omitting RS256 / advertising `none` broadly.
  - SYMPTOM: Client init fails — `missing required metadata`, `jwks_uri is required`, `no supported signing algorithm`; downstream signature verification breaks.

### jwks_uri & key discovery (§3)
- RULE: `jwks_uri` (REQUIRED) is the HTTPS URL of the OP JWK Set used to validate token signatures (§3).
  - ANTI-PATTERN: Hardcoding key material instead of fetching/refreshing from `jwks_uri`; not honoring `kid`.
  - SYMPTOM: After key rotation, `Unable to find a signing key` / `kid not found`; intermittent `invalid signature` post-rotation.

### Transport security — HTTPS everywhere (§4.1, §4.2, §7.1)
- RULE: Discovery request MUST be HTTPS with RFC 6125 cert validation; every endpoint advertised in the metadata (`authorization_endpoint`, `token_endpoint`, `userinfo_endpoint`, `jwks_uri`, `registration_endpoint`) MUST use the `https` scheme; follow BCP 195 (§4.1, §4.2, §7.1).
  - ANTI-PATTERN: Disabling TLS verification ("insecure"/`verify=false`) to get discovery working; allowing http endpoints behind a reverse proxy.
  - SYMPTOM: MITM / token interception exposure; `SSL handshake failed` / `unable to find valid certification path`; mixed-scheme `https required` errors.

### Response format (§3, §4.2)
- RULE: Success is HTTP 200 with `Content-Type: application/json`; multi-valued claims are JSON arrays; empty-array claims MUST be omitted (§3, §4.2). CORS SHOULD be supported for browser RPs (§4).
  - ANTI-PATTERN: Returning HTML/error page, wrong content-type, or `[]` placeholders for unsupported features; no CORS header for SPA clients.
  - SYMPTOM: `Unexpected token < in JSON` / parse failures; SPA discovery blocked by CORS (`No 'Access-Control-Allow-Origin'`).

### WebFinger issuer location (§2, §7.1)
- RULE: When deriving the OP from a user identifier, RP uses WebFinger with rel `http://openid.net/specs/connect/1.0/issuer` over TLS; the returned issuer `href` MUST be an `https` URI with host, no query/fragment (§2, §7.1).
  - ANTI-PATTERN: Trusting an unauthenticated/non-TLS WebFinger response, or accepting an issuer href with a query/fragment.
  - SYMPTOM: Issuer spoofing via WebFinger; malformed-issuer errors downstream when building the discovery URL.
