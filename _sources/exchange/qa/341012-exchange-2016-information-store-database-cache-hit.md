---
title: "Exchange 2016 - Information Store - Database Cache Hit %"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341012/exchange-2016-information-store-database-cache-hit
question_id: 341012
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 - Information Store - Database Cache Hit %

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341012/exchange-2016-information-store-database-cache-hit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

We are facing this alert about InformationStore (Exchange 2016) thats under 90% in 10 minutes.    

The counter Database Cache Hit % is flapping basically all the time between 0 and 100%.    

This server supports only one Database, has 16GB's of Memory and all the process together are consuming 90%.    

The process Worker is consuming about 1GB.    

Is this all right? Someone can tell me how can I fix or avoid this alert?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-02*

Hi, @Victor Florêncio       

The alert indicates that Database Cache Percent Hit should be over 90%.    

Please refer to this document: Mailbox Server Counters    

It is about Exchange 2010 while also applies to Exchange 2016.    

    

I suppose that the problem may be related to memory problems.    

Can you find some related warning or error events in the event viewer>application log?    

In addition, it is recommended to use the Exchange 2016 Server Role Requirements Calculator to calculate the required RAM and other hardware requirements for your Exchange server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
