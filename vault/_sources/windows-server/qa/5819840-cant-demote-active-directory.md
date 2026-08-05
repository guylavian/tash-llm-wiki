---
title: "Can't demote Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5819840/cant-demote-active-directory
question_id: 5819840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Can't demote Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5819840/cant-demote-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have promoted Active Directory on the new server. Then I want to demote it on the old server because this server will be used for other purposes. However, when I try to demote it, I get this error:  

I checked in Group Policy (GPO) under Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment, and the Administrators group is already listed, and the account used is an administrator, which is a member of the Administrators group. Then I tried adding the administrator account, then gpupdate /force and restarted. However, the result was still the same:

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-13*

Dear Haza Hafiz Risk,

Thank you for sharing the details about the issue encountered when attempting to demote the old domain controller. The error message indicates that the account used does not have sufficient rights to configure the computer account on the remote domain controller. Even if the Administrators group is listed in the “Enable computer and user accounts to be trusted for delegation” policy, the account performing the demotion must explicitly hold this right and replicate permissions across the domain. It is recommended to verify that the account has Domain Admin privileges and that the Default Domain Controllers Policy has been applied successfully to the server. Running `gpresult /r` can confirm whether the policy is active. If the policy is applied and the error persists, checking replication health with `repadmin /replsummary` may reveal underlying issues preventing the demotion.

If this answer resolves your concern, please click Accept the answer so that confirmation is received.

Best regards, 

QQ.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-13*

The error occurs because Dcpromo cannot configure the computer account on another domain controller and returns “Access is denied.” This matches the scenario where demotion fails due to permission or dependency issues on the remote DC.

Use the following approach:

-  Verify and fix the underlying cause first

-  Ensure network connectivity, name resolution, authentication, and AD replication between this DC and the helper DC are healthy. Any failure in these dependencies can cause the demotion to fail.

-  After fixing the underlying issue, rerun the normal demotion (Server Manager → remove AD DS / Dcpromo) and confirm it completes successfully.

-  If normal demotion still fails, perform a forced demotion

-  On Windows Server 2003/2008-style demotion, run on the DC to be removed:

```
dcpromo /forceremoval
```

-  Follow the wizard, set a local Administrator password when prompted, and complete the process. This forcibly removes AD DS from the server even when it cannot contact other DCs.

-  On newer versions using PowerShell, the equivalent is:

```
Uninstall-ADDSDomainController -ForceRemoval -DemoteOperationMasterRole -Force
```

     (Add credentials if not logged on as Enterprise/Domain Admin.)

-  Clean up metadata after a forced demotion

-  On a surviving domain controller, perform metadata cleanup for the demoted DC so that all references to it are removed from the directory.

-  Ensure replication completes across all DCs and global catalog servers before promoting any new DC with the same name.

-  If the DC cannot start normally

-  As a last resort only, boot into Directory Services Restore Mode (DSRM) and use the documented registry method to remove AD from the server. This should be used only when the DC cannot start in normal mode.

After demotion, restart the server before removing the AD DS role binaries or reusing the machine for other purposes.

References:

-  Domain controllers do not demote gracefully when you use the Active Directory Installation Wizard to force demotion

-  Demote domain controllers and domains

-  DCPROMO fails with error "Access is denied" if the user does the promotion isn't granted the "trusted for delegation" user right
