---
title: "Disabling TLS 1.1 With Exchange server 2016 (CU17)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108840/disabling-tls-1-1-with-exchange-server-2016-cu17
question_id: 108840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Disabling TLS 1.1 With Exchange server 2016 (CU17)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108840/disabling-tls-1-1-with-exchange-server-2016-cu17 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We already disabled SSL 2.0, 3.0 & TLS 1.0 with Exchange servers. As a security best practice we are planning to disable TLS 1.1 and keep only 1.2 with all servers. Do we get any guidance in applying this change to all and how this is going to affect other application servers and end users (how can we plan it properly)?  

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

Hi @LMS   , the article provided by Andy above should be helpful to you.    

You could referring to below link as well, which also peovides detailed information:    

Windows Server: Disabling SSL 3.0, TLS 1.0, and TLS 1.1    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-27*

Hi @LMS       

All the guidance ( three parts) is here:    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649
