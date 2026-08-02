---
title: "Exchange hybrid server migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/295284/exchange-hybrid-server-migration
question_id: 295284
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange hybrid server migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/295284/exchange-hybrid-server-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

current configuration on-premise is 3 Exchange servers:  

Exchange 2010 SP3 latest RU  CAS,HUB server   

Exchange 2010 SP3 latest RU  Mailbox server  

Exchange 2013 CU 14  Mailbox,CAS  

95% mailboxes are in O365  

Hybrid   

I need to upgrade to single Exchange 2016 in this hybrid environment and decomission Exchange 2010 and 2013 servers.  

Is it common migration + rerun HCW at the end of migration?  

https://jaapwesselius.com/2015/11/22/upgrade-hybrid-server-to-exchange-2016/  

e.g. I have found this article  

https://www.c-sharpcorner.com/article/hybrid-exchange-2010-to-hybrid-exchange-2016-part-one/  

which says that /prepareschema is little bit different.Is there any other suprises?  

Exchange Deployment assistant does not have option to choose hybrid server migration.  

https://assistants.microsoft.com/  

Any advice?Is there any official tutorial for this kind of migration?  

Thank you

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-03*

Hi @Andy      

Agree with the suggestions above from Andy, after you install Exchange 2016 and set all configurations right, you just re-run HCW and re-configure it with Exchange 2016 server.    

Some related threads discussed about the similar issue upgrade previous Exchange server version hybrid to newer version hybrid for your reference as well:    

Exchange 2010 to 2016 migration with Office 365 Hybrid deployment    

Upgrade Exchange 2010 Hybrid to Exchange 2016 Hybrid    

Mainly steps are list in the links you have found. By the way, here is also a good link tells How to Decommission Exchange Server?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
