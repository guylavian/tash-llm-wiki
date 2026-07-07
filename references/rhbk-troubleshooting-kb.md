# RHBK / RH-SSO Troubleshooting — Offline KB Reference

Red Hat Knowledge-Base **Solutions** for Red Hat build of Keycloak (RHBK) and legacy RH-SSO, distilled offline.
Backed by the bundled local KB (`kb/`): **1,030 KB Solutions** total — **40 with public bodies** (distilled into
actionable fixes below) and **990 subscriber-gated** (kept as pointers; open the URL with a Red Hat login for the
resolution). This file supersedes the earlier search-snippet pointer index.

## Querying the full KB offline

The 28 fixes below are the public-body solutions. For the full 1,030 (incl. gated pointers):

```bash
cd kb
python3 rhbk_kb.py search "<your symptom or component>" --gated   # ranked hits across all solutions + docs
python3 rhbk_kb.py show <kb-id>                                   # full body (or URL if gated)
```
The complete categorized list of all 1,030 (IDs + titles + gated/public) is in **`kb/solutions_by_area.md`**.

## Verified fixes — public KB bodies (28)

Each entry is distilled verbatim from the public KB body (symptom → cause → fix). Air-gap implications noted inline;
secrets shown as `***`, hosts as `example.internal`.

### Infrastructure — operator, DB, TLS, proxy, FIPS, image/build

### KB 7142778 — Oracle JDBC failover fails over TCPS at Keycloak startup
- **Applies to:** RHBK 26.0.x/26.2.x/26.4.x with Oracle Database (JDBC thin driver, TCPS/TLS)
- **Symptom:** Startup fails with `ORA-17002: I/O error: sleep interrupted, Authentication lapse 0 ms`; driver retries the first SCAN host only and never reaches the second `ADDRESS` despite `FAILOVER=ON`.
- **Cause:** Known defect in Oracle JDBC thin driver 23.2.0.0.0 — after a Refuse packet, `NSProtocolNIO.establishConnectionAfterRefusePacket` is interrupted during the TLS handshake (`InterruptedIOException: sleep interrupted`) instead of failing over.
- **Fix:** Update the Oracle JDBC driver to a version per the RHBK Supported Configurations article (the bundled 23.2.0.0.0 is affected). Confirm `DriverVersion=23.2.0.0.0` in startup logs and replace the JAR in the providers directory. (Air-gap: stage the corrected driver JAR in your internal mirror before deployment.)
- **Relevant guide:** server-configuration

### KB 7142577 — Uneven pod load / LOGIN_ERROR flood behind Kong/NGINX ingress
- **Applies to:** RHBK 26.x clustered behind Kong / NGINX Ingress
- **Symptom:** One pod shows much higher CPU than others; all pods flooded with `LOGIN_ERROR`/`user_not_found` warnings; 100% error rate, near-zero useful throughput.
- **Cause:** Load test (or client) sends auth to `POST /realms/master/.../token` with `client_id=admin-cli`; the reserved master realm has no application users, so every failed login still runs the full DB lookup + Infinispan check + thread-pool slot.
- **Fix:** Point auth at the application realm: `POST /realms/<application-realm>/protocol/openid-connect/token` with the app's registered client ID and a valid user; make each client/thread do its own independent login (JMeter: HTTP Cookie Manager clears cookies each iteration); clear any brute-force lockout on the admin account.
- **Relevant guide:** high-availability

