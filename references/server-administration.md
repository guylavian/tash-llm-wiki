# RHBK 26.6 — Server Administration

Internal runbook for administering realms in Red Hat build of Keycloak (RHBK) 26.6. Content is shared with upstream Keycloak 26 except where marked **RHBK**. Air-gap notes use `example.internal` / `***` for secrets. Grounded in the RHBK Server Administration Guide chapter bodies; details not present there are omitted.

---

## 1. Core concepts

| Term | Meaning |
|---|---|
| realm | Isolated space managing a set of users, credentials, roles, groups. A user belongs to and logs into one realm. Realms are isolated from one another. |
| client | Entity that requests RHBK to authenticate a user (apps/services). Each client has a built-in service account. |
| role | Type/category of user. Realm-level (global namespace) or client-level (per-client namespace). |
| composite role | Role associated with other roles; users mapped to it inherit the associated roles (recursive). |
| group | Collection of users; carries attributes + role mappings that members inherit. Hierarchical (one parent, many subgroups). |
| user federation provider | External user store (LDAP/AD, custom via User Storage SPI). |
| identity provider (IdP) | External service that authenticates a user (OIDC/SAML/social). RHBK as broker delegates auth to it. |
| required actions | Actions a user must complete during authentication before login finishes. |
| authentication flow | Container of authentications/screens/actions for login, registration, reset, etc. |
| client scope | Shared protocol-mapper + role-scope-mapping config; `default` (always) or `optional` (requested via `scope` param). |

**Air-gap:** RHBK is a server on your network. Apps redirect the browser to RHBK; users never expose credentials to apps. Use OIDC or SAML.

---

## 2. First administrator

- **Localhost:** browse `http://localhost:8080`, set username/password on the Welcome page.
- **Remote / CLI bootstrap:** set env vars then start:

```bash
export KC_BOOTSTRAP_ADMIN_USERNAME=<username>
export KC_BOOTSTRAP_ADMIN_PASSWORD=<password>
bin/kc.[sh|bat] start
```

Admin Console: `http://localhost:8080/admin/`.

---

## 3. Realms & realm settings

Create: Admin Console → **Create Realm** → name → **Create**. Realms disabled by default when created via API/CLI; enable to use.

- **master realm** — created at first start; holds the super-admin account. Use it only to create/manage other realms.
- **Other realms** — created by master-realm admins; isolated.

> Admin-Console export files are **not** suitable for backups or server-to-server transfer — only boot-time exports are.

### SSL mode (General tab → Require SSL)
| Mode | Behavior |
|---|---|
| External requests | No SSL allowed only for private IPv4 (`localhost`, `127.0.0.1`, `10.x`, `192.168.x`, `172.16.x`) + IPv6 link-/unique-local; error otherwise. |
| None | No SSL required (development only). |
| All requests | SSL required for all IP addresses. |

### Email (Email tab)
Template: `From`, `From display name`, `Reply to`, `Reply to display name`, `Envelope from`. Connection & Auth: `Host`, `Port` (465 for SSL/TLS), `Encryption`, `Authentication` (ON if SMTP needs auth), `Username`, `Authentication Type` (`password` or `token`). For `password`: `Password` (can reference an external vault). For `token`: `Auth Token URL`, `Auth Token Scope`, `Auth Token ClientId`, `Auth Token Client Secret` (vault-capable). `Allow UTF-8` enable only if the mail server supports SMTPUTF8.

**Air-gap:** point Host to an internal relay, e.g. `smtp.example.internal`, password `***` via vault.

### Themes (Themes tab)
Pick per category: **Login**, **Account**, **Admin console**, **Email**.

### Internationalization (Localization tab)
Enable Internationalization, select supported languages + default. Locale selection order: User selected → User profile → Client (`ui_locales`) → Cookie → Accept-Language → Realm default → English.

### Login options (Login tab)
- **Forgot password** ON → "Forgot Password?" link (needs Email `Host`+`From`).
- **Remember Me** ON → persistent login cookie. Disabling invalidates all "Remember me" sessions (lazily, when their cookie/token is next used).
- **User Registration** ON → "Register" link.
- ACR→LoA Mapping (General settings): map ACR string → numeric LoA used in flow conditions; requestable via `claims`/`acr_values`.

### Update Email workflow (RHBK / Keycloak 26)
Enable `UPDATE_EMAIL` required action (Authentication → Required actions). Forces re-auth if last auth older than **Maximum Age of Authentication** (default 300 s / 5 min; `0` = always). `Force Email Verification` setting forces verification even when realm email verification is off. Pending verifications manageable from user details (admin can cancel).

---

## 4. Realm keys & rotation

