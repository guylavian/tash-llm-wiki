---
title: "How to fix Exchange mailbox migration error: Corrupt property type in restriction."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1636248/how-to-fix-exchange-mailbox-migration-error-corrup
question_id: 1636248
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to fix Exchange mailbox migration error: Corrupt property type in restriction.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1636248/how-to-fix-exchange-mailbox-migration-error-corrup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Could you please provide assistance in resolving the error encountered during the Microsoft Exchange migration to O365 process? Thank you.

Migration rate:

Error: CorruptRestrictionPropertyTypeException: Corrupt property type in restriction. --> Corrupt PropertyTag found. --> Unable to create custom property with property key [{00020329-0000-0000-c000-000000000046}:'Keywords'] type [31].

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-04-02*

It seems that the problem has been corrected on the Microsoft side.

In my case, the problem was due to the usage of Dynamics 365 searchfolder properties.

These properties are now automatically ignored (excluded) from the migration.
