---
title: "Unable to add Exchange server to DAG."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1372750/unable-to-add-exchange-server-to-dag
question_id: 1372750
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to add Exchange server to DAG.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1372750/unable-to-add-exchange-server-to-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two Exchange servers and version Exchange Server 2019.  We installed Both exchange servers in different AD sites. we are facing an issue when we try to add second server into Exchange DAG. I am sharing the error message:

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-19*

In some cases, the cluster can be corrupted. You may try the following steps to see if it helps !

`Clear-ClusterNode -Name EX01 -Force`

Restart the EX01 server. Try adding the DAG member again.

`Add-DatabaseAvailabilityGroupServer -Identity DAG19 -MailboxServer EX01`

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
