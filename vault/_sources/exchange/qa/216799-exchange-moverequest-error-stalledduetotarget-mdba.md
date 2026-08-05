---
title: "Exchange moverequest error - StalledDueToTarget_MdbAvailability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216799/exchange-moverequest-error-stalledduetotarget-mdba
question_id: 216799
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor"]
---
# Exchange moverequest error - StalledDueToTarget_MdbAvailability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216799/exchange-moverequest-error-stalledduetotarget-mdba (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

While trying to move a mailbox to another database with the command new-moverequest, the job remains stuck in state :    

StalledDueToTarget_MdbAvailability    

I would like to know, how to resolve this issue, please?    

    

PS:    

We an Exchange 2016 CU15 dag, of two nodes.    

When i run test-replicationhealth, all checks are passed correctly,    

When i run get-mailboxdatabasecopystatus * everything is in normal state (mounted or healthy)    

Thank you in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-05*

Hi @LotfiBOUCHERIT-4930   

Thank you for sharing the logs. Error message found in the log is StalledDueToSource_MailboxCapacityExceeded. Based on my research, it looks like some issue with the source server and the solution is to restart the server.  

https://social.technet.microsoft.com/Forums/ie/en-US/3d3d2865-de88-4e2a-b143-a423b8ec29da/cannot-move-archive-mailbox-to-other-database-status-detail?forum=Exch2016Adm  

Earlier you have also mentioned that another mailbox moved. So it looks like issue could be with this specific mailbox.  

If the above suggestion helps, please click on "Accept Answer" and upvote it

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-04*

Hello @Anonymous       

The command is : new-MoveRequest USER -TargetDatabase DB_16_500M -CompleteAfter 1    

Tested moverequest for a second user, with larger mailbox (the first one was 0,3G the second one is 1,4G), it did give in first place the same status (StalledDueTo...), but it worked later.    

But the fist mailbox did not change anything    

@Ashok M    : no, it is not a batch move, a single mailbox that needs more space, and about Content Indexes, are healthy

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-04*

Hi @LotfiBOUCHERIT-4930 ,    

In addition to what AshokM said, I want to ask some questions for a further troubleshooting:    

Are you moving this mailbox to the other DAG member database?      

Besides, can you share the new-moverequest command you use?    

Are there any logs generated in Event Log when this happened? If so, please share with us.    

After research, I found an explanation about this issue in: Troubleshooting Slow Migrations     

StalledDueToTarget_MdbAvailability: the move monitors replay queue of transactions logs into remote copies of databases. Migration stalls when the queue gets too big and will last until it drains.    

This article is about Exchange Online Migration, but it also has some things in common with on-premise Exchange. We may pay attention to these parts mentioned in this article:    

    

To eliminate these possible causes, I recommend you to move a new mailbox by using the New-MoveRequest, and specify a new database as the target.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-03*

Hi @LotfiBOUCHERIT-4930,  

Could you please try the below,  

1.If this is caused while running a migration batch, then please try moving a single mailbox to that target database  

2.Is ContentIndexState healthy for the target database?  

Can you share Get-MoveRequest | Get-MoveRequestStatistics -IncludeReport | fl to check for InnerException (Please remove personal information while sharing)  

If the above suggestion helps, please click on "Accept Answer" and upvote it

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-03*

Hi @LotfiBOUCHERIT-4930   

At high level with your error and test results / status .. It can be target server side Disk LAtency.  

You can once try to ---  restart the MSExchangeMailboxReplication service  

===Further Steps===  

 Move a single mailbox by using the New-MoveRequest  

New-MoveRequest  

For troubleshooting this migration error, you should first try to move a single mailbox by using the New-MoveRequest. Don’t hesitate to specify the target mailbox as a new one.  

This should work if the issue was indeed caused by a database copy.  

-  Increase the number of simultaneous mailbox moves  

MSExchangeMailboxReplication.exe.config  

Open Explorer on the Exchange server.  

Go to C:Program FilesMicrosoftExchange ServerV14Bin. This is the default path; the path on your server might be different.  

Make a backup copy of the file MSExchangeMailboxReplication.exe.config.  

Open MSExchangeMailboxReplication.exe.config.  

Then, find the following part in the file:  

<MRSConfiguration  

MaxRetries = “60”  

MaxCleanupRetries = “5”  

MaxStallRetryPeriod = “00:15:00”  

RetryDelay = “00:00:30”  

MaxMoveHistoryLength = “2”  

MaxActiveMovesPerSourceMDB = “5”  

MaxActiveMovesPerTargetMDB = “2”  

MaxActiveMovesPerSourceServer = “50”  

MaxActiveMovesPerTargetServer = “5”  

MaxTotalMovesPerMRS = “100”  

FullScanMoveJobsPollingPeriod = “00:10:00”  

MinimumTimeBeforePickingJobsFromSameDatabase = “00:00:04”  

ServerCountsNotOlderThan = “00:10:00”  

MRSAbandonedMoveJobDetectionTime = “01:00:00”  

BackoffIntervalForProxyConnectionLimitReached = “00:30:00”  

DataGuaranteeCheckPeriod = “00:00:10”  

DataGuaranteeTimeout = “00:30:00”  

DataGuaranteeLogRollDelay = “00:01:00”  

EnableDataGuaranteeCheck = “true”  

DisableMrsProxyCompression = “false”  

DisableMrsProxyBuffering = “false”  

MinBatchSize = “100”  

MinBatchSizeKB = “256” />  

</configuration>  

Change these parameters to fix the error:  

MaxActiveMovesPerSourceMDB = “5”  

MaxActiveMovesPerTargetMDB = “2”  

MaxActiveMovesPerSourceServer = “50”  

MaxActiveMovesPerTargetServer = “5”  

MaxTotalMovesPerMRS = “100”  

Use the following command: Restart-Service MSExchangeMailboxReplication to restart the Mailbox Replication service and keep the changes.  

If you see the migration error after successfully moving a few mailboxes, then it may be caused by a limit for the number of simultaneous mailbox moves.  

Increase it by modifying some parameters’ value in MSExchangeMailboxReplication.exe.config file  

(If this reply was helpful please don't forget to Upvote and/or Accept as an answer, Thank You)  

Regards,  

J.D.  

Disclaimer: This posting is provided "AS IS" with no warranties or guarantees, and confers no rights.
