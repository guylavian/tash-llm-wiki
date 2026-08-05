---
title: "Exchange Server 2019 - Renovación de certificado"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160361/exchange-server-2019-renovaci-n-de-certificado
question_id: 1160361
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Server 2019 - Renovación de certificado

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160361/exchange-server-2019-renovaci-n-de-certificado (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Tengo un servidor con Exchange 2019 se vencio el certificado firmado de una autoridad de certificacion

 

Ejecute la renovacion y envie  el archivo .req 

Me devolvieron el archivo.crt  lo aplico pero no desaparece el estado invalido y el pedido pendiente

Agradezco la ayuda posible para solver este inconveniente

Saludos y muchas gracias

Rene

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-23*

Hi @Jose Rene Rangel  ,

They sent me three files with these extensions:

After receiving the certificate files, have you also followed the instructions in the document below to complete the request?  

Complete a pending Exchange Server certificate request

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-13*

Hi @Jose Rene Rangel,

Currently in Microsoft Q&A we only support English, could you please edit your question into English？Then we can help to solve your issues, thanks for your understanding.   

Then based on a quick machine translation, my understanding is that the certificate still show as "Pending" after you renewing it, right? If this is the case, I'd suggest reviewing the document below to make sure you've followed the steps correctly to renew the certificate:  

Renew an Exchange Server certificate

With this confirmed and the issue persists, please check the certificate via MMC, if it shows up properly with the private key, you could try the steps below and see the result.

-  Using MMC to export the certificate with the private key.

-  Delete this certificate from Exchange.

-  Put the certificate back into Exchange using the Import-ExchangeCertificate.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
