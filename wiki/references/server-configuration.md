# RHBK 26.6 Server Configuration

Operating/configuring the Red Hat build of Keycloak (RHBK) 26.6 server. Pinned to RHBK 26.6; the underlying Server Configuration Guide content is shared with upstream Keycloak 26 unless flagged RHBK-specific (container image registry, RPM-stripped base image, OpenShift-only support statement). Air-gap notes use `example.internal` and `***` for secrets.

> Scope: build-vs-runtime model, starting, hostname v2, HTTP/TLS, database, reverse proxy, bootstrap/recovery, logging, truststores, mTLS, FIPS 140-2, vault, health/metrics, features, import/export, production checklist. Cross-references to distributed caches and tracing where they touch server config.

---

## 1. Configuration model: BUILD vs RUNTIME

`start`/`start-dev` implicitly run a `build` under the covers. For production, run `build` explicitly (CI/CD step) then `start --optimized`.

- **Build options** — marked with a tool icon (🛠) in *All configuration*; persisted into the optimized image; only usable with `build`. Stored in **plain text** — never store secrets as build options (this includes the KeyStore Config Source).
- **Configuration (runtime) options** — usable at `start`; e.g. `db-password`, `hostname`, `https-certificate-file`.

```bash
bin/kc.[sh|bat] build --db=postgres        # set build option
bin/kc.[sh|bat] start --optimized          # skip build check at startup
```

`--optimized` tells RHBK to assume a pre-built image. A build option seen at start with a value equal to the built value is silently ignored; a different value logs a warning and the previously built value is used (re-run `build` for it to take effect).

Underlying concepts: Quarkus re-augmentation/mutable-jar. `build` creates a closed-world provider registry, pre-parses config files, configures DB-specific resources, and persists build options.

### Config sources & precedence (highest → lowest)

1. Command-line parameters
2. Environment variables
3. Options in `conf/keycloak.conf` (or a user-created config file)
4. Sensitive options in a user-created Java KeyStore file

When set in multiple sources, the highest in the list wins. Example: `--db-url=cliValue` beats `KC_DB_URL=envVarValue` beats `db-url=confFileValue` beats `kc.db-url=keystoreValue`.

### Per-source formats

| Source | Format |
|---|---|
| Command-line | `--<key-with-dashes>=<value>` (some have `-<abbrev>=<value>` shorthand) |
| Environment variable | `KC_<KEY_WITH_UNDERSCORES>=<value>` |
| Config file (`conf/keycloak.conf`) | `<key-with-dashes>=<value>` |
| KeyStore config file | `kc.<key-with-dashes>` (value = password stored in KeyStore) |

These formats apply to `spi` options too. See *All configuration* (Ch. 21) for the full option list.

```bash
bin/kc.[sh|bat] start --db-url-host=mykeycloakdb     # CLI
export KC_DB_URL_HOST=mykeycloakdb                   # env
db-url-host=mykeycloakdb                             # conf/keycloak.conf
```

### Referencing env vars from keycloak.conf

```properties
db-url-host=${MY_DB_HOST}
db-url-host=${MY_DB_HOST:mydb}     # :fallback after colon
```

### Explicit config file

```bash
bin/kc.[sh|bat] --config-file=/path/to/myconfig.conf start   # or -cf
```

### Sensitive options via Java KeyStore (Keystore Config Source)

Default type `PKCS12`. Secrets must use the `PBE` key algorithm.

```bash
keytool -importpass -alias kc.db-password -keystore keystore.p12 -storepass *** -storetype PKCS12 -v
bin/kc.[sh|bat] start --config-keystore=/path/to/keystore.p12 \
  --config-keystore-password=*** --config-keystore-type=PKCS12
```

Use the KeyStore Config Source primarily for sensitive data (e.g. `kc.db-password`). Do not store build options in a keystore.

### Raw Quarkus properties (unsupported, last resort)

Create `conf/quarkus.properties`. A lock icon in the Quarkus docs = build-time (run `build`); no lock = runtime. Properties already mapped by RHBK (e.g. `quarkus.http.port`) are ignored — RHBK value takes precedence.

### Special characters & env-var key edge cases

