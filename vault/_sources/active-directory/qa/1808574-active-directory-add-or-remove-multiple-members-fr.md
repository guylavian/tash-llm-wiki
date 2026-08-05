---
title: "Active Directory - Add or remove multiple members from a security Group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1808574/active-directory-add-or-remove-multiple-members-fr
question_id: 1808574
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory - Add or remove multiple members from a security Group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1808574/active-directory-add-or-remove-multiple-members-fr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What's the maximum limit to add/remove users to a security group in On-Prem AD? Also, is there a limit to the sync process between On-Prem & AZURE Sync for such additions? 

e.g. can I add 100K users to an AD Group using PowerShell script in a single run?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-11*

In theory yes, however note some caveats:

https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits
