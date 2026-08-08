---
title: CORS for SPA OAuth Clients
type: entity
domain: keycloak
slug: cors-for-spa
summary: "Defines what CORS headers an authorization server must emit for browser-based OAuth clients, and what CORS policy a resource server or BFF must enforce to prevent cross-origin data theft while still allowing legitimate SPA fetch calls."
sources:
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (draft-ietf-oauth-browser-based-apps-26, fetched 2026-06-17)
  - web:https://owasp.org/www-project-application-security-verification-standard/ (OWASP ASVS 4.0.3, fetched 2026-06-18)
  - web:https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html (OWASP Cheat Sheet Series, fetched 2026-06-18)
provenance_extracted: 12
provenance_inferred: 4
provenance_ambiguous: 0
tags: [clients, security, concept]
symptoms:
  - "blocked by CORS policy"
  - "No 'Access-Control-Allow-Origin' header"
status: reviewed
updated: 2026-07-02
graph_community: "Tokens & Sessions"
---

# CORS for SPA OAuth Clients

**The set of CORS header requirements that an authorization server must satisfy to permit browser-based token requests, and the complementary allow-list policy that every resource server or BFF must enforce on credentialed API calls.**

## Rule

### Authorization server endpoints

The AS must send correct `Access-Control-Allow-Origin` headers on every endpoint a browser-based OAuth client calls directly: the token endpoint, and wherever provided — discovery (`/.well-known/openid-configuration`), JWKS, revocation, introspection, and UserInfo (§6.3.3.4 of draft-ietf-oauth-browser-based-apps-26). Without these, the browser blocks the code-for-token exchange before it reaches the AS.

### Resource server / API allow-list

`Access-Control-Allow-Origin` must be drawn from a strict allow-list of trusted domains validated against the request `Origin`; the `null` origin must never be allowed (ASVS V14.5.3). ASVS 5.0 tightens this: the header is either a fixed application value or the `Origin` is validated against an allowlist.

Wildcard (`*`) and `Allow-Credentials: true` are mutually exclusive at the browser level — the browser hard-rejects that combination. A cookie-bearing or Authorization-carrying SPA must therefore receive a specific, allow-listed origin (ASVS V14.5.3).

**Origin reflection is forbidden (inferred from ASVS V14.5.3 intent).** Echoing the request `Origin` verbatim into `Access-Control-Allow-Origin` (especially combined with `Allow-Credentials: true`) lets any attacker page perform a credentialed cross-origin read.

### BFF CSRF layer (inferred cross-spec)

Where a BFF fronts the SPA, CORS policy is the first of three complementary CSRF defenses (§6.1.3.3): SameSite cookie attributes, CORS preflights, and/or explicit anti-forgery tokens. A custom request header (e.g. `My-Static-Header: 1`) forces even simple cross-origin reads through a preflight that the browser then blocks for unknown origins (§6.1.3.3.2). Deploying the BFF same-origin as the SPA avoids the problem entirely (§6.1.3.3.2).

`SameSite=Strict` alone is insufficient when the BFF shares an eTLD+1 with sibling apps (§6.1.3.3.1) — a subdomain compromise makes same-site and same-origin equivalent.

### Origin header is not authentication

The `Origin` request header is trivially spoofed by non-browser clients. It must never be used as a credential or access-control gate; it supplements, but does not replace, real authentication and CSRF defenses (ASVS V14.5.3).

## Anti-pattern

1. Token endpoint with no CORS headers — a common misconfiguration on proxied or split-domain AS deployments where the CORS middleware does not explicitly add the OAuth endpoints.
2. `Access-Control-Allow-Origin: *` on any credentialed endpoint (cookie or Authorization header). Teams cargo-cult this from public CDN configurations where credentials are absent.
3. Reflecting the incoming `Origin` verbatim — typically implemented as a "convenient" dynamic CORS helper that never actually validates the origin against an allowlist.
4. Whitelisting `null` origin for local dev, then forgetting to remove it before production. Sandboxed iframes and `file://` contexts send `null` and would then gain credentialed read access.
5. Cookie-auth BFF with no explicit CSRF control beyond `SameSite=Strict`, relying on cookie scope alone on a shared subdomain (§6.1.3.3.1).
6. Treating Bearer-header flows as CORS-exempt — the `Authorization` header is not auto-sent cross-origin, so there is no cookie-CSRF risk, but the cross-origin call still requires a correct CORS allow-list on the API (inferred from owasp-cheatsheets cors-for-spa section).

