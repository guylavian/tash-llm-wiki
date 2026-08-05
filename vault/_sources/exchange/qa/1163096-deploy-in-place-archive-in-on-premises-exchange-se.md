---
title: "Deploy In-Place Archive in on-premises Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163096/deploy-in-place-archive-in-on-premises-exchange-se
question_id: 1163096
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Deploy In-Place Archive in on-premises Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163096/deploy-in-place-archive-in-on-premises-exchange-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to deploy In-Place Archiving solution for 500 users for on-premises Exchange Server. How will be the size of Archive Database?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-22*

Hi, it all depends on how much the quotas are you have set as well, messages per day, deleted item recovery  as well as other factors like backup, recovery etc...

I would download and fill out the Mailbox Calculator and input the number of users and run the numbers.

That will give you a starting point to determine how to size your storage:

[https://www.microsoft.com/en-us/download/details.aspx?id=102123

[https://techcommunity.microsoft.com/t5/exchange-team-blog/announcing-the-exchange-server-2019-sizing-calculator/ba-p/644180

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-22*

The size of the archive database for an In-Place Archiving solution for 500 users on an on-premises Exchange Server will depend on several factors, including the amount and size of email data that each user will be archiving.

As a rough estimate, you can expect the archive database to be approximately 2-3 times the size of the primary mailbox database. However, this is just an approximation and the actual size of the archive database may vary depending on your specific usage and retention policies.

It's recommended to use the Mailbox Size and Growth report in the Exchange admin center or PowerShell command (Get-MailboxStatistics) to get an idea of the current mailbox sizes and expected growth, this will help you to determine the size of the archive database.

It's also important to note that you should have enough storage capacity to accommodate the archive database and enough available resources (CPU, memory and IOPS) to support the additional load caused by archiving.

It's recommended to perform a pilot test before you deploy the In-Place Archiving solution to a large number of users, this will help you to identify any potential issues and fine-tune your archiving strategy.
