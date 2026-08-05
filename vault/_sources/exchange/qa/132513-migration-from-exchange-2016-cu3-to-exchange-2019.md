---
title: "Migration from Exchange 2016 CU3 to Exchange 2019 latest with new environment Server 2019 Std"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132513/migration-from-exchange-2016-cu3-to-exchange-2019
question_id: 132513
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migration from Exchange 2016 CU3 to Exchange 2019 latest with new environment Server 2019 Std

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132513/migration-from-exchange-2016-cu3-to-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are planning to migrate all of our Windows Server 2012 R2 Standard to Server 2019 Standard. For this, we will have to migrate our Exchange 2016 CU3 (2 instances running in redundant mode) to new Windows Server 2019 Standard server machines. We have got the VMware virtualized environment and these exchange server are working internally only.  

Can any one please guide us through the detailed step by step process to migrate our Exchange server instances to new Windows Server 2019 standard environment with healthier and smooth transition without loosing any data or application.  

Also, do we need license key if we upgrade from Exchange server 2016 to 2019 during this OS migration?  

Thanks and Regards  

Ali,

## Answer (community) — community member

*upvotes: 1 · updated: 2020-10-21*

@ahmed qureshi    

Here are some suggestions for you to update your server:  

-  You cannot update Exchange 2016 to Exchange 2019 directly. You need to create Exchange 2019 coexist with Exchange 2016 first, then migrate mailboxes to Exchange 2019, then uninstall Exchange 2016.  

-  Exchange 2016 and Exchange 2019 are two different products, so, you still need to purchase license for Exchange 2019.

Before updating, I want to confirm that your DC server is also Windows Server 2012 R2?  

Here are update steps for you:  

-  Update Exchange 2016 at least to CU 11 which supported coexist with Exchange 2019.  

-  Install Exchange 2019 which hosted on Windows server 2019. (Before this step, make sure the domain function level is at least Windows server 2012 R2)  

-  Migrate mailboxes and other needed thing such as public folder to Exchange 2019.  

-  Change DNS record to Exchange 2019 and uninstall Exchange 2016.  

-  Migrate DC from Windows server 2012 R2 to Windows server 2019. This article may be help for you, for more detailed tutorials, you could confirm with Windows server team.

Here are some other article which will be useful to you during updating:

-    Exchange Server supportability matrix

-    Exchange Deployment Assistant

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-20*

Exchange 2016 is not supported on Windows 2019! Do not do this  :)    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019    

Also, what you proposing is not supported regardless and you should be at CU17 at a minimum.     

If you want to migrate to new servers, bring up new Windows 2016 Servers and move mailboxes. That is the only supported method