## Symptom

| Failure | Observable error |
|---|---|
| AS token endpoint missing CORS headers | Browser console: "No 'Access-Control-Allow-Origin' header is present on the requested resource"; code-for-token exchange never completes; the SPA appears to hang at the redirect callback |
| Wildcard ACAO + `Allow-Credentials: true` | Browser blocks the response: "The value of the 'Access-Control-Allow-Origin' header … must not be the wildcard '\*' when the request's credentials mode is 'include'" |
| Origin reflection | CORS scanner reports ACAO mirrors arbitrary attacker origin; credentialed cross-origin data reads succeed from attacker-controlled pages |
| `null` origin allowed | Sandboxed iframe or `file://` page completes a credentialed API read; pentest flags `null` in allow-list |
| BFF no CSRF control | Simple-form cross-origin request rides the session cookie without hitting a preflight; state-changing CSRF succeeds |

## Surface (client vs backend)

**Client (SPA / browser)** — the browser enforces the same-origin policy automatically; the SPA has no direct control over CORS. The client's obligations are: (a) send a custom header (e.g. `X-Requested-With` or any non-CORS-safelisted header) on BFF API calls to guarantee a preflight; (b) not assume Bearer-header flows are free of CORS policy on the API side.

**Authorization server (backend)** — must emit `Access-Control-Allow-Origin` (and `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` as needed) on the token endpoint and all other AS endpoints callable from a browser. This is entirely a server-side configuration responsibility.

**Resource server / API (backend)** — owns the CORS allow-list for API calls. Must validate incoming `Origin` against an explicit allowlist, never reflect verbatim, never use wildcard with credentials. If fronted by a BFF that proxies all requests, the resource server may restrict CORS to the BFF's server-to-server calls only (i.e. no browser-direct calls), hardening the surface further.

**BFF (backend)** — is both a resource server (toward the SPA) and an OAuth client (toward the AS). Its CORS policy covers the SPA-to-BFF leg only; it must also enforce the three-layer CSRF defense (SameSite + CORS preflight trigger + anti-forgery token) and the outbound request allowlist (§6.1.3.6) to prevent token forwarding to attacker hosts.

## Contradictions / caveats

- The OWASP Cheat Sheets provide no detailed `Access-Control-Allow-Origin` allow-list guidance of their own — they defer explicitly to ASVS V14.5.3. The cheat-sheet CORS material here covers cookie-scope vs CORS as complementary controls and the Bearer-header/CSRF interaction; the allow-list rules are ASVS-sourced.
- ASVS 4.0.3 and 5.0 both address this area but with different numbering. The 4.0.3 clause V14.5.3 is the stable, widely-cited reference; ASVS 5.0 rewording is noted inline where it tightens the rule.
- This page covers upstream/community best practice (web: tier). For what Keycloak/RHBK configures and enforces by default on its token endpoint, see [[securing-apps-oidc-saml]] and the RHBK server-configuration guides.

## See also

- [[bff-token-handler]] — BFF architecture, session-cookie attributes, CSRF defense layers, outbound request allowlist
- [[token-storage-browser]] — why tokens must not reach the SPA at all in high-security deployments, removing the CORS exposure on the resource-server leg
- [[state-and-nonce]] — `state` parameter as the complementary anti-CSRF control at the OAuth redirect layer
- [[pkce]] — PKCE as the primary public-client code-injection defense (orthogonal to CORS but part of the same SPA hardening set)
- [[redirect-uri-validation]] — validates the endpoint the AS redirects back to; pairs with CORS on the AS side
- [[oidc-client-best-practices]] — RHBK-specific SPA client hardening
- [[securing-apps-oidc-saml]] — RHBK adapter and JS client configuration
- [[client-libraries-by-stack]] — per-stack client library choices that affect how CORS calls are made
- [[dpop]] — sender-constraining as an alternative mitigation when CORS alone cannot prevent token exfiltration
- [[bearer-token-usage]] — how `Authorization: Bearer` interacts with CORS preflight requirements
- [[fapi2-security-profile]] — higher-assurance profile that builds on these baseline controls
- [[sso-implementation-review]] — MOC: implementation review checklist
