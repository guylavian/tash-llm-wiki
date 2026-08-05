---
title: "Exchange hybrid spam from office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1039040/exchange-hybrid-spam-from-office-365
question_id: 1039040
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange hybrid spam from office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1039040/exchange-hybrid-spam-from-office-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In an hybrid environment all the traffic from outside (Received traffic) go through an onprem antispam, after go to onprem exchange, than it routing to O365. In some cases some spam email goes through O365 and bypass the antispam. How can I avoid this spam email?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-10-07*

Bit difficult to say, given the scarse amount of information. First, it's not recommended to have e-mail hygiene components sitting between Exchange on-prem and EXO, but in front (if you must).    

Is the route Internet > Exchange on-prem > AS Component > EXO, and sometimes taking the Internet > Exchange on-prem > EXO route?
