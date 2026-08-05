---
title: "Cannot mount Exchange 2010 database after DAG member failed - Active Database cannot mount"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/156443/cannot-mount-exchange-2010-database-after-dag-memb
question_id: 156443
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Cannot mount Exchange 2010 database after DAG member failed - Active Database cannot mount

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/156443/cannot-mount-exchange-2010-database-after-dag-memb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Great Morning All!!

I have a Exchange 2010 DAG  

(3) servers

ProdMB - mailboxes  

ProdHTCA - Hub Transport and Client Access - also Witness Server  

DRHTCAMB - Disastery Recovery - Mailboxes, Hub Transport, Client Access

whenever DRHTCAMB shuts down, email doesn't work

Currently I have a System Board that Failed on DRHTCAMB and this server is temporarily out of commission. (waiting for replacement parts)  

3 databases display "service down"

I cannot mount the three databases on ProdMB even though this server houses the Active Databases.  

3 databases display "dismounted"

* this began with the shutdown of all systems to replace UPS batteries *  

* I did suspend copy first *  

* I did shut down the two PROD systems first*  

* I did then shut down the DR server*

when trying to mount the databases on ProdMB,  

I get the following error message

Microsoft Exchange Error

Failed to mount database 'DBA-L'.

DBA-L  

Failed  

Error:  

Couldn't mount the database that you specified. Specified database: DBA-L; Error code: An Active Manager operation failed. Error An Active Manager operation encountered an error. To perform this operation, the server must be a member of a database availability group, and the database availability group must have quorum. Error: Server 'ProdMB' isn't in the stopped or started servers list. This may be due to an Active Directory replication delay.. [Server: ProdMB.domain.com].

An Active Manager operation failed. Error An Active Manager operation encountered an error. To perform this operation, the server must be a member of a database availability group, and the database availability group must have quorum. Error: Server 'ProdMB' isn't in the stopped or started servers list. This may be due to an Active Directory replication delay.. [Server: ProdMB.domain.com]

OK

Any help, ASAP would be really appreciated.....

b-safe all.....

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-30*

hi erik,  

thanks for getting back to me.....  

I ended up openning a $499 one-time ticket with Microsoft......  

they have me delete the DAG after removing the servers,  

then I setup the DR system to be the new email server since the PROD Exchange databases would not mount,  

after many changes, DNS public and private, port changes, ip address changes...... it seems to be working,  

I still have some issues with smart phones connecting, but I am working on that.  

somehow the two sets of databases were out of synch, and the DAG broke or didn't work correctly.....  

so much for Disaster Recovery..... we got the Disaster part..... just not an auto recovery....  

thanks again for responding.  

don

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-10*

I now have the new system board in and the server is up and running.    

Production Email shows "dismounted" and won't let me mount    

DR Email shows "Failed"    

I ran your commands and come up with the following messages.    

38862-gmbcs.pdf38770-trh.pdf

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

38654-rmsdag.pdf38596-rmsdag2.pdf    

I ran the two commands    

The DR Server is down needs new motherboard that I have ordered,    

but wanted to see if I can get the email working before that comes in.    

thanks for your help, don

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

When you shutdown the two PROD servers, DAG might has lost quorum, please run the following commands and post the results:    

```
Get-DatabaseAvailabilityGroup –Status –Identity DAG01 | FL  
Test-replicationhealth   
Get-MailboxDatabaseCopyStatus *
```

Normally, we could run the following commands to restart the cluster service and restart DAG:    

```
Stop-Service ClusSvc  
Net start CluSvc /forcequorum  
Start-DatabaseAvailabilityGroup –Identity DAG01 –MailboxServer name
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
