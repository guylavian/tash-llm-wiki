---
title: JWT Validation Pitfalls
type: topic
domain: keycloak
slug: jwt-validation-pitfalls
summary: "A catalogue of the ways JWT validation goes wrong — algorithm confusion, skipped signature checks, header-injection, and cross-token misuse — so reviewers can predict the faults a broken implementation will produce."
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth 2.0 Access Tokens, fetched 2026-06-17)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (OWASP Cheat Sheets — Authentication/Session/JWT, fetched 2026-06-18)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://owasp.org/www-project-web-security-testing-guide/ (OWASP WSTG, fetched 2026-06-18)
provenance_extracted: 28
provenance_inferred: 5
provenance_ambiguous: 0
tags: [tokens, security, anti-pattern]
symptoms:
  - "alg:none"
  - "invalid_token"
status: reviewed
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# JWT Validation Pitfalls

**The set of implementation mistakes that cause a resource server or OIDC client to accept a forged, expired, mistyped, or replayed JWT when it should reject it.**

---

## Rule

What correct JWT validation looks like. Each sub-rule cites its normative home.

### 1. Pin the algorithm; never trust the `alg` header

The verifier must be configured with the expected algorithm and must reject tokens that claim a different one (RFC 9068 §2.1; WSTG-SESS-10). `alg: none` (and case variants like `NoNe`) must always be rejected. For RSA/EC tokens, the verifier must not accept `HS256` — an attacker who knows your public key (published at `/.well-known/jwks.json`) can forge an `HS256` token by re-signing with that key as the HMAC secret.

### 2. Verify the signature — do not merely decode

`jwt.verify()` and `jwt.decode()` are different operations (WSTG-SESS-10). Only the former checks the signature. Any path that returns claims without cryptographic verification must be treated as untrusted.

### 3. Reject `typ` that does not match the expected token class (RFC 9068 §4)

JWT access tokens per RFC 9068 carry `typ: at+jwt`. Resource servers must reject tokens that carry `typ: JWT`, no `typ`, or any other value — an ID Token and an access token from the same AS are both signed JWTs, but only one is the right class for a protected endpoint.

### 4. Validate all required claims: `iss`, `aud`, `exp`, `sub`, `client_id`, `iat`, `jti` (RFC 9068 §2.2, §4)

- `iss` must exactly match the trusted AS issuer string (no prefix/substring matching).
- `aud` must contain a resource indicator identifying this specific resource server — not just any audience from the same issuer (RFC 9068 §4; RFC 9700 §4.10.2).
- `exp` must be in the future; allow only minimal clock-skew leeway (a few minutes maximum — RFC 9068 §4).
- For client-credentials grants, `sub` identifies the client application, not an end user (RFC 9068 §2.2).

### 5. Never trust header fields to locate the signing key

The `kid` header must be resolved against a server-controlled JWKS, not a filesystem path, SQL query, or any attacker-influenced lookup (WSTG-SESS-10). The `jwk` header field (an embedded key) must be ignored entirely — accepting it lets the attacker supply and verify their own key.

### 6. Prevent cross-JWT confusion with distinct `aud` per resource (RFC 9068 §5; RFC 8725 §2.8)

Even if `typ` is checked, a shared audience across multiple APIs means a token for API-A can be replayed at API-B. Each resource server must have its own audience identifier (inferred from RFC 9068 §5 + RFC 8725 §2.8 together).

### 7. Use strong signing keys

HMAC-signed tokens require a high-entropy secret from a CSPRNG — not a short password or default value (WSTG-SESS-10; OWASP JWT Cheat Sheet). Weak secrets are offline-crackable.

### 8. Do not rely on key separation as a security boundary (RFC 9068 §5)

Assuming "ID Tokens use a different key than access tokens, so they can't be confused" is wrong: the resource server must accept any key published in the AS's OIDC discovery metadata. A single compromised or leaked published key allows access-token forgery.

### 9. Return `invalid_token` on every validation failure (RFC 9068 §4 / RFC 6750 §3.1)

The `WWW-Authenticate: Bearer error="invalid_token"` response tells clients the token is the problem and they should refresh. Generic 500s or empty 200s obscure the root cause.

### 10. Pair `exp` with revocation for stolen-token scenarios (OWASP JWT Cheat Sheet)

`exp` alone cannot invalidate a token before its natural expiry. A server-side denylist (keyed on `jti` or a SHA-256 digest) is needed for logout and credential-theft response. Without it, a user "logout" only drops the client copy while the token remains valid (inferred from OWASP JWT Cheat Sheet + RFC 9068 §2.2).

---

## Anti-pattern

The most common wrong implementations, grouped by failure class:

