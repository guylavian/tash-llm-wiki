---
title: "Exchange 2016 Standard ‎(Build 466.34)‎ | What the correct way to deal with an expired certificate (Exchange UCC 2017)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317710/exchange-2016-standard-build-466-34-what-the-corre
question_id: 317710
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Standard ‎(Build 466.34)‎ | What the correct way to deal with an expired certificate (Exchange UCC 2017)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317710/exchange-2016-standard-build-466-34-what-the-corre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are running an Exchange 2016 Standard server (Version 15.1 ‎(Build 466.34)‎).

The following Self-Signed Certificate recently expired:

Name: Exchange UCC 2017  

Status: DateInvalid  

Issuer: CN=Starfield Secure Certificate Authority - G2, OU=http://certs.starfieldtech.com/repository/, O="Starfield Technologies, Inc.", L=Scottsdale, S=Arizona, C=US  

Expires on: 10/23/2020  

Subject:

Assigned to services  

SMTP: CN=remote.<domain>.com, OU=Domain Control Validated  

Thumbprint: D********CECA  

Serial Number: 1D0*********F3E20  

Public key size: 2048  

Has Private key: Yes

Services:  

IMAP  

POP

We do have a separate, valid cert that handles IIS & SMTP:  

Microsoft Exchange  

Self-signed certificate  

Issuer: CN=<Exchange Server Name>  

Status  

Valid  

Expires on: 8/16/2021  

Expires on:Renew  

Assigned to services  

IIS, SMTP

What is the appropriate action to take? Should it simply be renewed?

There is currently no impact, but I want to ensure I do this correctly.

Thanks in advance.

Regards,  

Rudy

78992-certificate-exchange-ucc-2017.txt

![78945-78438-certlist.png][2]

![78591-cert3.jpg][5]

[2]: /api/attachments/78945-78438-certlist.png?platform=QnA [5]: /api/attachments/78591-cert3.jpg?platform=QnA

## Answers

_No answers on this thread._
