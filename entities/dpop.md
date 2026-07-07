---
title: DPoP — Demonstrating Proof-of-Possession
type: entity
domain: keycloak
slug: dpop
summary: "RFC 9449 mechanism that turns Bearer tokens into *sender-constrained* tokens by binding them to a client's public/private key pair, so a stolen token is useless without the private key. Covers both RHBK product behavior and the RFC 9449 wire protocol."
aliases: [DPoP sender-constraining, dpop-sender-constraining]
sources:
  - guide:securing_applications_and_services_guide
  - kb:dpop-
  - web:https://www.rfc-editor.org/rfc/rfc9449 (RFC 9449 — DPoP, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 — OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
source_notes:
  - "[[rhbk-26-6-dpop]]"
provenance_extracted: 34
provenance_inferred: 5
provenance_ambiguous: 0
tags: [clients, tokens, security, concept]
symptoms:
  - "invalid_dpop_proof"
  - "use_dpop_nonce"
  - "invalid_token"
status: reviewed
updated: 2026-07-02
---

# DPoP — Demonstrating Proof-of-Possession

**RFC 9449 mechanism that turns Bearer tokens into *sender-constrained* tokens by
binding them to a client's public/private key pair, so a stolen token is useless
without the private key.**

## Why
A Bearer token works for anyone who holds it; if leaked (logs, XSS, browser
storage) it can be replayed. DPoP binds the access **and** refresh token to a key
pair the client controls.

## How it works (RHBK)
1. **Key binding** — at the token request the client generates a key pair and
   sends its public key. RHBK computes the JWK **thumbprint** (base64url SHA-256)
   and embeds it in the access token under the `cnf.jkt` confirmation claim; the
   token's `token_type` becomes `DPoP`.
2. **Proof of possession** — on every resource request the client sends a fresh,
   single-use **DPoP proof JWT** in the `DPoP` header, signed with its private
   key. The resource server checks the signature against the embedded thumbprint.

## DPoP proof JWT
- Header: `typ: dpop+jwt`, asymmetric `alg` (e.g. `ES256`, `RS256`), and the
  public key `jwk`.
- Body: `jti` (unique id), `htm` (HTTP method), `htu` (target URI, no
  query/fragment), `iat`; plus `ath` (base64url SHA-256 of the access token,
  required when accessing resources) and `nonce` only if the server demands one
  via a `DPoP-Nonce` header.

## Use cases & client metadata
Best for public clients (SPAs, native/mobile), browser apps exposed to XSS,
high-security/FAPI environments, and to stop service-chaining. The
`dpop_bound_access_tokens` client registration metadata enables it.

---

## Specification detail (RFC 9449)

The material below is the upstream wire protocol RHBK implements. It is normative
RFC text, not an RHBK support statement — use it to understand *why* RHBK behaves
as documented above.

### Proof JWT structure (RFC 9449 §4.2)
The client generates a DPoP proof JWT for every request. The JOSE header MUST set
`typ` to `dpop+jwt`, `alg` to a registered asymmetric algorithm (never `none`,
never HMAC), and `jwk` to the public key (private key MUST NOT appear in `jwk`).
Required payload claims: `jti` (unique, unguessable per-request ID), `htm` (HTTP
method), `htu` (target URI without query string or fragment), and `iat` (creation
time). When presenting a token to a resource server the proof MUST also include
`ath` = base64url(SHA-256(access token ASCII value)). When the server has issued a
nonce, the `nonce` claim MUST be present (§7, §8).

### AS token binding (RFC 9449 §5, §6.1)
At the token endpoint the authorization server MUST associate the issued token
with the public key from the proof and MUST return `token_type: DPoP`. For JWT
access tokens the binding travels as `cnf.jkt`, the base64url JWK SHA-256
thumbprint of the proof key (§6.1). The Security BCP (RFC 9700 §2.2.1, §4.10.1)
requires ASes and RSes to sender-constrain tokens via DPoP or mTLS; DPoP is the
mechanism that works for public clients (SPAs, native apps) without requiring
client certificates.

### RS validation (RFC 9449 §4.3, §7.1)
The resource server MUST verify: exactly one `DPoP` header present; proof is a
well-formed JWT; all required claims present; `typ=dpop+jwt`; asymmetric non-`none`
algorithm; signature verifies against the embedded `jwk`; `jwk` contains no private
key; `htm`/`htu` match the actual request; `nonce` matches if one was issued; `iat`
falls within an acceptable clock window; `ath` equals the SHA-256 of the presented
token value; and the token's `cnf.jkt` thumbprint equals the proof's `jwk`
thumbprint (§4.3 item 12). Critically, the RS MUST require a `DPoP` header for any
DPoP-bound token and MUST NOT grant access if any check fails (§7.1).

### Bearer-scheme downgrade rejection (RFC 9449 §7.2)
A DPoP-bound access token presented using the `Authorization: Bearer` scheme MUST
be rejected. The binding is scheme-specific; accepting the token under Bearer
silently removes the sender-constraint.