RHBK uses asymmetric key pairs (private/public). One **active** key pair signs new tokens; **passive** keys verify old signatures. A realm gets a key pair + self-signed cert at creation.

Realm settings → **Keys**: filter Active/Passive/Disabled. Active selected = first key provider by priority that can provide an active pair.

**Rotation:** add new keys with higher priority (or same priority + make old ones passive). New tokens/cookies use new keys; SSO cookies & refreshed tokens migrate. Recommended: new keys every 3–6 months, delete old keys 1–2 months later. Applies to offline tokens too (refresh before old keys removed).

### Key provider procedures (Keys → Providers → Add provider)
| Provider | Notes |
|---|---|
| `rsa-generated` | Generated key pair + self-signed cert. Set **Priority** (highest = active), **AES Key size**. Changing keysize regenerates keys. |
| `rsa` | Existing key pair: upload PEM **Private RSA Key** + optional **X509 Certificate** (self-signed generated if omitted). |
| `java-keystore` | Load from JKS on host. Set Algorithm (e.g. `RS256`→RSA, `ES256`→EC, `AES`→AES), `Keystore` path, `Keystore Password` (vault-capable), Keystore Type (`JKS`/`PKCS12`/`BCFKS`), `Key Alias`, `Key Password` (vault), Key Use (`sig`/`enc`). Cert chain must be imported under the same alias. JKS (all modes) and PKCS12 in FIPS (`BCFIPS`) cannot store secret keys. |

Make passive: provider → Active Off. Disable: Enabled Off. **Compromised key:** generate new pair, remove the compromised provider, then push not-before policy (Clients → `security-admin-console` → set Admin URL → Advanced → Revocation → Set to now → Push). REST/confidential clients must set Admin URL to receive pushed not-before.

**Air-gap:** keystores live on the host filesystem; no external KMS calls required.

---

## 5. Users, attributes, credentials, required actions

Create: Users → Add User (only **Username** required). Avoid creating users in master realm.

### User profile (Realm Settings → User Profile)
Per-realm JSON schema for attributes. Default managed attributes: `username`, `email`, `firstName`, `lastName` (`username`/`email` cannot be removed and follow Login settings).

**Unmanaged Attributes policy** (General tab): `Disabled` (default), `Enabled`, `Admin can view` (read-only), `Admin can edit`. JSON `unmanagedAttributePolicy`: `DISABLED` / `ENABLED` / `ADMIN_VIEW` / `ADMIN_EDIT`. Unmanaged attribute max length = 2048 chars.

Per-attribute settings: Name, Display name, Multivalued, Default Value, Attribute Group, **Enabled when** (`Always` / `Scopes are requested`), **Required** (`Required for` user/admin; `Required when` scopes), **Permission** (`Who can edit`/`Who can view` = User/Admin), Validation, Annotation. New attributes are admin-only until permissions changed.

JSON schema example:
```json
{
  "unmanagedAttributePolicy": "DISABLED",
  "attributes": [
    {
      "name": "myattribute",
      "required": { "roles": ["user","admin"], "scopes": ["foo","bar"] },
      "permissions": { "view": ["admin","user"], "edit": ["admin","user"] },
      "validations": { "email": {"max-local-length":64}, "length": {"max":255} }
    }
  ],
  "groups": [ { "name": "personalInfo", "displayHeader": "Personal Information" } ]
}
```

### Built-in validators
`length` (min/max/trim-disabled), `integer` (min/max), `double` (min/max), `uri`, `pattern` (pattern/error-message), `email` (max-local-length, default 64), `local-date`, `iso-date`, `person-name-prohibited-characters`, `username-prohibited-characters`, `options`, `up-username-not-idn-homograph`, `multivalued` (min/max). Without a `length` validator, editable attributes default to max 2048 chars.

`VerifyProfile` required action (enabled by default) forces profile compliance at login. Searches in Users encompass DB + federated backends (LDAP users get imported).

### Credentials (Credentials tab)
Columns: Type, User Label, Data (Show data…), Actions (Reset password / Delete). Drag rows to set priority. **Set/Reset Password**: `Temporary` ON ⇒ user must change at next login. **Credential Reset** → email link (`Update Password`, `Configure OTP`); validity defaults to Tokens-tab presets. Admin cannot configure arbitrary credential types for a user.

### Required actions
Examples: Update Password, Configure OTP, Verify Email, Update Profile. Set per-user (Users → Required User Actions) or default for all (Authentication → Required Actions → "Set as default action"). Enable Terms and Conditions / Delete Account from Required Actions tab. `Delete Credential` is a parameterized AIA only.

