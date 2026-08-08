---
title: "Moving mailbox to another Exchange server 2016 member gives error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191999/moving-mailbox-to-another-exchange-server-2016-mem
question_id: 1191999
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# Moving mailbox to another Exchange server 2016 member gives error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191999/moving-mailbox-to-another-exchange-server-2016-mem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moving mailbox to another Exchange server 2016 member gives error

Running command 

New-MoveRequest -Identity 'username' -TargetDatbase "DB01"

gives

```
Couldn't switch the mailbox into Sync Source mode.
This could be because of one of the following reasons:
  Another administrator is currently moving the mailbox.
  The mailbox is locked.
  The Microsoft Exchange Mailbox Replication service (MRS) doesn't have the correct permissions.
  Network errors are preventing MRS from cleanly closing its session with the Mailbox server. If this is the case, MRS may continue to encounter this error for up to 2 hours - this duration is controlled by
the TCP KeepAlive settings on the Mailbox server.
Wait for the mailbox to be released before attempting to move this mailbox again.
    + CategoryInfo          : NotSpecified: (:) [New-MoveRequest], RemoteTransientException
    + FullyQualifiedErrorId : [Server=L1PRDVES04030,RequestId=f8e35547-fdc7-463e-8503-926b5977d2e0,TimeStamp=3/21/2023 11:36:19 AM] [FailureCategory=Cmdlet-RemoteTransientException] 7BDCC377,Microsoft.Exchange
   .Management.Migration.MailboxReplication.MoveRequest.NewMoveRequest
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-22*

Hi @azhar Nasim,

-  Have you checked the above reasons for the failure of the move？If not, please check if any move request is running for the mailbox using the following command.

```
Get-MoveRequest -Identity ‘******@contoso.com’ | Get-MoveRequestStatistics –IncludeReport | fl
```

-  Please try restarting MRS on the server. Make sure it is running well and set to log in as an account with "Mailbox Move and Migrate Permissions". You can move the mailbox again after restarting.

-  Check whether other mailboxes can be moved normally, if the problem only exists in the current mailbox, we suggest you export the mailbox data to a pst file and try to fix the mailbox or create a new one to enable it.

Run Mailbox Repair Request:

```
New-MailboxRepairRequest -Mailbox  -CorruptionType ProvisionedFolder,SearchFolder,AggregateCounts,Folderview
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