- Disable expression evaluation by escaping `$` with `\`: value `my$$password` → `--db-password='my\$\$password'` (bash single quotes) / `--db-password="my\\$\\$password"` (double) / `kc.db-password=my\\$\\$password` (properties file).
- Windows paths: escape backslashes (`C:\\path\\to\\file`) or use forward slashes.
- PowerShell with special chars: `.\kc.bat start --log-level='"INFO,org.hibernate:debug"'`.
- Env-var key non-alphanumerics → `_`; mapped back by lower-casing and `_`→`-`. **Exception:** logging wildcards map `_`→`.` (e.g. `KC_LOG_LEVEL_PACKAGE_CLASS_NAME` → `kc.log-level-package.class.name`).
- To force a key, use a paired env var: `KC_<UNIQ>=value` + `KCKEY_<UNIQ>=key`, e.g. `KC_MYKEY=debug` and `KCKEY_MYKEY=log-level-package.class_name`.

---

## 2. Directory structure

Zip install root default: `rhbk-26.4.11`. Containers: `/opt/keycloak`. Relative paths are relative to install root.

| Dir | Purpose |
|---|---|
| `bin/` | Shell scripts: `kc.sh|bat`, `kcadm.sh|bat`, `kcreg.sh|bat` |
| `conf/` | Config files incl. `keycloak.conf`; many path options are relative here |
| `conf/truststores/` | Default path for `truststore-paths` |
| `data/` | Runtime info, e.g. transaction logs |
| `data/import/` | Realm import dir for `--import-realm` (`/opt/keycloak/data/import` in containers) |
| `logs/` | Default file-logging dir |
| `providers/` | User-provided JARs (extensions, JDBC drivers); `build` required after change |
| `themes/` | Admin Console customizations |
| `client/`, `lib/` | Used internally |

---

## 3. Starting the server

### Development mode

```bash
bin/kc.[sh|bat] start-dev
```
Defaults: HTTP enabled; strict hostname resolution disabled (`--hostname-strict false`); cache local (no distributed cache); theme/template caching disabled. **Never use in production.**

### Production mode

```bash
bin/kc.[sh|bat] start
```
Secure-by-default; **will not start without configuration** (errors out). Defaults: HTTP disabled (HTTPS essential); hostname expected; HTTPS/TLS expected. Example prod options are commented in `conf/keycloak.conf`.

### Initial admin user

Web frontend via localhost, or env vars `KC_BOOTSTRAP_ADMIN_USERNAME=<username>` / `KC_BOOTSTRAP_ADMIN_PASSWORD=***` (parsed at first startup; master realm). If admin already exists and the vars remain, RHBK logs an error and starts up normally. After the first admin, use Admin Console or `kcadm.[sh|bat]`.

### Optimizing startup

Run `build` explicitly (CI/CD) then `start --optimized`. Using `keycloak.conf` avoids CLI init steps for even faster start.

```bash
bin/kc.[sh|bat] build --db=postgres
# conf/keycloak.conf: db-url-host, db-username, db-password, hostname, https-certificate-file
bin/kc.[sh|bat] start --optimized
```

### System variables in realm config

Disallowed by default. Allow a comma list explicitly:
```bash
bin/kc.[sh|bat] start --spi-admin--allowed-system-variables=FOO,BAR
```
(Capability slated for removal in a future release.)

---

## 4. Hostname v2

Requires feature `hostname:v2` (enabled by default). Setting `hostname` is mandatory in production (security: prevents fraudulent-issuer / poisoned URLs).

```bash
bin/kc.[sh|bat] start --hostname my.keycloak.org            # scheme/port auto → https://my.keycloak.org:8443
bin/kc.[sh|bat] start --hostname https://my.keycloak.org    # full URL (e.g. behind proxy on 443)
bin/kc.[sh|bat] start --hostname https://my.keycloak.org:123/auth   # full URL with context path
```

Endpoint groups: **Frontend** (front channel — login, password reset, token binding), **Backend** (token, introspection, userinfo, JWKS), **Administration** (Admin Console, static resources, Admin REST API). Base URL impacts token issue/validation, redirect links, and OIDC discovery (`realms/{realm-name}/.well-known/openid-configuration`).

### Backchannel (internal URL) & edge termination

```bash
# Dynamic backchannel from request headers; public frontend stays https://my.keycloak.org
bin/kc.[sh|bat] start --hostname https://my.keycloak.org --hostname-backchannel-dynamic true
# Edge TLS-termination proxy (proxy↔KC over HTTP:8080)
bin/kc.[sh|bat] start --hostname https://my.keycloak.org --http-enabled true
```
`hostname-backchannel-dynamic` default `false` (backchannel = frontchannel). If set `true`, `hostname` must be a full URL.

### Separate Admin hostname

```bash
bin/kc.[sh|bat] start --hostname https://my.keycloak.org \
  --hostname-admin https://admin.my.keycloak.org:8443
```
Best practice: expose Admin REST API + Console on a different hostname/context-path than public frontend URLs to reduce attack surface; **block Admin REST API at the reverse proxy** if not public. `hostname-admin` does **not** prevent reaching Admin REST API via the frontend URL — restrict at proxy level. Hostname/proxy options change only generated URLs (JS/CSS, well-known, redirect URIs), **not** the listen ports.

### Dynamic resolution with proxy headers

```bash
bin/kc.[sh|bat] start --hostname-strict false --proxy-headers forwarded   # fully dynamic
bin/kc.[sh|bat] start --hostname my.keycloak.org --proxy-headers xforwarded # scheme/port dynamic, host fixed
bin/kc.[sh|bat] start --hostname https://my.keycloak.org --proxy-headers xforwarded # fixed URLs, headers set origin
```

### Validations

- `hostname` / `hostname-admin` must be full URLs (scheme + host); port validated only if present (else default 80/443).
- Prod profile (`start`): either `--hostname` or `--hostname-strict false` must be set explicitly. Dev (`start-dev`) defaults `--hostname-strict false`.
- If `--hostname` not configured: `hostname-backchannel-dynamic` must be `false` and `hostname-strict` must be `false`.
- If `hostname-admin` set, `hostname` must be a URL. If `hostname-backchannel-dynamic` true, `hostname` must be a URL.
- If `hostname` configured, `hostname-strict` is ignored.

### Troubleshooting

```bash
bin/kc.[sh|bat] start --hostname=mykeycloak --hostname-debug=true
# → http://mykeycloak:8080/realms/<realm>/hostname-debug
```

> **Air-gap:** use an internal FQDN such as `--hostname https://sso.example.internal`; keep backchannel internal with `--hostname-backchannel-dynamic true` for on-prem client traffic.

---

## 5. HTTP & TLS

PEM files take precedence over Java keystore when both are configured.

```bash
# PEM
bin/kc.[sh|bat] start --https-certificate-file=/path/certfile.pem --https-certificate-key-file=/path/keyfile.pem
# Keystore
bin/kc.[sh|bat] start --https-key-store-file=/path/existing-keystore-file
bin/kc.[sh|bat] start --https-key-store-password=***
```

If no keystore explicitly configured and `http-enabled=false`, RHBK looks for `conf/server.keystore`. If no password set, default password `password` is used (avoid in prod — use a vault / mounted secret).

Keystore extensions: `.p12`/`.pkcs12`/`.pfx` (pkcs12); `.jks`/`.keystore` (jks); `.key`/`.crt`/`.pem` (pem). If the extension doesn't match the type, set `https-key-store-type`.

