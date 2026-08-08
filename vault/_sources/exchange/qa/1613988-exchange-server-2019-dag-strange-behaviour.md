---
title: "Exchange server 2019 DAG strange behaviour"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1613988/exchange-server-2019-dag-strange-behaviour
question_id: 1613988
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange server 2019 DAG strange behaviour

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1613988/exchange-server-2019-dag-strange-behaviour (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I'm doing upgrade of Exchange 2013 hybrid servers (I know, should done that a while ago). So along side of 2013, I've setup two Exchange virtual 2019 CU all patched, polished and checked with health check. DAG is two node with FSW.

If I unplug the network of active server or stop the Information store service, the failover is executed immediately and databases are mounted on passive server.

But if I initiate a shutdown of active server, failover is not executed immediately but in exactly 3 minutes. The event ID 288 is also logged which states: "Added delayed failover entry for exch01.local.pri with 00:03:00 delay. Databases will remain mounted during the delay unless there are further error."

No other clear explanation is given with other entries regarding this. I've checked some things also removed databases and DAG, recreated all, but with same result.

Has anyone come across something like this or has any idea where to look for more info why this delay?  

Any help is appreciated.

Thank you.

## Answers

_No answers on this thread._
