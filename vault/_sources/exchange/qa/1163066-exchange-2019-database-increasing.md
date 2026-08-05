---
title: "exchange 2019 database increasing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163066/exchange-2019-database-increasing
question_id: 1163066
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange 2019 database increasing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163066/exchange-2019-database-increasing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,

 

one of my DBs on exchange 2019 is increasing more than 300 MB per day although it has only 15 users, how can I trace which user is causing this problem by using Exmon tool or any different approach ?

 

Regards,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-22*

Hi,

You can use the following powershell command to get the size of each mailbox:

`Get-Mailbox -ResultSize Unlimited | foreach { Get-MailboxStatistics -identity $_.userprincipalName | select Displayname,TotalItemSize} `

Please don't forget to mark helpful answer as accepted
