---
title: "Connect exchange online through grpah api"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1011475/connect-exchange-online-through-grpah-api
question_id: 1011475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connect exchange online through grpah api

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1011475/connect-exchange-online-through-grpah-api (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hii,    

What's  the command to connect exchange online through graph api? And what is the procedure?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-17*

There are no Graph API endpoints for Exchange Online. Some mailbox-level operations might be possible by other means, but overall you should be using Exchange Online PowerShell instead: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps
