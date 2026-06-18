# Keycloak / RHBK Wiki — Index

The map of this LLM-maintained wiki. Every topic and entity page links from here.
New pages **must** be added to the right list below (the linter flags orphans).

Schema & workflows: see [`CLAUDE.md`](./CLAUDE.md). **All data lives in this Obsidian
vault**: synthesized pages + the immutable `reference/<domain>/` doc notes (grep them,
or `python3 _meta/bin/kb.py --domain <d> search …` for ranked search) + `../references/`.
Per-domain routing indexes are in `index.<domain>.md` (below).

<!-- index.py:domains:begin (generated — do not edit) -->
## Domains
_Per-domain routing indexes (generated). A QUERY routes here first, then opens the relevant index below to stay inside the model's context window._

- [active-directory](index.active-directory.md) — 3 pages · review lens [[active-directory-implementation-review]]
- [keycloak](index.keycloak.md) — 157 pages · [[_ref-keycloak|800 reference notes]] · review lens [[sso-implementation-review]]
<!-- index.py:domains:end -->

## Topics
- [[ldap-user-federation]] — importing/syncing users from LDAP & Active Directory
- [[ha-cross-site]] — multi-cluster / cross-site Active-Passive HA with Infinispan
- [[tokens-and-sessions]] — access/refresh token lifespans, sessions, token exchange
- [[oidc-client-best-practices]] — how to write the client/refresh/validation/logout code correctly (+ RFC 9700 upstream)
- [[client-libraries-by-stack]] — which OIDC library per stack (Java / Node / SPA) + migration-readiness signal
- [[saml-clients-and-migration]] — SAML SP integration, which SAML adapters survive RHBK, SLO/air-gap
- [[air-gapped-client-integration]] — disconnected-network library acquisition, validation, migration
- [[terraform-keycloak-iac]] — managing Keycloak as IaC (keycloak/keycloak provider): RHBK base_path, air-gap mirror, drift
- [[rhsso-to-rhbk-migration]] — migrating RH-SSO 7.6 → RHBK (server, operator, adapters) + RHBK version upgrades
- [[server-config-migration]] — mapping standalone.xml subsystems (DB/TLS/cache/hostname/vault) to kc.sh options
- [[spi-provider-model]] — SPI provider/factory model, JAR deployment + kc.sh build, override/order rules
- [[operator-deployment]] — deploying RHBK via the Operator: OLM install → Keycloak CR → access
- [[operator-advanced-config]] — truststores, podTemplate, scheduling, secret refs, resources
- [[fine-grained-authorization]] — Authorization Services: resources, scopes, policies, permissions, PEP/PDP, UMA
- [[securing-apps-oidc-saml]] — OIDC vs SAML, client types, flows, endpoints, FAPI/OAuth2.1/DPoP
- [[rhbk-ha-architectures]] — single-cluster vs multi-cluster HA, embedded vs external Infinispan, sizing
- [[troubleshooting-index]] — triage map by area (DB, HA, TLS, LDAP, operator, tokens, upgrade, perf) with public fixes + gated pointers
- [[server-configuration]] — config sources, build vs runtime, precedence, dev/prod modes
- [[production-checklist]] — secure-by-default requirements for `kc.sh start` in production

- [[observability-stack]] — health, metrics, tracing & OpenTelemetry centralization end to end
- [[realm-administration]] — realm settings: SSL, email, themes, login options
- [[authentication-flows]] — flows, requirement types, MFA, WebAuthn, step-up
- [[identity-brokering]] — external OIDC/SAML/social IdPs as an identity broker
- [[security-hardening-checklist]] — mitigating security threats, production hardening

### SSO implementation review (upstream `web:` tier — IETF/OIDF/OWASP best practice)
- [[sso-implementation-review]] — **MOC / evaluation lens**: rule→anti-pattern→symptom checklists (client + backend) + symptom→cause reverse index
- [[bff-token-handler]] — Backend-for-Frontend / Token Handler: confidential server holds tokens, browser gets only HttpOnly cookies
- [[access-token-validation-resource-server]] — what a resource server must verify on every token (sig/exp/iss/aud/scope) before granting access
- [[jwt-validation-pitfalls]] — the JWT-checking mistakes (alg=none, unverified kid, skipped aud/exp) that defeat token validation

