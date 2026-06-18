---
title: "Angular SPA + backend resource server on RHBK — best practice & the strongest signals it's built wrong"
type: question
domain: keycloak
slug: spa-resource-server-implementation-review
summary: "Applied instance of the SSO implementation-review lens: what a correct Angular-SPA-plus-resource-server integration against an RHBK realm looks like across both surfaces, and the concrete tickets that betray a wrong build."
sources:
  - guide:securing_applications_and_services_guide
  - guide:server_administration_guide
  - ref:securing-apps-oidc-saml.md
  - ref:server-administration.md
  - kb:oidc-layers-
  - kb:overview-
  - kb:javascript-adapter-
  - kb:assembly-managing-clients_server_administration_guide
  - kb:configuring-authentication_server_administration_guide
  - kb:dpop-
  - kb:authz-client-
  - kb:migrating-applications
  - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700 OAuth 2.0 Security BCP, fetched 2026-06-18)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html (Browser-Based Apps draft-26, fetched 2026-06-18)
  - web:https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-15.html (OAuth 2.1 draft-15, fetched 2026-06-18)
  - web:https://www.rfc-editor.org/rfc/rfc7636 (RFC 7636 PKCE, fetched 2026-06-18)
  - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Access Tokens, fetched 2026-06-18)
  - web:https://owasp.org/API-Security/editions/2023/en/0x11-t10/ (OWASP API Security Top 10 2023, fetched 2026-06-18)
provenance:
  extracted: 9
  inferred: 14
  ambiguous: 1
tags: [clients, tokens, security, concept]
status: draft
updated: 2026-06-18
---

# Angular SPA + backend resource server on RHBK — best practice & the strongest signals it's built wrong

**A correct build splits the work cleanly: the SPA is a *public* client that proves
possession of the auth code with PKCE and never holds a secret; the backend is a
*resource server* that independently re-validates every access token. Most "wrong"
builds collapse that split — the SPA stores tokens unsafely, or the backend trusts
tokens it never verified.** This is the [[sso-implementation-review]] lens applied to
this specific stack.

## Best practice — the SPA (browser, public client)

- **Public client + Authorization Code + PKCE (S256).** Client authentication **off**
  (no secret in the browser), Standard Flow **on**, Implicit Flow and Direct Access
  Grants **off** (kb: Ch.13 *Managing Clients*; the JS adapter chapter states a
  client-side app "has to be a public client"). PKCE is set on the client
  (`pkce.code.challenge.method=S256`). See [[pkce]], [[oidc-grant-types]],
  [[client-authentication-methods]].
- **Exact redirect URIs + web origins**, scoped to the app origin — RHBK's own JS
  adapter guidance says "be as specific as possible … failing to do so may result in
  a security vulnerability." No broad wildcards. See [[redirect-uri-validation]],
  [[cors-for-spa]].
- **Tokens in memory, never `localStorage`/`sessionStorage`.** Refresh proactively and
  single-flight; on `invalid_grant` force a clean re-login. See [[token-storage-browser]],
  [[refresh-token-rotation]], [[oidc-client-best-practices]].
- **Validate `state` and `nonce`** on the callback (login-CSRF + ID-token replay). See
  [[state-and-nonce]].
- **Logout** via the `end_session_endpoint` with `id_token_hint` +
  `post_logout_redirect_uri`; register **back-channel logout** so a server-side session
  kill actually invalidates the app. See [[rp-initiated-logout]], [[back-channel-logout]],
  [[oidc-logout]].
- **Discover endpoints** from `/.well-known/openid-configuration` rather than
  hard-coding them. See [[authorization-server-metadata-discovery]], [[oidc-endpoints]].
- **Hardening when the data warrants it:** DPoP sender-constraining (full feature in
  **RHBK 26.6**) so a stolen in-memory token is useless without the browser-held key
  ([[dpop-sender-constraining]], [[dpop]]); or move tokens out of the browser entirely
  with a **BFF / token handler** ([[bff-token-handler]]); or bind a Client Policy to an
  OAuth-2.1 / FAPI profile ([[fapi-oauth21-profiles]], [[fapi2-security-profile]]).

## Best practice — the backend (resource server)

- **Independently validate every access token** before granting access: verify the
  **signature against JWKS** (`jwks_uri`, cached + key-rotation aware) and check
  `iss`, `exp`, `nbf`. The SPA does **not** validate its own token; the RS does. See
  [[access-token-validation-resource-server]], [[oidc-token-validation]], [[jwt-validation-pitfalls]].
