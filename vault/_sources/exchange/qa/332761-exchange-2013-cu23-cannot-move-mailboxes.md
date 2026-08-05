---
title: "Exchange 2013 CU23 Cannot Move Mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/332761/exchange-2013-cu23-cannot-move-mailboxes
question_id: 332761
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 CU23 Cannot Move Mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/332761/exchange-2013-cu23-cannot-move-mailboxes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am having a Database Content Index issue with Exchange Mailbox Server. When I tried to move some mailboxes from one database to another, it won't start and I get some message from Get-MoveRequestStatistics shown below:  

```
Resource reservation failed for 'DATABASE_NAME/MdbWrite' (CiAgeOfLastNotification(“DATABASE_NAME”)): load ratio 1.79769313486232E+308, load state 'Critical', metric 161625. This resource is currently unhealthy.
```

However, the ContentIndexStatus from Get-MailboxDatabaseCopyStatus is still in healthy state. Then, I found that the metric value in this message is the same as ContentIndexBacklog from Get-MailboxDatabaseCopyStatus. Most of my databases (70~80%) have a large value ContentIndexBacklog, when others remains 0.  

I have tried reseeding the database, but that didn't help. Does anybody has any thoughts/experiences about this situation?

## Answers

_No answers on this thread._
