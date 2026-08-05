---
title: "Upgrade Active Directory Windows Server 2016 to Windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5921853/upgrade-active-directory-windows-server-2016-to-wi
question_id: 5921853
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Independent Advisor"]
---
# Upgrade Active Directory Windows Server 2016 to Windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5921853/upgrade-active-directory-windows-server-2016-to-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team!

We are planning to upgrade Active Directory Windows Server 2016 to 2022.

I am looking for more information and steps to perform this inplace upgrade.

I am looking for more details like detailed steps and dependencies like databases upgrade and others.

Please share those details

## Answer (community) — community member

*upvotes: 1 · updated: 2026-06-16*

For Active Directory domain controllers, the recommended method is not an in-place OS upgrade but adding new Windows Server 2022 DCs, moving roles, and then demoting the old 2016 DCs. This approach gives better AD performance and avoids in-place upgrade risks.

Below is an end-to-end outline based on the documented guidance.

1. Plan the upgrade method

-  Do not use in-place upgrade on AD DS servers. The guidance explicitly states:

-  "Don't use in-place upgrade for servers that run Active Directory Domain Services (AD DS)."

-  Instead, perform a clean OS install on new servers, promote them to DCs, and demote the older DCs.

-  If the server also hosts other workloads (for example, SQL Server or application databases), plan those upgrades separately. The AD guidance does not require or describe database upgrades on the DC itself; DCs should ideally not host application databases.

2. Prerequisites and checks

Before adding Windows Server 2022 DCs:

-  Verify hardware and OS requirements for the new Windows Server 2022 machines using the system requirements.

-  Verify application compatibility for anything that interacts with AD.

-  Verify security settings and connectivity to the target servers.

-  Confirm FSMO role availability and connectivity:

-  Use PowerShell on an existing DC:

```
Get-ADDomain | FL InfrastructureMaster, RIDMaster, PDCEmulator
     Get-ADForest | FL DomainNamingMaster, SchemaMaster
```

-  Ensure the server used to install the first 2022 DC can reach the schema master, infrastructure master, domain naming master, and RID master as required.

-  Confirm forest and domain functional levels meet prerequisites for newer DCs (for Windows Server 2016/2019/2022 DCs, forest functional level must be at least Windows Server 2012).

3. Add new Windows Server 2022 domain controllers

For each new Windows Server 2022 DC:

-  Join the new Windows Server 2022 machine to the existing domain and restart when prompted.

-  Sign in with a domain admin account.

-  In Server Manager, use Add Roles and Features to install Active Directory Domain Services on the new server.

-  When promoting a new DC, `adprep` (forestprep/domainprep) is run automatically as part of the wizard/PowerShell if needed.

-  In Server Manager, select the post-deployment notification (yellow triangle) and choose Promote the server to a domain controller.

-  In the AD DS Configuration Wizard:

-  Choose Add a domain controller to an existing domain.

-  Provide credentials if prompted.

-  On Domain Controller Options, set the DSRM password and continue through the wizard.

-  Complete the prerequisite check and select Install. The server will restart and become a DC.

Repeat for all planned Windows Server 2022 DCs.

4. Move FSMO roles to Windows Server 2022 DCs

After at least one Windows Server 2022 DC is online and healthy:

-  On an existing DC (or the new one), open Active Directory Module for Windows PowerShell.

-  Use `Move-ADDirectoryServerOperationMasterRole` to move FSMO roles to a chosen Windows Server 2022 DC, for example:

```
Move-ADDirectoryServerOperationMasterRole -Identity "DC-W2022" -OperationMasterRole 0,1,2,3,4
```

-  On the new Windows Server 2022 DC, verify FSMO roles:

```
Get-ADDomain | FL InfrastructureMaster, RIDMaster, PDCEmulator
   Get-ADForest | FL DomainNamingMaster, SchemaMaster
```

5. Demote and remove Windows Server 2016 DCs

Once Windows Server 2022 DCs are in place and FSMO roles are moved:

-  On each Windows Server 2016 DC, use Server Manager or `Uninstall-ADDSDomainController` (or the demotion wizard) to demote the DC.

-  Follow the documented demotion guidance (see "Demoting domain controllers and domains" in the referenced article).

-  After demotion, remove the old servers from the domain and decommission them.

6. Raise domain and forest functional levels (optional, after cleanup)

When all DCs are running supported newer versions (for example, only 2019/2022/2025 DCs remain) and prerequisites are met:

-  Raise the domain functional level to the desired level (for example, Windows Server 2016) using Active Directory Domains and Trusts or PowerShell.

-  Raise the forest functional level similarly.

Note:

-  In environments with Windows Server 2016, 2019, and 2022 DCs, the default domain and forest functional level is Windows Server 2016. It remains there until manually raised after upgrading to Windows Server 2025 or later.

7. In-place OS upgrade notes (if still considered)

If in-place upgrade is still being considered despite the recommendation:

-  Only 64-bit in-place upgrades are supported, and there are strict supported paths by version.

-  For AD DS specifically, the guidance is to avoid in-place upgrades and instead use the clean-install/promote/demote pattern described above.

8. Databases and other dependencies

From the provided guidance:

-  The AD DS upgrade path described focuses on domain controllers and AD itself. It does not require or describe upgrading application databases on DCs.

-  Best practice is to avoid running application databases (for example, SQL Server user databases) on DCs. If such workloads exist, plan their migration or upgrade separately, following their own product guidance.

References:

-  Upgrade domain controllers to a newer version of Windows Server

-  Perform an in-place upgrade of Windows Server

-  Plan your Windows Server upgrade

-  Identifying your functional level upgrade

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-16*

Dear Ravi Kiran Moole,

An in‑place upgrade of Active Directory from Windows Server 2016 to 2022 is supported, but it requires careful preparation. The upgrade process itself is straightforward: you run the Windows Server 2022 setup on the domain controller and choose “Upgrade” rather than a clean install. However, before doing this you must ensure the forest and domain functional levels are compatible, all FSMO roles are healthy, replication is error‑free, and critical services such as DNS are functioning correctly. Databases like NTDS.dit are upgraded automatically during the process, but you should run `dcdiag /v` and `repadmin /showrepl` to confirm there are no underlying issues.

It is best practice to take a full system state backup of the domain controller before the upgrade. If you have multiple domain controllers, upgrade one at a time and allow replication to stabilize before moving to the next. There are no separate database upgrade steps required beyond what setup performs, but you should verify that any third‑party agents or backup software are compatible with Server 2022. Microsoft’s official documentation emphasizes that in‑place upgrades are supported only from 2016 → 2019 → 2022, so if you are on 2016 you can upgrade directly to 2022.

If my answer is useful for you, please hit Accept the answer to support me.

Thank you, 

QQ.
