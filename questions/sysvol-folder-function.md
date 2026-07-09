---
title: What is the function of the SYSVOL folder?
type: question
domain: active-directory
slug: sysvol-folder-function
status: draft
summary: SYSVOL is the shared system volume on every domain controller that hosts the Group Policy template files, logon/logoff/startup/shutdown scripts, and other domain-wide file-based policy content, replicated between DCs via FRS or DFSR.
sources:
  - kb:ad-ds-group-policy-overview
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controller-troubleshooting
  - kb:ad-ds-ad-forest-recovery-authoritative-recovery-sysvol
  - kb:ad-ds-install-active-directory-domain-services-level-100
  - kb:ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview
provenance:
  extracted: 10
  inferred: 1
  ambiguous: 0
question_tier: conceptual
updated: 2026-07-09
---

# What is the function of the SYSVOL folder?

**SYSVOL (System Volume) is a mandatory shared folder on every Active Directory domain controller (DC) that stores the file-based components of Group Policy Objects and domain-wide scripts, and is replicated among all DCs within a domain.**

## Core functions

### 1. Group Policy Template (GPT) storage

Every Group Policy Object (GPO) consists of two halves:

- **Group Policy container** — stored in the domain partition of Active Directory, replicated by AD replication.
- **Group Policy template** — the actual policy files (registry settings in `Registry.pol`, security settings, administrative templates, scripts, and other policy data) stored on-disk under `\\<domain>\SYSVOL\<domain>\Policies\{GPO-GUID}\`.

Because the template lives in SYSVOL, a GPO can exist in AD but fail to apply if SYSVOL replication is unhealthy and the template files are not present on a given DC (inferred).

### 2. Logon / logoff / startup / shutdown scripts

Group Policy logon and logoff scripts (for users) and startup/shutdown scripts (for computers) are placed in the SYSVOL share, typically under:
`\\<domain>\SYSVOL\<domain>\scripts\`
or within individual GPO policy paths. Client machines access these over the network via the `NETLOGON` share (which maps to `SYSVOL\<domain>\scripts`).

### 3. DFSR / FRS replication target

SYSVOL is a directory that must be identical across all DCs in a domain. It is kept in sync via:

- **FRS (File Replication Service)** — the legacy replication engine, still supported through Windows Server 2016 (the last release to support FRS).
- **DFSR (Distributed File System Replication)** — the modern, more efficient engine replacing FRS. Newer Windows Server versions and higher functional levels require DFSR for SYSVOL.

The replication service on each DC ensures that GPO templates and scripts created or updated on one DC propagate to all other DCs.

### 4. Netlogon share

The `NETLOGON` share, used during domain logon for processing logon scripts and policies, is a published share pointing into the SYSVOL directory tree. The Netlogon service only shares SYSVOL as `NETLOGON` after SYSVOL initialization is complete.

### 5. Domain controller advertisement prerequisite

A DC does not advertise itself as available (via LDAP ping, DNS SRV, etc.) until SYSVOL has finished its initial synchronization. Event ID 13516 (FRS) or 4604 (DFSR) confirms that SYSVOL initialization is complete and the Netlogon service has been notified to share SYSVOL. This is a gating condition for DC readiness.

### 6. Forest recovery role

During AD forest recovery, SYSVOL requires distinct handling:

- **Authoritative restore** — The first DC restored in the domain must perform an authoritative sync of SYSVOL, typically using `wbadmin -authsysvol` or editing the `msDFSR-Options` attribute, so that this DC's SYSVOL is treated as the primary copy and propagated to all other recovered DCs.
- **Non-authoritative restore** — Subsequent DCs are restored non-authoritatively; their SYSVOL is overwritten from the authoritative source.

### 7. Safe virtualization trigger

When a virtualized DC running Windows Server 2012+ is restored from a hypervisor snapshot, VM-GenerationID detection triggers a non-authoritative SYSVOL synchronization (FRS uses D2 BURFLAGS; DFSR deletes its database files) to ensure SYSVOL converges with the rest of the domain.

## Physical location

Default path: `%SystemRoot%\SYSVOL` (e.g., `C:\Windows\SYSVOL`). The path is configurable during DC promotion via `-SYSVOLPath` (PowerShell) or the AD DS Installation Wizard Paths page. The SYSVOL path is subject to the Win32 `MAX_PATH` limit (260 characters). Microsoft recommends storing NTDS.DIT, logs, and SYSVOL on a dedicated virtual SCSI disk separate from the OS disk for durability and performance.

## ReFS restriction

The AD DS database (NTDS.DIT), transaction logs, and SYSVOL must **not** be placed on a volume formatted with ReFS (Resilient File System). Only NTFS-formatted volumes are supported for these components.

## References

### Microsoft Learn (ground truth)

- [Group Policy overview for Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
- [Virtualized Domain Controller Architecture](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture)
- [AD Forest Recovery — authoritative sync of DFSR-replicated SYSVOL](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-authoritative-recovery-sysvol)
- [AD DS Installation and Removal Wizard page descriptions](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/AD-DS-Installation-and-Removal-Wizard-Page-Descriptions)

### Wiki / vault

- [[group-policy]]
- [[virtualized-domain-controllers]]
- [[ad-forest-recovery]]
- [[dns-for-ad-ds]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-group-policy-overview|Group Policy overview for Windows Server]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-virtualized-domain-controller-troubleshooting|Virtualized Domain Controller Troubleshooting]]
- [[ad-ds-ad-forest-recovery-authoritative-recovery-sysvol|AD Forest Recovery]]
- [[ad-ds-install-active-directory-domain-services-level-100|Install Active Directory Domain Services on Windows Server]]
- [[ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200|Install a New Windows Server 2012 Active Directory Forest (Level 200)]]
<!-- crosslink:end -->
