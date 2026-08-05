---
title: SYSVOL/DFSR Troubleshooting
type: topic
domain: active-directory
slug: sysvol-dfsr-troubleshooting
summary: Recurring SYSVOL/DFSR failure patterns from field reports — folder not syncing to a subset of DCs, SYSVOL/NETLOGON missing after promotion, DFSR's dependence on (not independence from) AD replication after a PDC restore, and the FRS-to-DFSR migration prerequisites — with the non-authoritative-sync remediation path each resolves to.
sources:
  - "web:https://learn.microsoft.com/en-us/answers/questions/1014064/the-sysvol-dfsr-folder-cannot-be-sync-in-couple-of (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1025360/frs-to-dfsr-migration-when-sysvol-netlogon-are-not (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1375980/how-to-restore-a-pdc-domain-controller-dfsr-dfs-na (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1105201/sysvol-netlogon-not-shared-rather-unusual-issue (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1471057/why-does-sysvol-replication-fail-if-the-disk-with (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1483236/how-to-fix-sysvol-policies-not-sync-issue (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 11
provenance_inferred: 2
provenance_ambiguous: 1
tags: [replication, group-policy, troubleshooting]
status: draft
updated: 2026-07-25
---

# SYSVOL/DFSR Troubleshooting

**SYSVOL replication (via DFSR, or legacy FRS) carries GPO templates and logon
scripts between domain controllers; when it silently stops for a subset of DCs,
the standard remediation is a non-authoritative sync — but several field reports
show root causes upstream of that fix (AD replication health, NIC configuration,
unsupported cloning) that the sync alone won't resolve.**

## Community Q&A (upstream)

> Microsoft Q&A threads, not Microsoft support statements. Answerer roles are
> noted per claim — MVP/Microsoft-employee answers carry more weight than
> anonymous community replies, but even those are frequently unconfirmed by the
> original poster. Verify against current Microsoft Learn documentation before
> relying on any of this in production.

### First-line triage: check the DFS Replication event log before syncing

Across every thread in this cluster, the first recommended step — before running
any authoritative/non-authoritative sync — is to check the **DFS Replication**
event log for errors, and to run `repadmin /showrepl` / `repadmin /replsummary`
to confirm plain AD replication is healthy first. Only once AD replication is
confirmed clean does the standard advice move to SYSVOL-specific troubleshooting
(web:1014064, MVP answer; web:1483236, Microsoft-employee-affiliated answer).

### The standard fix: non-authoritative sync per KB2218556

When SYSVOL/DFSR has stopped replicating to one or more DCs but AD replication
itself shows no errors, the documented remediation is a **non-authoritative
synchronization** of DFSR-replicated SYSVOL on the affected DC(s) only — never
on all DCs at once, and never on the PDC unless it's the confirmed source of
truth. Source: "How to force an authoritative and non-authoritative
synchronization for DFS Replication SYSVOL" (KB2218556), linked directly from an
MVP answer (web:1014064). A separate 2024 MS-employee-affiliated answer confirms
the same procedure and adds: back up SYSVOL and the DC first, confirm the
problematic DC is **not** the PDC, then allow 30+ minutes after the sync steps
before expecting SYSVOL to reappear (web:1483236).

### SYSVOL/NETLOGON missing after promotion: DFSR membership disabled + multi-homed NIC

One thread reports SYSVOL and NETLOGON shares entirely absent on a newly
promoted DC (Windows 2019) even though AD replication (users, GPO changes) was
confirmed bidirectional and healthy. The DFS Replication Health Report showed:
*"One or more replicated folders are not replicating to this member because
their memberships are disabled"* (Event ID 4114) — meaning the SYSVOL
replicated-folder membership had been manually disabled on that member and must
be re-enabled via the DFS Management snap-in or `dfsradmin.exe`
(web:1105201). The reporter also checked
`HKLM\SYSTEM\CurrentControlSet\Services\DFSR\Parameters\StopReplicationOnAutoRecovery`
— this should be `0` to let DFSR's JET-database auto-recovery complete and
resume replication on its own; in this case it was already `0`, so it wasn't
the cause here (web:1105201). **(ambiguous)** — the thread's MVP answerer then
identified that the problem DC was multi-homed (two NICs) and recommended
disabling the extra adapter, giving the DC a single static IP with itself listed
first for DNS, then `ipconfig /flushdns` + `/registerdns` + a Netlogon service
restart. The reporter did this and SYSVOL/NETLOGON *still* did not appear —
so multi-homing was a real anti-pattern to fix regardless, but the thread never
confirms it was the actual root cause of the missing shares; it ends with the
MVP requesting fresh `dcdiag`/`repadmin`/`ipconfig` output, unresolved in the
corpus (web:1105201).

