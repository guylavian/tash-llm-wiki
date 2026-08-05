---
title: "Exchange Database Size mismatch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1425055/exchange-database-size-mismatch
question_id: 1425055
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Database Size mismatch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1425055/exchange-database-size-mismatch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have been using Microsoft Exchange as our mail service since 2017. We have total 5 databases. The total storage of 5 databases is 4.13TB where 2 of my databases have more than 1TB. Rest of the databases are less than 1TB. We have around 3k mailboxes. Recently we found that, when we disabled our mailbox who left from our company, based on Microsoft article it will remove all content of that mailbox after 30 days which is by default settings. In our case we configured it for 14 days.

The total Database storage = 4.13TB

Total Item Size = 2.5TB

Total Deleted Item Size = 0.5TB

Total disabled mailbox size = 61GB

Now, My concern is where is my rest of 1.13TB space? And when we checked the whitespace of databases we found total 441GB is availablenewmailboxspace. Log size of every database is approximately 300-400MB. Now, please suggest me how can we find out our rest of the space usage? I have attached the screenshot which we found from mailbox server.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-11-14*

That command is not useful actually as it only looks at the root avail space:

https://blog.rmilne.ca/2013/08/20/how-to-check-database-white-space-in-exchange/

If you want to reduce the database size, I would move ALL the mailboxes to another database and then delete the source DB after that.