| Option | Notes |
|---|---|
| `--https-protocols=<proto>[,...]` | Deprecated TLS protocols off by default; e.g. `TLSv1.3` |
| `--https-port=<port>` | HTTPS listen port (default `8443`) |
| `--https-certificates-reload-period` | Default reload every hour for `https-*` files; `java.time.Duration` / seconds / int+unit (`ms,h,m,s,d`); must be > 30s; `-1` disables |
| `--http-enabled=true` | Enable HTTP (port `8080`); required for edge TLS termination |
| `--http-max-queued-requests` | Limit queued requests; over-limit → immediate `503 Server not Available`. No limit by default |
| `--http-relative-path` | Change KC context path (e.g. `/auth`) |

Cert/key/keystore files referenced by `https-*` reload every hour by default for in-place rotation without restart.

Management-server TLS (`https-management-*`) options exist and are available only when `http-management-scheme` is inherited (see §16).

> **Air-gap:** mount certs from internal PKI (e.g. signed by `ca.example.internal`); rotate via the reload period rather than restarts. Store keystore password in a vault/secret (`***`).

---

## 6. Database

### Supported vendors (`--db` value)

| Database | `db` value | Tested | Supported |
|---|---|---|---|
| MariaDB Server | `mariadb` | 11.8 | 11.8/11.4/10.11/10.6 (LTS) |
| Microsoft SQL Server | `mssql` | 2022 | 2022, 2019 |
| MySQL | `mysql` | 8.4 | 8.4/8.0 (LTS) |
| Oracle Database | `oracle` | 23.5 | 23.x (23.5+), 19c (19.3+); Oracle RAC supported on same engine version |
| PostgreSQL | `postgres` | 17 | 17.x/16.x/15.x/14.x |
| EnterpriseDB Advanced | (EDB) | 17 | 17 |
| Amazon Aurora PostgreSQL | (postgres + AWS wrapper) | 17.5 | 17.x/16.x/15.x |
| Azure SQL Database / Managed Instance | (mssql) | latest | latest |

Default DB is `dev-file` — **development only, replace before production.** Using a Hibernate dialect version outside the table is unsupported.

### Drivers

Shipped except **Oracle** and **Microsoft SQL Server**. Overriding built-in drivers / supplying your own is unsupported (Oracle is the documented exception).

- Oracle: download `ojdbc17` + `orai18n` (e.g. 23.6.0.24.10), place in `providers/` (or `ADD` in Containerfile before `kc.sh build`).
- MSSQL: download `mssql-jdbc` (e.g. 13.2.1.jre11) into `providers/`.
- Amazon Aurora PostgreSQL: add `aws-advanced-jdbc-wrapper` JAR; set `db-url` to `jdbc:aws-wrapper:postgresql://...` and `db-driver=software.amazon.jdbc.Driver`; keep `failover`/`failover2` plugin.

> **Air-gap:** Maven Central / vendor download pages are unreachable. Pre-stage driver JARs into `providers/` from an internal artifact mirror (e.g. `nexus.example.internal`) before building the optimized image.

### Configuring

```bash
# Recommended: build + optimized start; minimal connect settings in conf/keycloak.conf
# db=postgres / db-username=keycloak / db-password=*** / db-url-host=keycloak-postgres
bin/kc.[sh|bat] build
bin/kc.[sh|bat] start --optimized

# Or single start (exposes password — not recommended)
bin/kc.[sh|bat] start --db postgres --db-url-host keycloak-postgres --db-username keycloak --db-password ***
```

Default schema `keycloak` (`--db-schema`). DB options also apply to `import`/`export`/`bootstrap-admin` (`--help`).

### JDBC URL & pool

```bash
bin/kc.[sh|bat] start --db postgres --db-url jdbc:postgresql://mypostgres/mydatabase
```
Escape shell-special chars (e.g. `;`) or set in the config file. PostgreSQL: RHBK auto-sets `targetServerType=primary` on the primary datasource (override in DB URL if needed); grant `SELECT` on `pg_class`, `pg_namespace` for efficient upgrades. MySQL/MariaDB: default max lifetime 7h50m (< default 8h `wait_timeout`); set `db-pool-max-lifetime` below your `wait_timeout`. MySQL 8.0.30+: disable `sql_generate_invisible_primary_key` (`OFF`).

### XA transactions

Non-XA is the default. Enable XA (build option):
```bash
bin/kc.[sh|bat] build --db=<vendor> --transaction-xa-enabled=true
```
XA recovery defaults enabled; logs at `KEYCLOAK_HOME/data/transaction-logs`. Containerized XA recovery is not fully supported without stable storage at that path. Azure SQL and MariaDB Galera don't rely on XA.

### Other DB tuning

| Need | Option |
|---|---|
| Cluster DB lock timeout (default/max 900s) | `--spi-dblock--jpa--lock-wait-timeout 900` |
| JPA migration strategy (manual/update/validate) | `--spi-connections-jpa--quarkus--migration-strategy=manual` |
| Emit init SQL file | `--spi-connections-jpa--quarkus--initialize-empty=false` |
| Migration export path | `--spi-connections-jpa--quarkus--migration-export=<path>/<file.sql>` |

### Multiple datasources

Define a `META-INF/persistence.xml` (transaction-type `JTA`, set `jakarta.persistence.jtaDataSource`) in your extension; configure RHBK with per-datasource option names, e.g. `db-username-<datasource>`. Required build option `db-kind-<name>`:
```bash
bin/kc.[sh|bat] start --db-kind-user-store=postgres
export KC_DB_KIND_USER_STORE=postgres
export KC_DB_USERNAME_USER_STORE=my-username
# special chars in name → KC_..._DB_KIND + KCKEY_..._DB_KIND=db-kind-user_store$marketing
```

---

## 7. Reverse proxy

Ports: `8443` (or `8080` with `--http-enabled=true`) for Admin UI/Account/SAML/OIDC/Admin REST API; `9000` for management (health/metrics). **Only proxy 8443/8080; do not proxy 9000.**

