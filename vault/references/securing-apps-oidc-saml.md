# Securing Applications & Services with RHBK 26.6 (OIDC & SAML)

Offline runbook distilled from the **Red Hat build of Keycloak (RHBK) 26.6 Securing Applications and Services Guide** (Ch. 1-21). RHBK 26.6 tracks upstream Keycloak 26; protocol/endpoint behavior is shared with upstream unless flagged **RHBK-specific**. Pin client-library/adapter Maven artifacts to RHBK 26.6 GA versions (the docs show `999.0.0-SNAPSHOT` placeholders and the SAML Galleon pack at `26.6.2`).

Air-gap note: all examples use `localhost`/`example.internal` and `***` for secrets. In disconnected environments serve the discovery/JWKS/IdP-metadata endpoints internally, mirror NPM/Maven artifacts to an internal registry, and never reach `vscode.dev`, social IdPs, or public OTLP/JWKS URLs without an allow-listed egress proxy.

---

## 1. Planning: OIDC vs SAML decision

RHBK is an OAuth2, OpenID Connect and SAML compliant server; it can secure anything that speaks one of those protocols. **Leverage existing OIDC/SAML support from your language/framework/reverse-proxy first**; use a Keycloak Client Adapter only as a last resort (avoids vendor lock-in).

Basic steps to secure an app/service:
1. **Register a client** to a realm via Admin Console, the client registration service, or the CLI.
2. **Enable OIDC or SAML** in the app — via the ecosystem's existing support or via an RHBK adapter.

| Protocol | Recommended client-side implementations (per docs) |
|---|---|
| OIDC | JavaScript (client-side, `keycloak-js`); Node.js (server-side, `keycloak-connect`) |
| SAML | Java (SAML Galleon feature pack for WildFly/EAP) |

Terminology: **Client** = entity interacting with RHBK to authenticate users and obtain tokens. **Client adapter** = library giving tight platform integration. **Service account** = a client type that obtains tokens on its own behalf. "Creating a client" (Admin Console) and "registering a client" (Client Registration Service) are the same action.

**Decision guidance** (from chapters): prefer **OIDC** for new web/SPA/native/mobile/API workloads and where you want to avoid SAML's `SameSite` cookie workarounds (Ch. 6, 8). Use **SAML** when integrating Jakarta EE servlet apps via the Galleon pack, or third-party SPs that only speak SAML.

---

## 2. OIDC endpoints (per realm)

Base every path with `{server}/realms/{realm-name}`. The discovery doc lists them all:

```
/realms/{realm-name}/.well-known/openid-configuration
```
e.g. `http://localhost:8080/realms/{realm-name}/.well-known/openid-configuration`. Some RP libraries pull all endpoints from here; others need each listed individually.

| Purpose | Endpoint path (under `/realms/{realm-name}`) | Notes |
|---|---|---|
| Authorization | `/protocol/openid-connect/auth` | Authenticates end-user via user-agent redirect |
| Token | `/protocol/openid-connect/token` | Exchange code / credentials; refresh; also token-exchange & jwt-bearer grants |
| Userinfo | `/protocol/openid-connect/userinfo` | Standard claims; protected by bearer token |
| Logout | `/protocol/openid-connect/logout` | RP-initiated (redirect) logout |
| Certificate (JWKS) | `/protocol/openid-connect/certs` | Realm public keys as JWK; used for local token validation |
| Introspection | `/protocol/openid-connect/token/introspect` | Active state of access/refresh token; **confidential clients only** |
| Dynamic Client Registration | `/clients-registrations/openid-connect` | OIDC Dynamic Client Registration |
| Token Revocation | `/protocol/openid-connect/revoke` | Revokes access + refresh tokens (refresh revoke also revokes user consent) |
| Device Authorization | `/protocol/openid-connect/auth/device` | Returns device code + user code; confidential or public clients |
| Backchannel Authentication (CIBA) | `/protocol/openid-connect/ext/ciba/auth` | Returns `auth_req_id`; **confidential clients only** |
| SAML descriptor (for SAML clients) | `/protocol/saml/descriptor` | IdP metadata XML |
| Docker v2 token | `/protocol/docker-v2/auth` | Distribution registry auth (see §16) |

**Introspection with `Accept: application/jwt`** (RHBK-specific switch): response may include an extra `jwt` claim carrying the full JWT access token — useful when the introspected token was a *lightweight access token*. Requires enabling **Support JWT claim in Introspection Response** on the client's advanced settings.

**Logout endpoint direct invocation** is a non-standard legacy format kept only for legacy RHBK OIDC Java adapters / Elytron WildFly OIDC adapter — do **not** call it directly. For logout, use OIDC/SAML standard logout, Admin Console / Admin REST API, or Account Console / Account REST API.

---

## 3. Grant types (flows)

