---
title: "Exchange 2016 and mail.que file"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/414342/exchange-2016-and-mail-que-file
question_id: 414342
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 and mail.que file

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/414342/exchange-2016-and-mail-que-file (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, so we've just deployed Exchange 2016 in our environment and I am in the process of moving mailboxes from our older 2010 server.  One thing I've noticed is this file called mail.que sitting in the following folder:   

C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue  

As you can see it is sitting on the OS volume and it is beginning to become a concern as that drive is running low on space.  This que file is at about 6Gb in size now and seems to continue to grow.  I found the following article which describes how to adjust the "SafetyNetHoldTime" value using set-TransportConfig.  I guess lowering this value would make it grow less.  Although you can't shrink once it gets out of control it seems.  Right now our value is 7 days it appears.  Which is different than the article mentions it should be, perhaps it is 2013 that is default at 2 days.  

https://www.admin-enclave.com/en/articles/exchange/296-resolved-exchange-hub-transport-mail-que-file-large-in-size.html  

Anyway, it appears this is basically a database and probably should get moved to a data volume just like our mailbox databases are.  I'm curious what best practice is.  Our little OS drive is only 80Gb and is down to 25Gb or so left over.  It's nice having a small OS drive for restore purposes, but I need to get things like this off that drive.  

Here is another article that describes the process of moving the mail.que file to a data volume.  Bad idea?  Is this a non-disruptive task?  Recommended?  Microsoft provided script for this task: .\Move-TransportDatabase.ps1  

https://www.alitajran.com/move-mail-queue-exchange-2016-to-another-location/  

Regards,  

Adam Tyler

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-29*

No, a good idea. I have done this when faced with a disk space issues on the system drive.     

You can also change the location manually:    

https://learn.microsoft.com/en-us/exchange/mail-flow/queues/relocate-queue-database?view=exchserver-2019#use-the-command-prompt-to-move-the-existing-queue-database-and-transaction-logs-to-a-new-location    

Just stops the transport service and restarts when done.    

Pretty non disruptive and reasonably quick.