### FRS→DFSR migration: SYSVOL/NETLOGON must already exist everywhere first

A DC-promotion blocker: adding a 2019/2022 DC to an older domain fails at
`dcpromo`/`Install-ADDSDomainController` with an FRS warning when SYSVOL is
still on FRS. The prerequisite chain, per an MVP answer, is: (1) domain
functional level must be 2008 or higher, **and** (2) SYSVOL replication must
already have been migrated from FRS to DFSR — both before the first higher-OS-version
DC can be introduced (web:1025360). If some DCs show `SysvolReady=0` in
`HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters` with no
SYSVOL/NETLOGON share at all, and this has persisted longer than the domain's
tombstone lifetime, the recommended path is not to attempt migration on them —
seize FSMO roles to a healthy DC, run [[ad-metadata-cleanup]] to remove the
broken DCs, confirm health with `dcdiag`/`repadmin`, **then** proceed with the
FRS-to-DFSR migration (web:1025360).

### DFSR does not follow AD replication automatically after a DC restore

A recurring misconception: restoring a PDC from backup after a crash will
resync **AD replication** automatically (the restored DC finds an authoritative
partner and becomes non-authoritative for AD data) — but this does **not**
extend to DFSR/SYSVOL content. A Volunteer Moderator (MVP) answer states
explicitly: *"there is no relationship between DFSR replication and AD
replication"* for this purpose, and after restoring a PDC the administrator must
manually compare SYSVOL contents between DCs and set whichever DC has the
newest data as the **primary member** of the DFSR replication group before
normal (non-authoritative) sync will pull correctly — otherwise the restored
DC's stale SYSVOL can silently persist or conflict (web:1375980). See
[[sysvol-folder-function]] for what SYSVOL's DFSR-replicated content actually
contains.

### Unsupported DC cloning breaks AD replication, which breaks SYSVOL/DFSR downstream

A vendor-affiliated answer directly states the reverse dependency: **SYSVOL and DFSR
replication depend on AD replication**, not the other way around. Cloning a
running domain controller with third-party disk-imaging tools (Macrium Reflect,
EaseUS Disk Copy) — instead of the only supported method, sysprep-based
[[vdc-cloning]] — breaks AD replication, and SYSVOL/DFSR replication (and any
other DFSR configuration on that box) stops as a direct downstream effect. The
same thread reports that deleting the stray cloned partitions and temporarily
raising `MaxOfflineTimeInDays` restored replication, years after the original
clone (web:1471057).

## Contradictions / caveats

- The multi-homed-NIC / `StopReplicationOnAutoRecovery` thread (web:1105201)
  never reaches a confirmed root cause — the MVP's leading hypothesis
  (multi-homing) was addressed but did not fix the symptom, and the thread ends
  with more diagnostics requested. Treat the DFSR-membership-disabled fix and
  the multi-homed-NIC anti-pattern as **things to rule out**, not a guaranteed
  resolution for every "SYSVOL missing after promotion" case (inferred).
- The claim that DFSR is fully decoupled from AD replication (web:1375980) and
  the claim that DFSR/SYSVOL replication *depends on* AD replication
  (web:1471057) are not actually contradictory once read carefully — AD
  replication converging does not itself resync SYSVOL *content*, but a broken
  AD replication channel does take DFSR down with it. Both threads agree DFSR
  has its own separate health path that must be checked independently of
  `repadmin` output (inferred).

## See also
- [[sysvol-folder-function]]
- [[ad-replication]]
- [[fsmo-roles]]
- [[ad-metadata-cleanup]]
- [[virtualized-domain-controllers]]
- [[group-policy]]
- [[active-directory-implementation-review]]
- [[dfs-replication]]
