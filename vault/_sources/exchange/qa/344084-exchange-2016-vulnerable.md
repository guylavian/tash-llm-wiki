---
title: "exchange 2016 vulnerable"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/344084/exchange-2016-vulnerable
question_id: 344084
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange 2016 vulnerable

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/344084/exchange-2016-vulnerable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi     

after running below PS1 for exchange 2016 march 2021 security we get below result    

please give me hand to fix our issue     

*run MSERT and KB5000871 for all exchnage server but still our server are vulnerable    

84340-cassrv01-cve-2021-26855.txt

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-06*

we done all below steps  

-run KB5000871  

-run MSERT (every time we run this application we get different result)  

-run exchangemitigation.ps1  

-run Test-ProxyLogon  

the main post attachment show the result and i wanna know we are compromised ?  

if yes what should we do

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-05*

Follow:  

https://msrc-blog.microsoft.com/2021/03/16/guidance-for-responders-investigating-and-remediating-on-premises-exchange-server-vulnerabilities/
