---
title: "Exchange ApplicationImpersonation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190286/exchange-applicationimpersonation
question_id: 1190286
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange ApplicationImpersonation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190286/exchange-applicationimpersonation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I found the Exchange Organization Management Group as Member of ApplicationImpersonation Role. Is that by default?

That means that every member of the organization management group has rights on every mailbox?

Regards  

Peter

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-16*

They should not be a member of that role, no.

What Org management has by default is the ability to delegate that role to other groups or users

https://learn.microsoft.com/en-us/exchange/applicationimpersonation-role-exchange-2013-help
