---
title: "Exchange 2016 Transport Service failed to start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1030251/exchange-2016-transport-service-failed-to-start
question_id: 1030251
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Transport Service failed to start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1030251/exchange-2016-transport-service-failed-to-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 server transport service failed to start. Exhausted with all the troubleshooting steps     

We have noticed that security event log was not accessible, so after we fixed the event log access issue by following the article below, transport server was started surprisingly     

Would like to understand relation between exchange transport service and security event log access, appreciate if anyone can share some input.     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/error-unable-access-security-log

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-03*

@Sridhar      

The security log records the Exchange and health mailbox activity. I guess the write limitation on system/health mailbox caused the Exchange Transport Service cannot be started.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-30*

Probably cant start the service if it cant write to the security event log.
