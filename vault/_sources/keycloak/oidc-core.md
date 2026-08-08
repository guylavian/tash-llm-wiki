---
source: OpenID Connect Core 1.0
url: https://openid.net/specs/openid-connect-core-1_0.html
fetched: 2026-06-17
status: OIDF final (errata set)
feeds: [state-and-nonce, redirect-uri-validation]
---

# OpenID Connect Core 1.0 (raw staging note)

Distilled load-bearing requirements, grouped by the wiki concept they feed. Each bullet: RULE (+ section) / ANTI-PATTERN / SYMPTOM. Paraphrased tightly (no verbatim spec text — copyright).

## state-and-nonce

### nonce
- RULE (§3.1.2.1 / §3.2.2.1 / §3.3.2.1): `nonce` is OPTIONAL in the auth-code flow, but REQUIRED in the implicit flow and for hybrid `response_type=code id_token` / `code id_token token` (OPTIONAL only for hybrid `code token`). ANTI-PATTERN: omitting `nonce` whenever an ID Token comes back from the authorization endpoint. SYMPTOM: AS rejects the request, or (lax AS) an unbound ID Token that can be replayed/injected.
- RULE (§2, ID Token): when a `nonce` was sent, the AS MUST echo it as the `nonce` Claim in the ID Token; value is a case-sensitive string. ANTI-PATTERN: AS drops or alters the nonce. SYMPTOM: client-side nonce check fails -> login error / "nonce mismatch".
- RULE (§3.1.3.7 step 11 / §3.2.2.11): client MUST verify the ID Token `nonce` equals the value it sent; client SHOULD also check it for replay (method is client-specific). ANTI-PATTERN: ignoring the returned nonce, or reusing a static/predictable nonce. SYMPTOM: ID-token replay / cross-session injection -> wrong-subject login, no error surfaced.
- RULE (§15.5.2 nonce implementation notes): nonce SHOULD carry sufficient entropy (e.g. derived from a high-entropy per-session secret) so it is unguessable and binds to the browser session. ANTI-PATTERN: counter / timestamp / low-entropy nonce. SYMPTOM: attacker predicts nonce, defeats replay protection.
- RULE (purpose, §2 + §15.5.2): nonce associates a client session with the ID Token and mitigates replay; it is the OIDC-layer binding (distinct from OAuth `state`). ANTI-PATTERN: treating `state` as a substitute for `nonce` for ID-token binding. SYMPTOM: CSRF covered but ID-token replay still open.

### state
- RULE (§3.1.2.1): `state` is RECOMMENDED — an opaque value to maintain state between request and callback; CSRF mitigation is typically done by cryptographically binding `state` to a browser cookie. ANTI-PATTERN: no `state`, or a `state` not bound to the user agent. SYMPTOM: login CSRF / session fixation — victim lands in attacker's session.
- RULE (§3.2.2.5, implicit response; same expectation across flows): if `state` was in the request it is REQUIRED in the response, and the client MUST verify the returned `state` equals the value it sent. ANTI-PATTERN: client doesn't compare returned `state`. SYMPTOM: forged callback accepted; `state`-swap / CSRF goes undetected.

## redirect-uri-validation
- RULE (§3.1.2.1 / §3.2.2.1): `redirect_uri` is REQUIRED in the authentication request and MUST exactly match one of the Client's pre-registered Redirection URIs, using RFC 3986 §6.2.1 Simple String Comparison. ANTI-PATTERN: prefix/substring/wildcard/regex matching, or accepting an unregistered URI. SYMPTOM: code/token delivered to attacker URI; `redirect_uri_mismatch` / `invalid_redirect_uri` once tightened.
- RULE (§3.1.2.1, auth-code flow scheme): redirect URI SHOULD use `https`; MAY use `http` only for a confidential client, or a native app using `http` with `localhost`/loopback. ANTI-PATTERN: `http://` redirect for a public/web client. SYMPTOM: code/token interception on the wire; registration rejected when enforced.
- RULE (§3.2.2.1, implicit flow scheme): redirect URI MUST NOT use `http` unless the client is a native app (loopback). ANTI-PATTERN: `http` redirect with `response_type` returning tokens in the fragment. SYMPTOM: access-token leak over cleartext.
- RULE (§3.1.2.6, error response): if the redirect URI is missing/invalid/mismatched, the AS MUST NOT redirect the user agent to it — it must show/return the error without honoring the bad URI. ANTI-PATTERN: bouncing the browser to the unvalidated `redirect_uri` to "report" the error. SYMPTOM: open-redirect / error-channel leakage to an attacker domain.

## NOTES / scope
- §15.5.2 (nonce implementation notes) is the canonical home for nonce entropy/replay guidance; §3.x.3.7 / §3.x.2.11 give the per-flow ID-Token validation steps that include the nonce check.
- This is an upstream OIDF spec (web: tier), not RHBK ground truth — use to enrich best-practice; defer to RHBK `kb:`/`guide:`/`ref:` sources for what RHBK actually enforces. Keycloak/RHBK implements exact `redirect_uri` matching (with documented wildcard caveats of its own) and emits/validates `nonce` and `state`; cross-check specifics against the RHBK corpus when answering support questions.
- Broader OAuth-layer CSRF / redirect hardening (PKCE-as-CSRF, open-redirector ban, loopback variable-port rule) lives in RFC 9700 — see [[../_sources/rfc9700.md]] feeds for `state-and-nonce` and `redirect-uri-validation`; this note is the OIDC-specific `nonce` binding layer on top.
