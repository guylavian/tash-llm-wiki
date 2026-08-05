---
title: "error id 1100 exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324124/error-id-1100-exchange-2019
question_id: 324124
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# error id 1100 exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324124/error-id-1100-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

We installed exchange server 2019 "new installation " on two server and build DAG. I moved default mailboxes "health, arbitration" database to another database and then delete default database. Now i have error 1100 on both exchange servers:

Request 'DB#902acbb7-4c10-4516-b1a9-cdc3e9652e11\049cfac9-fc86-4357-a65b-e2b734d9dca0' (049cfac9-fc86-4357-a65b-e2b734d9dca0) failed.  

Error code: -2146233088  

This mailbox exceeded the maximum number of corrupt or missing items that were specified for this request.

Context:

>>> Scheduled WorkItems: CopyFolder_Working Set(P:1154,R:0,S:0,C:19); CopyFolder_Recoverable Items(P:1173,R:0,S:0,C:18); CopyFolder_Calendar Logging(P:1191,R:0,S:0,C:20); CopyFolder_Deletions(P:1212,R:0,S:0,C:25); CopyFolder_Purges(P:1237,R:0,S:0,C:18); CopyFolder_Versions(P:1256,R:0,S:0,C:19); CopyMailboxProperties(P:1275,R:0,S:0,C:154); FinalizeMerge(P:1431,R:0,S:0,C:1); TargetContentVerification(P:1,R:0,S:0,C:41,Cnt=22); TargetContentVerification(P:301,R:0,S:0,C:9)

i run the following commands:

Get-MoveRequest -MoveStatus InProgress  

Get-MoveRequest | Get-MoveRequestStatistics

but there is no result. I checked ADSI for the removed default database, but it was't there.

what else i have to check in order to solve this error.

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Hi @HamoudaAlbakri-3924    

When did you receive the error information, after migrating the mailboxes or deleting the mailbox database?    

You may try setting the -BadItemLimit for the move request.    

Set-MoveRequest    

The BadItemLimit parameter specifies the maximum number of bad items that are allowed before the request fails. A bad item is a corrupt item in the source mailbox that can't be copied to the target mailbox. Also included in the bad item limit are missing items. Missing items are items in the source mailbox that can't be found in the target mailbox when the request is ready to complete.    

Valid input for this parameter is an integer or the value unlimited. The default value is 0, which means the request will fail if any bad items are detected. If you are OK with leaving a few bad items behind, you can set this parameter to a reasonable value (we recommend 10 or lower) so the request can proceed. If too many bad items are detected, consider using the New-MailboxRepairRequest cmdlet to attempt to fix corrupted items in the source mailbox, and try the request again.    

Get-Moverequest <identity> | Set-Moverequest –baditemlimit <input value>    

Resume-Moverequest <identity>    

And a related thread which discussed about Remove a Database that is part of a DAG for your reference as well    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
