---
title: "How do i upgrade exchange dag to cu 23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193350/how-do-i-upgrade-exchange-dag-to-cu-23
question_id: 1193350
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How do i upgrade exchange dag to cu 23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193350/how-do-i-upgrade-exchange-dag-to-cu-23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How do i upgrade exchange 2016 DAG to cu 23

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-27*

Hi you can follow these steps:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/install-cumulative-updates?view=exchserver-2019

Since you are using a DAG, be sure to put the server you are upgrading in maint mode before applying:

https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/manage-dags?view=exchserver-2019#performing-maintenance-on-dag-members
