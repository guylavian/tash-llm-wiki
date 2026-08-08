---
title: "Exchange Server Edgesync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/362902/exchange-server-edgesync
question_id: 362902
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server Edgesync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/362902/exchange-server-edgesync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 CU20 Mailbox Server and Edge Server - working and normal edgesync  

Exchange 2019 cu9 mailbox server will not connect via edgesync  

getting 10104 event id and 1024.  All certificates seem in date and fine.  

any help appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-28*

Edge server is Exchange 2016 CU20  

third party cert for mailbox only  

All Servers subscribed and 2016 has lease.  

I am going to try building edge as 2019 to see if that helps  

All Services are running  

Brian

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-20*

Hi @BRIAN N   ,    

As Andy said, you could provide more information so we could better help you out.    

I did a research about the Event 10104 and Event 1024, and they both point to the certificate.    

So please check/test the following:    

-  Is the Edge server also Exchange 2019 CU9?    

-  Are you using a third-party certificate for the mailbox server and edge server?    

-  Have you subscribed Edge to the mailbox server? Procedures for Edge Subscriptions    

-  Run Test-ServiceHealth to test if all services are running.    

Please also find the answer provided by Felix in this thread: EdgeSync Errors and see if it's helpful.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