| Grant | Spec status / recommendation |
|---|---|
| **Authorization code** | Redirect-based; web apps + recommended for native/mobile. App swaps code (+ client creds) for Access + Refresh + ID token. |
| **Implicit** | Access/ID token returned directly, **no refresh token**. RFC 9700 says SHOULD NOT use; removed from OAuth 2.1. Token leak risk via logs/history. |
| **Hybrid** | Returns both code and tokens; same URL-fragment leak risk as implicit, but refresh token is available. |
| **Resource Owner Password Credentials** (Direct Grant) | RFC 9700: **MUST NOT** use. Prefer Device Grant or Authorization code. Requires client option **Direct Access Grants Enabled**. Not part of OIDC; removed from OAuth 2.1. |
| **Client credentials** | Client acts on its own behalf (background services). Secret or public/private keys. OAuth 2.0 only. |
| **Device Authorization Grant** | Input-constrained / browserless devices: get device+user code, user verifies in a browser, app polls token endpoint. |
| **CIBA** (Client Initiated Backchannel Authentication) | Client starts auth out-of-band (no browser redirect); polls for token OR uses **ping** mode with a configured **Client Notification Endpoint**. Confidential clients only. |
| **Token exchange** (`urn:ietf:params:oauth:grant-type:token-exchange`) | See §11. |
| **JWT authorization grant** (`urn:ietf:params:oauth:grant-type:jwt-bearer`) | See §12. |

**PKCE**: enforce S256 via the `pkce-enforcer` executor / FAPI baseline profile; `keycloak-js` defaults `pkceMethod` to `S256`.

Direct Grant example (CURL):
```bash
curl \
 -d "client_id=myclient" \
 -d "client_secret=***" \
 -d "username=user" \
 -d "password=***" \
 -d "grant_type=password" \
 "http://localhost:8080/realms/master/protocol/openid-connect/token"
```

**RHBK-specific error**: OIDC responses may carry `error=temporarily_unavailable` & `error_description=authentication_expired` when the SSO session exists but the per-tab authentication session expired. Client should immediately retry with a fresh OIDC auth request. (SAML equivalent: SAML `Status` with `AuthnFailed` + `StatusMessage=authentication_expired`; the SAML adapter retries automatically.)

---

## 4. Client types, registration & registration CLI

### Client Registration Service
Endpoint: `/realms/<realm>/clients-registrations/<provider>`. Built-in providers:

| Provider | Format | Operations |
|---|---|---|
| `default` | RHBK Client Representation (JSON) | create/get/update/delete (full Admin-Console-equivalent config incl. protocol mappers) |
| `install` | RHBK Adapter Configuration (JSON) | retrieve only (basic auth allowed; no auth for public clients) |
| `openid-connect` | OIDC Client Metadata (JSON) | OIDC Dynamic Client Registration / management |
| `saml2-entity-descriptor` | SAML v2 Entity Descriptor (XML) | **create only** |

**Authentication tokens** for the service:
- **Bearer token** — needs `create-client`/`manage-client` (create), `view-client`/`manage-client` (view), `manage-client` (update/delete). For create, prefer a Service Account with only `create-client`.
- **Initial Access Token** — recommended for new-client creation; configurable expiration + max-clients count; created in Admin Console (Clients → Initial access token). Value shown only once.
- **Registration Access Token** — returned on create; lets you later get/update/delete that one client. **Rotation enabled by default** (single-use; new token returned each use); can be disabled via Client Policies. Can be regenerated in Admin Console (client → Credentials → Generate registration access token).
- **Anonymous** registration possible but governed by **Client Registration Policies**.

CORS: configure **Allowed Registration Web Origins** for user-agent registration.

Default & install/SAML CRUD use `/clients-registrations/default[/<client id>]` etc. GET does not rotate the registration access token; create/update return a new one.

**Client Registration Policies** (being superseded by Client Policies): Trusted Hosts (no whitelisted host by default → anonymous registration de-facto disabled; loopback normalized to `localhost`), Consent Required, Protocol Mappers (whitelist; also applied to authenticated requests), Client Scope, Full Scope (disables Full Scope Allowed), **Max Clients** (default **200** for anonymous), Client Disabled.

### CLI: `kcreg` (`kcreg.sh` / `kcreg.bat` in `bin/`)
Server recognizes the CLI as the `admin-cli` client by default. To grant a user CLI rights, assign `manage-clients` (or `view-clients` / `create-client`, or in master realm the `NAME-realm` variant). Without `realm-management` roles a user can still log in but needs an Initial Access Token (else `403 Forbidden`).

```bash
kcreg.sh config credentials --server http://localhost:8080 --realm demo --user user --client reg-cli
kcreg.sh create -s clientId=my_client -s 'redirectUris=["http://localhost:8980/myapp/*"]'
kcreg.sh get my_client
kcreg.sh get myclient -e install > keycloak.json   # adapter config
kcreg.sh update myclient -s enabled=false -d redirectUris
kcreg.sh update myclient --merge -d redirectUris -f mychanges.json
kcreg.sh delete myclient
```
Config file default: `./.keycloak/kcreg.config` (contains tokens/secrets — keep private). Use `--config <path>` for parallel sessions, `--no-config` to avoid storing secrets. Initial token: `kcreg.sh config initial-token $TOKEN` or per-command `-t $TOKEN`. Refresh a lost registration access token: `kcreg config registration-token` / `kcreg update-token`. List attributes: `kcreg attrs`. In production use `https:`; for non-default CA use `kcreg config truststore --trustpass *** ~/.keycloak/truststore.jks`. **Troubleshoot**: `Parameter client_assertion_type is missing [invalid_client]` → client uses Signed JWT, so log in with `--keystore`.

Java API: `org.keycloak:keycloak-client-registration-api`.

---

## 5. Client authentication methods

