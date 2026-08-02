---
title: "exchange publishing using tls1.2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/156382/exchange-publishing-using-tls1-2
question_id: 156382
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange publishing using tls1.2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/156382/exchange-publishing-using-tls1-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,  

i have exchange servers 2016 published on cisco firewall.  

TLS 1.2 was enabled on the firewall and then all email traffic stopped working.  

how can i check TLS from server side and how can we make it use TLS 1.2 and disable the old one.  

Thanks,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-09*

Unless you messed with something, you are already using TLS 1.2 for SMTP traffic with Exchange 2016.    

You can verify this very easily in the message headers or SMTP protocol logs.    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761    

    

For other clients, follow the steps in those docs starting here:    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649    

NO need to change anything on the firewall in that regard.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-10*

Hi @eg1995  ,    

how can i check TLS from server side and how can we make it use TLS 1.2 and disable the old one.    

To validate whether TLS 1.2 is in use, agree with Andy that you can check the Message header or SMTP Logging. To analyze the message header, it's suggested to use the Message Header Analyzer at https://testconnectivity.microsoft.com. As regards to the protocol logging, you can enable the protocol logging on specific connectors and check if the following string exists:    

When the server is the SMTP receiving system:    

-  TLS protocol SP_PROT_TLS1_2_SERVER    

When the server is the SMTP sending system:    

-  TLS protocol SP_PROT-TLS1_2_CLIENT    

Regarding disabling the old one, please make sure you have completed the steps outlined in the two blogs shared above by Andy( Part 1: Getting Ready for TLS 1.2 and Part 2: Enabling TLS 1.2 and Identifying Clients Not Using It), then you can proceed to turn off TLS 1.0/1.1 by referring to Exchange Server TLS guidance Part 3: Turning Off TLS 1.0/1.1.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
