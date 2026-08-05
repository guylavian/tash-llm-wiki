---
title: "[Migrated from MSDN Exchange Dev] Clean Exchange Instalation on working domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145446/migrated-from-msdn-exchange-dev-clean-exchange-ins
question_id: 145446
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Clean Exchange Instalation on working domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145446/migrated-from-msdn-exchange-dev-clean-exchange-ins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have lost my exchange server and all my emails, but my domain server is still working. i want to reinstall the exchange server, the os has also been reinstalled but the instalation keeps failing with this erro  

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/e14df5ef-90a9-4a26-bd56-9a5f73372b42/clean-exchange-instalation-on-working-domain?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

If you want to recover old Exchange server, you need to follow this article to recover it on a new computer: Recover Exchange servers, before recovering Exchange server, you need to notice this requirement:    

    

If you want to install a new Exchange server, I would suggest you try install Exchange server on a new Windows server rather than a restored Windows server. Make sure all the prerequisites are installed correctly: Exchange Server prerequisites    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
