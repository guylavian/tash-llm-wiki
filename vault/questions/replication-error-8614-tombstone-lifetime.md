---
title: Replication Error 8614 — Tombstone Lifetime Exceeded
type: question
domain: active-directory
slug: replication-error-8614-tombstone-lifetime
summary: Error 8614 ("The Active Directory cannot replicate with this partner because the time since the last replication with this partner has exceeded the tombstone lifetime") indicates a DC was offline past the forest tombstone lifetime (default 180 days), creating lingering objects; resolution requires identifying and removing lingering objects, then re-establishing replication.
sources:
  - kb:ad-ds-troubleshooting-active-directory-replication-problems
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/manage/troubleshoot/Troubleshooting-Active-Directory-Replication-Problems (Microsoft Learn — Troubleshooting AD Replication, fetched 2026-06-18)
  - web:https://support.microsoft.com/help/3108513 (How to troubleshoot common AD replication errors, fetched 2026-06-18)
provenance_extracted: 5
provenance_inferred: 2
provenance_ambiguous: 0
question_tier: support-kb
status: draft
updated: 2026-07-09
graph_community: "Active Directory Replication & Site Topology"
---

# Replication Error 8614 — Tombstone Lifetime Exceeded

> ⚠️ Out of corpus coverage — `active-directory` holds `conceptual` only; this is a `support-kb` question and that tier is not ingested; verify against the primary source.

**repadmin /showrepl shows "The Active Directory cannot replicate with this partner because the time since the last replication with this partner has exceeded the tombstone lifetime." This means the destination DC has not received inbound replication from the named source DC for longer than the forest's tombstone lifetime (default 180 days), and AD DS has garbage-collected tombstoned objects the source still holds — creating lingering objects.**

## Root cause

When a DC is offline or isolated from replication for longer than the tombstone lifetime (default 180 days, configurable via the `tombstone-lifetime` schema attribute), Microsoft's [Active Directory Replication Concepts](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc776877(v=ws.10)) explains that:

1. Objects deleted on the healthy side were tombstoned, replicated, and garbage-collected (permanently removed) from the NTDS.dit database on surviving DCs.
2. The offline DC never received those tombstone records. Its copy of the database still contains the now-garbage-collected objects as **lingering objects**.
3. AD's strict replication consistency mode (enabled by default since Windows Server 2008) refuses to replicate from a source that has lingering objects, because doing so would reintroduce "dead" objects into the directory (Event ID 2042).

This manifests as error **8614** in `repadmin /showrepl` output and **Event ID 2042** (`It has been too long since this machine replicated`) in the Directory Service event log (`ad-ds-troubleshooting-active-directory-replication-problems:159-176`).

## Resolution

### Step 1 — Identify the lingering-object source DC

Run `repadmin /showrepl` from each DC to see which source DC is failing. The error names the partner. Confirm with:

```
repadmin /showrepl <destination-DC> <source-DC>
```

Check the Directory Service event log for Event ID 2042 to confirm the tombstone-lifetime violation (`ad-ds-troubleshooting-active-directory-replication-problems:176`).

### Step 2 — Determine the tombstone lifetime

Query the current tombstone lifetime (in days) for the forest:

```
repadmin /showattr . cn=<forest-name>,cn=partition,cn=configuration,dc=<domain> /filter:"cn=*" /atts:tombstonelifetime
```

The default is 180 days (`ad-ds-restore-virtualized-domain-controller:21`).

### Step 3 — Remove lingering objects

Use `repadmin /removelingeringobjects` on each DC that has been offline past the tombstone lifetime. Run this against the affected naming context (directory partition) for every source DC that still holds the lingering objects:

```
repadmin /removelingeringobjects <destination-DC> <source-DC-guid> <NC> /advisory_mode
```

First run in `/advisory_mode` to see what would be removed, then repeat without it to execute. This removes the lingering objects from the local DC's directory store.

### Step 4 — Verify replication

After removing lingering objects from the affected DCs, force replication:

```
repadmin /syncall <DC-name> /AdeP
```

Verify with `repadmin /showrepl` — error 8614 should be gone and the "Last Success Time" column should show a recent timestamp.

### Step 5 — If cleanup alone does not resolve

If the DC has been offline so long that core objects (the server object, NTDS Settings object, or its own computer account) were tombstoned and garbage-collected, metadata cleanup + re-promotion may be the only fix (`ad-ds-troubleshooting-active-directory-replication-problems:66-73`):

1. Force remove AD DS from the affected DC (`ad-ds-troubleshooting-active-directory-replication-problems:93-97`).
2. Clean up the orphaned server metadata using **ntdsutil** or the AD management consoles (`ad-ds-troubleshooting-active-directory-replication-problems:72-73`).
3. Reinstall the OS or re-promote the DC fresh (`ad-ds-troubleshooting-active-directory-replication-problems:96-97`).

> **Important:** DO NOT skip the metadata cleanup step. AD re-animates deleted NTDS Settings objects for 14 days by default — if you do not remove metadata, the revived object triggers replication attempts that will fail persistently (`ad-ds-troubleshooting-active-directory-replication-problems:72`).

## Prevention

- Monitor replication health daily (`repadmin /showrepl * /csv` into Excel, sort by last success time) (`ad-ds-troubleshooting-active-directory-replication-problems:112-143`).
- Never pause or save-state a DC VM for longer than the tombstone lifetime (`ad-ds-virtualized-domain-controllers-hyper-v:254`).
- Never apply hypervisor snapshots to running DCs outside VM-GenerationID-aware tools — this creates the same lingering-object class (`ad-replication:59-60`).
- Back up DCs at least every 90 days (`ad-ds-restore-virtualized-domain-controller:21`).

## Contradictions / caveats

- The strict replication consistency that blocks replication on lingering-object detection is **enabled by default only on Windows Server 2008 and newer** (inferred — implicit from the configuration changes in 2008-era AD). On legacy Windows Server 2003 DCs, lingering objects could replicate silently — this is why the MS reference note still discusses "1388 NTDS Replication — strict replication consistency isn't in effect" as a root cause (`ad-ds-troubleshooting-active-directory-replication-problems:173`).

## See also
- [[ad-replication]]
- [[virtualized-domain-controllers]]
- [[active-directory-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-troubleshooting-active-directory-replication-problems|Troubleshooting Active Directory Replication Problems]]
<!-- crosslink:end -->
