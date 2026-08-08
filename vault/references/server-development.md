# Server Development — Extending RHBK 26.6

Internal runbook for building custom providers (SPIs), themes, and scripts for **Red Hat build of Keycloak 26.6**. Grounded in the RHBK 26.6 Server Developer Guide (some Themes content is from the 26.2 chapter, Identity Brokering from 26.6). The provider/factory model is shared with upstream Keycloak 26; the runtime is Quarkus-only (since Keycloak 20 — no WildFly/EJB/CDI).

> **Air-gap note:** Custom extensions are deployed as JARs copied into `providers/` — no registry pull needed. The build (`kc.sh build`) is fully offline. Watch out for external touchpoints inside *your* provider code: LDAP/AD federation, remote vaults, external IdPs, remote DBs (use `example.internal` hosts, secrets as `***`). Build your provider JAR against the matching Maven artifacts on an internal mirror.

---

## 1. Provider / Factory model

Every SPI has two interfaces you implement plus one service file:

| Element | Role |
|---|---|
| `Provider` (e.g. `ThemeSelectorProvider`) | Light-weight, created **per request** via `create(KeycloakSession)`. Holds per-request state. |
| `ProviderFactory` (e.g. `ThemeSelectorProviderFactory`) | **Single instance** per server; can hold cross-request state. Lifecycle: `init` → `postInit` → (`create` per request) → `close`. |
| `META-INF/services/<fully.qualified.FactoryInterface>` | Service registration file; one FQ factory classname per line. |

### Factory lifecycle methods

| Method | When | Notes |
|---|---|---|
| `create(KeycloakSession session)` | Per request | Returns a new light-weight provider instance. |
| `init(Config.Scope config)` | Boot, once | Read SPI config (`config.get("...")`). |
| `postInit(KeycloakSessionFactory factory)` | Boot, after all `init` | Cross-SPI wiring. |
| `close()` | Shutdown | |
| `getId()` | — | Unique provider ID. Must match what you reference in config / `getProvider(..., "<id>")`. |
| `order()` | optional | Higher value wins when multiple factories share the same provider ID (see Overriding). |

```java
package org.acme.provider;
public class MyThemeSelectorProviderFactory implements ThemeSelectorProviderFactory {
    @Override public ThemeSelectorProvider create(KeycloakSession session) { return new MyThemeSelectorProvider(session); }
    @Override public void init(Config.Scope config) { }
    @Override public void postInit(KeycloakSessionFactory factory) { }
    @Override public void close() { }
    @Override public String getId() { return "myThemeSelector"; }
}
```

Service file `META-INF/services/org.keycloak.theme.ThemeSelectorProviderFactory`:

```
org.acme.provider.MyThemeSelectorProviderFactory
```

### Configuring a provider

```
bin/kc.[sh|bat] --spi-theme-selector--my-theme-selector--enabled=true --spi-theme-selector--my-theme-selector--theme=my-theme
```

Read it back in `init`:

```java
public void init(Config.Scope config) { String themeName = config.get("theme"); }
```

### Single- vs multiple-implementation provider types

- **Single-implementation** (e.g. `HostnameProvider`): one active impl per server. If several exist, pick a default at build time:
  ```
  bin/kc.[sh|bat] build --spi-hostname--provider=default
  ```
  The value must match a factory's `getId()`. Retrieve via `keycloakSession.getProvider(HostnameProvider.class)`.
- **Multiple-implementation** (e.g. `EventListener`): many coexist. Retrieve a named one: `session.getProvider(EventListener.class, "jboss-logging")`. The second arg is the `provider_id` = factory `getId()`.

### Overriding a built-in provider

Recommended: unique ID + set as default. When you must keep the **same provider ID** (e.g. customizing `OIDCLoginProtocolFactory`, whose ID `openid-connect` is relied on by the admin console / OIDC well-known endpoint), extend the built-in factory and bump `order()`:

