---
title: "Exchange Hybrid (Exchange 2016 & Office 365) Three Services not started"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/121043/exchange-hybrid-exchange-2016-office-365-three-ser
question_id: 121043
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid (Exchange 2016 & Office 365) Three Services not started

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/121043/exchange-hybrid-exchange-2016-office-365-three-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi in our hybrid Exchange Environment, I just noticed there are three services Not Starting:   

Sync Host_3d6a513 service  

Download Map Manager  

MS exchange notification broker.   

Are they supposed to be stopped or started?   

Thanks  

ML

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-08*

They aren't needed for Exchange. They are typically set to Automatic but not running.  

You can ignore them.
