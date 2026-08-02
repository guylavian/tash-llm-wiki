---
title: "WSUS GPO setting conflict with SCCM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1498723/wsus-gpo-setting-conflict-with-sccm
question_id: 1498723
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
---
# WSUS GPO setting conflict with SCCM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1498723/wsus-gpo-setting-conflict-with-sccm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
When we migrate the software update from WSUS to MCM. Some GPO setting for WSUS will conflict with the SCCM. I tested “Specify intranet Microsoft update service location” setting will cause conflict error in WUAHandler.log. Any other GPO setting in windows update will conflict with SCCM?
According below documents, the Windows update (not WSUS) still work when using MCM deploy software update.
Manage settings for software updates - Configuration Manager | Microsoft Learn

I tested deploy a CU to client by SCCM, it can show the update. And the Microsoft update services location auto point to the SCCM server. But in Windows Update, it show up-to-date and no patch can be download or install. How to make it coexistence?

## Answers

_No answers on this thread._
