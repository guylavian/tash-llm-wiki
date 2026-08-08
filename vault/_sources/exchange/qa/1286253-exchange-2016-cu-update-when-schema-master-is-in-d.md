---
title: "Exchange 2016 cu update when schema master is in different site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1286253/exchange-2016-cu-update-when-schema-master-is-in-d
question_id: 1286253
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 cu update when schema master is in different site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1286253/exchange-2016-cu-update-when-schema-master-is-in-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 cu update when schema master is in different site fails 

with various errors how to update Exchange Servers 2016 which are on other DR site

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-16*

You have to run the schema update in the same site as the schema master:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019
