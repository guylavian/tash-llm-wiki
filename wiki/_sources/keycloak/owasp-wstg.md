---
source: OWASP WSTG — Authentication/Session/OIDC test cases
url: https://owasp.org/www-project-web-security-testing-guide/
fetched: 2026-06-18
status: OWASP WSTG
feeds: [jwt-validation-pitfalls, state-and-nonce]
---

<!-- Test IDs follow the WSTG "latest" scheme.
     JWT:          WSTG-SESS-10 (Testing JSON Web Tokens)
     OAuth/state:  WSTG-AUTHZ-05.1 (Testing for OAuth Authorization Server Weaknesses)
     OAuth client: WSTG-AUTHZ-05.2 (Testing for OAuth Client Weaknesses)
     CSRF:         WSTG-SESS-05 (Testing for Cross Site Request Forgery)
     All under: latest/4-Web_Application_Security_Testing/
     Paraphrased tightly — see the pages for full test method. -->

## jwt-validation-pitfalls

Source: WSTG-SESS-10 "Testing JSON Web Tokens"
(latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/10-Testing_JSON_Web_Tokens)

- **WSTG-SESS-10 — reject `alg: none`.**
  - RULE: only accept the explicitly-configured signing algorithm(s); never honor the `none` ("unsecured JWT") algorithm.
  - ANTI-PATTERN: library treats a `none`-algorithm token as a valid, already-verified token; also case-trick bypasses like `NoNe`/`nOnE`.
  - SYMPTOM: a token with tampered payload and an empty signature (header.payload + trailing dot, no third segment) is accepted; claims like `admin:true` / `sub` swap take effect with no verification error.

- **WSTG-SESS-10 — verify the signature, do not merely decode.**
  - RULE: cryptographically verify the signature before trusting any claim (use `verify`, not `decode`).
  - ANTI-PATTERN: calling a decode-only path (e.g. Node `jwt.decode()` instead of `jwt.verify()`) that returns claims without checking the signature.
  - SYMPTOM: editing only the payload (header + signature unchanged) is accepted; forged claims processed; no "signature invalid" rejection.

- **WSTG-SESS-10 — pin the algorithm; reject header-driven algorithm choice (RS256→HS256 confusion).**
  - RULE: when the token is expected to use an asymmetric alg (`RSxxx`/`ESxxx`), enforce that; do not let the untrusted `alg` header pick the verification key/algorithm.
  - ANTI-PATTERN: verifier reads `alg` from the header and, on `HS256`, uses the RSA *public* key as the HMAC secret — the public key is attacker-knowable (TLS cert, or `/.well-known/jwks.json`).
  - SYMPTOM: attacker re-signs a modified token with `alg:HS256` using the public key as the HMAC secret and the server accepts it — full forgery / auth bypass.

- **WSTG-SESS-10 — ECDSA "Psychic Signatures" (CVE-2022-21449).**
  - RULE: Java versions 15–18 had a critical ECDSA verification bug; apply patches or avoid those JVM versions for ES256 token validation.
  - ANTI-PATTERN: running unpatched Java 15–18 for ES256/ES384/ES512 verification.
  - SYMPTOM: a forged ES256 token containing the hardcoded signature value `MAYCAQACAQA` is accepted by the verifier; any payload passes without a valid signature.

- **WSTG-SESS-10 — use a strong, unique HMAC secret.**
  - RULE: HMAC-signed tokens require a high-entropy, unique secret (not a default/short/dictionary value).
  - ANTI-PATTERN: weak, default, or shared signing key shipped with off-the-shelf software.
  - SYMPTOM: a captured JWT is cracked offline (Hashcat / John / `crackjwt.py`); attacker then forges arbitrary valid tokens at will.

- **WSTG-SESS-10 — sanitize the `kid` header (path traversal).**
  - RULE: validate/canonicalize the `kid` parameter before using it to locate a key file; never feed it raw into a filesystem path.
  - ANTI-PATTERN: building a key path directly from `kid`, allowing `../../../../dev/null` (or `nul`) to point at a predictable/empty file.
  - SYMPTOM: attacker sets `kid` to a path-traversal target with known/empty contents, signs with the empty string, and the forged token verifies.

