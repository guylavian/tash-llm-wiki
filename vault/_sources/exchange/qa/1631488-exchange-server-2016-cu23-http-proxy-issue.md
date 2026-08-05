---
title: "Exchange server 2016 CU23 Http proxy issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1631488/exchange-server-2016-cu23-http-proxy-issue
question_id: 1631488
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server 2016 CU23 Http proxy issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1631488/exchange-server-2016-cu23-http-proxy-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have an error : Microsoft.Exchange.Data.Storage.UserHasNoMailBoxException. I get this error when i attempt to access from server 1 to user mailbox hosted on server 2.

It seems that http proxy doesn't work.

In my enviroment :

2 exchange server 2016 CU 23

5 exchange server 2010 sp3

How can I resolve this issue ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-26*

Hi @Hadjer Mansouri,

For Exchange 2010 to coexist with Exchange 2016, you need Update Rollup 11 for Exchange 2010 SP3 or later.

While since Exchange 2010 has reached its end of support on 2020/10/13, please consider migrating to Exchange 2016 to keep you in a supported situation.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
