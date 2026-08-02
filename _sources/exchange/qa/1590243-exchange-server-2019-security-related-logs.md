---
title: "Exchange Server 2019 Security related logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1590243/exchange-server-2019-security-related-logs
question_id: 1590243
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Server 2019 Security related logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1590243/exchange-server-2019-security-related-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
For monitoring purpose we required the location of Security related logs in Exchange 2019 Server. 
All logs location that related to security.
Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-27*

Hi System Admin - Exch

Can you share some more information on "security related logs"?

As to me, there aren't specific "security related logs" in Exchange.

For example, if you are looking for sign-in failure attempts, you can check Event Viewer>Windows logs>Security for event 4625, or check IIS logs for the sign-in request.

IIS log location: C:\inetpub\logs\LogFiles\W3SVC1

If you are looking for admin audit log or mailbox audit log, you can refer to below links:

How to use administrator audit logging in Exchange Server

Mailbox audit logging in Exchange Server

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
