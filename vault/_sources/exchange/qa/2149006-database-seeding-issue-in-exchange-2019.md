---
title: "Database Seeding Issue in Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149006/database-seeding-issue-in-exchange-2019
question_id: 2149006
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Database Seeding Issue in Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149006/database-seeding-issue-in-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,

I'm encountering an issue with an Exchange 2019 database. My environment consists of four Exchange servers (two in the DC site and two in the DR site) configured in a Database Availability Group (DAG) running CU 13.

The database has a copy on the two servers in the DC site, where it is working perfectly. The database size is approximately 800 GB. However, when I attempt to add this database as a copy to the DR site servers, the following issues arise:

-  The database starts seeding but shows a CopyQueueLength of more than 740,000, and this value keeps increasing continuously.

-  Other database copies on the DR site servers are replicating successfully.

-  All database copies (including the problematic one) reside on the same physical disk across all servers.

Troubleshooting Steps Performed

I have tried the following steps to resolve the issue:

-  Removed the problematic database copy, cleared the disk, and re-added it.

-  Ran the necessary commands to delete existing files before re-seeding.

-  Increased the bandwidth to 500 Mbps.

-  Verified the disk's average read/write speed, which is below 0.020 seconds.

-  Checked the Active Directory replication status, and it is working fine.

-  Verified the network latency, which is around 6 ms.

-  Confirmed the DAG network configuration is correct, and all nodes are operational.

-  Ensured the cluster is working and all nodes are up.

-  Rebooted the Exchange servers.

Observations

-  During seeding, the disk storage consumes space for the EDB file, but the log disk remains completely free.

-  Other databases on the DR site servers, which use the same physical disk, are functioning without issues.

-  If there were a network issue, it would affect replication for other databases, but this is not happening.

-  The servers have antivirus software installed, but the antivirus logs show no blocked URLs or activities related to Exchange.

I am attaching the relevant event logs for your reference.

-  Database redundancy two-copy health check failed. You can ignore this error if you have less than 3 database copies configured. This event can be disabled by setting the following regkey to 1: 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\Replay\Parameters -> DatabaseHealthCheckRedundancyTwoCopyAlertDisabled'. Database: DIAMONDDB Redundancy count: 2 Error: There were database redundancy check failures for database 'DIAMONDDB' that may be lowering its redundancy and putting the database at risk of data loss. Redundancy Count: 2. Expected Redundancy Count: 2. Detailed error(s):          godfe-04:         Passive database copy 'DIAMONDDB\Server04' has an unhealthy status 'Seeding' for duration 00:04:26.0832770. [SuspendComment: None specified.] [ErrorMessage: None specified.].

-  The Microsoft Exchange Replication service encountered an error while inspecting the logs and database for DIAMONDDB\Server-04 on startup. Error: File check failed : Database file 'N:\DIAMONDDB\DIAMONDDB.edb' was not found.

-  The log copier for 'DIAMONDDB\Server-04' is starting with the lowest generation on the source at gen 0xBC1B4 (770484).

Any feedback would be great and if its a network or disk related issue that I haven't ruled out yet, how do I check for that?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-20*

Hi, @Dipto  @Moshiur (Moshiur Khan)  

Another URL for this thread is here Exchange 2019 Database Seeding Issue in DAG Environment - Microsoft Q&A

You've done detailed troubleshooting, so there are some potential causes and other steps you can take: 

-  Make sure there is no additional load or disk delay outside of the torrenting period. Check the Event Viewer logs for any disk errors. 

-  Use a network monitoring tool to verify that there is no packet loss, high retransmission rate, or network congestion during seeding. 

-  Make sure the database and log files are not corrupted, which can be checked with Eseutil, etc. 

-  Verify that the DAG configuration and operational status check are optimal.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-20*

Please refer my answer here- https://learn.microsoft.com/en-us/answers/questions/edit/2148680/answer/1904542?orderby=helpful#answer-1904542
