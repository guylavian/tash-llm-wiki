---
source: draft-ietf-oauth-browser-based-apps-26
url: https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html
fetched: 2026-06-17
status: Internet-Draft rev-26 (3 Dec 2025), work-in-progress
feeds: [token-storage-browser, bff-token-handler, refresh-token-rotation, cors-for-spa]
---

# OAuth 2.0 for Browser-Based Applications (draft-26) — raw staging note

Three architecture patterns defined in §6: BFF / proxying backend (§6.1), token-mediating backend (§6.2), browser-based OAuth client (§6.3). BFF is strongly recommended for sensitive / personal-data apps (§6.1.4.3.3); token-mediating backend only when a proxying BFF is infeasible (§6.2.4.4.3). Core premise: malicious JS has the same privileges as legit app code, so no purely browser-side storage stops token theft under XSS (§5.5).

## token-storage-browser

- RULE: Don't put tokens in localStorage/sessionStorage reachable by JS (§8.5). ANTI-PATTERN: stashing access/refresh tokens in Web Storage for convenience. SYMPTOM: XSS payload reads `localStorage`/`sessionStorage` and exfiltrates the token — single-execution & persistent token theft (§5.1.1, §5.1.2).
- RULE: In-memory storage only protects during the active session; lost on reload (§8.4). ANTI-PATTERN: treating in-memory as a security boundary. SYMPTOM: token gone after refresh -> silent re-auth on every reload; still readable by JS during the session.
- RULE: Web Workers do NOT isolate token from the main execution context (§8.3); Service Workers may hold tokens but stay vulnerable to malicious code with origin access (§8.2). ANTI-PATTERN: "worker = sandbox" assumption. SYMPTOM: token still extractable by injected script — persistent token theft (§5.1.2).
- RULE: HttpOnly cookies keep token data out of JS reach (§6.1.3.2). The only architecture that avoids exposing tokens to the browser at all is the BFF (§6.1). ANTI-PATTERN: any browser-readable token store for a sensitive app. SYMPTOM: stolen-token abuse (§5.2.2).

## bff-token-handler

- RULE: BFF MUST be a confidential OAuth client using the Authorization Code grant, not Implicit (§6.1.3.1); same for token-mediating backend (§6.2.3.1). ANTI-PATTERN: public client / implicit flow in the backend. SYMPTOM: attacker silently acquires new tokens — "acquisition & extraction of new tokens" (§5.1.3).
- RULE: BFF session cookie MUST set `Secure` + `HttpOnly`; SHOULD set `SameSite=Strict`, SHOULD use `__Host-` name prefix, SHOULD NOT set `Domain` (§6.1.3.2). ANTI-PATTERN: cookie without HttpOnly / with broad `Domain`. SYMPTOM: XSS reads session id, or a subdomain takeover hijacks the session (§6.1.3.3.1).
- RULE: If using client-side (cookie-stored) sessions, SHOULD encrypt cookie contents (§6.1.3.2). ANTI-PATTERN: plaintext tokens inside a session cookie. SYMPTOM: malware/disk access reads tokens straight from cookie store.
- RULE: BFF MUST enforce outbound request controls — allowlist of approved resource servers (§6.1.3.6). ANTI-PATTERN: open proxy forwarding to any URL/host the browser names. SYMPTOM: attacker redirects a proxied call to an attacker host and the BFF attaches the token -> token leak.
- TOKEN-MEDIATING vs BFF: token-mediating backend keeps the refresh token server-side but hands the access token to the browser (§6.2.1); CSRF defenses there cover only the token-retrieval endpoint (§6.2.3.3), narrower than BFF which proxies/defends all endpoints. TRADE-OFF: refresh token protected, but access token still stealable from the browser (§5.1.1/§5.1.2 -> §5.2.2). Use only when a proxying BFF is not possible (§6.2.4.4.3).
- NOTE: BFF residual risk is "proxying requests via the user's browser" / client hijacking (§5.1.4 -> §5.2.3), inherent to web apps; BFF otherwise does not enlarge the OAuth attack surface (§6.1.4.3.2).

## refresh-token-rotation

- RULE: AS MUST either rotate the refresh token on every use OR issue sender-constrained (DPoP) refresh tokens (§6.3.2.3). ANTI-PATTERN: long-lived static refresh token for a browser client. SYMPTOM: stolen refresh token replayed indefinitely; no reuse/replay detection (cf. RFC 9700 §4.14.2).
- RULE: AS MUST set a maximum lifetime OR expire the refresh token if unused within a defined window (§6.3.2.3). ANTI-PATTERN: never-expiring refresh token. SYMPTOM: a single theft yields permanent access.
- RULE: AS MUST NOT extend a rotated token's lifetime past the original issuance expiry (§6.3.2.3) — e.g. an initial 8h window stays fixed across rotations. ANTI-PATTERN: resetting the clock on each rotation. SYMPTOM: "rotating" token that effectively lives forever via continuous refresh.
- RULE: AS SHOULD bind refresh-token lifetime to the user's authenticated session (§6.3.2.3) and MAY apply stricter policy to browser apps than other public clients. SYMPTOM if ignored: refresh token outlives logout -> session survives single-logout.
- LIMITATION (don't over-claim): rotation does NOT stop persistent token theft — attacker can prevent the app using the newest token (clear it / wait for browser offline) (§5.1.2.3); and DPoP doesn't save a freshly minted access token, since the attacker can bind it to their own key (§5.2.2.4). Browser clients issued refresh tokens MUST follow RFC 9700 recommendations (§6.3.2.3).

## cors-for-spa

- RULE: For browser-based OAuth clients, the AS MUST send CORS headers on the token endpoint, and on discovery/JWKS/revocation/introspection/UserInfo where provided (§6.3.3.4). ANTI-PATTERN: token endpoint with no CORS headers. SYMPTOM: browser fetch blocked — "No 'Access-Control-Allow-Origin' header is present" / CORS preflight failure during the code-for-token exchange. (Spec leaves wildcard-vs-restrictive policy to the implementer.)
- RULE: BFF MUST implement CSRF defense — `SameSite`, CORS, and/or anti-forgery tokens (§6.1.3.3). ANTI-PATTERN: cookie-auth API with no CSRF control. SYMPTOM: cross-site request rides the session cookie -> state-changing CSRF.
- RULE: `SameSite=Strict` alone is insufficient when the BFF shares an eTLD+1 (sibling subdomains) with other apps (§6.1.3.3.1). ANTI-PATTERN: relying solely on SameSite on a multi-tenant domain. SYMPTOM: subdomain takeover -> same-site CSRF.
- RULE: BFF SHOULD require a custom request header on all API calls so any cross-origin call triggers a CORS preflight the browser then blocks (e.g. `My-Static-Header: 1`) (§6.1.3.3.2); alternatively deploy the BFF same-origin as the frontend to avoid CORS entirely (§6.1.3.3.2). BFF MAY also use anti-forgery / double-submit cookie tokens (§6.1.3.3.3). SYMPTOM if absent: simple-request CSRF that never hits preflight.
