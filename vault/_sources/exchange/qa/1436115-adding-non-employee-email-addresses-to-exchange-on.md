---
title: "Adding non-employee email addresses to Exchange Online Global Address List (GAL)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1436115/adding-non-employee-email-addresses-to-exchange-on
question_id: 1436115
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Adding non-employee email addresses to Exchange Online Global Address List (GAL)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1436115/adding-non-employee-email-addresses-to-exchange-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My management wants me to add non-employee email addresses, such as parent emails and frequent contact suppliers, to our Exchange Online Global Address List (GAL). 

What is the best practice for this and how can I ensure it is secure?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-11-23*

That's what Mail contacts are for: https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-contacts

Security-wise, there's nothing to be concerned about here, you are simply creating a "placeholder" for a given address. It's not an actual user, it cannot be used to access any resources or expose company data.
