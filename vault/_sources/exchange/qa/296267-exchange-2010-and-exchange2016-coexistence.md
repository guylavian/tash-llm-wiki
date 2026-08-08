---
title: "Exchange 2010 and Exchange2016 coexistence"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/296267/exchange-2010-and-exchange2016-coexistence
question_id: 296267
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2010 and Exchange2016 coexistence

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/296267/exchange-2010-and-exchange2016-coexistence (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI ， engineer  

During the coexistence of exchange 2010ru31 and exchange 2016 cu19, does exchange 2010 SP3 ru31 have to enable tls1.0-1.2?  

If TLS encryption is not enabled, will outlook client agent affect it? Will mail flow have an impact?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-04*

Hi, @超 邓      

Agree with Ashok, you may need to enable TLS on Exchange 2010.    

Otherwise, it would affect both client connection and mail flow between the servers.    

While if there aren't some clients which only support using TLS1.0 or TLS1.1 to connect, you only need to enable TLS1.2 and may disable TLS1.0 and TLS1.1 on the Exchange 2010 server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
