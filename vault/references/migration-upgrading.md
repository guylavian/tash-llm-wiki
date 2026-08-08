# Migration & Upgrading — RH-SSO 7.6 → RHBK and RHBK version upgrades — 26.6 (Offline Reference)
Distilled runbook for migrating RH-SSO 7.6 to RHBK 26.6 and for upgrading RHBK x → 26.6. Air-gap notes inline.

---

## PART A — Migration: RH-SSO 7.6 → RHBK 26.6

RHBK 26.6 is built on **Quarkus** (replaces JBoss EAP). RPM distribution of the server is **no longer available**. Migration covers: server, Operator, Templates, applications/adapters, custom providers, custom themes.

### A.1 Server migration (standalone ZIP)

**Prerequisites:** old RH-SSO 7.6 shut down (must not share the DB target) · database backed up · OpenJDK 21 installed · Release Notes reviewed.

**High-level steps:** Download RHBK ZIP (Red Hat customer portal) → migrate configuration → migrate database → start server.

> Air-gap: pull the RHBK server ZIP from the customer portal on a connected host, transfer to the disconnected segment. No internet is needed to run the server. Oracle/MSSQL drivers must be installed manually (not bundled).

#### Config model change
`standalone.xml` / `jboss-cli` no longer apply. One unified option model; sources in precedence order (first wins): **CLI parameters → Environment variables → Configuration file → Java KeyStore file**.

| Source | Format (db host example) |
|---|---|
| CLI | `--db-url-host cliValue` |
| Env var | `KC_DB_URL_HOST=envVarValue` |
| Config file | `db-url-host=confFileValue` |
| Java KeyStore | `kc.db-url-host=keystoreValue` |

`kc.sh --help` lists all options. Troubleshoot with `kc.sh show-config` (shows source+value) and `kc.sh --verbose start` (full stack trace).

#### Key config deltas (7.6 → RHBK)

| Area | RH-SSO 7.6 | RHBK 26.6 |
|---|---|---|
| DB drivers | Manual install | Built-in for supported DBs; **Oracle & MSSQL drivers still manual** |
| Datasource | `<datasource>` in subsystem | `--db postgres --db-url-host … --db-url-port … --db-url-database … --db-schema … --db-pool-min-size … --db-pool-max-size … --db-username … --db-password …` |
| Extra datasource | `<xa-datasource>` | `--db-kind-<name> --db-url-full-<name> --db-username-<name> --db-password-<name>`; `persistence.xml` v3.0, `jakarta.persistence.jtaDataSource` |
| HTTP/TLS | EAP `<tls>` | `start` ⇒ HTTP disabled, TLS+hostname required. `--http-enabled=true` (isolated nets only). Context root: add `--http-relative-path=/auth` to mimic old `/auth`. JKS: `--https-key-store-file/--https-key-store-password`; PEM: `--https-certificate-file/--https-certificate-key-file` |
| Cache/cluster | Infinispan subsystem | Single `kc.sh`; `--cache` default = `local` (start-dev) / `ispn` (start). Most via Infinispan config file; e.g. `cache-embedded-realms-max-count`. **Domain clustered mode not supported** |
| Transport stack | jgroups stacks | Default **`jdbc-ping`** (DB discovery, TCP, auto-TLS). All other stacks deprecated; set `cache-embedded-network-bind-address`; for non-transparent nets set `cache-embedded-network-external-port`/`-address` |
| Hostname/proxy | `spi hostname` | `--hostname <url>` (required with `start` unless `--hostname-strict=false`); `--hostname-admin`; `--proxy-headers xforwarded` (or `forwarded`). Hostname/proxy affect resource URLs only, not bind addr/port |
| Truststore | `spi truststore` JKS | PEM or PKCS12 (`.p12`/`.pfx`, **unencrypted, no password**). Convert JKS via keytool→openssl. `--truststore-paths … --tls-hostname-verifier WILDCARD` |
| Vault | Elytron `elytron-cs-keystore` | `--vault keystore --vault-file /path/keystore.p12 --vault-pass ***`. No realm config changes; `${vault.realm-name_alias}` still works with `REALM_UNDERSCORE_KEY` |
| JVM | `standalone.conf` | No `/bin` conf file. `JAVA_OPTS` (full override) or `JAVA_OPTS_APPEND` (append) |
| SPI providers | `<spi>` XML | `spi-<spi-id>--<provider-id>--<property>=<value>` |