| Method | How | Where configured |
|---|---|---|
| Client ID + secret | secret known to client + server; form params, Basic Auth, or admin-configured flow | Credentials tab (`secret`) |
| Signed JWT (`private_key_jwt`) | client signs `client_assertion` JWT with private key (RFC 7523); server verifies via JWKS URL or uploaded PEM/JWK/keystore | Credentials → Signed JWT + Keys tab |
| Signed JWT with Client Secret | HMAC-signed JWT using the client secret; algorithm `HS256`/`HS384`/`HS512` (default `HS256`) | Credentials → Signed JWT with Client Secret |
| mTLS (`tls_client_auth`) | X.509 client-certificate-bound auth | (used by FAPI / CIMD confidential-client requirements) |

Public clients (e.g. SPAs) hold no secret — authenticate by `client_id` only and rely on PKCE/redirect-URI hygiene.

Authorization-client `keycloak.json` credential blocks:
```json
"credentials": { "secret": "***" }
```
```json
"credentials": { "jwt": {
  "client-keystore-file": "classpath:keystore-client.jks",
  "client-keystore-type": "JKS",
  "client-keystore-password": "***",
  "client-key-password": "***",
  "client-key-alias": "clientkey",
  "token-expiration": 10 } }
```
```json
"credentials": { "secret-jwt": { "secret": "***", "algorithm": "HS512" } }
```

For Signed JWT, the client public key reaches RHBK either via a **JWKS URL** (most flexible — keys rotate, RHBK re-downloads on unknown `kid`) or by **uploading** the public key/certificate (PEM/JWK/keystore — hardcoded, change on rekey).

---

## 6. Validating tokens: JWKS (local) vs Introspection (network)

- **Introspection endpoint** (`/token/introspect`): authoritative but costs a network round-trip per validation; can overload the server. Confidential clients only.
- **Local JWS validation** (recommended for scale): RHBK access tokens are JWTs signed with JWS. Validate with the issuing realm's **public key** — hard-code it, or look up & cache it from the certificate (JWKS) endpoint keyed by the token's `kid` (KID). Many third-party libraries handle JWS validation.

**Redirect URIs**: be as specific as possible (especially public clients) to avoid open-redirect / unauthorized-entry. Production web apps: `https` only, never `http`. Special URIs: `http://127.0.0.1` (native apps, any port — prefer the IP literal over `localhost` per OAuth 2.0 for Native Apps); `urn:ietf:wg:oauth:2.0:oob` (no web server/browser — code shown on a page to copy-paste).

---

## 7. Logout: single / front- / back-channel

- **RP-Initiated (front-channel) logout**: redirect user-agent to `/protocol/openid-connect/logout`; ends the active user session, then redirects back to the app.
- **SAML Single Logout (SLO)**: via the IdP `SingleLogoutService` (POST/REDIRECT bindings, §10). Jakarta EE: `HttpServletRequest.logout()`. Any browser app: hit a security-constrained URL with `?GLO=true`. The SAML adapter stores SAML-session-index ↔ principal ↔ HTTP-session-ID mapping; for clustered/distributable apps use Infinispan `InfinispanSessionCacheIdMapperUpdater` and a **replicated** cache; multi-DC needs the cache replicated across data centers (e.g. via standalone Infinispan/JDG remote store).
- **Node.js adapter**: middleware catches `/logout` (configurable via `{ logout: '/logoff' }`); supports `redirect_url` query param; admin callbacks at `/` (configurable via `{ admin: '/callbacks' }`) to log out single/all sessions.
- **JS adapter Single-Sign-Out detection**: hidden **Session Status iframe** (status cookie, no network). Disable with `checkLoginIframe: false`. Limited by browser tracking protection (§9).
- **DPoP logout** (public clients): logout request (using refresh token) requires a DPoP proof (§13).

---

## 8. Client scopes, protocol mappers & audiences

- Client scopes are referenced by the `scope` request parameter (space-delimited). `openid` is always added by `keycloak-js`. Scopes are **Default** (always applied) or **Optional** (only when requested).
- **Audience mapper** adds a client/custom audience to `aud`. Used heavily for MCP audience binding (§14) and cross-domain chaining (§12).
- **Protocol Mappers** shape token contents; whitelistable via the Protocol Mappers registration policy.
- Token-exchange `scope` requests Optional scopes of the requester; `audience` filters (downscopes) audiences and client roles (§11).

---

## 9. Adapters / client libraries & supported status

