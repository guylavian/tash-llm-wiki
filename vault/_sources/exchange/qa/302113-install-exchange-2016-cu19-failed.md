---
title: "Install exchange 2016 CU19 failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302113/install-exchange-2016-cu19-failed
question_id: 302113
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Install exchange 2016 CU19 failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302113/install-exchange-2016-cu19-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I got below message when installing exchange 2016 CU19 from CU15  

Couldn't remove product with code cd981244-e9b8-405a-9026-6aeb9dcef1f1. The installation source for this product is not available.   

how can it be fixed? Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Hi @alan gao   ,    

How are you running the setup - GUI or command prompt? Please share the error message from that setup to assist (cover your personal information while sharing). Also, you can share the logs from <system drive>:\ExchangeSetupLogs\ExchangeSetup.log     

This error looks like issue while installing windows pre-requisites. Please make sure to install all windows pre-requisites and restart the server before running the Exchange setup.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016#windows-server-2016-prerequisites-for-exchange-2016    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