| Failure class | Common mistake |
|---|---|
| **Algorithm confusion** | Permissive `verify()` honors the token's own `alg` header, accepting `none`, downgraded HMAC, or RS256→HS256 substitution |
| **Signature skip** | Calling decode instead of verify; trusting a decoded payload without checking the signature |
| **Missing `typ` check** | Accepting any signed JWT from the trusted AS, including ID Tokens, as a valid access token |
| **Loose `iss`/`aud`** | Prefix/substring matching on `iss`; no `aud` check at all; shared audience across all APIs |
| **Wide `exp` leeway** | Disabling or greatly expanding expiry tolerance to "suppress clock complaints" |
| **`kid` injection** | Building a key-lookup path or SQL query from the raw `kid` value; honoring the `jwk` header |
| **Weak HMAC secret** | Short, human-chosen, or default signing key for HS* tokens |
| **No revocation** | Logout that only clears the client-side token; no denylist; stolen token valid until `exp` |
| **Sensitive data in payload** | PII, roles, internal IDs in claims that are only Base64-encoded, not encrypted |

---

## Symptom

Observable faults — what shows up in tickets, logs, and pen-test findings:

- **Auth bypass / privilege escalation** — attacker crafts a token with `admin:true` or an arbitrary `sub`; accepted without a verification error. (alg confusion or signature skip)
- **Token-type confusion** — ID Token replayed at an API endpoint and honored; audit entry shows wrong token class; interop tools report "unexpected typ". (missing `typ` check)
- **Cross-service token replay** — token minted for API-A accepted at API-B without error. (shared or absent `aud`)
- **Expired tokens still active** — long-expired legitimately-issued tokens pass validation. (wide `exp` leeway or missing `exp` check)
- **`invalid_token` never surfaced** — clients receive opaque 500s and cannot distinguish a bad token from a server bug. (wrong error handling)
- **Key-lookup injection** — path traversal or SQL-injection via `kid` causes the verifier to use an empty/attacker-controlled key. (raw `kid` in lookup)
- **JWK injection** — token signed with attacker's own key pair, key embedded in `jwk` header, accepted as verified. (honoring `jwk` header)
- **CVE-2022-21449 ("Psychic Signatures")** — any ES256 token with the hardcoded signature `MAYCAQACAQA` accepted on unpatched Java 15–18. (ECDSA verification bug)
- **Post-logout replay** — user logs out; token remains valid until `exp`; stolen token used by attacker. (no revocation denylist)
- **PII / role disclosure** — claims readable by Base64-decoding the token in browser DevTools or server logs. (unencrypted sensitive claims)

---

## Surface (client vs backend)

**Backend (resource server) — carries most of this page's load:**

The resource server must perform the full validation chain on every inbound request: pin algorithm, verify signature against the JWKS endpoint, check `typ`, verify `iss` exactly, verify `aud` against its own identifier, reject expired/missing `exp`, resolve `kid` through a server-controlled allow-list, ignore `jwk` header, check `scope`/roles before authorizing the action, and return `invalid_token` on any failure. It must also maintain or query a revocation denylist to support pre-expiry invalidation (see [[token-revocation]] and [[token-introspection]]).

**Client (SPA / native app) — narrower surface:**

The client validates the ID Token (not the access token) on receipt: signature via AS JWKS, `iss`, `aud` = its own `client_id`, `exp`, `nonce` matches the value it sent in the authorization request (see [[state-and-nonce]]). The client must not pass JWTs in URL query parameters (leaks via Referer/history — RFC 9700 §4.3.2), must not store tokens in `localStorage` where XSS can reach them (see [[token-storage-browser]]), and must not embed `client_secret` in browser-accessible code (see [[oidc-client-best-practices]]).

**Service-to-service (confidential clients):**

A downstream service acting as a resource server has the same full validation obligation as above. A service acting as an OAuth client (client-credentials grant) has no user-facing token to validate but must still authenticate to the AS with a strong method — prefer asymmetric `private_key_jwt` or mTLS over a static shared secret (see [[service-to-service-client-credentials]]). (inferred from RFC 9700 §2.5 + RFC 9068 §2.2 together)

---

## Contradictions / caveats

- **Token storage in the browser — two OWASP sheets disagree.** The Session Management sheet bans tokens from both `localStorage` and `sessionStorage` (both JS-readable). The JWT for Java sheet recommends `sessionStorage` + `Authorization` header as a pragmatic SPA pattern when paired with a strict CSP. Resolution: prefer the BFF / `HttpOnly`-cookie pattern (see [[bff-token-handler]] and [[token-storage-browser]]); treat `sessionStorage`+CSP+short-lifetime as a minimum-bar fallback, not the default.
- **Key separation is not a security boundary (inferred).** RFC 9068 §5 explicitly calls this out: do not assume distinct signing keys for ID Tokens vs access tokens prevent substitution, because a resource server trusts all keys from the AS's published JWKS.
- **RFC 9700 does not cover classic JWT pitfalls in depth.** Its §4.6.1 notes audience and nonce validation; algorithm confusion (`alg:none`, RS256→HS256) is out of scope there — see RFC 8725 (JWT BCP) and RFC 9068 for the normative rules on those.

---

## See also

- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[oidc-token-validation]]
- [[oidc-client-best-practices]]
- [[token-storage-browser]]
- [[token-revocation]]
- [[token-introspection]]
- [[state-and-nonce]]
- [[bff-token-handler]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[service-to-service-client-credentials]]
- [[bearer-token-usage]]
- [[fapi2-security-profile]]
- [[tokens-and-sessions]]
- [[sso-implementation-review]]
