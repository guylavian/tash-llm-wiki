# Angular SPA secured against RHBK / Keycloak

A minimal, modern (Angular 18 standalone) SPA wired to a **Red Hat Build of
Keycloak (RHBK) / Keycloak** realm as a **public client using Authorization Code
+ PKCE (S256)** via [`keycloak-angular`](https://www.npmjs.com/package/keycloak-angular)
(over `keycloak-js`).

Every decision here is grounded in the wiki:
`wiki/questions/angular-spa-oidc-best-practice.md` →
[[oidc-client-best-practices]], [[securing-apps-oidc-saml]],
[[client-libraries-by-stack]], [[fapi-oauth21-profiles]], [[dpop]], [[oidc-logout]].

> This is a scaffold, not a generated project: it has the files that carry the
> security decisions. Generate the rest with `ng new` (or the Angular CLI) and
> drop these in, then `npm install`.

## File map → wiki rule

| File | What it does | Grounded in |
|---|---|---|
| `src/environments/environment.ts` | RHBK URL/realm/clientId + the public-client realm settings checklist | securing-apps-oidc-saml, client-authentication-methods |
| `src/app/keycloak.config.ts` | `provideKeycloak` — **PKCE S256**, `check-sso`, in-memory tokens, auto-refresh, scoped bearer interceptor | oidc-client-best-practices §1,§4,§9 |
| `src/app/app.config.ts` | App providers: Keycloak + router + HTTP bearer interceptor | client-libraries-by-stack |
| `src/app/auth/auth.service.ts` | login/logout/`getValidToken` (single-flight proactive refresh; `invalid_grant` → re-auth), role checks | oidc-client-best-practices §4,§7 · oidc-logout |
| `src/app/guards/auth.guard.ts` | functional auth guard; redirect-login if anon; realm/client role enforcement | oidc-grant-types |
| `src/app/pages/profile.component.ts` | calls a resource-server API; token attached only for the API origin | oidc-token-validation |
| `src/assets/silent-check-sso.html` | hidden-iframe silent SSO helper | (keycloak-js mechanics) |

## Realm setup (run once against your realm)

Create the **public** client with `kcadm.sh` (or the Admin Console):

```sh
kcadm.sh create clients -r my-realm \
  -s clientId=angular-spa \
  -s publicClient=true \
  -s 'redirectUris=["https://app.example.com/*"]' \
  -s 'webOrigins=["https://app.example.com"]' \
  -s standardFlowEnabled=true \
  -s implicitFlowEnabled=false \
  -s directAccessGrantsEnabled=false \
  -s 'attributes={"pkce.code.challenge.method":"S256","post.logout.redirect.uris":"https://app.example.com/*"}'
```

What each line enforces (from the wiki):

- `publicClient=true` → **client authentication OFF** — no secret in the browser.
- `standardFlowEnabled=true` → Authorization Code flow.
- `implicitFlowEnabled=false`, `directAccessGrantsEnabled=false` → the two flows
  RFC 9700 / OAuth 2.1 disallow.
- `pkce.code.challenge.method=S256` → **server-side PKCE enforcement** (the SPA
  also sets `pkceMethod: 'S256'`). Realm-wide you can instead bind a Client Policy
  to the `fapi-1-baseline` profile (its `pkce-enforcer` executor).
- exact `redirectUris` / `post.logout.redirect.uris` / `webOrigins` — no broad
  wildcards beyond the app path; CORS limited to the app origin.

Optional hardening:
- Enable **DPoP** (`dpop.bound.access.tokens=true`) so a stolen in-memory token
  is useless without the browser-held key — full feature in **RHBK 26.6**, preview
  earlier. ([[dpop]])
- Apply an **OAuth 2.1 public-client** policy profile. ([[fapi-oauth21-profiles]])
- Shorten access-token lifespan (Realm → Tokens) to ~5–15 min for sensitive APIs.

## Token handling — what the scaffold guarantees

- Endpoints are discovered from `/.well-known/openid-configuration` by keycloak-js
  (you only configure base URL/realm/clientId).
- Tokens stay **in memory** (never `localStorage`).
- Refresh is **proactive + single-flight** (`updateToken` / `withAutoRefreshToken`);
  a dead session forces a clean re-login instead of a retry loop.
- The bearer token is attached **only** to your API origin — never leaked to
  third-party hosts.

## Resource server (the other half)

The SPA does **not** validate its own access token. Your backend API must:
- validate the JWT via **JWKS** (`jwks_uri`), cached + rotation-aware;
- check `iss`, `aud`, `exp`, `nbf`;
- read roles from `resource_access[clientId].roles` / `realm_access.roles`.

See [[oidc-token-validation]] and the per-stack resource-server guidance in
[[client-libraries-by-stack]].

## If you need stronger XSS protection: BFF

The PKCE-public-client pattern keeps tokens in the browser, so any XSS can read
them (DPoP mitigates *reuse*, not *exfiltration of the bound proof flow*). RFC
9700's strongest SPA recommendation is a **BFF / Token Handler**: a server-side
**confidential** client holds the tokens, the browser holds only an
`HttpOnly`+`Secure` session cookie, and the BFF proxies API calls. Choose it when
you already run a backend tier or handle high-value data. See
`wiki/questions/angular-spa-oidc-best-practice.md` → "Code + PKCE vs BFF" and the
Node BFF note in [[client-libraries-by-stack]].

## Air-gapped note

On a disconnected network, resolve `keycloak-angular` / `keycloak-js` from an
internal npm mirror and prefer loading `keycloak-js` from the internal RHBK
server so it tracks the server version. ([[client-libraries-by-stack]])
