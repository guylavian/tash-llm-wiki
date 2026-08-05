---
title: "Exchange 2016 Send & Receive Connectors & limitations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143985/exchange-2016-send-receive-connectors-limitations
question_id: 143985
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Send & Receive Connectors & limitations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143985/exchange-2016-send-receive-connectors-limitations (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

We are documenting mail flow with our Exchange 2016 environment. There are a few clarifications we need with connector configurations

Receive Connectors:-  

-  Organization Max Receive message size is 37 MB  

a) Client Frontend MBS01 & Client Proxy MBS01 - 20 MB (IMAP & POP are not allowed)  

b) Default Frontend MBS01 Max Receive message size is 37 MB (Configured to receive mails only from SMTP gateway Ironport Appliances)  

c) Default RHOE16MBX01 Max Receive message size is 19 MB (even though this is configured as 19 MB we are receiving 37 MB mails from internet, how this works?)

Our actual requirement is to receive 37 MB mails, does the above configuration looks fine or do we have make changes with default connectors? How this affect internal users?

Send Connectors:-  

-  Organization Max Send message size is 28 MB  

a) Internet connector is configured with 20 MB (uses smart host)

Here our requirement is to allow 28 MB internally & externally. Do we need to change the internet connector?

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-18*

Thanks a lot Andy David, it's clear..

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-08*

Hello Andy  

We found that to receive 37 MB mails from outside, we have to make both MaxReceiveSize  & MaxSendSize as 37 MB (actually 37 MB + additional 33% ~49 MB). Why we should increase the global send size in receiving 37 MB? We are not getting the idea / config behind that