### JavaScript adapter — `keycloak-js` (OIDC, public client)
Install `npm install keycloak-js`. Client **must be public** (Client authentication Off); set Valid Redirect URIs + Web Origins precisely.
```js
import Keycloak from 'keycloak-js';
const keycloak = new Keycloak({ url: "http://keycloak-server", realm: "my-realm", clientId: "my-app" });
const authenticated = await keycloak.init({ onLoad: 'check-sso',
  silentCheckSsoRedirectUri: `${location.origin}/silent-check-sso.html` });
```
- `onLoad`: `login-required` (force login) or `check-sso` (only if already logged in). **silent check-sso** uses a hidden iframe + `silentCheckSsoRedirectUri` page (must be a valid redirect URI; just `parent.postMessage(location.href, location.origin)`).
- Bearer requests: `authorization: Bearer ${keycloak.token}`. Refresh via `keycloak.updateToken(minValidity)`. Tokens kept **in memory only** (never persist — hijack risk).
- Flows: default Authorization Code; `flow: 'implicit'` / `'hybrid'` (require respective flags enabled on client). `init` `flow` values: `standard`/`implicit`/`hybrid`.
- `responseMode`: `fragment` (default, safer) or `query`. `pkceMethod`: `"S256"` (default) or `false`. `checkLoginIframe` default true (`checkLoginIframeInterval` 5s). `useNonce` default true. `silentCheckSsoFallback` default true. `messageReceiveTimeout` default 10000ms.
- **Cordova** `cordova` / `cordova-native` adapters are **deprecated** (removal in a future major). Custom adapters via the `KeycloakAdapter` interface.
- Methods: `login`/`logout`/`register`/`accountManagement`, `createLoginUrl`/`createLogoutUrl`/`createRegisterUrl`/`createAccountUrl`, `hasRealmRole`/`hasResourceRole`, `loadUserProfile`, `isTokenExpired`, `updateToken`, `clearToken`. `login` options include `prompt`, `maxAge`, `loginHint`, `scope`, `idpHint`, `acr`/`acrValues`, `action` (`register`/`UPDATE_PASSWORD`), `locale`. Callbacks: `onReady`, `onAuthSuccess/Error`, `onAuthRefreshSuccess/Error`, `onAuthLogout`, `onTokenExpired`.
- **Tracking protection**: Session Status iframe disabled under blocked third-party cookies (rely on tokens + short Access Token Lifespan); silent check-sso falls back to regular check-sso unless `silentCheckSsoFallback: false`. Affected: Chrome 84+ (SameSite=Lax), Safari 13.1+ (blocked 3rd-party cookies).

### Node.js adapter — `keycloak-connect` (OIDC; Connect/Express)
Supports public, confidential, **bearer-only**. Download `keycloak.json` (Admin Console → Action → Download adapter config → Keycloak OIDC JSON).
```js
const Keycloak = require('keycloak-connect');
const keycloak = new Keycloak({ store: memoryStore });
app.use(keycloak.middleware());
app.get('/complain', keycloak.protect(), handler);          // any authenticated user
app.get('/special', keycloak.protect('special'), handler);  // app role
app.get('/admin', keycloak.protect('realm:admin'), handler);// realm role
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'token'}), handler); // authz
```
- `keycloak.enforcer` `response_mode`: `token` (server issues new access token w/ permissions) or `permissions` (default; granted permissions on `req.permissions`). `resource_server_id` to point at a different (backend) client. Behind TLS-terminating proxy: `app.set('trust proxy', true)`.
- Custom scope: `new Keycloak({ scope: 'offline_access' })`. IdP hint: `new Keycloak({ store, idpHint: myIdP }, kcConfig)`. Override `Keycloak.prototype.redirectToLogin` to return 401 (not redirect) for API paths.

### mod_auth_openidc (Apache HTTPD, OIDC) — **best-effort, not officially supported by RHBK**
Needs `client_id`, `client_secret`, `redirect_uri`, the realm `.well-known/openid-configuration` URL.
```apache
OIDCProviderMetadataURL ${KC_ADDR}/realms/${KC_REALM}/.well-known/openid-configuration
OIDCClientID ${CLIENT_ID}
OIDCClientSecret ***
OIDCRedirectURI http://${HOSTIP}/${CLIENT_APP_NAME}/redirect_uri
OIDCRemoteUserClaim preferred_username
```

### mod_auth_mellon (Apache, SAML) — **best-effort, not officially supported by RHBK**
RHEL: `yum install httpd mod_auth_mellon mod_ssl openssl`. Admin Console SAML client Installation page → **Mod Auth Mellon files** generates the SP descriptor + PEMs. Config in `/etc/httpd/conf.d/mellon.conf` (`MellonSPMetadataFile`, `MellonSPPrivateKeyFile`, `MellonSPCertFile`, `MellonIdPMetadataFile`). SP metadata via `/usr/libexec/mod_auth_mellon/mellon_create_metadata.sh`. Fetch IdP metadata: `curl -k -o /etc/httpd/saml2/idp_metadata.xml https://$idp_host/realms/test_realm/protocol/saml/descriptor`. Set `MellonSecureCookie On` + `MellonCookieSameSite none` (module ≥ 0.16.0) to survive `SameSite=Lax` defaults. Client edits: Force POST Binding On; add `paosResponse` redirect URI for SAML ECP; add a Group list mapper (`groups`) to send groups.

### Java client libraries (Maven `org.keycloak`)
| Artifact | Purpose | Status notes |
|---|---|---|
| `keycloak-admin-client` | Admin REST API Java client | Requires Java 11+ at runtime |
| `keycloak-authz-client` | Authorization Services client (entitlements, protection API, RPT introspection) | |
| `keycloak-policy-enforcer` | PEP for Jakarta EE | |
| `keycloak-client-common-synced` | shared classes used by the others | |
| `keycloak-client-registration-api` | client registration | |
| `keycloak-saml-adapter-galleon-pack` | SAML SP feature pack | `26.6.2` |

**Compatibility**: the last released client libraries are supported with **all supported RHBK server versions** — you need not upgrade the server in lockstep. They *may* work with older servers but that is not guaranteed/supported; consult the javadoc for endpoint/parameter support per server version. **Admin client**: when injecting a custom Jackson provider, ensure `ObjectMapper` has `setSerializationInclusion(JsonInclude.Include.NON_NULL)` and `configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)` (extend `org.keycloak.admin.client.JacksonProvider`) to avoid cross-version compatibility issues. **Upgrade Node.js adapter**: download new archive, remove old dir, unzip new, update `keycloak-connect` dependency in `package.json`.

---

