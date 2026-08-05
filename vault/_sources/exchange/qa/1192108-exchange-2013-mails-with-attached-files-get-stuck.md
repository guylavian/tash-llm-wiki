---
title: "Exchange 2013: Mails with attached files get stuck in queue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192108/exchange-2013-mails-with-attached-files-get-stuck
question_id: 1192108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013: Mails with attached files get stuck in queue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192108/exchange-2013-mails-with-attached-files-get-stuck (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Good morning! I have a problem with outgoing emails. Indeed, all emails sent to the outside which have attached files remain blocked in the queue. The send connector is well configured and the maximum size of messages sent is 100 MB. The Exchange server for mails sent to the outside is connected to a Cisco ESA (Email Security Appliance) which is responsible for transmitting mails to outside (the ESA serves as a relay for outgoing emails).
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-23*

Hi @Harvey NGOUAMA ,

-  Please check the QueueViewer in Exchange Tool first to see the last error encountered in the email message.

-  Do emails with attachments send properly to internal mailboxes? If only emails to external users are stuck in the queue, you can try temporarily disabling the use of Cisco Relay to determine if the problem is on the server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-23*

Disable the antimalware engine using the PowerShell script and restart the Exchange Transport Service

& $env:ExchangeInstallPath\Scripts\Disable-AntimalwareScanning.ps1

Restart-Service MSExchangeTransport

Source: https://techcommunity.microsoft.com/t5/exchange-team-blog/email-stuck-in-transport-queues/ba-p/3049447
