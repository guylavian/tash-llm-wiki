---
title: "Exchange 2016 DAG Logfile error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/248717/exchange-2016-dag-logfile-error
question_id: 248717
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 DAG Logfile error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/248717/exchange-2016-dag-logfile-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I Have two DAG members in Exchange 2016 with 3 DB, MB01, MB02, and MB03.  

MBO3 Active Copy of First Server gives below error in ECP:  

"The Microsoft Exchange Replication service encountered an error while inspecting the logs and database for MB03\EXC01 on startup. Error: File check failed: Logfile 'G:\MB03-Log\E0300000004.log' was not found."  

Is it an urgent problem? What must I do to solve this?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-30*

Thank you, Andy David.  

Is there a risk of doing this process on Exchange? I am not so Experienced so should I be irritated?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-30*

See my previous question:    

Are you running any anti-virus software on those servers? If so, make sure you are excluding the correct things    

https://learn.microsoft.com/en-us/exchange/antispam-and-antimalware/windows-antivirus-software?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-30*

Hello,  

The log file "G:\MB03-Log\E0300000004.log" is not there really, it is lost. All filenames in that directory like "E03000007**.log" .

The Get-MailboxDatabaseCopyStatus command results below:

C:\Windows\system32>Get-MailBoxDatabaseCopyStatus -Identity Mb03 | Format-List  

RunspaceId : 5e6203c2-9a86-47ee-b1a0-0af820df28ab  

Identity : MB03\EXC01  

Id : MB03\EXC01  

Name : MB03\EXC01  

DatabaseName : MB03  

Status : FailedAndSuspended  

InstanceStartTime : 1/23/2021 4:26:57 AM  

LastStatusTransitionTime : 9/14/2020 10:41:14 AM  

InternalStartupMessage : StartupFailed  

InternalStartupMessageTimeUtc : 1/23/2021 1:26:58 AM  

MailboxServer : EXC01  

ActiveDatabaseCopy : EXC02  

ActiveCopy : False  

ActivationPreference : 1  

StatusRetrievedTime : 1/30/2021 3:08:13 PM  

WorkerProcessId : 18348  

IsLastCopyAvailabilityChecksPassed : False  

LastCopyAvailabilityChecksPassedTime : 9/10/2020 4:12:42 PM  

LastCopyAvailabilityCheckFailedID : DatabaseCheckPassiveCopyStatusIsOkForAvailability  

LastCopyAvailabilityCheckFailedErrorMsg : Database copy 'MB03' is in a Failed state on server 'EXC01'. Reason: The  

Microsoft Exchange Replication service encountered an error while inspecting  

the logs and database for MB03\EXC01 on startup. Error: File check failed :  

Logfile 'G:\MB03-Log\E0300000004.log' was not found.  

. If you need to activate this database copy, you can use the  

Move-ActiveMailboxDatabase cmdlet with the -SkipHealthChecks parameter to  

forcibly activate the database copy.  

IsLastCopyRedundancyChecksPassed : False  

LastCopyRedundancyChecksPassedTime : 9/10/2020 4:12:42 PM  

LastCopyRedundancyCheckFailedID : DatabaseCheckPassiveCopyStatusIsOkForRedundancy  

LastCopyRedundancyCheckFailedErrorMsg : Passive database copy 'MB03\EXC01' has an unhealthy status  

'FailedAndSuspended' for duration 138.04:26:47.5008824. [SuspendComment: The  

database copy was automatically suspended due to failure item processing  

having failure item tag Reseed. At '9/14/2020 10:41:14 AM' the copy of  

'MB03' on this server experienced an error that requires it be reseeded. For  

more detail about this failure, consult the Event log on the server for  

other storage and "ExchangeStoreDb" events. The passive database copy has  

been suspended.  

] [ErrorMessage: The Microsoft Exchange Replication service encountered an  

error while inspecting the logs and database for MB03\EXC01 on startup.  

Error: File check failed : Logfile 'G:\MB03-Log\E0300000004.log' was not  

found.  

].  

ActivationSuspended : False  