### Application Initiated Actions (AIA) — OIDC clients only (RHBK proprietary)
Add `kc_action=<ACTION>` to the OIDC login URL (e.g. `kc_action=UPDATE_PASSWORD`, `kc_action=CONFIGURE_TOTP`). Cancel → redirect with `kc_action_status=cancelled` + `kc_action`. Parameterized: `kc_action=delete_credential:<credential-id>`. Re-auth: default max age 5 min (configurable per required action); `delete_account` always re-auths; `UPDATE_PASSWORD` honors Maximum Authentication Age password policy. `max_age` may only shorten (not lengthen) re-auth window; `prompt=login` always re-auths.

### Other user operations
- **Self-registration**: Login tab → User Registration ON; can require Terms & Conditions (Authentication → Flows → registration).
- **Delete account by user**: enable Delete Account required action + grant `account` client role `delete-account`; user deletes via Account Console.
- **Impersonation**: Users → Actions → Impersonate (needs `impersonation` role). Same realm = admin logged out + in as user; cross-realm = admin stays logged in too.
- **reCAPTCHA** (anti-bot registration): Authentication → Flows → Registration → set reCAPTCHA Required, configure Site Key/Secret, toggle reCAPTCHA v3. Must whitelist `https://www.google.com` (or `https://www.recaptcha.net`) in X-Frame-Options + Content-Security-Policy (Security Defenses). reCAPTCHA Enterprise variant uses Project ID / Site Key / API Key / Min. Score Threshold.

**Air-gap:** reCAPTCHA and social providers require outbound internet to Google/Meta etc.; not usable in a disconnected enclave — prefer LDAP/X.509/Kerberos auth instead.

---

## 6. Roles, groups, default roles

- **Realm role**: Realm Roles → Create Role (Name, Description — localizable via `${var-name}`).
- **Client role**: per-client Roles tab.
- **Composite role**: role → Action → Add associated roles (realm + client roles). Inheritance is recursive; composites add their roles to token claims/SAML assertions.
- **Role mapping**: Users → user → Role mappings → Assign role. Inherited roles show Inherited "True".
- **Default roles**: Realm settings → User registration tab → auto-assigned on user creation or IdP import.
- **Default groups**: Realm settings → User registration → Default Groups tab.

### Role scope mappings
By default each client gets **all** user role mappings (Full Scope Allowed). To restrict: Clients → client → Client scopes → "Dedicated scope and mappers" → Scope tab → Full Scope Allowed OFF → declare specific roles. Limits token contents.

### Groups
Hierarchical (path `/top/level1/level2`, separated by `/`). Slashes in names are not escaped by default; start with `--spi-group--jpa--escape-slashes-in-group-path=true` to escape with `~`:
```bash
bin/kc.[sh|bat] start --spi-group--jpa--escape-slashes-in-group-path=true
```
Add: Groups → Create group. Add user: Users → user → Groups → Join Group. Subgroups inherit parent attributes + role mappings. Use **composite roles** to manage applications/services; use **groups** to manage collections of users.

---

## 7. Authentication

### Password policies (Authentication → Policies)
| Policy | Notes |
|---|---|
| HashAlgorithm | `argon2` (default non-FIPS), `pbkdf2-sha512` (default FIPS), `pbkdf2-sha256`, `pbkdf2-sha1` (deprecated). Set default via `--spi-password-hashing--provider-default=<algorithm>`. |
| Hashing iterations | Default `-1` = algorithm default: argon2 `5`, pbkdf2-sha512 `210000`, pbkdf2-sha256 `600000`, pbkdf2-sha1 `1300000`. |
| Digits / Lowercase / Uppercase / Special characters | Required counts. |
| Not username / Not email | Password ≠ username/email. |
| Regular expression | Java regex match. |
| Expire password | Valid N days. |
| Not recently used | Cannot reuse from stored history (count configurable). |
| Not recently used (In Days) | Cannot reuse within N days. |
| Password blacklist | UTF-8 file in `${kc.home.dir}/data/password-blacklists/`; case-insensitive; BloomFilter (default FP prob 0.01%). Configure path via `keycloak.password.blacklists.path` or `--spi-password-policy--password-blacklist--blacklists-path=`. |
| Maximum Authentication Age | Max age (s) to update password without re-auth; `0` = always. Prefer the Update Password required action config. |

New policies apply to new passwords only; existing users unaffected until they change/expire passwords.

### OTP (Authentication → Policy → OTP Policy)
TOTP (time + secret, short window) vs HOTP (shared counter, increments on success, DB write each time). Options: **OTP hash algorithm** (SHA1 default; SHA256/SHA512), Number of digits, Look around window (default 1), OTP token period (TOTP), Initial counter (HOTP), **Reusable code** (default: not reusable).

