---
title: "Exchange email storage alert to admin"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656660/exchange-email-storage-alert-to-admin
question_id: 1656660
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange email storage alert to admin

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656660/exchange-email-storage-alert-to-admin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

Is it possible to set up a policy or rule to notify admin that a particular email is nearly full ie 80%

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-16*

If your tenant has over 5000 licenses, you can address this via priority accounts monitoring, as detailed here: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-exchange-monitoring?view=o365-worldwide

Otherwise, schedule a script/workflow to periodically fetch mailbox usage data via PowerShell or the Graph API reports endpoint. There are plenty examples available online, look them up.
