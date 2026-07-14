---
origin: eval-cohort
title: "Active Directory Forest Recovery Procedure"
type: question
domain: active-directory
slug: ad-forest-recovery-procedure
question: "What is the procedure for recovering an entire Active Directory forest after failure?"
summary: "Forest recovery is the last-resort procedure for when a forest-wide failure (corruption, ransomware, bad change replicated everywhere) renders all DCs unusable — you restore one DC per domain from a known-good backup, seize FSMO roles, reset secrets, clean up metadata, then rebuild the remaining DCs."
sources: "kb:ad-ds-ad-forest-recovery-guide,kb:ad-ds-ad-forest-recovery-perform-initial-recovery,kb:ad-ds-ad-forest-recovery-steps-for-restoring-the-forest,kb:ad-ds-ad-forest-recovery-seizing-operations-master-role,kb:ad-ds-ad-forest-recovery-reset-the-krbtgt-password,kb:ad-ds-ad-forest-recovery-cleaning-metadata-of-removed-dcs"
provenance_extracted: 8
provenance_inferred: 1
provenance_ambiguous: 0
question_tier: conceptual
status: draft
updated: "2026-07-12"
tags: "[troubleshooting, disaster-recovery, directory-services]"
---

# Active Directory Forest Recovery Procedure

**Forest recovery is the last resort when a disaster (corruption, ransomware, bad AD change) has replicated to every DC so no healthy DC remains to restore from within the running forest.**

## High-level phases

Microsoft documents five top-level phases (`ad-ds-ad-forest-recovery-steps-for-restoring-the-forest.md:30-45`):

1. **Identify the problem** — work with IT and Microsoft Support to determine scope and causes; total forest recovery should be the last option.
2. **Determine how to recover** — complete preliminary preparation steps.
3. **Perform initial recovery** — recover one DC per domain in isolation, clean it, reconnect domains, reset privileged accounts.
4. **Redeploy remaining DCs** — return the forest to its pre-failure state by installing/promoting new DCs.
5. **Cleanup** — reconfigure name resolution and get LOB applications working.

## Detailed initial recovery steps (per domain)

For each domain (starting with the forest root domain, then child domains) (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:36-39`):

### Restore the first writable DC
1. **Disconnect from the network** physically or by removing the virtual NIC (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:50-55`).
2. **Perform a non-authoritative restore of AD DS and an authoritative restore of SYSVOL** from a known-good backup using Windows Server Backup (recommended) or an AD-aware backup app (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:56-79`). *(extracted)*
3. **Verify data integrity** — if damaged, repeat with a different backup.
4. If the DC held a FSMO role, add `HKLM\System\CurrentControlSet\Services\NTDS\Parameters\Repl Perform Initial Synchronizations` = `REG_DWORD: 0` to avoid AD DS being unavailable until replication completes (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:83-101`). *(extracted)*