> Air-gap: store DB creds and TLS/vault secrets (`***`) in a Java KeyStore source rather than CLI/env. Truststore must hold the internal CA chain (`ldap.example.internal`, etc.) for LDAP/HTTPS egress.

#### Start commands

| Mode | RHBK | RH-SSO 7.6 |
|---|---|---|
| Dev (NOT prod) | `./kc.sh start-dev` | `./standalone.sh` |
| Production | `./kc.sh start` (HTTP off, TLS+hostname enforced) | — |

### A.2 Database migration

RHBK auto-migrates the schema on first start against the target DB. RHBK can reuse the **same DB instance** as 7.6 (schema migrated automatically on first connect).

| Strategy | How |
|---|---|
| Automatic (default) | Start server connected to DB; schema migrated if changed |
| Manual | `kc.sh start --spi-connections-jpa-quarkus-migration-strategy=manual` → writes `bin/keycloak-database-update.sql`, then server exits. Change path with `--spi-connections-jpa-quarkus-migration-export=<path>/<file.sql>` |

> Air-gap: use **manual** strategy to generate the SQL offline, review it, and apply via your DBA pipeline against the on-prem DB. No external calls during migration.

### A.3 Operator on OpenShift

Operator was **completely recreated**; not backward compatible with the 7.6 Operator. Requires a **new** Keycloak deployment.

**Procedure:** install RHBK Operator into namespace → create new CRs + Secrets (manually port 7.6 config) → for custom providers/themes, build a custom optimized image.

**Keycloak CR** supports all server options as first-class fields; unknowns go in `additionalOptions`; raw pod overrides via `unsupported.podTemplate` (Tech Preview).

```yaml
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
  name: example-kc
spec:
  instances: 1
  db:
    vendor: postgres
    host: postgres-db.example.internal
    usernameSecret: { name: keycloak-db-secret, key: username }
    passwordSecret: { name: keycloak-db-secret, key: password }
  http:
    tlsSecret: example-tls-secret
  hostname:
    hostname: sso.example.internal
  additionalOptions:
    - name: spi-connections-http-client--default--connection-pool-size
      value: 20
```

