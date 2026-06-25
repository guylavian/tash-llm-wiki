---
title: Virtualized Domain Controllers
type: topic
domain: active-directory
slug: virtualized-domain-controllers
summary: Windows Server 2012 introduced safe virtualization for AD DS domain controllers, using VM-GenerationID to detect snapshot rollbacks and prevent USN divergence; pre-2012 hypervisors lack this protection and remain vulnerable.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100 (Microsoft Learn — Safely virtualizing Active Directory Domain Services (AD DS), fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Deployment-and-Configuration (Microsoft Learn — Virtualized Domain Controller Deployment and Configuration, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Architecture (Microsoft Learn — Virtualized Domain Controller Architecture, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v (Microsoft Learn — Virtualizing domain controllers with Hyper-V, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Support-for-using-Hyper-V-Replica-for-virtualized-domain-controllers (Microsoft Learn — Support for using Hyper-V Replica for virtualized domain controllers, fetched 2026-06-18)
provenance_extracted: 22
provenance_inferred: 6
provenance_ambiguous: 0
symptoms:
  - "Event ID 2095.*previously acknowledged USN"
  - "Dsa Not Writable.*0x4"
  - "Event ID 1988.*lingering object"
  - "Event ID 2170.*Generation ID change has been detected"
tags: [directory-services, replication, virtualization, concept]
status: draft
updated: 2026-06-18
---

# Virtualized Domain Controllers

**Running Active Directory domain controllers as virtual machines requires Windows Server 2012 or later to safely handle snapshot and restore operations via VM-GenerationID; earlier OS versions are vulnerable to USN rollback.**

## The core problem: USN rollback

AD DS replication uses Update Sequence Numbers (USNs) and an InvocationID to track which changes each DC has already sent and received. Each DC stores its InvocationID in the `msDS-GenerationId` attribute of its NTDS Settings object.

When a hypervisor administrator applies a snapshot outside the DC's awareness, the DC's USN reverts in time while its replication partners still believe they have received all updates up to the pre-snapshot USN. Replication then silently stops converging: partners refuse to request changes they believe they already have, but those changes are permanently gone from the rolled-back DC. The symptom is **Event ID 2095** in the Directory Service log and a registry entry `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters\Dsa Not Writable = 0x4`.

Importantly, USN rollback is often undetected when the rolled-back DC's USN advances past the highest USN the partner last received — replication resumes but with divergent, duplicate objects (**lingering objects**, Event ID 1988).

## Windows Server 2012 safe virtualization (VM-GenerationID)

Beginning with Windows Server 2012 and hypervisors that expose **VM-GenerationID**, AD DS detects rollback automatically. The hypervisor stores a GUID — the VM-Generation ID — that changes whenever the VM is restored from a snapshot or imported. AD DS stores the same GUID in the DIT (`msDS-GenerationID`). On every boot, NTDS compares the live driver value to the stored value. If they differ:

1. **InvocationID is reset** — replication partners see a new identity and re-replicate from that DC.
2. **RID pool is discarded** — prevents duplicate SID issuance.
3. **SYSVOL is non-authoritatively synchronized** — FRS/DFSR re-syncs from a healthy partner.

This is called **safe restore** and requires no administrator intervention. It is logged as Event ID 2170. The feature extends to shut-down VMs restored from snapshot, not only running VMs.

Safe virtualization requires:
- Guest OS: Windows Server 2012 or later
- Hypervisor: must expose VM-GenerationID (Hyper-V on Windows Server 2012+; third-party hypervisors — contact vendor)
- AD DS schema version 56 or higher; forest functional level Windows Server 2003 Native or higher

## Snapshot dangers pre-2012

On Windows Server 2008 R2 and earlier, there is no VM-GenerationID protection. Applying a hypervisor snapshot to a running or shut-down DC causes USN rollback. The domain controller is quarantined (Net Logon paused, replication disabled) only if another DC detects the anomaly — silent divergence is common. VHD/VHDX file copies produce the same outcome regardless of OS version (inferred: a manually copied VHD does not change the VM-Generation ID, so even 2012 safeguards are not triggered).

The **only supported backup and restore method** at any version is a VSS-aware backup application (e.g., Windows Server Backup). VM snapshots must never be used as a substitute for system-state backups.

## DC cloning (fast DC provisioning)

Windows Server 2012 introduced [[vdc-cloning]] as a fast, safe mechanism to provision additional DCs from a source image. The clone detects a new VM-GenerationID on first boot, reads `DCCloneConfig.xml`, and promotes itself as a new DC — reusing the source NTDS.DIT to minimize replication traffic. This requires the source DC to be a member of the **Cloneable Domain Controllers** group and the PDC Emulator to be reachable.

## Hyper-V Replica

When using Hyper-V Replica for DR, planned and unplanned failover of Windows Server 2012+ DCs is supported. On failover, the replica DC detects a VMGenID change and triggers safe-restore safeguards — resetting InvocationID and discarding the RID pool — before rejoining replication. Windows Server 2008 R2 replica VMs support only planned failover and are at risk of USN rollback on unplanned failover.

## Placement and security

- Run at least two virtualized DCs per domain on **different hypervisor hosts** to eliminate single points of failure (inferred: losing one host must not lose the domain).
- The hypervisor host's local administrator credentials are functionally equivalent to Domain Admin for every guest DC on that host.
- Store NTDS.DIT, logs, and SYSVOL on a virtual SCSI disk (second VHD) separate from the OS disk; SCSI provides Forced Unit Access (FUA) and better durability guarantees.
- Avoid differencing disk VHDs for DC VMs: they degrade performance and complicate snapshot hygiene.
- Disable Hyper-V time synchronization for DC guests — the DC must follow the domain time hierarchy, not the hypervisor clock. See [[windows-time-service]].
- For branch offices with poor physical security, prefer [[read-only-domain-controller]] to limit credential exposure.

## Recovery from USN rollback

If safe-restore safeguards are unavailable (pre-2012 guest, unsupported hypervisor, or VHD copy):

1. Isolate the rolled-back DC from the network immediately.
2. Forcibly demote it (removes Active Directory, creates a standalone server).
3. Clean up its metadata on a healthy DC — see [[ad-metadata-cleanup]].
4. Transfer or seize any FSMO roles the DC held — see [[fsmo-roles]].
5. Re-promote from scratch, or restore from a known-good VSS backup.

Do **not** delete or modify the `Dsa Not Writable` registry value; it is forensic evidence and removing it leaves the DC in an unsupported state.

## Contradictions / caveats

- Safe restore is **not** a replacement for system-state backups. Changes made after the snapshot point and not yet replicated outbound are permanently lost.
- VHD/VHDX files restored by block-level file copy (not through the hypervisor) do **not** change the VM-Generation ID — even on Windows Server 2012+ hosts — and therefore bypass safe-restore safeguards.
- Do not pause or save-state a DC VM for longer than the forest tombstone lifetime (default 180 days); resuming past that point creates lingering objects.
- On a suspended (not shut-down) DC, restoring a snapshot requires restarting the NTDS service to trigger a new RID pool request: `Restart-Service NTDS -Force`.

## Reference notes

- [[ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100]]
- [[ad-ds-virtualized-domain-controller-deployment-and-configuration]]
- [[ad-ds-virtualized-domain-controller-architecture]]
- [[ad-ds-virtualized-domain-controllers-hyper-v]]
- [[ad-ds-support-for-using-hyper-v-replica-for-virtualized-domain-controllers]]

## See also

- [[vdc-cloning]]
- [[vm-generation-id-safe-restore]]
- [[ad-replication]]
- [[ad-metadata-cleanup]]
- [[read-only-domain-controller]]
