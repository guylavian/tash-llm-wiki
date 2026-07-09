---
title: "Two DCs in different sites — split-brain replication delta + PAC signing errors: what happened and fix order"
type: question
question_tier: scenarios
domain: active-directory
slug: cross-site-split-brain-pac-signing
summary: After an inter-site network partition (split-brain), two AD Domain Controllers diverged. When the network recovered, the replication delta produces Kerberos PAC signing errors because the divergent directory state causes PAC validation failures. Fix replication first — the PAC errors are a downstream symptom of inconsistent group/key state.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts (Microsoft Learn — Active Directory Replication Concepts, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/Troubleshooting-Active-Directory-Replication-Problems (Microsoft Learn — Troubleshooting Active Directory Replication Problems, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide (Microsoft Learn — AD Forest Recovery Guide, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-the-krbtgt-password (Microsoft Learn — AD Forest Recovery: Reset the krbtgt password, fetched 2026-06-18)
  - note:_sources/active-directory/_raw/identity/ad-ds/plan/active-directory-domain-services-maximum-limits.md
  - kb:ad-ds-troubleshooting-active-directory-replication-problems
  - kb:ad-ds-active-directory-domain-services-maximum-limits
provenance_extracted: 8
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "Event ID 1988.*lingering object"
  - "Event ID 2095.*previously acknowledged USN"
  - "Event ID 2042.*tombstone lifetime"
  - "Kerberos.*PAC.*validation"
  - "Event ID 4768/4769 with failure code 0x1F or 0x12"
  - "repadmin /showrepl.*last attempt failed"
  - "KDC_ERR_PADATA_TYPE_NOSUPP"
status: draft
updated: 2026-07-02
---

# Two DCs in different sites — split-brain replication delta + PAC signing errors

> ⚠️ Out of corpus coverage — `active-directory` holds `conceptual` only; this is a `scenarios` question and that tier is not ingested; verify against the primary source.

**After an inter-site network partition, two AD Domain Controllers independently accepted writes, producing divergent directory state. When the link came back, the replication delta causes Kerberos PAC (Privilege Attribute Certificate) signing errors because the group membership and security-identifier state the PAC encodes has not yet converged. Fix replication first — the PAC errors resolve as a downstream consequence.**

## What happened

### Step 1: Network partition → split-brain

Two AD Domain Controllers in different sites (connected by a site link) lost connectivity due to a WAN/network failure. AD DS is **multi-master**: each DC processes writes (password changes, group membership updates, user creations) independently during the outage. This is by design — no single DC is the authoritative master for most directory partitions.

### Step 2: Divergent state (replication delta)

When the network was restored, the two DCs held a **replication delta** — a set of changes on each side that the other has never seen. AD uses USN-based replication to converge, but the divergence creates several possible failure modes:

| Symptom | Cause |
|---|---|
| Event ID 2095 (`previously acknowledged USN`) | USN rollback or USN conflict between the DCs |
| Event ID 1988 (`lingering object`) | An object exists on one DC but was deleted/tombstoned on the other, and the tombstone lifetime has elapsed on the partner that doesn't have it |
| Event ID 2042 (`tombstone lifetime exceeded`) | Replication has not occurred for longer than the tombstone lifetime (default 180 days); the link was down longer than that |
| `repadmin /showrepl` shows failures | Standard replication convergence error — the KCC builds connection objects but the USN high-water marks don't match |

(Source: [[ad-replication]], [[virtualized-domain-controllers]], [[ad-ds-troubleshooting-active-directory-replication-problems]])

### Step 3: PAC signing errors

The Privilege Attribute Certificate (PAC) is a data structure embedded in every Kerberos Ticket-Granting Ticket (TGT). It contains the user's security identifier (SID), group SIDs, and other authorization data, and is **signed by the issuing KDC** using the domain `krbtgt` account's key. (See [[krbtgt-reset]], [[ad-ds-maximum-limits]].)

When the directory state diverges between two DCs:

1. **A user authenticates against DC-A** → DC-A issues a TGT. The PAC inside it encodes the user's group memberships *as they exist on DC-A* (including groups that were added/modified on DC-A during the split-brain).

2. **The user then contacts a service that triggers a service-ticket request to DC-B** → DC-B receives the TGT and must validate the PAC signature and the group SIDs it contains.

3. **Validation failure** — DC-B sees group SIDs in the PAC that don't match what it has in its copy of the directory (because the group membership changes from side A haven't replicated yet, or a group was created on side A with a SID that conflicts on side B). The PAC **signature verification itself** will succeed (both DCs share the same `krbtgt` key *when replication is healthy*), but the **authorization data validation** fails — the Kerberos protocol manifests this as KDC_ERR_PADATA_TYPE_NOSUPP, Event ID 4768/4769 with failure codes, or generic "PAC validation" errors in application logs.

The errors are **not** about the cryptographic signature of the PAC being bad (unless `krbtgt` was reset on one DC during the split-brain — see caveats below). They are about the **authorization data inside the PAC being inconsistent** with what the verifying DC has in its directory.

## Fix order: replication FIRST, PAC signing resolves itself

The PAC signing errors are a **symptom** of the divergent directory state, not an independent failure. Therefore:

### ✅ Step 1: Fix replication convergence (the root cause)

1. **Assess the damage**
   ```cmd
   repadmin /showrepl * /csv > showrepl.csv
   repadmin /replsummary
   ```
   Identify which naming contexts failed, for how long, and whether the tombstone lifetime was exceeded.

2. **Check for USN rollback**
   - Look for Event ID 2095 in the Directory Service event log.
   - If found, isolate the affected DC and follow the USN rollback recovery in [[virtualized-domain-controllers]]: demote, metadata-cleanup on a healthy DC, re-promote.

3. **Remove lingering objects** (if Event ID 1988 or 2042 present)
   ```cmd
   repadmin /removelingeringobjects <Dest_DC> <NC> <Source_DC_GUID> /advisory_mode
   ```
   Run in advisory mode first, then without it. (Source: [[ad-ds-troubleshooting-active-directory-replication-problems]])

4. **Force replication convergence**
   ```cmd
   repadmin /syncall /AdeP <Dest_DC>
   ```
   This forces inbound replication from all partners. Wait for completion and re-check `repadmin /showrepl`.

5. **Verify time synchronization**
   Kerberos requires all DCs to be within 5 minutes of each other. Run `w32tm /monitor` across both DCs.

### ✅ Step 2: PAC signing errors clear automatically

Once the directory state is consistent between the two DCs:

- Group membership SIDs in newly issued TGTs match what both DCs have in their copy of the directory.
- The `krbtgt` key is identical across all DCs (it's directory-replicated data).
- Services and KDCs that validate PAC authorization data find consistent SID-to-object resolution.

No separate "fix PAC signing" step exists — fix replication, and the next authentication attempt that gets a fresh TGT from a converged DC will succeed.

### ❗ When you might need an extra step: `krbtgt` divergence

If during the split-brain, someone **reset the `krbtgt` password** on one DC but the change never replicated to the other before the network was restored, the two DCs will have different Kerberos signing keys. In that scenario, PAC **cryptographic** signature verification actually fails — a much more severe situation. The fix is still to converge replication (the `krbtgt` password change is a directory write and will replicate), but in-flight tickets issued after the reset may be permanently invalid. Users re-authenticate and get new TGTs once replication catches up.

## Contradictions / caveats

- **PAC error ≠ krbtgt mismatch.** Most PAC validation errors after a split-brain are about authorization-data inconsistency (group SIDs), not cryptographic signature failure. Check whether `krbtgt` was modified during the outage before assuming a key-divergence scenario.
- **Tombstone lifetime clock.** If the network was down for more than the tombstone lifetime (default 180 days), the DC that was isolated has **lingering objects** and cannot be safely re-introduced via normal replication. Forcefully demote it, clean metadata, and re-promote — see [[ad-forest-recovery]].
- **This is not a Keycloak/RHBK bug.** If your Keycloak/RHBK deployment authenticates users via Kerberos/SPNEGO against AD, you may see PAC validation errors *in Keycloak logs* as authentication failures. The root cause is the AD split-brain, not Keycloak. Fix AD first; Keycloak recovers without changes.
- **The `sessions` cache is not cross-site replicated.** In cross-site RHBK deployments with external Data Grid, only `actionTokens`, `authenticationSessions`, `loginFailures`, and `work` are SYNC-replicated — the `sessions` cache loads from the database (see [[active-passive-failover-sessions-lost]]). If you saw split-brain in that context, the correct recovery is [[site-synchronization]].

## See also

- [[ad-replication]]
- [[virtualized-domain-controllers]]
- [[ad-forest-recovery]]
- [[krbtgt-reset]]
- [[ad-metadata-cleanup]]
- [[vm-generation-id-safe-restore]]
- [[ad-ds-maximum-limits]]
- [[site-synchronization]] (for RHBK cross-site Data Grid split-brain, not AD DCs)
- [[active-passive-failover-sessions-lost]]

## References

### RH ground-truth (kb: / web: / note:)

- **web: Microsoft Learn — Active Directory Replication Concepts** — the multi-master model, USNs, InvocationID, site topology, KCC  
  <https://learn.microsoft.com/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts>
- **web: Microsoft Learn — Troubleshooting Active Directory Replication Problems** — common replication errors (Event IDs 1388, 1988, 2042, 2095), `repadmin` workflow, lingering-object removal  
  <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/troubleshoot/Troubleshooting-Active-Directory-Replication-Problems>
- **web: Microsoft Learn — AD Forest Recovery Guide** — the authoritative forest-recovery procedure when replication cannot be repaired  
  <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide>
- **web: Microsoft Learn — AD Forest Recovery: Reset the krbtgt password** — the double-reset procedure and why krbtgt is the Kerberos signing key  
  <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-reset-the-krbtgt-password>
- **note:_sources/active-directory/_raw/identity/ad-ds/plan/active-directory-domain-services-maximum-limits.md** — [MS-PAC] Privilege Attribute Certificate Data Structure reference
- **note:_sources/active-directory/fsmo-roles.md** — FSMO seizure after split-brain (never re-introduce a DC that was the role holder)

### Wiki

- [[ad-replication]] — AD multi-master replication, site topology, KCC, common failures
- [[virtualized-domain-controllers]] — USN rollback mechanism, safe-restore safeguards, VM-GenerationID
- [[ad-forest-recovery]] — last-resort forest-wide recovery (restore, krbtgt reset, metadata cleanup, re-promote)
- [[krbtgt-reset]] — the krbtgt account as the Kerberos signing key; two-reset procedure
- [[ad-metadata-cleanup]] — removing NC/Settings objects of dead DCs before re-promotion
- [[vm-generation-id-safe-restore]] — the VMGenID safeguard that prevents USN rollback on snapshot restore
- [[ad-ds-maximum-limits]] — 1,015-group access-token limit; PAC bloat from large group memberships (`MaxTokenSize`)
- [[site-synchronization]] — split-brain recovery for the *Keycloak cross-site Data Grid* scenario (a different topology — use this if the question is about RHBK cross-site Infinispan, not AD DCs)
- [[active-passive-failover-sessions-lost]] — why `sessions` is not cross-site replicated in the RHBK HA blueprint

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-troubleshooting-active-directory-replication-problems|Troubleshooting Active Directory Replication Problems]]
- [[ad-ds-active-directory-domain-services-maximum-limits|Active Directory Domain Services Maximum Limits and Scalability]]
<!-- crosslink:end -->
