---
title: How does virtualization safely support Active Directory domain controllers?
type: question
domain: active-directory
slug: virtualized-domain-controllers-safety
summary: Windows Server 2012+ DCs use VM-GenerationID (a hypervisor GUID that changes on snapshot restore) to detect rollbacks and automatically reset the InvocationID, discard the RID pool, and non-authoritatively sync SYSVOL — preventing USN rollback and replication divergence.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100 (Safely virtualizing AD DS, fetched 2026-07-07)
  - kb:ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controllers-hyper-v
provenance:
  extracted: 12
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# How does virtualization safely support Active Directory domain controllers?

**The core risk with virtualized DCs is USN rollback — hypervisor snapshots revert the DC's update-sequence clock, causing silent replication divergence. Windows Server 2012+ eliminates this via VM-GenerationID, a hypervisor-supplied GUID that changes on any snapshot restore or VM copy, triggering automatic safe-restore safeguards on every boot.**

## The problem: USN rollback

AD replication tracks changes via a per-DC tuple `(InvocationID, USN)` — the identity of the DC's database instance plus a monotonically increasing counter. When a VM snapshot reverts a DC's USN counter, the DC reuses old USN values for new writes. Its replication partners still believe they have received all changes up to the pre-snapshot USN and stop requesting. The directory silently diverges.

Symptoms include **Event ID 2095** ("previously acknowledged USN, no corresponding change in invocation ID") and the registry marker `Dsa Not Writable = 0x4` under `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters`. Worse, when the rolled-back DC's USN advances past the partner's high-water mark before replication resumes, divergence is **undetected** — producing lingering objects (Event ID 1988).

## The solution: VM-GenerationID (Windows Server 2012+)

Windows Server 2012 introduced **VM-GenerationID** — a 128-bit GUID the hypervisor exposes to the guest OS through the `vmgencounter.sys` driver. During DC promotion, AD DS reads this value and stores it in the `msDS-GenerationId` attribute of the DC's computer object inside `NTDS.DIT`. On every subsequent boot — and on snapshot restore of a *running* VM — NTDS compares the current driver value to the stored value:

| Comparison | Action |
|---|---|
| **Match** | Normal boot; USNs are valid |
| **Mismatch, no `DCCloneConfig.xml`** | **Safe restore**: InvocationID reset, RID pool discarded, SYSVOL non-authoritatively synced. Event ID 2170 logged |
| **Mismatch + `DCCloneConfig.xml`** | **VDC cloning**: clone promotion begins (see [[vdc-cloning]]) |
| **No VMGenID from hypervisor + `DCCloneConfig.xml`** | Clone boots into **DSRM** (unsupported platform). Event ID 2169/2175 |

### Safe-restore actions

1. **InvocationID reset** — the DC gets a new replication identity; partners request all changes from USN 0 for this identity, ensuring full convergence.
2. **RID pool discarded** — the DC requests a fresh pool from the RID Master, preventing duplicate SID issuance from the rolled-back pool.
3. **SYSVOL non-authoritative sync** — DFSR deletes its database and re-syncs inbound; FRS sets the D2 BURFLAGS registry key.
4. **`msDS-GenerationId` updated** — the new value is persisted so subsequent boots compare correctly.

All four steps run **automatically** with no administrator intervention.

## Prerequisites

- Guest OS: Windows Server 2012 or later
- Hypervisor: must expose VM-GenerationID (Hyper-V on WS2012+; third-party vendors — verify)
- AD DS schema version ≥ 56; forest functional level ≥ Windows Server 2003 Native

## Pre-2012 and unsupported hypervisors

On Windows Server 2008 R2 and earlier — or on hypervisors that do not expose VM-GenerationID — snapshot restore causes USN rollback with no automatic protection. The DC is quarantined (Net Logon paused) only if another DC detects the anomaly; silent divergence is common. VHD/VHDX files restored via file-level copy (not through the hypervisor) bypass safe-restore safeguards regardless of OS version, because the VM-GenerationID does not change.

## VDC cloning

The same VM-GenerationID mechanism powers [[vdc-cloning]]: copy a source DC's disks, place `DCCloneConfig.xml`, and boot. The clone detects the changed VM-GenerationID, reads the configuration, and promotes itself as a new DC with minimal replication traffic. The source DC must be in the **Cloneable Domain Controllers** group and the PDC Emulator must be reachable.

## Operational best practices

- Run at least two virtualized DCs per domain on **different hypervisor hosts**.
- The hypervisor host admin is functionally equivalent to Domain Admin for all guest DCs.
- Store NTDS.DIT, logs, and SYSVOL on a **virtual SCSI disk** (separate from the OS disk) — SCSI provides FUA.
- Avoid differencing disk VHDs for DC VMs.
- **Disable Hyper-V time synchronization** for DC guests — DCs must follow the domain time hierarchy (see [[windows-time-service]]).
- Never pause or save-state a DC VM for longer than the forest tombstone lifetime (default 180 days).

## Recovery from USN rollback (when safeguards fail)

1. Isolate the rolled-back DC immediately.
2. Forcibly demote it.
3. Clean up metadata on a healthy DC (see [[ad-metadata-cleanup]]).
4. Transfer or seize FSMO roles (see [[fsmo-roles]]).
5. Re-promote or restore from a known-good VSS backup.

Do not delete or modify the `Dsa Not Writable` registry value — it is forensic evidence.

## References

**Wiki:**
- [[virtualized-domain-controllers]]
- [[vm-generation-id-safe-restore]]
- [[vdc-cloning]]
- [[ad-replication]]
- [[ad-metadata-cleanup]]

**Ground-truth:**
- `kb:ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100` — Safely virtualizing AD DS (level 100)
- `kb:ad-ds-virtualized-domain-controller-architecture` — Virtualized DC Architecture
- `kb:ad-ds-virtualized-domain-controllers-hyper-v` — Virtualizing DCs with Hyper-V
- `kb:ad-ds-support-for-using-hyper-v-replica-for-virtualized-domain-controllers` — Hyper-V Replica support for virtualized DCs
- `web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100` — Safely virtualizing AD DS (MS Learn)

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100|Safely virtualizing Active Directory Domain Services (AD DS)]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-virtualized-domain-controllers-hyper-v|Virtualizing domain controllers with Hyper-V]]
<!-- crosslink:end -->
