---
title: "New Exchange server installation in a new site/DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/206055/new-exchange-server-installation-in-a-new-site-dc
question_id: 206055
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# New Exchange server installation in a new site/DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/206055/new-exchange-server-installation-in-a-new-site-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am doing a project of Exchange 2013 migration to a new DC/site in the same forest/organization. So we have built 2 new Exchange 2013 servers in the new site. All okay but am seeing Microsoft Exchange server Auth Cert is missing in both the new exchange servers installed. The servers already there in the old site have got the cert and SMTP service assigned to it. I have tested creating test mailboxes on the new Exchange server DB and did some mail flow testing internally and it worked. Will there be any issues having the cert missing on the new server? I didn't find any error while installing Exchange 2013 on those two new servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Hi @GoodResource   ,    

According to my research and test, the Microsoft Exchange Server Auth Certificate is one of the certificates that comes with the installation of Exchange and is used for server-to-server authentication and integration by using OAuth. So this certificate is indispensable, when I remove this certificate from my Exchange server, some functions of Exchange are abnormal.     

Please run the following command to confirm whether the certificate is really authentic:    

```
Get-ExchangeCertificate | fl
```

If your Exchange is functioning normally, you can observe it for a period of time as Andy said. You can also run the following command line to export the existing Microsoft Exchange server Auth Cert, and then import it to the server that lacks the certificate:    

```
Export-ExchangeCertificate -Thumbprint  -FileName "\.pfx" -BinaryEncoded -Password (ConvertTo-SecureString -String ' ' -AsPlainText -Force) [-Server ]  
Import-ExchangeCertificate -FileName "\" -Password (ConvertTo-SecureString -String ' ' -AsPlainText -Force) [-PrivateKeyExportable ] [-Server ]
```

For more detailed steps, you can refer to：Export a certificate from an Exchange server and Import or install a certificate on an Exchange server    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