### Authentication flows (Authentication → Flows)
Built-in flows are immutable but requirements are adjustable. Auth types include Cookie, Kerberos (disabled by default), Identity Provider Redirector, Forms (Username Password Form, Browser - Conditional 2FA, Condition - User Configured, Condition - credential, OTP Form, WebAuthn Authenticator, Recovery Authentication Code Form).

**Requirements:** Required, Alternative, Disabled, Conditional (sub-flows only; true→acts Required, any false→Disabled). Create: Create flow (Top-Level Flow Type `basic` or `client`); add executions (Add step) / sub-flows (Add sub-flow, type `basic` or `form`). Executions may have a **reference value** consumed by the AMR protocol mapper → `amr` claim (RFC-8176). Drag to reorder.

**Step-up authentication:** wrap authenticators in Conditional sub-flows each with **Conditional - Level Of Authentication** (alias, LoA number, **Max Age** in seconds — `0` = valid this auth only; e.g. `36000` ≈ default SSO Session Max). Request via OIDC `claims` (essential `acr`) or `acr_values`. `acr` claim added by `acr loa level` mapper in the default `acr` client scope. Order subflows lowest LoA first.

Direct registration/reset redirects: `prompt=create` → registration (or deprecated `/registrations`); `/forgot-credentials` → reset. Bypassing OIDC/SAML to other endpoints is unsupported.

**User session limits** (User session count limiter authenticator, REQUIRED): max sessions per realm + per client; behavior `Deny new session` or `Terminate oldest session`. Add to Browser (in a separate ALTERNATIVE subflow, not top-level), Direct grant, Reset credentials, and Post broker login flows. Not available for CIBA.

### MFA / credential types
- **OTP** — see above (FreeOTP / Google Authenticator).
- **WebAuthn / Passkeys** — RHBK = Relying Party. Enable `Webauthn Register` required action; add WebAuthn Authenticator (Alternative/Required) in Browser - Conditional 2FA. **WebAuthn Policy** (Authentication → Policy → WebAuthn Policy): Relying Party Entity Name (default `keycloak`), Signature Algorithms (default ES256+RS256), Relying Party ID, Attestation Conveyance Preference, Authenticator Attachment, Require Discoverable Credential, User Verification Requirement, Timeout (default 0), Avoid Same Authenticator Registration, Acceptable AAGUIDs. **Passwordless/Loginless** uses a separate **WebAuthn Passwordless Policy** + `Webauthn Register Passwordless` action + WebAuthn Passwordless Authenticator. Enable **Passkeys** via the *Enable Passkeys* switch in WebAuthn Passwordless Policy (Conditional UI autofill `autocomplete="username webauthn"` + Modal UI "Sign in with Passkey"). AIA: `kc_action=webauthn-register`, `kc_action=webauthn-register-passwordless` (supports `:skip_if_exists`). User ID handle max 64 bytes — use short IDs for federated users.
- **X.509 client certificate** — needs mutual TLS. Add X509/Validate Username Form (browser, Alternative) or X509/Validate Username (direct grant). Identity sources: SubjectDN regex, email, SAN (RFC822Name / UPN otherName), Common Name, IssuerDN regex, Serial Number, Serial+IssuerDN, SHA-256 thumbprint, Full certificate (PEM, LDAP-only — RHBK cannot store full certs in DB). Validations: CRL / CRL Distribution Point, OCSP (+ Fail-Open, Responder URI), KeyUsage, ExtendedKeyUsage, Certificate Policy (mode All/one). Options: Canonical DN, hex serial, User Mapping Method, Bypass identity confirmation, **Revalidate client certificate** (app-level chain check behind non-validating proxy). Web container/reverse proxy must validate PKIX path.
- **Kerberos / SPNEGO** — enable Kerberos in browser flow (Alternative/Required). Add HTTP service principal `HTTP/www.mydomain.org@REALM`, export keytab; configure `/etc/krb5.conf` `domain_realm`. Use LDAP provider with **Allow Kerberos authentication** ON, or the standalone Kerberos User Storage provider. Supports credential delegation (gss delegation credential mapper), cross-realm trust (`krbtgt/B@A`, attribute `KERBEROS_PRINCIPAL`, `Kerberos principal attribute` e.g. `userPrincipalName`). Negotiate may fall back to NTLM (unsupported — user cancels dialog).
- **Recovery Codes** — 12 sequential one-time passwords. Enable `Recovery Authentication Codes` required action; add Recovery Authentication Code Form (Alternative) in Browser - Conditional 2FA. Warning Threshold config.

