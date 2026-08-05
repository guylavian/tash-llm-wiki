---
title: "Steps to decomission onprem exchange after migrating all mailboxes to exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1648944/steps-to-decomission-onprem-exchange-after-migrati
question_id: 1648944
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Steps to decomission onprem exchange after migrating all mailboxes to exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1648944/steps-to-decomission-onprem-exchange-after-migrati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Currently exchange hybrid configuration, all mailboxes has been moved to exchange online.

Plan:

Change the mailflow to exchange online and remove hybrid configuration, decommission onprem-exchange server.

All new account will be created directly using office 365 here after.

Questions we have:

Do we need onprem exchange? There is Ad sync currently setup for directory synchronisation between onprem ad and office 365.

Can we edit user attributes, make changes using office 365 if we decommission onprem exchange server?

what does other organisations who want to move complete exchange online do in this case?

If we can decommission onprem exchange, kindly help with the steps need to follow.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-08*

Since all of the users will be managed in Microsoft 365 or Office 365, and there are no other directory synchronization requirements, you can safely disable directory synchronization and remove Exchange from the on-premises environment. You could refer to the following official documents for detailed steps:

How and when to decommission your on-premises Exchange servers in a hybrid deployment | Microsoft Learn

 Please note:

Scenario one
