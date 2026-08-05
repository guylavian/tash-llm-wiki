---
title: "Connect-ExchangeOnline suddenly stopped working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427165/connect-exchangeonline-suddenly-stopped-working
question_id: 1427165
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Connect-ExchangeOnline suddenly stopped working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427165/connect-exchangeonline-suddenly-stopped-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

we use hybrid workers in our environment and Connect-ExchangeOnline suddenly stopped working yesterday.

Runbooks fail when trying to connect to Exchange.

Error: Module could not be correctly formed. Please run Connect-ExchangeOnline again.

We use module ExchangeOnlineManagement version 3.4.0

Also tried connection directly from hybrid worker machine:

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-11-17*

We tried different scenarios...at the end this is workaround for us:

App registration with Exchange role, we will not use account. As described here https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps
