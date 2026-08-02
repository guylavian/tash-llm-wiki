---
title: "Microsoft Exchange 2010 to 2016 migration - mailbox move slow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126746/microsoft-exchange-2010-to-2016-migration-mailbox
question_id: 126746
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Microsoft Exchange 2010 to 2016 migration - mailbox move slow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126746/microsoft-exchange-2010-to-2016-migration-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

I am moving some mailboxes from an Exchange 2010 to 2016 server and I am getting very slow transfer speeds (2mb/minute) - it took over 5 hours to move a 2gb mailbox.  

I have tried the usual things (changing the config file for the MRS service, importing registry keys, rebooting the server) and i just cannot get these moves to go any quicker.  

Has anyone else got any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-15*

HI there  

I have added in the registry key with no success in speed change  

This is the output of one of the commands  

RunspaceId : a65e6255-01fc-4484-a4a3-85824b026a05  

MailboxIdentity : xxx.local/Hosting/FC2/SCOC/xx  

DistinguishedName : CN=xx,OU=SCOC,OU=FC2,OU=Hosting,DC=xxx,DC=local  

DisplayName : xx  

Alias : xx  

ExchangeGuid : 490a1ff7-1e42-48b1-bfa4-c358b96697c8  

ArchiveGuid :  

Status : InProgress  

StatusDetail : CopyingMessages  

SyncStage : LoadingMessages  

Flags : IntraOrg, Pull, HighPriority  

RequestStyle : IntraOrg  

Direction : Pull  

IsOffline : False  

Protect : False  

DoNotPreserveMailboxSignature : True  

Priority : Emergency  

WorkloadType : Local  

Suspend : False  

SuspendWhenReadyToComplete : False  

IgnoreRuleLimitErrors : False  

RecipientTypeDetails : UserMailbox  

SourceVersion : Version 14.3 (Build 409.0)  

SourceDatabase : xxxExchDBUn03  

SourceServer : FTGH-EXCH01.xxx.local  

TargetVersion : Version 15.1 (Build 1979.0)  

TargetDatabase : xxxExch02DB09  

TargetServer : FTGH-Exch02.xxx.local  

SourceArchiveDatabase :  

SourceArchiveVersion :  

SourceArchiveServer :  

TargetArchiveDatabase :  

TargetArchiveVersion :  

TargetArchiveServer :  

RemoteHostName :  

RemoteGlobalCatalog :  

BatchName :  

StartAfter :  

CompleteAfter :  

EffectiveIncrementalSyncInterval : 00:15:00  

ConfiguredIncrementalSyncInterval :  

RemoteCredentialUsername :  

RemoteDatabase :  

RemoteDatabaseName :  

RemoteArchiveDatabase :  

RemoteArchiveDatabaseName :  

TargetDeliveryDomain :  

ArchiveDomain :  

BadItemLimit : 0  

BadItemsEncountered : 0  

LargeItemLimit : 0  

LargeItemsEncountered : 0  

AllowLargeItems : True  

QueuedTimestamp : 16/10/2020 8:33:08 AM  

StartTimestamp : 16/10/2020 8:33:41 AM  

LastUpdateTimestamp : 16/10/2020 8:33:49 AM  

LastSuccessfulSyncTimestamp :  

InitialSeedingCompletedTimestamp :  

FinalSyncTimestamp :  

CompletionTimestamp :  

SuspendedTimestamp :  

OverallDuration : 00:05:27.1008444  

TotalSuspendedDuration : 00:00:00  

TotalFailedDuration : 00:00:00  

TotalQueuedDuration : 00:00:02.4281849  

TotalInProgressDuration : 00:05:24.6766597  

TotalStalledDueToContentIndexingDuration : 00:00:00  

TotalStalledDueToMdbReplicationDuration : 00:00:00  

TotalStalledDueToMailboxLockedDuration : 00:00:00  

TotalStalledDueToReadThrottle : 00:00:00  

TotalStalledDueToWriteThrottle : 00:00:00  

TotalStalledDueToReadCpu : 00:00:00  

TotalStalledDueToWriteCpu : 00:00:00  

TotalStalledDueToReadUnknown : 00:00:00  

TotalStalledDueToWriteUnknown : 00:00:00  

TotalTransientFailureDuration : 00:00:00  

TotalIdleDuration : 00:00:00  

MRSServerName : FTGH-Exch02.xxx.local  

TotalMailboxSize : 5.294 GB (5,684,054,577 bytes)  

TotalMailboxItemCount : 43662  

TotalArchiveSize :  

TotalArchiveItemCount :  

BytesTransferred : 13.48 MB (14,132,917 bytes)  

BytesTransferredPerMinute : 0 B (0 bytes)  

ItemsTransferred : 187  

PercentComplete : 25  

CompletedRequestAgeLimit : 3650.00:00:00  

PositionInQueue :  

