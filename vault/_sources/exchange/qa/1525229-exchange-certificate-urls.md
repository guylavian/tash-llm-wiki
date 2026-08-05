---
title: "Exchange certificate URL's"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1525229/exchange-certificate-urls
question_id: 1525229
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange certificate URL's

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1525229/exchange-certificate-urls (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019. SAN certificate from 3rd party CA.
Confirmation on required URL's.
URL's:
owa.contoso.com
autodiscover.contoso.com
Any other specific requirements for the SAN that is required for exchange online hybrid with my exchange 2019 server?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-02-05*

What namespace are you using for SMTP? 
You can use an existing one or add:
https://learn.microsoft.com/en-us/exchange/certificate-requirements
Edge servers are not required. so really could just use owa.contoso.com as the SMTP namespace as well and then set that on the send connector to from on-prem to Exchange Online
