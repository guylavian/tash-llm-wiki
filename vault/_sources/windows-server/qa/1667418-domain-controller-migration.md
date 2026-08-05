---
title: "domain controller migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1667418/domain-controller-migration
question_id: 1667418
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# domain controller migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1667418/domain-controller-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

what is the os upgrade workflow for windows 2003 to 2022?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-16*

Hello,

 

Thank you for posting in Q&A forum.

To migrate DC from 2003 to 2022, please kindly notice:

1.Before the migration please backup please kindly check if all software and application are available on windows server 2022 to aovid any compatibility issue.

2.Create a server snapshot or backup before the os upgrade.

3.Follow Microsoft Official Documentation to complete the server upgrade. You will need to upgrade to Windows Server 2008 or 2012 first.

REF: https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview

4.After the os upgrade please verify is all applications work fine or not.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-15*

If you're talking for a Domain Controller migration, it will be 2-steps migration because you cannot upgrade from 2003 to 2022 directly.

Here is how i would do it...

Let say you have only 1 DC...

First, run dcdiag on current DC to be sure that your AD is healthy / fix issues if having any

Deploy a new 2012 R2 server

Promote it as domain controller  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers-to-windows-server-2012-r2-and-windows-server-2012

Migrate FSMO rôles https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/view-transfer-fsmo-roles

Update the Time Server  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/configure-authoritative-time-server

Migrate other roles (DNS/DHCP)  

https://www.rebeladmin.com/2014/11/step-by-step-guide-to-migrate-dhcp-from-windows-server-2003-to-windows-server-2012-r2/

Demote 2003 domain controller

Upgrade domain / forest level to Windows 2012 R2  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels

Migrate FRS to DFSR (SYSVOL replication)  

https://techcommunity.microsoft.com/t5/storage-at-microsoft/streamlined-migration-of-frs-to-dfsr-sysvol/ba-p/425405

Implement AD Recycle Bin (Optional but recommended)  

https://petri.com/active-directory-recycle-bin/

Implement GPO Central Store (Optional)  

https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/create-and-manage-central-store

If you have a DFS Namespace (domain namespace) you can migrate to Windows 2008 mode  

https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/migrate-a-domain-based-namespace-to-windows-server-2008-mode

Deploy a new 2022 server

Promote it as domain controller

Migrate from 2012 to 2022 (FSMO / DHCP / DNS...)

Demote 2012 R2 DC  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/demoting-domain-controllers-and-domains--level-200-

Upgrade domain / forest level  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels
