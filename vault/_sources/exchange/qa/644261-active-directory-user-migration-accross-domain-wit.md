---
title: "Active directory user migration accross domain with Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/644261/active-directory-user-migration-accross-domain-wit
question_id: 644261
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Active directory user migration accross domain with Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/644261/active-directory-user-migration-accross-domain-wit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts,  

Need your advise one below-  

We have one of our customer running domain abc.com, for whom the acquisition is done by xyz.com. They are running abc.com with on-primise exchange 2013 and AD is on Windows 2012 R2. Now they want to migrate all users from abc.com to xyz.com with minimal or no downtime. What the best way forward here (any 3rd party paid tool with can be used).  

Our objective -   

-  Migrate all users with exchange mailbox to xyz.com domain  

-  We want to ultimately upgrade to Windows 2019 based DCs  

-  Exchange also needs to be upgraded to Exchange 2019  

We read of internet about not doing any migration to across forest with Exchange as its not supported. Need your expert opinion and advise.  

Thanks for the help in advance.  

Regs,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-01*

Hi there,    

Your first step would be to complete all the prerequisites for migrating to Windows 2019 DC from Windows Server 2012.    

Here are some quick steps to do the migration with less downtime.    

Set up a new server using Windows Server 2019.     

Join the new server to your existing Active Directory domain.    

Install the Active Directory Domain Services role.     

Promote the new server to a domain controller.    

Here are some articles which might be really useful for your carrying on these steps properly.    

Exchange Cross-forest migration when source and target domain use the same email address    

https://learn.microsoft.com/en-us/answers/questions/572404/exchange-cross-forest-migration-when-source-and-ta.html    

Upgrade Active Directory Windows server 2012 R2 to Windows server 2019    

https://learn.microsoft.com/en-us/answers/questions/384793/upgrade-active-directory-windows-server-2012-r2-to.html    

-----------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
