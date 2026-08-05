---
source: OWASP Cheat Sheets — Authentication, Session Management, JWT
url: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
fetched: 2026-06-18
status: OWASP Cheat Sheet Series
feeds: [token-storage-browser, state-and-nonce, jwt-validation-pitfalls, cors-for-spa]
---

<!-- Three sheets fetched:
       Authentication_Cheat_Sheet.html        (foundational; defers token/session/CORS specifics to the sheets below)
       Session_Management_Cheat_Sheet.html     (cookie attributes, web-storage ban, timeouts, fixation)
       JSON_Web_Token_for_Java_Cheat_Sheet.html (JWT validation pitfalls + client-side storage)
     The Authentication sheet itself carries little load here — it references the others for
     token storage, CSRF state, alg validation, and CORS. Section names are sheet headings (anchors),
     not numbered clauses (OWASP cheat sheets are best-practice guidance, not a numbered standard).
     Cookie-attribute rules overlap [[owasp-asvs]] V3.4.* — cited there with ASVS clause numbers;
     here they are kept tight to avoid duplication. -->

## token-storage-browser

- **Session Mgmt → "HttpOnly Attribute" / "Secure Attribute" — session cookies must be `HttpOnly` + `Secure`.**
  - RULE: set `HttpOnly` so `document.cookie`/JS cannot read the session ID; set `Secure` so it rides TLS only.
  - ANTI-PATTERN: omitting either flag, or terminating TLS at a proxy and forwarding the cookie over plaintext.
  - SYMPTOM: XSS reads the session via `document.cookie`; cookie observable on the wire; header scanner flags "Set-Cookie missing HttpOnly/Secure".

- **Session Mgmt → "SameSite Attribute" — set `SameSite=Strict` (or `Lax`); never `None` without `Secure`.**
  - RULE: `SameSite` stops the cookie from riding cross-site requests, giving baseline CSRF defense.
  - ANTI-PATTERN: leaving it unset (browser default), or `SameSite=None` on a session cookie with no complementary CSRF token.
  - SYMPTOM: cross-site form/`fetch` silently carries the session cookie → CSRF.

- **Session Mgmt → "Cookie Name Prefixes" — use the `__Host-` prefix for session IDs.**
  - RULE: `__Host-` binds the cookie to the host (forces `Secure`, `Path=/`, no `Domain`).
  - ANTI-PATTERN: generic cookie name + broad `Domain=.example.com`, so a sibling subdomain can set/read it.
  - SYMPTOM: cross-subdomain cookie injection / fixation; missing-`__Host-` audit note.

- **Session Mgmt → "Domain and Path Attributes" — narrowest scope; do not set a permissive `Domain`.**
  - RULE: restrict the cookie to the origin host and the narrowest `Path`; don't run apps of different security levels on the same host.
  - ANTI-PATTERN: `Domain=.example.com` to "share login across subdomains"; co-hosting public + private apps.
  - SYMPTOM: a vuln in one subdomain/app hijacks the parent's session; cross-subdomain CSRF.

- **Session Mgmt → web-storage ban — do NOT store session IDs / tokens / JWTs / refresh tokens in `localStorage` or `sessionStorage`.**
  - RULE: keep browser-held session tokens in a secured cookie, not in Web Storage (JS-readable).
  - ANTI-PATTERN: persisting an access/refresh token or JWT in `localStorage` so a SPA framework can read it across tabs/restarts.
  - SYMPTOM: a single XSS exfiltrates every active token; pentest/SAST flags "JWT in localStorage"; token survives tab-close and replays. (Aligns with [[owasp-asvs]] V3.2.3 / V8.2.2.)

- **Session Mgmt → "Used vs. Accepted Session ID Exchange Mechanisms" — no session IDs in the URL.**
  - RULE: exchange session IDs via cookies only; never via query/path parameters or URL rewriting.
  - ANTI-PATTERN: `?jsessionid=` / token-in-URL for "stateless deep links."
  - SYMPTOM: session ID leaks into browser history, server logs, the `Referer` header, and bookmarks.

- **Session Mgmt → "Web Content Caching" — `Cache-Control: no-store` on responses carrying a session ID.**
  - RULE: session identifiers must never be cached; use `no-store` (not merely `no-cache`).
  - ANTI-PATTERN: relying on `no-cache`, or letting `Set-Cookie` ride a cacheable response.
  - SYMPTOM: session ID recoverable from browser/proxy cache after logout (shared-kiosk replay).

