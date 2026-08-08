---
title: "Delegate Exchange Content Search ability to specific users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2139860/delegate-exchange-content-search-ability-to-specif
question_id: 2139860
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-purview", "office-exchange-online"]
---
# Delegate Exchange Content Search ability to specific users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2139860/delegate-exchange-content-search-ability-to-specif (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Background

We have a group of users in our “Cyber IT Team” and would like to be able to delegate the ability for that team to carry out Content Searches in our Exchange Online mailboxes. The results of these searches can then subsequently be used by the Exchange team (which is a separate team) to purge related data from Exchange mailboxes.

Requirements

-  Delegate the ability for our “Cyber IT Team” to carry out Content Searches of Exchange Online mailboxes.

-  The “Cyber IT Team” should only be able to see Content Searches that they own.

-  Results of these searches can subsequently be used by the Exchange Team to purge Exchange data related to those searches. Today the Exchange Team uses the New-ComplianceSearchAction cmdlet. For example, the cmdlet below would purge items which are part of the “Cyber-IT-Team-12-12-2024” Content Search:

 New-ComplianceSearchAction -SearchName "Cyber-IT-Team-12-12-2024" -Purge -PurgeType HardDelete 

Thanks!

## Answers

_No answers on this thread._
