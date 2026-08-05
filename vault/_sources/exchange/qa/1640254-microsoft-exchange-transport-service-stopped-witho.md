---
title: "Microsoft Exchange Transport service Stopped without any log !"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1640254/microsoft-exchange-transport-service-stopped-witho
question_id: 1640254
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Exchange Transport service Stopped without any log !

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1640254/microsoft-exchange-transport-service-stopped-witho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello 

i have a problem with exchange server 2019 . this server was good for 2 years . last week started problem with service exchange transport ! all of exchange service be running ! but this service started and stop quickly ! there isnt any event and log in event viewer

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-03*



## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-05*

Hello,

Transport service automatic stop may occur when the service area has a high number of CPU cores and a high transport load, you can refer to this article to deal with.

https://learn.microsoft.com/en-us/exchange/troubleshoot/mailflow/event-17018-msexchangetransport-service-stop

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-03*

Hi,

I am writing to clarify a point that I did not quite understand regarding “all of exchange service be running! but this service started and stop quickly”. Does this mean that the transport service keeps restarting? Also, is this problem with all exchange services, or just transport service? If you provide screenshots of the problem, it will significantly help us determine what is causing the problem.

Can you tell me if this problem is affecting our work in any way? For example, does it affect the normal delivery of emails, or accessing mailboxes?

Best,

Kelly
