---
title: "Exchange 2010 - Exchange Online migration - Public folder to shared mailbox migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/177451/exchange-2010-exchange-online-migration-public-fol
question_id: 177451
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 2010 - Exchange Online migration - Public folder to shared mailbox migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/177451/exchange-2010-exchange-online-migration-public-fol (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are migrating Exchange 2010 to Exchange Online using Full Hybrid migration process.   

All mailbox were already migrated. Now, there is only one public folder containing just contacts. The idea is to migrate those contacts to an online shared mailbox, before the decomission of the Exchange Server 2010 and then the migration to Exchange 2016 just for administration purpose.  

The question is, how to create the shared mailbox in this migration phase in order to then migrate the public folder content to it?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-27*

If it's just contacts you could EXPORT them to PST and then IMPORT the PST into the shared Exchange online mailbox  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-27*

@Cristian Ruiz      

There doesn't exist a build-in to migrate data from Exchange on-premises public folder to Exchange online shared mailbox. We can only migrate Exchange on-premises public folder to Exchange online.    

So, you may need to recreate those contacts in Exchange online again. You can also try to check from Exchange development forum, whether there exist way to use EWS service to do this job.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
