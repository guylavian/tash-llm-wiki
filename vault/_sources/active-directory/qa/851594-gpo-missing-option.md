---
title: "GPO missing option"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/851594/gpo-missing-option
question_id: 851594
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO missing option

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/851594/gpo-missing-option (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We just switched to Cisco Umbrella DNS, since the switch our PCs have been showing a No Internet connection warning on the taskbar. Internet connection is fine and this is a known problem.  

After doing a search I found there is a fix for this, available in an ADMX download from 2017. I downloaded this, extracted all files and placed them in the Policy Definitions folder in SYSVOL.  

However, even after doing this, the setting I need, Computer Configuration > Administrative Templates > Network > Network Connectivity Status Indicator > Specify global DNS, is still not visible.  

I know this can be resolved using a registry change but my boss wants to use the GPO option so it's easier to manage.  

Does anybody have any idea why this is not visible or how I can get it to appear?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-18*

Hello  

Thank you for your question and reaching out. I can understand you are  having issues related  to GPO missing.  

-  As you have mentioned that  downloaded this, extracted all files and placed them in the Policy Definitions folder in SYSVOL. Can you please verify if you have configured the settings from Group Policy Management console after copying new ADMX files.  

-  Please also verify that AD replication \ SYSVOL replication is good in health and all are synced.  

-  On the Client computer run gpresult /h C:\temp\gpresul.html   to verify that GPO have been successfully applied.  

--If the reply is helpful, please Upvote and Accept as answer--
