---
title: "Exchange Delegation Federation Cert Expaired"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1290927/exchange-delegation-federation-cert-expaired
question_id: 1290927
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Delegation Federation Cert Expaired

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1290927/exchange-delegation-federation-cert-expaired (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I keep seeing the error for "Exchange Delegation Federation" is expired.

It was expire back in Feb 2023

I try to delete it but I keep getting this error

We are using digicert which is for SMTP/IIS for our domain

"Exchange Delegation Federation" is self sign and Assigned to services SMTP, Federation

Do we need it and how do I renew it and remove the old one

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-24*

Yes, renew it  :)

You can follow these steps:

https://learn.microsoft.com/en-us/exchange/renew-the-federation-certificate-exchange-2013-help#replace-an-expired-federation-certificate
