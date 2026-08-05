---
title: "Exchange Server Throttling"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261873/exchange-server-throttling
question_id: 2261873
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server Throttling

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261873/exchange-server-throttling (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

The theory:

The pratice:

Q1: Why do non of my users (that's the test network so it's ok to display usernames) have the default throttling policy  applied?

Q2: I added the folowing policy:

New-ThrottlingPolicy -Name OWAConcurrency -OwaMaxConcurrency 1 -ThrottlingPolicyScope Organization

Set-ThrottlingPolicyAssociation -Identity ******@contoso1.net -ThrottlingPolicy OWAConcurrency

Nevertheless the user michael.firsov can open more than 1 connection to the server ... ???

Exchange Server 2019 CU15

Thank you in advance,  

Michael

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-28*

Exchange Server throttling is a mechanism used to limit the number of requests a user or application can make to the server in a given time frame, preventing server overload and ensuring fair resource distribution among all users.
