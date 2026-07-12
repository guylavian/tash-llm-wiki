---
origin: eval-cohort
title: Common JWT Validation Pitfalls
type: question
domain: keycloak
slug: common-jwt-validation-pitfalls
summary: A catalogue of the ways JWT validation goes wrong — algorithm confusion, skipped signature checks, header-injection, and cross-token misuse.
sources:
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth 2.0 Access Tokens)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (OWASP Authentication Cheat Sheet)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP)
  - web:https://owasp.org/www-project-web-security-testing-guide/ (OWASP WSTG)
question_tier: conceptual
status: draft
updated: 2026-07-12
provenance_extracted: 28
provenance_inferred: 5
provenance_ambiguous: 0
---

# What are the common JWT validation pitfalls?

The most frequent JWT validation mistakes fall into nine failure classes, each with a correct rule and an observable symptom:

## Rule (what correct validation looks like)

1. **Pin the algorithm; never trust the `alg` header** — reject `alg: none`, RS256→HS256, and any algorithm mismatch (RFC 9068 §2.1; WSTG-SESS-10)
2. **Verify the signature — do not merely decode** — `jwt.verify()` ≠ `jwt.decode()` (WSTG-SESS-10)
3. **Reject `typ` that does not match the expected token class** — access tokens carry `typ: at+jwt`; ID Tokens must not be accepted at resource endpoints (RFC 9068 §4)
4. **Validate all required claims:** `iss` (exact match), `aud` (specific to this resource server), `exp` (future, minimal clock skew), `sub`, `client_id`, `iat`, `jti` (RFC 9068 §2.2, §4)
5. **Never trust header fields to locate the signing key** — `kid` resolves against a server-controlled JWKS, not attacker-influenced lookup; reject embedded `jwk` header (WSTG-SESS-10)
6. **Prevent cross-JWT confusion with distinct `aud` per resource** (RFC 9068 §5; RFC 8725 §2.8)
7. **Use strong signing keys** — HMAC secrets must be high-entropy CSPRNG output (WSTG-SESS-10; OWASP JWT Cheat Sheet)
8. **Do not rely on key separation as a security boundary** — all keys from the AS's JWKS are trusted (RFC 9068 §5)
9. **Return `invalid_token` on every validation failure** (RFC 9068 §4 / RFC 6750 §3.1)
10. **Pair `exp` with revocation for stolen-token scenarios** — expiry alone cannot pre-expire after logout (OWASP JWT Cheat Sheet)

## Anti-pattern (failure class → common mistake)

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

## Symptom (observable faults)

- **Auth bypass / privilege escalation** — signed-in as arbitrary user/admin (alg confusion or signature skip)
- **Token-type confusion** — ID Token replayed at API endpoint (missing `typ` check)
- **Cross-service token replay** — token for API-A accepted at API-B (shared/absent `aud`)
- **Expired tokens still active** — wide `exp` leeway or missing `exp` check
- **`invalid_token` never surfaced** — opaque 500s instead of `WWW-Authenticate: Bearer error="invalid_token"`
- **Key-lookup injection** — path traversal/SQL injection via `kid`
- **JWK injection** — attacker embeds their own key in `jwk` header
- **CVE-2022-21449 ("Psychic Signatures")** — ES256 tokens accepted on unpatched Java 15–18
- **Post-logout replay** — no revocation denylist; stolen token valid until `exp`
- **PII / role disclosure** — claims readable via Base64 decoding

## References

**RH ground-truth:**
- None — this page draws entirely from RFCs and OWASP.

**Wiki:**
- [[jwt-validation-pitfalls]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[oidc-token-validation]]
- [[oidc-client-best-practices]]
- [[token-revocation]]
- [[token-introspection]]

**Upstream `web:` sources:**
- RFC 9068 (JWT Profile for OAuth 2.0 Access Tokens)
- RFC 9700 (OAuth 2.0 Security BCP)
- RFC 8725 (JWT Best Current Practices)
- RFC 6750 (Bearer Token Usage)
- OWASP WSTG (SESS-10)
- OWASP JWT Cheat Sheet