`--proxy-headers`:
- unset (default) — no proxy headers parsed; use for no-proxy or https passthrough.
- `forwarded` — parse `Forwarded` (RFC7239).
- `xforwarded` — parse `X-Forwarded-*` (`-For`, `-Proto`, `-Host`, `-Port`).

```bash
bin/kc.[sh|bat] start --proxy-headers forwarded
```

Without `--proxy-headers` (for anything beyond passthrough) origin-checked requests return **403 Forbidden**. With `forwarded`/`xforwarded`, your proxy must correctly set/overwrite those headers — misconfiguration is a security vulnerability. Don't use `forwarded`/`xforwarded` with passthrough. Edge termination requires `http-enabled`. `xforwarded`: `X-Forwarded-Port` takes precedence over the port in `X-Forwarded-Host`.

Context path: KC assumes the same context path as the proxy. Use full-URL `--hostname=https://my.keycloak.org/auth` or change KC's path with `--http-relative-path`.

### Sticky sessions

Stick on `AUTH_SESSION_ID` cookie (`<session-id>.<owner-node-id>`). If the proxy does affinity without reading backend cookies:
```bash
bin/kc.[sh|bat] start --spi-sticky-session-encoder--infinispan--should-attach-route=false
```
(Default `true` — node name attached to cookies.)

### Exposed path recommendations

| KC path | Expose | Reason |
|---|---|---|
| `/` | No | Avoids exposing admin paths |
| `/admin/` | No | Unnecessary attack vector |
| `/realms/` | Yes | OIDC endpoints |
| `/resources/` | Yes | Assets (may use CDN) |
| `/.well-known/` | Yes | RFC8414 metadata |
| `/metrics` | No | Attack vector |
| `/health` | No | Attack vector |

If `http-relative-path` is set, map `/.well-known/` (without prefix) to the prefixed path for RFC8414 discovery.

### Trusted proxies, PROXY protocol, client-cert lookup

```bash
bin/kc.[sh|bat] start --proxy-headers forwarded --proxy-trusted-addresses=192.168.0.32,127.0.0.0/8
bin/kc.[sh|bat] start --proxy-protocol-enabled true   # HA PROXY protocol; cannot combine with --proxy-headers
```

X.509 via TLS-termination proxy header (security-sensitive; prefer passthrough). Providers: `apache`, `haproxy`, `nginx`.
```bash
bin/kc.[sh|bat] build --spi-x509cert-lookup--provider=<provider>
bin/kc.[sh|bat] start --spi-x509cert-lookup--<provider>--ssl-client-cert=SSL_CLIENT_CERT \
  --spi-x509cert-lookup--<provider>--ssl-cert-chain-prefix=CERT_CHAIN \
  --spi-x509cert-lookup--<provider>-certificate-chain-length=10
```
Provider options: `ssl-client-cert`, `ssl-cert-chain-prefix`, `certificate-chain-length`, `trust-proxy-verification` (only if proxy verifies the chain), `cert-is-url-encoded`. NGINX provider rebuilds the chain from the RHBK truststore (see §10).

---

## 8. Bootstrapping & recovering an admin account

Bootstrapped accounts are **temporary** — remove manually after gaining permanent access. UI banners/labels/logs flag them.

### At startup (master realm, first start only)

```bash
bin/kc.[sh|bat] start --bootstrap-admin-username tmpadm --bootstrap-admin-password ***
bin/kc.[sh|bat] start-dev --bootstrap-admin-client-id tmpadm --bootstrap-admin-client-secret ***
```
Standard config options (any source). Created only when master realm doesn't yet exist.

### Dedicated `bootstrap-admin` command (offline recovery)

Stop **all** nodes first. Recommended: use the same options the server starts with (e.g. `db`). With `--optimized`, drop build-time options. Without `--optimized` the command may implicitly create/update an optimized build (affects next server start).

```bash
bin/kc.[sh|bat] bootstrap-admin user
bin/kc.[sh|bat] bootstrap-admin user --username tmpadm --password:env PASS_VAR
bin/kc.[sh|bat] bootstrap-admin service
bin/kc.[sh|bat] bootstrap-admin service --client-id tmpclient --client-secret:env=SECRET_VAR
bin/kc.[sh|bat] bootstrap-admin user --username tmpadm --no-prompt   # disable prompt
```

Defaults: username and client ID default to `temp-admin`. Env: `--username:env`, `--password:env`, `--client-id:env`, `--client-secret:env` (client secret must be an env var for `service`).

### Recovering a realm with enforced advanced auth

```bash
bin/kcadm.[sh|bat] config credentials --server http://localhost:8080 --realm master \
  --client <service_account_client_name> --secret ***
bin/kcadm.[sh|bat] get users/{userId}/credentials -r {realm-name}     # find type=otp credentialId
bin/kcadm.[sh|bat] delete users/{userId}/credentials/{credentialId} -r {realm-name}
```

---

## 9. Logging

JBoss Logging; handlers `console` (default on), `file`, `syslog`, parent `root`.

### Levels & root/category

`FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL, OFF`. Case-insensitive in `log-level`; last occurrence wins.
```bash
bin/kc.[sh|bat] start --log-level=<root-level>
bin/kc.[sh|bat] start --log-level="INFO,org.hibernate:debug,org.hibernate.hql.internal.ast:info"
bin/kc.[sh|bat] start --log-level-org.keycloak=trace   # individual option; takes precedence over log-level
```
Env form: `KC_LOG_LEVEL_ORG_KEYCLOAK=trace` (uppercase, dots→underscores).

### Enabling handlers & per-handler levels

```bash
bin/kc.[sh|bat] start --log="console,file,syslog"
```
Per-handler level options: `log-console-level`, `log-file-level`, `log-syslog-level` (lowercase values only). Handler levels **restrict** (cannot exceed) the root `log-level`; default handler level is `all`.
```bash
bin/kc.[sh|bat] start --log=console,file --log-level=debug --log-console-level=info
```