ActionInitiator : Service  

ErrorMessage : The Microsoft Exchange Replication service encountered an error while  

inspecting the logs and database for MB03\EXC01 on startup. Error: File  

check failed : Logfile 'G:\MB03-Log\E0300000004.log' was not found.  

ErrorEventId : 2070  

ExtendedErrorInfo : Microsoft.Exchange.Cluster.Replay.FileCheckLogfileMissingException: File  

check failed : Logfile 'G:\MB03-Log\E0300000004.log' was not found.  

at Microsoft.Exchange.Cluster.Replay.FileChecker.CheckLogfiles(Int64  

minimumGeneration, Int64 maximumGeneration, LogRepair repair)  

at Microsoft.Exchange.Cluster.Replay.FileChecker.RunChecks(LogRepair  

repair, Boolean forceDeleteCheckPointFile)  

at Microsoft.Exchange.Cluster.Replay.TargetReplicaInstance.ConfigurationCh  

eckerInternal()  

at Microsoft.Exchange.Cluster.Replay.ReplicaInstance.<ConfigurationChecker

b__31_0()

SuspendComment : The database copy was automatically suspended due to failure item processing  

having failure item tag Reseed. At '9/14/2020 10:41:14 AM' the copy of  

'MB03' on this server experienced an error that requires it be reseeded. For  

more detail about this failure, consult the Event log on the server for  

other storage and "ExchangeStoreDb" events. The passive database copy has  

been suspended.  

RequiredLogsPresent :  

SinglePageRestore : 0  

ContentIndexState : Suspended  

ContentIndexErrorMessage :  

ContentIndexErrorCode : 0  

ContentIndexVersion :  

ContentIndexCrawlVersion :  

ContentIndexBacklog :  

ContentIndexRetryQueueSize :  

ContentIndexMailboxesToCrawl :  

ContentIndexSeedingPercent :  

ContentIndexSeedingSource :  

ContentIndexServerSource :  

SeedingSourceForDB : False  

SeedingSourceForCI : False  

SeedingThrottleStatus :  

RecentServerCpuPercentage : 13  

RecentServerCpuPercentageFloat : 13.17299  

IsFileModeReplicationBeingThrottled : False  

RecentDiskReadLatencyMs : 0  

RecentDiskReadsPerSec : 0  

RecentDiskWriteLatencyMs : 0  

RecentDiskWritesPerSec : 0  

CopyQueueLength : 124661  

ReplayQueueLength : 0  

ReplaySuspended : False  

ResumeBlocked : False  

ReseedBlocked : False  

InPlaceReseedBlocked : False  

MinimumSupportedDatabaseSchemaVersion : 0.121  

MaximumSupportedDatabaseSchemaVersion : 0.174  

RequestedDatabaseSchemaVersion :  

LatestAvailableLogTime : 9/10/2020 4:36:55 PM  

LastCopyNotificationedLogTime : 9/10/2020 4:36:55 PM  

LastCopiedLogTime : 9/10/2020 4:13:18 PM  

LastInspectedLogTime : 9/10/2020 4:13:18 PM  

LastReplayedLogTime : 9/10/2020 4:13:18 PM  

CurrentReplayLogTime : 9/10/2020 4:13:18 PM  

LastLogGenerated : 593927  

LastLogCopyNotified : 469268  

LastLogCopied : 469266  

LastLogInspected : 469266  

LastLogReplayed : 469266  

LowestLogPresent : 0  

LastLogInfoIsStale : False  

LastLogInfoFromCopierTime :  

LastLogInfoFromClusterTime : 1/30/2021 3:07:16 PM  

LastLogInfoFromClusterGen : 593927  

ReplicationIsInBlockMode : False  

ReplicationIsInScavengeMode : False  

ActivationDisabledAndMoveNow : False  

AutoActivationPolicy : Unrestricted  

LogsReplayedSinceInstanceStart : 0  

LogsCopiedSinceInstanceStart : 0  

LatestFullBackupTime : 8/31/2020 11:02:21 PM  

LatestIncrementalBackupTime :  

