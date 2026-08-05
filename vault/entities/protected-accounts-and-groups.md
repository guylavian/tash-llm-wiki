---
title: Protected Accounts and Groups (AdminSDHolder / SDProp)
type: entity
domain: active-directory
slug: protected-accounts-and-groups
summary: A built-in AD DS mechanism that periodically resets ACLs on privileged accounts and groups to match a template object (AdminSDHolder), preventing delegation, OU ACL inheritance, and unauthorized permission changes on the highest-privilege principals.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Appendix-C--Protected-Accounts-and-Groups-in-Active-Directory (Microsoft Learn — Appendix C: Protected Accounts and Groups in Active Directory, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Reducing-the-Active-Directory-Attack-Surface (Microsoft Learn — Reducing the Active Directory Attack Surface, fetched 2026-06-18)
  - kb:ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory
  - kb:ad-ds-reducing-the-active-directory-attack-surface
provenance_extracted: 16
provenance_inferred: 4
provenance_ambiguous: 0
symptoms:
  - "adminCount=1 orphan — OU delegation not applying"
  - "SDProp overwrites custom ACL on privileged group"
  - "account removed from DA still not inheriting OU permissions"
tags: [security, directory-services, concept]
status: draft
updated: 2026-07-02
graph_community: "Securing Active Directory (best practices)"
---

# Protected Accounts and Groups (AdminSDHolder / SDProp)

**AdminSDHolder is a template object in the System container whose ACL is enforced every 60 minutes by the SDProp process on all protected accounts and groups, ensuring their permissions cannot be altered by OU-level delegation.**

## Body

### The protected groups

The following security accounts and groups are protected in AD DS (list as of Windows Server 2008–2025):

- Account Operators, Administrator, Administrators
- Backup Operators
- Domain Admins, Domain Controllers
- Enterprise Admins, Enterprise Key Admins, Key Admins
- Krbtgt
- Print Operators
- Read-only Domain Controllers, Replicator
- Schema Admins, Server Operators

Any account with **direct or transitive membership** in any of these groups (including membership via nested distribution groups that are later converted to security groups) is flagged as a protected account — its `adminCount` attribute is set to 1.

### AdminSDHolder

Located at `CN=AdminSDHolder,CN=System,DC=<domain>`. This object holds the "template" ACL for all protected accounts and groups. The Domain Admins group owns the AdminSDHolder object by default (not the Administrators group). Enterprise Admins can modify any domain's AdminSDHolder.

Key property: **inheritance is disabled** on protected accounts and groups. Even if you move a protected account to an OU that has delegated permissions, the account does not inherit those permissions.

### SDProp (Security Descriptor Propagator)

SDProp runs every 60 minutes on the PDC Emulator. It compares the ACL on each protected account/group against the AdminSDHolder template and resets any divergence back to the template. To change permissions on protected accounts, you must change AdminSDHolder itself — not the individual account or group.

To force an immediate SDProp run (for testing), connect to the PDCE with Ldp.exe, bind, then modify rootDSE with attribute `RunProtectAdminGroupsTask = 1`.

To change the interval, set `HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters\AdminSDProtectFrequency` (range 60–7200 seconds). Reducing the interval increases LSASS overhead on the PDCE.

### The adminCount orphan trap

When an account is **removed** from all protected groups, SDProp stops managing its ACL — but the `adminCount` attribute remains set to 1 and inheritance stays disabled. The account continues to not inherit OU-level delegated permissions, which breaks tools and processes that rely on OU delegation. (inferred: this is the most common operational trap encountered when offboarding former admins — it must be corrected manually.)

Fix: run the script from Microsoft Support article 817433 to locate and reset formerly protected objects. Steps:
1. Clear `adminCount` to 0.
2. Re-enable permission inheritance on the object.

### Security implications

- An attacker who compromises AdminSDHolder permissions can permanently backdoor every privileged account in the domain — even newly added members of DA/EA will have their ACLs reset to the attacker's template (inferred).
- Modifications to AdminSDHolder (the dSHeuristics attribute) can remove specific groups from the protected set; this should be reviewed if found in assessments.
- AdminSDHolder ownership by DA (not BA) means a DA-only attack path to modify the template exists without BA involvement.

## Contradictions / caveats

- In Windows Server releases before 2008, owners of an object could grant themselves additional permissions; post-2008, the AdminSDHolder object's default protections are more robust.
- Nested distribution group members whose distribution group is later converted to a security group will retroactively receive the parent protected group's SID in their access tokens at next logon.
- The dSHeuristics attribute allows selective removal of groups from the protected set. This is occasionally needed for operational reasons but requires careful consideration.

## Reference notes
- [[ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory]]
- [[ad-ds-reducing-the-active-directory-attack-surface]]

## See also
- [[securing-active-directory]]
- [[tiered-administration-model]]
- [[credential-theft-and-attractive-accounts]]
- [[monitoring-ad-for-compromise]]
- [[security-groups]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory|Appendix C]]
- [[ad-ds-reducing-the-active-directory-attack-surface|Reducing the Active Directory Attack Surface]]
<!-- crosslink:end -->