- **JWT (Java) → "Token Storage on the Client Side" — `sessionStorage` + `Authorization: Bearer`, hardened by CSP; (inferred) cross-references the Session-Mgmt cookie advice above.**
  - RULE (upstream, JWT sheet): when a JWT must live in the browser, prefer `sessionStorage` read into an `Authorization` header, paired with a strict Content Security Policy (or hold it in a JS closure / private variable); if it must sit in `localStorage`, force short idle (15–30 min) + absolute (~8 h) expiry plus rotation/refresh.
  - ANTI-PATTERN: a long-lived JWT in `localStorage` with no CSP and no rotation; or a JWT in a plain cookie (auto-sent → CSRF) with no SameSite.
  - SYMPTOM: XSS exfiltrates the bearer token; large replay window after theft. (NOTE: this JWT-sheet `sessionStorage` recommendation and the Session-Mgmt sheet's "no tokens in any Web Storage" guidance pull in different directions — see Contradictions.)

## state-and-nonce

- **Session Mgmt → "SameSite Attribute" — `SameSite` is a first-class CSRF mitigation.**
  - RULE: `SameSite=Strict`/`Lax` prevents the browser from attaching the session cookie to cross-site requests; treat it as a defense-in-depth layer alongside an explicit anti-CSRF token, not a replacement.
  - ANTI-PATTERN: relying solely on `SameSite` (or solely on a CSRF token) instead of both; `SameSite=None` on a state-changing endpoint.
  - SYMPTOM: attacker-page form auto-submits with the victim's session → state-changing CSRF succeeds.

- **Session Mgmt → "Permissive and Strict Session Management" — reject any session ID the app never issued (strict mode).**
  - RULE: the app must only honor session IDs it generated; never adopt a client-supplied unknown ID.
  - ANTI-PATTERN: permissive mode (e.g. PHP default) that accepts an attacker-planted session ID.
  - SYMPTOM: session fixation — attacker pre-seeds the victim's session ID, then rides the authenticated session.

- **Session Mgmt → "Renew the Session ID After Any Privilege Level Change" — regenerate on login / privilege change.**
  - RULE: issue a fresh session ID at every privilege boundary (login, step-up, role change, password change).
  - ANTI-PATTERN: reusing the pre-auth session ID after login.
  - SYMPTOM: a session ID captured before login still works after authentication → privilege escalation / fixation.

- **(inferred) These sheets are the CSRF/session-fixation backstop for the OAuth `state` and OIDC `nonce` parameters.**
  - RULE: OWASP's session-fixation + SameSite guidance is the browser-side complement to the protocol-level anti-forgery in `state` (CSRF on the redirect) and `nonce` (ID-token replay) — see [[oidc-core]] / [[oauth21]]. The cheat sheets do not define `state`/`nonce` themselves.
  - ANTI-PATTERN: assuming `SameSite` cookies alone remove the need for the OAuth `state` check (it does not — `state` also binds the callback to the originating request).
  - SYMPTOM: login-CSRF / authorization-code injection despite "we set SameSite" (gap covered only by `state`).

## jwt-validation-pitfalls

- **JWT (Java) → "None Hashing Algorithm" — pin the expected algorithm; reject `alg:none`.**
  - RULE: the verifier must explicitly require the expected algorithm (e.g. RS256), not trust the token's own `alg` header.
  - ANTI-PATTERN: a permissive `verify()` that honors the header `alg`, including `none` (unsigned) or downgraded HMAC.
  - SYMPTOM: attacker strips/forges the signature, edits claims (roles, `sub`), and the app accepts it — auth bypass / privilege escalation. (Same root cause as RS256→HS256 algorithm-confusion when the public key is fed as an HMAC secret.)

- **JWT (Java) → "Token Sidejacking" — bind the token to a per-session user-context fingerprint.**
  - RULE: mint a random fingerprint, send the raw value in a hardened cookie, and store only its SHA-256 inside the JWT; verify both on each request.
  - ANTI-PATTERN: a bearer JWT with no binding to the client/session context.
  - SYMPTOM: a stolen/leaked token is fully usable from the attacker's browser; no way to detect replay.

- **JWT (Java) → "No Built-In Token Revocation by the User" — keep a server-side denylist.**
  - RULE: maintain a revocation denylist (e.g. SHA-256 digest of the token + revocation date) so logout / compromise can invalidate a token before its `exp`.
  - ANTI-PATTERN: relying only on `exp`; "logout" that just drops the client copy.
  - SYMPTOM: a stolen token stays valid until natural expiry; user "logout" doesn't actually kill access. (Keycloak's server-side analog is session/token revocation + token introspection — see [[introspection-revocation]].)

