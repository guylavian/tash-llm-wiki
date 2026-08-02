---
title: "FSMO role transfer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/785190/fsmo-role-transfer
question_id: 785190
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# FSMO role transfer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/785190/fsmo-role-transfer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My DC fails. Is there any time limit before I have to transfer fsmo roles from DC to ADC?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-24*

Hi

When a DC fails , you should fix it. If it’s impossible to fix the issue and restore it, you should perform a metadata cleanup and seize fsmo role to another Online DC if the failed one hosts some fsmo roles.  

So,You have to fix the Failed DC before tombstone time period. After this period, you have to demote it using metadata cleanup and seize fsmo tombstone time period role to another DC .

*Please don’t forget to mark helpful reply as answer *
