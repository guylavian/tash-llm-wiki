---
title: "EXCHANGE 2016 DAG - Failover Cluster Event ID 1090"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185443/exchange-2016-dag-failover-cluster-event-id-1090
question_id: 185443
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-high-availability-clustering-high-availability"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# EXCHANGE 2016 DAG - Failover Cluster Event ID 1090

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185443/exchange-2016-dag-failover-cluster-event-id-1090 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have 6 exchange 2016 Server and failover Cluster in one of the server is not starting. But mailbox database copies are fine.  

The Cluster service cannot be started. An attempt to read configuration data from the Windows registry failed with error '2'. Please use the Failover Cluster Management snap-in to ensure that this machine is a member of a cluster. If you intend to add this machine to an existing cluster use the Add Node Wizard. Alternatively, if this machine has been configured as a member of a cluster, it will be necessary to restore the missing configuration data that is necessary for the Cluster Service to identify that it is a member of a cluster. Perform a System State Restore of this machine in order to restore the configuration data.  

These are the command from the output. As per this Replication and seeding status Healthy. But Cluster Service Failed.  

We don't have any backup data to restore.  

[PS] C:\Windows\system32>Get-MailboxDatabaseCopyStatus -Server “d-email02”  

Name                                          Status          CopyQueue ReplayQueue LastInspectedLogTime   ContentIndex  

                                                              Length    Length                             State

DB1\D-EMAIL02                             Healthy         0         0           12/3/2020 12:54:51 PM  Healthy  

DB2\D-EMAIL02                             Healthy         0         0           12/3/2020 12:55:28 PM  Healthy  

DB3\D-EMAIL02                             Healthy         0         0           12/3/2020 12:55:17 PM  Healthy  

DB4\D-EMAIL02                             Healthy         0         0           12/3/2020 12:55:42 PM  Healthy  

DB5\D-EMAIL02                             Healthy         0         0           12/3/2020 12:54:50 PM  Healthy  

PS C:\Users\administrator.NYCC> Get-ClusterNod  

Name                 ID    State  

D-EMAIL01           3     Up  

D-EMAIL02           4     Down  

D-EMAIL03           6     Up  

C-EMAIL01           1     Up  

C-EMAIL02           2     Up  

C-EMAIL03           5     Up

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-12-05*

If you face same problem in Exchange 2019 server:    

-  Clear-ClusterNode -Name XXXXXX (Problematic Server) -Force (PowerShall)    

-  Restart the server    

-  Add-DatabaseAvailabilityGroupServer -Identity "DAG Name" -MailboxServer XXXXXX(Problematic Server)    

-  Server should be added and validate the DAG members and FileShare.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-05*

I would remove the server from the DAG if it lets you. ( Remove all the database copies first)  

Then try to re-add back to the DAG, if that fails, consider simply removing Exchange at that point and rebuilding the server from scratch and then re-adding back to the DAG and re-adding mailbox copies.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi,  

Getting this error when I try - Start-DatabaseAvailabilityGroup DAG1 -MailboxServer D-EMAIL02  

WARNING: The operation wasn't successful because an error was encountered. You may find more details in log file  

"C:\ExchangeSetupLogs\DagTasks\dagtask_2020-12-04_20-57-47.659_start-databaseavailabilitygroup.log" on "D-EMAIL02".  

You can run this command on a database availability group (DAG) only when the DatacenterActivationMode parameter for  

the DAG is set to DagOnly

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi EricYin,  

Do I need to remove the server first before re-add back to DAG ?    

Remove-DatabaseAvailabilityGroupServer DAG1 -MailboxServer D-EMAIL02 - ?  

Do I need to re-seed from scratch by updating the database copy?  

Thanks  

SMI

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

It might be caused by a corruption over the cluster, please try the following steps:    

Manually Start Cluster Service of D-EMAIL02 in Cluster Service Manager.    

If failed, open the Command prompt as an administration and run the below command:    

```
Cluster Node D-EMAIL02 /ForceCleanup
```

Then reboot the server and run the below command on Exchange Powershell to re-add the node back to Cluster:    

```
Start-DatabaseAvailabilityGroup DAG1 -MailboxServer D-EMAIL02
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