| Topic | 7.6 Operator | RHBK Operator |
|---|---|---|
| DB | Secret `POSTGRES_*`; only PostgreSQL; embedded DB managed | `spec.db` w/ Secret refs; **all server-supported vendors**; embedded-DB migration **not supported** (convert to external first) |
| TLS | OpenShift-CA TLS Secret default; reencrypt Route | User must supply `tlsSecret` (`kubernetes.io/tls`); **passthrough** Route default; no TLS termination config; disable default Route via `spec.ingress.enabled: false` + custom Route |
| Extensions | In CR | **Not supported** — build optimized custom image, set `spec.image`. Operator skips optimization for custom images |
| Upgrade strategy | recreate/rolling (manual choice) | Default **recreate** (scale down first); alt strategies **Auto**/**Explicit**; only one server version may hit DB |
| Health | — | Health endpoints on by default, management port **9000**, not exposed as Route |
| Pod-level | Many low-level fields | Use first-class fields; else `spec.unsupported.podTemplate` (Tech Preview). Prefer `spec.imagePullSecrets` over `podTemplate…imagePullSecrets` |
| External instance | Supported | **Not supported** |
| HPA | Needed `disableReplicasSyncing: true` | Scale CR directly via HPA |

**CR migration:** `KeycloakRealm` (CR) → **`KeycloakRealmImport`** (bootstrap only; no update/delete; full realm representation; `spec.keycloakCRName`). **Client and User CRs removed** (Client CR planned future; User CR not planned).

> Air-gap: `spec.image` must reference a **mirrored** registry (e.g. `registry.example.internal/rhbk/keycloak:<tag>`). Build custom provider/theme images, push to the internal registry, reference via `spec.image` + `imagePullSecrets`. JGroups encryption is automatic with `jdbc-ping` (no `JGROUPS_*` CR equivalents).

### A.4 Templates on OpenShift

OpenShift templates **deprecated and removed** from RHBK images; use the Operator. **OpenShift 3.x unsupported.** RHBK Operator does **not** manage a DB — provision/manage it separately (you may retain the `<app>-postgresql` DeploymentConfig from the old template and point the new Keycloak CR at it).

Template-class buckets: H2 `*-https` (devel, unsupported for prod), ephemeral `*-postgresql` (dev only), persistent `*-postgresql-persistent`/`*-x509-postgresql-persistent`.

| 7.6 param | RHBK 26.6 |
|---|---|
| `APPLICATION_NAME` | `.metadata.name` |
| `IMAGE_STREAM_NAMESPACE` | N/A — Operator-controlled or `spec.image` |
| `SSO_ADMIN_USERNAME/PASSWORD` | Default `admin`; password created by Operator on first reconcile |
| `SSO_REALM` | Not needed if reusing DB; else RealmImport CR |
| `DB_JNDI` | No longer applicable |
| `HTTPS_KEYSTORE*` | N/A — secret referenced by `tlsSecret` |
| `JGROUPS_*` | No first-class field; `jdbc-ping` encrypts by default |

Proxy/TLS termination override (passthrough default): `additionalOptions: name: proxy / value: reencrypt`.

### A.5 Applications & adapters

**OIDC Java adapters no longer released:** JBoss EAP 6.x, EAP 7.x, Spring Boot, Red Hat Fuse. RH-SSO 7.6 adapters remain in maintenance support and **are supported against the RHBK 26.6 server**.

| App type | Migration target |
|---|---|
| EAP 8.x (OIDC) | EAP **native OIDC client** (delete `EAP_HOME/modules/system/add-ons/keycloak/`); `keycloak.json` maps to EAP config |
| EAP 7.x / 6.x | No RHBK support; use 7.6 adapter (7.x maint; 6.x EOL) |
| Spring Boot | Spring Security OAuth2/OIDC |
| Fuse | No RHBK support; 7.6 adapter maintenance only |
| Policy enforcer | Separate `org.keycloak:keycloak-policy-enforcer` artifact |
| SPA (JS) | `@redhat/keycloak-js` **26.2.x** (legacy `.success()/.error()` removed; must use `new`) |
| Node.js | `@redhat/keycloak-connect` **26.1.1** |
| SAML (EAP) | EAP 8.x: Keycloak SAML Adapter feature pack/RPM. EAP 6.x/7.x: 7.6 only |

> Air-gap: JS/Node adapters install from `https://npm.registry.redhat.com` — mirror to your internal npm proxy (`npm.example.internal`) and point `@redhat:registry` there.

**OIDC protocol/client changes:** Access Type removed (use Capability config: no flow = Bearer-only, auth off = Public, auth on = Confidential; `bearerOnly`/`publicClient` still in JSON/REST/import). Custom non-http(s) schemes need explicit redirect pattern (`custom:/test`; `*` no longer covers them). New `client_id` param on logout endpoint. New **Valid Post Logout Redirect URIs** (`+` = reuse Valid Redirect URIs). UserInfo: RFC 6750 errors via `WWW-Authenticate`, requires `openid` scope (else 403), checks user status. Service Account `Client ID` mapper claim renamed `clientId` → `client_id`. `iss` param (RFC 9207) added by default — disable per client via **Exclude Issuer From Authentication Response**.

**SAML changes:** SP metadata now exposes only encryption realm keys (algorithm-tagged: `rsa-oaep-mgf1p`→RSA-OAEP, `rsa-1_5`→RSA1_5). `RSA_SHA1`/`DSA_SHA1` deprecated (fail verification on Java 17+).

### A.6 Custom providers

Deploy to `providers/` (not `standalone/deployments/`). No separate classpath; **EAR/WAR and `jboss-deployment-structure.xml` unsupported**; no hot-deploy/auto-discovery — run a build or restart after changes. Java EE → **Jakarta EE 10** (`javax.*` → `jakarta.*`, except JDK `javax.*`; session/stateless beans unsupported). Removed 3rd-party deps: `openshift-rest-client`, `okio-jvm`, `okhttp`, `commons-lang`, `commons-compress`, `jboss-dmr`, `kotlin-stdlib` (copy explicitly if needed). `@Context` injection on JAX-RS removed — use `session.getContext().getHttpRequest()/getHttpResponse()`. Storage layer consolidated: keep `users()`/`clients()`/`groups()`; `*LocalStorage()`/`*StorageManager()` removed (use `StoreManagers`/`DatastoreProvider` for local-vs-cache). New modules: `keycloak-model-storage`, `-private`, `-services`. `RealmModel` storage-provider getters → cast to `LegacyRealmModel`. `UserCache` moved to `keycloak-storage-legacy` (`UserStorageUtil.userCache(session)` / `session.invalidate(...)`). Credentials: `user.credentialManager().createStoredCredential(...)`; `UserModel.credentialManager()` must be implemented (`LegacyUserCredentialManager`).

### A.7 Custom themes

New Admin Console & Account Console (`keycloak.v2`, React) — **no migration path** from the old AngularJS/server-templated `keycloak` themes or the base Admin Console theme. Login themes: reference built-in templates in `${KC_HOME}/lib/lib/main/org.keycloak.keycloak-themes-${KC_VERSION}.jar`. `start-dev` disables theme caching. Install as JAR in `${KC_HOME}/providers` or files in `${KC_HOME}/themes`.

### A.8 Upstream Keycloak → RHBK 26.6

Minimal differences since v22: artifacts on Red Hat customer portal (not keycloak.org); Oracle/MSSQL drivers **not bundled**; **GELF log handler unavailable**. Match versions: equal → use RHBK artifacts; older → upgrade KC first via Upgrading Guide; newer → cannot migrate. ZIP → swap artifacts; Operator → uninstall, install RHBK Operator (**CRs are compatible**); custom image → rebuild on RHBK base image.

### A.9 Other notable changes

Nashorn JS engine bundled by default (don't copy it for script providers). Admin client artifact renamed: `keycloak-admin-client-jakarta` retired → `keycloak-admin-client` (Jakarta, since 26.6.0); Java EE → `keycloak-admin-client-jee`. **Never expires** combo removed from client Advanced Settings (was `-1`). New email rule: 64-char local-part limit; `--spi-user-profile-declarative-user-profile-max-email-local-part-length` (default 64).

---

## PART B — Upgrading: RHBK x → 26.6

Documented path: **26.4.x → 26.6**. From earlier (22.x/24.x/26.2/26.4) review every intervening upgrading guide first. RH-SSO 7.6 customers use Part A instead.

**Order of operations:** 1) review release-specific changes → 2) upgrade the **server** → 3) upgrade **adapters** (if new versions) → 4) upgrade **admin client** if needed. *Server is upgraded before adapters.*

### B.1 Prepare & download server

Rolling updates of **patch** releases supported since 26.6.0 (see Rolling Updates Guide); for minor/major upgrades shut down first. Back up installation (config, themes). If XA enabled, settle open transactions and delete `data/transaction-logs/`. Back up the DB.

- Schema becomes incompatible with the old server after upgrade; **no DB rollback** — to revert, restore old install **then** restore DB from backup.
- If `persistent-user-sessions` is disabled, all non-offline user sessions are lost on upgrade (feature disabled by default before 26.0.0). Brute-force/in-flight auth state lives only in caches cleared on shutdown.

Download/extract `rhbk-26.6.2.zip` → move into place → copy `providers/` and `themes/` from old install → copy all `conf/` files **except `cache-ispn.xml`** (re-apply cache customizations onto the new `cache-ispn.xml`).

> Air-gap: mirror `rhbk-26.6.2.zip` (and any new adapter packages / custom images) into the disconnected segment **before** the maintenance window. The upgrade itself requires no internet.

### B.2 Database migration (upgrade)

Auto-migrated on first start by default. Shut down **all** old-version nodes first. Not supported with default H2 `dev-file` type.

| Item | Detail |
|---|---|
| Migration timeout | `transaction-setup-timeout` (default 30 min). `kc.sh start --transaction-setup-timeout=60m` |
| Auto index threshold | **300000** records — above it, index creation skipped and SQL logged for manual apply. `--spi-connections-liquibase--quarkus--index-creation-threshold=<n>` (0/negative disables) |
| Manual strategy | `--spi-connections-jpa--quarkus--migration-strategy=manual` → `bin/keycloak-database-update.sql`, then exits. Export path: `--spi-connections-jpa--quarkus--migration-export=<path>/<file.sql>` |

New indexes this release: `OFFLINE_CLIENT_SESSION` (`IDX_OFFLINE_CSS_BY_CLIENT_AND_REALM`, `IDX_OFFLINE_CSS_BY_USER_SESSION_AND_OFFLINE`), `BROKER_LINK` (`IDX_BROKER_LINK_USER_ID`, `IDX_BROKER_LINK_IDENTITY_PROVIDER`) — skipped if table > 300k rows. New columns: `USER_ENTITY.LAST_MODIFIED_TIMESTAMP`; `KEYCLOAK_GROUP.CREATED_TIMESTAMP`/`LAST_MODIFIED_TIMESTAMP` (NULL for pre-existing rows). After manual SQL, first startup may run extra data migrations.

> Air-gap: prefer **manual** strategy to apply schema SQL via the on-prem DBA pipeline, or pre-create skipped indexes offline. Honor `transaction-setup-timeout` for large datasets.

### B.3 Release-specific changes (26.6)

**Breaking:**
| Change | Action |
|---|---|
| JS policies need `scripts` feature | Enable `scripts` feature |
| `secure-client-uris` stricter (FAPI 2.0) | HTTPS required for Post-logout redirect / Logo / Policy / ToS URLs; `+` wildcard now allowed in post-logout redirect & web origins |
| Unique issuer for JWT grant / client assertions | Fix duplicate IdP `issuer` before upgrade |
| Ports open during init (health on) | Health-check `/health/ready`; revert via `--server-async-bootstrap=false` |
| SAML `SubjectConfirmationData` bearer check | Allow sufficient clock skew |
| Outgoing HTTP no redirect-follow | Revert: `--spi-connections-http-client--default--allow-redirects true` (deprecated) |
| Client-scope eval needs `view-users` | Grant role/permission |
| Introspection validates `aud` | Server: `allow-token-introspection-without-audience-check` (deprecated); add audience mapper |
| UserInfo rejects lightweight tokens | `allow-userinfo-with-lightweight-access-token` (deprecated); use introspection/token exchange |

**Notable:** second-class options now honored ahead of first-class defaults (check startup warnings). `transaction-default-timeout` (default 5 min) overrides `quarkus.transaction-manager.default-transaction-timeout`. Dev mode `http-host` defaults to `localhost` (set `0.0.0.0` for old behavior). Graceful HTTP shutdown (1s delay/timeout). `X-Forwarded-Prefix` supported with `proxy-headers=xforwarded`. New brute-force **Secondary Authentication Failures Lockout**. `client_secret_basic`/`_post` method now preserved per registration. **Zero-downtime patch updates default on** (`rolling-updates:v2` flag gone; Operator update strategy `Auto`). **Infinispan 16.0** (external Data Grid → upgrade to 16.0, set `legacy: true` metrics, `indexing.startupMode=NONE`). not-before clock skew default 10s (15s for JWT client assertions). Base themes now abstract. New CLI: `db-tls-mode` (`disabled`/`verify-server`), `db-tls-trust-store-file/-password/-type`, `--db-connect-timeout` (default `10s`), `transaction-setup-timeout` (30 min, replaces `spi-dblock--jpa--lock-wait-timeout`). MSSQL `sendStringParametersAsUnicode=false` by default. UTF-8 DB encoding check (MySQL/MariaDB → `utf8mb4`). `KCRAW_` env prefix for literal values. Virtual threads need ≥4 CPU cores. URLs with `;` rejected (HTTP 400) unless `http-accept-non-normalized-paths=true`. SAML REDIRECT inflate cap 128KB (`--spi-login-protocol--saml--max-inflating-size=`). OIDC token-endpoint param max 4000 chars (`req-params-default-max-size`). Required Actions now one-time by default.

> Air-gap: cluster CA truststore now auto-discovered (`--truststore-kubernetes-enabled=true` default) — adds `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` and `service-ca.crt`. On Operator upgrades that rely on trusting the cluster CA, **upgrade custom images first**, or pre-set `truststore-paths` in the CR so older Pods keep trusting the CA mid-upgrade. Mirror Infinispan 16.0 Data Grid images internally before upgrade.

### B.4 Upgrade adapters

Adapter and server versions are decoupled. Rule of thumb: older adapter may work with newer server; newer adapter may **not** work with older server.

| Adapter | Supported version / action |
|---|---|
| JBoss EAP SAML | Not shipped since 26.0; EAP 6.x/7.x → 7.6 only; delete `EAP_HOME/modules/system/add-ons/keycloak/`, install EAP 8.x feature pack/RPM |
| JBoss EAP OIDC | Not shipped since 26.0 (EOL); delete add-ons dir; use EAP 8.x native OIDC client |
| JavaScript | **26.2.x** — `npm install @redhat/keycloak-js@latest` |
| Node.js | **26.1.1** — `npm install @redhat/keycloak-connect@latest` |

```bash
npm config set @redhat:registry https://npm.registry.redhat.com   # mirror to npm.example.internal in air-gapped envs
npm install @redhat/keycloak-js@latest
```

### B.5 Migrate themes (upgrade)

Copy custom themes from old `themes/` to new `themes/`. Diff customized templates/messages/styles against the new base theme (per Migration Changes). For styles, e.g. `diff RHSSO_HOME_OLD/themes/keycloak/login/resources/css/login.css RHSSO_HOME_NEW/.../login.css`. Extending the base theme → styles step can be skipped.

_Source: Red Hat build of Keycloak 26.6 Migration Guide and Upgrading Guide (docs.redhat.com), distilled offline._
