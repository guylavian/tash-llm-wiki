---
title: "Transport Rule."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1292206/transport-rule
question_id: 1292206
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transport Rule.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1292206/transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How i can get the traffic details of Transport rule in my office 365 tenant. i.e. I want to know how many emails are coming through different different transport rules. From where i can get this report.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-26*

Have you looked at the `Get-MailTrafficSummaryReport` cmdlet? 

`Get-MailTrafficSummaryReport -Category InboundTransportRuleHits | select * | ft`

`RunspaceId                           C1                                                               C2                  C3`

`----------                           --                                                               --                  --`

`80bc884f-84df-4c27-9d07-af14630228ba includes any of these recipients in the To or Cc box: 'Exchan... SetAuditSeverityLow 106`

`80bc884f-84df-4c27-9d07-af14630228ba Drop spam                                                        SetAuditSeverityLow 1`

Per-message details can be queried via the Get-MailDetailTransportRuleReport cmdlet.
