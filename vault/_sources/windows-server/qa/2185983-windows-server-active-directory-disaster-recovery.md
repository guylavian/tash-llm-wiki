---
title: "Windows Server Active Directory Disaster Recovery support without Windows Server Backups."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185983/windows-server-active-directory-disaster-recovery
question_id: 2185983
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Windows Server Active Directory Disaster Recovery support without Windows Server Backups.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185983/windows-server-active-directory-disaster-recovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to inquire what Microsoft's position is on supporting a business that hypothetically requires their direct help in resolving an issue with say a corrupt Active Directory domain or other issue. Does said company have to have full Windows Server Backups or can third party Active Directory and Server Backups suffice. My workplace is considering saving considerable resources by switching off Windows Server Backup for our Domain Controllers and relying on a solution offered by Cohesity to save our OS and Active Directory information/data. We currently run an Windows Server 2022 environment at Functional Level 2016 on Virtual Machines.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-09*

Hello Adam Trudeau,  

No problem.  

Have a nice day!  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-08*

Thank you for your reply.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-08*

Hello Adam Trudeau,  

Thank you for posting in Microsoft Community forum.  

For backing up AD Domain Controller, Microsoft recommendation is to use Windows built-in backup role to perform a full server back up or perform system state back up.  

AD Forest Recovery - Backing up a full server | Microsoft Learn

For any non-Windows tools or non-Microsoft tools, we may be not familiar with it, and the engineers or the venders of the specific third-part tools know more about their tools.   

The dedicated engineer about the tools will give you more professional and effective reply.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
