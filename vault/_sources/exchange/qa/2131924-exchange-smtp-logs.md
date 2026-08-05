---
title: "Exchange SMTP Logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2131924/exchange-smtp-logs
question_id: 2131924
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange SMTP Logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2131924/exchange-smtp-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, I am using an Exchange 2016 hybrid environment. One of my applications is using an internal relay (i.e., on-prem relay). The application is triggering emails, but users are not receiving them. The users are in exchange online. Which logs do I need to check to determine where the email has hit Exchange? I have the server IP where the application is hosted, as well as the sender ID and recipient ID. Please guide me

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-16*

Start with the message tracking logs in the on-prem Exchange Server

https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/search-message-tracking-logs?view=exchserver-2019

IF you dont see the messages being routed to Exchange Online there, then enable and check the SMTP protocol logs on the receive connector on the on-prem Exch Servers and see if the messages are being rejected there:

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/configure-protocol-logging?view=exchserver-2019
