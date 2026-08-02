---
title: "Cannot Send Email From Exchange Online (365) To Exchange Server (On-Premise)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161451/cannot-send-email-from-exchange-online-365-to-exch
question_id: 1161451
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cannot Send Email From Exchange Online (365) To Exchange Server (On-Premise)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161451/cannot-send-email-from-exchange-online-365-to-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, does anyone has a solution for my issue in the hybrid exchange environment, I can't send email from 365 to Onprem user. This is the error in the message trace

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Have you enabled TLS 1.2 on your on-prem Exchange Servers?

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-18*

Hi @Ardan Zaki  ,

Typically, this error means Microsoft 365 connected to the destination email server, but the server responded with an immediate error, or doesn't meet the connection requirements. The error details will explain the problem. For example:

-  The destination email server responded with a "Service not available" error, which indicates the server is unable to maintain communication with Microsoft 365.

-  The connector is configured to require TLS, but the destination email server doesn't support TLS.

Please verify the TLS settings and certificates on your on-premises email servers, and the TLS settings on the connector.

In addition, please check is there anything between Exchange and O365, for example firewall,  antivirus software, or any other third-party software installed on Exchange that may interfere. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
