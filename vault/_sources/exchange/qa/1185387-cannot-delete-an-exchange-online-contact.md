---
title: "Cannot delete an Exchange Online contact"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185387/cannot-delete-an-exchange-online-contact
question_id: 1185387
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cannot delete an Exchange Online contact

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185387/cannot-delete-an-exchange-online-contact (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

we tried to delete a contact on our Exchange Online tenant but we have error message below :

Microsoft.Exchange.Configuration.DualWrite.LocStrings.UnableToWriteToAadException|An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online. However, it failed

This contact is not synchronized from our local AD or through Azure AD Connect

If I search this contact on MSOL, I cannot find it

I tried also to delete using Graph API but I have same error

How can I solve this issue ?

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-01*

Looks like it might have been orphaned, best open a support case.
