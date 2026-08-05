---
title: "mail not relaying from exchange to external application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180037/mail-not-relaying-from-exchange-to-external-applic
question_id: 1180037
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# mail not relaying from exchange to external application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180037/mail-not-relaying-from-exchange-to-external-applic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,

we have to relay from application server to exchanger server and goes to third party sendinblue smtp and goes to external client.

right now the mail if only going from application to exchange server and to external client.

but same is not going through sendinblue application.

can you help on that.

thanks

sooraj

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-13*

Hello there,

Verify that your firewall or antivirus software is not blocking the outgoing mail server/SMTP relay. Try turning off your firewall or antivirus software and sending a message. If the message goes through, you need to adjust your firewall or antivirus software's settings.

In Exchange Server, you can create a dedicated Receive connector in the Front End Transport service on a Mailbox server that allows anonymous relay from a specific list of internal network hosts.

Allow anonymous relay on Exchange servers https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/allow-anonymous-relay?view=exchserver-2019

Relay from external application https://techcommunity.microsoft.com/t5/exchange/relay-from-external-application/m-p/3031500

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–
