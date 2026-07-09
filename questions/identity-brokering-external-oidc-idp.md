---
title: How does identity brokering work with an external OIDC identity provider in RHBK?
type: question
question_tier: support-kb
domain: keycloak
slug: identity-brokering-external-oidc-idp
summary: "RHBK acts as an identity broker — it delegates authentication to an external OpenID Connect provider, validates the response, imports/links the user, and then issues its own token to the client application. The client never interacts with the external IdP directly."
sources:
  - kb:identity_broker
  - guide:server_administration_guide
  - guide:server_developer_guide
  - ref:rhbk-26-4-identity-broker.md
  - ref:rhbk-26-6-identity-brokering-apis.md
provenance:
  extracted: 18
  inferred: 2
  ambiguous: 0
tags: [brokering, identity-provider, clients]
status: reviewed
updated: 2026-06-28
---

# How does identity brokering work with an external OIDC identity provider in RHBK?

**RHBK acts as an identity broker — an intermediary that delegates authentication to an external OpenID Connect provider, validates the security token response, imports or links the user, and then issues its *own* token to the client application. The client application never talks to the external IdP directly; it only integrates with RHBK.**

## The broker flow (end to end)

```
User → Client App → RHBK → External OIDC IdP → RHBK → Client App
```

1. **User requests a protected resource** in a client application.
2. **Client redirects to RHBK** for authentication.
3. **RHBK shows the login page** with a list of configured identity providers (or auto-redirects to a default IdP).
4. **User selects an OIDC identity provider** (e.g., "Log in with Google/ Microsoft/ your corporate OIDC IdP").
5. **RHBK issues an OIDC Authorization Request** (Authorization Code Flow) to the external IdP — the user's browser is redirected to the IdP's login page.
6. **User authenticates at the external IdP** (username/password, MFA, etc.).
7. **External IdP redirects back** to RHBK with an authorization code.
8. **RHBK exchanges the code** at the IdP's token endpoint for an ID token (and optionally an access token).
9. **RHBK validates the response**: verifies the ID token signature (using the IdP's JWKS or configured public key), validates `iss`, `aud`, `exp`, and any essential claims.
10. **RHBK imports or links the user:**
    - **First-time user:** RHBK creates a local user account, importing identity information from the IdP's claims (this is *identity federation*). The **First Login Flow** governs this step (e.g., ask for additional attributes, enforce terms of service, etc.).
    - **Returning user:** RHBK links the external identity to the existing account (account linking).
11. **RHBK issues its own token** to the client application (access token + refresh token).
12. **Client accesses the protected resource** using RHBK's token.

## Configuring an external OIDC IdP in the Admin Console

1. **Identity Providers** → **Add provider** → **OpenID Connect v1.0**.
2. Fill in the required OIDC endpoints:

| Field | Description |
|---|---|
| **Authorization URL** | The OIDC authorization endpoint of the external IdP |
| **Token URL** | The token endpoint for exchanging the authorization code |
| **Logout URL** | *(Optional)* The IdP's end_session endpoint |
| **User Info URL** | Endpoint for fetching additional user profile claims |
| **Client ID** | The OIDC client ID RHBK uses to identify itself to the external IdP |
| **Client Secret** | The client secret for the Authorization Code Flow |
| **Issuer** | The `iss` claim value RHBK expects in the ID token (validated by RHBK) |
| **Default Scopes** | Space-separated list of OIDC scopes (default: `openid`) |

3. Configure **Client Authentication**: `Client secret` (shared secret), `JWT signed with private key` (RHBK uses the realm private key), or `Client secret as JWT`.
4. Set **Validate Signatures** to ON and provide the IdP's public key via **JWKS URL** (preferred, e.g. `<idp>/realms/{realm}/protocol/openid-connect/certs` for an external RHBK) or a **Validating Public Key** in PEM format.
5. Optionally import the entire config from the IdP's metadata URL: `<root>/.well-known/openid-configuration`

### Common IdP settings

| Setting | Purpose |
|---|---|
| **Alias** | Unique identifier; RHBK uses it to build redirect URIs and the `kc_idp_hint` parameter |
| **Store Tokens** | When ON, RHBK stores the external IdP's token so applications can retrieve it via the broker API |
| **Stored Tokens Readable** | When ON, users can read stored tokens (assigns the `read-token` broker client-level role) |
| **Trust Email** | Skip email verification for users from this IdP |
| **First Login Flow** | Authentication flow for first-time brokered users (account linking, attribute gathering) |
| **Post Login Flow** | Flow triggered after the IdP login completes (e.g., MFA step-up after brokering) |
| **Sync Mode** | `legacy` / `import` / `force` — how RHBK updates user attributes from the IdP |
| **Verify essential claim** | Require a specific JWT claim (name + value, supports regex) in the IdP's ID token |
| **Default Scopes** | Scopes sent in the auth request (e.g., `openid profile email`) |
| **Prompt** | The OIDC `prompt` parameter (`login`, `consent`, `select_account`, `none`) |

### Customizing the login page

- **Default Identity Provider:** Set in **Authentication** → **Browser flow** → **Identity Provider Redirector** → **Default Identity Provider**. When configured, RHBK skips the IdP selection page and redirects directly to the default IdP.
- **`kc_idp_hint`:** A client can request a specific IdP by appending `?kc_idp_hint=<provider_alias>` to the auth URL — RHBK skips the selection page for that login only.
- **Hide on Login Page:** Keep the IdP configured but invisible on the selection page; only accessible via `kc_idp_hint`.
- **GUI Order:** Sort order of IdP buttons on the login page.

## Advanced: Retrieving external IdP tokens (Identity Brokering APIs)

RHBK can store the token returned by the external OIDC IdP so your application can use it to call the IdP's APIs on behalf of the user.

### V1 (default, enabled by default)
- Enable **Store Tokens** on the IdP's **Advanced settings**.
- User gets the `read-token` broker role.
- Application retrieves the token:
  ```
  GET /realms/{realm}/broker/{provider_alias}/token
  Authorization: Bearer <RHBK access token>
  ```

### V2 (Technology Preview)
- Enable `--features=identity-brokering-api:v2`.
- Client config has two new options: **Allow retrieve external tokens** and **Allowed Identity Providers for External Tokens**.
- Uses `POST` with client authentication (confidential clients only):
  ```
  POST /realms/{realm}/broker/{provider_alias}/token
  Content-Type: application/x-www-form-urlencoded
  client_id=...&client_secret=...&token=ey...
  ```

### Client-initiated account linking
A client can prompt a user to link their existing RHBK account to an external IdP:
```
kc_action=idp_link:<provider_alias>
```
Appended to the OIDC authentication URL. Requires `account.manage-account` or `account.manage-account-links` role.

## Contradictions / caveats

- The identity-brokering topic page is sourced from **RHBK 26.4**; the OIDC IdP configuration fields are stable across 26.x but social provider names and SAML option sets may shift between versions.
- Identity brokering is distinct from **LDAP user federation** ([[ldap-user-federation]]). LDAP federation syncs users from a directory; brokering delegates authentication to an external IdP.
- The **First Login Flow** (brokering) is separate from LDAP import modes — do not conflate them.
- V2 of the Identity Brokering API is Technology Preview and requires an explicit feature flag.

## See also
- [[identity-brokering]] — RHBK topic page on identity brokering (social, OIDC, SAML)
- [[authentication-flows]] — browser flows, First Login Flow, Post Login Flow
- [[token-exchange]] — exchanging tokens across realms/IdPs
- [[oidc-endpoints]] — RHBK's own OIDC endpoints
- [[tf-identity-providers]] — Terraform resources for declaring IdPs

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- **`kb:identity_broker`** → `rhbk-26-4-identity-broker.md` — Chapter 9. Integrating identity providers, RHBK 26.4 Server Administration Guide (Section 9.5 "OpenID Connect v1.0 identity providers": full OIDC IdP configuration, broker flow, common settings)
- **`ref:rhbk-26-6-identity-brokering-apis.md`** — Chapter 3. Identity Brokering APIs, RHBK 26.6 Server Developer Guide (retrieving external tokens V1/V2, client-initiated account linking)
- **`guide:server_administration_guide`** — The guide that hosts the Identity Brokering chapter across RHBK 26.x versions

### Wiki pages
- [[identity-brokering]] — RHBK topic page on identity brokering (overview, provider types, common settings)
- [[authentication-flows]] — browser flow, Identity Provider Redirector, First/Post Login Flows
- [[tf-identity-providers]] — Terraform resources for declaring OIDC/social/SAML/Kubernetes/SPIFFE IdPs
  - `web:https://raw.githubusercontent.com/keycloak/terraform-provider-keycloak/main/docs/resources/oidc_identity_provider.md` — Terraform `keycloak_oidc_identity_provider` resource docs (fetched 2026-06-16)
- [[token-exchange]] — exchanging tokens between realms and IdPs
- [[oidc-endpoints]] — RHBK's OIDC protocol endpoints

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-4-identity-broker|Chapter 9. Integrating identity providers]]
<!-- crosslink:end -->
