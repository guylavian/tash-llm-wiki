---
title: "windows 2012 R2 KB5008380  Kerberos-Key-Distribution-Center event 35 and  37"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/944328/windows-2012-r2-kb5008380-kerberos-key-distributio
question_id: 944328
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# windows 2012 R2 KB5008380  Kerberos-Key-Distribution-Center event 35 and  37

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/944328/windows-2012-r2-kb5008380-kerberos-key-distributio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've recently patched a windows 2012R2 DC, only one dc present on the domain. After reboot many of Kerberos-Key-Distribution-Center event 35 and  37 are logged related . I've read the article KB5008380 that explain that this event are addressed by the patch. But key pacrequestorenforcement is not present on registry. Looking for KB5008380 does not give results so is not clear to me if it  was intalled as part of an other update or is missing (but I don't uderstand why event 35 and 37 are generated)    

DO I need to manual install KB5008380? Or the registry was removed by a patch?    

Thank you for any suggestione

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-07-27*

Patch all the domain controllers as first step. Then each user will get the new improved authentication information PACs of Kerberos Ticket-Granting Tickets. (TGT) described in the KB    

Then it appears you may get one warning for every user.    

https://support.microsoft.com/en-us/topic/kb5008380-authentication-updates-cve-2021-42287-9dafac11-e0d0-4cb8-959a-143bd0201041    

Adds the new PAC to users who authenticated using an Active Directory domain controller that has the November 9, 2021 or later updates installed. When authenticating, if the user has the new PAC, the PAC is validated.    

the PacRequestorEnforcement registry value's only function is to allow you to transition to the Enforcement phase early. Otherwise not needed.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