### JSON output & async

```bash
bin/kc.[sh|bat] start --log-console-output=json --log-console-json-format=ecs   # default|ecs
bin/kc.[sh|bat] start --log-async=true                                          # all handlers
bin/kc.[sh|bat] start --log-console-async=true --log-file-async-queue-length=512 # default queue 512
```

### Console format

Default template: `%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c] (%t) %s%e%n`. Symbols include `%c %d{} %e %h %H %i %m %n %N %p %r %s %t %t{id} %z{zone} %L`.
```bash
bin/kc.[sh|bat] start --log-console-format="'%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c{3.}] (%t) %s%e%n'"
bin/kc.[sh|bat] start --log-console-color=true
```

### File logging

Default file `keycloak.log` in `data/log`. `--log-file=<path>`, `--log-file-format`, `--log-file-level`. If the dir is not writable, server starts but logs an error and no file is created.

### Syslog (RFC 5424)

```bash
bin/kc.[sh|bat] start --log="console,syslog" --log-syslog-endpoint=myhost:12345 \
  --log-syslog-app-name=kc-p-itadmins --log-syslog-protocol=tcp --log-syslog-type=rfc5424
```
Defaults: host `localhost`, port `514`, app-name `keycloak`, protocol `tcp` (also `udp`, `ssl-tcp`), type `rfc5424` (also `rfc3164`). `--log-syslog-counting-framing` = `protocol-dependent` (default) / `true` / `false`. `--log-syslog-max-length` default `2048B` (RFC5424) / `1024B` (RFC3164). `--log-syslog-output=json`.

> **Air-gap:** point `--log-syslog-endpoint=siem.example.internal:514`; use `ssl-tcp` toward an internal collector; avoid the `long` HTTP access pattern in prod (sensitive headers).

### HTTP access logging

```bash
bin/kc.[sh|bat] start --http-access-log-enabled=true --http-access-log-pattern=combined
bin/kc.[sh|bat] start --http-access-log-exclude='/realms/my-internal-realm/.*'
```
Written at `INFO` (category `org.keycloak.http.access-log`). Patterns: `common` (default), `combined`, `long`, or custom. `Authorization` header and selected KC cookies (`AUTH_SESSION_ID`, `KC_AUTH_SESSION_HASH`, `KEYCLOAK_IDENTITY`, `KEYCLOAK_SESSION`, and `*_LEGACY` variants) are auto-masked — masking list may be incomplete.

### MDC (preview)

```bash
bin/kc.[sh|bat] start --features=log-mdc --log-mdc-enabled=true   # keys via log-mdc-keys
```

---

## 10. Trusted certificates (truststore)

The Java default truststore is always trusted. Add internal/self-signed CAs as PEM or **unencrypted** PKCS12 (`.p12`/`.pfx`/`.pkcs12`) into `conf/truststores/` (recursively scanned). Becomes the system default via `javax.net.ssl` and the internal RHBK default.

```bash
bin/kc.[sh|bat] start --truststore-paths=/opt/truststore/myTrustStore.pfx,/opt/other-truststore/myOtherTrustStore.pem
```
Prefer absolute paths (relative is to launch dir).

`--tls-hostname-verifier`: `DEFAULT` (default; wildcard matches same level, public-suffix rules), `ANY` (no verification — not for prod), `WILDCARD` (deprecated), `STRICT` (deprecated). Does **not** apply to LDAP secure connections (always strict).

> **Air-gap:** internal CAs (`ca.example.internal`) are not in the JRE default store — drop their PEM/PKCS12 into `conf/truststores/` so outgoing TLS (LDAP, external IdP brokering, OTLP) validates.

---

## 11. mTLS (Mutual TLS)

Disabled by default. Truststore + clients shared across **all realms** (no per-realm truststore).

```bash
bin/kc.[sh|bat] start --https-client-auth=<none|request|required>
```
`required` = always demand a cert, fail if absent; `request` = accept without, validate if present. Management interface inherits mTLS; override with `https-management-client-auth`.

Dedicated mTLS truststore:
```bash
bin/kc.[sh|bat] start --https-trust-store-file=/path/to/file --https-trust-store-password=***
```
Truststore extensions: `.p12`/`.pkcs12`/`.pfx`; `.jks`/`.truststore`; `.ca`/`.crt`/`.pem`. Non-matching extension → set `https-key-store-type`. For RHBK-as-client mTLS (e.g. brokered IdP token endpoint), configure the outgoing HTTP client (§12).

---

## 12. Outgoing HTTP requests

```bash
bin/kc.[sh|bat] start --spi-connections-http-client--default--<option>=<value>
```

| Option | Default | Notes |
|---|---|---|
| `establish-connection-timeout-millis` | Not set | |
| `socket-timeout-millis` | `5000` | inactivity between packets |
| `connection-pool-size` | `128` | |
| `max-pooled-per-route` | `64` | per host |
| `connection-ttl-millis` | Not set | |
| `max-connection-idle-time-millis` | `900000` | `-1` disables |
| `disable-cookies` | `true` | |
| `allow-redirects` | `false` | deprecated; keep `false` to avoid SSRF |
| `client-keystore` | — | client certs for mTLS |
| `client-keystore-password` | — | required when keystore set |
| `client-key-password` | — | required when keystore set |
| `proxy-mappings` | — | see below |
| `disable-trust-manager` | `false` | dev only — disables SSL cert verification |

Proxy via env: `HTTP_PROXY`, `HTTPS_PROXY` (precedence over HTTP regardless of scheme), `NO_PROXY` (comma list, subdomains excluded). Lowercase env wins over uppercase.

Regex proxy mappings (`hostname-pattern;proxy-uri`, special `NO_PROXY`; first match wins):
```bash
bin/kc.[sh|bat] start --spi-connections-http-client--default--proxy-mappings='.*\\.(google|googleapis)\\.com;http://www-proxy.acme.com:8080'
```

