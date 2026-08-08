---
title: "Exchange transaction logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/307696/exchange-transaction-logs
question_id: 307696
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange transaction logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/307696/exchange-transaction-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! I have exchange server 2016. I have several databases which storage on other disk and transaction logs which storages on other disk too. Circular logging doesn't configured Untill i can't configure backup for exchange. How long will grow transaction logs? Exchnage will Delete transaction logs or they will grow untill will not run out disk space? Space for transaction logs one database 700GB

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Thank You All. I turned on circular logging

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-10*

It will keep growing till it runs out of space.  

Get an Exchange Aware FULL  backup ASAP to clear those logs or enable circular logging.   

Do this soon - before you run out of space and the server crashes.  

Do not remove the logs manually.
