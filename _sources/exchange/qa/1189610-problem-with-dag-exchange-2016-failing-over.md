---
title: "Problem with DAG exchange 2016 failing over"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189610/problem-with-dag-exchange-2016-failing-over
question_id: 1189610
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Problem with DAG exchange 2016 failing over

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189610/problem-with-dag-exchange-2016-failing-over (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, at site where we have 1 public domain name and we are using 1 public IP for exchange 2016. I have setup DAG having server1 be prim and server2 be standby. I have firewall nat'ing public ip to server1 and server2 which I believe might be wrong. So when we switchover manually the database to server2 everything works as should. But when we simulate a failover(rebooting) the server we cannot access email externally(when I mean this by hitting refresh on the mailbox it times out) or receive external emails into mailbox until server1 boots back up.  I'm wondering if there is anything else that needs set in exchange. I run Test-ReplicationHealth and they all pass. I didn't know if there is something to move the web services over that is needed? or anything like that?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-14*

Yea, the issue there is that if you arent using  a true load balancer, then clients can continue to use Server1 since the public IP is natted to it and the clients have no idea its down.

You will need to use a load balancer or round robin DNS or if you have a failover, remove Server1 from the natting logic

https://learn.microsoft.com/en-us/exchange/architecture/client-access/load-balancing?view=exchserver-2019