> **Air-gap:** route brokered IdP/userinfo/JWKS fetches through the internal forward proxy: `HTTPS_PROXY=http://proxy.example.internal:8080`, `NO_PROXY=example.internal`. Add internal CAs to the truststore (§10) instead of `disable-trust-manager`.

---

## 13. FIPS 140-2 support

Run on a FIPS-enabled system (`fips-mode-setup --check` / `--enable`); OpenJDK then runs in FIPS mode. RHBK uses BouncyCastle internally; the default BC is **not** FIPS-compliant — add BCFIPS JARs to `KEYCLOAK_HOME/providers`:

- `bc-fips` 2.1.2, `bctls-fips` 2.1.22, `bcpkix-fips` 2.1.10, `bcutil-fips` 2.1.5.

Keystores: PKCS12 works in non-approved mode (can store PBE keys for KeyStore Vault / Config Source). BCFKS requires BCFIPS libs + custom security file (`securerandom.strongAlgorithms=PKCS11:SunPKCS11-NSS-FIPS`).

```bash
# non-approved (non-strict) — default keystore/truststore type PKCS12
bin/kc.[sh|bat] start --features=fips --hostname=localhost --https-key-store-password=*** \
  --log-level=INFO,org.keycloak.common.crypto:TRACE,org.keycloak.crypto:TRACE
# strict (approved) — default keystore/truststore type BCFKS
bin/kc.[sh|bat] start --features=fips --fips-mode=strict
```

`fips-mode` auto-set to `non-strict` when `fips` feature enabled; `strict` = approved mode. Non-default keystore type → set `--https-key-store-type=bcfks` (and truststore type as needed). Verify via TRACE: `KC(BCFIPS ... Approved Mode, FIPS-JVM: enabled)`.

### Strict-mode restrictions

- No `jks`/`pkcs12` keystores; use `bcfks`.
- User passwords ≥ 14 chars (PBKDF2 ≥ 112 bits). Allow shorter via `--spi-password-hashing--pbkdf2-sha512--max-padding-length=14` (also `pbkdf2-sha256` for migrated users).
- RSA keys ≥ 2048 bits (realm/client/IdP). HMAC SHA-XXX ≥ 112 bits (client secrets ≥ 14 chars). JWE `RSA1_5` disallowed (use `RSA-OAEP`/`RSA-OAEP-256`).
- SAML needs `XMLDSig`; Kerberos needs `SunJGSS` (not fully FIPS-compliant → `KERBEROS` auto-disabled on FIPS platforms when the provider is unavailable). Add providers in `JAVA_HOME/conf/security/java.security` or a custom `-Djava.security.properties=...`.

### CLI on FIPS host

Copy BCFIPS JARs into `bin/client/lib/`:
```bash
cp $KEYCLOAK_HOME/providers/bc-fips-*.jar $KEYCLOAK_HOME/bin/client/lib/
cp $KEYCLOAK_HOME/providers/bctls-fips-*.jar $KEYCLOAK_HOME/bin/client/lib/
cp $KEYCLOAK_HOME/providers/bcutil-fips-*.jar $KEYCLOAK_HOME/bin/client/lib/
```

### Containers / migration

Host must be in FIPS mode (container inherits). Build a custom image adding BCFIPS JARs, keystore, and `kc.java.security`, then `RUN kc.sh build --features=fips --fips-mode=strict`. Supported on FIPS-enabled RHEL 8 (`ubi8`) and RHEL 9 (`ubi9`). Migration from non-FIPS: default hash `argon2` is **not** FIPS-supported — set realm password policy to `pbkdf2-sha512` early or have users reset passwords; remove/disable Kerberos.

> **Air-gap:** stage BCFIPS JARs from an internal mirror; bake them into the optimized image during build.

---

## 14. Vault

Two SPI impls: **file** (Kubernetes/OpenShift secrets as mounted files) and **keystore** (Java KeyStore, password-encrypted). Used for SMTP password, LDAP bind credential, OIDC IdP client secret in the Admin Console.

```bash
bin/kc.[sh|bat] build --vault=file        # or --vault=keystore
bin/kc.[sh|bat] start --vault-dir=/my/path                              # file vault
bin/kc.[sh|bat] start --vault-file=/path/keystore.p12 --vault-pass=*** --vault-type=PKCS12  # keystore vault (type optional, default PKCS12)
```

File naming (default resolver `REALM_UNDERSCORE_KEY`): `${vault.<realmname>_<secretname>}`; double underscores within names. Keystore secret creation: `keytool -importpass -alias <realm-name>_<alias> -keystore keystore.p12 -storepass ***`. Reference in realm config as `${vault.realm-name_alias}`.

> **Air-gap:** mount internal secrets as files into the file vault dir; reference `${vault.<realm>_ldapBc}` for the LDAP bind credential to `ldap.example.internal` instead of plaintext.

---

## 15. Health checks & metrics

Both exposed on the **management interface** (port `9000`).

### Health (build option `health-enabled`)

```bash
bin/kc.[sh|bat] build --health-enabled=true
bin/kc.[sh|bat] build --health-enabled=true --metrics-enabled=true   # DB check requires metrics
```
Endpoints `/health/live`, `/health/ready`, `/health/started`, `/health`. `200 OK` / `503 Service Unavailable`; JSON `{"status":"UP","checks":[...]}`. Monitor via external HTTP (container image strips `curl`); use Kubernetes HTTP Probe (not a liveness command). Available check: **Database** (requires metrics).

```bash
curl --head -fsS http://localhost:9000/health/ready
```

### Metrics (build option `metrics-enabled`)

```bash
bin/kc.[sh|bat] start --metrics-enabled=true
```
Endpoint `/metrics`; `application/openmetrics-text` (Prometheus/OpenMetrics). Groups: System, JVM, Database, HTTP, Cache. Cache metrics auto-exposed when metrics enabled; histograms via `--cache-metrics-histograms-enabled=true`. Cluster size metric `vendor_cluster_size`.

