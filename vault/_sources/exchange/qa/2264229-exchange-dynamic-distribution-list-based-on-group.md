---
title: "Exchange Dynamic distribution list based on Group with Dynamic membership rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2264229/exchange-dynamic-distribution-list-based-on-group
question_id: 2264229
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Dynamic distribution list based on Group with Dynamic membership rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2264229/exchange-dynamic-distribution-list-based-on-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We're trying to create a distribution group in Exchange Online that will only include members of an (in Entra ID created) Dynamic User group with Dynamic membership rules. Is this possible, if so how?

The goal is to have an internal mailing list based on users/members based on specific queries as configured under Entra ID with Dynamic membership rules.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-08*

No, that's not possible. You might however be able to use a dynamic membership Microsoft 365 Group, which offers both the ability to configure membership based on Entra ID attributes and can handle mail flow. Have you considered this option?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-08*

Hi Michel G,

Thank you for posting your question in the Microsoft Q&A forum.

In general, not all Entra ID properties used in your dynamic membership rule could be used directly for Exchange Online dynamic distribution group. We can check this article, find corresponding and available Exchange online properties. Then set the similar RecipientFilter used for dynamic distribution groups:

Filterable properties for the RecipientFilter parameter | Microsoft Learn

For how to create a dynamic distribution group with PowerShell, please check:

Create and manage dynamic distribution groups in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
