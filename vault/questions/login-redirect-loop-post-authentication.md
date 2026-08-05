---
title: "Login redirect loop after successful authentication — browser bounces between Keycloak and app until 'Too Many Redirects'"
type: question
domain: keycloak
slug: login-redirect-loop-post-authentication
summary: "User enters correct credentials, Keycloak authenticates them and redirects to the app, but instead of loading the app, the browser endlessly loops between Keycloak and application until a 'Too Many Redirects' error. Covers six root causes: mismatched redirect URI, keycloak-js nonce after migration (kb:7125224), proxy scheme/hostname misconfiguration, SameSite cookie blocking, public-client-without-PKCE, and clock skew."
sources:
  - web:https://access.redhat.com/solutions/7125224 (RH KB Solution 7125224 — keycloak-js nonce redirect loop; gated, cited via _gated-kb-index.md)
  - web:https://access.redhat.com/solutions/7134938 (RH KB Solution 7134938 — Admin Console login redirect loop; gated, cited via _gated-kb-index.md)
  - guide:securing_applications_and_services_guide
  - ref:rhbk-26-0-migration-changes
  - ref:rhsso-7-4-openid-connect-3
  - ref:rhbk-26-6-javascript-adapter
  - ref:rhbk-26-6-single-cluster-introduction
  - ref:rhbk-26-2-assembly-managing-clients-server-administration-guide
  - ref:rhbk-26-0-red-hat-build-of-keycloak-26-0
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)
provenance:
  extracted: 6
  inferred: 6
  ambiguous: 0
question_tier: support-kb
status: draft
updated: 2026-07-09
graph_community: "Tokens & Sessions"
---

# Login redirect loop after successful authentication — browser bounces between Keycloak and app until "Too Many Redirects"

**User enters correct credentials on the Keycloak login page. Keycloak authenticates them and redirects the browser back to the application. Instead of loading the dashboard, the browser endlessly loops between Keycloak and the application until it crashes with a "Too Many Redirects" error.**

---

## The loop mechanics

The loop follows this pattern:

1. Browser → **Keycloak**: `GET /realms/{realm}/protocol/openid-connect/auth?...`
2. User logs in → Keycloak issues auth code, redirects browser to `redirect_uri`
3. Browser → **Application**: lands at the callback URL with the auth code
4. Application exchanges the code for tokens (or validates the response)
5. Application **does not recognize the authentication as valid** → redirects browser back to Keycloak (step 1)
6. Keycloak finds an existing SSO session → immediately redirects back (step 3) → **loop**

The root cause is **always** something that makes the application believe the user is not authenticated after every redirect back from Keycloak. The six most common causes, ranked by frequency, are below.

---

## Root cause H1: `Valid Redirect URIs` does not match the actual callback URL — MOST COMMON

The client configuration's `Valid Redirect URIs` must include the exact URL the browser is redirected to after authentication (`redirect_uri` parameter). If there's a mismatch — even a trailing slash, different port, or scheme — Keycloak's redirect URI enforcer rejects the callback, or the application's OIDC library rejects the token because `iss` or `aud` doesn't match its own base URL (`rhbk-26-2-assembly-managing-clients-server-administration-guide.md:51`).

**Common mismatch patterns:**
- Trailing slash: registered `https://app.example.com/`, redirects to `https://app.example.com` (no slash) — *fails*
- Port mismatch: registered `https://app.example.com:443/`, redirect hits `https://app.example.com/` — *fails*
- Scheme: registered `https://app.example.com/*`, reverse proxy terminates TLS → redirect arrives as `http://app.example.com/` — *fails*
- Path: registered `https://app.example.com/*`, app redirects to `https://app.example.com/callback` — *works* (wildcard catches subpaths)
- Query params: after RHBK 26, query params are **not** ignored when matching (`rhsso-7-4-release-changes.md:241-243`) — if the app adds unexpected query params, they must be in the registered URI or use a wildcard suffix

**Fix:** Check the exact `redirect_uri` the app sends in the auth request. Make sure it matches a `Valid Redirect URI` on the client. Use the browser DevTools Network tab to capture it.

---

## Root cause H2: `keycloak-js` adapter redirect loop after migration (kb:7125224) — common after RH-SSO → RHBK migration

The most documented gated-KB redirect loop (`_gated-kb-index.md:2866-2868`, kb:7125224). After migrating from RH-SSO to RHBK, the JavaScript adapter `keycloak-js` enters an endless authentication loop.

**Root cause:** RHBK 26 changed the `nonce` claim behavior. Per OIDC Core 1.0, `nonce` is now added only to the ID token (not to access/refresh tokens as before). Older versions of `keycloak-js` (pre-24.0.0) expected `nonce` in all tokens and fail validation when it's absent (`rhbk-26-0-migration-changes.md:324-329`). The adapter then re-initiates authentication → redirect loop.

**Fixes:**
1. **Upgrade `keycloak-js`** — use the adapter version matching the RHBK server version (26.x). `npm install @redhat/keycloak-js@latest` (`rhbk-26-0-upgrading-red-hat-build-of-keycloak-adapters.md:45`).
2. **If you must keep the old adapter:** add the **Nonce backwards compatible** protocol mapper to the client. Assign it via a client scope that the app uses (`rhbk-26-0-migration-changes.md:327-329`).

---

## Root cause H3: Proxy scheme/hostname misconfiguration — common behind ELB, nginx, HAProxy

Keycloak forms redirect URLs using the `Host` header it receives. Behind a reverse proxy that terminates TLS:
- If `proxy-headers` is not set (or set incorrectly), Keycloak sees an HTTP connection from the proxy and generates redirect URLs with `http://` — the app then rejects the callback because the scheme doesn't match *(inferred from RHBK proxy configuration guidance)*.
- If `--hostname` (or `KC_HOSTNAME`) is not set, Keycloak uses the inbound request's `Host` header, which may be the proxy's internal hostname rather than the public one *(inferred)*.
- If `--hostname-strict` is `true` and the `Host` header doesn't match the configured hostname, Keycloak rejects the request or generates wrong URLs *(inferred)*.

**Fix:**
```sh
kc.sh start --proxy-headers xforwarded --hostname https://sso.example.com
```
Or on the CR:
```yaml
spec:
  hostname: https://sso.example.com
  proxy:
    headers: xforwarded
```

Set `proxy-headers` to `forwarded`, `xforwarded`, or the precise header your proxy sends *(inferred)*. See [[reverse-proxy-configuration]] and [[hostname-v2]].

---

## Root cause H4: SameSite cookie blocking / insecure connection — common with `check-sso` / `checkLoginIframe`

The JavaScript adapter's session-status iframe reads a special SSO cookie to detect the login state. Starting with Chrome 80 (`rhsso-7-4-openid-connect-3.md:1631`), the iframe can only see this cookie over a **secure (HTTPS)** connection. If Keycloak is served over HTTP behind a proxy, Chrome blocks the cookie access → the iframe reports "not authenticated" → the adapter initiates a new auth flow → redirect loop.

Also affects `silentCheckSsoRedirectUri` — if the silent check fails because third-party cookies are blocked (ITP on Safari), the adapter falls back to a regular redirect, which can cause a visible loop (`rhsso-7-4-openid-connect-3.md:1707-1721`).

**Fixes:**
1. **Enable HTTPS on Keycloak.** Set `--https-certificate-file` and ensure the public URL is HTTPS.
2. **Disable the status iframe** if HTTPS is impossible: `keycloak.init({ checkLoginIframe: false })`.
3. **Configure `silentCheckSsoFallback: false`** to prevent the fallback to regular redirect when third-party cookies are blocked (`rhsso-7-4-openid-connect-3.md:1715-1716`).
4. **Set the access token lifespan shorter** so the adapter detects logout sooner without the iframe.

---

## Root cause H5: Public client without PKCE — common with SPA apps

A public SPA client that does not use PKCE may fail the auth code exchange *(inferred)*. From RHBK 26, some configurations (especially with FAPI/OAuth 2.1 client policies) enforce PKCE. Without PKCE, the code exchange fails → no tokens returned → the adapter interprets this as a failure → re-initiates auth → loop.

**Fix:** Enable PKCE (S256) in the client adapter. For `keycloak-js`, ensure:
```javascript
keycloak.init({ pkceMethod: 'S256' })
```
And the client in the Admin Console has **Standard Flow Enabled** with no secret (public client).

---

## Root cause H6: Clock skew between servers

RHBK and the application server clocks are out of sync by more than the allowed skew window *(inferred)*. Tokens appear expired or not-yet-valid immediately after issuance. The application rejects the token → re-authenticates → loop.

**Fix:** Synchronize clocks (NTP) on all servers. Check the difference between Keycloak server, application server, and browser. If NTP is already in place, check the token `iat` vs `exp` in the JWT itself to confirm.

---

## Diagnostic checklist

