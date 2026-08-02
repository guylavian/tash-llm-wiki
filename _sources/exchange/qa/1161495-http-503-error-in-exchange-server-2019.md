---
title: "http 503 error in Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161495/http-503-error-in-exchange-server-2019
question_id: 1161495
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# http 503 error in Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161495/http-503-error-in-exchange-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange Server 2019 Version 15.2 ‎(Build 221.12)‎, Recently I installed another Exchange server 2019 Version 15.2 ‎(Build 1118.7)‎ in my environment. but I can't log in to ECP / OWA from the new Exchange Server.

## Answer (community) — community member

*upvotes: 2 · updated: 2023-01-18*

Hi @Md. Al Amin ,

You could check the following things:

1.check the certificates bindings of Default Web Site and Exchange Back End in IIS manager.

2.check if the MSExchangeECPapppool stops or recycle the MSExchangeECPapppool.

3.check if there is any error message in the application log.

Here is a similar case that you could refer to: "HTTP Error 503. The service is unavailable" then browsing to /ECP "exchange 2019"

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Have you read through the Exchange Server Troubleshooting documentation, specifically the Client Connectivity section, even more specifically the checklists and procedures in OWA or ECP stops working after you install a security update
