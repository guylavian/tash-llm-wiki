---
title: "Exchange Server 2013 - Restore took 20 hours - how can we speed up that process ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126162/exchange-server-2013-restore-took-20-hours-how-can
question_id: 126162
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2013 - Restore took 20 hours - how can we speed up that process ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126162/exchange-server-2013-restore-took-20-hours-how-can (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Exchange Pros.  

We made a full restore of our Exchange Server 2013 virtual machine to be sure that restore works before we install Cumulative Update 23. Restore of complete VM took 20 hours !  

The System Disk C: is 30GB of data, the Mailbox Database on Disk D: is 600GB of Data and the archive Disk on Disk E: is 220 GB, so all together is almost 1 TB of Data that has to be restored in restore process.  

How can we speed up that process the best way?  

I know, it is possible to move the databases to another place but whats best practice here ?  

When we move the databases to an other system / storage, how will this complicate the backup / restore process ?  

Thank you very much for help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-15*

Hello  

Thank you for your feedback.  

The server (Exchange 2013) is am vm running on Hyper-v, we make backup with VmWare Software.  

The complete VM with Exchange 2013, mailbox database and archive database is between 950GB and 1 TB.  

We tested this restore to be sure that we can go back if installation of cumulative update 23 will go wrong. We never had to restore an Exchange Server before so we wanted to test that before we start with the CU update.   

When you say "Instead,you should restore the server from a backup or using Setup /m:RecoverServer."...that means, restore the whole VM with VmWare is NOT ok ???  

Thank you for your time and effort to help me.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-15*

@IT Guy       

Hi,    

Agree with Andy.    

Did you restored the server by using snapshots?It is not supported.    

Instead,you should restore the server from a backup or using  Setup /m:RecoverServer.    

Here is a document for your reference:Backup, restore, and disaster recovery    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-14*

So taking snapshots of Exchange isn't supported  :)     

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/virtualization?view=exchserver-2019    

What is supported is restoring the Exchange Data from an Exchange aware backup to new server using the recoverserver switch    

https://learn.microsoft.com/en-us/exchange/recover-an-exchange-server-exchange-2013-help#:~:text=The%20%2Fm%3ARecoverServer%20switch%20rebuilds,also%20use%20an%20existing%20server.    

That should cut down on the actual restore time in that sense.
