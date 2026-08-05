---
title: "Prevent user \"click-expansion\" of Exchange distribution group?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1570486/prevent-user-click-expansion-of-exchange-distribut
question_id: 1570486
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Prevent user "click-expansion" of Exchange distribution group?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1570486/prevent-user-click-expansion-of-exchange-distribut (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
I have been ask to create new DL with list of 100 users but the user shouldn't be allow to click-expansion to see who is in the DL.
I cant create Dynamic Distribution Groups as users are in different department/Job title.
Is they anyway I can stop user clicking on expansion  to see who is in the DL

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-22*

If in 365, create a 365 group
or create a DL with hidden membership on-prem or in 365:

https://office365itpros.com/2022/10/04/hidden-membership-groups/

on-prem?
See:
https://www.reddit.com/r/exchangeserver/comments/3g0ety/hiding_distribution_list_membership/
