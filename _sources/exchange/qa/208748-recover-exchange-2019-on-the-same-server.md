---
title: "recover Exchange 2019 on the same server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208748/recover-exchange-2019-on-the-same-server
question_id: 208748
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# recover Exchange 2019 on the same server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208748/recover-exchange-2019-on-the-same-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

After the installation of a Security patch upon Exchange 2019 CU6, the Exchange server crashed (one server in a two-server setup).  

2 of the 6 fail-over databases are in a dirty shutdown mode and multiple Exchange services are down, not able to start them.  

After some analysis, we would like to recover the lost server, using the ISO file which was used during the initial setup:  

Setup /m:RecoverServer /IAcceptExchangeServerLicenseTerms /TargetDir:"<MSExchangeinstalldir>"  

therefor we plan to first do the following:  

-  Remove Passive mailbox copies  

-  evict faulty node from the cluster  

-  remove faulty server from DAG (Remove-DatabaseAvailabilityGroupServer <name of faulty server> -Identity <name of DAG> -ConfigurationOnly)  

Questions  

-  Does this small procedure make sense? Are we missing something?  

-  Can we do this from the same server (where exchange is still installed, but not running)?  

-  What are the actions afterwards (to make sure databases are replicating correctly)?   

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-23*

Hello, Thank you for your replies.  

The two corrupted databases are replica databases.  

For now, the mail is fully operational, but only on one note.  

The recover will be done on the same server, without rebuilding the OS.   

The actions are planned for the coming weekend.  

I'll keep you updated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-23*

You will want to follow :    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-dag-member-servers?view=exchserver-2019    

Your steps look generally correct but be sure to follow the doc steps exactly.    

And yes, you can run this on the same server ( I would rebuild the O/S of course)    

After installation is complete, you can re-add the databases and test health:    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-dag-member-servers?view=exchserver-2019#how-do-you-know-this-worked    

```
Test-ReplicationHealth   
Get-MailboxDatabaseCopyStatus -Server 
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-23*

Couple of things    

-  Regarding the two databases that are in a dirty shutdown state, are those replicas and therefore don't need to be recovered or is that something to be addressed?    

-  Have you checked the SYSTEM & APPLICATION logs to see if there was an underlying issue on that server to be addressed?  If not I would suggest filtering out to show only error and critical events for the SYSTEM & APPLICATION logs to understand what if any other issues were at play with the failure, else you may have another failure occur in the future.  For example if there are hardware related issues, they need to be resolved first    

-  If you have not already done so, I would recommend copying all the DB's to an alternate location so that should something go wrong you are in a better please    

-  Once you have completed the above and corrected any problems, follow this article to accomplish the recovery https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-dag-member-servers?view=exchserver-2019    

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
