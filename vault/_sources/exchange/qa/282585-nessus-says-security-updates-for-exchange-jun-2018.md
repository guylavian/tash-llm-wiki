---
title: "Nessus Says \"(Security Updates for Exchange (Jun 2018)\" in Exchange 2016 (CU17) High Vulnerability Hello Support,"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/282585/nessus-says-security-updates-for-exchange-jun-2018
question_id: 282585
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
---
# Nessus Says "(Security Updates for Exchange (Jun 2018)" in Exchange 2016 (CU17) High Vulnerability Hello Support,

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/282585/nessus-says-security-updates-for-exchange-jun-2018 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support,  

My Exchange Sever 2016 (CU17)  

When i run Nessus tool says that "Security Updates for Exchange (Jun 2018)"  

https://www.tenable.com/plugins/nessus/110642  

How to fix this issue without any impact

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-23*

Hi, @SathishkumarSingh-0068     

According to the link, your Exchange server should install:    

KB4295699(Update Rollup 22 for Exchange Server 2010 Service Pack 3)     

KB4099855 (Cumulative Update 21 for Exchange Server 2013)    

KB4099852(Cumulative Update 10 for Exchange Server 2016)    

And since you are using Exchange 2016, it may indicate you to install KB4099852(upgrade to CU10)    

However,CU10 is a previous version compared to your current version(CU17).    

And all the update should have been contained in CU17.    

    

I suppose that the problem may be with the Nessus tool and it is recommended to contact the Nessus support for help.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-02-22*

Unlike your previous question on disabling plaintext login on POP3, to fix this vulnerability you have to install patches from Microsoft and it always involve the risks of breaking things. (Especially when KB4295699 is update rollup that includes multiple updates)  

The only advice I can give you is to setup test installation (by cloning the production server) to an isolated environment, then install the update and test various functions, and see if anything breaks.  

However quick search on KB4295699/KB4099855/KB4099852 didn't return any cry-out for fails, so if the patch can be installed it should be safe.  

======  

Btw, the next time you see issues returned by Nessus, why don't you try do your homework to decide whether you should install the fix or not? IMO this is what your employer pays your salary for. Setup test environment, plan ahead for test-case to be included, validate updates, and plan how to execute the updates are all essential skillsets for MIS staffs.
