---
title: "Exchange Power Shell command to add \"Reset Password Role\" to Organization Management role group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1474720/exchange-power-shell-command-to-add-reset-password
question_id: 1474720
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Power Shell command to add "Reset Password Role" to Organization Management role group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1474720/exchange-power-shell-command-to-add-reset-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Looking for Exchange PS command to  add "Reset Password Role" to "Organization Management role group". on Exchange 2019 Server

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-02*

Try the following cmdlet:

`New-ManagementRoleAssignment -Role "Reset Password" -SecurityGroup "Organization Management"`
