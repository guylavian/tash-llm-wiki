---
title: "2019 Exchange on-prem email classification Not showing in external mail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1135840/2019-exchange-on-prem-email-classification-not-sho
question_id: 1135840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-information-protection", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# 2019 Exchange on-prem email classification Not showing in external mail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1135840/2019-exchange-on-prem-email-classification-not-sho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have configured the email classification on 2019 on prem exchange server and have exported my xml file. It works fine internally. Please how do I get the classification to show on external mails that I send outside my organization. I would want the recipient to see the classification as well.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-20*

Sorry for the delay.    

That sounds expected. The classifications are using an ID that the external recipient client does not understand.    

Consider using IRM instead for external users:    

https://learn.microsoft.com/en-us/exchange/irm?WT.mc_id=M365-MVP-5000284

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-20*