## 10. SAML Galleon feature pack (WildFly/EAP)

Distributed as a Galleon feature pack for **WildFly 29+** and **JBoss EAP 8 GA**, provisioned with `wildfly-maven-plugin`, `wildfly-jar-maven-plugin`, or `eap-maven-plugin`. Layers: `keycloak-saml`, `keycloak-client-saml`, `keycloak-client-saml-ejb`. Adapter artifact `org.keycloak:keycloak-saml-adapter-galleon-pack:26.6.2`.

Config file `/WEB-INF/keycloak-saml.xml` (or externally via the `urn:jboss:domain:keycloak-saml:1.1` subsystem `<secure-deployment name="MODULE.war">`, where name = `module-name` + `.war`). `web.xml`: `<auth-method>KEYCLOAK-SAML</auth-method>` + standard servlet `security-constraint`s. ACS/SLO endpoint = app base URL + `/saml` (`https://example.internal/contextPath/saml`).

### `<SP>` attributes
| Attr | Meaning / default |
|---|---|
| `entityID` | client identifier — **REQUIRED** |
| `sslPolicy` | `ALL` / `EXTERNAL` (default) / `NONE` |
| `nameIDPolicyFormat` | requested NameID format (e.g. `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`); default none |
| `forceAuthentication` | default `false` |
| `isPassive` | default `false` (opposite of forceAuthentication) |
| `turnOffChangeSessionIdOnLogin` | default `false` (keep on) |
| `autodetectBearerOnly` | `true` → 401 for SOAP/REST vs redirect for browser; default `false` |
| `logoutPage` | post-logout page (full URL = 302 redirect; path = displayed) |
| `keepDOMAssertion` | default `false`; store raw assertion DOM in `SamlPrincipal` |

### Keys
`<Key signing="true" encryption="true">` with `<KeyStore resource=... password=***>` (`<PrivateKey alias=... password=***/>`, `<Certificate alias=.../>`) **or** PEM (`<PrivateKeyPem>`/`<PublicKeyPem>`/`<CertificatePem>`). At least one of `signing`/`encryption` must be true.

`<PrincipalNameMapping policy="FROM_NAME_ID"|"FROM_ATTRIBUTE" attribute="email"/>`. `<RoleIdentifiers>` maps SAML attributes (`Role`, `member`, `memberOf`) to Jakarta EE roles. `<RoleMappingsProvider id="properties-based-role-mapper">` (`org.keycloak.adapters.saml.PropertiesBasedRoleMapper`) maps via a properties file (`properties.file.location` filesystem, else `properties.resource.location` WAR, else `/WEB-INF/role-mappings.properties`).

### `<IDP>` attributes
| Attr | Meaning / default |
|---|---|
| `entityID` | IdP issuer — **REQUIRED** |
| `signaturesRequired` | default `false` (sets default for sub-elements) |
| `signatureAlgorithm` | `RSA_SHA1`/`RSA_SHA256` (default)/`RSA_SHA512`/`DSA_SHA1`. `*_SHA1` deprecated; signature verify fails on Java 17+ for SHA1 |
| `signatureCanonicalizationMethod` | default `http://www.w3.org/2001/10/xml-exc-c14n#` |
| `metadataUrl` | retrieve IdP metadata (key rotation pickup) |

`<AllowedClockSkew unit="...">` (units MICRO/MILLI/SECONDS(default)/MINUTES/NANOSECONDS; default value 0). `<SingleSignOnService>`: `signRequest`, `validateResponseSignature`, `requestBinding` (POST default / REDIRECT), `responseBinding`, `assertionConsumerServiceUrl` (must end `/saml`), `bindingUrl` (**REQUIRED**). `<SingleLogoutService>`: `signRequest`/`signResponse`/`validateRequestSignature`/`validateResponseSignature` (each default to IDP `signaturesRequired`), `requestBinding` (POST default), `responseBinding` (POST default), `postBindingUrl` (REQUIRED for POST), `redirectBindingUrl` (REQUIRED for REDIRECT).

`<IDP><Keys>`: signature-verify certs/public keys; if both SP & IdP are RHBK, omit Keys to auto-fetch from the SAML descriptor (cannot mix auto-fetch + static keys). Multiple `signing="true"` keys supported for key rotation. `<HttpClient>` (descriptor retrieval): `connectionPoolSize` (10), `disableTrustManager`/`allowAnyHostname` (dev only, default false), `truststore`/`truststorePassword` (REQUIRED unless disableTrustManager), `clientKeystore`/`clientKeystorePassword`, `proxyUrl`, `socketTimeout`/`connectionTimeout`/`connectionTtl` (default `-1`). Air-gap: point `truststore`/`proxyUrl` at internal CA/proxy; never disable the trust manager in production.

**SameSite**: set `JSESSIONID` SameSite=None (WildFly `undertow-handlers.conf`: `samesite-cookie(mode=None, cookie-pattern=JSESSIONID)`, WildFly ≥ 19.1.0) to keep SAML POST binding working — or switch to REDIRECT binding / OIDC. **Multi-tenancy**: implement `org.keycloak.adapters.saml.SamlConfigResolver`, wire via `keycloak.config.resolver` context-param. **Assertion attrs**: cast `getUserPrincipal()` to `org.keycloak.adapters.saml.SamlPrincipal` (`getAttribute`/`getFriendlyAttribute`/`getAssertion`). **Errors**: `HttpServletResponse.sendError` (400/401/403/500); inspect request attr `org.keycloak.adapters.spi.AuthenticationError` → `SamlAuthenticationError` (`EXTRACTION_FAILURE`/`INVALID_SIGNATURE`/`ERROR_STATUS`). Debug: log `org.keycloak.saml` at DEBUG.

