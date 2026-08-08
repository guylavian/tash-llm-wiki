---
title: "Sync M365 mailbox to on-prem Exchange mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1226596/sync-m365-mailbox-to-on-prem-exchange-mailbox
question_id: 1226596
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Sync M365 mailbox to on-prem Exchange mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1226596/sync-m365-mailbox-to-on-prem-exchange-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Background:  

We have our own AD DS and on-prem Exchange 2019 server. We sync users to M365 where each user has M365 Business Standard license or even M365 E3. Also configured SSO.  

Every users have Word, Excel, Outlook, Teams,... Users don't have email in M365, since we have on-prem Exchange.  

ˑ
Question:  

Is it possible to create/use M365 mailbox for a synced user with the same email address as on the on-prem Exchange?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-04-13*

If you are asking if you create a new mailbox for an existing user with a mailbox on-prem, that won't work.