1. **Capture the redirect_uri** — open browser DevTools Network tab, find the auth request to Keycloak, inspect the `redirect_uri` parameter. Verify it matches exactly a `Valid Redirect URI` on the client.
2. **Check the browser console** — errors like "Nonce not found", "Invalid token", "Session not active", or "SameSite cookie blocked" narrow the cause.
3. **Check Keycloak server logs** — look for `Invalid redirect_uri`, `Session not found`, or `Code exchange failed` errors.
4. **If behind a proxy:** verify `proxy-headers` and `--hostname`. Check the `Location` header in the redirect response — does it match the public URL? Is it HTTP or HTTPS?
5. **If after migration:** check the `keycloak-js` adapter version vs RHBK version. Add the Nonce backwards compatible mapper as a test.
6. **Enable adapter debug logs** — most OIDC client libraries have verbose logging; it usually shows exactly why it rejected the redirect.

## Contradictions / caveats

- The `nonce` redirect loop (H2) only applies when using the `keycloak-js` JavaScript adapter — it does not apply to confidential server-side clients or non-Keycloak OIDC libraries (inferred from kb:7125224's scope limitation to `keycloak-js`).
- The `checkLoginIframe` / SameSite issue (H4) only applies to the JS adapter's session-status iframe — it does not affect server-side adapter flows.
- Redirect loops that are **intermittent** (work sometimes, fail others) are more likely a session-affinity / Infinispan remote-lookup problem (see [[passthrough-roundrobin-login-loop]]) than any of the above.

## See also

- [[passthrough-roundrobin-login-loop]] — intermittent login loops from lost session affinity in a cluster
- [[reverse-proxy-configuration]] — proxy-headers and hostname settings
- [[hostname-v2]] — the hostname configuration model
- [[redirect-uri-validation]] — exact-match redirect URI best practice
- [[oidc-client-best-practices]] — writing the client integration code correctly
- [[securing-apps-oidc-saml]] — client types, public vs confidential
- [[dpop]] — sender-constrained tokens prevent token replay
- [[troubleshooting-index]] — triage map for other Keycloak issues
- [[admin-console-confidential-lockout]] — redirect loop in Admin Console specifically

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **kb:7125224** (gated) — Red Hat Build of Keycloak redirect loop due to missing `nonce` integrated with `keycloak-js` (endless loop after RH-SSO → RHBK migration).
- **kb:7134938** (gated) — Red Hat build of Keycloak Admin Console Login Redirect Loop (Admin Console login loop, related symptom).
- **rhbk-26-0-migration-changes.md:324-329** — Nonce claim change: now only in ID token per OIDC spec; backwards-compatible mapper available for old JS adapters.
- **rhbk-26-0-migration-changes.md:330-341** — Using older JS adapter with newer server requires `session_state` and `nonce` backwards-compatible mappers.
- **rhsso-7-4-openid-connect-3.md:1631** — Chrome 80: status iframe needs HTTPS; insecure connection → redirect to Keycloak every time.
- **rhsso-7-4-openid-connect-3.md:1707-1721** — Third-party cookie blocking: silent check-sso fallback to regular redirect; status iframe auto-disabled.
- **rhbk-26-2-assembly-managing-clients-server-administration-guide.md:51** — Valid Redirect URIs client configuration field.
- **rhbk-26-6-javascript-adapter.md:296** — `useNonce` option (default true) for cryptographic nonce verification.
- **rhbk-26-0-red-hat-build-of-keycloak-26-0.md:154-170** — Persistent user sessions (online sessions stored in DB) introduced.
- **rhsso-7-4-release-changes.md:241-243** — Query params no longer ignored in redirect URI matching.

### Wiki

- [[passthrough-roundrobin-login-loop]] — intermittent login loops from lost session affinity in cluster
- [[reverse-proxy-configuration]] — proxy-headers and hostname settings (not yet written — see `reference/`)
- [[hostname-v2]] — the hostname configuration model
- [[redirect-uri-validation]] — exact-match redirect URI best practice
- [[oidc-client-best-practices]] — writing the client integration code correctly
- [[securing-apps-oidc-saml]] — client types, public vs confidential
- [[dpop]] — sender-constrained tokens
- [[admin-console-confidential-lockout]] — redirect loop in Admin Console specifically
- [[troubleshooting-index]] — triage map

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[_ref-keycloak-securing_applications_and_services_guide|keycloak reference — securing_applications_and_services_guide]]
<!-- crosslink:end -->
