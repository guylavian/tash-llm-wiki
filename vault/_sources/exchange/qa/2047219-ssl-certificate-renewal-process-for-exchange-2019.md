---
title: "SSL Certificate Renewal Process for Exchange 2019 Hybrid Environment with Edge Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2047219/ssl-certificate-renewal-process-for-exchange-2019
question_id: 2047219
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# SSL Certificate Renewal Process for Exchange 2019 Hybrid Environment with Edge Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2047219/ssl-certificate-renewal-process-for-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are managing an Exchange Hybrid environment with the following on-premises setup:

-  Two Exchange Mailbox Servers 2019

-  Two Edge Servers 2019

Recently, we renewed our third-party SSL certificates, which include SANs for mail.xyz.com and autodiscover.xyz.com. I imported the renewed certificate on all four servers, but encountered these warnings:

-  Edge Servers need to be resubscribed after the SSL certificate renewal.

-  The same SSL certificate should not be used on both Hub Transport Servers and Edge Servers.

I’ve reviewed various Microsoft resources, but I'm still seeking clear guidance on the best practices and specific requirements for SSL certificate renewal in an Exchange 2019 environment, particularly when Edge Servers are involved.

Could anyone provide detailed advice or clarify the correct process for:

-  Handling SSL certificates between Mailbox and Edge Servers

-  Resubscribing Edge Servers following certificate renewal

-  Best practices for SSL management in a hybrid setup

Any expert insights or pointers to relevant documentation would be highly valuable!

Thank you in advance for your support!

## Answers

_No answers on this thread._