- **Audience + scope/role enforcement:** reject any token whose `aud` does not name
  this API; authorize from `resource_access[clientId].roles` / `realm_access.roles`.
  See [[audience-and-scope-checks]].
- **Bearer token in the `Authorization` header only**, over TLS, never in URLs or logs.
  See [[bearer-token-usage]].
- **Service-to-service** calls use the **client-credentials** grant from a *confidential*
  client, audience-scoped to the callee — never the SPA's user token replayed. See
  [[service-to-service-client-credentials]].
- Opaque-token deployments validate via **introspection** instead of local JWT checks
  ([[token-introspection]]); revoke at the **revocation endpoint** ([[token-revocation]]).

## Strongest signals it's built wrong (the tickets you'd actually see)

| Symptom / ticket | Most likely cause | Page |
|---|---|---|
| Tokens visible in DevTools → stolen via XSS | tokens in `localStorage`; no BFF | [[token-storage-browser]] |
| Client secret shipped in JS bundle | client not actually public (confidential config in a browser) | [[client-authentication-methods]] |
| Auth code intercepted / "code injection" | Implicit Flow on, or PKCE missing | [[pkce]] · [[oidc-grant-types]] |
| Open-redirect / token exfiltration after login | wildcard or loose `redirectUris` | [[redirect-uri-validation]] |
| CORS preflight 403 calling the API or token endpoint | web origins not scoped (or, wrongly, wildcarded) | [[cors-for-spa]] |
| "Logged out but the token still works" | access-token lifespan too long; only client-side logout; no back-channel logout | [[back-channel-logout]] · [[rp-initiated-logout]] |
| `invalid_grant` loops / refresh races | rotation reuse-detection firing; no single-flight refresh | [[refresh-token-rotation]] |
| RS accepts `alg=none` or wrong-key JWT | signature not verified against JWKS | [[jwt-validation-pitfalls]] |
| API accepts a token minted for a different client | no `aud` check (confused deputy / BOLA) | [[audience-and-scope-checks]] |
| SPA trusts the ID token to authorize API calls | RS must validate the **access** token, not the ID token | [[access-token-validation-resource-server]] |
| Refresh token never expires | session/idle lifespans misconfigured | [[tokens-and-sessions]] |

## Contradictions / caveats — RH ground-truth vs upstream (ambiguous)

- **Browser token storage.** RHBK's **Securing Applications and Services Guide**
  presents the **keycloak-js public client holding tokens in the browser** (in-memory)
  as the standard, fully-supported SPA pattern. The **upstream** IETF
  *browser-based-apps* draft-26 and OWASP hold that **no purely-browser token store is
  XSS-safe** and steer high-value apps to a **BFF**. This is a difference of
  *emphasis/recency*, not a correctness contradiction: RHBK is downstream of OSS
  Keycloak and the BBA spec is still a **work-in-progress Internet-Draft**. For a
  Red Hat **support** question, the public-client pattern is supported; for a
  **threat-model** question on high-value data, prefer the BFF (inferred). See
  [[token-storage-browser]], [[bff-token-handler]].
- **Spec maturity.** OAuth 2.1 (draft-15) and browser-based-apps (draft-26) are
  **drafts**, not ratified RFCs; RHBK implements the stable pieces (PKCE, exact
  redirect matching). DPoP (RFC 9449, final) is a **full feature only in RHBK 26.6**
  (preview earlier) — version-gate any DPoP requirement (kb:dpop- is 26.6).

## See also
- [[sso-implementation-review]] — the general evaluation lens (both-surface checklists + symptom→cause index)
- [[angular-spa-oidc-best-practice]] — the SPA-only companion answer (+ the scaffolded `examples/angular-rhbk-spa/`)
- [[oidc-client-best-practices]] · [[securing-apps-oidc-saml]] · [[client-libraries-by-stack]]

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
Resolved from the `sources:` of every wiki page used above — surfaced even where the
wiki already synthesizes the point.