```java
public class CustomOIDCLoginProtocolFactory extends OIDCLoginProtocolFactory {
    @Override public int order() { return 1; }
}
```

Highest `order()` for a given provider ID wins.

### Showing info in the Admin Console

Implement `org.keycloak.provider.ServerInfoAwareProviderFactory` on your factory to surface build/config/operational info on the **Server Info** page:

```java
public class MyThemeSelectorProviderFactory implements ThemeSelectorProviderFactory, ServerInfoAwareProviderFactory {
    @Override public Map<String, String> getOperationalInfo() {
        Map<String, String> ret = new LinkedHashMap<>();
        ret.put("theme-name", "my-theme");
        return ret;
    }
}
```

### `ProviderConfigProperty` (per-instance, component-based SPIs)

Component-based factories (e.g. User Storage) declare admin-rendered config via `getConfigProperties()` returning `List<ProviderConfigProperty>`. Build with `ProviderConfigurationBuilder`:

```java
configMetadata = ProviderConfigurationBuilder.create()
    .property().name("path")
        .type(ProviderConfigProperty.STRING_TYPE)
        .label("Path")
        .defaultValue("${jboss.server.config.dir}/example-users.properties")
        .helpText("File path to properties file")
    .add().build();
```

Validation/lifecycle callbacks (from `org.keycloak.component.ComponentFactory`): `validateConfiguration(...)` (throws `ComponentValidationException`), `onCreate(...)`, `onUpdate(...)`.

---

## 2. Packaging, build & registration

