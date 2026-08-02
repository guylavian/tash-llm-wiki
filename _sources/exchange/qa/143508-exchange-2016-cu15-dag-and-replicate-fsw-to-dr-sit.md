---
title: "Exchange 2016 CU15 DAG and replicate FSW to DR site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143508/exchange-2016-cu15-dag-and-replicate-fsw-to-dr-sit
question_id: 143508
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 CU15 DAG and replicate FSW to DR site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143508/exchange-2016-cu15-dag-and-replicate-fsw-to-dr-sit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Exchange 2016 DAG over 2 sites consisting of an Exchange server and FSW in the Prod site and a DR site containing one Exchange server.  

Can someone please tell me if we were to replicate the FSW server in near real-time to the DR site (RPO <30 seconds) and we lost our Prod site - could we bring the replica FSW online in DR (same name but different IP) and the DBs would mount on the DR Exchange server and be accessible?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Hi Kael, thanks for the reply.  We have set up DAC and the AFSW.  All good.
