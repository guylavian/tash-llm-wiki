---
title: DPoP Sender-Constraining
type: entity
domain: keycloak
slug: dpop-sender-constraining
summary: "DPoP (Demonstrating Proof of Possession, RFC 9449) sender-constrains access and refresh tokens by binding them to a client-held asymmetric key pair, so a stolen token alone cannot be replayed without the matching private key."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9449 (RFC 9449 — DPoP, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 — OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
provenance_extracted: 28
provenance_inferred: 4
provenance_ambiguous: 0
tags: [tokens, security, concept]
status: reviewed
updated: 2026-06-17
---

# DPoP Sender-Constraining

**A mechanism defined in RFC 9449 that binds an OAuth access (or refresh) token to a client's public key by requiring the client to sign a proof JWT on every token request and resource call, rendering a stolen token useless without the private key.**

## Rule

### Proof JWT structure (RFC 9449 §4.2)

The client generates a DPoP proof JWT for every request. The JOSE header MUST set `typ` to `dpop+jwt`, `alg` to a registered asymmetric algorithm (never `none`, never HMAC), and `jwk` to the public key (private key MUST NOT appear in `jwk`). Required payload claims: `jti` (unique, unguessable per-request ID), `htm` (HTTP method), `htu` (target URI without query string or fragment), and `iat` (creation time). When presenting a token to a resource server the proof MUST also include `ath` = base64url(SHA-256(access token ASCII value)). When the server has issued a nonce, the `nonce` claim MUST be present (§7, §8).

### AS token binding (RFC 9449 §5, §6.1)

At the token endpoint the authorization server MUST associate the issued token with the public key from the proof and MUST return `token_type: DPoP`. For JWT access tokens the binding travels as `cnf.jkt`, the base64url JWK SHA-256 thumbprint of the proof key (§6.1). The Security BCP (RFC 9700 §2.2.1, §4.10.1) requires ASes and RSes to SHOULD sender-constrain tokens via DPoP or mTLS; DPoP is the mechanism that works for public clients (SPAs, native apps) without requiring client certificates.

### RS validation (RFC 9449 §4.3, §7.1)

The resource server MUST verify: exactly one `DPoP` header present; proof is a well-formed JWT; all required claims present; `typ=dpop+jwt`; asymmetric non-`none` algorithm; signature verifies against the embedded `jwk`; `jwk` contains no private key; `htm`/`htu` match the actual request; `nonce` matches if one was issued; `iat` falls within an acceptable clock window; `ath` equals the SHA-256 of the presented token value; and the token's `cnf.jkt` thumbprint equals the proof's `jwk` thumbprint (§4.3 item 12). Critically, the RS MUST require a `DPoP` header for any DPoP-bound token and MUST NOT grant access if any check fails (§7.1).

### Bearer-scheme downgrade rejection (RFC 9449 §7.2)

A DPoP-bound access token presented using the `Authorization: Bearer` scheme MUST be rejected. The binding is scheme-specific; accepting the token under Bearer silently removes the sender-constraint.

### Nonce mechanism (RFC 9449 §8, §9)

The AS MAY require a server nonce to shorten the proof pre-generation window. If a nonce is missing, the AS returns HTTP 400 with `error=use_dpop_nonce` and a `DPoP-Nonce` response header. The RS signals the same requirement via HTTP 401 with `WWW-Authenticate: DPoP` plus `DPoP-Nonce`. Nonce values MUST be unpredictable. Once a nonce has been issued the server MUST NOT accept proofs without it — no nonce-downgrade (§11.3).

### Replay protection (RFC 9449 §11.1, §11.3)

Servers MUST enforce a short `iat` acceptance window (seconds to a few minutes). Servers SHOULD track `jti` values (or their hashes) to enforce one-time use. Without server nonces, pre-generated proofs become a risk, so deployments that skip nonces SHOULD NOT issue long-lived DPoP-bound access tokens (§11.2).

### Refresh-token scope (RFC 9700 §2.2.2, §4.14; OAuth 2.1 §1.4.3)

For public clients, refresh tokens MUST be sender-constrained OR use single-use rotation. DPoP sender-constraining is one accepted path to satisfy this MUST (inferred). Rotation is the common alternative when DPoP is not deployed.

## Anti-pattern

1. **Wrong `typ` or symmetric `alg`** — emitting `typ:JWT` instead of `dpop+jwt`, or accepting `alg:none` / `alg:HS256`. Makes proofs forgeable and triggers key-confusion.
2. **Reusing or sequential `jti`** — reusing a `jti` value across requests breaks replay detection.
3. **`htu` with query string attached** — the URI bound in `htu` MUST exclude query and fragment; attaching them causes valid proofs to fail `htu` comparison.
4. **Dropping `ath` on resource calls** — omitting the access-token hash means one proof is reusable with arbitrary tokens (token-substitution attack).
5. **Validating the proof signature but skipping the `jkt` == thumbprint(`jwk`) check** — the RS confirms the proof was signed but never checks that it matches the key bound in the token; a proof from key A is accepted with a token bound to key B.
6. **Accepting a DPoP-bound token without an accompanying proof** — allows stolen tokens to be replayed as bearer tokens.
7. **Falling back to Bearer validation for a DPoP token** — an RS that accepts `Authorization: Bearer <dpop-token>` strips the binding silently.
8. **Predictable or static server nonces** — nonces MUST be unpredictable; static nonces provide no window control.
9. **Storing the DPoP private key alongside the token** (RFC 9700 §4.10.1) — if both are captured together, sender-constraining is defeated; the key should be non-exportable where the platform allows.
10. **Long token lifetimes without server nonces** — expands the window in which a pre-generated proof can be misused (§11.2).

## Symptom

Concrete observable failures from the wrong implementations above:

- RS returns `invalid_dpop_proof` — proof structure violation: wrong `typ`, bad `alg`, missing required claim, `htu` mismatch, wrong or missing `ath`, `nonce` mismatch, or signature failure.
- RS returns `invalid_token` — token/binding mismatch: `cnf.jkt` does not match proof `jwk` thumbprint.
- RS returns `use_dpop_nonce` (HTTP 400 or 401) — nonce required but absent; client must retry with the `DPoP-Nonce` value echoed from the response.
- Infinite 400/401 loop labeled `use_dpop_nonce` in client logs — client not implementing nonce retry.
- Stolen token accepted without a DPoP header — bearer-scheme fallback not blocked; "DPoP binding defeated" pen-test finding.
- Proof from key A accepted with token bound to key B — `jkt` vs `jwk` thumbprint check absent; pen-test / audit finding "sender-constraining bypassed".
- Duplicate request abuse within a replay window — no `jti` cache, no nonce; captured proof replayable until `iat` window closes.
- Security review flags `alg:none` in DPoP validation — CVE-class finding if `none` or HMAC allowed in the server's algorithm allowlist.

## Surface (client vs backend)

### Client (SPA / native app / confidential client)

- Generate a fresh asymmetric key pair on startup (non-exportable if the platform supports it).
- Produce a new DPoP proof JWT per request: unique `jti`, correct `htm`/`htu`, `ath` on resource calls, `nonce` when required.
- On receiving `use_dpop_nonce` (400 or 401), extract the `DPoP-Nonce` value from the response header and retry the request with a new proof containing that `nonce`. (inferred)
- Never reuse a proof across requests or different tokens.
- Use `Authorization: DPoP <token>`, not `Authorization: Bearer <token>`.

### Backend — Authorization Server

- Validate the incoming DPoP proof per §4.3 on the token endpoint.
- Bind issued tokens to the proof's public key (`cnf.jkt` in JWT access tokens; `token_type: DPoP`).
- Optionally enforce server nonces via `DPoP-Nonce` to tighten the replay window.
- Never issue a `Bearer` token when a valid DPoP proof was presented.

### Backend — Resource Server

- Require a `DPoP` header for all DPoP-bound tokens.
- Perform the full §4.3 validation checklist, including `ath` recomputation and `jkt` == thumbprint(`jwk`) cross-check.
- Reject DPoP-bound tokens presented under the `Bearer` scheme.
- Issue `WWW-Authenticate: DPoP` challenges with the correct `error` code and, where applicable, advertise acceptable algorithms via `algs`.
- Maintain a short-lived `jti` cache (or equivalent) for within-window replay detection. (inferred)

### Scope limitation (both sides)

DPoP binds only HTTP method and URI — request body integrity depends on TLS (§11.7). DPoP cannot protect against an attacker who can run code inside the client's process and mint proofs in real time (§11.4). For highest-assurance flows (FAPI 2.0) see [[fapi2-security-profile]] and [[mtls-bound-tokens]] as alternatives or complements.

## See also

- [[dpop]]
- [[mtls-bound-tokens]]
- [[bearer-token-usage]]
- [[oidc-client-best-practices]]
- [[fapi-oauth21-profiles]]
- [[fapi2-security-profile]]
- [[oidc-token-validation]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[refresh-token-rotation]]
- [[token-storage-browser]]
- [[bff-token-handler]]
- [[client-authentication-methods]]
- [[tokens-and-sessions]]
- [[jwt-validation-pitfalls]]
- [[token-revocation]]
- [[token-introspection]]
- [[service-to-service-client-credentials]]
- [[securing-apps-oidc-saml]]
- [[sso-implementation-review]]