### Nonce mechanism (RFC 9449 §8, §9)
The AS MAY require a server nonce to shorten the proof pre-generation window. If a
nonce is missing, the AS returns HTTP 400 with `error=use_dpop_nonce` and a
`DPoP-Nonce` response header. The RS signals the same requirement via HTTP 401 with
`WWW-Authenticate: DPoP` plus `DPoP-Nonce`. Nonce values MUST be unpredictable.
Once a nonce has been issued the server MUST NOT accept proofs without it — no
nonce-downgrade (§11.3).

### Replay protection (RFC 9449 §11.1, §11.3)
Servers MUST enforce a short `iat` acceptance window (seconds to a few minutes).
Servers SHOULD track `jti` values (or their hashes) to enforce one-time use.
Without server nonces, pre-generated proofs become a risk, so deployments that skip
nonces SHOULD NOT issue long-lived DPoP-bound access tokens (§11.2).

### Refresh-token scope (RFC 9700 §2.2.2, §4.14; OAuth 2.1 §1.4.3)
For public clients, refresh tokens MUST be sender-constrained OR use single-use
rotation. DPoP sender-constraining is one accepted path to satisfy this MUST
(inferred). Rotation is the common alternative when DPoP is not deployed.

### Anti-patterns (RFC 9449 / RFC 9700)
1. **Wrong `typ` or symmetric `alg`** — emitting `typ:JWT` instead of `dpop+jwt`,
   or accepting `alg:none` / `alg:HS256`. Makes proofs forgeable and triggers
   key-confusion.
2. **Reusing or sequential `jti`** — reusing a `jti` value across requests breaks
   replay detection.
3. **`htu` with query string attached** — the URI bound in `htu` MUST exclude
   query and fragment; attaching them causes valid proofs to fail `htu` comparison.
4. **Dropping `ath` on resource calls** — omitting the access-token hash means one
   proof is reusable with arbitrary tokens (token-substitution attack).
5. **Validating the proof signature but skipping the `jkt` == thumbprint(`jwk`)
   check** — a proof from key A is accepted with a token bound to key B.
6. **Accepting a DPoP-bound token without an accompanying proof** — allows stolen
   tokens to be replayed as bearer tokens.
7. **Falling back to Bearer validation for a DPoP token** — an RS that accepts
   `Authorization: Bearer <dpop-token>` strips the binding silently.
8. **Predictable or static server nonces** — nonces MUST be unpredictable.
9. **Storing the DPoP private key alongside the token** (RFC 9700 §4.10.1) — if
   both are captured together, sender-constraining is defeated; the key should be
   non-exportable where the platform allows.
10. **Long token lifetimes without server nonces** — expands the window in which a
    pre-generated proof can be misused (§11.2).

### Scope limitation
DPoP binds only HTTP method and URI — request body integrity depends on TLS
(§11.7). DPoP cannot protect against an attacker who can run code inside the
client's process and mint proofs in real time (§11.4). For highest-assurance flows
(FAPI 2.0) see [[fapi2-security-profile]] and [[mtls-bound-tokens]] as alternatives
or complements.

---

## Symptoms — observable failures
- RS returns `invalid_dpop_proof` — proof structure violation: wrong `typ`, bad
  `alg`, missing required claim, `htu` mismatch, wrong or missing `ath`, `nonce`
  mismatch, or signature failure.
- RS returns `invalid_token` — token/binding mismatch: `cnf.jkt` does not match
  proof `jwk` thumbprint.
- RS/AS returns `use_dpop_nonce` (HTTP 400 or 401) — nonce required but absent;
  client must retry with the `DPoP-Nonce` value echoed from the response.
- Infinite 400/401 loop labeled `use_dpop_nonce` in client logs — client not
  implementing nonce retry.
- Stolen token accepted without a DPoP header — bearer-scheme fallback not blocked.
- Proof from key A accepted with token bound to key B — `jkt` vs `jwk` thumbprint
  check absent.
- Security review flags `alg:none` in DPoP validation — CVE-class finding if
  `none` or HMAC allowed in the server's algorithm allowlist.

## Contradictions / caveats
- Documented as a full feature in **RHBK 26.6**; in earlier 26.x it was referred
  to as a **preview** feature recommended alongside the OAuth 2.1 public-client
  profile. Confirm feature flag status for your version.
- Refresh-token handling differs by client type: public clients cannot hold
  credentials, so their refresh tokens are DPoP-bound; confidential clients
  behave slightly differently.
- Upstream RFC 9700 phrases token sender-constraining as a **SHOULD** for ASes/RSes
  (via DPoP or mTLS); RHBK exposes it as opt-in per client via
  `dpop_bound_access_tokens`. Prefer the RHBK docs for a support question and treat
  the RFC as the protocol rationale.

## See also
- [[client-authentication-methods]]
- [[fapi-oauth21-profiles]]
- [[fapi2-security-profile]]
- [[oidc-token-validation]]
- [[oidc-grant-types]] — grants that issue the tokens DPoP binds
- [[mtls-bound-tokens]]
- [[bearer-token-usage]]
- [[oidc-client-best-practices]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[refresh-token-rotation]]
- [[token-storage-browser]]
- [[bff-token-handler]]
- [[tokens-and-sessions]]
- [[jwt-validation-pitfalls]]
- [[token-revocation]]
- [[token-introspection]]
- [[service-to-service-client-credentials]]
- [[securing-apps-oidc-saml]]
- [[sso-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-dpop|Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP)]]
<!-- crosslink:end -->
