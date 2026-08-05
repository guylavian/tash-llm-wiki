---
title: "Exchange 2013 database full"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278453/exchange-2013-database-full
question_id: 278453
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 database full

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278453/exchange-2013-database-full (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, Hope you can give me a hand with this problem. My exchange database is so big that I can not defrag it on the same disk (the sice is 350GB and free space is 37GB). I have an external NAS with enough space. Would it be possible to defrag using eseutil and use that NAS as temporary destination???. If so, could you please send me commands to do that?. If not, any idea???? Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Thanks for all you replies. They have been very helpful.  

After all, what I decided is (and I have some doubts):  

1.- Create a new database on another internal hard disk  

2.- Move mailboxes to the new database  

3.- Once all mailboxes are moved, copy database to the original folder (where it was the old one). But at this point, how do I tell exchange server that the new database will be the correct one?  

Or I do have another idea:  

1.- Use eseutil and an internal hard disk as a temporary folder. But my question is, that temporary folder will contain the new database and the old one will be deleted?. Or do I have to do everything manually (I mean, delete the old one and copy the one on the hard disk).  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

@Juanma Gómez      

This article introduce about Exchange database whitespace:    

    

84M is not a problem, if there has a lot of white space after the mailbox is migrated, you can just use the above methods to release it.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-18*

Its better to bring up a new database and move the mailboxes to it and remove the old database  

If that is not possible,   

How much white space is available? You should know that before doing any offline defrag. You will need to take the database offline and check with eseutil to know the true amount with ESEUTIL /MS   

https://blog.rmilne.ca/2013/08/20/how-to-check-database-white-space-in-exchange/  

You can defrag to a network drive:  

https://www.itprotoday.com/email-and-calendaring/defragment-exchange-database-using-network-drive  

Q. Can I defragment an Exchange database using a network drive if I don't have enough space locally?  

A. Yes, you can use the /t switch with the Eseutil utility to specify a local or remote location as the temporary folder to be used for the database to be defragmented. Using a remote location might slow down the defragmentation process, however. In the example below, I specified the Z drive, which maps to a network path (or you can use a UNC path), and a temporary file name for the database.  

Example:  

  C:\Program Files\Exchsrvr\bin>eseutil /d "c:\program files\exchsrvr\mdbdata\priv1.edb" /tz:\tempdfrg.edb
