---
title: RID Issuance Management
type: entity
domain: active-directory
slug: rid-issuance-management
summary: The RID master FSMO issues RID pools to domain controllers; Windows Server 2012 added consumption warnings, a 10%-ceiling block, and a 30-bit-to-31-bit unlock escape hatch for near-exhausted domains.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/Managing-RID-Issuance (Microsoft Learn — Managing RID Issuance, fetched 2026-06-18)
provenance_extracted: 18
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "Windows can't create the object because the Directory Service was unable to allocate a relative identifier"
  - "Directory-Services-SAM event 16657"
  - "Directory-Services-SAM event 16656"
  - "Directory-Services-SAM event 16653"
  - "Directory-Services-SAM event 16658"
tags: [directory-services, fsmo, troubleshooting, concept]
status: draft
updated: 2026-06-18
---

# RID Issuance Management

**Every AD security principal (user, group, computer) gets a unique Relative Identifier (RID) drawn from a per-DC pool issued by the RID master; Windows Server 2012 adds safeguards against pool exhaustion.**

## Body

Each domain controller holds a local **RID pool** — a pre-allocated block of RID values — and draws from it when creating new security principals. When the pool is nearly consumed, the DC contacts the **RID master** [[fsmo-roles]] to request a new block. By default each request is for 500 RIDs (`RID Block Size` registry value, capped at 15,000 in Windows Server 2012+). The resulting SID for each new object is `<domain SID>-<RID>`.

### Global RID space

By default the global RID pool is **2^30 ≈ 1.07 billion** RIDs per domain. A domain is unlikely to exhaust this organically, but problematic scenarios include:

- Bulk provisioning scripts accidentally creating large numbers of objects.
- Repeated forest recovery or DC restore/re-promote cycles (RID pool invalidation consumes a block).
- Frequent `InvalidateRidPool` operations.
- Historically inflated `RID Block Size` registry values (prior to the 15,000 cap).

### Windows Server 2012 safeguards

**Periodic consumption warnings (event 16658).** At every 10%-consumed milestone of the global pool the System event log records a Directory-Services-SAM warning on all DCs. Events accelerate as the pool shrinks.

**RID Block Size cap.** The registry value `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\RID Values\RID Block Size` is capped at **15,000**. If set higher, the value is treated as 15,000 and event 16653 is logged at each reboot until corrected.

**Ceiling enforcement.** When the RID master allocates a pool that crosses the **90% consumed** threshold, it:
- Logs event 16656 (approaching ceiling) on any DC that requests a pool at the 99% mark.
- Logs event 16657 (ceiling hit) on the RID master itself and sets `msDS-RIDPoolAllocationEnabled = FALSE` on `CN=RID Manager$,CN=System,DC=...`, blocking all further issuance.

To unblock after investigating runaway creation, use **LDP.exe** to set `MsDS-RidPoolAllocationEnabled = TRUE` on the RID Manager$ object on a Windows Server 2012 RID master. Be aware: unblocking allows issuance to continue toward the hard limit, after which only forest recovery or domain migration restores the ability to create security principals.

### 31-bit unlock (emergency escape hatch)

If the 30-bit space (≈1.07 B) is approaching exhaustion, the global pool can be expanded to **2^31 ≈ 2.15 billion** by setting the hidden `SidCompatibilityVersion = 1` attribute on the RootDSE via LDP.exe on a Windows Server 2012 RID master. Event 16655 confirms the expansion.

**Caveats before unlocking:**
- This operation is **irreversible** (reverts only via full forest recovery to a pre-unlock backup).
- Windows Server 2003 and Windows Server 2008 DCs cannot issue RIDs from the 31-bit pool; Windows Server 2008 R2 DCs require KB 2642658. Ensure all DCs are Windows Server 2012 or patched WS2008R2 before unlocking.
- Application compatibility issues may exist with SIDs generated from the extended range (inferred — Microsoft guidance warns of this).
- Use only in conjunction with the ceiling-enforcement unblock above, not preemptively (inferred).

### Troubleshooting flow

When account creation fails with "unable to allocate a relative identifier":

1. Check the System event log on the failing DC and RID master for events 16642–16658.
2. Run `Dcdiag.exe /TEST:RidManager /v` to check available pool and RID master reachability.
3. Validate AD replication health with `Repadmin.exe` — a replication failure can prevent the DC from contacting the RID master.

## Contradictions / caveats

- There is a known leak: creating an account that fails (e.g., password does not meet complexity) still consumes a RID. This is unfixed.
- Prior to Windows Server 2012 there was a `rIDSetReferences` attribute leak on Windows Server 2008 R2 DCs, fixed by KB 2618669.
- Domain migration or forest recovery remains the only option once the 31-bit space is exhausted.

## Reference notes
- [[ad-ds-managing-rid-issuance]]

## See also
- [[fsmo-roles]]
- [[ad-forest-recovery]]
- [[security-identifiers-sid]]
- [[ad-replication]]
