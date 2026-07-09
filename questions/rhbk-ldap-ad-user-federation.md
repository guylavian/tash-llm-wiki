---
title: How does RHBK's LDAP/AD user federation work?
type: question
question_tier: conceptual
domain: keycloak
slug: rhbk-ldap-ad-user-federation
summary: RHBK ships a built-in LDAP/AD provider under the User Storage SPI that turns directory users into RHBK users, governed by storage mode (import vs on-demand), edit mode (READ_ONLY/WRITABLE/UNSYNCED), and LDAP mappers for attributes/groups/roles.
sources:
  - guide:server_administration_guide
  - ref:rhbk-26-4-user-storage-federation
  - kb:user-storage-federation
  - kb:user-storage-spi
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 0
tags: [federation]
status: reviewed
updated: 2026-07-07
---

# Q: How does RHBK's LDAP/AD user federation work?

## Answer

RHBK includes a built-in LDAP/Active Directory federation provider (User Federation → Add LDAP providers in the admin console). It implements the **User Storage SPI**, the same SPI used for any custom external user store, and supports both plain LDAP and Active Directory vendor presets. The architecture and mechanics are as follows:

### Lookup chain

When a user logs in, RHBK checks in order: the user cache, its local database, then loops through each enabled User Storage provider (ordered by priority) until one returns the user (`rhbk-26-4-user-storage-federation.md:20`). If a provider fails, RHBK does **not** fail over — user databases often have duplicate usernames/emails between providers, and failing over could load the wrong record (`rhbk-26-4-user-storage-federation.md:35`). The local RHBK database is checked first, so keep an admin account local in case LDAP is unreachable (`rhbk-26-4-user-storage-federation.md:31`).

### Storage mode — the *Import Users* switch

| Mode | Behavior |
|---|---|
| **Import ON** (default) | RHBK imports and synchronizes a local copy of each LDAP user into its own DB. Enables full querying/listing and lets other mappers/attributes attach locally. |
| **Import OFF** | Users are read from LDAP on demand with no local copy. Lower storage footprint, but some features that depend on local DB data are limited. Passwords are **never** imported — always validated against LDAP (`rhbk-26-4-user-storage-federation.md:47`). |

With Import OFF, username/email remain case-sensitive (they are lowercased with Import ON). RHBK recommends avoiding case-sensitive usernames as some features may not work correctly (`rhbk-26-4-user-storage-federation.md:106-107`).

### Edit mode

| Mode | Behavior |
|---|---|
| **READ_ONLY** | No changes flow back to LDAP. Profile is immutable from RHBK's side. |
| **WRITABLE** | Profile/password changes propagate back into LDAP automatically. Requires the bind account to have write permission. |
| **UNSYNCED** | Changes stored in RHBK's local DB only, not pushed to LDAP. Useful for read-only LDAP servers. Can cause drift between RHBK and LDAP when combined with Import ON (`ldap-storage-mode.md:39`). |

The Edit Mode and Import Users settings are best decided at provider creation time — changing them later does not retroactively adjust existing LDAP mappers (`rhbk-26-4-user-storage-federation.md:66`).

### LDAP mappers

Mappers are listeners triggered when a user logs in, registers, or is queried. RHBK auto-creates an initial set based on the Vendor/Edit Mode/Import Users combination. Common types:

- **User Attribute Mapper** — maps one LDAP attribute (e.g. `mail`) to an RHBK user attribute (e.g. `email`)
- **FullName Mapper** — maps `cn` to `firstName`/`lastName`
- **Role Mapper** — maps LDAP groups/roles to RHBK realm or client roles
- **Group Mapper** — maps LDAP groups to RHBK groups
- **Hardcoded Attribute Mapper** — forces a value (e.g. `enabled=true`) on every LDAP-linked user
- MSAD vendor preset auto-adds account-control/password mappers

Mappers are configured as `components` with `providerType=org.keycloak.storage.ldap.mappers.LDAPStorageMapper`, manageable via Admin Console or `kcadm.sh` (`ldap-mappers.md:37-44`).

