---
title: "Exchange certificate status says “Invalid”"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1690305/exchange-certificate-status-says-invalid
question_id: 1690305
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 4
qa_tags: ["office-exchange-other-l1"]
---
# Exchange certificate status says “Invalid”

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1690305/exchange-certificate-status-says-invalid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I’ve got two exchange servers, certification is on Ex01-2019,  after export certification and import to Ex02-2019, its status says "invalid" but has an expiration date like the below image :

 

How can I resolve this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-02*

The problem was solved!

Ex02-2019 required the Internet to check Certificate Revocation List (CRL).
