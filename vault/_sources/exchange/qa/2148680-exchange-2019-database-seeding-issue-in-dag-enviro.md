---
title: "Exchange 2019 Database Seeding Issue in DAG Environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2148680/exchange-2019-database-seeding-issue-in-dag-enviro
question_id: 2148680
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Database Seeding Issue in DAG Environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2148680/exchange-2019-database-seeding-issue-in-dag-enviro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am encountering an issue with an Exchange 2019 database. My environment consists of four Exchange servers (two in the DC site and two in the DR site) configured in a Database Availability Group (DAG) running CU 13.

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

Please provide proper resolution steps for this issue. Additionally, if the issue is caused by the network or disk, how can I find out it?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-20*

Hello, @Dipto Adhikary,

Welcome to the Microsoft Q&A platform!

Based on the information provided, here are some detailed steps to help troubleshoot and potentially resolve the issue:

-  Network Configuration and Health Checks: Use the `Get-DatabaseAvailabilityGroupNetwork` command to verify your network configuration. Test the replication health with the `Test-ReplicationHealth` cmdlet.

-  Monitor Seeding Progress: Track the seeding progress with the `Get-MailboxDatabaseCopyStatus` cmdlet.

-  Disk Performance and Event Logs:  Verify disk performance metrics and review event logs for any errors. Ensure antivirus software has the necessary exclusions for Exchange files and processes to avoid interference.

-  Network and Bandwidth Considerations: Take into account network latency, available disk space, and bandwidth utilization during the seeding process. Ensure consistent network performance using tools like `ping` and `tracert` to check for packet loss or jitter. Monitor disk performance with `PerfMon` to identify any intermittent bottlenecks.

-  DAG Configuration: Confirm that DAG networks are configured correctly. Ensure that circular logging is disabled for the involved databases.

-  Granular Control of Seeding: Run the `Update-MailboxDatabaseCopy` cmdlet with the `-ManualResume` parameter to manage the seeding process more precisely. Review Exchange Replication service logs for detailed error messages that might provide more context about the issue.

-  Database Consistency and Seeding Timing: Perform a consistency check on the database using `eseutil` to ensure that the database is in a good state. Consider conducting the seeding process during off-hours to minimize operational load on the network and disk.

-  Cluster Configuration: Ensure that the Windows Server Failover Cluster configurations are optimal and working as intended.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-20*

As log disk remains empty. There can be the issue with the log disk or its configuration. Ensure that the log disk has enough space, and verify that the logs are being written correctly. Sometimes, Exchange can’t create log files if the disk is full or if there are permission issues. Move the transaction log files to another disk, if possible, and check if that resolves the seeding issue.

-The large `CopyQueueLength` you're seeing (740,000+) is a clear sign that replication is struggling. Since replication is working fine for other databases, this might be isolated to the DIAMONDDB copy. Run the `Get-MailboxDatabaseCopyStatus` cmdlet to check the status of all database copies, and look for any specific errors or warnings related to this database. Also, check the database path (`N:\DIAMONDDB\DIAMONDDB.edb`) to make sure the file exists and is accessible. The error saying the database file was not found suggests a potential path or permission issue. Make sure that the `Exchange Trusted Subsystem` has full permissions on the directory where the database and log files reside.

-Network latency is around 6ms, which is fine. However, network congestion or issues like intermittent packet loss might still be affecting replication, even if other databases are fine. Use tools like `ping` or `tracert` to check for any network drops or delays between your servers, particularly focusing on the DAG replication traffic.

-Antivirus software can sometimes interfere with Exchange operations, even if the logs don’t show any obvious problems. Since the software is running on all servers, try temporarily disabling it and attempt seeding again. If this works, you’ll need to adjust antivirus exclusions for Exchange files and directories.

-Running a tool like eseutil could also help identify any potential corruption or issues with the database files themselves.