- **WSTG-SESS-10 — sanitize the `kid` header (SQL/command injection).**
  - RULE: retrieve keys by `kid` using parameterized queries; never concatenate `kid` into SQL or shell commands.
  - ANTI-PATTERN: `SELECT key FROM keys WHERE kid='<raw_kid>'` style string concatenation.
  - SYMPTOM: injecting a `UNION SELECT 'attacker-key'--` style `kid` makes the DB return an attacker-known key; token forged and accepted.

- **WSTG-SESS-10 — reject attacker-provided public keys (JWK injection).**
  - RULE: validate signing keys against a trusted, server-side allow-list; never accept keys embedded in the JWT header via the `jwk` parameter.
  - ANTI-PATTERN: using the `jwk` header field's key material to verify the same token — lets the attacker supply and use their own key.
  - SYMPTOM: token signed with attacker's own key pair, with that key embedded in the `jwk` header, is accepted as fully verified.

- **WSTG-SESS-10 — validate `exp` (and reasonable token lifetime).**
  - RULE: check the `exp` claim against current time; reject expired tokens; keep lifetimes short.
  - ANTI-PATTERN: decoding without comparing `exp` to "now"; ignoring `nbf`/`iat`.
  - SYMPTOM: a long-expired but legitimately-issued token is replayed and still accepted.

- **WSTG-SESS-10 — no sensitive data in the payload; transmit/store securely.**
  - RULE: payload is not encrypted by default — keep secrets/PII out of it; send only over HTTPS; if cookie-stored, set `HttpOnly`/`Secure`/`SameSite`.
  - ANTI-PATTERN: passwords/PAN/SSN in claims; JWT over plain HTTP; cookie without `HttpOnly`/`Secure`.
  - SYMPTOM: base64-decoding the payload reveals plaintext secrets; token captured on the wire / readable from `document.cookie`, then replayed.

## state-and-nonce

Sources: WSTG-AUTHZ-05.1 "Testing for OAuth Authorization Server Weaknesses" (4.5.5.1),
WSTG-AUTHZ-05.2 "Testing for OAuth Client Weaknesses" (4.5.5.2),
WSTG-SESS-05 "Testing for Cross Site Request Forgery"
(latest/4-Web_Application_Security_Testing/05-Authorization_Testing/05.1-Testing_for_OAuth_Authorization_Server_Weaknesses
; .../05.2-Testing_for_OAuth_Client_Weaknesses
; .../06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery)

- **WSTG-AUTHZ-05.1 — `state` must exist, be unguessable, be session-bound, and be validated on callback.**
  - RULE: the OAuth `state` is the CSRF defense for the authorization-code flow — present on the request, cryptographically unguessable, tied to the user-agent/session, and matched on the redirect-back before any token exchange.
  - ANTI-PATTERN: missing/optional `state`; predictable or reused value; callback accepted without comparing returned `state` to the one issued; `state` not bound to the originating session.
  - SYMPTOM: forged consent / CSRF — e.g. `POST /u/consent?state=Tampered_State` is accepted; an arbitrary client gains access on the victim's behalf (login-CSRF / authorization-code injection → account takeover).

- **WSTG-AUTHZ-05.1 — OIDC `nonce` binds the ID token to the auth request (replay defense).**
  - RULE: in OpenID Connect, include `nonce` in the authorization request and verify the same `nonce` is present in the returned ID token.
  - ANTI-PATTERN: omitting `nonce`; not checking the ID token's `nonce` claim; `nonce` not tied to the specific authentication session.
  - SYMPTOM: an ID token from an earlier flow is replayed to assume another user's identity because nothing binds the token to this request.

