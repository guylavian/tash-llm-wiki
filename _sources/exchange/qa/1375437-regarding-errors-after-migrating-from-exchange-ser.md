---
title: "Regarding errors after migrating from Exchange Server 2013 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1375437/regarding-errors-after-migrating-from-exchange-ser
question_id: 1375437
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Regarding errors after migrating from Exchange Server 2013 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1375437/regarding-errors-after-migrating-from-exchange-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

thank you

Migrated from ExchangeServer2013 to ExchangeServer2019

I have already uninstalled 2013 because it was necessary to keep the host name the same during migration.

We used a temporary Exchange Server for mailbox migration. This server is currently shut down as we plan to delete it in the future.

Based on what I wrote above, please tell me about the following two things.

-  About “MSExchange Mitigation Service”

 　The error "MSExchange Mitigation Service" (Event ID: 1008) is occurring every hour.

 　I understand that this error occurs because a temporary Exchange Server remains and there is no actual harm, but is this correct?

　 *There are no mailboxes left on the temporary server

-  About BackEnd's certificate

　 I created an SSL certificate using ADCS for use with Exchange Server.

　 I bound the created SSL certificate in IIS

　 I bound the created SSL certificate with both "DefaultWebSite (http, port 443)" and "ExchangeBackEnd (http, port 444)" in IIS

 　However, I saw an article that says that in ExchangeBackEnd, self-certificates should not be deleted.

　 https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-ecp-ems-cannot-connect-after-self-signed-certificate-removed

　Please tell me whether I should restore the ExchangeBackEnd certificate.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-09-25*

Generally speaking, it is not a good idea to remove the self-signed certificate from the IIS website for ExchangeBackEnd. Exchange does internal server communication using this certificate. The exchange might not run properly if you erase the certificate.

You can make a new SSL certificate and bind it to the ExchangeBackEnd website if you are concerned about the security of the self-signed certificate. The self-signed certificate should, nonetheless, be backed up in case you ever need to recover it.
