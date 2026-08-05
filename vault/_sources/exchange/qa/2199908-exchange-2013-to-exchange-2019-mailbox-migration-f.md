---
title: "Exchange 2013 to Exchange 2019 Mailbox Migration fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199908/exchange-2013-to-exchange-2019-mailbox-migration-f
question_id: 2199908
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange 2013 to Exchange 2019 Mailbox Migration fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199908/exchange-2013-to-exchange-2019-mailbox-migration-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Below you will find some background information.

-  We are in the process of migrating from the On-Prem Exchange 2013 to On-Prem Exchange 2019.

-  Exchange 2013 is installed on Windows 2012 R2.

-  Exchange 2019 is installed on Windows 2022.

-  Exchange 2012 is at 15.00.1497.048 level (the latest possible level -    Exchange Server 2013 CU23 Mar23SU)

-  Exchange 2019 is at 15.02.1544.004 level.

-  Exchange 2019 was installed without any issues.

-  Both Exchange servers can see each other in their EAC.

-  We have verified that all the Arbitration Mailboxes are created. There are seven such accounts because of Exchange 2019. We have moved all the Arbitration Mailboxes to Exchange 2019.

-  FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042

-  Migration.8f3e7716-2011-43e4-96b1-aba62d229136

-  SystemMailbox{1f05a927-xxxx-xxxx-xxxx-xxxxxxxxxxxx}

-  SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}

-  SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}

-  SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}

-  SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}

-  Exchange 2019 (using EAC) can see both Databases (Exchange 2013 and 2019) and indicates that both are mounted. We can click on both databases and get the status.

-  Exchange 2013 (using EAC) can see both Databases (Exchange 2013 and 2019) but indicates that the Exchange 2013 database is mounted but provides no status for the Exchange 2019 database (it is blank). When you click on the database it gives errors to 500 on the right screen.

-  We wanted to try migrating a test mailbox from Exchange 2013 to Exchange 2019 (just one test mailbox – a few pieces of email). When we set up the batch and started the process, it started, but the status stayed in SYNCING and was not complete. We can only cancel it from the CLI command level.

-  We have identified that the Arbitration Mailboxes are all present, but they are all DISABLED. We cannot enable any of the mailboxes (Migration.8f3e7716-2011-43e4-96b1-aba62d229136) which is necessary using GUI or CLI.

-  We have deleted the Migration mailbox and recreated it without any error messages (used commands below)

-  \Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD

-  Enable-Mailbox -Identity "Migration.8f3e7716-2011-43e4-96b1-aba62d229136" -Arbitration

-  Set-Mailbox -Identity "Migration.8f3e7716-2011-43e4-96b1-aba62d229136" -Arbitration -Management $true -Force

The mailbox (Migration.8f3e7716-2011-43e4-96b1-aba62d229136) gets created but it is never enabled. Without this mailbox being enabled, migration will not work. Has anyone experienced this issue, and have they been able to resolve the issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-25*

Hello A2I-1,    

thank you for posting on the Microsoft Community Forums.     

Based on the description, I understand that your issue is related to Exchange.     

Since there are no engineers dedicated to Exchange in this forum. In order to be able to deal with your questions quickly and efficiently, I recommend that you repost your questions in the Q&A forum, where there will be a dedicated engineer to provide you with a professional and effective response.    

Here is a link to the Q&A forum: https://learn.microsoft.com/en-us/answers/questions/    

Have a nice day.    

Best regards,   

Lei