### KB 7141508 — AD Kerberos/SPNEGO SSO on an IdM-enrolled RHEL host
- **Applies to:** RHBK 26.x on RHEL enrolled in Red Hat IdM (FreeIPA), users in separate Microsoft AD domain
- **Symptom:** Browser SPNEGO logins fail with `GSSException ... Cannot find key of appropriate type to decrypt AP-REQ` or "no user storage provider that handles kerberos credentials," because the JVM defaults to the IdM-managed `/etc/krb5.conf`.
- **Cause:** Java reads the host OS `/etc/krb5.conf` (pointing at the IdM realm); also restrictive keytab permissions block the Keycloak user from reading it.
- **Fix:** Create AD keytab `ktpass -out keycloak-ad.keytab -princ HTTP/sso.example.internal@AD.EXAMPLE.INTERNAL -mapuser keycloak-svc -pass *** -crypto AES256-SHA1 -ptype KRB5_NT_PRINCIPAL`; write an isolated `/opt/keycloak/conf/krb5-ad.conf` with `default_realm = AD.EXAMPLE.INTERNAL`; `chown keycloak:keycloak` + `chmod 600` the keytab; append `JAVA_OPTS_APPEND="-Djava.security.krb5.conf=/opt/keycloak/conf/krb5-ad.conf"`; set Browser flow Kerberos to ALTERNATIVE and enable "Allow Kerberos authentication" on the AD LDAP provider (Realm/Server Principal/KeyTab). No IdM↔AD forest trust required.
- **Relevant guide:** server-administration

### KB 7138771 — Admin console lockout after enabling Client Authentication on security-admin-console
- **Applies to:** RHBK 26.x, master realm `security-admin-console` client
- **Symptom:** Admin WebUI login fails; server logs show `type="CODE_TO_TOKEN_ERROR" ... clientId="security-admin-console" ... error="invalid_client_credentials"`.
- **Cause:** Enabling "Client authentication" converted the public `security-admin-console` client into a confidential client; the browser UI has no client secret, so the code-to-token exchange fails.
- **Fix:** Preferred (no restart) via admin-cli: `./kcadm.sh update clients/<ID> -r master -s publicClient=true -s 'attributes."pkce.code.challenge.method"=""'`. If admin has OTP (CLI fails with `invalid_grant`), revert in PostgreSQL: `UPDATE client SET public_client = true WHERE id='<CLIENT_ID>';` then `DELETE FROM client_attributes WHERE client_id='<CLIENT_ID>' AND name='pkce.code.challenge.method';` and restart RHBK to flush cache. (Test in lower env first; air-gapped restart flushes the in-memory cache.)
- **Relevant guide:** server-administration

### KB 7135122 — FIPS mode startup fails with UnsatisfiedLinkError from wrong Bouncy Castle libs
- **Applies to:** RHBK 26.x in FIPS mode
- **Symptom:** Server fails to start: `Fips1402StrictCryptoProvider` config error, `java.lang.UnsatisfiedLinkError: /tmp/bc-fips-jni.../libbc-probe.so: failed to map segment from shared object`.
- **Cause:** Bundled Bouncy Castle FIPS libraries were replaced with external/newer versions (e.g., bc-fips 2.1.x) from Maven Central / the BC website, which are not certified with the product runtime.
- **Fix:** Use only the bundled BC FIPS libraries; remove any externally placed versions from the library path/classpath. For RHBK 26.2.10 the bundled versions are `bc-fips: 2.0.0`, `bctls-fips: 2.0.19`, `bcpkix-fips: 2.0.7`, `bcutil-fips: 2.0.3`. (Air-gap: never substitute jars from a public mirror; keep the product-shipped jars.)
- **Relevant guide:** server-configuration

### KB 7135124 — Admin login "Invalid credentials" after enabling FIPS due to Argon2 hash
- **Applies to:** RHBK 26.x switched to FIPS mode
- **Symptom:** Admin login shows "Invalid credentials" with correct password; TRACE log shows `PasswordHashProvider argon2 not found for user admin`.
- **Cause:** Existing admin password was hashed with Argon2 (default in non-FIPS), which is not FIPS-compliant and is disabled in FIPS mode, so the hash cannot be verified.
- **Fix:** Restart out of FIPS mode, log in, create a new admin (e.g. `admin_fips`) whose password uses a FIPS-compliant algorithm (PBKDF2; strict FIPS typically requires >=14 chars); restart with `--features=fips --fips-mode=strict`; verify login with the new user and delete the old Argon2-hashed admin.
- **Relevant guide:** server-configuration

