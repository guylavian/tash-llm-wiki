---
title: "Migration Exchange 2013 to Exch 2019 - Problems with the digital certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1065652/migration-exchange-2013-to-exch-2019-problems-with
question_id: 1065652
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Migration Exchange 2013 to Exch 2019 - Problems with the digital certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1065652/migration-exchange-2013-to-exch-2019-problems-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys, migration Exch2013 to Exch2019 on Domain W2016 with FFL and DFL W2012R2.    

I have already installed Exch2019 but every time someone opens Outlook the security warning of the digital certificate pops up (auto-generated during the installation of Exch2019) (see error: https://postimg.cc/YLYY7TGp).    

On the "Exchange Admin Center" of Exch2019, Servers, Certificates, selecting Exch2019 in the list of servers, I do not see the valid certificate (Sectigo) in the list of installed certificates, instead I see them on the 2 Exch2013 (CAS and Mailbox).    

When I try to import it from a .pfx it tells me:    

Error:    

A special Rpc error occurs on server SRV-EXCH2019: Cannot import certificate. A certificate with the thumbprint 801010101010101010101010101E already exists.    

How can I solve?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-29*

The tool reported a problem, lack of private key to be precise, surely I did wrong the export / import of the certificate, I corrected it, restarted the services, and the certificate became available on the EAC to install it on the Exchange services.    

Problem solved!!!    

Thanks 10000000 @Andy David - MVP

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-28*

Hi @Andy David - MVP   , in the mmc snap-in I see 4 certificates. The 3 certificates that I also see in the EAC and a fourth certificate that corresponds precisely to that of Sectigo that I do not see in the EAC.
