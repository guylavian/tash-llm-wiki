# Wiki tag taxonomy — controlled vocabulary

This is the **only** source of legal `tags:` values. `tags.py` and `lint.py` parse
this file (the backticked tokens under each facet heading) — keep tags from these
lists, kebab-case. Tags are navigation/faceting aids, not facts; they never replace
`sources:` or `provenance:`.

A page's `tags:` should carry **one or more `area`**, optionally **one `kind`**, and
optionally **version** tags when the page is version-specific. Example:

```yaml
tags: [federation, concept, v26.6]
```

## Areas
- `realm` — realms, realm settings, keys/rotation, import/export, localization
- `authn` — authentication flows, MFA/OTP/WebAuthn, passwords, brute force, step-up
- `authz` — Authorization Services: resources/scopes/policies/permissions, UMA, PEP/PDP
- `clients` — OIDC/SAML clients, client auth, scopes, protocol mappers, registration
- `tokens` — access/refresh tokens, sessions, lifespans, exchange, DPoP, logout
- `federation` — LDAP/AD user federation, user storage, mappers, Kerberos
- `brokering` — external OIDC/SAML/social identity providers, IdP mappers
- `users` — users, credentials, roles, groups, profile attributes
- `operator` — RHBK Operator, Keycloak CR, OLM, realm-import CR, OpenShift deploy
- `ha` — clustering, Infinispan caches, multi-site, load balancer, failover, sizing
- `observability` — health, metrics, tracing, OpenTelemetry, SLIs, dashboards
- `server-config` — kc.sh build/runtime, hostname, db, TLS, proxy, vault, features
- `migration` — RH-SSO→RHBK, version upgrades, adapter/provider/theme porting
- `spi` — SPI provider/factory model, custom providers, themes, scripts
- `iac` — Infrastructure-as-Code, the keycloak/keycloak Terraform provider
- `security` — hardening, FAPI/OAuth2.1, threat mitigation, production checklist
- `troubleshooting` — symptom→cause→fix pages, gated-KB pointers
<!-- active-directory areas (notes-first domain) -->
- `directory-services` — AD DS: forests, domains, trees, OUs, schema, the directory database (NTDS)
- `replication` — multi-master replication, the KCC, replication topology/latency, USN/tombstones
- `group-policy` — GPO processing, ADMX/ADML, GPO scope/precedence (LSDOU), loopback
- `ad-dns` — AD-integrated DNS, SRV/`_msdcs` records, locator process, scavenging
- `fsmo` — the five operations-master roles (Schema, Domain Naming, RID, PDC, Infrastructure)
- `trusts` — domain & forest trusts, trust direction/transitivity, SID filtering
- `sites-topology` — sites, subnets, site links, DC locator, replication topology
- `ad-certificate-services` — AD CS / PKI: CA roles, templates, enrollment, autoenrollment
- `ad-authn` — Kerberos & NTLM authentication, SPNs, delegation, tickets

## Kinds
- `concept` — broad synthesis / how-something-works (usually topics/)
- `config-option` — a single config key / flag / setting
- `cli` — a command-line tool or command (kcadm.sh, kcreg.sh, kc.sh)
- `cr-field` — a Keycloak Custom Resource field/section
- `provider` — an SPI provider / built-in component
- `endpoint` — an HTTP endpoint or protocol surface
- `profile` — a client/security policy profile (FAPI, OAuth 2.1)
- `procedure` — a step-by-step task
- `troubleshooting` — a diagnosis/fix page
- `anti-pattern` — a page centered on a common wrong implementation (paired with the rule it violates); used by the upstream SSO-dev best-practice pages (Rule / Anti-pattern / Symptom framing)
- `failure-mode` — a page centered on the observable fault/symptom a wrong implementation produces (the ticket you'd actually see)

## Versions
- `v26.0`
- `v26.2`
- `v26.4`
- `v26.6`

## Domains
The `domain:` **frontmatter facet** (required on every page) partitions the wiki by
technology. It is *not* a tag — it lives in frontmatter, and `lint.py` validates each
page's `domain:` against the domains declared below (parsed from the `- domain: <name>`
lines). `index.py` reads each block to build that domain's `index.<domain>.md`. The
per-domain `areas:` are a subset of the `## Areas` vocabulary above; when you add a
domain that needs a *new* area, add it to `## Areas` too (areas are a flat union).

### keycloak
- domain: keycloak
- areas: [realm, authn, authz, clients, tokens, federation, brokering, users, operator, ha, observability, server-config, migration, spi, iac, security, troubleshooting]
- shape: corpus-backed
- sources: [corpora/keycloak/, _sources/keycloak/]
- review-moc: sso-implementation-review

### active-directory
- domain: active-directory
- areas: [directory-services, replication, group-policy, ad-dns, fsmo, trusts, sites-topology, ad-certificate-services, ad-authn, users, security, troubleshooting, migration]
- shape: notes-first
- sources: [_sources/active-directory/]
- review-moc: active-directory-implementation-review

<!-- Template — copy per new technology (placeholders are ignored by lint/index):
### <domain>
- domain: <domain>
- areas: [...]                       # also add any NEW area to ## Areas above
- shape: notes-first | corpus-backed
- sources: [_sources/<domain>/]      # + corpora/<domain>/ if corpus-backed
- review-moc: <domain>-implementation-review
-->

## Synonyms (normalized away by `tags.py --normalize`)
- `auth` -> `authn`
- `authentication` -> `authn`
- `authorization` -> `authz`
- `oidc` -> `clients`
- `saml` -> `clients`
- `ldap` -> `federation`
- `infinispan` -> `ha`
- `cache` -> `ha`
- `metrics` -> `observability`
- `tracing` -> `observability`
- `telemetry` -> `observability`
- `terraform` -> `iac`
- `session` -> `tokens`
- `sessions` -> `tokens`
- `hardening` -> `security`
