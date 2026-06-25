---
title: Redirect URI Validation
type: entity
domain: keycloak
slug: redirect-uri-validation
summary: "The authorization server must match every redirect_uri against pre-registered values using exact string comparison; any looser matching (prefix, wildcard, regex) creates an open-redirect that allows auth-code or token exfiltration to an attacker-controlled URI."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-17)
  - web:https://www.rfc-editor.org/rfc/rfc9700 (RFC 9700 OAuth Security BCP, fetched 2026-06-17)
  - web:https://openid.net/specs/openid-connect-core-1_0.html (OIDC Core 1.0, fetched 2026-06-17)
provenance_extracted: 14
provenance_inferred: 4
provenance_ambiguous: 0
tags: [security, clients, anti-pattern]
status: reviewed
updated: 2026-06-17
---

# Redirect URI Validation

**The AS must validate every redirect_uri against a pre-registered allowlist using RFC 3986 §6.2.1 exact string comparison — no wildcards, no prefix matching, no runtime mutation.**

## Rule

All three upstream standards converge on the same requirement:

- **Exact string match required.** The AS must compare the `redirect_uri` submitted in the authorization request against every pre-registered URI using RFC 3986 §6.2.1 Simple String Comparison. This applies to scheme, host, port, path, and query string as a whole (OAuth 2.1 §4.1.1/§2.3.1; RFC 9700 §2.1/§4.1.3; OIDC Core §3.1.2.1/§3.2.2.1).
- **Pre-registration is mandatory.** The full URI, including path, must be registered before use. Open-ended registrations (e.g. `https://app.example.com/*`) are not conformant (OAuth 2.1 §2.3.1).
- **URI must be absolute, may carry a query component, must not carry a fragment.** Per-request data belongs in `state`, not in a dynamically varied URI (OAuth 2.1 §2.3).
- **On mismatch the AS must not redirect.** If the redirect URI is missing, invalid, or mismatched, the AS must show the error to the user rather than bouncing the browser to the unvalidated URI (OAuth 2.1 §2.3.5; OIDC Core §3.1.2.6). Redirecting to expose the error is itself an open-redirect.
- **No open redirectors anywhere.** Both clients and ASes must not expose endpoints that forward a browser to an arbitrary URI supplied in a query parameter (OAuth 2.1 §2.3.1/§7.12; RFC 9700 §2.1).
- **Scheme must be https for public/web clients.** OIDC Core §3.1.2.1 says the redirect URI should use `https`; `http` is only permitted for confidential clients or native apps on loopback. The implicit flow (§3.2.2.1) is stricter: `http` must not be used unless the client is a native loopback app.
- **Token request echo.** The `redirect_uri` included in the token endpoint request must be re-validated for exact match against the value used in the authorization request (OAuth 2.1 §10.2, inferred from the echo requirement). (inferred)
- **Loopback exception for native apps.** For `localhost`/loopback redirect URIs, the AS must allow a variable port — exact-match on everything except the port component (OAuth 2.1 §4.1.1; RFC 9700 §4.1.3). See [[native-app-oauth]].

## Anti-pattern

| Pattern | Why it fails |
|---|---|
| Registering `https://app.example.com/*` or host-only `https://app.example.com` | Any path on the host becomes valid; attacker chooses a path they control. |
| Prefix matching (URI starts with registered value) | Same exfiltration surface as wildcards. |
| Varying the `redirect_uri` per request with dynamic data in the path or query | Requires a loose registration to accommodate, which re-opens the attack surface. (inferred) |
| Bouncing to the unvalidated URI to report the error | Turns the error-reporting path into the exfiltration path. |
| Generic `?redirect=` / `?next=` forwarding endpoint on the client | Chains with a valid registered URI to exfiltrate the code. |
| Fixed loopback port in native-app registration | Intermittent failures when the OS assigns a different ephemeral port. |
| `http://` redirect for SPA or web-browser client | Code/token interceptable on the wire; blocked when AS enforces scheme. |

## Symptom

Observable faults when redirect URI validation is wrong or loose:

- **`invalid_redirect_uri`** (Keycloak error) or **`redirect_uri_mismatch`** — returned immediately when the AS enforces exact match but the submitted URI doesn't match. If the AS is lenient and you later tighten it, this error suddenly appears in production.
- **Authorization code or token delivered to an attacker-controlled URI** — the primary security consequence of loose matching; may surface as an account takeover incident rather than an error.
- **CVE-style auth-code theft / open-redirect security scanner finding** — pen-tests and SAST scanners flag wildcard or prefix registrations.
- **Open-redirect chaining** — a `?redirect=` endpoint on the app plus a legitimately registered URI lets an attacker route the code off-host, no AS misconfiguration required.
- **Intermittent `invalid_redirect_uri` for native app on loopback** — AS has a hardcoded port in the registration; breaks when the OS picks a different ephemeral port.
- **Code/token in Referer header leaking to third-party resources** — suppressing the Referer header (Referrer-Policy) is a companion mitigation (RFC 9700 §4.2.4); the symptom is code/state visible in server access logs of embedded resources. (inferred)

## Surface (client vs backend)

**Authorization server (backend):**
- Enforce exact RFC 3986 §6.2.1 string comparison on every authorization request and on the token-endpoint echo.
- Reject registrations containing wildcards, glob patterns, or host-only URIs.
- On mismatch: return an error page to the user, never redirect to the submitted URI.
- For loopback/localhost URIs: match on everything except the port (variable port allowed).
- Do not expose any endpoint that follows an arbitrary `?redirect=` or `?next=` parameter.

**Client (SPA / native / confidential):**
- Register all redirect URIs as precise, absolute URIs before deployment.
- Do not mutate the URI per-request; use `state` to carry per-request data (see [[state-and-nonce]]).
- For native apps, claim a reverse-domain URI scheme or use loopback; do not embed a fixed port. (see [[native-app-oauth]])
- Ensure no app endpoint acts as an open redirector that an attacker could chain after a legitimate registered URI.
- Use `https` for all non-loopback redirect URIs; for SPAs this is a hard requirement. (inferred)

## See also

- [[pkce]] — PKCE is the companion control that prevents a stolen code (exfiltrated via open-redirect) from being redeemed.
- [[state-and-nonce]] — `state` is the right place for per-request app context; do not vary the redirect URI instead.
- [[native-app-oauth]] — loopback / claimed-https / private-use-scheme options for native apps and the variable-port rule.
- [[oidc-client-best-practices]] — RHBK-specific client configuration guidance including redirect URI settings.
- [[securing-apps-oidc-saml]] — RHBK adapter-level redirect URI enforcement.
- [[oidc-grant-types]] — implicit flow removed in OAuth 2.1; its stricter redirect scheme requirements are noted above.
- [[oidc-endpoints]] — authorization endpoint is where the redirect URI is submitted and first validated.
- [[cors-for-spa]] — CORS and redirect URI validation are distinct controls; both apply to SPAs.
- [[issuer-identification-mixup]] — when multiple ASes are in play, a distinct redirect URI per issuer is one mitigation.
- [[fapi2-security-profile]] — FAPI profiles layer additional constraints on redirect URI registration.
- [[bearer-token-usage]] — query-string token transmission creates analogous exfiltration risk via logs/referrer.
- [[sso-implementation-review]] — MOC; this page feeds the redirect-URI validation check.
