---
title: "Exchange 2019 CU12 - how to import new SSL-certificate?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1434788/exchange-2019-cu12-how-to-import-new-ssl-certifica
question_id: 1434788
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 CU12 - how to import new SSL-certificate?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1434788/exchange-2019-cu12-how-to-import-new-ssl-certifica (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody! Need some help - we have to replace the SSL-certificate on the Exchange 2019 CU12 server. So this procedure should look like this:

Import-ExchangeCertificate -Server "MAIL" -FileData ([System.IO.File]::ReadAllBytes('\mail\Certificates\our_domain_cert.pfx')) -PrivateKeyExportable:$true -Password (ConvertTo-SecureString -String '12345678' -AsPlainText -Force)

And, after this we check with the command

[PS] C:\Windows\system32>Get-ExchangeCertificate

Thumbprint                                Services   Subject

8490765C4C47D81***E2F46BEBB98EF9084A3B  I..WS..    CN=.ourdomain.com, O=LLC Company, L=NY, S...

D5EFF683AD986C988***24C107EEDCA3B484E799  ....S..    CN=Microsoft Exchange Server Auth Certificate

F960DCC7F5BEB003****563638FD85BC40D855E8  .P.WS..    CN=mail

C4D2E9EBA63795484***C1660EBCBB307E987EBC  .......    CN=WMSvc-SHA2-MAIL

So the question is - after we have imported a new certificate (but the current one has not yet expired) - do we need to take any other actions or is it enough just to carry out the import procedure? Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-11-22*

You need to assign  the new certificate for the right services:

https://learn.microsoft.com/en-us/exchange/architecture/client-access/assign-certificates-to-services?view=exchserver-2019#use-the-eac-to-assign-a-certificate-to-exchange-services

Once that is done, restart IIS, and test. 

Then you can remove the old one if not needed
