---
title: Why does an AD password change take time to take effect in RHBK LDAP user federation?
type: question
domain: keycloak
slug: ldap-password-change-propagation-delay
summary: "When a user changes their password in Active Directory, RHBK continues to accept the old password briefly while rejecting the new one, then flips. This is caused by a combination of AD multi-DC replication latency and the RHBK user cache policy — not by password caching (RHBK never imports passwords)."
sources:
  - kb:rhbk-26-4-user-storage-federation
  - kb:rhbk-26-0-user-storage-federation
  - kb:user-storage-federation
  - kb:rhbk-26-4-user-storage-spi
  - kb:rhbk-26-4-caching
  - kb:rhbk-26-4-multi-cluster-introduction
  - kb:rhbk-26-0-concepts-multi-site
  - kb:rhbk-26-2-concepts-multi-site
  - guide:server_administration_guide
  - gated:https://access.redhat.com/solutions/7005967
  - gated:https://access.redhat.com/solutions/7124865
provenance:
  extracted: 8
  inferred: 2
  ambiguous: 0
tags: [authn, federation]
status: draft
updated: 2026-06-22
---

# Why does an AD password change take time to take effect in RHBK LDAP user federation?

**The delay is not caused by RHBK caching the password itself — RHBK never imports or caches LDAP passwords. The delay comes from two distinct mechanisms: Active Directory multi-domain-controller replication latency, and the RHBK Infinispan user cache that caches the user object (but not the credential).**

## The short answer

The observed behavior — old password works, new password doesn't, then it flips — is most likely **AD replication delay** across multiple domain controllers. RHBK always validates passwords against AD via an LDAP BIND operation; if the DC handling the BIND hasn't yet received the password-change replication, the old password is still valid on that DC. A secondary contributor is the **RHBK user cache** (`CachePolicy` on the LDAP provider), which caches the user object and can cause stale AD `userAccountControl` / `pwdLastSet` state when the MSAD User Account Mapper is involved.

## How RHBK validates LDAP/AD passwords

RHBK's LDAP/AD provider performs password validation exclusively via the LDAP/AD protocol — it never stores or caches the actual password:

> "Red Hat build of Keycloak never imports passwords. Password validation always occurs on the LDAP server."
> — RHBK 26.4 Server Administration Guide, Chapter 4.3.2 (Storage mode)

When a user authenticates with username + password:

1. RHBK looks up the user in its Infinispan user cache → if not found, checks the local imported DB → if still not found, queries the LDAP provider.
2. RHBK performs an LDAP BIND operation against the configured AD connection URL using the user's DN and the supplied password.
3. AD responds with success (the BIND worked) or failure (invalid credentials).
4. RHBK never writes the password to its own database — authentication is purely delegated to AD.

## Cause 1 (most likely): Active Directory multi-DC replication latency

Typical AD deployments have multiple domain controllers. When a user changes their password:

1. The change is written to one DC (the one that processed the password-reset request).
2. AD replicates the new password hash to all other DCs. Default intra-site replication is **15 seconds** (notification-based), but cross-site replication follows the site-link schedule (default **180 minutes**, configurable).
3. RHBK's LDAP provider is configured with `Connection URL` pointing to a specific DC or DNS load-balanced name (`ldap://dc1.example.com:389` or `ldap://domain.example.com:389`).
4. If the RHBK connection hits a DC that **has not yet received** the replication:
   - The **OLD password** still works (the DC has the old hash).
   - The **NEW password** is rejected (the DC doesn't have the new hash yet).
5. Once replication propagates to all DCs, the new password works and the old one stops — the "flip."

**This is the most common explanation** for the exact pattern described: a gradual transition window rather than an instantaneous switch.

### If using Kerberos (`Allow Kerberos authentication` ON + `UseKerberosForPasswordAuthentication` ON)

Password-based authentication is converted to a Kerberos password-authentication request. The Kerberos KDC (typically a DC) must also have the updated password hash. If the KDC that issues the TGT hasn't received the replication yet, the same delay applies.

## Cause 2: RHBK user cache and CachePolicy

Although passwords are never cached, the **user object is cached** in RHBK's Infinispan user cache. This cache includes:

- The user's profile attributes (username, email, first name, last name)
- The user's DN and LDAP provider reference
- Data hydrated by **LDAP mappers**, including the **MSAD User Account Mapper**

The MSAD User Account Mapper reads two AD-specific attributes on every access:
- `userAccountControl` — determines if the account is enabled/disabled/locked
- `pwdLastSet` — if `0`, triggers an `UPDATE_PASSWORD` required action

Each LDAP provider has a **Cache Policy** (`cachePolicy`) that controls how long the user object stays cached:

| Cache Policy | Behavior |
|---|---|
| `DEFAULT` | No TTL eviction; evicted only on user modification (e.g., admin explicitly saves user) |
| `EVICT_DAILY` | Evicted daily at a configured hour |
| `EVICT_WEEKLY` | Evicted weekly on a configured day/hour |
| `MAX_LIFESPAN` | Evicted after N seconds |

If the Cache Policy is `DEFAULT` (typical), the user object stays in the Infinispan cache until it is explicitly invalidated. The `pwdLastSet` value read from AD at cache time is frozen in the cached user object. When the user authenticates, RHBK still validates the password via LDAP BIND — but the MSAD mapper uses the **cached** `pwdLastSet`, which can affect whether the user is prompted to change their password on next login.

### How to clear the user cache immediately

If you need to force user cache eviction after an AD password change:

```bash
kcadm.sh create clear-user-cache -r <realm-name> -s realm=<realm-name>
```

This evicts all cached user objects from the Infinispan user cache for that realm. On the next authentication, the user object is freshly loaded from LDAP.

You can also evict per-provider or adjust the Cache Policy in the LDAP provider's admin console settings.

## Cause 3: Existing SSO sessions

If the user had an active SSO session **before** the password change, they continue to access applications without re-authenticating. From their perspective, they are "still logged in with the old password." This is not the same as the login-page scenario described, but it can confuse diagnosis — distinguish between:

- **Fresh login attempt** (enters credentials on login page) → password is validated against AD via LDAP BIND
- **Session reuse** (redirected to app without credential prompt) → no password validation occurs; existing token/session is still valid

## Summary of mechanisms

| Mechanism | Affects password validation? | Typical delay | Mitigation |
|---|---|---|---|
| AD multi-DC replication | Yes — BIND is against whichever DC handles it | Intra-site: ~15s; Cross-site: 15-180 min | Direct RHBK at a single DC, or wait for replication |
| RHBK user cache (`CachePolicy`) | No (password always goes to AD), but can affect `userAccountControl`/`pwdLastSet` | Until cache eviction or expiry | `kcadm.sh create clear-user-cache` or set a shorter `maxLifespan` |
| Existing SSO sessions | No re-auth required | Until session timeout | N/A (session idle/max config) |
| LDAP connection pool | Indirect (connection reuse for BIND) | None (BIND is per-request) | N/A |

## See also

- [[ldap-user-federation]]
- [[ldap-storage-mode]]
- [[ldap-mappers]]
- [[managing-users-credentials]]
- [[tokens-and-sessions]]

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **RHBK 26.4 Server Administration Guide, Chapter 4 — Using external storage** (`guide:server_administration_guide`, `kb:rhbk-26-4-user-storage-federation`) — "Red Hat build of Keycloak never imports passwords. Password validation always occurs on the LDAP server."
- **RHBK 26.0 Server Administration Guide, Chapter 4 — Using external storage** (`kb:rhbk-26-0-user-storage-federation`) — Same wording, confirming the behavior across versions.
- **RHBK 26.4 User Storage SPI guide** (`kb:rhbk-26-4-user-storage-spi`) — Documents the user cache, `OnUserCache`, `CachePolicy`, and eviction.
- **RHBK 26.4 Caching guide** (`kb:rhbk-26-4-caching`) — Infinispan cache architecture: local user caches default to 10,000 entries, invalidation-cache semantics for clusters.
- **RHBK 26.4 Multi-cluster Introduction & Concepts** (`kb:rhbk-26-4-multi-cluster-introduction`, `kb:rhbk-26-0-concepts-multi-site`) — Warnings that stale caches cause users to "log in with an old password" when invalidation messages fail to propagate across sites.
- **RHBK 26.4 Admin CLI** (`kb:rhbk-26-4-admin-cli`) — `clear-user-cache` endpoint and `cachePolicy` configuration on LDAP providers.
- **Gated: Does RH-SSO cache password in the database from LDAP?** — https://access.redhat.com/solutions/7005967 (subscriber login required).
- **Gated: How to clear realm cache, user cache, and key cache in RHBK** — https://access.redhat.com/solutions/7124865 (subscriber login required).

### Wiki pages

- [[ldap-user-federation]] — Overview of RHBK's LDAP/AD federation, storage modes, edit modes, and mappers.
- [[ldap-storage-mode]] — Import ON/OFF and EDIT modes (`READ_ONLY`, `WRITABLE`, `UNSYNCED`).
- [[ldap-mappers]] — LDAP mappers including the MSAD User Account Mapper.
- [[distributed-caches]] — Infinispan cache architecture in RHBK.
- [[troubleshooting-index]] — Triage map by area; LDAP-related issues.

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[rhbk-26-4-user-storage-federation|Chapter 4. Using external storage]]
- [[rhbk-26-0-user-storage-federation|Chapter 4. Using external storage]]
- [[rhbk-26-4-user-storage-spi|Chapter 5. User Storage SPI]]
- [[rhbk-26-4-caching|Chapter 10. Configuring distributed caches]]
- [[rhbk-26-4-multi-cluster-introduction|Chapter 3. Multi-cluster deployments]]
- [[rhbk-26-0-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
- [[rhbk-26-2-concepts-multi-site|Chapter 2. Concepts for multi-site deployments]]
<!-- crosslink:end -->
