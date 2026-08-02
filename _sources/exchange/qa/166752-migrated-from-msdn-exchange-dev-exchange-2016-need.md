---
title: "[Migrated from MSDN Exchange Dev]Exchange 2016 need more space"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/166752/migrated-from-msdn-exchange-dev-exchange-2016-need
question_id: 166752
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Exchange 2016 need more space

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/166752/migrated-from-msdn-exchange-dev-exchange-2016-need (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange 2016 need more space  

[Original post]  

Hi,  

We have an Exchange 2016 server running on premises and have a need for more spaces.  

This is Exchange 2016 running on Hyper-V (Windows Server 2012 R2).  The host server is a Dell PowerEdge 430 with 4 hard drives Raid6.  There are more available slots for more hard drives on the server.  

What is the best way to proceed to get more spaces for Exchange?  

Can we add more hard drives to the server and create another or new Mailbox Database on the new hard drive?  Is that possible?  

Can we add more hard drives with enough space to the server and move existing Mailbox Database to these new hard drives?   

Your comment and suggestion will be greatly appreciated.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-11-18*

Hi,    

What is the best way to proceed to get more spaces for Exchange?    

According to this article from TechNet wiki: Exchange: Steps to increase database storage    

    

You can power off the server and expand the disk space for it.    

Can we add more hard drives to the server and create another or new Mailbox Database on the new hard drive? Is that possible?    

Yes.     

It can be done when creating a new database.    

You need to configure the database path to be on the new hard drive.    

Can we add more hard drives with enough space to the server and move existing Mailbox Database to these new hard drives?    

Yes.    

You can use this command via EMS to move the existing databases to other disks:    

```
Move-DatabasePath -Identity MyDatabase01 -EdbFilePath C:\NewFolder\MyDatabase01.edb
```

While,there may be some downtime since during the process the database will be dismounted.    

I think it is more recommended to create a new database on other disks,move all mailboxes to it and delete the old database to free disk space.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
