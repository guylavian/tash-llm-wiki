---
source: OWASP ASVS — Authentication & Session Management chapters
url: https://owasp.org/www-project-application-security-verification-standard/
fetched: 2026-06-18
status: OWASP ASVS
feeds: [token-storage-browser, cors-for-spa]
---

<!-- Version note: section numbers below are ASVS 4.0.3 (the stable, widely-cited scheme).
     ASVS 5.0.0 (2025-05-30) reorganized these: session-cookie rules moved toward a new
     "V50 Web Frontend Security" chapter; CORS reworded (see notes inline). Both cited where useful. -->

## token-storage-browser

- **V3.2.3 (Session Binding) — only secure browser storage for session tokens.**
  - RULE: store browser-held session/access tokens only in appropriately-secured cookies (per §3.4) or HTML5 *sessionStorage* — nothing else qualifies.
  - ANTI-PATTERN: persisting an access/refresh token (or JWT) in `localStorage` or IndexedDB so a JS framework can read it across tabs/restarts.
  - SYMPTOM: pentest/SAST flags "JWT in localStorage / sensitive data in web storage"; any XSS payload exfiltrates the bearer token; token survives tab close and is replayable.

- **V8.2.2 (Data Protection) — no sensitive data in client storage.**
  - RULE: data in `localStorage`, `sessionStorage`, IndexedDB, or cookies must not contain sensitive data or PII (reinforces V3.2.3; aligns with NIST SP 800-63B §7.1 — session secrets must not sit in insecure locations exposed to XSS).
  - ANTI-PATTERN: caching id_token claims, refresh tokens, or PII client-side "to avoid an extra round trip."
  - SYMPTOM: data-leak ticket after an XSS / malicious-dependency incident; tokens/PII readable from DevTools Application tab.

- **V3.4.1 (Cookie-based Session Mgmt) — `Secure` attribute.**
  - RULE: cookie-based session tokens must set `Secure` so they transmit only over TLS.
  - ANTI-PATTERN: omitting `Secure` (or terminating TLS at a proxy and forwarding plaintext) so the cookie rides cleartext HTTP.
  - SYMPTOM: session cookie observable in an HTTP request / on the wire; MITM session hijack; header scanners flag "Set-Cookie without Secure".

- **V3.4.2 (Cookie-based Session Mgmt) — `HttpOnly` attribute.**
  - RULE: cookie-based session tokens must set `HttpOnly` so `document.cookie`/JS cannot read them.
  - ANTI-PATTERN: leaving `HttpOnly` off so SPA JavaScript can introspect the session cookie.
  - SYMPTOM: XSS payload reads cookie via `document.cookie`; scanners flag "Set-Cookie missing HttpOnly". (In ASVS 5.0 this rule is reworded/relocated toward the V50 frontend chapter.)

- **V3.4.3 (Cookie-based Session Mgmt) — `SameSite` attribute.**
  - RULE: session cookies should use `SameSite` (Lax/Strict) to limit CSRF exposure from cross-site requests.
  - ANTI-PATTERN: `SameSite=None` (or unset on older browsers) without a complementary CSRF defense.
  - SYMPTOM: CSRF finding; cross-site request silently carries the session cookie.

- **V3.4.4 (Cookie-based Session Mgmt) — `__Host-` prefix.**
  - RULE: session cookies should carry the `__Host-` prefix so the cookie is host-bound (forces Secure, path `/`, no Domain).
  - ANTI-PATTERN: broad `Domain=.example.com` cookies shared across subdomains; trusting a cookie a sibling subdomain could have set.
  - SYMPTOM: cookie-fixation / cross-subdomain injection; missing-`__Host-` audit note.

## cors-for-spa

- **V14.5.3 (V14 Configuration → HTTP Request Header validation) — strict CORS allow-list.**
  - RULE: `Access-Control-Allow-Origin` must come from a strict allow-list of trusted domains/subdomains validated against the request `Origin`; do **not** support the `null` origin. (ASVS 5.0 rewording: ACAO is a fixed application value, or the `Origin` value is validated against an allowlist of trusted origins; if `ACAO: *` is genuinely required, the response must carry no sensitive info.)
  - ANTI-PATTERN: serving `Access-Control-Allow-Origin: *` on credentialed/sensitive endpoints, or whitelisting `null` "for local dev."
  - SYMPTOM: any-origin browser can read the API response; auditors flag wildcard ACAO on an authenticated route; `null`-origin page (sandboxed iframe / `file://`) reads data.

- **Origin reflection is forbidden (V14.5.3 intent).**
  - RULE: never echo the request `Origin` straight back into `Access-Control-Allow-Origin`; an unknown/forged origin must yield *no* ACAO header.
  - ANTI-PATTERN: reflecting `Origin` verbatim, especially together with `Access-Control-Allow-Credentials: true` — lets an attacker page do a credentialed cross-origin read.
  - SYMPTOM: CORS scanner shows ACAO == arbitrary attacker `Origin` (even a non-existent domain); cross-site data theft of credentialed responses.

- **`Allow-Origin: *` is incompatible with credentials.**
  - RULE: browsers reject `Access-Control-Allow-Credentials: true` combined with wildcard ACAO — a credentialed SPA must echo an exact, allow-listed origin.
  - ANTI-PATTERN: trying `ACAO: *` + `Allow-Credentials: true` for a cookie/Authorization-bearing SPA call.
  - SYMPTOM: browser blocks the response with "The value of the 'Access-Control-Allow-Origin' header ... must not be the wildcard '*' when the request's credentials mode is 'include'"; fetch/XHR fails CORS preflight.

- **Origin header alone is not authentication.**
  - RULE: do not authenticate requests by trusting `Origin` — non-browser clients (curl/Burp) set it freely; require real credentials and CSRF defenses on the resource.
  - ANTI-PATTERN: gating access on `Origin` matching instead of tokens/session + CSRF token.
  - SYMPTOM: server-to-server / scripted client bypasses the "origin check" by spoofing `Origin`; access granted without valid credentials.