---

## 11. Token exchange

Two implementations:
- **Standard token exchange V2** — `token-exchange-standard:v2`, **enabled by default**, fully supported. Internal→internal only (RFC 8693). Per-client switch **Standard token exchange** must be on; requester must be **confidential** + use its configured client auth.
- **Legacy V1** — preview, **deprecated**, off by default (`--features=preview` or `--features=token-exchange`); requires **FGAP v1** (FGAP v2 has no token-exchange permissions, intentionally). Supports internal↔external + impersonation. Will be removed; use Standard V2 / JWT Authorization Grant / Identity Brokering APIs instead.

Standard request:
```
POST /realms/test/protocol/openid-connect/token
Authorization: Basic ***
Content-Type: application/x-www-form-urlencoded
Accept: application/json
grant_type=urn:ietf:params:oauth:grant-type:token-exchange&
subject_token=$SUBJECT_TOKEN&
subject_token_type=urn:ietf:params:oauth:token-type:access_token&
requested_token_type=urn:ietf:params:oauth:token-type:access_token
```
| Param | Standard V2 |
|---|---|
| `grant_type` | REQUIRED `urn:ietf:params:oauth:grant-type:token-exchange` |
| `subject_token` | REQUIRED |
| `subject_token_type` | REQUIRED — must be `urn:ietf:params:oauth:token-type:access_token` |
| `requested_token_type` | OPTIONAL — `...:access_token` (default), `...:id_token`, `...:refresh_token` |
| `scope` | OPTIONAL — adds Optional client scopes of requester (upscoping) |
| `audience` | OPTIONAL, multi-valued — filters/downscopes `aud` & client roles |

Response includes `access_token`, `issued_token_type` (= requested), `token_type` (`Bearer`, or `N_A` for ID token), and `refresh_token` only if requested & allowed. `subject_token` must list the requester in `aud` (unless exchanging its own token). **Sender-constrained tokens (RFC 7800, incl. DPoP-bound and X.509-bound) cannot be the `subject_token`** → `invalid_request`; but you can *output* a DPoP-bound token by supplying a valid DPoP proof. Public clients cannot send exchange requests. Refresh token requires **Allow refresh token in Standard Token Exchange** ≠ `No` (other value: `Same session`; not allowed from Transient/Offline subject sessions, nor `scope=offline_access`). Never creates a new user session (may create a client session for refresh). No `resource` param support yet; impersonation supported, delegation not. Consents: allowed only if user already consented to all requested scopes. Revocation: access→access no chain (keep access tokens short-lived); access→refresh supports a revocation chain (revoking the original revokes the chain). Enforce downscoping via the `downscope-assertion-grant-enforcer` policy executor; integrate with Client Policies (`client-scope`+`grant-type`+`client-roles` conditions).

Legacy V1 form params add `subject_issuer`, `requested_issuer` (internal→external IdP alias), `requested_subject` (impersonation by username/id), and support **direct-naked-impersonation** (no `subject_token`; very risky; public clients forbidden). Permissions granted via the `token-exchange` fine-grained permission + a client policy on the target client / IdP / Users; service-account roles can group exchange permissions. External→internal: `subject_token_type` `...:access_token` (+ `subject_issuer`) or `...:jwt` (matched by `iss`); validated via the IdP userinfo service or JWT signature.

---

## 12. JWT Authorization Grant (RFC 7521/7523) & cross-domain chaining

`grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`, with an `assertion=<JWT>`. **Confidential clients only**; enable **JWT Authorization Grant** capability + select **Allowed Identity Providers for JWT Authorization Grant**. Trust is an Identity Provider (OIDC v1.0 / Keycloak OIDC, or the **JWT Authorization Grant** IdP type).

