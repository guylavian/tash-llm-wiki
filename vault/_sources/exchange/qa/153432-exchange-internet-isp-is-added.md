---
title: "Exchange internet ISP is added"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153432/exchange-internet-isp-is-added
question_id: 153432
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange internet ISP is added

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153432/exchange-internet-isp-is-added (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have two internet provider (Main link and backup link) when we switched for the second ISP internet provide we does not receive external email and i am listing down the dedicated environment  

Exchange 2016  

Mail Gateway  

Public DNS

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi @Bebo Edward   ,    

Did the problem occur after you changed your ISP?    

Did the external sender receive an NDR after sending it failed?    

First, please contact your ISP and check whether your DNS records are set correctly, including MX records and A records.Please make sure to point to the correct Exchange server.    

Check your firewall settings, whether the necessary ports are opened, and SMTP communication can pass smoothly.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
