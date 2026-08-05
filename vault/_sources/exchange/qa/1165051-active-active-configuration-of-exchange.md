---
title: "Active-Active configuration of Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165051/active-active-configuration-of-exchange
question_id: 1165051
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active-Active configuration of Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165051/active-active-configuration-of-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have two Data Centers A & B and exchange clusters are present in both of them. However, I got notified that Exchange server DB is mounted/active on only Data Center A.

We have SailPoint application configured with Exchange that creates mailbox for new joiners in the company.

Our Exchange administrator recently changed the priority of Exchange Databases from Data Center B to Data Center A. SailPoint servers did not have firewall rules for Data Center A. As a result, the mailbox creation for many users failed. I have following question:

Is there an active-active configuration that can be setup so that if SailPoint is unable to connect to Data Center A, (because of network issue) our Sailpoint application will establish connectivity with Data Center B ?

Please note that the exchange in Data Center will be up and running, can SailPoint still establish connectivity with Data Center B if it's unable to reach to Data Center A ?

Many thanks,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-28*

This isn't really about where the databases are active, Sailpoint wont care about that, it just needs the ability to connect to client endpoint  so the "active-active" piece doesnt apply.

What's needed is a single load balanced FQDN pool that all the server in both data centers are members of. You may already have that configured. 

Sailpoint then connects to the load balanced pool and it doesn't matter if one Data center is down, it can still connect to the remaining servers in the pool that are up.

https://learn.microsoft.com/en-us/exchange/architecture/client-access/load-balancing?view=exchserver-2019
