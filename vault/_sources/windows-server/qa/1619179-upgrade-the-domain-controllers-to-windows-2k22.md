---
title: "Upgrade the Domain controllers to Windows 2k22."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1619179/upgrade-the-domain-controllers-to-windows-2k22
question_id: 1619179
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Upgrade the Domain controllers to Windows 2k22.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1619179/upgrade-the-domain-controllers-to-windows-2k22 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a project for a client to upgrade the Domain Controller OS to 2k22 (Current os is 2k12 R2).

my concern is, the client has couple of legacy os workstation (Windows XP and Windows 7), will this system be still be able to work with the Server OS upgrade.

Thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 2 · updated: 2024-03-18*

Hello 24777677,  

Thank you for posting in Q&A forum.  

will this system still be able to work with the Server OS upgrade.  

A: Yes.

If you want to upgrade the operating system of Domain Controller from 2012 R2 to 2022, the minimum requirement to add one a domain controller of one of Windows Server 2022 is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.

Functional levels determine the available Active Directory Domain Services (AD DS) domain or forest capabilities. They also determine which Windows Server operating systems you can run on domain controllers in the domain or forest. However, functional levels do not affect which operating systems you can run on workstations and member servers that are joined to the domain or forest.

Meanwhile, you can check if the apps or programs on legacy os workstation (Windows XP and Windows 7) can work fine after you upgrade the OS of domain controller (maybe also after the functional level upgrade).  

Reference:  

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-03-15*

Hi @24777677

yes they should be to contact domain control after the upgrade if you doesn’t disable RC4 for windows XP.

It’s time to upgrade all unsupported OS servers clients and domain controllers in order to secure your production environment 

Please don’t forget to accept helpful answer
