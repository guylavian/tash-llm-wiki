---
title: "Exchange 2019 - DAG and move database problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1146818/exchange-2019-dag-and-move-database-problem
question_id: 1146818
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 - DAG and move database problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1146818/exchange-2019-dag-and-move-database-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have 2 exchange 2019 in DAG Failover Cluster in other data centers.    

DC1 - Exch01 - 10.0.0.5    

DC2 - Exch02 - 10.0.1.5    

DC2 - Witness - 10.0.1.6    

I have 3 Mailbox Databases:    

DB01. DB02, Archive.    

When I move DB02 from Exch01 to Exch02 than emails stopped on Queue.     

In Queue Viewer I see this error:    

    

When I trying to move DB's to Exch02 I've got this:    

Active Manager operation failed. Error:The database action failed. Error: Move for database 'DB02' was suppressed because too many moves have happened recently. 3 moves have  happened within 01:00:00.. [Databases: DB02, Server: exch01.contoso.com]    

    + CategoryInfo          : InvalidOperation: (DB02:ADObjectId) [Move-ActiveMailboxDatabase], AmDbMoveMoveSuppressedException    

    + FullyQualifiedErrorId : [Server=Exch01,RequestId=651ecbd7-3318-46d3-979f-b3ec4d7454dd,TimeStamp=30.12.2022 12:32:45] [FailureCategory=Cmdlet-AmDbMoveMoveSuppressedException] 2701F309,Microsoft.Exch    

   ange.Management.SystemConfigurationTasks.MoveActiveMailboxDatabase    

    + PSComputerName        : exch01.contoso.com    

I can move databases only with parameter -SkipMoveSuppressionChecks.    

What is wrong with this configuration?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-03*

Hi @Yuki Sun-MSFT  ,  

Yeah, I checked Event Viewer.

Event Viewer errors from Exch01:

Error - Source: MSExchange Common - Event ID: 4999  

Watson report about to be sent for process id: 1940, with parameters: E12IIS, c-RTL-AMD64, 15.02.0922.027, w3wp#MSExchangeOWAAppPool, M.E.C.Owa2.Server, M.E.C.O.S.C.OwaMapiNotificationManager.SubscribeToSuiteNotification, System.NotSupportedException, 80d2-dumptidset, 15.02.0922.027.  

ErrorReportingEnabled: True

Error - Source: MSExchangeDiagnostics - Event ID: 1006  

The performance counter '\Exch01\MSExchange Assistants - Per Database(msexchangemailboxassistants-db01)\Event Dispatchers Catching Up' sustained a value of '187,00', for the '30' minute(s) interval starting at '03.01.2023 07:18:00'. Threshold breached since '03.01.2023 06:48'. None Trigger Name:EventDispatchersCatchupQueueTrigger. Instance:msexchangemailboxassistants-db01

Warning- Source: MSExchangeTransport - Event ID: 22004  

The periodic heartbeat to primary server exch02.contoso.com failed.

Warning- Source: MSExchange ADAccess - Event ID: 2160  

Process MSExchangeHMWorker.exe (ExHMWorker) (PID=22240). Recipient object CN=HealthMailbox6b71fad40e784990879a374fefcf1470,CN=Monitoring Mailboxes,CN=Microsoft Exchange System Objects,DC=contoso,DC=com read from AD1.contoso.com failed validation and will be excluded from the result set. Set event logging level for Validation category to Expert to get additional events about each failure.

Warning - Source: MSExchangeIS - Event ID: 1077  

The mailbox 4cc5de2e-9923-4dc3-9e5c-4b2db273a7df on database de65149d-2abc-4679-9923-78c204b0220b is approaching its storage limit. A notification has been sent to the user. This warning will not be sent again for at least twenty four hours.

Event Viewer errors from Exch02:

Warning - Source: MSExchange Mailbox Replication - Event ID: 1006  

The Microsoft Exchange Mailbox Replication service was unable to process jobs in a mailbox database.  

Database: Missing database (d800a330-b725-43c2-b874-b2964a783a5b)  

Error: Database 'd800a330-b725-43c2-b874-b2964a783a5b' doesn't exist.

Warning - Source: MSExchange ADAccess - Event ID: 2160  

Process MSExchangeHMWorker.exe (ExHMWorker) (PID=24904). Recipient object CN=HealthMailbox1fa460b28196438380410186d49e7512,CN=Monitoring Mailboxes,CN=Microsoft Exchange System Objects,DC=contoso,DC=com read from AD2.contoso.com failed validation and will be excluded from the result set. Set event logging level for Validation category to > Expert to get additional events about each failure.

Now I would like to unbutton the DAG, wait for a few houres and rebuild DAG.  

What do you think about it?
