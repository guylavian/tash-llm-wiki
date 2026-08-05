---
origin: eval-cohort
title: What must a resource server do to prevent token substitution attacks?
type: question
domain: keycloak
slug: token-substitution-attack-resource-server
summary: A resource server prevents token substitution by validating `aud` (rejecting tokens not addressed to it), checking `typ` (preventing ID Token replay), and enforcing DPoP proof-of-possession with the `ath` claim — the three normative defenses against cross-service token replay.
sources:
  - note:_sources/keycloak/rfc9068.md   # aud + typ=at+jwt rules (its `feeds:` labels were previously
  - note:_sources/keycloak/rfc9449.md   #   mis-cited here as kb: ids — they are sections, not notes)
  - note:_sources/keycloak/rfc8705.md
  - kb:dpop
  - web:https://datatracker.ietf.org/doc/rfc9068/ (RFC 9068, JWT Profile for Access Tokens)
  - web:https://datatracker.ietf.org/doc/rfc9449/ (RFC 9449, DPoP)
  - web:https://datatracker.ietf.org/doc/rfc8705/ (RFC 8705, mTLS-Bound Tokens)
provenance:
  extracted: 10
  inferred: 2
  ambiguous: 0
question_tier: conceptual
tags: [tokens]
status: draft
updated: 2026-07-12
graph_community: "Tokens & Sessions"
---

# What must a resource server do to prevent token substitution attacks?

**Token substitution (also called cross-service token replay) occurs when an attacker takes an access token that was legitimately issued for Resource Server A and presents it to Resource Server B, and RS-B incorrectly accepts it. Three independent defenses prevent this:**

## 1. Audience (`aud`) validation — the primary defense

The resource server MUST verify that the `aud` claim in the JWT access token contains a resource indicator identifying *this specific resource server* (`access-token-validation-resource-server.md:51`). If `aud` does not include the RS's own identifier, the token MUST be rejected regardless of any other valid claims (`audience-and-scope-checks.md:29`). This is the fundamental defense: a token minted for API-A carries `aud: api-a.example.com` and will be rejected at `api-b.example.com` because the audience doesn't match (inferred).

The AS must cooperate by issuing tokens with a **distinct `aud` per resource server** (`audience-and-scope-checks.md:39-41`, citing RFC 9068 §5 / RFC 8725 §2.8). A shared or wildcard audience across multiple APIs means tokens are freely replayable across the entire estate — the `aud` check becomes a no-op (`audience-and-scope-checks.md:54`).

Symptom when absent: "Token minted for API-A replayed against API-B and accepted — `aud` unchecked; token substitution / privilege crossing" (`access-token-validation-resource-server.md:102`).

## 2. `typ` header validation — prevents ID Token replay

The RS MUST reject any JWT whose `typ` header is absent, wrong, or `JWT` — only `typ: at+jwt` (per RFC 9068 §2.1, §4) is acceptable (`access-token-validation-resource-server.md:41-42`). This prevents ID Tokens (which carry `typ: JWT` or no `at+jwt` marker) from being replayed at resource server endpoints. Key separation between ID Token and access-token signing keys does NOT substitute for this check — the RS accepts all keys published by the AS, so key diversity does not achieve isolation (`access-token-validation-resource-server.md:42`).

## 3. Sender-constrained tokens (DPoP / mTLS)

### DPoP (RFC 9449)

DPoP binds the access token to a client-held key pair via the `cnf.jkt` confirmation claim. The RS must require a `DPoP` header containing a DPoP proof JWT and must validate:

- The proof JWT's `ath` (access token hash) equals the SHA-256 of the presented access token (`dpop.md:93-94`). **Dropping the `ath` check is the DPoP-layer token-substitution vulnerability**: omitting `ath` means "one proof is reusable with arbitrary tokens (token-substitution attack)" (`dpop.md:130-131`).
- The `cnf.jkt` thumbprint in the token equals the JWK thumbprint of the proof's embedded public key (`dpop.md:94-95`).
- `htm`, `htu`, `iat`, and `nonce` (if required) all validate (`dpop.md:89-93`).

A DPoP-bound token presented under `Authorization: Bearer` (instead of `DPoP`) MUST be rejected — accepting it silently removes the sender-constraint, enabling replay (`dpop.md:98-101`).

### mTLS certificate-bound tokens (RFC 8705)

The RS obtains the client TLS certificate from the mutual-TLS layer, computes SHA-256 of the DER encoding, and compares against `cnf.x5t#S256` in the token (`mtls-bound-tokens.md:52`). Mismatch → HTTP 401 `invalid_token`. The RS MUST NOT validate the cert's trust chain — only the thumbprint match matters (`mtls-bound-tokens.md:52`).

## Supporting controls

- **Scope enforcement**: after verifying `aud`, the RS must check scope/roles before granting access (`access-token-validation-resource-server.md:59-60`). This prevents substitution where a token has the right `aud` but was issued for narrower privileges.
- **Exact `iss` match**: prefix or substring matching on `iss` enables issuer-confusion attacks (`access-token-validation-resource-server.md:47-48`).
- **Use `Authorization: Bearer` header only**: tokens transmitted via query string (`?access_token=`) leak into logs, browser history, and Referer headers — increasing the risk of substitution (`bearer-token-usage.md:see body`).

## Anti-pattern

| Gap | Consequence |
|---|---|
| No `aud` check | Token from API-A accepted at API-B — token substitution succeeds silently |
| No `typ` check | ID Token replayed as access token; valid signature, wrong token class |
| DPoP without `ath` validation | A single proof JWT works with any token — defeats DPoP binding |
| Bearer-scheme fallback for DPoP token | Stolen DPoP token replayed without the private key |
| Shared `aud` across all APIs | One token for everything; `aud` check is a no-op |
| Introspection-only for opaque tokens | Cached introspection result survives token revocation — stale cache enables substitution window |

## See also

- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[dpop]]
- [[mtls-bound-tokens]]
- [[bearer-token-usage]]
- [[jwt-validation-pitfalls]]
- [[oidc-token-validation]]
- [[sso-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-dpop|Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP)]]
<!-- crosslink:end -->
