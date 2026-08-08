---
title: "SYSVOL folder being empty"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194981/sysvol-folder-being-empty
question_id: 2194981
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# SYSVOL folder being empty

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194981/sysvol-folder-being-empty (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I got an old Windows server 2012R2 standard - Physical which is a domain controller.

We got a new Hyper-V server - Windows Server 2022 standard which is promoted as Domain controller. 

We have migrated FRS to DFRS, but the SYSVOL folder is empty on the new server. 

Below is the error message:

The processing of Group Policy failed. Windows attempted to read the file **********gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:

-  a) Name Resolution/Network Connectivity to the current domain controller.

-  b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).

-  c) The Distributed File System (DFS) client has been disabled.

User Policy could not be updated successfully. The following errors were encountered: This is the main error message. We are just a small business. I am not allowed to get paid services. 

Please advise me. I am stuck with this for long time now.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-23*

Hi Neuvi, 

Thanks for the response.

-  Run this command on new server:

 All domain controllers have migrated successfully to the Global state ('Eliminated'). 

Migration has reached a consistent state on all domain controllers. 

Succeeded. 

-  Verify DFS Replication Status - How to Check DFS Replication Status | Resilio Blog

followed this one, the commands are not recognised

-  DNS resolution

Old server :

nslookup

Default server : localhost 

Address :  : :1

New server:

Default server : xyz.sha.local 

4)  

Verify SYSVOL Sharing and Permissions

Successful

SYSVOL -> Log on server share 

5)

>Update-DfsrConfigurationFromAD 

'Update-DfsrConfigurationFromAD' is not recognized as an internal or external command, 

operable program or batch file.

not recognised 

-  Check the event log : error 

The processing of Group Policy failed. Windows attempted to read the file **********gpt.ini from a domain controller and was not successful. Group Policy settings may not be applied until this event is resolved. This issue may be transient and could be caused by one or more of the following:

-  a) Name Resolution/Network Connectivity to the current domain controller.

-  b) File Replication Service Latency (a file created on another domain controller has not replicated to the current domain controller).

-  c) The Distributed File System (DFS) client has been disabled.

-  Restarting the DFS Replication Service : Not helped 

Sometimes, restarting the DFS Replication service can resolve synchronization issues. Before restarting the service, make sure that you have saved all necessary configuration and status information.

Could you please advise?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-20*

Hi Ta_16,

Thank you for posting in the Microsoft Community Forums.

-  Check the migration status

First, make sure that the SYSVOL migration process is fully completed and that all domain controllers have been successfully migrated to the DFSR state. You can use the dfsrmig /getmigrationstate command to check the migration state. If the migration is not yet complete or if some domain controllers are still in one of the states of the migration process, the SYSVOL folder may not yet be properly synchronized on the new server.

-  Verify DFS Replication Status

Ensure that the DFS Replication service is running on the new server and is configured to start automatically. You can check the status of the DFS replication service through the Service Manager. In addition, use the dfsradmin or dfsrdiag tools to check the detailed status and progress of DFS replication to ensure that there are no replication errors or delays.

-  Check network connectivity and DNS resolution

Since the error message mentions name resolution and network connectivity issues, make sure that the new server is able to resolve domain controller names correctly and that the network connection is stable. You can use the ping command and the nslookup command to test network connectivity and DNS resolution.

-  Verify SYSVOL Sharing and Permissions

Ensure that the SYSVOL folder is properly shared on the new server and has the appropriate permission settings. You can use the net share command to view a list of shared folders and use File Explorer or command line tools to check folder permissions.

-  Force synchronization of DFS replication

If the DFS replication service is working but the SYSVOL folder is still not synchronized, you can try to force synchronization of DFS replication. This can be done with the dfsrdiag tool or a PowerShell cmdlet such as Update-DfsrConfigurationFromAD. Note that forced synchronization may increase network load and should be used with caution.

-  Check the event log

Viewing the application on the new server and logs help you and the system determine the logs next to look for errors or warnings related to SYSVOL replication, DFS replication, or Group Policy. These logs may provide more detailed information about the problem, the resolution steps.

-  Restarting the DFS Replication Service

Sometimes, restarting the DFS Replication service can resolve synchronization issues. Before restarting the service, make sure that you have saved all necessary configuration and status information.

Best regards

Neuvi
