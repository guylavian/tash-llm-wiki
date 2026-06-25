---
title: PKCE (Proof Key for Code Exchange)
type: entity
domain: keycloak
slug: pkce
summary: "PKCE binds an authorization code to the browser session that requested it by requiring the client to prove knowledge of a per-request secret at the token endpoint, blocking code interception and injection attacks."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc7636 (RFC 7636, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 Security BCP, fetched 2026-06-17)
provenance_extracted: 22
provenance_inferred: 4
provenance_ambiguous: 0
tags: [clients, security, concept]
status: reviewed
updated: 2026-06-17
---

# PKCE (Proof Key for Code Exchange)

**A per-request cryptographic binding that prevents a stolen or injected authorization code from being redeemed by any party other than the client that initiated the flow.**

## Rule

### Scope of requirement

Public clients (SPAs, native/mobile apps) MUST use PKCE for every authorization code request (RFC 9700 §2.1.1; OAuth 2.1 §4.1.1). Confidential clients are RECOMMENDED to use it as well. Authorization servers MUST support PKCE and MUST enforce the verifier check when a challenge was presented. The only narrow exception in OAuth 2.1 is a confidential client talking directly to the token endpoint over an already-secure channel (OAuth 2.1 §7.5.1) — public clients have no exception.

### code_verifier generation

Generate `code_verifier` as a high-entropy random string, 43–128 characters from the unreserved character set `[A-Z][a-z][0-9]-._~` (RFC 7636 §4.1). The recommended construction is 32 random bytes from a CSPRNG, base64url-encoded (no padding) to produce 43 characters with ≥256 bits of entropy (RFC 7636 §7.1).

### Challenge method: always S256

`code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))` — base64url with no trailing `=` padding (RFC 7636 §4.2). If the client can perform SHA-256 it MUST use `S256` and MUST send `code_challenge_method=S256` explicitly — omitting the method parameter defaults to `plain` (RFC 7636 §4.3), which quietly breaks S256 clients. `plain` is allowed only when `S256` is genuinely impossible and the server is known to support it (RFC 7636 §4.2; RFC 9700 §2.1.1). Clients MUST NOT fall back to `plain` after an S256 failure — that fallback is a downgrade-attack vector (RFC 7636 §7.2).

### Authorization endpoint binding

The AS MUST store the `code_challenge` and `code_challenge_method` alongside the issued code (RFC 7636 §4.4) and MUST NOT expose the challenge value to other parties. If PKCE is required and no challenge arrives, or the method is unsupported, the AS MUST reject with `error=invalid_request` (RFC 7636 §4.4.1).

### Token endpoint verification

The client MUST include `code_verifier` in the token request whenever a challenge was used (RFC 7636 §4.5). The AS recomputes the challenge from the verifier and compares it to the stored value; a mismatch or a missing verifier MUST produce `error=invalid_grant` (RFC 7636 §4.6). Conversely, the AS MUST NOT accept a `code_verifier` on a token request if no challenge was stored in the corresponding code — this prevents a downgrade where an attacker strips the challenge from the authorization request (RFC 9700 §2.1.1).

### PKCE as CSRF defense (inferred)

PKCE also defends against login CSRF (RFC 9700 §2.1 / §4.7.1). A client MAY rely on PKCE for CSRF protection instead of `state`, but only after confirming that the AS actually enforces PKCE — without that confirmation, a separate `state` or OIDC `nonce` parameter is still required (inferred from the requirement that the defense must be verified, not assumed).

## Anti-pattern

| Anti-pattern | Where |
|---|---|
| Running authorization code flow with no `code_challenge` | SPA / native client |
| `code_challenge_method=plain` (or omitting the method while sending a plain verifier) | SPA client |
| Omitting `code_challenge_method` while sending an S256 hash | SPA client — AS treats it as `plain` and the comparison always fails |
| "Retry with plain on S256 failure" fallback | Client library or custom auth layer |
| Verifier derived from timestamp, `Math.random()`, GUID, or a static per-install constant | Client |
| Standard base64 instead of base64url; leaving `=` padding; hashing non-ASCII bytes | Client encoding layer |
| AS accepting a token request that carries `code_verifier` when no challenge was stored | AS configuration |
| AS configured with PKCE optional rather than required for public clients | Keycloak client config: "Proof Key for Code Exchange Code Challenge Method" left blank |

## Symptom

Concrete errors produced by each failure mode:

- **Missing challenge accepted** — stolen code is redeemed by attacker; pen-test flags "authorization code injection"; no runtime error, just a silent security failure.
- **S256 encoding errors** (wrong base64, padding, charset) — `error=invalid_grant` ("PKCE verification failed") on every token exchange, reproducible 100% of the time.
- **Method parameter omitted with S256 hash** — `error=invalid_grant`; AS compared the S256 hash literally to the verifier, which never matches.
- **plain method in use** — verifier leaks in request logs or Referrer headers; scanner flags "weak PKCE method"; or `error=invalid_request` ("plain not supported") if AS forbids it.
- **Low-entropy verifier** — codes get hijacked in the wild; server may reject with `invalid_request` for a verifier outside the 43–128 character range.
- **Downgrade fallback to plain** — MITM forces plain, harvests verifier from the intercepted request, and replays the stolen code; interception protection silently defeated.
- **Verifier sent without stored challenge** — no error on a vulnerable AS; the downgrade injection succeeds. Correct AS behavior: `invalid_grant`.

## Surface (client vs backend)

**Client (SPA / native app) — all of these are client responsibilities:**

1. Generate `code_verifier` with a CSPRNG (32 bytes minimum, base64url-encoded).
2. Compute `code_challenge = BASE64URL-NO-PAD(SHA256(ASCII(code_verifier)))`.
3. Send `code_challenge` and `code_challenge_method=S256` in the authorization request.
4. Store `code_verifier` in short-lived session state (not localStorage — see [[token-storage-browser]]).
5. Send `code_verifier` in the token request.
6. Never fall back to `plain` under any error condition.
7. Verify AS supports PKCE before relying on it as CSRF protection (inferred; otherwise also send [[state-and-nonce]]).

**Authorization server (backend — Keycloak/RHBK configuration):**

- Mark public clients as requiring PKCE; do not leave the challenge method optional.
- Store challenge + method with the issued code; never echo the challenge back.
- At the token endpoint: recompute, compare, and reject with `invalid_grant` on any mismatch.
- Reject token requests that carry a verifier when no challenge was stored (downgrade defense).
- Publish `code_challenge_methods_supported` in discovery metadata (RFC 9700 §2.1.1).

**Resource server:** no PKCE responsibility — PKCE is purely an authorization endpoint / token endpoint mechanism (inferred).

## See also

- [[oidc-grant-types]]
- [[oidc-endpoints]]
- [[state-and-nonce]]
- [[redirect-uri-validation]]
- [[token-storage-browser]]
- [[native-app-oauth]]
- [[refresh-token-rotation]]
- [[dpop-sender-constraining]]
- [[bff-token-handler]]
- [[oidc-client-best-practices]]
- [[fapi-oauth21-profiles]]
- [[fapi2-security-profile]]
- [[client-authentication-methods]]
- [[tokens-and-sessions]]
- [[issuer-identification-mixup]]
- [[cors-for-spa]]
- [[authorization-server-metadata-discovery]]
- [[sso-implementation-review]]
