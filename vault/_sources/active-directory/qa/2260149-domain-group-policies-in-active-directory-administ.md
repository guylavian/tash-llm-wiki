---
title: "Domain group policies in Active Directory Administrative Center?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2260149/domain-group-policies-in-active-directory-administ
question_id: 2260149
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Domain group policies in Active Directory Administrative Center?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2260149/domain-group-policies-in-active-directory-administ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can we manage AD group policy with Active Directory Administrative Center? If yes how?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-28*

Hi Younis,

   Based on your question of managing AD group policy with Active Directory Administrative Center (ADAC), I am afraid the answer is No. T Active Directory Administrative Center (ADAC) is primarily used for managing Active Directory objects like users, groups, and computers, and it doesn't directly allow you to manage Group Policy Objects (GPOs). To manage GPOs, you need to use the Group Policy Management Console (GPMC).

  Even though ADAC can be used to view resultant set of policies for a user, it cannot be used to create or edit GPOs. You can use ADAC to view the password settings that are applied to a user by navigating to the user, selecting "View Resultant Password Settings" in the Tasks pane.
