---
title: "Exchange 2019 installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193822/exchange-2019-installation
question_id: 1193822
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193822/exchange-2019-installation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I am as a Domain Admin have prepared the schema and AD etc for the Exchange server 2019.

Now exchange user wants to install exchange 2019 on the member server.

My question:

What role should I assigned to that user who wants to install Exchange server 2019?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-28*

Either Exchange Org Mgmt role or you can delegate to that user if you are an Exchange Admin:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/delegate-installations?view=exchserver-2019
