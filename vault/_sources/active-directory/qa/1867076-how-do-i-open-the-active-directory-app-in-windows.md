---
title: "How do I open the Active Directory app in Windows 11 Pro without the assistance of a domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1867076/how-do-i-open-the-active-directory-app-in-windows
question_id: 1867076
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How do I open the Active Directory app in Windows 11 Pro without the assistance of a domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1867076/how-do-i-open-the-active-directory-app-in-windows (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Day. My name is Alexander V and I have an issue In regards to the Active Directory apps (Administrator Tools) in Windows 11 Pro. Since acquiring this new computer (HP 17"by4xxxx) about a year ago. I have tried to add 6 new different domains to Windows 11 Pro and have failed to do so. I have in turn created more issues when installing the Active Directory using the Windows 11 Optional Feature(s). The Active Directory, Users and Computers, and DNS apps will not open based on "naming issues, or this computer is not joined to a domain." I have unsuccessfully tried to open these apps, however, I have failed to do so. My question is this: How do I open the aforementioned apps without joining my computer to a domain?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-04*

But this feature was available in windows 10 and could view all the domains.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-15*

Hello,

Thank you for posting in Q&A forum.

The Active Directory tools such as "Active Directory Users and Computers" are designed to manage Active Directory Domain Services. They require a connection to an Active Directory domain to function properly. Even after installing the RSAT tools, these tools are only useful if your computer is connected to an Active Directory domain, as they are designed to interact with AD DS. They will not manage local users/groups, etc.

In short, if you are not part of a domain, then the Active Directory tools are of little use to you. For local management, "Computer Management" or "Local Users and Groups" in Windows is more appropriate. To access it, do the following:

Press Win + X and select Computer Management.

Alternatively, you can press Win + R, type 'lusrmgr.msc', and press Enter to open Local Users and Groups directly.

If you need to create or manage Active Directory domains, you need to configure your Windows Server computer as a domain controller.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
