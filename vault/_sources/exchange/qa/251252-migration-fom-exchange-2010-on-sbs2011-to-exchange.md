---
title: "Migration fom Exchange 2010 on SBS2011 to Exchange 2016 on same domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251252/migration-fom-exchange-2010-on-sbs2011-to-exchange
question_id: 251252
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migration fom Exchange 2010 on SBS2011 to Exchange 2016 on same domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251252/migration-fom-exchange-2010-on-sbs2011-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,  

how could be right this guide about migration from an exchang 2010 on SBS2010 to exchange 2016 on Windows 2016 Standard on the same domain, following this?  

https://msexperttalk.com/exchange-2010-to-exchange-2016-migration-part-1/  

there is some microsoft guide to do that?  

i have a small organization with 50 Mailbox

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-10*

According to Microsoft, the steps have not changed since this article:    

https://learn.microsoft.com/en-gb/archive/blogs/infratalks/transition-from-small-business-server-to-standard-windows-server    

For Exchange 2016 migration, I recommend you to use Microsoft Exchange Server Deployment Assistant - a web-based tool that provides you a custom step-by-step checklist about migration:    

Exchange Deployment Assistant    

How to Migrate SBS 2011 to Server 2016 (Exchange 2016)?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-22*

A question about my migration,  

i have an Exchange 2010 SP1, it is supported by CodeTwo,  

but i have to prepare exchange 2016 in the same domain, you think it's a problem that i do it in the same forest\domain?  

mabye I need to upgrade to SP3 ru11 before also if i use CodeTwo after for migrating mailbox?  

I need to test it before doing in production.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-04*

Hi @MarcoMandricardo-1414 ,    

Sorry for the delay of this reply.    

Yes you should update your Exchange to SP3 CU11 to coexist with Exchange 2016,  but you can first use Get-ExchangeServer to check which version you’re using.    

And sorry that I have never used CodeTwo to do the migration before. Besides, according to Microsoft product strategy, we only provide support for Microsoft products. If you have questions about the third-party software, I think you can try to contact with their support center to get help.    

If you don’t use Exchange 2010 and SBS2011, you can directly remove them after migration and configuration, make sure CAS FQDNs, mail flow connectors and virtual directory urls are pointing to Exchange 2016.    

The Exchange Deployment Assistant will tell you how to migrate all needed mailboxes, records, URLs and other items to the new server, so you could directly remove the legacy Exchange 2010 after the migration.    

Also you can read this article: Removing Exchange 2010 after Coexistence with Exchange 2013, it is same in Exchange 2016.    

I found a guidance of the migration from Exchange 2010 to Exchange 2016 using CodeTwo: How to migrate Exchange 2010 to 2016? A step-by-step guide. Hope it will help you.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Bests,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-01*

Hi @MarcoMandricardo-1414  ,    

I think you should check the version of Exchange 2010 first. Because the minimum version of Exchange 2010 required to coexist with Exchange 2016 is SP3 RU11.    

    

Run Get-ExchangeServer in EMS, and compare the Build number with Exchange Server 2010 build numbers, if the version doesn’t reach the requirement, you should update it to at least SP3 RU11 first.     

Then you can do the following steps for coexistence and migration:    

-  Prepare SBS 2011 and raise domain function level.    

-  Install Windows Server 2016 and join domain.    

-  Promote Windows Server 2016 as domain controller.    

-  Install Exchange 2016 on another Windows Server.    

-  Configure Exchange 2016 and migrate mailboxes and public folders to it. Exchange Deployment Assistant    

-  Uninstall Exchange 2010 on SBS 2011.    

These articles have a detailed guidance for the migration: SBS Exchange 2010 Update and How to Migrate SBS 2011 to Server 2016 (Exchange 2016)?, I think they would help you.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
