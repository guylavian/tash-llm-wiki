---
title: "Exchange 2019 How to configure custom email content for mailbox quota warning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664903/exchange-2019-how-to-configure-custom-email-conten
question_id: 1664903
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 How to configure custom email content for mailbox quota warning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664903/exchange-2019-how-to-configure-custom-email-conten (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI How to configure custom email content for mailbox quota warning.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2024-05-10*

https://learn.microsoft.com/en-us/powershell/module/exchange/set-systemmessage?view=exchange-ps

Example:

Set-SystemMessage En\WarningMailbox -Text "Your mailbox has exceeded the warning limit specified by your email administrator. Please reduce the size of your mailbox."
