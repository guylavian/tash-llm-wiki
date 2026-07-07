---
title: State and Nonce Parameters
type: entity
domain: keycloak
slug: state-and-nonce
summary: "OAuth `state` prevents login CSRF by binding the authorization callback to the originating browser session; OIDC `nonce` additionally binds the returned ID Token to that same session, blocking replay and cross-session injection. Both must be validated on the client — omitting either leaves a distinct, exploitable gap."
sources:
  - web:https://openid.net/specs/openid-connect-core-1_0.html (OIDC Core 1.0, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-17)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (OWASP Cheat Sheets, fetched 2026-06-18)
  - web:https://owasp.org/www-project-web-security-testing-guide/ (OWASP WSTG, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
tags: [clients, security, concept]
status: reviewed
updated: 2026-06-18
---

# State and Nonce Parameters

**Two complementary anti-forgery parameters in the OAuth 2.0 / OIDC authorization flow: `state` defends against login CSRF at the OAuth layer; `nonce` defends against ID Token replay at the OIDC layer.**

## Rule

### `state` (OAuth layer — CSRF defense)

`state` is RECOMMENDED in OIDC Core 1.0 §3.1.2.1 for the authorization-code flow and mandatory in practice. It is an opaque, unpredictable value the client generates, sends in the authorization request, and then verifies on the redirect callback before exchanging the code. Cryptographically binding `state` to a server-side cookie or session ties it to the originating user agent (OIDC Core §3.1.2.1; RFC 9700 §2.1).

If the AS supports PKCE, RFC 9700 §4.7.1 permits a client to rely on PKCE for CSRF protection instead — but only after confirming PKCE support via AS metadata. When PKCE is absent or unconfirmed, one-time `state` tokens bound to the user agent MUST be used (RFC 9700 §2.1). Regardless, if `state` is sent in the request, it is REQUIRED in the response and the client MUST compare the returned value to the one it issued (OIDC Core §3.2.2.5; WSTG-AUTHZ-05.2).

If `state` also carries application state (e.g. the post-login return path), its integrity must be protected against tampering — sign or encrypt it (RFC 9700 §4.7.1). OWASP WSTG-SESS-05 reinforces that the `state` value is the anti-CSRF token for the OAuth flow: it must be cryptographically unpredictable, per-request, and session-bound.

### `nonce` (OIDC layer — ID Token replay defense)

`nonce` is OPTIONAL in the authorization-code flow, but REQUIRED in the implicit flow and in hybrid flows with `response_type=code id_token` or `code id_token token` (OIDC Core §3.1.2.1, §3.2.2.1, §3.3.2.1). It is a case-sensitive string the client generates per request.

When sent, the AS MUST echo the `nonce` value verbatim inside the ID Token (OIDC Core §2). The client MUST verify the returned `nonce` matches the one it sent and SHOULD check for replay (OIDC Core §3.1.3.7 step 11, §3.2.2.11, §15.5.2). The `nonce` SHOULD carry sufficient entropy that it is unguessable and serves as a per-session secret binding (OIDC Core §15.5.2).

RFC 9700 §2.1 notes that in OIDC flows the `nonce` parameter itself provides CSRF protection at the token level — it is a distinct, deeper guarantee than `state`.

`state` and `nonce` are complementary, not interchangeable (inferred): `state` protects the redirect leg (CSRF on the callback); `nonce` protects the ID Token itself (replay across sessions even after a valid redirect).

## Anti-pattern

**`state` anti-patterns:**
- Omitting `state` entirely, or generating it but not binding it to the originating session/cookie.
- Sending `state` but not comparing the returned value on the callback (treating any redirect to the callback URI as legitimate).
- Trusting unsigned `state` contents when the value carries application routing data.
- Assuming PKCE eliminates the need for `state` without first confirming AS PKCE support via discovery metadata (inferred from RFC 9700 §4.7.1).

**`nonce` anti-patterns:**
- Omitting `nonce` when an ID Token is returned from the authorization endpoint (implicit / hybrid flows).
- Using a counter, timestamp, or low-entropy value instead of a high-entropy per-session secret.
- Using a static or reused `nonce` across requests.
- Receiving the ID Token but skipping the `nonce` claim check.
- Treating `state` as a substitute for `nonce` — CSRF is covered but ID Token replay is still open.

## Symptom

**From `state` failures:**
- Login CSRF / session fixation: a victim is silently signed into an attacker-controlled account because the forged callback is accepted without `state` validation. Observable as an account-takeover or unexpected session after following a crafted link — no error is surfaced to the victim (WSTG-AUTHZ-05.1).
- `POST /u/consent?state=Tampered_State` is accepted; a third party gains access on the victim's behalf.
- A state-swap causes the app to return the user to a wrong route (if unsigned state carries the return path).

**From `nonce` failures:**
- An ID Token from an earlier authentication session is replayed to assume another user's identity — the app logs in the wrong user with no error (WSTG-AUTHZ-05.1).
- Cross-session injection: an attacker's flow produces an ID Token that is injected into the victim's callback; without the `nonce` check the client accepts it (RFC 9700 §2.1).
- If the AS rejects a missing `nonce` on a required flow: login fails immediately with an AS error.
- If the AS is lax and the client skips the check: silent wrong-subject login with no error code surfaced.

## Surface (client vs backend)

**Client (SPA / public client / browser):**
- Generate a cryptographically random `state` (and `nonce` for OIDC flows) on every authorization request.
- Store both values in a `HttpOnly` + `Secure` + `SameSite` session cookie or equivalent server-side session before the redirect — not in `localStorage` or plain JS variables that survive page load (inferred from OWASP Session-Mgmt + RFC 9700 §2.1).
- On the callback, before any token exchange: compare the returned `state` to the stored value and abort on mismatch; discard the code.
- After receiving the ID Token: compare the `nonce` claim to the stored value and abort on mismatch or absence.
- If relying on PKCE for CSRF instead of `state`: confirm AS PKCE support via authorization server metadata discovery before dropping `state` (RFC 9700 §4.7.1); see [[pkce]] and [[authorization-server-metadata-discovery]].

**Backend (confidential client / BFF):**
- A BFF (backend-for-frontend) pattern keeps `state`/`nonce` generation and validation server-side, so the values never traverse the browser — this is the recommended model for SPAs handling sensitive tokens (inferred; see [[bff-token-handler]]).
- For confidential clients the same generation + validation rules apply; the backend also enforces that each `state` value is single-use (destroyed on first use).
- The backend must not accept a callback without a valid matching `state`, even when the same user has concurrent sessions.

**AS / server side (for completeness):**
- The AS must echo `nonce` in the ID Token when received; it must not drop or alter it. This is an AS obligation outside the client's direct control but should be verified during integration testing.

## See also

- [[pkce]]
- [[redirect-uri-validation]]
- [[oidc-token-validation]]
- [[bff-token-handler]]
- [[token-storage-browser]]
- [[oidc-client-best-practices]]
- [[jwt-validation-pitfalls]]
- [[authorization-server-metadata-discovery]]
- [[issuer-identification-mixup]]
- [[oidc-grant-types]]
- [[oidc-endpoints]]
- [[securing-apps-oidc-saml]]
- [[fapi2-security-profile]]
- [[sso-implementation-review]]
