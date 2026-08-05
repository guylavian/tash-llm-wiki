---
title: "Can't remove Exchange 2019 CU12"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021823/cant-remove-exchange-2019-cu12
question_id: 1021823
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Can't remove Exchange 2019 CU12

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021823/cant-remove-exchange-2019-cu12 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody! Please help - need to uninstall Exchange 2019 server but receiving some errors during process:    

    

This is fresh install 2 days ago - so I even didn't create any database, boxes - nothing. How to remove this Exchange correctly? Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-28*

I found a solution:    

C:\Windows\system32\lodctr.exe /R    

And then:    

 iisreset /stop     

 iisreset /start

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-27*

Hello! Please look at this:    

[PS] C:\Windows\system32>Get-MailboxDatabase    

Name                           Server          Recovery        ReplicationType    

----                           ------          --------        ---------------    

Mailbox Database 1277679589    MAIL            False           None    

[PS] C:\Windows\system32>Get-Mailbox -Database "Mailbox Database 1277679589"    

WARNING: Task module "CmdletHealthCountersModule.Task_IterateCompleted" fails with exception "The type initializer for    

'Microsoft.Exchange.Configuration.TenantMonitoring.TenantMonitor' threw an exception.". This module is skipped. Task    

execution result should not be affected.    

WARNING: Task module "CmdletHealthCountersModule.Task_Release" fails with exception "The type initializer for    

'Microsoft.Exchange.Configuration.TenantMonitoring.TenantMonitor' threw an exception.". This module is skipped. Task    

execution result should not be affected.    

[PS] C:\Windows\system32>    

What does it mean?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-27*

There is a possibility that the database you’re trying to remove is an Archive Database for a mailbox residing on a different mailbox database.    

The following command helps you list mailboxes using a specific database as Archive Database:    

```
Get-Mailbox | where {$_.ArchiveDatabase -eq ""}
```

Check following links for more details - This mailbox database contains one or more mailboxes… and How to Remove a Database from Exchange 2010, 2013, 2016, and 2019?]1    

Also Microsoft mentioned in the KB 3093175 that this could be caused by an AuditLog, so check if such one exists.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-26*

Hi    

You can first find the hidden mailboxes and delete them then delete the database and try to uninstall Exchange On-premises 2019 again. Here are the detailed steps:    

- 	Run “Get-MailboxDatabase” to see the MailboxDatabases you have.     

- 	Use the following commands to check the mailboxes in the Databases separately:    

Get-Mailbox -Database “Database Name”    

Get-Mailbox -Database “Database Name” -Archive    

Get-Mailbox -Database “Database Name” -Arbitration    

Get-Mailbox -Database “Database Name” -PublicFolder    

Get-Mailbox -Database “Database Name” -Monitoring    

Get-Mailbox -Database “Database Name” -AuditLog    

-   If you use the above commands to find any mailbox, you can use command of” Get-Mailbox -Arbitration/Archive/PublicFolder/Monitoring/AuditLog | Remove-Mailbox -Arbitration/Archive/PublicFolder/Monitoring/AuditLog -RemoveLastArbitrationMailboxAllowed “to remove the mailbox.    

-  Use EAC to navigate to Servers -> Databases, highlight the database you wish to remove and then click on the trash icon to delete the Database.    

-  Try to uninstall Exchange On-Premises 2019 again.    

If this Answer is helpful, please click "Accept Answer" to upvote it. If you have extra questions about this answer, please click "Comment" and I will come to your aid.