- **WSTG-AUTHZ-05.1 — authorization code must be single-use and context-bound (code injection).**
  - RULE: a code is one-time and must match its originating `client_id`, `redirect_uri`, and session/`state`; the consent page must validate `state` before granting.
  - ANTI-PATTERN: accepting a code for a different `client_id`/`redirect_uri`, replaying a code, or honoring a tampered/missing `state` at consent.
  - SYMPTOM: tests "send a valid code for another client_id / another resource owner / resend the code" return an `access_token` — code injection / account takeover.

- **WSTG-AUTHZ-05.1 — strict `redirect_uri` allow-listing.**
  - RULE: validate `redirect_uri` against an exact pre-registered allow-list; reject substring/wildcard/encoding bypasses.
  - ANTI-PATTERN: accepting an arbitrary `redirect_uri`, or partial/wildcard matching that lets attacker domains through.
  - SYMPTOM: AS redirects the user-agent (and the code) to `redirect_uri=...attacker.example.com...` — credential/code theft.

- **WSTG-AUTHZ-05.1 — enforce PKCE; validate `code_verifier` at token exchange.**
  - RULE: the authorization server must verify the `code_verifier` against the stored `code_challenge` at token exchange; reject requests missing or mismatching the verifier.
  - ANTI-PATTERN: token endpoint accepts requests with omitted or forged `code_verifier`; AS allows PKCE downgrade (accepting flow without challenge).
  - SYMPTOM: `POST /oauth/token` with no `code_verifier` succeeds; public client code interception attack is viable.

- **WSTG-AUTHZ-05.2 — client must validate `state` on the callback (client-side enforcement).**
  - RULE: the OAuth client must compare the `state` returned in the redirect against the value it originally issued; mismatch must abort the flow and discard the code.
  - ANTI-PATTERN: client ignores returned `state`; treats any redirect to the callback URI as legitimate regardless of `state` value.
  - SYMPTOM: attacker injects an authorization response for a victim's session; client processes the attacker's code without detecting the mismatch.

- **WSTG-AUTHZ-05.2 — tokens must not be stored in localStorage (public clients).**
  - RULE: public clients (SPAs) must store tokens in `sessionStorage` or `HttpOnly` cookies; never in `localStorage`.
  - ANTI-PATTERN: storing access tokens or refresh tokens in `localStorage` where any same-origin JS can read them.
  - SYMPTOM: tokens visible under DevTools → Application → Local Storage; persistent across sessions; fully exfiltrable via XSS.

- **WSTG-AUTHZ-05.2 — client secrets must not appear in client-side code.**
  - RULE: public clients cannot keep secrets; `client_secret` must not be embedded in JavaScript, native app binaries, or any browser-accessible resource.
  - ANTI-PATTERN: `client_secret` hardcoded in SPA source or URI parameters; discoverable via browser DevTools debugger search.
  - SYMPTOM: `client_secret` retrievable from minified JS or source map; allows attacker to impersonate the client application.

- **WSTG-SESS-05 — an unpredictable, session-bound anti-CSRF token is required (the `state` is this token for OAuth).**
  - RULE: state-changing requests need a per-request/per-session, cryptographically unpredictable token, bound to the user's session and validated server-side — browsers auto-send cookies, so cookie-presence alone is not proof of intent.
  - ANTI-PATTERN: relying solely on the session cookie; static/predictable token; accepting a request with the token missing or unvalidated.
  - SYMPTOM: a crafted cross-site request (image/form/link) executes with the victim's cookie; CSRF finding. (GET is trivially abusable; POST is auto-submittable via JS — POST alone is not protection.)

- **WSTG-SESS-05 — `SameSite` cookies complement, but do not replace, the anti-CSRF token.**
  - RULE: set `SameSite` (Lax/Strict) on session cookies to limit cross-site transmission, alongside the token defense.
  - ANTI-PATTERN: no `SameSite`; or `SameSite=None` without `Secure` and without a token defense.
  - SYMPTOM: cross-site-initiated request still carries the session cookie; CSRF possible where token validation is absent.
