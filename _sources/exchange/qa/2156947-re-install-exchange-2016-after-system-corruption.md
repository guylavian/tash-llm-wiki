---
title: "Re-install Exchange 2016 after system corruption"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2156947/re-install-exchange-2016-after-system-corruption
question_id: 2156947
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Re-install Exchange 2016 after system corruption

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2156947/re-install-exchange-2016-after-system-corruption (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

Before we open a pay-per-incident(s) MS ticket, I thought I'd lob this scenario out to the community.

Our sister organization has a lot of technical debt, both hardware and & software. We needed to get them on Exchange Online, and to do that, 1-2 years ago we installed ADSync and hybrid Exchange on separate VMs at our office instead of at their office and depended upon the site-to-site tunnel & Windows 2-way trust to integrate it with their old 2008R2 domain/forest in their office.

Fast forward to October 2024, we had a ransomware attack on our VM environment, which encrypted all the VMDKs, various logs, etc. We wiped all our VMware hosts and shared storage partitions, re-installed from scratch, performed bare metal recovery for all of our servers, but not for our sister company servers. That is because we removed the trust & S2S tunnel and there are no plans to reactivate them. We put in a tiny physical server for ADSync in their office.

But during attempted recovery of their Exchange 2016, the AD computer object was deleted before realizing the AD Recycle Bin was not enabled, so without that object we can't perform a recovery. We need to get the hybrid Exchange 2016 back into their environment quickly, but orphan references from the last 2016 server remain in AD. 

Knowing that E2016 & E2019 reach end of extended support in October 2025, what is best practice to permit Exchange 2016 to re-install while trying to keep as many as the prior settings as possible, and then to get them migrated to Exchange SE before EOS?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-03*

That's not exactly what I'm asking. Due to their technical debt, the only compatible Exchange version is 2016. I'm asking 1) how to re-introduce Exchange Hybrid 2016 into their org when the previous E2016 hybrid server was ungracefully removed from the domain and the old E2016 computer object was also deleted and not recoverable. New E2016 install detects old Exchange server from AD metadata, yet I'd sure like to have the replacement E2016 server pickup as much as the old configuration as possible to ease deployment.

The only databases on the on-premise server are system mailboxes (discovery, health, etc.), the user mailboxes will be in Exchange Online (if that changes the migration steps from E2016 to E2019SE). Because E2016 and E2019SE will likely have different supported OS's, I don't think the upgrade from E2016 CU23 > E2019 CU15 > E2019 SE is an in-place upgrade?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-13*

Hello, @Mueller, Jim,

Welcome to the Microsoft Q&A platform! 

According to the official statement (Upgrading your organization from current versions to Exchange Server SE | Microsoft Community Hub), only Exchange 2019 CU15 version supports in-place upgrade to SE version. So, I would recommend you use the latest Exchange 2019 CU15 version now.

If you need to use Exchange 2016 version in your organization, you need to fully backup the database as well as other custom settings while doing the update migration. The following methods are for your reference:

-  using Windows Server Backup, backup the entire Exchange database. You can download the Features through Server manager.

-  Create a backup folder and export the customized settings (database, connectors, etc.) using powershell:

```
Get-MailboxDatabase | Export-Clixml -Path “C:\Backup\MailboxDatabases.xml”
Get-ReceiveConnector | Export-Clixml -Path “C:\Backup\ReceiveConnectors.xml”
Get-SendConnector | Export-Clixml -Path “C:\Backup\SendConnectors.xml”
Get-TransportRule | Export-Clixml -Path “C:\Backup\TransportRules.xml”
```

-  Backup the certificate:

```
$cert = Get-ExchangeCertificate | Where-Object { $_.Services -match “IIS” }
Export-ExchangeCertificate -Thumbprint $cert.Thumbprint -BinaryEncoded -Password (Read-Host “Enter password” -AsSecureString) | Set-Content - Path “C:\Backup\ExchangeCert.pfx” -Encoding Byte
```

After completing the backup operation, when releasing the SE, then upgrade from Exchange 2016 CU23 to Exchange 2019 CU15 and finally to the SE version.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
