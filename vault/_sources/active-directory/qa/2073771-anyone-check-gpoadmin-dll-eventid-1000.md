---
title: "anyone check GPOAdmin.dll eventID 1000 ???"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2073771/anyone-check-gpoadmin-dll-eventid-1000
question_id: 2073771
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# anyone check GPOAdmin.dll eventID 1000 ???

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2073771/anyone-check-gpoadmin-dll-eventid-1000 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

anyone check GPOAdmin.dll eventID 1000 ???

my AD server able to check AD user&computers.

but when i start gpmc.msc i cant find my domain.

and check event viewer, i find GPOAdmin.dll eventID 1000.

anyone see same issue??

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-23*

Hello,

Event ID 1000 often refers to an application crash, and in the context of your question, it seems that the Group Policy Management Console (GPMC) is crashing due to an issue with the GPOAdmin.dll.

Make sure you have the latest updates and patches installed for Windows Server.

If other same system version machines don't have this issue, try to copy the GPOAdmin.dll. Try to manually register the GPOAdmin.dll using regsvr32.

Open a command prompt as an administrator and run regsvr32 GPOAdmin.dll.

Best Regards, 

Hania Lian

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
