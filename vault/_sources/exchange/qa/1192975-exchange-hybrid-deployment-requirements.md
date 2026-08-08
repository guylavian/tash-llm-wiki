---
title: "Exchange Hybrid Deployment Requirements"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192975/exchange-hybrid-deployment-requirements
question_id: 1192975
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Hybrid Deployment Requirements

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192975/exchange-hybrid-deployment-requirements (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We will migrate our on-prem mailboxes to exchange online.  We are on Exchange 2013. We will have a 2019 hybrid server. Our Domain/Forest Functional Level is Windows Server 2012 R2.   Our Domain Controllers are 2012 R2. We will upgrade our DCs after the migration because of compatibility issues with Exchange 2013.

Do we meet the requirements for having a 2019 Exchange Hybrid Server given our Level and DCs? I did read Microsoft's documentation., I want to make sure I did not misunderstand anything.  Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-27*

Hi @mara2021 ,

Your environment meets the requirements for having a 2019 Exchange Hybrid Server, you could refer to:

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2019

For Best Practices for Migrating from Exchange Server 2013 to Exchange Server 2019, you could refer to this article:

https://techcommunity.microsoft.com/t5/exchange-team-blog/best-practices-for-migrating-from-exchange-server-2013-to/ba-p/3773084

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