Assertion validation: `iss` = IdP (`issuer` option); `sub` = external user ID (RHBK user must be linked to the IdP); `aud` = RHBK issuer or token-endpoint URL; `exp` mandatory; `nbf`/`iat`/`jti` validated if present; JWT signed + verified against IdP keys. By default one-time assertions (require `jti`). IdP options: **Allow assertion reuse**, **Max allowed assertion expiration** (default 5 min), **Assertion signature algorithm** (any if unset), **Allowed clock skew** (default 0), **Limit access token expiration**, **Use JWKS URL** (recommended On)/**JWKS URL**, **Validating public key (id)** (when JWKS URL off). OIDC IdP extra: **Allows Client ID as audience for assertions** (non-standard); client-side **Custom audience mapping** (Advanced tab) maps per-IdP-alias custom audiences. **Never issues a refresh token; always a transient session.** Brute-force protection does not apply (no credential-based auth). Client policies: condition `identity-provider-alias`; executors `downscope-assertion-grant-enforcer`, `jwt-claim-enforcer`.

Example assertion claims: `{"jti","iss":"https://jwt-idp.example.internal","sub":"<ext-user-id>","aud":"https://keycloak.server/realms/demo","iat","exp"}`; header `{"alg":"ES256","kid":"..."}`.

Google IdP: only the **ID Token** works as the assertion; `aud` must equal the Google Client ID (no custom audience allowed); no `jti` → no replay check (token reusable); ID token fixed at 1 h. Mismatched Google client → use **Custom audience mapping** keyed by IdP alias (`google`). Air-gap: Google/external JWT grants require egress to the IdP JWKS — not fully usable offline.

**Cross-domain chaining** (OAuth Identity & Authorization Chaining draft): in `domaina` use Standard Token Exchange (`scope=access-domainb`, `audience=http://.../realms/domainb`) to mint an assertion; `domainb` configures `domaina` as an OIDC IdP (Discovery endpoint of `domaina`, with JWT Authorization Grant enabled) and a `clientb` with the JWT grant capability that accepts the exchanged token as `assertion`. Link the user in `domainb` to `domaina` first. Recommended replacement for legacy external↔internal token exchange.

---

## 13. DPoP — Demonstrating Proof-of-Possession (RFC 9449)

Sender-constrains tokens to a client key pair (defeats replay of leaked Bearer tokens). Use for public clients/SPAs/native, XSS-exposed browser apps, FAPI/high-security, and to stop service-chaining.

**DPoP proof** = a fresh JWT per HTTP request in the `DPoP` header. Header: `typ` MUST be `dpop+jwt`, `alg` asymmetric (e.g. `ES256`/`RS256`), `jwk` = public key. Body: `jti`, `htm` (HTTP method), `htu` (target URI w/o query/fragment), `iat`, `ath` (base64url SHA-256 of access token — required on resource access), `nonce` (only if server requests via `DPoP-Nonce`).

Token binding: RHBK embeds the key thumbprint (base64url SHA-256 of the JWK) in the token as `cnf.jkt` (`token_type: "DPoP"`). Resource access uses `Authorization: DPoP <token>` (not Bearer) + a new `DPoP` proof; RS compares proof key to `cnf.jkt`. Nonce challenge: `401 Unauthorized` + `DPoP-Nonce` → retry with `nonce` claim.

Config: client Capability config **Require DPoP bound tokens** (maps to `dpop_bound_access_tokens` registration metadata). If enabled, all token requests need a valid proof; if disabled, RHBK binds only when a proof is sent. Public clients: both access + refresh tokens bound (proof on refresh too). Confidential clients: only access token bound (creds secure the refresh). RHBK enforces DPoP on UserInfo, Logout (public clients via refresh), and Admin/Account APIs when a DPoP token is used. Client Policies executor **`dpop-bind-enforcer`**: auto-enable for new clients, refresh-token-only binding, or strict OIDC enforcement requiring `dpop_jkt` in the auth-code flow. Token exchange: DPoP-bound token cannot be `subject_token`, but DPoP output is possible (upgrade Bearer → DPoP, optionally with down-scope/audience change).

---

## 14. MCP (Model Context Protocol) integration

RHBK as MCP authorization server. Versions: `2025-11-25` (supported), `2025-06-18` & `2025-03-26` (**partially supported, no Resource Indicators RFC 8707**); `2024-11-05` has no authz. RHBK does **not** yet support the RFC 8707 `resource` parameter.

**Audience binding workaround** (no RFC 8707): use OAuth `scope` instead of `resource`. For MCP server `https://example.internal/mcp` with scopes `mcp:tools`/`mcp:prompts`/`mcp:resources`, create each as an **Optional** client scope with an **Audience** mapper whose **Included Custom Audience** = the MCP server URL, so issued tokens carry `"aud": "https://example.internal/mcp"`. The Included Custom Audience must equal the auth request `resource` value and the MCP server URL.

**MCP 2025-11-25 / OAuth Client ID Metadata Document (CIMD)** — **experimental** (breaking changes possible), enable with `--features=cimd`. Profile executor `client-id-metadata-document` options: **Allow http scheme** (OFF in prod), **Trusted domains** (wildcards e.g. `*.example.internal`; empty = all denied), **Restrict same domain**, **Required properties**, **Only Allow Confidential Client** (requires `jwks`/`jwks_uri` + `private_key_jwt`/`tls_client_auth`). Policy condition `client-id-uri` options: **URI scheme** (only `https` in prod), **Trusted domains** (empty = false always). System-wide SPI options (not in Admin Console): `min-cache-time` (300s), `max-cache-time` (259200s = 3 days), `upper-limit-metadata-bytes` (5000 = 5 KB) via `--spi-client-policy-executor--client-id-metadata-document--<prop>=<value>`. MCP Inspector / VS Code desktop need CORS / anonymous-registration policy setup (Allowed Client Scopes, Allowed Registration Web Origins, Trusted Hosts). VS Code desktop is a public client using PKCE with `client_id` on `vscode.dev` and `http://127.0.0.1:<port>/callback` redirect → set **Restrict same domain** OFF, Trusted domains `vscode.dev,127.0.0.1`. Air-gap: CIMD fetches client metadata from a URL — host it on `*.example.internal`; do not allow `vscode.dev` / external CIMD URLs without an egress allow-list.

---

## 15. Authorization Services client & Policy Enforcer (Java)

**`keycloak-authz-client`** (`AuthzClient`): config in `keycloak.json` (`realm`, `auth-server-url`, `resource`, `credentials`; default classpath location). Create via `AuthzClient.create()`. Obtain entitlements / RPT (`authzClient.authorization("alice","alice").authorize(request)` → `response.getToken()`), manage resources via the Protection API (`authzClient.protection().resource()`), introspect RPT (`authzClient.protection().introspectRequestingPartyToken(rpt)`). Client auth: secret, signed JWT (keystore), or signed JWT with client secret (HS256/384/512). TLS: `truststore`/`truststore-password`.

**`keycloak-policy-enforcer`** (PEP for Jakarta EE): JSON config.
```json
{ "enforcement-mode": "ENFORCING",
  "paths": [ { "path": "/users/*",
    "methods": [ { "method": "GET",  "scopes": ["urn:app.com:scopes:view"] },
                 { "method": "POST", "scopes": ["urn:app.com:scopes:create"] } ] } ] }
```
`enforcement-mode`: `ENFORCING` (default — deny when no policy), `PERMISSIVE`, `DISABLED`. Options: `on-deny-redirect-to` (default 403), `path-cache` (`lifespan` 30000ms, `max-entries` 1000; 0 disables, -1 no expiry), `paths` (auto-discovered if omitted; `name`, `path` patterns `/*`, `/*.html`, `/path/*`, `/resource/{id}`, `/resource`), per-method `scopes-enforcement-mode` `ALL`(default)/`ANY`, `claim-information-point` (CIP — request/external-HTTP/static/SPI claims), `lazy-load-paths`, `http-method-as-scope`. Decisions via `org.keycloak.AuthorizationContext` (`hasResourcePermission`/`hasScopePermission`); get an `AuthzClient` via `ClientAuthorizationContext.getClient()`. TLS: `truststore`/`truststore-password`. Node.js equivalent: `keycloak.enforcer` (§9).

---

## 16. Distribution (Docker) registry auth

"Docker Registry" renamed **Distribution Registry** (feature/endpoint/protocol still called *docker*). **Docker auth disabled by default** — enable via the features chapter. RHBK Docker provider emits config (Admin Console client → Action):
```yaml
auth:
  token:
    realm: http://localhost:8080/realms/master/protocol/docker-v2/auth
    service: docker-test
    issuer: http://localhost:8080/realms/master
```
Or env overrides: `REGISTRY_AUTH_TOKEN_REALM`, `REGISTRY_AUTH_TOKEN_SERVICE`, `REGISTRY_AUTH_TOKEN_ISSUER`. **Must** set `rootcertbundle` (or `REGISTRY_AUTH_TOKEN_ROOTCERTBUNDLE`) to the realm public-key location, else auth fails. Docker Compose YAML option is **dev-only**; configure the registry client in a non-`master` realm (HTTP Basic flow has no forms). `docker login localhost:5000 -u $username`.

---

## 17. Advanced security profiles (FAPI, OAuth 2.1)

Enforced via **Client Policies** linked to built-in global client profiles (RHBK validates the AS side only — adapters do no FAPI/OAuth 2.1 client-side validation).

FAPI profiles: `fapi-1-baseline` (contains `pkce-enforcer` → S256), `fapi-1-advanced`, `fapi-2-security-profile`, `fapi-2-dpop-security-profile`, `fapi-2-message-signing`, `fapi-2-dpop-message-signing`; CIBA via `fapi-ciba` (+ `fapi-1-advanced`). **PAR** (Pushed Authorization Request): use `fapi-1-baseline` + `fapi-1-advanced`. **Open Finance Brasil** (FAPI 1.0 ID3) is stricter (encrypted request objects via `secure-request-object` with Encryption Required; JWS `PS256`, JWE `RSA-OAEP`/`A256GCM`). **Australia CDR** = FAPI 1 Advanced (+ PKCE/`pkce-enforcer` when using PAR). TLS: FAPI requires TLS — tune `https-protocols` / `https-cipher-suites`; RHBK defaults to `TLSv1.3`.

**OAuth 2.1** profiles: `oauth-2-1-for-confidential-client`, `oauth-2-1-for-public-client` (still draft — built-in profiles may change). For public clients, combine with the **DPoP** preview feature (binds access+refresh tokens to the client key pair).

**Lightweight access tokens**: a slimmer access token; pair with introspection `Accept: application/jwt` + **Support JWT claim in Introspection Response** (§2) to recover the full JWT. **mTLS-bound tokens** and **X.509 certificate-bound tokens** are sender-constrained (RFC 7800/8705) and, like DPoP-bound tokens, cannot be used as a token-exchange `subject_token`.

---

## 18. Specifications implemented (selected)

| Area | Status / conformity |
|---|---|
| OpenID Connect (core/discovery/dynamic reg/CIBA/etc.) | Supported — Certified (18.0.0) |
| FAPI 1 (baseline/advanced), JARM, FAPI-CIBA | Supported — Certified (15.0.2) |
| FAPI 2 (security profile / message signing) | Supported — Passed |
| SAML 2.0 | Supported (multiple bindings; some parts unimplemented) |
| UMA 2.0 | Supported |
| JSON Web (JWT/JWS/JWE/JWK/JWA) | Supported |
| FIPS 140-2 | Supported — Certified (BC FIPS libs; needs certified OS+JVM stack) |
| WebAuthn (Level 2) | Supported (RHBK acts as Relying Party) |
| OID4VCI (Verifiable Credential Issuer) | Experimental |

Status meanings: **supported** / **preview** / **experimental**. Air-gap: experimental/preview features (CIMD, legacy token exchange, OID4VCI) gate behind `--features=` flags and should be reviewed before enabling in disconnected production.

_Source: Red Hat build of Keycloak 26.6 Securing Applications and Services Guide (docs.redhat.com), distilled offline._
