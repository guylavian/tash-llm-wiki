---
title: "Account lockout  | source domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/681261/account-lockout-source-domain-controller
question_id: 681261
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Account lockout  | source domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/681261/account-lockout-source-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

my domain user id get locked frequently. The event id 4740 show caller pc as domain controller.  

end use do not aware of my domain controller details. They do not have access to store the credentials in domain controller.  

Let me know how come domain controller can be caller computer.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-13*

both PDC and DC1 shows the Caller Computer Name as a DC1. 

LoL

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-03*

Thank you for the response.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-03*

Some ideas here.  

https://community.spiceworks.com/topic/2256233-account-lock-out-shows-caller-computer-name-dc2  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
