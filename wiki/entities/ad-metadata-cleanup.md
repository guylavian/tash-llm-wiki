---
title: AD Metadata Cleanup
type: entity
domain: active-directory
slug: ad-metadata-cleanup
summary: Metadata cleanup removes the directory objects that identify a domain controller to the replication system; during forest recovery you clean up every DC you are NOT restoring so the directory stops expecting them.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleaning-metadata-of-removed-dcs (Microsoft Learn — AD Forest Recovery: Cleaning metadata of removed writable domain controllers, fetched 2026-06-18)
provenance_extracted: 5
provenance_inferred: 2
provenance_ambiguous: 0
tags: [troubleshooting, replication, directory-services]
status: draft
updated: 2026-06-18
---

# AD Metadata Cleanup

**Metadata cleanup removes the Active Directory data (DC, server, and NTDS Settings objects) that identifies a domain controller to the replication system, so the directory no longer tries to replicate with a DC that's gone.**

## Body

In a normal demotion, metadata cleanup happens automatically as part of demoting a DC.
But when a DC is no longer reachable — it can't be demoted cleanly — you must clean its
metadata manually. In a [[ad-forest-recovery]] this applies to **every DC you are not
restoring**: clean up their metadata so the restored directory stops expecting the
non-restored (lingering) DCs, then add those servers back later by **reinstalling
AD DS** rather than reconnecting their stale state.

**Easiest path — Active Directory Users and Computers / Active Directory Administrative
Center (RSAT):** deleting the DC object performs metadata cleanup **automatically**, and
the associated **server object** and **computer object** are deleted along with it. When
prompted, select the *"This Domain Controller is permanently offline and can no longer
be demoted…"* checkbox so the tool does the full cleanup; confirm the global-catalog
prompt if the DC was a GC.

**Alternatives:**
- **AD Sites and Services (RSAT)** — you must manually delete the associated **server
  object** and **NTDS Settings object** before you can delete the DC object (it does not
  cascade the way ADUC does).
- **Command line** — `ntdsutil`, or PowerShell with the Active Directory module.

Cleaning metadata for the unrestored DCs is the prerequisite for safely seizing FSMO
roles onto the restored DC (inferred — the old role holders must be erased from the
directory before [[fsmo-roles]] are seized so they can never come back).

## Contradictions / caveats

- **ADUC/ADAC cascade vs. Sites-and-Services manual order.** With ADUC/ADAC the server
  and computer objects are removed automatically; with AD Sites and Services you must
  delete the server and NTDS Settings objects first, by hand.
- **Reinstall, don't reconnect.** Metadata cleanup is meant for DCs you'll add back by
  reinstalling AD DS; never reconnect the old, un-restored DC after recovery — its stale
  directory state causes lingering objects / split-brain (inferred from the forest-
  recovery rebuild model).

## Reference notes
- [[ad-ds-ad-forest-recovery-cleaning-metadata-of-removed-dcs]]

## See also
- [[ad-forest-recovery]]
- [[krbtgt-reset]]
- [[fsmo-roles]]
- [[ad-replication]]