- `kb:overview-` — Chapter 1. Planning for securing applications and services (RHBK 26.0, Securing Applications and Services Guide)
- `kb:oidc-layers-` — Chapter 2. Secure applications and services with OpenID Connect — endpoints, flows, token/userinfo/introspection (RHBK 26.0, SAS Guide)
- `kb:javascript-adapter-` — Chapter 3. RHBK JavaScript adapter (keycloak-js) — "must be a public client", configure Valid Redirect URIs + Web Origins as specifically as possible (RHBK, SAS Guide)
- `kb:assembly-managing-clients_server_administration_guide` — Chapter 13. Managing OpenID Connect and SAML Clients — public client, Standard/Implicit/Direct-Access flow toggles, **PKCE S256/plain per RFC 7636**, Securing Client URIs §13.7.7, token introspection (RHBK, Server Administration Guide)
- `kb:configuring-authentication_server_administration_guide` — Chapter 8. Configuring authentication (RHBK, Server Administration Guide)
- `kb:authz-client-` — Chapter 14. RHBK authorization client — resource-server / policy enforcement (RHBK 26.0, SAS Guide)
- `kb:dpop-` — Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP) (RHBK **26.6**, SAS Guide)
- `kb:migrating-applications` — Chapter 5. Migrating applications secured by RH-SSO 7.6 (RHBK 26.2, Migration Guide)
- `guide:securing_applications_and_services_guide` — Securing Applications and Services Guide (RHBK) — the SPA + adapter + OIDC spine
- `guide:server_administration_guide` — Server Administration Guide (RHBK) — client/flow/token-lifespan configuration
- `ref:securing-apps-oidc-saml.md` — curated reference: OIDC/SAML securing-apps
- `ref:server-administration.md` — curated reference: server administration

### Wiki pages + upstream `web:` sources
- [[sso-implementation-review]] (MOC) — RFC 9700; BBA draft-26; OAuth 2.1 draft-15; OWASP ASVS / cheat sheets
- [[oidc-client-best-practices]] — RFC 9700
- [[securing-apps-oidc-saml]] · [[oidc-token-validation]] · [[tokens-and-sessions]] · [[oidc-endpoints]] · [[oidc-grant-types]] · [[client-authentication-methods]]
- [[client-libraries-by-stack]] — angulararchitects.io (Angular+Spring RS); Spring Security OAuth migration; react-oidc-context; RFC 9700
- [[pkce]] — RFC 7636; OAuth 2.1 draft-15; RFC 9700
- [[token-storage-browser]] — BBA draft-26; OWASP ASVS; OWASP cheat sheets; Curity BFF
- [[bff-token-handler]] — BBA draft-26; Curity BFF + token-handler; Keycloak securing-apps (OSS)
- [[access-token-validation-resource-server]] — RFC 9068; RFC 6749/6750; RFC 7662/7009; OWASP API Top 10 2023
- [[audience-and-scope-checks]] — RFC 9068; RFC 9700; OWASP API Top 10 2023
- [[jwt-validation-pitfalls]] — RFC 9068; RFC 9700; OWASP cheat sheets; OWASP WSTG
- [[redirect-uri-validation]] — OAuth 2.1 draft-15; RFC 9700; OIDC Core
- [[state-and-nonce]] — OIDC Core; RFC 9700; OWASP
- [[refresh-token-rotation]] — OAuth 2.1 draft-15; RFC 9700; BBA draft-26
- [[cors-for-spa]] — BBA draft-26; OWASP ASVS; OWASP cheat sheets
- [[dpop-sender-constraining]] · [[dpop]] — RFC 9449; OAuth 2.1; RFC 9700
- [[rp-initiated-logout]] · [[back-channel-logout]] · [[oidc-logout]] — OIDC logout family (RP-initiated / back-channel / front-channel / session)
- [[bearer-token-usage]] — RFC 6750; RFC 9700
- [[service-to-service-client-credentials]] — RFC 6749/6750; RFC 9700; OAuth 2.1
- [[token-introspection]] · [[token-revocation]] — RFC 7662 / RFC 7009
- [[fapi-oauth21-profiles]] · [[fapi2-security-profile]] — FAPI 2.0 Security Profile + Attacker Model

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-6-oidc-layers|Chapter 2. Securing applications and services with OpenID Connect]]
- [[rhbk-26-6-overview-2|Chapter 1. Authorization services overview]]
- [[rhbk-26-6-javascript-adapter|Chapter 3. Red Hat build of Keycloak JavaScript adapter]]
- [[rhbk-26-4-assembly-managing-clients-server-administration-guide|Chapter 13. Managing OpenID Connect and SAML Clients]]
- [[rhbk-26-4-configuring-authentication-server-administration-guide|Chapter 8. Configuring authentication]]
- [[rhbk-26-6-dpop|Chapter 16. Securing applications with Demonstrating Proof-of-Possession (DPoP)]]
- [[rhbk-26-6-authz-client|Chapter 19. Red Hat build of Keycloak authorization client]]
- [[rhbk-26-6-migrating-applications|Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6]]
<!-- crosslink:end -->
