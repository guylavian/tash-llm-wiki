---
title: "Exchange Server 2019 - TLS negotiation failed with error BadBindings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202312/exchange-server-2019-tls-negotiation-failed-with-e
question_id: 202312
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2019 - TLS negotiation failed with error BadBindings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202312/exchange-server-2019-tls-negotiation-failed-with-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,    

I'm trying to troubleshoot a TLS negotiation issue on an Exchange 2019 server.    

Various clients (multifunctional device which preform scan to mail) cannot connect to the Exchange server.    

The TLS negotiation fails because the Exchange server closes the connection after the client has send    

the 'client hello' packet. Because the server closes the connection, I'm assuming that the server does not    

like / understand something that the client send in the 'client hello' packet.    

The server log includes the following error:    

"TLS negotiation failed with error BadBindings"    

Searching for 'BadBindings' does not result in an useful leads, as I was hoping to find    

some sort explanation of what this error might mean (what might be wrong or what could be causing this).    

The 'BadBindings' error might be related to the timestamp used in the TLS clienthello, as it seems    

that clients which are failing to connect use a 'random' timestamp and clients which can connect use    

a timestamp which is based on the actual / current date and time.    

Does anyone know if Exchange 2019 checks the timestamp in the TLS clienthello?    

I've attached a screenshot from a network capture showing the 'random' timestamp    

Thank you in advance for your feedback

## Answers

_No answers on this thread._
