---
title: "Regarding delays in receiving emails on Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656850/regarding-delays-in-receiving-emails-on-exchange-s
question_id: 1656850
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Regarding delays in receiving emails on Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656850/regarding-delays-in-receiving-emails-on-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This sentence was translated from Japanese to English using Google Translate.

For some reason, I would like to use two on-premises Exchange Servers, but as shown in the ExchangeECP delivery report results below, there will be a delay in reception.

[6 minute delay report] Sent at 16:54 → Received at 17:00

Delivery report

  Information System Department (Information System Address@*************)‎

On hold 

2024/04/13 16:54 <ExchangeServer A FQDN>

<ExchangeServer A FQDN> received a message from <ExchangeServer A FQDN>*PC name is uppercase.

2024/04/13 16:54 <ExchangeServer A FQDN>

The email address of the recipient "Information system address @************" is the email address

Updated to "Information system address@*************". The message is being delivered.

2024/04/13 16:54 <ExchangeServer A FQDN>

Messages are from 2024/04/13 16:54:18 (UTC+09:00) Osaka, Sapporo, Tokyo,

Queued on server '<ExchangeServer A FQDN>'.

The time of the last attempt to send a message was 2024/04/13 16:55:13 (UTC+09:00)

Osaka, Sapporo, Tokyo, the error generated is '[{LED=};{MSG=};{FQDN=};{IP=};{LRT=}]'.

[No delay report] Sent at 16:39 → Received at 16:39

Delivery report

Information System Department ‎(Information System Address@***************)‎

On hold 

2024/04/13 16:39 <ExchangeServer A FQDN>

Message from <ExchangeServer A FQDN> to <ExchangeServer B FQDN>=421 4.2.1 Unable to connect ->

SocketError: Failed to connect. Winsock error code: 10051, Win32 error code: 10051;Redirected to <ExchangeServer B FQDN>.

2024/04/13 17:05 <ExchangeServer A FQDN>

There are no further logs, so no further information is available about this message.

The sender and recipient are the same in both cases.

Also, in the delay report, for some reason, his FQDN for Exchange Server A was written in lowercase letters only in one place.

The OS of each Exchange Server is shown below.

ExchangeServer A: Windows Server 2016 std/Exchange Server 2016

ExchangeServer B: Windows Server 2022 std/Exchange Server 2019

We look forward to hearing from you, no matter how trivial.

If we have any other necessary information, we will share it immediately.

## Answers

_No answers on this thread._
