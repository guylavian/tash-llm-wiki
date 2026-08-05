---
title: Delegated Managed Service Accounts (dMSA)
type: entity
domain: active-directory
slug: delegated-managed-service-accounts
summary: A Windows Server 2025 service-account type that binds authentication to a specific machine identity using fully randomized, Credential-Guard-protected keys — preventing Kerberoasting and enabling migration from legacy service accounts.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-overview (Microsoft Learn — Delegated Managed Service Accounts overview, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/delegated-managed-service-accounts-set-up-dmsa (Microsoft Learn — Setting up delegated Managed Service Accounts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts (Microsoft Learn — Service Accounts in Windows Server, fetched 2026-06-18)
  - kb:ad-ds-delegated-managed-service-accounts-overview
  - kb:ad-ds-delegated-managed-service-accounts-set-up-dmsa
  - kb:ad-ds-understand-service-accounts
provenance_extracted: 14
provenance_inferred: 3
provenance_ambiguous: 0
tags: [users, security, directory-services]
status: draft
updated: 2026-07-02
graph_community: "Group Managed Service Accounts (gMSA)"
---

# Delegated Managed Service Accounts (dMSA)

**A Windows Server 2025 machine-linked service account whose secret is randomized, held only on the DC, and bound to a named device identity — making password theft and Kerberoasting structurally impossible.**

## Body

A dMSA is a new account type introduced in Windows Server 2025. It extends [[group-managed-service-accounts]] concepts but goes further: whereas a gMSA password is machine-generated and auto-rotated, it can still be retrieved from a DC by any authorized host. A dMSA secret is derived from the machine account credential and is never accessible outside the DC — it cannot be found or retrieved anywhere else (inferred from source: the secret is held by the DC and computed per-machine).

Authentication is **device-bound**: only the specific machine identities listed in the dMSA's `groupMSAMembership` attribute can obtain a ticket. Combined with Credential Guard (CG), this means even compromised credentials cannot be used from an unauthorized device.

### dMSA vs gMSA

| Dimension | gMSA | dMSA |
|---|---|---|
| Password generation | KDS root key (DC-computed) | DC-held secret derived from machine credential |
| Machine binding | No (any authorized host can retrieve) | Yes — only the named machine can authenticate |
| Server scope | Multiple servers | Single server only |
| Credential Guard support | No | Yes — CG binds tickets and rotates password |
| Kerberoasting risk | Mitigated (auto-rotation) but not eliminated | Structurally eliminated (secret never leaves DC) |
| Windows Server version | 2012+ | 2025 only |

### Migration flow

dMSA can supersede an existing traditional service account:

1. Run `Start-ADServiceAccountMigration` — grants the old account Generic Read to all properties on the dMSA and Write access to `msDS-groupMSAMembership`; sets `msDS-DelegatedMSAState=1`. During this phase the DC tracks which machines log on using the old account and automatically adds them to the dMSA's `groupMSAMembership`.
2. Wait at least **two Kerberos ticket lifetimes (14 days)**, recommended four lifetimes (28 days), before completing. This ensures all machines have been discovered and group membership has replicated.
3. Run `Complete-ADServiceAccountMigration` — copies SPNs, delegation settings, and AuthN policy to the dMSA; sets `msDS-DelegatedMSAState=2`; disables the original account via the UAC disable bit and strips its SPNs.

The old account should **not** be deleted after migration — keep it as a rollback target. Use `Undo-ADServiceAccountMigration` or `Reset-ADServiceAccountMigration` to revert if needed.

### Key operational caveats

- You **cannot** migrate an sMSA or gMSA to a dMSA — only traditional (user) service accounts are eligible.
- Each client machine must have the registry key `HKLM:\...\Kerberos\Parameters\DelegatedMSAEnabled = 1` set before it can use a dMSA.
- Pay attention to sites with replication cycles longer than the default ticket renewal time of **10 hours**: `groupMSAMembership` is checked at every ticket renewal, so slow replication can cause membership to be lost during initial cycles (inferred: from the per-site replication delay caveat in the source).
- **Unconstrained delegation** stops working after migration completes if the old account used it and Credential Guard is enabled.
- A **KDS root key** ([[kds-root-key]]) must exist before creating a dMSA. Verify with `Get-KdsRootKey`.
- Setting up dMSA requires Windows Server 2025 DCs; mixed environments with older child domains use **realms** (Group Policy: *Enable Delegated Managed Service Account logons*) to allow older domains to participate.

### Event log

Enable the `Microsoft\Windows\Security-Kerberos\Operational` provider in Event Viewer. Key events:

| Event ID | Meaning |
|---|---|
| 307 | dMSA migration in progress or complete |
| 308 | Machine adding itself to `PrincipalsAllowedToRetrieveManagedPassword` |
| 309 | Kerberos client fetching keys for dMSA from DC |

## Contradictions / caveats

The sources note that setting `msDS-DelegatedMSAState=3` is required for standalone dMSAs (not migration) but the overview article doesn't enumerate all state values — the setup article fills that gap. The migration timing guidance (14–28 days) is a recommendation, not an enforced limit; environments with replication delays should err toward the longer window (inferred).

## Reference notes
- [[ad-ds-delegated-managed-service-accounts-overview]]
- [[ad-ds-delegated-managed-service-accounts-set-up-dmsa]]
- [[ad-ds-understand-service-accounts]]

## See also
- [[service-accounts-overview]]
- [[group-managed-service-accounts]]
- [[kds-root-key]]
- [[securing-active-directory]]
- [[credential-theft-and-attractive-accounts]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-delegated-managed-service-accounts-overview|Delegated Managed Service Accounts overview in Windows Server 2025]]
- [[ad-ds-delegated-managed-service-accounts-set-up-dmsa|Setting up delegated Managed Service Accounts (dMSA) in Windows Server 2025]]
- [[ad-ds-understand-service-accounts|Service Accounts in Windows Server]]
<!-- crosslink:end -->