### KB 7135882 — Expired/logged-out user sessions linger in PostgreSQL
- **Applies to:** RHBK 26.x (25/26 with persistent-user-sessions enabled by default) on PostgreSQL
- **Symptom:** Sessions vanish from the Admin UI but remain in the DB (`user_session` count >> UI count) for ~10–15 min; possible DB saturation/connection-pool exhaustion under high churn.
- **Cause:** Lazy/asynchronous cleanup — the `UserSessionPersister` background task batch-deletes expired sessions on a schedule (default 900s), so deletion lags eviction from the Infinispan cache.
- **Fix:** Tune in `conf/keycloak.conf`: `spi-user-sessions-jpa-expiration-cleanup-interval=300` and `spi-user-sessions-jpa-expiration-batch-size=5000`. Optionally move sessions to RAM with `--features-disabled=persistent-user-sessions` (all users logged out if all nodes restart together); align SSO Session Idle/Max; increase autovacuum and ensure indexes on `max_expiration`/`timestamp` of `user_session`.
- **Relevant guide:** server-configuration

### KB 7078215 — Configure OpenShift HPA for RHBK
- **Applies to:** RHBK 26.2+ on OpenShift Container Platform 4.x with Horizontal Pod Autoscaler
- **Symptom:** Need to dynamically add/remove RHBK pods as demand changes.
- **Cause:** HPA support for the Keycloak CR was added in RHBK 26.2.
- **Fix:** Create a `HorizontalPodAutoscaler` (apiVersion `autoscaling/v2`) with `scaleTargetRef` pointing at `apiVersion: k8s.keycloak.org/v2alpha1`, `kind: Keycloak`, `name: keycloak`; set `minReplicas`/`maxReplicas` and a `Resource` metric (e.g. cpu `Utilization` `averageUtilization: 80`).
- **Relevant guide:** rhbk-operator

