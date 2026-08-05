---
title: "ECP/OWA is no longer accessible after renewing the certificates (MS Exchange and MS Ex Server Auth Certificate) Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1498032/ecp-owa-is-no-longer-accessible-after-renewing-the
question_id: 1498032
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# ECP/OWA is no longer accessible after renewing the certificates (MS Exchange and MS Ex Server Auth Certificate) Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1498032/ecp-owa-is-no-longer-accessible-after-renewing-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,
Yesterday, I renewed the certificates ( Microsoft Exchange Server Auth Certificate) on Exchange Server 2019 from ECP. Then The clients could no longer send and receive emails, and the Exchange Admin Center was no longer accessible.
In IIS Manager I selected the certificates again. After that, the clients could work again only with outlook app. but the problem is, ECP and OWS are still unreachable.
I followed (https://learn.microsoft.com/en-us/exchange/architecture/client-access/assign-certificates-to-services?view=exchserver-2019#use-the-exchange-management-shell-to-assign-a-certificate-to-exchange-services) to assigned correct services to my SSL certificate.  Also Enable-ExchangeCertificate -Thumbprint 5113ae0233a72fccb75b1d0198628675333d010e -Services POP,IMAP,SMTP,IIS. and lastly by following (https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-access-owa-or-ecp-if-oauth-expired)  created new AUTH certificate. but error I got is something went wrong OWA Exchange Server SCREENSHOT (Error 3).Error 3.JPG
Please help me to resolve this error and access EAC and OWA.Certificate Info.PNG
Thank you

## Answers

_No answers on this thread._
