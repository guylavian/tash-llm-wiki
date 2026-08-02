---
title: "Exchange Server 2019 dymantic Port"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180448/exchange-server-2019-dymantic-port
question_id: 1180448
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange Server 2019 dymantic Port

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180448/exchange-server-2019-dymantic-port (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

Could anyone help to advise on this, whereby mounting on exchange database is failed stated. 

EMS > Get-Mountdatabase status on remote exchange server will show up this message. 

Warning: Exchange can't connect to the information store service on remote server. Make sure that the service is running and that there is network connectivity to the server.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-17*

Hi @Russell Ang ,

Microsoft documentation indicates that the service is required to hang on to the database. Therefore, you need to make sure that the connectivity between servers is working. You could refer to: Mount-Database

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-15*

Hi @Russell Ang ,

According to the error report, you could check whether the information store service is enabled, you could try to restart the service and check whether the network connection is normal. 

Also, what are the CU and SU versions of your Exchange Server? If it is not the latest version, you could update it to the latest, which may also help you solve the problem.

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