> **Air-gap:** scrape `9000/metrics` and `9000/health` only from the internal monitoring network (`prometheus.example.internal`); do not proxy 9000 publicly.

---

## 16. Management interface

Turns on when something is exposed (health/metrics). Inherits from default HTTP server when not set.

| Option | Default | Notes |
|---|---|---|
| `http-management-port` | `9000` | |
| `http-management-relative-path` | inherits `http-relative-path` | e.g. `/management` → `/management/metrics`, `/management/health` |
| `http-management-scheme` | inherits (HTTPS if main TLS set) | set `http` to disable HTTPS on mgmt |
| `https-management-*` | inherit from main HTTP server | TLS params (see §5) |
| `https-management-client-auth` | inherits mTLS | override mgmt mTLS |
| `legacy-observability-interface` | `false` | **DEPRECATED**; `true` exposes health/metrics on the main server (not recommended) |

Management interface runs only HTTP **or** HTTPS, not both. Prefer the management interface over exposing health/metrics on the main server.

---

## 17. Enabling/disabling features

```bash
bin/kc.[sh|bat] build --features="docker,token-exchange"
bin/kc.[sh|bat] build --features="preview"            # all preview
bin/kc.[sh|bat] build --features-disabled="impersonation"
```
A feature cannot be in both `features` and `features-disabled`. Versioned (`feature:v1`) pins exactly; unversioned picks by precedence: highest default-supported → non-default-supported → deprecated → preview → experimental. Disabling a feature disables all its versions.

Selected defaults-on: `account-api:v1`, `account:v3`, `admin-api:v1`, `admin:v2`, `admin-fine-grained-authz:v2`, `authorization:v1`, `ciba:v1`, `device-flow:v1`, `dpop:v1`, `hostname:v2`, `impersonation:v1`, `kerberos:v1`, `login:v2`, `opentelemetry:v1`, `organization:v1`, `par:v1`, `passkeys:v1`, `persistent-user-sessions:v1`, `recovery-codes:v1`, `rolling-updates:v1`, `step-up-authentication:v1`, `token-exchange-standard:v2`, `update-email:v1`, `user-event-metrics:v1`, `web-authn:v1`.

Disabled-by-default (supported): `docker:v1`, `fips:v1`, `multi-site:v1`. Preview: `admin-fine-grained-authz:v1`, `client-auth-federated:v1`, `client-secret-rotation:v1`, `log-mdc:v1`, `rolling-updates:v2`, `scripts:v1`, `spiffe:v1`, `token-exchange:v1`. Deprecated: `instagram-broker:v1`, `login:v1`, `logout-all-sessions:v1`, `passkeys-conditional-ui-authenticator:v1`.

---

## 18. Importing & exporting realms

`import`/`export` are partial server launches — run with **server stopped**, not on the same machine as a running instance (port conflicts). For > 50,000 users, export to a **directory**, not a single file. DB connection options apply (`--help`); build-time option changes trigger implicit rebuild unless `--optimized`.

```bash
# Export
bin/kc.[sh|bat] export --dir <dir>                                  # one file per realm
bin/kc.[sh|bat] export --dir <dir> --users different_files --users-per-file 100
bin/kc.[sh|bat] export --file <file>                                # all realms one file
bin/kc.[sh|bat] export --dir <dir> --realm my-realm                 # single realm

# Import (stop all nodes before --override)
bin/kc.[sh|bat] import --dir <dir>                                  # --override default true
bin/kc.[sh|bat] import --dir <dir> --override false
bin/kc.[sh|bat] import --file <file>
```

`--users` strategies: `different_files` (default; `--users-per-file` default `50`), `skip`, `realm_file`, `same_file`. Naming: `<realm>-realm.json`, `<realm>-users-<n>.json`, `<realm>-federated-users-<n>.json`. Placeholders `${MY_REALM_NAME}` resolve from env (no restriction on which vars — beware exposing secrets).

### Import at startup

```bash
bin/kc.[sh|bat] start --import-realm
```
Imports `.json` files from `data/import` (`/opt/keycloak/data/import` in containers; sub-dirs ignored). Existing realm → import skipped. Server doesn't fully start until imports complete.

Admin Console export/import is **partial** (no users; values masked with `*`) and not suitable for backups — only CLI exports are.

> **Air-gap / GitOps:** keep realm JSON in an internal git repo; use `${ENV}` placeholders for `example.internal` hostnames and `***` secrets; import at startup from a mounted `data/import` volume.

---

## 19. Distributed caches (server-config touch points)

`start` enables caching (`--cache=ispn`, default stack `jdbc-ping`); `start-dev` forces `--cache=local` (dev/test only). Config file `conf/cache-ispn.xml` (override via `--cache-config-file`). Caches: local (`realms`, `users`, `authorization`, `keys`, `crl`), replicated (`work`), distributed (`authenticationSessions`, `sessions`, `clientSessions`, `offlineSessions`, `offlineClientSessions`, `loginFailures`, `actionTokens`).

```bash
bin/kc.[sh|bat] start --cache=ispn --cache-stack=jdbc-ping
bin/kc.[sh|bat] start --cache-embedded-offline-sessions-max-count=1000
```
TLS for TCP-based stacks is on by default (auto self-signed RSA 2048, TLS 1.3, certs in DB, 60-day validity, 30-day rotation via `cache-embedded-mtls-rotation-interval-days`); disable with `cache-embedded-mtls-enabled=false`. Remote cache CLI: `cache-remote-host/-port/-username/-password`, `cache-remote-tls-enabled`. Ports `7800` (unicast) and FD detection; bind via `cache-embedded-network-bind-address`. Topology: `spi-cache-embedded--default--site-name|rack-name|machine-name`.

> **Air-gap:** keep cache transport on the internal cluster network; point remote cache at `infinispan.example.internal`; keep mTLS enabled (or rely on service-mesh) between nodes.

