---
title: "Exchange database recovery: Why can third-party tools do more?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278576/exchange-database-recovery-why-can-third-party-too
question_id: 278576
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange database recovery: Why can third-party tools do more?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278576/exchange-database-recovery-why-can-third-party-too (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When facing a corrupted EDB file which is probably holding the last messages which have been received between the last backup and when disaster struck, you are going to look at your options on how you can get those missing mails out of there. The first thing to try will often be MS's own eseutil.exe which undoubtly can sometimes do a great job in recovering a database that has been shutdown dirty. Some other times, though it can't. Even a 'Hard Recovery' using the `/p` option would fail. It is that moment, at the latest, when you start considering third-party options like removed by moderator for example. So you download one of those and most certainly it can access the corrupted EDB file right away and instantly lists all the mailboxes and the messages they contain in a matter of a few seconds. "Huh...", you say and ask yourself why MS's own tools go for minutes or even hours only to report that they cannot do anything at the end while a third-party tool can seemingly access the file as if there was nothing wrong with it. Should it not be that the company that created the format should have the most knowledge about it und therefore being able to recover from corrupted data better than anyone else? Put another way: Why does MS not include a tool with abilities similar to the one described above in Exchange Server?

## Answers

_No answers on this thread._