- **JWT (Java) → "Weak Token Secret" — HMAC secret ≥ ~64 random chars from a CSPRNG.**
  - RULE: for HS* tokens, use a long high-entropy secret from a cryptographically secure source.
  - ANTI-PATTERN: short / human-memorable / guessable signing secret.
  - SYMPTOM: offline brute-force or dictionary attack recovers the key; attacker forges valid tokens at will.

- **JWT (Java) → "Token Information Disclosure" — claims are only Base64, not secret.**
  - RULE: don't put sensitive data in a signed-only JWT; if confidentiality is needed, encrypt the payload (e.g. AES-GCM / JWE).
  - ANTI-PATTERN: stuffing roles, internal IDs, PII into a plain (signed, unencrypted) JWT.
  - SYMPTOM: anyone Base64-decodes the token and reads roles / architecture / PII from the browser or logs.

- **(inferred) `exp` / lifetime is necessary but not sufficient.**
  - RULE: always validate `exp` (and issuer/audience per the relying-party rules in the Authentication sheet — validate `iss`, `aud`, signature against JWKS, `exp`), but pair short lifetimes with the denylist + fingerprint above, since signature+`exp` alone can't detect theft or force logout.
  - ANTI-PATTERN: long-lived JWTs with no revocation and no binding, "because they're signed."
  - SYMPTOM: large post-theft attack window; no logout/revocation path. (See [[jwt-validation-pitfalls]], [[rfc9068]] for the JWT access-token profile.)

## cors-for-spa

- **(thin in these sheets) Cross-origin guidance here is cookie-scope, not `Access-Control-*` headers.**
  - RULE: the Session-Mgmt sheet's "Domain and Path Attributes" + "SameSite" sections are its cross-site story — keep cookies host-scoped (`__Host-`, no broad `Domain`) and `SameSite`d so they never ride to another origin. The detailed `Access-Control-Allow-Origin` allow-list / no-wildcard-with-credentials / no-origin-reflection rules live in OWASP's CORS guidance and [[owasp-asvs]] V14.5.3 — cited there, not duplicated here.
  - ANTI-PATTERN: treating SameSite/`Domain` as a substitute for a correct CORS allow-list on the API (or vice-versa).
  - SYMPTOM: either a CSRF gap (cookie too loosely scoped) or a CORS data-theft gap (wildcard/reflected ACAO on a credentialed route) — the two are complementary controls. (See [[cors-for-spa]], [[owasp-asvs]].)

- **JWT (Java) → "Token Storage on the Client Side" — Bearer-header SPAs sidestep cookie-CSRF but inherit the CORS preflight + XSS surface.**
  - RULE: a SPA sending the JWT in an `Authorization: Bearer` header (not a cookie) is not auto-sent cross-site, so it avoids classic CSRF — but the cross-origin call still requires a correct CORS allow-list, and the token is now reachable by XSS (hence CSP).
  - ANTI-PATTERN: assuming "we use Bearer headers, so CORS/XSS don't matter."
  - SYMPTOM: CORS preflight failures on the API, and XSS-driven token exfiltration if CSP is weak.

## Contradictions / caveats

- **Token storage — the two sheets disagree (ambiguous).** The *Session Management* sheet says do **not** put session tokens/JWTs in `localStorage` **or** `sessionStorage` (both JS-readable → XSS-exfiltratable), preferring a secured `HttpOnly` cookie. The *JWT for Java* sheet recommends `sessionStorage` + `Authorization` header (hardened with CSP) as a pragmatic SPA pattern. Resolution for RHBK SPAs: prefer the BFF / `HttpOnly`-cookie model (see [[curity-bff]], [[token-storage-browser]]); if a public SPA must hold the token, treat the JWT-sheet `sessionStorage`+CSP+short-lifetime+rotation as the minimum-bar fallback, never the default. ASVS V3.2.3 permits `sessionStorage` as a *secured* location, splitting the difference.
- **Not numbered clauses.** OWASP cheat sheets are best-practice guidance, not a normative numbered standard — anchors above are heading names, not clause numbers. For numbered requirements use [[owasp-asvs]] (ASVS V3.x/V14.x) or the IETF RFCs.
- **Authentication sheet is largely a hub here.** It defers token storage, CSRF `state`, algorithm validation, and CORS to the Session-Mgmt / JWT / CORS sheets; its own load-bearing contribution is the relying-party ID-token checks (`iss`, `aud`, signature-vs-JWKS, `exp`) and TLS-only transmission.
- **Upstream tier.** All of the above is `web:` (upstream/community best practice), not Red Hat ground truth — for what RHBK supports/enforces, defer to `kb:`/`guide:`/`ref:` sources.
