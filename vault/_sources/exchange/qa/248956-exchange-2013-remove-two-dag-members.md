---
title: "Exchange 2013 Remove Two DAG Members"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/248956/exchange-2013-remove-two-dag-members
question_id: 248956
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 Remove Two DAG Members

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/248956/exchange-2013-remove-two-dag-members (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Exchange 2013 environment which consists of 4 mailbox\hub\cas servers with 4 mailbox database replicated across all 4 servers as members of the DAG plus a separate file witness server.  

Due to a data centre closure I need to remove two members from the DAG which should leave two mailbox\hub\cas servers & the one file witness server making three servers in the DAG so no split brain issue can occur.  

My question is do I remove the two members of the DAG each one at a time but very close together as I don't want to leave the DAG on an even number causing a split brain scenario?  

Is their a guide for removing two members of a five DAG cluster?  

Thanks in advance for any answers.

## Answers

_No answers on this thread._
