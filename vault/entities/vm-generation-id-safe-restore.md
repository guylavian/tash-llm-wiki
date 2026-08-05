---
title: VM-GenerationID Safe Restore
type: entity
domain: active-directory
slug: vm-generation-id-safe-restore
summary: VM-GenerationID is a hypervisor-supplied GUID that changes on snapshot restore or VM copy; AD DS on Windows Server 2012+ compares it to the stored value in NTDS.DIT and, on mismatch, automatically resets the InvocationID and discards the RID pool to prevent USN rollback and duplicate SID issuance.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100 (Microsoft Learn — Safely virtualizing Active Directory Domain Services (AD DS), fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Architecture (Microsoft Learn — Virtualized Domain Controller Architecture, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v (Microsoft Learn — Virtualizing domain controllers with Hyper-V, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Support-for-using-Hyper-V-Replica-for-virtualized-domain-controllers (Microsoft Learn — Support for using Hyper-V Replica for virtualized domain controllers, fetched 2026-06-18)
  - kb:ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-virtualized-domain-controllers-hyper-v
  - kb:ad-ds-support-for-using-hyper-v-replica-for-virtualized-domain-controllers
provenance_extracted: 16
provenance_inferred: 5
provenance_ambiguous: 0
symptoms:
  - "Event ID 2170.*Generation ID change has been detected"
  - "Event ID 2095.*previously acknowledged USN.*no corresponding change in invocation ID"
  - "Dsa Not Writable = 0x4"
  - "Event ID 1988.*lingering object"
  - "Event ID 2169.*no VM Generation ID detected"
tags: [directory-services, replication, virtualization, troubleshooting]
status: draft
updated: 2026-07-02
graph_community: "Active Directory Replication & Site Topology"
---

# VM-GenerationID Safe Restore

**VM-GenerationID (VMGenID) is a hypervisor-vendor-independent 128-bit identifier exposed to the guest OS; when AD DS detects it has changed since the last boot, it automatically invokes safe-restore safeguards to prevent replication corruption caused by snapshot rollback.**

## How it works

During DC promotion, AD DS reads the current VMGenID from the Windows `vmgencounter.sys` driver and stores it in the DC's computer object attribute `msDS-GenerationId` inside NTDS.DIT.

On every subsequent boot — and whenever a snapshot restore occurs on a running VM — NTDS compares the live driver value to `msDS-GenerationId`:

| Comparison result | Action |
|---|---|
| **Match** | Normal boot continues; USNs are valid. |
| **Mismatch + no DCCloneConfig.xml** | Safe restore: InvocationID reset, RID pool discarded, SYSVOL non-authoritatively synced. Logged as **Event ID 2170**. |
| **Mismatch + DCCloneConfig.xml present** | [[vdc-cloning]] path: clone promotion begins. |
| **No VMGenID from hypervisor + DCCloneConfig.xml** | Clone boots into DSRM (unsupported platform). Logged as **Event ID 2169/2175**. |

## Safe restore actions in detail

When a mismatch is detected and cloning is not intended:

1. **InvocationID is reset** to a new GUID in the NTDS Settings object. Partner DCs now see a new replication identity and request all changes from USN 0 for this new InvocationID — ensuring full convergence.
2. **RID pool is invalidated** — the DC contacts the RID Master to obtain a new pool, preventing duplicate SID issuance from the discarded (rolled-back) pool.
3. **SYSVOL is non-authoritatively synchronized** — DFSR deletes its database files and re-syncs inbound; FRS sets the D2 BURFLAGS registry key to trigger a non-authoritative sync.
4. **`msDS-GenerationId` is updated** in the DIT to the new VMGenID value, so subsequent reboots compare correctly.

This process runs automatically with no administrator input. The DC re-advertises after convergence completes.

## Snapshot rollback scenario (walk-through)

At time T1, snapshot of DC1 (USN=100, InvocationID=A) is taken. Between T1 and T2, 100 users are added (USN=200); all changes replicate to DC2, which records `DC1(A)@USN=200` in its up-to-dateness vector. At T3, the T1 snapshot is restored. DC1's USN reverts to 100 but its VMGenID changes. On next write attempt, DC1 detects the mismatch, resets InvocationID to B, and discards the RID pool. DC2 knows nothing of InvocationID B and requests everything from B@USN=0, safely converging. Meanwhile, T1–T2 changes that had replicated to DC2 replicate back into DC1 — no data loss for changes that had escaped. Changes that had **not** replicated before the restore point are permanently lost.

## USN rollback without VMGenID protection

On hypervisors without VMGenID support (or guests older than Windows Server 2012), snapshots cause **USN rollback**. The rolled-back DC resumes with reused USNs; replication partners believe they are up to date and stop requesting changes from this DC. Divergence is silent until an out-of-range USN is detected, at which point Event ID 2095 fires and the Net Logon service is paused (quarantine). The registry key `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters\Dsa Not Writable = 0x4` is the forensic marker.

**Undetected divergence** occurs when the rolled-back DC's USN counter advances past the partner's high-water mark before replication is attempted — replication resumes but with divergent objects. This surfaces later as **lingering objects** (Event ID 1988). (inferred: the window for undetected divergence grows with replication latency and snapshot age.)

## Hypervisor support matrix

| Hypervisor | VMGenID support | Notes |
|---|---|---|
| Hyper-V on Windows Server 2012+ | Yes | Driver: `vmgencounter.sys` visible in Device Manager as "Microsoft Hyper-V Generation Counter" |
| Windows Server 2008 R2 / 2008 Hyper-V | No | USN rollback protection only via quarantine (Event 2095) |
| Non-Microsoft hypervisors | Varies | Contact vendor; VMGenID is a hypervisor-vendor-independent spec |

When migrating a VM between hypervisors: source supports VMGenID → target does not: safeguards **not** triggered (VMGenID unavailable; if DCCloneConfig.xml present, boots to DSRM). Source does not → target does: safeguards **triggered** (new VMGenID detected against no stored value). Source and target both support VMGenID and definition unchanged: safeguards not triggered (ID unchanged). (inferred: live migration without snapshot does not change VMGenID.)

## Suspended-state caveat

If the DC VM is in a **suspended** (rather than shut-down) state when a snapshot is restored, and then resumed, the NTDS service is already running and does not re-read VMGenID at service start. To force safe-restore safeguards in this scenario, restart the NTDS service manually:

```powershell
Restart-Service NTDS -Force
```

## Contradictions / caveats

- VHD/VHDX files restored via file-level backup or manual copy do **not** change VMGenID — safe-restore safeguards are bypassed even on Windows Server 2012+ hypervisors.
- Safe restore does not recover changes originating after the snapshot point that had not replicated outbound. Those changes are permanently lost.
- Hyper-V Replica failover (planned or unplanned) triggers a VMGenID change on the replica DC, invoking safe restore automatically — this is the expected, supported behaviour for Windows Server 2012+ replica DCs.

## Reference notes

- [[ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100]]
- [[ad-ds-virtualized-domain-controller-architecture]]
- [[ad-ds-virtualized-domain-controllers-hyper-v]]
- [[ad-ds-support-for-using-hyper-v-replica-for-virtualized-domain-controllers]]

## See also

- [[virtualized-domain-controllers]]
- [[vdc-cloning]]
- [[ad-replication]]
- [[krbtgt-reset]]
- [[ad-metadata-cleanup]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100|Safely virtualizing Active Directory Domain Services (AD DS)]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-virtualized-domain-controllers-hyper-v|Virtualizing domain controllers with Hyper-V]]
- [[ad-ds-support-for-using-hyper-v-replica-for-virtualized-domain-controllers|Support for using Hyper-V Replica for virtualized domain controllers]]
<!-- crosslink:end -->
