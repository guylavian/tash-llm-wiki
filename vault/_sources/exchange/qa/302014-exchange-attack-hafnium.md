---
title: "Exchange attack Hafnium"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302014/exchange-attack-hafnium
question_id: 302014
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange attack Hafnium

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302014/exchange-attack-hafnium (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, please can anybody tell me by this log, if my 2 servers had been compromised please? Thank you.    

Server log    

CVE-2021-26855    

"2021-03-03T07:52:03.579Z","ServerInfo~a]@Testta  .domain.local:444/autodiscover/autodiscover.xml?#"    

"2021-03-04T23:03:44.923Z","ServerInfo~akak]@Testta  .domain.local:444/autodiscover/autodiscover.xml?#"    

"2021-03-05T05:37:27.400Z","ServerInfo~akak]@Testta  .domain.local:444/autodiscover/autodiscover.xml?#"    

"2021-03-05T16:44:51.174Z","ServerInfo~a]@Testta  .domain.local:444/autodiscover/autodiscover.xml?#"    

"2021-03-05T16:44:54.680Z","ServerInfo~a]@Testta  .domain.local:444/autodiscover/autodiscover.xml?#"    

"2021-03-05T16:45:32.913Z","ServerInfo~a]@Testta  /autodiscover/autodiscover.xml#"    

"2021-03-06T14:55:28.198Z","ServerInfo~burpcollaborator.net/ecp/default.flt?"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

You could run the script here and it will give you the result like following if it's not affected:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-06*

Probably. Consider opening a Microsoft support ticket or hiring a security consultant to investigate further:  

https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/  

Personally, I would take all the Exchange Servers offline and rebuild them from scratch.