### Post-restore steps on the first DC (in order)
5. **Reset admin credentials** — reset passwords for all privileged accounts (Enterprise Admins, Domain Admins, Schema Admins, etc.) and the krbtgt account if the failure was a security breach (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:103-117`). *(extracted)*
6. **Seize all FSMO roles** using `ntdsutil` (`ad-ds-ad-forest-recovery-seizing-operations-master-role.md:17-69`):
   - `connect to server <FQDN>`
   - `seize schema master`, `seize naming master`, `seize rid master`, `seize pdc`, `seize infrastructure master`
   - EA credentials for forest-wide roles; DA for domain-wide roles.
7. **Clean up metadata** of all writable DCs being not restored — use ADUC/ADAC (auto-cascade deletes server + computer objects) or `ntdsutil` / PowerShell (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:133-155`). *(extracted)*
8. **Configure DNS** — install DNS Server role if not present; set preferred DNS to self IP in root domain or root DC in child domains; delete NS/SRV records of cleaned-up DCs (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:157-177`). *(extracted)*
9. **Raise available RID pool by 100,000** — prevents SID collisions between pre- and post-recovery objects (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:178-199`). *(extracted)*
10. **Invalidate the current RID pool** — unless a full system-state restore was performed (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:201-205`). *(extracted)*
11. **Reset the DC's computer account password twice** (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:210`). *(extracted)*
12. **Reset the krbtgt password twice** with a 10-hour interval between resets — flushes the two-password history so old Kerberos keys (including those used in Golden Tickets) are invalidated (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:211-212`, supported by [[krbtgt-reset]]). *(extracted)*
13. **Reset trust passwords** (if security breach) (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:214`).
14. **Remove the Global Catalog flag** on the restored DC if the forest has multiple domains — prevents lingering objects from GC partial replicas (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:216-249`). *(extracted)*
15. **Recreate gMSA accounts** if needed (Golden gMSA attack scenario) (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:252-255`).
16. **Configure Windows Time Service** — sync the PDC emulator to an external time source (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:257-259`).

### Reconnect and verify
17. **Reconnect restored DCs** from all domains to a common isolated network (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:261-269`).
18. **Verify forest replication health** — `repadmin /replsum`, `dcdiag /v`, create temporary connection objects if needed (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:271-286`). *(extracted)*
19. **Add Global Catalog** to a DC in the forest root domain — required for user logons and DNS registration by child domains (`ad-ds-ad-forest-recovery-perform-initial-recovery.md:288-314`). *(extracted)*
20. **Take a fresh backup** of each restored DC before proceeding.

### Redeploy remaining DCs
21. Install AD DS on new servers and promote them — **never reconnect old, un-restored DCs** — reintroducing stale directory state causes lingering objects and split-brain ([[ad-forest-recovery]] caveats, [[ad-metadata-cleanup]] caveats). *(inferred)*

## Contradictions / caveats

- **Never reconnect** an un-restored old DC after recovery — its stale directory state causes a split-brain / lingering-object mess. Rebuild by fresh promotion (`ad-ds-ad-forest-recovery-perform-initial-recovery.md` procedures, [[ad-forest-recovery]] caveats).
- **The krbtgt double-reset requires a 10-hour interval** between the two resets (the default maximum Kerberos ticket lifetime) — not back-to-back ([[krbtgt-reset]]).
- **ADUC/ADAC cascade vs. Sites-and-Services manual order** — ADUC deletes the server and computer objects automatically; AD Sites and Services requires manual order ([[ad-metadata-cleanup]]).
- **RODCs have separate krbtgt accounts** (`krbtgt_<number>`) — do not delete them during recovery ([[krbtgt-reset]]).
- **Multi-domain forests**: always recover the parent domain before any child domain to preserve trust hierarchy and DNS resolution.

## References

### RH ground-truth (kb:)
- `kb:ad-ds-ad-forest-recovery-guide` — Active Directory Forest Recovery Guide
- `kb:ad-ds-ad-forest-recovery-steps-for-restoring-the-forest` — AD Forest Recovery - Steps for Restoring the forest
- `kb:ad-ds-ad-forest-recovery-perform-initial-recovery` — AD Forest Recovery - Perform initial recovery
- `kb:ad-ds-ad-forest-recovery-seizing-operations-master-role` — AD Forest Recovery - Seizing an Operations Master Role
- `kb:ad-ds-ad-forest-recovery-cleaning-metadata-of-removed-dcs` — AD Forest Recovery - Cleaning metadata of removed DCs
- `kb:ad-ds-ad-forest-recovery-reset-the-krbtgt-password` — AD Forest Recovery - Reset the krbtgt password

### Wiki
- [[ad-forest-recovery]] — Active Directory Forest Recovery (synthesis)
- [[krbtgt-reset]] — krbtgt Password Reset (double-reset with 10-hour wait)
- [[ad-metadata-cleanup]] — AD Metadata Cleanup (ADUC cascade vs. manual Sites-and-Services)
- [[fsmo-roles]] — FSMO roles and seizure procedure