## Entities
- [[realm-keys-and-rotation]] — active/passive key providers and rotation procedure
- [[otp-policies]] — TOTP vs HOTP OTP policy configuration
- [[password-policies]] — password strength rules and hashing (Argon2/PBKDF2)
- [[brute-force-detection]] — temporary/permanent lockout on failed logins
- [[step-up-authentication]] — ACR→LoA mapping for level-based auth
- [[kcadm-cli]] — kcadm.sh Admin CLI for CRUD against the Admin REST API
- [[realm-import-export]] — partialImport and boot-time export caveats
- [[roles-and-groups]] — realm/client/composite roles and group role assignment
- [[managing-users-credentials]] — users, user profile attributes, credentials
- [[realm-resource-access]] — delegating admin via realm-management client roles
- [[opentelemetry-centralization]] — global telemetry-* options → one OTLP collector
- [[health-endpoints]] — /health/* probes (started/live/ready) on the management port
- [[management-port]] — the port 9000 management interface (health + metrics)
- [[server-metrics-endpoint]] — /metrics OpenMetrics endpoint, families, histograms/SLO buckets
- [[event-metrics]] — keycloak_user_events_total user-activity counters
- [[tracing-otlp]] — OpenTelemetry distributed tracing: OTLP exporter & sampling
- [[service-level-indicators]] — availability/latency/error SLIs & SLOs in PromQL
- [[grafana-dashboards]] — official troubleshooting & capacity-planning dashboards
- [[metrics-exemplars]] — linking metric points to traces via exemplars
- [[kc-bootstrap-admin]] — bootstrapping the first/temporary admin account
- [[ldap-storage-mode]] — import vs. read-only/writable edit modes for LDAP
- [[ldap-mappers]] — attribute/group/role mappers on an LDAP provider
- [[rhbk-operator]] — the Keycloak CR / OLM operator for OpenShift deployments
- [[oidc-token-validation]] — JWKS (offline) vs. introspection (online)
- [[3scale-rhsso-support]] — 3scale 2.14 ↔ RH-SSO 7.6 support matrix (user-supplied)
- [[quarkus-config-migration]] — EAP standalone.xml → Quarkus kc.sh config model & sources
- [[database-auto-migration]] — automatic vs manual JPA schema migration on first start
- [[operator-cr-migration]] — RH-SSO Operator → RHBK Operator CR rewrite (Realm Import, recreate strategy)
- [[adapter-migration]] — dropped RH-SSO Java adapters & OIDC/SAML client-setting changes
- [[custom-provider-migration]] — Jakarta EE 10 + consolidated KeycloakSession provider/theme porting
- [[distributed-caches]] — Infinispan caches in pods: embedded vs external, cache types
- [[user-storage-spi]] — bridge external user/credential stores into RHBK's user metamodel
- [[javascript-providers-scripts]] — script Authenticator/mapper/policy; the scripts-must-be-a-JAR constraint
- [[keycloak-themes]] — theme types, theme.properties, Theme Selector/Resource SPIs
- [[vault-spi]] — custom secrets-vault extension SPI
- [[override-built-in-providers]] — same id + order(), default-provider selection, disabling providers
- [[keycloak-session-spi]] — KeycloakSession lookup of other providers, context & lifecycle
- [[keycloak-cr]] — the Keycloak CR (k8s.keycloak.org/v2alpha1) field map
- [[operator-olm-install]] — OLM install, manual upgrade approval, disconnected mirror
- [[keycloak-realm-import]] — KeycloakRealmImport CR (create-only, placeholders)
- [[additional-options]] — additionalOptions escape hatch for omitted server options
- [[operator-rolling-updates]] — spec.update strategies, rolling-updates:v2
- [[custom-keycloak-image]] — pre-optimized custom images, startOptimized
- [[keycloak-truststores]] — trusted-certificate configuration on the CR
- [[operator-scheduling]] — affinity/tolerations/spread + default zone/node rules
- [[operator-pod-template]] — unsupported.podTemplate raw Pod override (Tech Preview)
- [[operator-secret-references]] — Secret/ConfigMap refs + ~1-min poll rolling restart
- [[operator-resources]] — compute requests/limits + defaults (1700MiB/2GiB)
- [[operator-initial-admin]] — bootstrapAdmin & the -initial-admin Secret
- [[operator-ingress]] — built-in ingress, className, proxy.headers exposure
- [[authorization-resources-scopes]] — protected resources & their scopes (the objects to protect)
- [[authorization-policy-types]] — built-in policy types (user/role/group/client/time/JS/regex/aggregated)
- [[authorization-permissions]] — resource- vs scope-based permissions binding policies to objects
- [[decision-strategies]] — Unanimous/Affirmative/Consensus combination + enforcement modes
- [[protection-api]] — UMA Protection API endpoints and the PAT (uma_protection)
- [[requesting-party-token]] — the RPT and the UMA-ticket token grant for obtaining permissions
- [[permission-ticket]] — UMA permission ticket and the person-to-person sharing flow
- [[policy-enforcer]] — Policy Enforcement Point (Java/JS enforcers, keycloak-js/authz)
- [[policy-enforcement-mode]] — Enforcing/Permissive/Disabled default-deny knob
- [[policy-evaluation-tool]] — Admin Console Evaluate tab for simulating authorization requests
- [[oidc-endpoints]] — the standard OIDC/OAuth2 endpoints from the well-known discovery doc
- [[oidc-grant-types]] — auth code/client credentials/device/CIBA vs discouraged implicit & direct grant
- [[client-authentication-methods]] — secret / signed-JWT / signed-JWT-with-secret; public vs confidential
- [[client-registration-service]] — DCR/SAML-descriptor REST API; Initial & Registration Access Tokens
- [[client-registration-cli]] — kcreg.sh self-service client config CLI
- [[token-exchange]] — standard V2 (supported) vs legacy V1 (preview/deprecated)
- [[dpop]] — RFC 9449 sender-constrained, key-bound tokens
- [[fapi-oauth21-profiles]] — built-in FAPI 1/2 and OAuth 2.1 client-policy profiles
- [[oidc-logout]] — OIDC logout endpoint (redirect/direct) & SAML single logout
- [[mod-auth-mellon]] — Apache SAML SP module fronting non-SAML apps with RHBK as IdP
- [[external-data-grid-operator]] — Cross-DC external Data Grid via the Data Grid Operator; remote-store CR options
- [[ha-load-balancer-failover]] — AWS Global Accelerator, /lb-check health probe, fencing Lambda, sticky sessions
- [[multi-site-feature-flag]] — the `multi-site` CR feature that enables /lb-check + multi-cluster mode
- [[site-synchronization]] — split-brain re-sync: take-offline, clearcache, bring-online
- [[session-persistence-volatile]] — DB-backed vs volatile (cache-as-source-of-truth) sessions
- [[rhbk-db-connection-pool]] — equal initial/min/max JDBC pool sizing for HA; XA-off on Aurora
- [[config-sources-precedence]] — the 4 config sources and their priority order
- [[build-vs-runtime-options]] — build-time (optimized image) vs runtime options
- [[hostname-v2]] — frontend/backchannel/admin URLs, hostname-strict, validations
- [[database-configuration]] — supported DBs, drivers, build+runtime db settings
- [[tls-configuration]] — HTTPS via PEM or keystore, ports, cert reloading
- [[reverse-proxy-configuration]] — proxy-headers, ports, sticky sessions, exposed paths
- [[management-interface]] — health & metrics management server (server-config angle)
- [[feature-flags]] — features / features-disabled, preview/deprecated categories
- [[keycloak-vault]] — file-based and KeyStore vaults for secrets
- [[tf-realm-resources]] — Terraform: the realm & realm-scoped resources (events, localization, user profile, scopes, keystores)
- [[tf-openid-client]] — Terraform: core OIDC clients, client scopes, scope permissions, service-account roles
- [[tf-client-authorization]] — Terraform: Authorization Services resources, scopes, policy types & permissions
- [[tf-protocol-mappers]] — Terraform: OIDC & SAML protocol mappers shaping claims/assertions
- [[tf-saml-clients]] — Terraform: SAML-protocol clients, client scopes & default-scope attachments
- [[tf-identity-providers]] — Terraform: external OIDC/SAML/social IdPs & IdP mappers for brokering
- [[tf-ldap-federation]] — Terraform: LDAP/AD user federation & the full set of LDAP mappers
- [[tf-roles-groups-users]] — Terraform: roles, groups, users, memberships/role assignments & role mappers
- [[tf-authentication-flows]] — Terraform: authentication flows, subflows, executions, config & realm bindings
- [[tf-data-sources]] — Terraform: read-only data sources for referencing existing Keycloak objects

### SSO best-practice concepts (upstream `web:` tier — feed [[sso-implementation-review]])
- [[pkce]] — bind the auth code to the requesting client; blocks code interception/injection (S256)
- [[redirect-uri-validation]] — exact-match registered redirect_uris; loose matching = open-redirect / code exfiltration
- [[state-and-nonce]] — `state` stops login-CSRF, `nonce` stops ID-token replay/injection; both validated client-side
- [[token-storage-browser]] — why no browser token store is XSS-safe; in-memory vs localStorage vs BFF
- [[refresh-token-rotation]] — one-time-use refresh tokens + replay detection revokes the grant chain
- [[audience-and-scope-checks]] — reject tokens whose `aud` isn't this API; enforce scope/role per operation
- [[dpop-sender-constraining]] — RFC 9449: bind tokens to a client-held key so a stolen token is useless
- [[mtls-bound-tokens]] — RFC 8705: certificate-bound access tokens (cnf/x5t#S256) for confidential clients
- [[rp-initiated-logout]] — end_session_endpoint, id_token_hint, post_logout_redirect_uri done right
- [[back-channel-logout]] — server-to-server logout tokens; the only logout that survives closed tabs
- [[cors-for-spa]] — scope CORS/web-origins to the app origin; never wildcard the token endpoint
- [[service-to-service-client-credentials]] — machine-to-machine grant: confidential client, no user, audience-scoped
- [[authorization-server-metadata-discovery]] — RFC 8414 / OIDC discovery: trust `.well-known`, validate issuer
- [[issuer-identification-mixup]] — RFC 9207 `iss` response param; defends multi-IdP mix-up attacks
- [[token-revocation]] — RFC 7009 revoke endpoint; what revocation does and doesn't invalidate
- [[token-introspection]] — RFC 7662 introspection for opaque tokens; caching and privacy caveats
- [[native-app-oauth]] — RFC 8252: system browser + PKCE + loopback/claimed-https redirects for mobile/desktop
- [[fapi2-security-profile]] — FAPI 2.0 baseline: sender-constrained tokens, PAR, exact redirect, attacker model
- [[bearer-token-usage]] — RFC 6750: Authorization header only, TLS, no tokens in URLs/logs

### Troubleshooting (public fixes)
- [[oracle-jdbc-failover]] — Oracle TCPS failover broken at startup (ORA-17002); driver-version fix
- [[persistent-sessions-db-cleanup]] — expired `user_session` rows linger in PostgreSQL; cleanup tuning
- [[admin-console-confidential-lockout]] — Admin UI lockout after security-admin-console made confidential
- [[fips-startup-bouncycastle]] — FIPS BC UnsatisfiedLinkError + Argon2 admin-login failure
- [[bootstrap-admin-dns-query]] — `dns_query can not be null or empty` (ISPN000541); use `--cache=local`
- [[operator-proxy-port-required]] — operator "Proxy port is required!" with portless cluster proxy
- [[separate-sso-admin-hostnames]] — distinct sso/admin hosts without forced redirect
- [[ad-idp-link-loss-objectguid]] — sporadic AD link loss / merge prompts; use immutable `objectGUID`
- [[uneven-pod-load-master-realm]] — hot pod + LOGIN_ERROR flood from master-realm auth

## Questions
- [questions/ldap-import-vs-noimport.md](./questions/ldap-import-vs-noimport.md)
- [questions/rhbk-default-password-hash.md](./questions/rhbk-default-password-hash.md)
- [questions/active-passive-session-consistency-failover.md](./questions/active-passive-session-consistency-failover.md)
- [questions/rhsso-to-rhbk-custom-providers-spis.md](./questions/rhsso-to-rhbk-custom-providers-spis.md)
- [questions/angular-spa-oidc-best-practice.md](./questions/angular-spa-oidc-best-practice.md)
- [questions/spa-resource-server-implementation-review.md](./questions/spa-resource-server-implementation-review.md)

---
_Seeded 2026-06-16. Grow it via the INGEST / QUERY operations in `CLAUDE.md`.
Run `python3 wiki/_meta/bin/lint.py` to check health, or `--status` for the
delta-manifest audit. Tooling lives in `wiki/_meta/bin/` (excluded from scanners)._
