---
title: "Cannot move mailbox to a new Database - Exchange 2016 on Prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299342/cannot-move-mailbox-to-a-new-database-exchange-201
question_id: 299342
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Cannot move mailbox to a new Database - Exchange 2016 on Prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299342/cannot-move-mailbox-to-a-new-database-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Not sure how to fix this, had no problem moving a mailbox to a new database before, but trying to move a mailbox to a new database and it is stuck at syncing and when I check the status, I see the following error - StalledDueToTarget_MdbReplication. I have checked both the databases on the DAG and there are no health issues and copy queue length is 0. I have tried to move 2 separate mailboxes on separate databases and the same thing is happening. I have also tried from both the Web GUI and powershell and they both seem to stall at the same 37%. I have also verified that the Migration Mailbox is listed when checking for the Arbitration mailbox. I am not sure what else to check, but seems I cannot migrate any mailboxes at this point. Anyone have any suggestions on what could be causing this issue?  

Exchange 2016 - 2 DAG groups - 4 Servers - Hybrid mode with all mailboxes on-prem. Tried to move a mailbox from each DAG and have the same problem on both of them.  

Thanks,  

Gavin

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

[PS] C:\WINDOWS\system32>Get-ServerComponentState SERVER1  

Server                         Component                  State  

SERVER1.domainname.com ServerWideOffline          Active  

SERVER1.domainname.com HubTransport               Active  

SERVER1.domainname.com FrontendTransport          Active  

SERVER1.domainname.com Monitoring                 Active  

SERVER1.domainname.com RecoveryActionsEnabled     Active  

SERVER1.domainname.com AutoDiscoverProxy          Active  

SERVER1.domainname.com ActiveSyncProxy            Active  

SERVER1.domainname.com EcpProxy                   Active  

SERVER1.domainname.com EwsProxy                   Active  

SERVER1.domainname.com ImapProxy                  Active  

SERVER1.domainname.com OabProxy                   Active  

SERVER1.domainname.com OwaProxy                   Active  

SERVER1.domainname.com PopProxy                   Active  

SERVER1.domainname.com PushNotificationsProxy     Active  

SERVER1.domainname.com RpsProxy                   Active  

SERVER1.domainname.com RwsProxy                   Active  

SERVER1.domainname.com RpcProxy                   Active  

SERVER1.domainname.com UMCallRouter               Active  

SERVER1.domainname.com XropProxy                  Active  

SERVER1.domainname.com HttpProxyAvailabilityGroup Active  

SERVER1.domainname.com ForwardSyncDaemon          Inactive  

SERVER1.domainname.com ProvisioningRps            Inactive  

SERVER1.domainname.com MapiProxy                  Active  

SERVER1.domainname.com EdgeTransport              Active  

SERVER1.domainname.com HighAvailability           Active  

SERVER1.domainname.com SharedCache                Active  

SERVER1.domainname.com MailboxDeliveryProxy       Active  

SERVER1.domainname.com RoutingUpdates             Active  

SERVER1.domainname.com RestProxy                  Active  

SERVER1.domainname.com DefaultProxy               Active  

SERVER1.domainname.com Lsass                      Active  

SERVER1.domainname.com RoutingService             Active  

SERVER1.domainname.com E4EProxy                   Active  

SERVER1.domainname.com CafeLAMv2                  Active  

SERVER1.domainname.com LogExportProvider          Active  

Everything looks fine?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

This is the error on all the databases in the DAG

SERVER1:  

Server 'SERVER1.domainname.com' component (HighAvailability) state is offline. If you need to activate databases copies on this server, you can use Set-ServerComponentState  

-Component 'HighAvailability' -State 'Active' and retry Move-ActiveMailboxDatabase.

```
There were database availability check failures for database 'SERVER1-MB02' that may be lowering its availability. Availability Count: 1. Expected Availability Count: 2. Detailed error(s):
```

When I check the status, it shows as active?

SERVER1.domainname.com HighAvailability Active

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Hi @Gavin Ross   ,    

Did you try to restart the mailbox replication service?    

Do you mean that this error occurs only when migrating to a new database? Successful when migrating to an existing database. I create a new database in Exchange hybrid environment, and it succeeded when I moved a mailbox to it. If possible, please try to create a another database and try to migrate again.    

If you run the following the first command to move only one mailbox, will there still be the same error? If so, run the second commands to view the detail report of the migration. Especially "ItemsTransferred", "PercentComplete" parameters, check whether the migration is in progress. If you migrate larger or more mailboxes, please wait patiently for some time. And check the specific report to see if there is any relevant information.    

```
New-MoveRequest -Identity <> -TargetDatabase “DB Name”  
Get-MoveRequest | Get-MoveRequestStatistics -IncludeReport | fl
```

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-05*

Hi @Gavin Ross   ,  

1.According to my research on “Stalledduetotarget_mdbreplication”, this value is also returned from Data Guarantee API on checking the replication health of the target database copies if they are a member of DAG and have database copies. We might get this message if the MRS service is waiting to get this information from the target server about the replication status of the database copies. Please run the following commands to check the status of database copy and the status of replication.

```
Get-MailboxDatabaseCopyStatus -Identity  | Format-List  
Test-ReplicationHealth
```

2.Please try to restart the mailbox replication service, then clear all move requests and create new move requests.  

3.Please run the following command to modifying the priority to highest:

```
New-MoveRequest -Identity <> -TargetDatabase “DB Name” -BatchName <> -Priority Highest
```

For more information : Exchange 2016 Migration Status

4.In addition, based on the research of similar cases, I found that some users use the following methods to disable MRS Resource Health, after which they can successfully migrate their mailboxes. It should be noted that after modifying the registry, we need to restart the computer for the modification to take effect.

Regedit -->find the key "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MSExchange ResourceHealth\MRS" --> set "MRS" REG_DWORD value from 1 to 0 --> Restart Exchange Mailbox Replication service

After migration is completed, we can revert back MRS value from 0 to 1 in regedit.  

In order to prevent the impact of incorrect modification, you could also back up your Regedit in advance: How to back up and restore the registry in Windows

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
