---
title: "GPO not mapping printers at times"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/562144/gpo-not-mapping-printers-at-times
question_id: 562144
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
---
# GPO not mapping printers at times

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/562144/gpo-not-mapping-printers-at-times (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

Our clients run Windows 10 Enterprise, and the domain controllers are still Windows Server 2012 R2.  

Recently many users report that they don't see the printers when logging onto some PCs but they see them when logging onto other PCs.  

This happens both for users with roaming and local profiles.  

Printers are mapped for users via GPO, with option "Run in logged-on user's security context.." enabled.  

When users then try to map the printer manually, they are asked for administrator credentials for installing the driver, and of course at that point they call the helpdesk.  

I tried to run gpupdate/force but it didn't help.  

gpresult reports the gpo has been received.  

Once I install the device drivers on the client, the printers are mapped for the users.  

Can anybody help me sort this out?  

Thank you and best regards.  

Roberto

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-23*

Hello Roberto,  

This is due to recent updates to protect from the PrintNightmare exploit.  

Microsoft released an article regarding the printer and printer driver management post patching:  

https://support.microsoft.com/en-us/topic/kb5005652-manage-new-point-and-print-default-driver-installation-behavior-cve-2021-34481-873642bf-2634-49c5-a23b-6d8e9a302872  

Hope it helps,  

--If the reply is helpful, please Upvote and Accept as answer--
