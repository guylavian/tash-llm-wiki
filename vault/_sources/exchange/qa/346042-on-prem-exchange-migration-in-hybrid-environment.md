---
title: "On-prem Exchange migration in hybrid environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/346042/on-prem-exchange-migration-in-hybrid-environment
question_id: 346042
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# On-prem Exchange migration in hybrid environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/346042/on-prem-exchange-migration-in-hybrid-environment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

current environment:  

-Exchange 2010 server  

-Exchange 2013 server  

-hybrid  

-99% mailboxes are migrated to O365  

I need to migrate on-prem Exchange 2010/2013  to Exchange 2016 in this hybrid environment and decommission Exchange 2010/2013  

Exchange deployment assistant does'nt have option for migration in hybrid environment  

https://assistants.microsoft.com/  

Is there any official Microsoft document for upgrading Exchange in hybrid environment?  

Any advice?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-07*

Hi @Andy   ,    

Agree with Andy, I also recommend that you first migrate all mailboxes before configuring the on-premises Exchange server. There are very specific steps in the article provided by Andy, you could refer to it.    

In addtion, before you introduce Exchange 2016, please make sure that your Exchange 2010 version is Rollup 11 for Exchange 2010 SP3 or later, your Exchange 2013 version is CU 10 or later. For more information you could refer to: Exchange Server system requirements    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
