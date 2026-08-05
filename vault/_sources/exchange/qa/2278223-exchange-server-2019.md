---
title: "Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278223/exchange-server-2019
question_id: 2278223
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278223/exchange-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am currently using Exchange Server 2016 and planning to upgrade to Exchange Server 2019.

My existing environment consists of two Exchange 2016 servers (Server01 and Server02). I have provisioned two new Exchange 2019 servers (Server03 and Server04). Below are the steps I have performed so far:

Upgraded the Active Directory schema for Exchange 2019.

Installed Exchange 2019 on Server03 and Server04.

Configured virtual directories and URLs on the Exchange 2019 servers.

Imported SSL certificates onto the Exchange 2019 servers.

Configured a Database Availability Group (DAG) using a file share witness.

-  On Exchange 2016:

-  Server01 hosts DB01

-  Server02 hosts DB02

   On Exchange 2019:

-  Created DB03 on Server03 and DB04 on Server04.

   For DB03, I created the database via the GUI and ensured the "Mount this database" option was unchecked. Then, I ran the following PowerShell commands. Please let me know if this approach is correct:

```
Mount-Database DB03
   Add-MailboxDatabaseCopy -Identity DB03 -MailboxServer "Server04" -SeedingPostponed
   Suspend-MailboxDatabaseCopy DB03\Server04 -DeleteExistingFiles
   Update-MailboxDatabaseCopy DB03\Server04
```

-  When I run the following command, I can see the arbitration mailboxes, and they appear to reside only on Server01.    Get-Mailbox -Arbitration | Format-Table Name, ServerName, Database, AdminDisplayVersion      Questions:

-  Should every Exchange server host arbitration mailboxes?

-  How can I move the arbitration mailboxes to Exchange 2019?

-  After moving the arbitration mailboxes, I plan to add Server03 and Server04 to the existing Send Connector.

Are there any additional steps I need to take before decommissioning the Exchange 2016 servers?

## Answers

_No answers on this thread._
