---
title: "Error applying GPO to restrict remote desktop for local Admins that are not domain accounts (SID S-1-5-114)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263545/error-applying-gpo-to-restrict-remote-desktop-for
question_id: 2263545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Error applying GPO to restrict remote desktop for local Admins that are not domain accounts (SID S-1-5-114)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263545/error-applying-gpo-to-restrict-remote-desktop-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error applying GPO to restrict remote desktop for local Admins that are not domain accounts (SID S-1-5-114)we get some errors after attempting to apply the GPO that resemble:

and 

\

i would understand the group s-1-5-114 to be non-domain local admin users..... however i cannot find some wayt o enumerate this groups members. if that is the case than from below i would expect the GPO to apply to the member below 'test'

H

however if i run the below nothing is returned.

i would expect the above to tell me who matches on that group., but maybe i am missing something.

Many thanks for your time.

Jamie

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-05-07*

Hello,

   Thank you for posting the question on Microsoft Windows forum!

   Based on your query of identify which members belonging to the well-known security group with SID s-1-5-114 which includes all local administrators

   To make sure that your local administrator account is assigned to this security group and NT AUTHORITY\Local account and member of Administrators group (SID S-1-5-114)), run the command:

-  whoami /all     You can check if these security groups exist on your Windows device by SID using the following PowerShell script:

-  $objSID = New-Object System.Security.Principal.SecurityIdentifier ("S-1-5-114")

-  $objAccount = $objSID.Translate([System.Security.Principal.NTAccount])

-  $objAccount.Value

-    If you want to restrict RDP connections for local users only (including local administrators), open the local GPO editor gpedit.msc (if you want to apply these settings on computers in the Active Directory domain, use the domain Group Policy Editor – gpmc.msc). Go to the GPO section User Rights Assignment and edit the Deny log on through Remote Desktop Services policy.   Add the built-in local security groups “Local account and member of Administrators group” and “Local account” to the policy. Update local Group Policy settings using the command: gpupdate /force.   

 Hope the above information is helpful!
