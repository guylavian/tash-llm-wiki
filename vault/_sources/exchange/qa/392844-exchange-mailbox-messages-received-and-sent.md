---
title: "Exchange mailbox messages received and sent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/392844/exchange-mailbox-messages-received-and-sent
question_id: 392844
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange mailbox messages received and sent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/392844/exchange-mailbox-messages-received-and-sent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are considering moving from an on-prem Exchange 2016 server to Office 365, but we have several mailboxes with high message volume.  These mailboxes are used to receive a large amount of messages from our hosted CRM, and also relay messages from the CRM to external recipients.  We've had to modify the frontend receive connector on the server to allow for the message volume, but this is something we can't do in Office 365 - we're stuck with the 3600/hour receive and 30/minute send limits.  So I'm trying to determine a way to find out how many messages each of these mailboxes receive per hour, and how many they are sending per minute.  Is there a way in the web console or EMS to get this info?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-12*

Two ways:    

Look through the SMTP protocol logs and count connections:    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/configure-protocol-logging?view=exchserver-2019    

or    

PerfMon    

Transport SMTP Receive: Messages Received/sec
