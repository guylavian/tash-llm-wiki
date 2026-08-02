---
title: "DAG Member Recovery in Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195964/dag-member-recovery-in-exchange-server-2016
question_id: 1195964
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# DAG Member Recovery in Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195964/dag-member-recovery-in-exchange-server-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to recover Exchange Server2016  DAG member which has four members , one witness server and alternate witness server if one member server goes down and also witness server goes down

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-04-04*

The quorum would not go down in that case, as three of 4 members are still up.
If you were to lose a server in the DAG and wanted to recover it with Exchange setup, you can follow:
https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-dag-member-servers?view=exchserver-2019
