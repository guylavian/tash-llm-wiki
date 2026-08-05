---
title: "How to shrink Exchange database in size after mailboxes removing?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1419096/how-to-shrink-exchange-database-in-size-after-mail
question_id: 1419096
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to shrink Exchange database in size after mailboxes removing?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1419096/how-to-shrink-exchange-database-in-size-after-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi! Have a question - we have Exchange 2019 CU12, so we decided to clean out the mailboxes of employees who left long ago; applied Remove-Mailbox, everything is fine. But the base never shrank. Is there a way to reduce the volume of the database after removing mailboxes? I figured this would happen automatically. Thanks for the help.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-08*

Hi @Evgeny Shupik,

These released space in this database are known as "whitespace" in Exchange.

If you create new mailboxes in this database, these new mailboxes will make use of these whitespace.

If you want to shrink the whitespace for disk space, the recommended method is to move all mailboxes from this database to another database, then remove this database. 

Below are some similar threads for your reference:

Exchange database edb size

Exchange database white space

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