### Conditions in conditional flows
Condition - User Role (`appname.approle`), Condition - User Configured, Condition - User Attribute (name/value, Include group attributes, Negate), Condition - sub-flow executed (executed/not-executed), Condition - client scope (Negate), Condition - credential (Credentials list, Included), Condition - Level Of Authentication. Explicit: **Allow Access** (always succeeds), **Deny Access** (alias + error message, supports localization property e.g. `access-denied`).

---

## 8. Identity brokering (IdP integration)

Identity Providers menu. Common config:

| Option | Notes |
|---|---|
| Alias | Unique ID; used to build redirect URIs. |
| Enabled / Hide on Login Page / Account Linking Only | Account Linking Only = links accounts but cannot log in. |
| Store Tokens / Stored Tokens Readable | Store IdP tokens; grant `broker` role `read-token` to read. |
| Trust Email | Skip email verification for users from this IdP. |
| GUI Order / Show in Account console | Login-page ordering / account console visibility. |
| Verify essential claim / Essential claim / Essential claim value | Require JWT claim (value supports regex). |
| First Login Flow / Post Login Flow | First broker login flow / post-IdP-login flow. |
| Sync Mode | legacy / import (no update) / force (update each login). |
| Case-sensitive username | Keep original IdP username casing. |

**Default IdP redirect:** Browser flow → Identity Provider Redirector ⚙️ → set Default Identity Provider. Processes `kc_idp_hint` query param (`kc_idp_hint=facebook`; empty value disables redirect).

### OIDC v1.0 IdP (key config)
Authorization URL, Token URL, Logout URL, Backchannel Logout, User Info URL, Client Authentication, Client ID, Client Secret (vault), Client Assertion Signature Algorithm/Audience, Issuer, Default Scopes (default `openid`), Prompt, Accepts `prompt=none` forward, Requires short state parameter, Validate Signatures, Use JWKS URL, JWKS URL, Validating Public Key / Key Id, Forwarded query parameters, Supports/Allows client assertions. Import from `<root>/realms/{realm}/.well-known/openid-configuration`.

### OAuth v2 IdP
Authorization/Token/User Info URL, Client Auth/ID/Secret, Client Assertion settings, Default Scopes, Prompt. Access tokens treated as opaque → user profile fetched from User Info URL (bearer). Claim mappings: ID Claim, Username Claim, Email Claim, Name Claim, Given/Family name Claim.

### SAML v2.0 IdP (key config)
Service Provider Entity ID, Identity Provider Entity ID, Single Sign-On Service URL, Artifact service URL, Single Logout Service URL, Backchannel Logout, NameID Policy Format, Principal Type/Attribute, Allow create, HTTP-POST/ARTIFACT Binding Response, HTTP-POST Binding for AuthnRequest, Want AuthnRequests/Assertions Signed/Encrypted, Signature/Encryption Algorithm, SAML Signature Key Name, Force Authentication, Validate Signature, Metadata descriptor URL + Use metadata descriptor URL, Validating X509 Certificates, Sign SP Metadata, Pass subject (`login_hint`→Subject), Attribute Consuming Service Index/Name. Requested AuthnContext: Comparison, ClassRefs, DeclRefs. SP descriptor: `http[s]://{host}/realms/{realm}/broker/{alias}/endpoint/descriptor`. Import from `<root>/realms/{realm}/protocol/saml/descriptor`.

**SPIFFE IdP** — Technology Preview, disabled by default (`--features=preview` or `--features=spiffe`). Config: Alias, SPIFFE Trust Domain (`spiffe://my-trust-domain`), SPIFFE Bundle Endpoint.

### Mappers, first-login, tokens
Mappers tab → Add mapper; Sync Mode Override: legacy / import / force / inherit. JSON claims support dot/bracket paths (`contact.address[0].country`). Debug with logger `org.keycloak.social.user_profile_dump`.

**First Broker Login** default authenticators: Review Profile (Update Profile On First Login: on/missing/off), Create User If Unique → else Handle Existing Account subflow, Confirm Link Existing Account, Verify Existing Account By Email (ALTERNATIVE, needs SMTP), Verify Existing Account By Re-authentication. Variants: Automatically Set Existing User (auto-link, dangerous in open registration), Detect Existing Broker User (only pre-registered users), Confirm Override Existing Link. Disable auto-creation (read-only LDAP): set Create User If Unique + Confirm Link Existing Account to DISABLED.

Retrieve external IdP token: `GET /realms/{realm}/broker/{provider_alias}/token` with bearer (needs `broker` role `read-token`). Logout sends logout to the original external IdP.

**Air-gap:** social providers (Google, Facebook, GitHub, etc.) need outbound internet. For disconnected enclaves use an internal OIDC/SAML IdP (`https://idp.example.internal/...`), import metadata from the internal well-known/descriptor URL, secrets `***` via vault. OpenShift v4 IdP: store the cluster cert in the RHBK truststore, Base URL = `https://api.<openshift-domain>:6443`.

