---
title: "Exchange Server almost out of disk space"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155282/exchange-server-almost-out-of-disk-space
question_id: 155282
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Exchange Server almost out of disk space

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155282/exchange-server-almost-out-of-disk-space (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are using Exchange 2016 and there is little disk space left for it's database.  

It seems that if we remove mailboxes, the respective disk space is not freed.  

It there a way to recover the disk space used by the deleted mailboxes?  

Or is there another way to free some disk space on the disk Exchange server is using?  

We are going to replace the almost full disks with bigger ones soon, but we are looking for an temporary solution.  

Thanks  

Costas

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-09*

I think it's the best way for you, it's offline defragmentation using ESEUTIL, because you don't have much space to create a new database.  

You will need a temporary space available to perform defragmentation, which can be a network share or a USB disk drive or other available space, equivalent to 110% of the database size. Of course, if it is not a local disk, the performance will not be as good.  

The bad news is that you need to dismount the database.  

I hope this helps you.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-09*

There is two possibilities  

You have to create new database and move all mailboxes to new Data base but if you have only 23 GB remaining so the only way out is offline database and defragment database .  

you can find  step by step guide to defragment database  

https://www.kerneldatarecovery.com/blog/remove-white-space-from-exchange-2013-database/#:~:text=STEPS%20TO%20PERFORM%20OFFLINE%20DEFRAG%20OF%20EXCHANGE%202013%20DATABASE&text=Run%20the%20command%20Dismount%2DDatabase,to%20defrag%20the%20dismounted%20database.  

Hope answer helps you if issue resolve please don't forget to accept answer .

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hello again,  

Currently our Exchange is left with 23 GB free space, out of 900 GB.  

Will Exchange use all of the available 23 GB until it reports it ran out of disk space?  

Or Exchange will report it ran out disk space before it consumes all available free space?  

Thanx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

@Επαμεινώνδας Γκαβέρας      

This phenomenon is related with Exchange database white space: when the mailbox is moved to the current database, the size of the database will increase, but the size of the database will not decrease when the mailbox is deleted, and this part of the database space will be occupied by white space. For more detailed information about white space, you can have a look about this blog: Database Maintenance in Exchange 2010 (Suitable for Exchange 2016)    

Here are some ways that you could to reclaim white space:    

    

According to your lab current situation, you may need to perform an offline defragmentation of the database using ESEUTIL.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