### KB 7128352 — "dns_query can not be null or empty" when creating a temporary admin user
- **Applies to:** RHBK 26.x using bootstrap-admin (Infinispan Kubernetes stack)
- **Symptom:** `bootstrap-admin` fails with `ISPN000541` / `java.lang.IllegalArgumentException: dns_query can not be null or empty`.
- **Cause:** The `jgroups.dns.query` property (required by Infinispan's Kubernetes cache stack) is missing during the bootstrap-admin transient server start.
- **Fix:** Switch to the local cache stack for the bootstrap run: set `KC_CACHE=local` or pass `--cache=local` on `kc.sh bootstrap-admin`. Confirm `KC-SERVICES0077: Created temporary admin user with username admin1` in logs, then revert the local cache setting and start normally. (Note: local cache may also surface "Unable to start the management interface"/"Address already in use", but the user is created before the server start.)
- **Relevant guide:** server-configuration

### KB 7128299 — Intermittent loss of AD identity-provider link (account merge prompts)
- **Applies to:** RHBK 26.x with Active Directory identity provider / federated links
- **Symptom:** Users sporadically lose their IdP link to AD and are prompted to "merge accounts" on login.
- **Cause:** The IdP "Username Template Importer" mapper uses a mutable AD attribute (e.g. `${ATTRIBUTE.sAMAccountName}`, `${ATTRIBUTE.userPrincipalName}`, `${ATTRIBUTE.cn}`); when AD admins change it, the new identifier no longer matches the stored federated link.
- **Fix:** Reconfigure the Identity Provider mapper's Template to an immutable AD attribute — the standard is `objectGUID`. Note this causes a one-time merge/relink for all existing users (old links were keyed on the previous attribute); a per-user fix is clicking "Link" on the merge screen or an admin manually relinking.
- **Relevant guide:** server-administration

### KB 7126933 — Separate SSO and Admin Console hostnames without forced redirect
- **Applies to:** RHBK 26.x with distinct user (sso) and admin hostnames behind a reverse proxy
- **Symptom:** Defining both `hostname` and `hostname-admin` forces redirection to a single canonical hostname, breaking separate user/admin URLs.
- **Cause:** By design, strict hostname validation enforces one trusted hostname / canonical redirect in production.
- **Fix:** Set `hostname-strict=false`; comment out `#hostname=` and `#hostname-admin=` in `keycloak.conf`; let the external reverse proxy/LB handle URL rewriting and TLS termination for both hosts. Verify with `kc.sh show-config` that `hostname-strict=false` is applied; admin console then serves at `https://ssoadmin.example.internal/admin` and user endpoints at `https://sso.example.internal`.
- **Relevant guide:** server-configuration

### KB 7125609 — CSPRNG / SecureRandom source for RHBK on Windows
- **Applies to:** RHBK 26.x on Windows
- **Symptom:** Question of how RHBK performs cryptographically secure random number generation on Windows.
- **Cause:** RHBK ships no dedicated CSPRNG library; it relies on the JVM and host OS crypto APIs.
- **Fix:** No action needed — on Windows, Java `SecureRandom` uses the `Windows-PRNG` provider via `sun.security.mscapi`, delegating CSPRNG operations to the Microsoft CryptoAPI/native Windows cryptographic functions.
- **Relevant guide:** server-development

### KB 7078728 — Realm-specific CIBA authentication channel URI not supported
- **Applies to:** RHBK 24.x / RH-SSO 7.x, CIBA HTTP authentication channel
- **Symptom:** Cannot set different CIBA channel URIs per realm in one instance; setting the property twice only keeps one value.
- **Cause:** `spi-ciba-auth-channel-ciba-http-auth-channel-http-authentication-channel-uri` is a global system property (instance-wide), not realm-scoped.
- **Fix:** Only one CIBA channel URI per instance is supported. To use different URIs per realm (e.g. `https://ciba.aaa.example.internal` vs `https://ciba.bbb.example.internal`), run separate RHBK instances, each dedicated to a realm with its own CIBA channel URI.
- **Relevant guide:** securing-apps

### KB 7074235 — "frame-ancestors" missing from response header on static HTML
- **Applies to:** RHBK 22.x/24.x, RH-SSO 7.x
- **Symptom:** Response Content-Security-Policy on static pages (e.g. `/realms/master/protocol/openid-connect/3p-cookies/step1.html`) shows `frame-src 'self'; object-src 'none';` with `frame-ancestors 'self'` absent.
- **Cause:** For static HTML resources the `frame-ancestors` directive is always omitted from the header output — expected behavior.
- **Fix:** Expected behavior; as a workaround add the header configuration at the proxy/Undertow layer (for RH-SSO/Undertow) ahead of RHBK to inject the directive.
- **Relevant guide:** server-configuration

### KB 7073090 — RHBK Operator fails: "Proxy port is required!" with portless cluster-wide proxy
- **Applies to:** RHBK Operator on OpenShift with a cluster-wide `Proxy` (HTTP_PROXY/HTTPS_PROXY)
- **Symptom:** Operator pod fails to start: `java.lang.IllegalArgumentException: Failure in creating proxy URL. Proxy port is required!` from `HttpClientUtils.getProxyUri`.
- **Cause:** The cluster-wide proxy `httpProxy`/`httpsProxy` values have no port number; the fabric8 Kubernetes client requires an explicit proxy port (upstream issue keycloak/keycloak#30165).
- **Fix:** Add an explicit port to the cluster `Proxy` CR, e.g. `httpProxy: http://myproxy:port` and `httpsProxy: https://myproxy:port` (keep `noProxy` and `trustedCA` as configured), then reconcile the Operator.
- **Relevant guide:** rhbk-operator

KB 7129284 (inactivity-based deactivation: RFE not yet available — no shipping resolution), KB 6985816 (proactive-case process), KB 7098117 (no way to encrypt password pre-transmission beyond TLS — Q&A, no fix), KB 7095007 (Maven repo licensing), KB 3213211 (container image support policy), KB 2428751 (RH-SSO subscription requirements), and KB 1129963 (when Keycloak is supported) were skipped as non-technical or as RFE/no-resolution Q&A.

### Identity — LDAP/AD, auth/login/SSO, SPI, REST API

I've read all 18 KB bodies. Now I'll emit the markdown entries, skipping non-technical Q&A (KB 7116127 Insights/subscription-manager RFE, KB 7093256 unused table lifecycle, KB 7072329 RFE-only, KB 7061421 not-possible/licensing, KB 6981558 CVE-not-affected advisory).

### KB 7126964 — Client role checks bypassed after Kerberos authentication
- **Applies to:** RHBK (all versions), browser login flow with Kerberos authenticator
- **Symptom:** After successful Kerberos auth, the flow skips subflows/conditional executions (e.g. client role checks), whereas username/password login runs them.
- **Cause:** The Kerberos authenticator is a passive early authenticator; on success the user is immediately authenticated and the flow skips remaining executions — by design.
- **Fix:** Implement a custom Authenticator SPI that runs after Kerberos auth, validates the required client role for the user, and fails the flow if the role is absent. Custom SPI development is unsupported — engage Red Hat Consulting. To diagnose, enable Kerberos DEBUG logging on authentication events to trace the path per login scenario.
- **Relevant guide:** server-development

### KB 7125052 — Unauthorized realms visible in RHBK 26 admin console dropdown
- **Applies to:** RHBK 26.0.9, admin console realm selector
- **Symptom:** A user scoped to one realm (e.g. ehrss_admin/test_admin) sees unauthorized realms (e.g. "master") in the dropdown; switching to one yields an error page. Earlier behavior hid unauthorized realms.
- **Cause:** Defect in this RHBK 26 version (SSOSUP raised to investigate).
- **Fix:** No fix in the article; workaround is to switch back to the authorized realm and click "Press here to refresh and continue". Track the support case for a corrected build.
- **Relevant guide:** server-administration

### KB 7115290 — "Cannot parse the JSON" when searching users with spaces in Admin console
- **Applies to:** RHBK 26.0.x, Admin console user search over LDAP federation (with pagination)
- **Symptom:** "Cannot parse the JSON" / "error unknown" when searching for certain users (e.g. firstName "abc") during LDAP sync.
- **Cause:** LDAP query failed with a class-cast exception from a mismatch between expected and actual data types.
- **Fix:** When the search value contains spaces, wrap it in double quotes, e.g. `https://host/auth/admin/realms/customrealm/users?firstName="XYZ jose"`; for an exact match add `&exact=true`, e.g. `.../users?firstName="XYZ jose"&exact=true`.
- **Relevant guide:** server-administration

### KB 7086086 — Group deletion in RHBK not propagated to LDAP
- **Applies to:** RHBK 24.x/22.x, RH-SSO 7.x; group-ldap-mapper user federation
- **Symptom:** Deleting or moving groups in Keycloak is not reflected in LDAP, even after manually triggering a sync.
- **Cause:** The group-ldap-mapper "Sync" button only performs group IMPORT (LDAP→Keycloak); deletion is not propagated Keycloak→LDAP. An RFE was filed for future releases.
- **Fix:** Remove the group from both Keycloak and LDAP manually. Air-gap note: plan an on-prem reconciliation procedure since no automatic two-way delete sync exists.
- **Relevant guide:** server-administration

### KB 7086512 — Generic message for LDAP "Could not modify attribute for DN" on password reset
- **Applies to:** RHBK 24.x/22.x, LDAP-backed users with password policy
- **Symptom:** Resetting a password that violates the policy shows `'Could not modify attribute for DN'`; admins want a friendlier message.
- **Cause:** The LDAP/directory rejects the password update; events log `error=password_rejected, type=UPDATE_PASSWORD_ERROR` with reason "Could not modify attribute for DN [...]".
- **Fix:** Customize the user-facing text via a custom theme (RHBK theme support covers web pages/emails). Diagnose by enabling `trace` logging on `org.keycloak` and reviewing the server.log continuation message.
- **Relevant guide:** server-development

### KB 7078462 — Create resource-based permissions and aggregate policies via REST API
- **Applies to:** RHBK 24.x/22.x, RH-SSO 7.x; fine-grained authorization (resource server)
- **Symptom:** Need to create resources, resource-based permissions, and aggregate policies via the Admin REST API/kcadm rather than the console.
- **Cause:** API not fully documented; tip: use browser dev tools while doing the operation in the console to capture the exact endpoint and payload, then replay it.
- **Fix:** POST to `/admin/realms/{realm}/clients/{clientUUID}/authz/resource-server/resource` (body `{"name":...,"uris":[...],...}`); resource permission to `.../authz/resource-server/permission/resource` (body `{"resources":[id],"policies":[id],"name":...,"decisionStrategy":"UNANIMOUS"}`); aggregate policy to `.../authz/resource-server/policy/aggregate` (body `{"policies":[id],"name":...,"decisionStrategy":"UNANIMOUS","logic":"POSITIVE"}`).
- **Relevant guide:** authorization

### KB 7072930 — List policies and resource-based permissions via Admin REST API
- **Applies to:** RHBK 22.0.10; authorization (resource server)
- **Symptom:** No obvious API to list JS/group/time/aggregate policies or resource-based permissions as a list.
- **Cause:** N/A (API usage).
- **Fix:** Get a token (`curl -d "client_id=admin-cli" -d username=*** -d password=*** -d grant_type=password .../realms/master/protocol/openid-connect/token`). List all policy types: `curl -H "Authorization: bearer $TKN" .../admin/realms/master/clients/{clientUUID}/authz/resource-server/policy | jq`. List resources/permissions: `.../authz/resource-server/resource/ | jq`.
- **Relevant guide:** authorization

### KB 7071708 — Account console fails to initialize with HTTP 403
- **Applies to:** RHBK 22.0.10, built-in account-console client
- **Symptom:** Account management page "Failed to initialize" with a 403 error in the browser.
- **Cause:** Redirect/Web Origins fall back to the default URI address.
- **Fix:** In the realm (e.g. Demo) edit the `account-console` client and add `+` to Web Origins (inherit allowed origins from Valid Redirect URIs).
- **Relevant guide:** securing-apps

### KB 7070447 — Add vs. replace user attributes via Admin REST API
- **Applies to:** RHBK 22.0.10, Admin REST API user attributes
- **Symptom:** Need to add user attributes (and bulk-register several) without replacing existing ones via API.
- **Cause:** A PUT to the user replaces the `attributes` map — attributes omitted from the body are dropped.
- **Fix:** GET the user (`/admin/realms/master/users/{userId}`), then `PUT` with `-d '{"attributes":{"phone":["..."],"age":["..."],...}}'`. To add to existing attributes, merge old+new and PUT the combined set; PUT with only the desired attributes to replace. Verify with a follow-up GET.
- **Relevant guide:** server-administration

### KB 7064052 — "Users in Role" tab not honoring read-only in RH-SSO 7.6
- **Applies to:** RH-SSO 7.6 (fixed in RHBK 22), admin console "Users in Role" tab
- **Symptom:** The "Users in Role" tab cannot be configured as read-only.
- **Cause:** Bug in RH-SSO 7.6; works as expected in RHBK 22.
- **Fix:** Upgrade to RHBK 22, where the behavior is corrected.
- **Relevant guide:** migration-upgrading

### KB 7053211 — Resource name vs. UID in the permission parameter when obtaining an RPT
- **Applies to:** RHBK 22.x, RH-SSO 7.x; UMA/RPT token endpoint
- **Symptom:** Unclear whether `RESOURCE_ID#SCOPE_ID` in the `permission` parameter uses the resource UUID or the resource name.
- **Cause:** `RESOURCE_ID#SCOPE_ID` combines an actual resource and scope; uniqueness and indexes exist for both name and UID, so either works.
- **Fix:** Use either form, e.g. `--data "permission=example_resource#Scope A"` or `--data "permission=569f67de-36e6-ac54-e52085109818#Scope A"` against `/realms/{realm}/protocol/openid-connect/token`. The optional `permission_resource_format` parameter (RHBK 22.x) accepts `id` (default, RESOURCE_ID) or `uri`.
- **Relevant guide:** authorization

### KB 3419601 — Tune JVM heap (Xmx/Xms) to avoid OutOfMemory in RH-SSO
- **Applies to:** RH-SSO 7.2 (JBoss EAP-based), standalone/domain
- **Symptom:** Default Xmx/Xms cause OutOfMemory exceptions.
- **Cause:** RH-SSO runs on JBoss EAP, so heap is set via JBoss EAP memory parameters.
- **Fix:** Append to `standalone.conf` or `domain.conf` (under `/opt/rh/rh-sso7/root/usr/share/keycloak/bin/`): `JAVA_OPTS="$JAVA_OPTS -Xms10g -Xmx10g"` (last value wins if duplicated). For RPM installs the startup config file takes precedence over service env vars; OpenShift uses a different documented process.
- **Relevant guide:** server-configuration

### KB 3010401 — Federate FreeIPA users into Keycloak via LDAP for OpenStack SAML SSO
- **Applies to:** Keycloak 2.4 (community, used with RH-SSO patterns), LDAP User Federation + SAML2 WebSSO to OpenStack Keystone/Horizon
- **Symptom:** Need FreeIPA users to log in to OpenStack Dashboard without exposing credentials to OpenStack; Keycloak acts as IdP (note: this guide is unsupported/untested by Red Hat).
- **Cause:** Keystone (SP) trusts Keycloak (IdP) via exchanged SAML metadata; Keycloak fronts FreeIPA over LDAP.
- **Fix:** Add Keycloak LDAP User Federation with Vendor `Red Hat Directory Server`, Edit Mode `READ_ONLY`, UUID attribute `ipaUniqueID`, `Connection URL ldaps://freeipa.example.internal:636`, Users DN `cn=users,cn=accounts,dc=...`, then Test connection and Synchronize all users. Add a SAML "Group list" protocol mapper (attribute name `groups`, NameFormat Basic, Single Group Attribute On); set mellon `MellonMergeEnvVars On ";"`; map groups in Keystone `mapping_rules.json`. Use FreeIPA-issued certs (passwords masked as ***).
- **Relevant guide:** securing-apps

## All KB Solutions by area (1,030)

Counts across the full harvested set (public body = resolution bundled locally; gated = subscriber login needed).

| Area | Total | Public body | Gated |
|---|--:|--:|--:|
| Operator & OpenShift deployment | 218 | 4 | 214 |
| Authentication, login & SSO | 259 | 9 | 250 |
| Database & JDBC | 79 | 3 | 76 |
| TLS, certificates & truststore | 78 | 3 | 75 |
| LDAP / AD / federation | 74 | 6 | 68 |
| Image, build & disconnected | 66 | 3 | 63 |
| Hostname, proxy & networking | 68 | 3 | 65 |
| Tokens & sessions | 41 | 0 | 41 |
| Admin console, realm & users | 34 | 3 | 31 |
| Custom providers / SPI / themes | 32 | 1 | 31 |
| Infinispan, caching & HA | 24 | 0 | 24 |
| Upgrade & RH-SSO→RHBK migration | 20 | 1 | 19 |
| FIPS & cryptography | 4 | 1 | 3 |
| Performance & sizing | 1 | 0 | 1 |
| Other / uncategorized | 32 | 3 | 29 |
| **All** | **1030** | **40** | **990** |

> Operator/OpenShift (218) and Authentication/SSO (259) dominate the gated set — for those, search the bundled docs
> first (`rhbk_kb.py search ... --kind doc`), then fall back to the gated KB pointer + a Red Hat login.

_Source: Red Hat Customer Portal KB Solutions (access.redhat.com) for RHBK/RH-SSO, distilled offline. Resolution
bodies for the 990 gated solutions are subscriber-only and intentionally not reproduced._