---

## 20. Tracing (OpenTelemetry, preview)

```bash
bin/kc.[sh|bat] start --tracing-enabled=true --features=opentelemetry
```
Defaults: gRPC batch export to `http://localhost:4317`; service name `keycloak` (`tracing-service-name` > `service.name` in `tracing-resource-attributes`). Samplers: `always_on`, `always_off`, `traceidratio` (default, `tracing-sampler-ratio` default `1.0`, range `(0,1]`), `parentbased_*`. Trace info appears in all log handlers (`traceId`, `sampled`); hide per handler with `--log-<handler>-include-trace=false`.

> **Air-gap:** set the OTLP endpoint to an internal collector, e.g. `otel-collector.example.internal:4317`; lower `tracing-sampler-ratio` in prod.

---

## 21. Running in a container (RHBK-specific)

Image `registry.redhat.io/rhbk/keycloak-rhel9:26.4`; **only OpenShift is supported** for running (other Kubernetes distros unsupported). Podman is for build/customize only — **not** supported for running in production.

```dockerfile
FROM registry.redhat.io/rhbk/keycloak-rhel9:26.4 AS builder
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true
ENV KC_DB=postgres
WORKDIR /opt/keycloak
RUN /opt/keycloak/bin/kc.sh build
FROM registry.redhat.io/rhbk/keycloak-rhel9:26.4
COPY --from=builder /opt/keycloak/ /opt/keycloak/
ENV KC_DB=postgres
ENV KC_DB_URL=<DBURL>
ENV KC_HOSTNAME=localhost
ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
```

```bash
podman build . -t mykeycloak -f Containerfile
podman run --name mykeycloak -p 8443:8443 -p 9000:9000 \
  -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=*** \
  mykeycloak start --optimized --hostname=localhost
```

- Custom providers: `ADD` JAR to `/opt/keycloak/providers` **before** `RUN kc.sh build`.
- Base image strips `microdnf`/`dnf`/`rpm` (hardening). Prefer `ADD` over `RUN curl`; install RPMs only via a two-stage ubi-micro chroot copy.
- Custom ENTRYPOINT scripts must `exec /opt/keycloak/bin/kc.sh start "$@"` (PID 1, receives SIGTERM for graceful shutdown — else cache inconsistency/data loss).
- Different external port: set full-URL hostname, e.g. `-p 3000:8443 ... start --optimized --hostname=https://localhost:3000`.
- Memory: heap uses `-XX:MaxRAMPercentage=70`/`-XX:InitialRAMPercentage=50` of container memory — **always set a memory limit** (≥ 750 MB; recommended 2 GB for small prod). Override via `JAVA_OPTS_KC_HEAP`.
- Initial admin only via `KC_BOOTSTRAP_ADMIN_USERNAME`/`KC_BOOTSTRAP_ADMIN_PASSWORD` (no localhost in container).
- `--import-realm` reads `/opt/keycloak/data/import` (typically Dev-mode use).
- Docker timestamp issue with provider JARs on `start --optimized`: `RUN touch -m --date=@<epoch> /opt/keycloak/providers/*` before `build`.

> **Air-gap:** mirror `registry.redhat.io/rhbk/keycloak-rhel9:26.4` into an internal registry (`registry.example.internal/rhbk/...`); pre-stage provider/driver JARs from an internal mirror; bake an optimized image so no pulls/builds happen at start.

---

## 22. Rolling-update compatibility check

```bash
bin/kc.[sh|bat] update-compatibility metadata --file=/path/to/file.json   # old config/version
bin/kc.[sh|bat] update-compatibility check --file=/path/to/file.json      # new config/version
```
Accepts all `start` options — include **every** option (env + CLI) or the result is wrong. Use the exit code in pipelines:

| Exit | Meaning |
|---|---|
| `0` | Rolling Update possible |
| `1` | Unexpected error (missing/corrupt metadata) |
| `2` | Invalid CLI option |
| (non-zero) | Rolling Update not possible — recreate (shut down before applying) |

Recreate-always on feature toggle: `multi-site:v1`, `persistent-user-sessions:v1`. Recreate on version change: `login:v1`, `login:v2`, `passkeys-conditional-ui-authenticator:v1`. Recreate config options include cache stack/config-file/mTLS-enabled, remote-cache, `db`/`db-schema`/db-name/host/port. `--db-url` changes can roll (take care: host/port/db-name divergence → data issues). Patch-release rolling updates (preview): `update-compatibility check --features=rolling-updates:v2` (enable sticky sessions). Today rolling is possible only when the RHBK version is unchanged.

---

## 23. Production checklist (Ch. 2)

- **TLS everywhere** — never expose endpoints over plain HTTP; secure cache communication too.
- **Hostname** — set the public `hostname` (v2); expose Admin REST API/Console on a separate hostname/context-path and block at the proxy if not public.
- **Reverse proxy** — set `--proxy-headers` correctly; expose only required paths (§7); hide `/admin/`, `/metrics`, `/health`.
- **Load shedding** — set `http-max-queued-requests` (no limit by default); also shed at the load balancers.
- **Production database** — replace `dev-file` with a supported vendor (§6).
- **Clustering** — run ≥ 2 nodes (JGroups + Infinispan, TLS between nodes by default); open required cache ports (§19).
- **IP stack** — `export JAVA_OPTS_APPEND="-Djava.net.preferIPv4Stack=true"` (IPv4 only) or `"-Djava.net.preferIPv4Stack=false -Djava.net.preferIPv6Addresses=true"` (IPv6).
- **Optimized image** — `build` then `start --optimized`; keep secrets out of build options.
- **Secrets** — use a vault / mounted secret (not plaintext CLI/conf) for keystore and DB passwords.

---

### Relevant produced file

_Source: Red Hat build of Keycloak 26.6 Server Configuration Guide (docs.redhat.com), distilled offline._
