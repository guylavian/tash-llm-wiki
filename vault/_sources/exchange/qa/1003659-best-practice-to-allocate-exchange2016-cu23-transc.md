---
title: "Best Practice to allocate Exchange2016(CU23)  Transcations Logs ->How much disk space is required"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003659/best-practice-to-allocate-exchange2016-cu23-transc
question_id: 1003659
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Best Practice to allocate Exchange2016(CU23)  Transcations Logs ->How much disk space is required

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003659/best-practice-to-allocate-exchange2016-cu23-transc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All    

My Current Infra    

1-Primary Domain Controller    

1-Secondary Domain Controller + File Server    

2-RODC    

-  UK-RODC    

2 Child Domain    

1 Exchange Server 2016 (CU23) Standard Version (Standalone Server)    

DB1 -600GB (Free 473)    

DB2 -600GB (Free 149)    

DB3 -600GB (Free 133)    

DB4 -600GB (Free 427)    

Logs-400GB (Exchange Transaction Logs) (Free 396)    

199179-hdd-dandr.png    

Now i have shortage of Infra storage .so planning to reduce Logs-400GB (Exchange Transaction Logs)    

I would like to know. what is the best practice for allocating separate partition (Exchange Transaction Logs)    

100GB is enough to maintain or need to be allocating more space? At present i have 400GB is allocated.    

even the Veeam backup exchange related configurations are enabled.    

Still is it good practice to reducing 400GB to 100GB for (Exchange Transaction Logs). in what cases Exchange Transaction Logs will be increased? will be occupied very fast?    

Please advise

## Answers

_No answers on this thread._
