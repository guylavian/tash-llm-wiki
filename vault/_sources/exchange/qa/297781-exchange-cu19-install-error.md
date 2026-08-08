---
title: "Exchange CU19 install error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297781/exchange-cu19-install-error
question_id: 297781
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange CU19 install error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297781/exchange-cu19-install-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to install CU19 on Exchange 2016 CU12. I got below error. I have restart the server twice but it still complains that it needs restart. Also the account I used to install the CU is domain administrator. It is a member of schema and enterprise group. Any help is appreciated.  1: /api/attachments/73948-download.jpg?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

If remove ECP virtual directory external URL and leave it empty, what kind of effect will it have? will it just prevent and internet connection to https://domain/ecp?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-06*

I moved schema master to the site and rest of issue is gone, except it keeps saying The computer needs to be restarted before Setup can continue [RebootPending]. What could be the problem?