- Package classes + `META-INF/services/...` into a JAR. Provider JARs are **not** loaded in isolated classloaders.
- Copy the JAR (and any extra deps Keycloak doesn't already provide) to `providers/`.
- Re-build: non-optimized start, or `kc.[sh|bat] build`.

```
# place JAR, then:
bin/kc.[sh|bat] build
```

**Classloading hazards:**
- Do **not** include an `application.properties` or override the `commons-lang3` dependency — auto-build fails if the provider JAR is later removed.
- Conflicting classes → "split package" warning in the start log. Not all `lib` JARs are checked; inspect `<install root>/lib/lib/main` before bundling:
  ```
  find . -type f -name "*.jar" -exec unzip -l {} \; | grep some.file
  ```
- No warning for conflicting **resource files** — give resource paths a provider-unique prefix.
- If a removed provider JAR causes `NoSuchFileException` on startup, force a Quarkus index rebuild:
  ```
  ./kc.sh -Dquarkus.launch.rebuild=true --help
  ```

**Disable a provider:**
```
bin/kc.[sh|bat] build --spi-user-cache--infinispan--enabled=false
```

**Maven `pom.xml`:** needs a `dependencyManagement` import of `org.keycloak:keycloak-parent` at the RHBK version. For RHBK 26.6 use `VERSION` = `26.6.2.redhat-00001`. Pull artifacts from an internal Maven mirror in air-gapped builds.

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.keycloak</groupId>
      <artifactId>keycloak-parent</artifactId>
      <version>VERSION</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

> **Container note:** the official RHBK image uses OpenJDK as the Java runtime — build custom extensions against a compatible JDK.

---

## 3. Key SPIs

| SPI | Provider / Factory | Service file |
|---|---|---|
| Theme Selector | `ThemeSelectorProvider` / `ThemeSelectorProviderFactory` | `org.keycloak.theme.ThemeSelectorProviderFactory` |
| Theme Resource | `ThemeResourceProvider` / `ThemeResourceProviderFactory` | (ThemeResource SPI) |
| Locale Selector | `LocaleSelectorProvider` / `LocaleSelectorProviderFactory` | — |
| User Storage | `UserStorageProvider` / `UserStorageProviderFactory<T>` | `org.keycloak.storage.UserStorageProviderFactory` |
| Vault | `VaultProvider` / `VaultProviderFactory` | (Vault SPI) |
| Event Listener | `EventListener` (multiple-impl) | — |
| OIDC protocol mapper | `ProtocolMapper` (+ `OIDCAccessTokenMapper`/`OIDCIDTokenMapper`/`UserInfoTokenMapper`) | `org.keycloak.protocol.ProtocolMapper` |

To list every SPI available at runtime, see the **Provider Info** page in the Admin Console.

### Locale Selector

Default is `DefaultLocaleSelectorProvider` (implements `LocaleSelectorProvider`). Single method `resolveLocale(RealmModel, UserModel)` (UserModel nullable); request via `KeycloakSession#getContext`. Extend the default and override e.g. `getAcceptLanguageHeaderLocale()` (return null) to ignore `Accept-Language`.

### Theme Resource

Easiest: ship a JAR with `theme-resources/templates`, `theme-resources/resources`, `theme-resources/messages`. For full control implement `ThemeResourceProviderFactory` / `ThemeResourceProvider`.

---

## 4. OIDC Protocol Mapper skeleton (computed claim)

A custom OIDC mapper changes ID Token / Access Token / UserInfo content. Implement `ProtocolMapper` and the relevant token interfaces; override the **exact 5-arg `setClaim`** signature.

```java
package org.acme.mapper;

import org.keycloak.models.*;
import org.keycloak.protocol.oidc.mappers.*;
import org.keycloak.protocol.ProtocolMapper;
import org.keycloak.representations.IDToken;

public class ComputedClaimMapper extends AbstractOIDCProtocolMapper
        implements OIDCAccessTokenMapper, OIDCIDTokenMapper, UserInfoTokenMapper {

    @Override
    protected void setClaim(IDToken token,
                            ProtocolMapperModel mappingModel,
                            UserSessionModel userSession,
                            KeycloakSession keycloakSession,
                            ClientSessionContext clientSessionCtx) {
        // compute and attach the claim value to `token`
    }

    @Override public String getId() { return "acme-computed-claim-mapper"; }
}
```

Service file `META-INF/services/org.keycloak.protocol.ProtocolMapper`:

```
org.acme.mapper.ComputedClaimMapper
```

Package, copy JAR to `providers/`, run `kc.[sh|bat] build`.

---

## 5. Themes

Theme types: **Account, Admin, Email, Login, Welcome**. All except *welcome* are set per realm in **Realm Settings → Themes**. Welcome theme is set via:

```
bin/kc.[sh|bat] start --spi-theme-welcome-theme=custom-theme
```

A theme = HTML (Freemarker `.ftl`) + images + message bundles + stylesheets + scripts + `theme.properties`. Extend an existing theme (`parent=base` or `parent=keycloak`) rather than editing bundled themes (`keycloak-themes-<version>.jar`).

### Development (disable caching)

```
bin/kc.[sh|bat] start --spi-theme-static-max-age=-1 --spi-theme-cache-themes=false --spi-theme-cache-templates=false
```

Re-enable caching in production. Clear cache by deleting `data/tmp/kc-gzip-cache`.

### `theme.properties`

| Key | Meaning |
|---|---|
| `parent` | Parent theme to extend |
| `import` | Import resources from another theme |
| `common` | Override common resource path (default `common/keycloak`); suffix of `${url.resourcesCommonPath}` |
| `styles` | Space-separated stylesheets (list last to override parent) |
| `locales` | Comma-separated supported locales |

Substitutions: `${some.system.property}`, `${env.ENV_VAR}`, with default `${foo:defaultValue}`. Resource layout: `<TYPE>/resources/css|js|img`, messages in `<TYPE>/messages/messages_<LOCALE>.properties` (UTF-8; falls back to ISO-8859-1). Override a template by copying `themes/base/<TYPE>/<TEMPLATE>.ftl` into your theme (admin/account use a single `index.ftl`). Custom IdP login icons via `kcLogoIdP-<alias>` keys (PatternFly classes), e.g. `kcLogoIdP-myProvider = fa fa-lock`.

### Packaging themes as an archive

Production: deploy a JAR with `META-INF/keycloak-themes.json` listing themes and the types each provides. Copy to `providers/`, restart.

```json
{ "themes": [{ "name" : "mytheme", "types": [ "login", "email" ] }] }
```

```
mytheme.jar
├── META-INF/keycloak-themes.json
├── theme/mytheme/login/theme.properties
├── theme/mytheme/login/login.ftl
└── theme/mytheme/login/resources/css/styles.css
```

### React-based consoles (Admin / Account)

Admin & Account consoles are React. Base npm packages: `@keycloak/keycloak-admin-ui`, `@keycloak/keycloak-account-ui`. Wrap with `KeycloakProvider` (set `serverBaseUrl`, `realm`, `clientId`). Translations via `i18next` + `i18next-fetch-backend` (loadPath `…/resources/{realm}/account/{lng}`). Theme behaviour is overridable via the **Theme Selector SPI** (`ThemeSelectorProviderFactory` / `ThemeSelectorProvider`).

> **Air-gap note:** npm packages come from npm. Mirror them to an internal registry (e.g. `registry.example.internal`); point `loadPath`/`serverBaseUrl` at internal hosts.

---

## 6. User Storage SPI (federation)

Bridge an external user store to Keycloak's user model. Enabled per realm under **User Federation**. Lookup order: user cache → local DB → loop over User Storage providers. Provider class is created **once per transaction**; `close()` then GC.

### Core interfaces

- `org.keycloak.storage.UserStorageProvider` — base (`preRemove` callbacks for realm/group/role).
- `org.keycloak.storage.UserStorageProviderFactory<T extends UserStorageProvider>` — must pass the **concrete** provider class as the template param (runtime introspects it for capabilities; omitting it breaks the provider). `create(KeycloakSession, ComponentModel)` per transaction.

Service file: `META-INF/services/org.keycloak.storage.UserStorageProviderFactory` (line-separated FQ factory classnames).

### Capability (mix-in) interfaces

| Interface | Implement when |
|---|---|
| `UserLookupProvider` | You want to log in with these users (almost always). |
| `UserQueryMethodsProvider` / `UserQueryProvider` | View/manage users in the console. (`UserQueryProvider` = `UserQueryMethodsProvider` + `UserCountMethodsProvider`.) |
| `UserCountMethodsProvider` | Provider supports count queries. |
| `UserRegistrationProvider` | Add/remove users (`addUser`/`removeUser`; return null from `addUser` to skip). |
| `CredentialInputValidator` | Validate credential types (e.g. password). |
| `CredentialInputUpdater` | Update/disable credential types. If absent, credentials can be overridden in local storage — implement & throw `ReadOnlyException` for read-only creds. |

### Models & Storage IDs

`UserModel` (impl required) maps external ↔ Keycloak (`getId`, username, name, email, roles, groups, attributes). ID format is mandatory:

```
"f:" + component id + ":" + external id     e.g.  f:332a234e31234:wburke
```

component id = `ComponentModel.getId()`. Parse with `org.keycloak.storage.StorageId` (`getExternalId()`). Helper base classes: `org.keycloak.storage.adapter.AbstractUserAdapter` (read-only; setters throw `ReadOnlyException`), `AbstractUserAdapterFederatedStorage`. **WebAuthn:** user handle limited to 64 bytes — keep full storage ID ≤ 64 chars; assign a short component ID in `validateConfiguration` via `KeycloakModelUtils.generateShortId()` (22-char short UUID).

### Federated vs Import strategy

- **Federated storage** (`org.keycloak.storage.federated.UserFederatedStorageProvider`, via `UserStorageUtil.userFederatedStorage(session)`): store extra attrs/roles/groups/creds/required-actions in the Keycloak DB when the external store can't. Only stores data as needed.
- **Import**: create the user locally (`session.getProvider(UserProvider.class).addUser(...)`, let Keycloak generate the id), `UserModel.setFederationLink(model.getId())`, proxy with `org.keycloak.models.utils.UserModelDelegate`. Becomes a persistence cache but needs sync. Removing the provider auto-removes imported users.
  - `ImportedUserValidation.validate(realm, user)` — called when a linked local user loads from DB; return null to delete the local copy.
  - `ImportSynchronization` (on the factory): `sync(...)` / `syncSince(...)` — enables manual + scheduled sync in the console.

> **Air-gap note:** LDAP/AD and any external DB the provider talks to must be reachable on the internal network (e.g. `ldaps://ldap.example.internal`). Use the additional-datasource config (`session.getProvider(JpaConnectionProvider.class, "user-store").getEntityManager()`) for JPA-backed stores. Mark identity-linking attributes (like `LDAP_ID`) read-only.

### User cache

`KeycloakSession.getProvider(UserCache.class)` → `evict(realm, user)`, `evict(realm)`, `clear()` (cluster-wide invalidation). `OnUserCache.onCache(realm, CachedUserModel, delegate)` callback caches extra data via `CachedUserModel.getCachedWith()`. Per-provider cache policy configurable in the console.

### REST management (components API)

```
/admin/realms/{realm-name}/components
```
Create with `providerType = "org.keycloak.storage.UserStorageProvider"`, set `providerId`, `parentId`, config. Java client via `realmResource.components()` (`add` / `query(parent, type, name)` / `component(id).update|remove`).

### Stream-based interfaces

Capability and `org.keycloak.storage.federated` interfaces offer `Streams` sub-interfaces (e.g. `UserQueryProvider.Streams`) — implement these to process large result sets without materializing collections.

---

## 7. Vault SPI

`org.keycloak.vault` package. Built-in example: `files-plaintext`. Write a custom provider to connect to an arbitrary vault.

- Implement `VaultProviderFactory.create(...)` (realm available from `KeycloakSession`) and a single `obtainSecret` method returning `VaultRawSecret` (holds `byte[]` / `ByteBuffer`).
- **Realm isolation:** to stop cross-realm leakage, prefix entries with the realm name so `${vault.key}` resolves differently per realm.
- Package/deploy like any SPI (`providers/` + `kc build`).

Consuming secrets — keep them in memory only as long as needed; use try-with-resources so buffers get scrubbed:

```java
try (VaultCharSecret cSecret = session.vault().getCharSecret(SECRET_NAME)) {
    char[] c = cSecret.getAsArray().orElse(null);   // contains password here
}   // c now contains garbage
```

Entrypoint `KeycloakSession.vault()`: `getCharSecret()`, `getStringSecret()`, `getRawSecret()`. Prefer byte/char arrays over `String` (immutable Strings survive at least to the next GC).

> **Air-gap note:** a custom vault provider talking to an external secrets manager (e.g. `vault.example.internal`) must reach it on the internal network; store all secret material as `***` in examples/configs.

---

## 8. JavaScript / scripts — must ship as a JAR

Scripting is **Technology Preview** (not fully supported), **disabled by default**. Enable with `--features=preview` or `--features=scripts`. Script types: **Authenticator, JavaScript Policy, OpenID Connect Protocol Mapper, SAML Protocol Mapper**.

> **`upload-scripts` was removed.** Scripts can no longer be uploaded via the admin console/REST — they must be **deployed as a JAR** to `providers/`.

JAR structure:

```
META-INF/keycloak-scripts.json
my-script-authenticator.js
my-script-policy.js
my-script-mapper.js
```

`META-INF/keycloak-scripts.json` descriptor (sections: `authenticators`, `policies`, `mappers`, `saml-mappers`; each entry needs mandatory `fileName`, optional `name`/`description`):

```json
{
  "authenticators": [
    { "name": "My Authenticator", "fileName": "my-script-authenticator.js", "description": "My Authenticator from a JS file" }
  ],
  "mappers": [
    { "name": "My Mapper", "fileName": "my-script-mapper.js", "description": "My Mapper from a JS file" }
  ]
}
```

Deploy: copy JAR to `providers/`, run `bin/kc.[sh|bat] build`.

**Authenticator script bindings:** `script` (`ScriptModel`), `realm` (`RealmModel`), `user` (`UserModel`), `session` (`KeycloakSession`), `authenticationSession` (`AuthenticationSessionModel`), `httpRequest`, `LOG`. Provide `authenticate(context)` and/or `action(context)`. Place an always-run script authenticator as REQUIRED at the end of the flow (wrap existing executions in a REQUIRED subflow so REQUIRED/ALTERNATIVE aren't mixed at the same level).

**OIDC mapper script bindings:** `user`, `realm`, `token` (ID token, if configured), `tokenResponse` (`AccessTokenResponse`, if configured), `userSession`, `keycloakSession`. The script `exports` value becomes the claim value.

---

## 9. Identity Brokering APIs (RHBK 26.6)

Retrieve external IdP tokens stored at login.

**V1 (default):** enable **Store Tokens** on the IdP (Advanced settings). The access token must carry the `broker` client-level role `read-token` (user role mapping + within client scope); auto-assign to imported users via **Stored Tokens Readable**.
```
GET /realms/{realm-name}/broker/{provider_alias}/token
Authorization: Bearer <KEYCLOAK ACCESS TOKEN>
```

**V2 (Technology Preview, disabled by default)** — enable with `--features=preview` or `--features=identity-brokering-api:v2`. Uses `POST`, requires client authentication (confidential clients only); client needs **Allow retrieve external tokens** + **Allowed Identity Providers for External Tokens**. Token from the user session (DB fallback). Returns a JSON access-token response (`access_token` on success, `error` on failure); client policies apply.
```
POST /realms/{realm-name}/broker/{provider_alias}/token
Content-Type: application/x-www-form-urlencoded
client_id=test-client&client_secret=***&token=ey...
```

**Client-initiated account linking (AIA):** attach `kc_action=idp_link:<identity-provider-alias>` to the OIDC auth URL and redirect. User needs `account.manage-account` or `account.manage-account-links` (and client scope for it); IdP must be enabled for the realm. Legacy `/{auth-server-root}/realms/{realm-name}/broker/{provider}/link?client_id=…&redirect_uri=…&nonce=…&hash=…` protocol still exists (hash = Base64Url SHA-256 of nonce+sessionState+clientId+provider) but may be removed — migrate to AIA.

> **Air-gap note:** public social IdPs (Google/Facebook etc.) are unreachable in a disconnected env. Use only internal/on-prem IdPs (`idp.example.internal`); keep `client_secret` as `***`.

---

## 10. Admin REST API (token acquisition)

Full Admin REST API mirrors the Admin Console. Obtain a token, then send `Authorization: bearer <token>`.

```
# password grant (admin-cli)
curl -d "client_id=admin-cli" -d "username=admin" -d "password=***" \
     -d "grant_type=password" \
     "http://localhost:8080/realms/master/protocol/openid-connect/token"

# service account (client_credentials) — client_id in master, Client authentication On,
# Service account roles enabled, assigned the `admin` realm role
curl -d "client_id=<YOUR_CLIENT_ID>" -d "client_secret=***" \
     -d "grant_type=client_credentials" \
     "http://localhost:8080/realms/master/protocol/openid-connect/token"
```

Default token lifespan is 1 minute. Use `access_token` from the JSON response in the `Authorization` header (e.g. `GET /admin/realms/master`).

_Source: Red Hat build of Keycloak 26.6 Server Developer Guide (docs.redhat.com), distilled offline._
