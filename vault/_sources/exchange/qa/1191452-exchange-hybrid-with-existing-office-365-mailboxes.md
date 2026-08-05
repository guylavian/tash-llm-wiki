---
title: "Exchange hybrid with existing Office 365 mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191452/exchange-hybrid-with-existing-office-365-mailboxes
question_id: 1191452
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange hybrid with existing Office 365 mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191452/exchange-hybrid-with-existing-office-365-mailboxes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

what is the procedure for creating hybrid with existing Office 365 mailboxes. For example, if we have O365 with N users with mailboxes and a new Exchange on-prem and we want to have hybrid.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-20*

Hi @Miroslav Kmet   ,

You have to start by installing and configure Azure AD Connect in order to synchronise User account from on-premise AD to Azure AD.

I invite you to read the following link to get more details about how create and configure hybrid envirement for Exchange : How To Set Up A Hybrid Exchange Office 365 Environment

Please don't forget to mark helpful answer as accepted
