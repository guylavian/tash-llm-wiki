---
title: "Outlook web icon changed after CU update ( Exchange server 2016 CU 22)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1104158/outlook-web-icon-changed-after-cu-update-exchange
question_id: 1104158
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Outlook web icon changed after CU update ( Exchange server 2016 CU 22)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1104158/outlook-web-icon-changed-after-cu-update-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are facing an outlook web icon-related issue from the External network after upgrading CU 22 for Exchange server 2016. Screenshots is given below-    

From the internal network is working fine.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-28*

Hi @MdMahfuzurRahman-9219   ,    

Microsoft recommends that you always keep the latest versions of CU and SU, and you ccould upgrade to the latest version of the current:    

https://www.microsoft.com/en-us/download/details.aspx?id=104132    

https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-november-8-2022-kb5019758-2b3b039b-68b9-4f35-9064-6b286f495b1d    

Do you have a firewall device enabled? Your internal work is fine and problems with your external environment may be due to firewall device blocking. Maybe the connectivity test of Microsoft Remote Connectivity Analyzer could help you troubleshoot.    

If the above response does not help you, please confirm the following information:    

-  Does changing browsers cause the same problem (you could also try clearing your browser cache)    

-  Do other users have the same problem    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