InternalFlags : SkipFolderPromotedProperties,SkipKnownCorruptions,JobFeaturesComputed  

FailureCode :  

FailureType :  

FailureSide :  

Message :  

FailureTimestamp :  

IsValid : True  

ValidationMessage :  

RequestGuid : c826d997-2711-4614-9b37-0d36aaa373f8  

RequestQueue : xxxExch02DB09  

MigrationMailboxGuid :  

SourceEndpointGuid :  

Identity : xxx.local/Hosting/FC2/SCOC/xx  

DiagnosticInfo :  

Report : 16/10/2020 8:33:08 AM [FTGH-Exch02] 'xxx.local/Users/xxxadmin'  

created move request.  

16/10/2020 8:33:10 AM [FTGH-Exch02] The Microsoft Exchange Mailbox  

Replication service 'FTGH-Exch02.xxx.local' (15.1.1979.3  

caps:3FFFFF) is examining the request.  

16/10/2020 8:33:10 AM [FTGH-Exch02] Connected to target mailbox  

'490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)', database  

'xxxExch02DB09', Mailbox server 'FTGH-Exch02.xxx.local'  

Version 15.1 (Build 1979.0).  

16/10/2020 8:33:10 AM [FTGH-Exch02] Sync state for request  

c826d997-2711-4614-9b37-0d36aaa373f8 is null.  

16/10/2020 8:33:10 AM [FTGH-Exch02] Connected to source mailbox  

'490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)', database  

'xxxExchDBUn03', Mailbox server 'FTGH-EXCH01.xxx.local'  

Version 14.3 (Build 409.0).  

16/10/2020 8:33:10 AM [FTGH-Exch02] Request processing started.  

16/10/2020 8:33:10 AM [FTGH-Exch02] Source mailbox information:  

Regular Items: 42546, 5.268 GB (5,656,348,265 bytes)  

Regular Deleted Items: 908, 26.42 MB (27,706,312 bytes)  

FAI Items: 208, 0 B (0 bytes)  

FAI Deleted Items: 0, 0 B (0 bytes)  

16/10/2020 8:33:11 AM [FTGH-Exch02] Cleared sync state for request  

490a1ff7-1e42-48b1-bfa4-c358b96697c8 due to 'CleanupOrphanedMailbox'.  

16/10/2020 8:33:11 AM [FTGH-Exch02] An old copy of the mailbox was removed  

from the destination database. The operation will try again in 30 seconds.  

16/10/2020 8:33:41 AM [FTGH-Exch02] Mailbox signature will not be preserved  

for mailbox '490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)'. Outlook  

clients will need to restart to access the moved mailbox.  

16/10/2020 8:33:41 AM [FTGH-Exch02] Stage: CreatingFolderHierarchy. Percent  

complete: 10.  

16/10/2020 8:33:41 AM [FTGH-Exch02] Initializing folder hierarchy from  

mailbox '490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)': 97 folders total.  

16/10/2020 8:33:41 AM [FTGH-Exch02] Folder creation progress: 0 folders  

created in mailbox '490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)'.  

16/10/2020 8:33:47 AM [FTGH-Exch02] Folder hierarchy initialized for  

mailbox '490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)': 96 folders  

created.  

16/10/2020 8:33:47 AM [FTGH-Exch02] Stage: CreatingFolderHierarchy. Percent  

complete: 10.  

16/10/2020 8:33:47 AM [FTGH-Exch02] Stage: CreatingInitialSyncCheckpoint.  

Percent complete: 15.  

16/10/2020 8:33:48 AM [FTGH-Exch02] Initial sync checkpoint progress: 0/97  

folders processed. Currently processing mailbox  

'490a1ff7-1e42-48b1-bfa4-c358b96697c8 (Primary)'.  

16/10/2020 8:33:49 AM [FTGH-Exch02] Initial sync checkpoint completed: 90  

folders processed.  

16/10/2020 8:33:49 AM [FTGH-Exch02] Stage: LoadingMessages. Percent  

complete: 20.  

16/10/2020 8:33:49 AM [FTGH-Exch02] Stage: LoadingMessages. Percent  

complete: 20.  

LastFailure :  

RequestExpiryTimestamp : 21/09/2120 7:33:08 PM  

IsSyncAggregation : False  

IsShadowSync : False  

ObjectState : New

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-15*

Hi anonymous user,    

Network speed and server resources also come into play when moving mailboxes, so please make sure the network speed is fast and the server resources are abundant.     

Then aside from the possible solutions you have mentioned, it's also suggested to try temporarily disabling content indexing on the target database and see if there could be any improvement:    

```
Set-MailboxDatabase  -IndexEnabled:$False
```

Besides, you can use the "-Priority" parameter with value "emergency" on the mailbox moves to give the move the highest priority in the MRS queue:    

```
New-MoveRequest -Identity "******@contoso.com" -TargetDatabase “DB1” -Priority emergency
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
