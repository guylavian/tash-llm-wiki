---
title: "Exchange 2019 certificate renewal-in hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166489/exchange-2019-certificate-renewal-in-hybrid-enviro
question_id: 1166489
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 certificate renewal-in hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166489/exchange-2019-certificate-renewal-in-hybrid-enviro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,

our SSL certificate will be expired in two weeks, so we renewed it and assigned exchange services as shown below, I have read on some articles that if both certificates old and new are matched then we don’t have to make any other changes on send and receive connector on premise side, please explain more about that part

Regards .

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-02*

You need to update the transport connectors even if the subject and issuer are the same in the new certificate

After that remove the old certificate

You can do so following:

https://www.alitajran.com/renew-certificate-exchange-hybrid/
