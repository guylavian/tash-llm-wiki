---
title: "Exchange 2019 - Periodic Email Delivery Issues in DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2247914/exchange-2019-periodic-email-delivery-issues-in-da
question_id: 2247914
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 - Periodic Email Delivery Issues in DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2247914/exchange-2019-periodic-email-delivery-issues-in-da (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What could be causing the periodic email delivery issues to internal mailboxes in a Database Availability Group (DAG) on Exchange 2019?

The situation involves two Exchange servers in the DAG where approximately once a month, there are problems with email delivery to mailboxes located on the neighboring DAG server. Each server has 50% of the databases running in active mode while the other half is in passive mode.

When a user on the EXCH1 server receives an email that arrives on the EXCH2 server, where the database is in passive mode, the email cannot be delivered to the user's mailbox. The Queue displays the following errors: 

-  `{LED=451 4.4.395 Target host responded with error. -> 421 4.3.2 Service not available}`

-  `{LED=451 4.4.395 Target host responded with error. -> 421 4.4.2 Connection dropped due to ConnectionReset}`.

This issue persists for about an hour, after which the emails are delivered without problems and the queues dissipate. Notably, rebooting the server prevents the problem for a month before it reappears.

Exchange version: 15.02.1544.014.

TLS 1.0 and TLS 1.1 is disabled, TLS 1.2 enabled.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-22*

Hi @Step to IT  ,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, these errors could be related to network issue between Exchange servers. Here are some suggestions for you

-  Please confirm that there are no network or port limitation between Exchange servers. It’s not supported to restrict or alter network traffic between internal Exchange servers.

You can check this article for more details:

Network ports for clients and mail flow in Exchange | Microsoft Learn 

-  If you have any third-party scan tool or antivirus software is installed on Exchange servers, please perform Exchange related folder, file and process exclusion according to the following document. This could avoid any file lock or service interference when Exchange function:

Running Windows antivirus software on Exchange servers | Microsoft Learn 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
