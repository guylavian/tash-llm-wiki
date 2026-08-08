---
title: "Exchange powershell cannot be connected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1361512/exchange-powershell-cannot-be-connected
question_id: 1361512
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange powershell cannot be connected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1361512/exchange-powershell-cannot-be-connected (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My Exchange server was once disjoined from the domain, and later I re-joined it to the domain. Now, I am unable to connect to Microsoft Exchange using PowerShell

the picture says ：connect to remote server failure

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-07*

Verify the Exchange Server is a member of the following security groups:

Exchange Trusted Subsystem

Exchange Servers

Exchange Install Domain Servers

Also make sure the "Exchange Trusted Subsystem" is a member of the local administrators group on the Exchange Server itself.
