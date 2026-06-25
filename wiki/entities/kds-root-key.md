---
title: KDS Root Key
type: entity
domain: active-directory
slug: kds-root-key
summary: The forest-wide cryptographic master key held by the Key Distribution Service (kdssvc.dll) that domain controllers use to derive gMSA and dMSA passwords; must be created before the first managed service account and carries a mandatory 10-hour replication wait.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/create-the-key-distribution-services-kds-root-key (Microsoft Learn — Create the Key Distribution Services KDS Root Key, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview (Microsoft Learn — Group Managed Service Accounts overview, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-set-up-dmsa (Microsoft Learn — Setting up delegated Managed Service Accounts, fetched 2026-06-18)
provenance_extracted: 8
provenance_inferred: 2
provenance_ambiguous: 0
tags: [security, directory-services]
status: draft
updated: 2026-06-18
---

# KDS Root Key

**The single forest-wide secret seed stored in AD (`CN=Master Root Keys,CN=Group Key Distribution Service,CN=Services,CN=Configuration`) from which every domain controller computes managed service account passwords on demand.**

## Body

The **Key Distribution Service** (`kdssvc.dll`) was introduced in Windows Server 2012. It provides a shared secret — the **KDS root key** — that DCs use to deterministically derive [[group-managed-service-accounts]] passwords from the account's AD attributes. Member hosts retrieve the current and previous password by contacting a DC over LDAP; no password is ever stored on the host. The same root key is a prerequisite for [[delegated-managed-service-accounts]] in Windows Server 2025.

### The 10-hour propagation window

After running `Add-KdsRootKey -EffectiveImmediately`, DCs wait up to **10 hours** before generating gMSA passwords. This is a safety measure: the key must replicate to all DCs so that any DC can answer a password-retrieval request. Attempting to create or use a gMSA before the key has fully replicated can cause password-retrieval failures, especially if DCs run limited replication schedules or a replication issue exists.

### Creating the root key

```powershell
# Production — waits 10 hours before taking effect on remote DCs
Add-KdsRootKey -EffectiveImmediately

# Test/lab only — backdates 10 hours to skip the wait
Add-KdsRootKey -EffectiveTime ((Get-Date).AddHours(-10))
```

Requires membership in **Domain Admins** or **Enterprise Admins**. A 64-bit PowerShell session is required. Verify creation by checking for Event ID **4004** in the KDS event log.

### Storage and lifecycle

- Stored at: `CN=Master Root Keys,CN=Group Key Distribution Service,CN=Services,CN=Configuration,DC=<forest root>`
- The `msKds-DomainID` attribute links to the computer object of the creating DC. If that DC is later decommissioned, the attribute points to a tombstone — this is harmless and can be ignored or updated to another DC's computer object.
- Keys rotate periodically; gMSA member hosts can retrieve both the current and the preceding key to allow seamless password transitions (inferred: derived from the source's statement that hosts retrieve "current and preceding password values").

### Deletion caveat

Deleting and re-creating the root key can cause stale-cache issues: DCs may continue using the old key after deletion. If a root key is re-created, **restart the KDC service on all domain controllers** to flush the cache.

### Relationship to managed account types

| Account type | Requires KDS root key | Version |
|---|---|---|
| gMSA | Yes | Windows Server 2012+ |
| dMSA | Yes | Windows Server 2025 |
| sMSA | No | Windows Server 2008 R2+ |
| Virtual account | No | Windows Server 2008+ |

## Contradictions / caveats

`-EffectiveImmediately` is misleading — the local DC uses the key immediately, but other DCs cannot use it until replication succeeds (up to 10 hours). In a lab with a single DC the distinction is moot, but in production with slow or broken replication it is a real operational trap (inferred).

## Reference notes
- [[ad-ds-create-the-key-distribution-services-kds-root-key]]
- [[ad-ds-group-managed-service-accounts-overview]]
- [[ad-ds-delegated-managed-service-accounts-set-up-dmsa]]

## See also
- [[group-managed-service-accounts]]
- [[delegated-managed-service-accounts]]
- [[service-accounts-overview]]
- [[ad-replication]]
