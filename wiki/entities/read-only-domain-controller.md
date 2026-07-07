---
title: Read-Only Domain Controller (RODC)
type: entity
domain: active-directory
slug: read-only-domain-controller
summary: A domain controller that holds a read-only copy of the AD DS database with a filtered attribute set and a per-RODC password replication policy, designed for branch offices and untrusted locations.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/RODC/Install-a-Windows-Server-2012-Active-Directory-Read-Only-Domain-Controller--RODC---Level-200- (Microsoft Learn — Install a Windows Server 2012 Active Directory Read-Only Domain Controller (RODC) (Level 200), fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/RODC/Read-Only-Domain-Controller-Updates (Microsoft Learn — Read-Only Domain Controller Updates, fetched 2026-06-18)
  - kb:ad-ds-install-a-windows-server-2012-active-directory-read-only-domain-controller-rodc-level-200
  - kb:ad-ds-read-only-domain-controller-updates
provenance_extracted: 14
provenance_inferred: 4
provenance_ambiguous: 0
tags: [directory-services, security, concept]
status: draft
updated: 2026-07-02
---

# Read-Only Domain Controller (RODC)

**A domain controller that stores a read-only, partial copy of the Active Directory database — suitable for branch offices where physical security cannot be guaranteed.**

## Body

An RODC holds a read-only replica of the NTDS.DIT that accepts no write operations; clients that need to write are referred to a writable DC. Because the database is read-only, an RODC compromise cannot be used to inject objects or modify the directory directly (inferred from the read-only guarantee and the branch-office threat model).

### Filtered attribute set

A domain-wide **filtered attribute set (FAS)** defines which attributes are excluded from RODC replication entirely. Attributes tagged as confidential can be kept off RODCs so that their theft yields less sensitive data. The FAS is configured on the schema and is forest-wide (inferred).

### Password Replication Policy (PRP)

By default, the RODC caches **no passwords** for any account. The **Password Replication Policy** controls, per-RODC, which accounts are permitted (Allowed RODC Password Replication Group) or denied (Denied RODC Password Replication Group) from having their passwords cached on that RODC.

Default deny entries include Administrators, Server Operators, Backup Operators, Account Operators, and the domain-wide Denied RODC Password Replication Group. Until an account's password is cached, authentication for that account requires a writable DC to be reachable; if the WAN is down, the account cannot authenticate at the branch (inferred).

### Admin role separation

A non-domain-admin user or group can be set as the **Delegated Administrator** for an individual RODC. That person gains local administrative rights on the RODC equivalent to the local Administrators group but is not a member of Domain Admins. This allows branch staff to manage the local DC without receiving domain-level privileges.

### Deployment: staged vs. unstaged

RODC installation supports two paths:

1. **Staged** — a Domain Admin pre-creates an unoccupied RODC computer account (via ADAC or `Add-ADDSReadOnlyDomainControllerAccount`). A delegated branch admin then attaches a server to that account using `Install-ADDSDomainController -UseExistingAccount:$true`. The PRP, site, DNS, and GC settings are locked in at staging time.
2. **Unstaged** — Domain Admin promotes the server directly using `Install-ADDSDomainController -ReadOnlyReplica:$true` in a single step.

`adprep /rodcprep` must have been run in the domain before any staged RODC account is created; it runs automatically when the first unstaged RODC is promoted.

DNS and Global Catalog are enabled on RODCs by default because branch sites depend on local DNS resolution and GC lookups when the WAN is unavailable (inferred).

### Replication

RODCs replicate inbound-only from a writable DC. They have no outbound replication partners. This asymmetry means a hijacked RODC cannot poison other DCs' copies of the directory (inferred).

## Contradictions / caveats

- If no writable DC is reachable and an account's password has not been pre-cached on the RODC, interactive logon fails for that account — plan the PRP to include accounts that must authenticate at the branch offline.
- `adprep /rodcprep` must be run once per domain before staged RODC account creation. The warning "adprep /rodcprep wasn't yet run" is shown if this is skipped.
- An IFM source for an RODC should come from a writable DC; using another RODC as IFM source produces false-positive replication warnings.
- Windows Server 2012 R2 and Windows Server 2012 introduced no changes to `adprep /rodcprep`.

## Reference notes
- [[ad-ds-install-a-windows-server-2012-active-directory-read-only-domain-controller-rodc-level-200]]
- [[ad-ds-read-only-domain-controller-updates]]

## See also
- [[fsmo-roles]]
- [[securing-active-directory]]
- [[ad-ds-deployment]]
- [[install-promote-domain-controller]]
- [[tiered-administration-model]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-install-a-windows-server-2012-active-directory-read-only-domain-controller-rodc-level-200|Install a Windows Server 2012 Active Directory Read-Only Domain Controller (RODC) (Level 200)]]
- [[ad-ds-read-only-domain-controller-updates|Read-Only Domain Controller Updates]]
<!-- crosslink:end -->