---

## 9. LDAP / Active Directory federation

User Federation → Add LDAP providers.

### Storage mode
**Import Users** ON → users copied to RHBK DB, synced on-demand/periodically (passwords never imported — validated on LDAP). OFF → LDAP backs the user model directly (no local profile attributes/metadata saved unless mapped). RHBK checks local DB first, then iterates providers by priority; lookups do not fail over (duplicate usernames/emails risk). Keep a local-DB admin account in case LDAP is unreachable.

### Edit Mode
| Mode | Behavior |
|---|---|
| READONLY | Cannot change username/email/name/mapped attrs; no password updates. |
| WRITABLE | Changes (incl. password) sync to LDAP automatically. |
| UNSYNCED | Changes stored locally only; admin must sync to LDAP. Allows updates on read-only LDAP. |

Edit Mode + Import Users must be decided at creation (mapper config won't change later for UNSYNCED).

### Connection / other options
Console Display Name, Priority, Sync Registrations (push new RHBK users to LDAP), Allow Kerberos authentication, Remove invalid users during searches, Relative User Creation DN, LDAPv3 Password Modify Extended Operation (OpenLDAP plaintext fix). SSL: use `ldaps://host:636` + configure a truststore (Use Truststore SPI deprecated, leave `Always`). Connection pooling enabled by default for `plain`+`ssl`; tune via `JAVA_OPTS_APPEND` (`com.sun.jndi.ldap.connect.pool.*`).

```bash
export JAVA_OPTS_APPEND="-Dcom.sun.jndi.ldap.connect.pool.initsize=10 -Dcom.sun.jndi.ldap.connect.pool.maxsize=50"
```

### Sync (Sync Settings)
Periodic Full sync (all users) / Periodic Changed users sync (since last sync). Best practice: "Synchronize all users" once at creation, then periodic changed-user sync.

### LDAP mappers (auto-created on provider creation)
User Attribute, FullName (`cn`→first/last), Hardcoded Attribute (can force `enabled`/`emailVerified`), Role, Hardcoded Role, Group, MSAD User Account (`userAccountControl`, `pwdLastSet`; `514`=disabled, `pwdLastSet=0`→UPDATE_PASSWORD), Certificate (X.509, enable `Always Read Value From LDAP`).

Troubleshooting: set TRACE on `org.keycloak.storage.ldap`; pool debug `com.sun.jndi.ldap.connect.pool.debug=all`.

### SSSD / FreeIPA
SSSD plugin (RHEL/Fedora) via read-only D-Bus + PAM. Requires **JDK 21**. Run `bin/federation-sssd-setup.sh`; add `ipaapi` user; PAM service `/etc/pam.d/keycloak`. User Federation → Add Sssd providers. Groups imported once, then managed in RHBK only.

**Air-gap:** point connection URL to an internal directory (`ldaps://ldap.example.internal:636`), bind DN credential `***`, import the LDAP server cert into the RHBK truststore.

---

## 10. User sessions, timeouts, offline access

Sessions menu: view active clients/sessions; **Sign out all active sessions** (invalidates SSO cookies; does not revoke outstanding access tokens — they expire naturally; SAML gets no back-channel logout). **Revocation** (Actions → Revocation → Set to now → Push) invalidates sessions/tokens issued before a time; Push reaches OIDC clients using the RHBK adapter.

### Sessions tab (Realm Settings)
SSO Session Idle, SSO Session Max, SSO Session Idle/Max Remember Me, Client Session Idle, Client Session Max, Offline Session Idle, Offline Session Max Limited, Offline Session Max, Client Offline Session Max, Login timeout, Login action timeout. (Idle timeout adds a ~2-minute window before expiry when persistent user sessions are inactive.)

### Tokens tab
Default Signature Algorithm, Revoke Refresh Token, Access Token Lifespan (+ Implicit Flow), Client login timeout, User-Initiated/Default Admin-Initiated Action Lifespan, Email Verification, IdP account email verification, Forgot password, Execute actions.

### Offline access
Client requests `scope=offline_access`. Offline token never expires and is not subject to SSO Session Idle/Max; survives logout. Must be used for refresh ≥ once per Offline Session Idle (default ~30 days). If **Offline Session Max Limited** enabled → expires after Offline Session Max (≈60 days default). Requires realm role `offline_access` mapped to user + in client scope (`offline_access` optional client scope added by default). Revoke Refresh Token ⇒ each offline token usable once. Internal cache for offline sessions defaults to 10000 entries (rest loaded from DB on demand).

**Transient sessions** — no persisted user session; used automatically during service-account auth with token refresh disabled. `sid`/`session_state` empty.

---

## 11. Admin & Account consoles, access control

### Master realm access control
Global roles: **admin** (superuser, all realms), **create-realm** (create + full access to new realms; also needs `query-realms` to list). Each realm = a client `<realm>-realm` in master with client roles. **Dedicated realm Admin Console**: `/admin/{realm-name}/console`; built-in client `realm-management` with roles:

`create-client`, `impersonation`, `manage-authorization`, `manage-clients`, `manage-events`, `manage-identity-providers`, `manage-realm`, `manage-users`, `query-clients`, `query-groups`, `query-realms`, `query-users`, `realm-admin`, `view-authorization`, `view-clients`, `view-events`, `view-identity-providers`, `view-realm`, `view-users`.

`manage-users` can only assign admin roles the assigner already holds.

### Fine-grained admin permissions (Realm Settings → Admin Permissions ON)
Policy-based delegation over resource types **Users, Groups, Clients, Roles**. Admin types: server admins (`admin`, master), realm admins (`realm-admin`), delegated admins (permission-based). Server/realm admins bypass permission evaluation. Scopes are independent (no transitive grant). Permissions need ≥1 policy; granted only if **all** policies GRANT; resource-specific permissions take precedence over all-resource. Query access needs `query-users`/`query-groups`/`query-clients`. Built-in policy types: User, Group, Role (used for partial evaluation/filtering at DB level).

### Account Console
`server-root/realms/{realm-name}/account` (extra scopes via `?scope=phone`). Users manage: profile, sign-in (OTP, Passkey 2FA, passwordless Passkey), Device activity, Linked accounts (IdP), Applications, Groups (needs `view-groups` role; Direct membership filter).

---

## 12. Threat mitigation & security checklist

### Brute-force detection (Realm Settings → Security Defenses → Brute Force Detection)
Disabled by default. Locked-out users see the generic "Invalid username or password". Modes:

**Lockout permanently** — Max Login Failures (30), Quick Login Check Milliseconds (1000), Minimum Quick Login Wait (1 min). **Lockout temporarily** — adds Strategy (Multiple/Linear), Wait Increment (1 min), Max Wait (15 min), Failure Reset Time (12 h). Multiples wait = `WaitIncrement * floor(count/MaxFailures)`; Linear = `WaitIncrement * (1 + count - MaxFailures)`. **Permanent after temporary** — adds Maximum temporary Lockouts (1). Downside: enables DoS by locking known accounts → pair with IPS reading RHBK login-failure logs.

### Security defenses & checklist
- **Hostname**: validate acceptable hostnames if not behind a validating proxy.
- **Admin endpoints**: same port as user traffic — do not expose externally if unneeded.
- **Read-only attributes**: internal metadata always read-only (`KERBEROS_PRINCIPAL`, `LDAP_ID`, `LDAP_ENTRY_DN`, `CREATED_TIMESTAMP`, `createTimestamp`, `modifyTimestamp`, `userCertificate`, `saml.persistent.name.id.for.*`, `ENABLED`, `EMAIL_VERIFIED`; admins also: first five). Extend via `--spi-user-profile--declarative-user-profile--read-only-attributes=foo,bar*` and `--admin-read-only-attributes`.
- **Clickjacking**: X-Frame-Options + Content-Security-Policy (Security Defenses); default same-origin iframe policy.
- **SSL/HTTPS**: enforce in production; client adapters should use a truststore.
- **CSRF**: state-cookie matching (login + Account Console protected); Admin Console uses bearer tokens (CSRF-immune).
- **Redirect URIs**: register specific patterns; non-http(s) schemes must be explicit (`custom:/app/*`); avoid `*`. Use *secure redirect uris enforcer* executor / Client Policies.
- **SSRF**: validate client URI fields (JWKS URI, rootUrl, adminUrl, redirectUris, webOrigins) with the **Secure Client URIs Pattern** executor (Allowed URI Patterns = Java regex allowlist; empty/invalid blocks all). Example: `^https://([a-zA-Z0-9-]+\.)?mycompany\.com(/.*)?$`.
- **Tokens**: shorten access-token lifespan; PKCE; mTLS holder-of-key; push not-before on compromise; auth-code lifespan < 10 s.
- **Password DB**: PBKDF2-HMAC-SHA512, 210000 iterations.
- **Scope**: limit role scope mappings; remove `offline` scope where unneeded; exclude scopes from discovery.
- **Auth session limit**: `--spi-authentication-sessions--infinispan--auth-sessions-limit=100` (default 300 AuthenticationSessionEntity per Root).
- FAPI / OAuth 2.1 compliance via Client Policies.

---

## 13. kcadm.sh (Admin CLI)

`bin/kcadm.sh` (Linux) / `kcadm.bat` (Windows). Set `KEYCLOAK_HOME`, add `$KEYCLOAK_HOME/bin` to PATH.

### Auth
```bash
kcadm.sh config credentials --server http://localhost:8080 --realm master --user admin
```
Maintains a session in `$HOME/.keycloak/kcadm.config` (override with `--config`). `--no-config` authenticates per-invocation (nothing saved). Password prompted unless `--password` or env `KC_CLI_PASSWORD`. Client-only login uses client secret or Signed JWT. Truststore for HTTPS:
```bash
kcadm.sh config truststore --trustpass *** ~/.keycloak/truststore.jks
```
**Air-gap:** use `https://kc.example.internal`, prepare `truststore.jks` with internal CA; never pass `--password` on the command line — use env or prompt.

### CRUD pattern
`create|get|update|delete ENDPOINT [ARGS]` → POST/GET/PUT/DELETE on `SERVER_URI/admin/realms/REALM/ENDPOINT`. `-r TARGET_REALM` overrides realm. `-s name=value` (JSON-parsed), `-f FILE`/`-f -` (body), `-o` print result, `-i` return ID only, `-n` no-merge update (PUT without GET), `--fields`, `--format csv --noquotes`, `--offset`/`--limit`.

### Common commands
```bash
# Realms
kcadm.sh create realms -s realm=demorealm -s enabled=true
kcadm.sh get realms --fields realm,enabled
kcadm.sh update realms/demorealm -s enabled=false
kcadm.sh delete realms/demorealm

# Keys (components, providerType org.keycloak.keys.KeyProvider; parentId = realm id)
kcadm.sh get keys -r demorealm
kcadm.sh create components -r demorealm -s name=rsa-generated -s providerId=rsa-generated \
  -s providerType=org.keycloak.keys.KeyProvider -s parentId=<REALM_ID> \
  -s 'config.priority=["101"]' -s 'config.active=["true"]' -s 'config.keySize=["2048"]'

# Events config
kcadm.sh update events/config -r demorealm -s 'eventsListeners=["jboss-logging"]'
kcadm.sh update events/config -r demorealm -s eventsEnabled=true -s eventsExpiration=172800
kcadm.sh update events/config -r demorealm -s adminEventsEnabled=true -s adminEventsDetailsEnabled=true

# Caches
kcadm.sh create clear-realm-cache -r demorealm -s realm=demorealm   # also clear-user-cache, clear-keys-cache

# Roles / users / groups
kcadm.sh create roles -r demorealm -s name=user -s 'description=Regular user'
kcadm.sh get-roles -r demorealm --uusername testuser --effective
kcadm.sh add-roles --uusername testuser --rolename user -r demorealm
kcadm.sh create users -r demorealm -s username=testuser -s enabled=true
kcadm.sh set-password -r demorealm --username testuser --new-password *** --temporary
kcadm.sh create groups -r demorealm -s name=Group
kcadm.sh update users/<UID>/groups/<GID> -r demorealm -n   # add user to group

# Identity providers
kcadm.sh get identity-provider/instances -r demorealm --fields alias,providerId,enabled
kcadm.sh create identity-provider/instances -r demorealm -s alias=keycloak-oidc -s providerId=keycloak-oidc \
  -s enabled=true -s config.authorizationUrl=... -s config.tokenUrl=... \
  -s config.clientId=demo-oidc-provider -s config.clientSecret=***   # providerId: oidc, saml, google, etc.

# User storage (components, providerType org.keycloak.storage.UserStorageProvider)
kcadm.sh create user-storage/<ID>/sync?action=triggerFullSync
kcadm.sh create user-storage/<ID>/sync?action=triggerChangedUsersSync
kcadm.sh create testLDAPConnection -s action=testConnection -s bindCredential=*** \
  -s bindDn=uid=admin,ou=system -s connectionUrl=ldaps://ldap.example.internal:636 -s useTruststoreSpi=always
```

### Realm import/export
- **Admin-Console / partialImport** (CLI): create on `partialImport`, set `ifResourceExists` to `FAIL`/`SKIP`/`OVERWRITE`:
```bash
kcadm.sh create partialImport -r demorealm2 -s ifResourceExists=FAIL -o -f demorealm.json
```
- For **backups / server-to-server transfer**, use **boot-time** import/export only — Admin-Console/partial exports are not suitable.

**Air-gap:** carry boot-time export JSON across the boundary on approved media; sanitize secrets (replace with `***`) before transfer and re-inject via vault on import.

_Source: Red Hat build of Keycloak 26.6 Server Administration Guide (docs.redhat.com), distilled offline._