### Synchronization

With Import ON, two sync types are available (`rhbk-26-4-user-storage-federation.md:109-114`):

- **Periodic Full sync** — synchronizes all LDAP users into RHBK's DB
- **Periodic Changed users sync** — only users created/updated since the last sync

Best practice: run **Synchronize all users** on first setup, then periodic changed-users sync.

### Kerberos integration

The LDAP provider has an **Allow Kerberos authentication** toggle that enables Kerberos/SPNEGO authentication with user data provisioned from LDAP. A standalone `KerberosFederationProvider` is also available (lets users self-update profiles). (`rhbk-26-0-configuring-authentication-server-administration-guide.md:530`)

### LDAPS

For `ldaps://` connection URLs, configure a truststore on the RHBK server so it trusts the LDAP server's SSL certificate. The `Use Truststore SPI` property (deprecated) should normally be left as `Always` (`rhbk-26-4-user-storage-federation.md:99-103`). In Operator/OpenShift deployments, the truststore is configured via `spec.truststores` separately from the provider page (`ldap-user-federation.md:50`).

### Provider failure handling

When a provider lookup fails (e.g. LDAP is down), RHBK does **not** fall through to the next provider — the invocation is cancelled (`rhbk-26-4-user-storage-federation.md:30`). A provider can be **disabled** in the admin console to skip it during queries while keeping imported users visible in read-only mode (`rhbk-26-4-user-storage-federation.md:33-34`).

### Provider configuration options (key ones)

- **Priority** — determines provider ordering in the lookup chain
- **Sync Registrations** — if ON, new RHBK users are added to LDAP
- **Remove invalid users during searches** — removes locally-imported users no longer found in LDAP
- **Relative User Creation DN** — sub-DN under Users DN where new users are created (`rhbk-26-4-user-storage-federation.md:80-95`)

### Key caveats

- Passwords are **never** stored locally — always validated against the LDAP server
- Import ON + UNSYNCED edit mode allows local copy to drift from LDAP
- Very large directories with Import ON incur DB insert per user on first query + an LDAP search per imported user on unfiltered searches (performance cost) (`rhbk-26-4-user-storage-federation.md:55`)
- The LDAP provider supports multiple LDAP URLs for HA via the `connectionUrl` field, but gated KB notes that listing multiple URLs does **not** enable transparent failover — the complete User Federation stops working if one URL goes down (`_gated-kb-index.md:2336`)
- CVE-2025-13467: an authenticated realm admin can configure the LDAP provider to connect to a malicious LDAP server with Referral:follow enabled, causing RHBK to deserialize untrusted Java objects (`rhbk-26-2-updates-for-26-2-11.md:26`)

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- `kb:user-storage-federation` — Chapter 4. Using external storage, RHBK 26.4 Server Administration Guide
- `kb:user-storage-spi` — Chapter 5. User Storage SPI, RHBK 26.6 Server Developer Guide
- `ref:rhbk-26-0-configuring-authentication-server-administration-guide.md`
- `ref:rhbk-26-2-updates-for-26-2-11.md` (CVE-2025-13467)
- `ref:_gated-kb-index.md` (multiple LDAP URLs, Kerberos, slowness, mTLS, pool config)

### Wiki
- [[ldap-user-federation]] — topic page: how the built-in LDAP/AD provider works
- [[ldap-storage-mode]] — Import Users vs Edit Mode details
- [[ldap-mappers]] — mapper types and kcadm configuration
- [[user-storage-spi]] — the SPI the built-in provider is implemented on
- [[ldap-import-vs-noimport]] — decision guide for Import Users toggle
- [[ldap-password-change-propagation-delay]] — AD password propagation latency
- [[tf-ldap-federation]] — Terraform resources for LDAP federation

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-4-user-storage-federation|Chapter 4. Using external storage]]
- [[rhbk-26-6-user-storage-spi|Chapter 5. User Storage SPI]]
<!-- crosslink:end -->