LatestDifferentialBackupTime :  

LatestCopyBackupTime :  

SnapshotBackup : True  

SnapshotLatestFullBackup : True  

SnapshotLatestIncrementalBackup :  

SnapshotLatestDifferentialBackup :  

SnapshotLatestCopyBackup :  

LogReplayQueueIncreasing : False  

LogCopyQueueIncreasing : False  

ReplayLagStatus : Enabled:False; PlayDownReason:None; ReplaySuspendReason:None; Percentage:0;  

Configured:00:00:00; MaxDelay:1.00:00:00; Actual:141.22:54:54  

DatabaseSeedStatus :  

OutstandingDumpsterRequests : {}  

OutgoingConnections :  

IncomingLogCopyingNetwork :  

SeedingNetwork :  

DiskFreeSpacePercent : 78  

DiskFreeSpace : 1.572 TB (1,728,485,810,176 bytes)  

DiskTotalSpace : 2 TB (2,198,886,936,576 bytes)  

ExchangeVolumeMountPoint :  

DatabaseVolumeMountPoint : G:\  

DatabaseVolumeName : \?\Volume{82286277-a68e-4291-9718-d00d2ac55533}\  

DatabasePathIsOnMountedFolder : False  

LogVolumeMountPoint : G:\  

LogVolumeName : \?\Volume{82286277-a68e-4291-9718-d00d2ac55533}\  

LogPathIsOnMountedFolder : False  

LastDatabaseVolumeName :  

LastDatabaseVolumeNameTransitionTime :  

VolumeInfoError :  

MaxLogToReplay : 0  

IsPrimaryActiveManager : False  

IsActiveManagerRoleUnknown : False  

MetaCacheDatabaseStatus : Disabled  

MetaCacheDatabaseFilePath :  

MetaCacheDatabaseLastReset :  

LowestRequiredLog : 0  

HighestRequiredLog : 0  

IsValid : True  

ObjectState : Unchanged  

RunspaceId : 5e6203c2-9a86-47ee-b1a0-0af820df28ab  

Identity : MB03\EXC02  

Id : MB03\EXC02  

Name : MB03\EXC02  

DatabaseName : MB03  

Status : Mounted  

InstanceStartTime : 1/14/2021 6:08:56 PM  

LastStatusTransitionTime :  

InternalStartupMessage : StartupSucceeded  

InternalStartupMessageTimeUtc : 1/14/2021 3:08:56 PM  

MailboxServer : EXC02  

ActiveDatabaseCopy : EXC02  

ActiveCopy : True  

ActivationPreference : 2  

StatusRetrievedTime : 1/30/2021 3:08:13 PM  

WorkerProcessId : 5720  

IsLastCopyAvailabilityChecksPassed : True  

LastCopyAvailabilityChecksPassedTime : 1/30/2021 3:07:55 PM  

LastCopyAvailabilityCheckFailedID : None  

LastCopyAvailabilityCheckFailedErrorMsg :  

IsLastCopyRedundancyChecksPassed : True  

LastCopyRedundancyChecksPassedTime : 1/30/2021 3:07:55 PM  

LastCopyRedundancyCheckFailedID : None  

LastCopyRedundancyCheckFailedErrorMsg :  

ActivationSuspended : False  

ActionInitiator : Service  

ErrorMessage :  

ErrorEventId :  

ExtendedErrorInfo :  

SuspendComment :  

RequiredLogsPresent :  

SinglePageRestore : 0  

ContentIndexState : Healthy  

ContentIndexErrorMessage :  

ContentIndexErrorCode : 1  

ContentIndexVersion : 22  

ContentIndexCrawlVersion : 0  

ContentIndexBacklog : 18  

ContentIndexRetryQueueSize : 0  

ContentIndexMailboxesToCrawl :  

ContentIndexSeedingPercent :  

ContentIndexSeedingSource :  

ContentIndexServerSource :  

SeedingSourceForDB : False  

SeedingSourceForCI : False  

SeedingThrottleStatus :  

RecentServerCpuPercentage : 9  

