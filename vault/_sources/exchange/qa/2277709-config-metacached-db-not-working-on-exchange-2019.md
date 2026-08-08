---
title: "Config MetaCached DB not working on Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277709/config-metacached-db-not-working-on-exchange-2019
question_id: 2277709
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Config MetaCached DB not working on Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277709/config-metacached-db-not-working-on-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I'm configuring metacache databases on our new Exchange 2019 servers.  

We've got 2 seperate disks available for them.

I used the official Microsoft documentation, but it seems to be missing some important info.

https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/metacachedatabase-setup#prerequisites

Done so far :

-  Configured DAG  

-  Configured autoreseed  

-  brought both SSD's for metacache DB online (did not format them)  

-  ran the powershell cmdlets 

I ran it in verbose mode and see the scripts formatting the disks and perform the other actions.  

I didn't get any errors in these activations, so i performed DB failovers to trigger the creation.

Done on all 4 servers

Unfortunately afterwards when I check to see if it works I get :

PS C:\scripts> Get-MailboxDatabaseCopyStatus | fl meta*

MetaCacheDatabaseStatus        : StorageOffline  

MetaCacheDatabaseStatusMessage : Directory 'C:\ExDatabases\DAG2019-DB1' is not configured as a mountpoint.  

MetaCacheDatabaseFilePath      : C:\ExchangeMetaCacheDbs\DAG2019-DB1\DAG2019-DB1.mcdb\DAG2019-DB1-mcdb.edb

MetaCacheDatabaseLastReset     :

It seems that I need to manually create the mountpoints then? But to which location should I map them ? And especially since I have 2 caching SSD disks?

## Answers

_No answers on this thread._
