---
title: "Exchange 2010 to 2016 Public Folder Migration question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192227/exchange-2010-to-2016-public-folder-migration-ques
question_id: 192227
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2010 to 2016 Public Folder Migration question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192227/exchange-2010-to-2016-public-folder-migration-ques (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

The customer has 4 Exchange 2010 mailbox servers, each has a public folder database. We are at the end of the migration and need to migrate public folders over. I have done this a few times (2010 to 2013/16/O365) and it's easy enough. However, what the MS documentation doesn't tell you is how to deal with when you have 4 servers that have different counts of public folders.    

Looking at this: https://learn.microsoft.com/en-us/Exchange/collaboration/public-folders/batch-migration-from-previous-versions?redirectedfrom=MSDN&view=exchserver-2016     

When I run: .\Export-PublicFolderStatistics.ps1 <Folder to size map path> <FQDN of source server>    

I get a different answer from the machines. This means the public folders are not in sync / the same, across all 4 public folder databases.    

What would be the best way to fix this to allow us to migrate everything without missing things?    

Like I said, if this was a single server - or all 4 servers were in sync, then this would be easy. But as I am not overly familiar with 2010 public folders in general, I have no idea why they are out of sync and therefore what the best way to catch all data at the migration would be.    

Any help would be great.    

Cheers    

James

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-10*

You can also try New-PublicFolderDatabaseRepairRequest to fix corruption issue of those public database, then check the sync status again.    

Personally,  you can run the step 3 as official doc says on the Exchange 2010 server where Public Folder database is located to get full PublicFolder Statistics/size and see if you would get any error in step 5.     

The status shown in Get-MigrationBatch should be "synced" that indicates success.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-29*

Sorry notifications broke, so was not aware anyone had replied.  

I had tried the repair, but that didn't help sadly.  

We ended up exporting a bunch of stuff to PST and then deleting a lot of old stuff and only migrating minimal stuff over.  

Seems to be the common thing with legacy Exchange that has been about since 2003 or older.  

Thanks for your help guys.
