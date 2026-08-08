---
title: "Azure Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1616475/azure-active-directory
question_id: 1616475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Azure Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1616475/azure-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error executing request. An Azure Active Directory call was made to keep object in sync between Azure Active Directory and Exchange Online. However, it failed. Detailed error message: Unable to update the specified properties for on-premises mastered Directory Sync objects or objects currently undergoing migration. DualWrite (Graph) RequestId: b9e0b11e-beea-4c29-be1c-156be7d5d18e The issue may be transient and please retry a couple of minutes later. If issue persists, please see exception members for more information.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-14*

Do you have a hybrid deployment and use AAD Connect?

How did you get this issue?

Based on my experience, this issue may occur that you try to make the changes for the synced mailboxes in Exchange Online admin center directly. If your organization uses a hybrid environment and those mailboxes are synced from AD, you have to manage them from on-premises Exchange.
