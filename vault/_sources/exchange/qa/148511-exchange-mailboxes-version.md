---
title: "Exchange mailboxes version"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/148511/exchange-mailboxes-version
question_id: 148511
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange mailboxes version

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/148511/exchange-mailboxes-version (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have Exchange 2013 Server, and ECP show mailboxes version 0.20 (15.0.0.0).  

Recently we install Exchange 2019 and migrate some mailboxes.  

But ECP still shows version 0.20 (15.0.0.0) for these mailboxes.  

Why?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-02*

AdminDisplayVersion is that value that matters, not ExchangeVersion    

ExchangeVersion is just the minimal version supported with the object, so you can ignore that    

Build Numbers:     

https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019