RecentServerCpuPercentageFloat : 9.32403  

IsFileModeReplicationBeingThrottled : False  

RecentDiskReadLatencyMs : 0.3333333  

RecentDiskReadsPerSec : 2.266667  

RecentDiskWriteLatencyMs : 0  

RecentDiskWritesPerSec : 2.05  

CopyQueueLength : 0  

ReplayQueueLength : 0  

ReplaySuspended : False  

ResumeBlocked : False  

ReseedBlocked : False  

InPlaceReseedBlocked : False  

MinimumSupportedDatabaseSchemaVersion : 0.121  

MaximumSupportedDatabaseSchemaVersion : 0.174  

RequestedDatabaseSchemaVersion :  

LatestAvailableLogTime :  

LastCopyNotificationedLogTime : 1/30/2021 3:06:57 PM  

LastCopiedLogTime :  

LastInspectedLogTime :  

LastReplayedLogTime :  

CurrentReplayLogTime :  

LastLogGenerated : 593927  

LastLogCopyNotified : 593927  

LastLogCopied : 0  

LastLogInspected : 0  

LastLogReplayed : 0  

LowestLogPresent : 468365  

LastLogInfoIsStale : False  

LastLogInfoFromCopierTime : 1/30/2021 3:08:13 PM  

LastLogInfoFromClusterTime : 1/30/2021 3:07:16 PM  

LastLogInfoFromClusterGen : 593927  

ReplicationIsInBlockMode : True  

ReplicationIsInScavengeMode : False  

ActivationDisabledAndMoveNow : False  

AutoActivationPolicy : Unrestricted  

LogsReplayedSinceInstanceStart : 0  

LogsCopiedSinceInstanceStart : 0  

LatestFullBackupTime : 9/9/2020 11:02:12 PM  

LatestIncrementalBackupTime :  

LatestDifferentialBackupTime :  

LatestCopyBackupTime :  

SnapshotBackup : True  

SnapshotLatestFullBackup : True  

SnapshotLatestIncrementalBackup :  

SnapshotLatestDifferentialBackup :  

SnapshotLatestCopyBackup :  

LogReplayQueueIncreasing : False  

LogCopyQueueIncreasing : False  

ReplayLagStatus : Enabled:False; PlayDownReason:None; ReplaySuspendReason:None; Percentage:0;  

Configured:00:00:00; MaxDelay:1.00:00:00; Actual:00:00:00  

DatabaseSeedStatus :  

OutstandingDumpsterRequests : {}  

OutgoingConnections : {}  

IncomingLogCopyingNetwork :  

SeedingNetwork :  

DiskFreeSpacePercent : 68  

DiskFreeSpace : 1.377 TB (1,514,056,859,648 bytes)  

DiskTotalSpace : 2 TB (2,198,886,936,576 bytes)  

ExchangeVolumeMountPoint :  

DatabaseVolumeMountPoint : G:\  

DatabaseVolumeName : \?\Volume{2f483481-d4ad-45ad-b840-465cc2f8bd86}\  

DatabasePathIsOnMountedFolder : False  

LogVolumeMountPoint : G:\  

LogVolumeName : \?\Volume{2f483481-d4ad-45ad-b840-465cc2f8bd86}\  

LogPathIsOnMountedFolder : False  

LastDatabaseVolumeName :  

LastDatabaseVolumeNameTransitionTime :  

VolumeInfoError :  

MaxLogToReplay : 0  

IsPrimaryActiveManager : True  

IsActiveManagerRoleUnknown : False  

MetaCacheDatabaseStatus : Disabled  

MetaCacheDatabaseFilePath :  

MetaCacheDatabaseLastReset :  

LowestRequiredLog : 0  

HighestRequiredLog : 0  

IsValid : True  

ObjectState : Unchanged

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-29*

Hi,    

Check the storage location, is the log file missing? Did you manually delete it?    

Run the following command to check the mailbox database copy status and post the result:    

```
Get-MailboxDatabaseCopyStatus -Identity DB1 | Format-List
```

Can you find any related error in Event log?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
