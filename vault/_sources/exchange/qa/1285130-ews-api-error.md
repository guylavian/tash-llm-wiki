---
title: "EWS API Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1285130/ews-api-error
question_id: 1285130
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# EWS API Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1285130/ews-api-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I was using the EWS API to get exchange data, API frequently reported errors，like this:

 "One or more errors occurred. The request failed. An error occurred while sending the request"

above error is from a piece of C# code

<<

var service =  GetService(email); 

var g = service.ExpandGroup(group_email).Result;

it some times run ok ,but reported errors frequently

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-15*

Yutong,

Any news on this?  I'm still getting this same error on my .Net 6 EWS source code.
