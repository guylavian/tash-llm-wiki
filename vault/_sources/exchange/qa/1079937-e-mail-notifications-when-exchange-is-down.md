---
title: "E-mail notifications when exchange is down"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1079937/e-mail-notifications-when-exchange-is-down
question_id: 1079937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# E-mail notifications when exchange is down

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1079937/e-mail-notifications-when-exchange-is-down (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What happens to e-mail change in a power automate flow when Exchange is down?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-09*

Hi @Ahmet UÇAR   ,    

If you are using Exchange On-perm, then you need to connect to the exchange server, if exchange is down, power automate will also stop working.    

If you are using Exchange Online, usually Exchange will not go down, if the server goes down, then power automate will also stop working.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
