---
title: "GPO setting vs SCCM patching requirement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/814721/gpo-setting-vs-sccm-patching-requirement
question_id: 814721
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO setting vs SCCM patching requirement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/814721/gpo-setting-vs-sccm-patching-requirement (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, In our test domain, one of the Domain GPO is having the setting for "Specify intranet Microsoft Update location -Enabled" which is causing SCCM patching fail because the location as per GPO is not valid. If the setting is changed to not configured via the same GPO, will SCCM team be able to set the local gpo setting per their requirement? ![193597-image.png][1] [1]: /api/attachments/193597-image.png?platform=QnA

## Answer (community) — community member

*upvotes: 2 · updated: 2022-04-18*

@SHANMUGAMSWAMINATHAN-5167   

Thanks for your posting on Q&A.  

Thanks very much for your feedback. We're glad that the question is solved now. Here's a short summary for the problem , this will help other users to search for useful information more quickly.  

Problem/Symptom:  

Set the Specify intranet Microsoft Update location Group Policy Not Configured  

Solution/Workaround:  

Setting an AD policy to "Not configured" and delete the associated registry key(s)  

Reference Link:  

https://superuser.com/questions/785214/how-to-return-a-gpo-to-not-configured  

Best regards,  

Rita  

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-04-16*

I got an answer from the link below  

https://superuser.com/questions/785214/how-to-return-a-gpo-to-not-configured

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-16*

Or can I get the setting from SCCM team and update the setting in the Domain GPO?
