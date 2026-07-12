---
title: How does virtualization safely support Active Directory domain controllers?
type: question
question_tier: conceptual
domain: active-directory
slug: virtualized-domain-controllers-safety
summary: Windows Server 2012+ DCs use VM-GenerationID (a hypervisor GUID that changes on snapshot restore) to detect rollbacks and automatically reset the InvocationID, discard the RID pool, and non-authoritatively sync SYSVOL — preventing USN rollback and replication divergence.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100 (Safely virtualizing AD DS, fetched 2026-07-07)
  - kb:ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controllers-hyper-v
provenance:
  extracted: 18
  inferred: 2
  ambiguous: 0
status: draft
updated: 2026-07-07
---

# How does virtualization safely support Active Directory domain controllers?

**The core risk with virtualized DCs is USN rollback — hypervisor snapshots revert the DC's update-sequence clock, causing silent replication divergence. Windows Server 2012+ eliminates this via VM-GenerationID, a hypervisor-supplied GUID that changes on any snapshot restore or VM copy, triggering automatic safe-restore safeguards on every boot.** (`virtualized-domain-controllers.md:35-51`)

## The problem: USN rollback

AD replication tracks changes via a per-DC tuple `(InvocationID, USN)` — the identity of the DC's database instance plus a monotonically increasing counter. When a VM snapshot reverts a DC's USN counter, the DC reuses old USN values for new writes. Its replication partners still believe they have received all changes up to the pre-snapshot USN and stop requesting. The directory silently diverges. (`virtualized-domain-controllers.md:35-42`)

Symptoms include **Event ID 2095** ("previously acknowledged USN, no corresponding change in invocation ID") and the registry marker `Dsa Not Writable = 0x4` under `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters`. (`virtualized-domain-controllers.md:39-40`) Worse, when the rolled-back DC's USN advances past the partner's high-water mark before replication resumes, divergence is **undetected** — producing lingering objects (Event ID 1988). (`virtualized-domain-controllers.md:41-42`)

## The solution: VM-GenerationID (Windows Server 2012+)

Windows Server 2012 introduced **VM-GenerationID** — a 128-bit GUID the hypervisor exposes to the guest OS through the `vmgencounter.sys` driver. During DC promotion, AD DS reads this value and stores it in the `msDS-GenerationId` attribute of the DC's computer object inside `NTDS.DIT`. On every subsequent boot — and on snapshot restore of a *running* VM — NTDS compares the current driver value to the stored value: (`vm-generation-id-safe-restore.md:34-45`, `virtualized-domain-controllers.md:43-51`)

| Comparison | Action |
|---|---|
| **Match** | Normal boot; USNs are valid |
| **Mismatch, no `DCCloneConfig.xml`** | **Safe restore**: InvocationID reset, RID pool discarded, SYSVOL non-authoritatively synced. Event ID 2170 logged |
| **Mismatch + `DCCloneConfig.xml`** | **VDC cloning**: clone promotion begins (see [[vdc-cloning]]) |
| **No VMGenID from hypervisor + `DCCloneConfig.xml`** | Clone boots into **DSRM** (unsupported platform). Event ID 2169/2175 |

### Safe-restore actions

1. **InvocationID reset** — the DC gets a new replication identity; partners request all changes from USN 0 for this identity, ensuring full convergence. (`vm-generation-id-safe-restore.md:49-53`)
2. **RID pool discarded** — the DC requests a fresh pool from the RID Master, preventing duplicate SID issuance from the rolled-back pool. (`vm-generation-id-safe-restore.md:51-52`)
3. **SYSVOL non-authoritative sync** — DFSR deletes its database and re-syncs inbound; FRS sets the D2 BURFLAGS registry key. (`vm-generation-id-safe-restore.md:53`)
4. **`msDS-GenerationId` updated** — the new value is persisted so subsequent boots compare correctly. (`vm-generation-id-safe-restore.md:54`)

All four steps run **automatically** with no administrator intervention. (`virtualized-domain-controllers.md:49-50`)

## Prerequisites

- Guest OS: Windows Server 2012 or later (`virtualized-domain-controllers.md:53-54`)
- Hypervisor: must expose VM-GenerationID (Hyper-V on WS2012+; third-party vendors — verify) (`virtualized-domain-controllers.md:55`)
- AD DS schema version ≥ 56; forest functional level ≥ Windows Server 2003 Native (`virtualized-domain-controllers.md:56`)

## Pre-2012 and unsupported hypervisors

On Windows Server 2008 R2 and earlier — or on hypervisors that do not expose VM-GenerationID — snapshot restore causes USN rollback with no automatic protection. The DC is quarantined (Net Logon paused) only if another DC detects the anomaly; silent divergence is common. (`virtualized-domain-controllers.md:58-60`) VHD/VHDX files restored via file-level copy (not through the hypervisor) bypass safe-restore safeguards regardless of OS version, because the VM-GenerationID does not change (`virtualized-domain-controllers.md:60-61` — `(inferred)`).

## VDC cloning

The same VM-GenerationID mechanism powers [[vdc-cloning]]: copy a source DC's disks, place `DCCloneConfig.xml`, and boot. The clone detects the changed VM-GenerationID, reads the configuration, and promotes itself as a new DC with minimal replication traffic. (`vdc-cloning.md:30-31`) The source DC must be in the **Cloneable Domain Controllers** group and the PDC Emulator must be reachable. (`vdc-cloning.md:36-42`)

## Operational best practices

- Run at least two virtualized DCs per domain on **different hypervisor hosts** (`virtualized-domain-controllers.md:73-74` — `(inferred)`).
- The hypervisor host admin is functionally equivalent to Domain Admin for all guest DCs (`virtualized-domain-controllers.md:75`).
- Store NTDS.DIT, logs, and SYSVOL on a **virtual SCSI disk** (separate from the OS disk) — SCSI provides FUA (`virtualized-domain-controllers.md:76`).
- Avoid differencing disk VHDs for DC VMs (`virtualized-domain-controllers.md:77`).
- **Disable Hyper-V time synchronization** for DC guests — DCs must follow the domain time hierarchy (`virtualized-domain-controllers.md:78`).
- Never pause or save-state a DC VM for longer than the forest tombstone lifetime (default 180 days) (`virtualized-domain-controllers.md:97`).

## Recovery from USN rollback (when safeguards fail)

1. Isolate the rolled-back DC immediately. (`virtualized-domain-controllers.md:85`)
2. Forcibly demote it. (`virtualized-domain-controllers.md:86`)
3. Clean up metadata on a healthy DC (`virtualized-domain-controllers.md:87`).
4. Transfer or seize FSMO roles (`virtualized-domain-controllers.md:88`).
5. Re-promote or restore from a known-good VSS backup (`virtualized-domain-controllers.md:89`).

Do not delete or modify the `Dsa Not Writable` registry value — it is forensic evidence (`virtualized-domain-controllers.md:91`).

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
