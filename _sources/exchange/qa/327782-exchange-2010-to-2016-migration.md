---
title: "Exchange 2010 to 2016 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327782/exchange-2010-to-2016-migration
question_id: 327782
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 to 2016 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327782/exchange-2010-to-2016-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello to all members as it is my first time here. I have an exchange 2010 sp3 installed on a VM with Windows 2008 R2 on it . I have to upgrade it to Exchange 2016 on another VM with Windows 2016 . As I am concerned for any possible interruption of users mail services , I would like to ask if there is an risk of stopping the mail services during the migration from Exchange 2010 to 2016 process. Thank you in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-23*

Hi,    

You can follow the migration steps as per the below,    

https://assistants.microsoft.com/    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-on-premises-best-practices-for-migrations-from-2010-to/ba-p/845660    

Possible minimal interruptions is only expected during DNS change from 2010 to 2016.    

Please also make a note of the outlook clients in the existing setup and if that’s supported with Exchange 2016    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#clients    

If the above suggestion helps, please click on “Accept Answer” and upvote it. Thanks for understanding.
