---
title: "windows 10 20h2 printers via gpo are not deployed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/727170/windows-10-20h2-printers-via-gpo-are-not-deployed
question_id: 727170
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-print-jobs"]
---
# windows 10 20h2 printers via gpo are not deployed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/727170/windows-10-20h2-printers-via-gpo-are-not-deployed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have windows 10 20h2, our printers deployed by gpo, but we don't see any printers deployed by gpo.  

We have configured the directive computer->directives->administrative template->printers ->point and print in packet for exploited servers, with our servers.  

Also, extend the connection point aprint and look in windows update disabled,  

Restriction of point and print with our enabled servers and to install controllers for a new connection: show advertise and indication of elevation,   

to update controllers of a connection: show advertise and indication of elevation.  

we have our printers gpo under the correct uo but we don't see the printers deployed  

gporesult says that all directives are applyed

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-10*

both users are in the same organizational unit.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-10*

I have tried with another user who sees the printers deployed in the same windows 10 client that fails in the deployment and sees the printers, the issue is that I have a new user who does not see the printers by gpo deployed.
