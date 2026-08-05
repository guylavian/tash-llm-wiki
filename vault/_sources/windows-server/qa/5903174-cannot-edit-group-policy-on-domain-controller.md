---
title: "Cannot edit Group Policy on Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5903174/cannot-edit-group-policy-on-domain-controller
question_id: 5903174
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Cannot edit Group Policy on Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5903174/cannot-edit-group-policy-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,

We have two domain controllers, one can edit Group Policy through Group Policy Management but the other domain controller cannot. All of the ACLs look correct. Domain replication looks to be working correctly. Otherwise editing group policy works only on one server and not the other.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-05-27*

@Domic Vo  

That's great, good point and I appreciate the response. Here is some clarification. When we log into the domain controller, we go into "Group Policy Management", click to expand the domain, and then expand "Group Policy Objects", when we click on a group policy (not right clicking), we immediately get the error "Network access is denied".

When we right click and select "Change Domain Controller" and select another domain controller, we will then follow the steps above and get no error. This only occurs on one domain controller, and it is the domain controller we RDP into at the time. Any thoughts on this?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-05-27*

Hi FunMum,

The inability to edit Group Policy on a single domain controller typically indicates a localized file lock or sharing violation within that specific server's SYSVOL folder. Even if Active Directory replication is healthy, a security agent, backup routine, or hung session can hold an exclusive open handle on the Registry.pol file, blocking the Group Policy Management Console from committing changes.

To resolve this, open Computer Management on the affected server, navigate to System Tools, expand Shared Folders, and select Open Files to locate and manually close any active locks on the policy path. You should also check the DFS Replication log in Event Viewer for error codes like 4412 or 4502, which flag sharing violations. Releasing the file lock or restarting the DFS Replication service will restore editing functionality.

Domic V.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-05-27*

On the domain controller where Group Policy cannot be edited, use these checks and fixes:

-  Confirm which DC is being used by GPMC  

   On the working server, open Group Policy Management → right‑click the domain → Change Domain Controller and note which DC is selected. Ensure the problematic DC is fully replicated and then explicitly select it there. This guarantees that when editing GPOs, the same DC (or the intended one) is used and avoids conflicts in a multi‑DC environment.

-  Avoid editing GPOs on out‑of‑date DCs  

   Before editing GPOs on the problematic DC, verify that it has an up‑to‑date copy of the GPOs. If a GPO is edited on two DCs before replication completes, merge conflicts can corrupt the configuration. Only edit GPOs on a DC after replication has completed.

-  Check for SYSVOL/Registry.pol locking issues  

   If the error on the problematic DC mentions a file in use or similar when editing a GPO, the issue may be an exclusive lock on `Registry.pol` in SYSVOL. In that case:

-  Install the relevant hotfix on the domain controller that cannot edit GPOs (Windows Server 2008 R2 SP1 or Windows Server 2012 only).

-  Create the registry value on that DC:

-  `HKLM\Software\Policies\Microsoft\Windows\System`

-  `DWORD` name: `GroupPolicyForceCloseSysvolFileHandle`

-  Value: `1` (any non‑zero value enables it)

-  Restart the Group Policy service or the domain controller.

-  If the DC is not the PDC for certain GPO types  

   Some GPOs (for example, DirectAccess client and application server GPOs) are managed specifically by the PDC. Ensure that when editing those GPOs, the PDC is the DC used by GPMC or by any PowerShell cmdlets (for example, via the `-DomainController` parameter with `Open-NetGPO`).

If, after these steps, the DC still cannot edit GPOs while the other can, keep all GPO edits on the working DC (typically the PDC) until the problematic DC’s SYSVOL and AD replication and file locking issues are fully resolved.

References:

-  You cannot edit GPO and the Registry.pol file is not replicated when locked in Windows Server 2008 R2 or Windows Server 2012

-  Step 2 Plan the Multisite Infrastructure

-  Step 1 Plan the Advanced DirectAccess Infrastructure
