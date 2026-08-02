---
title: "Single Exchange2016(CU19) Win2012R2 Giving RAM 32GB in VM. How much page file to be set?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/331419/single-exchange2016-cu19-win2012r2-giving-ram-32gb
question_id: 331419
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Single Exchange2016(CU19) Win2012R2 Giving RAM 32GB in VM. How much page file to be set?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/331419/single-exchange2016-cu19-win2012r2-giving-ram-32gb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

My Current Infra  

1-Primary Domain Controller  

1-Secondary Domain Controller + File Server  

2-RODC  

2 Child Domain  

1 Exchange Server 2016 (CU19) Windows2012 R2 64Bit  

DB01  

DB02  

Current Memory is 20GB . So created Additional partition for SWAP Memory  as 21GBHDD Pagefile set as 20GB  

We have 300 Mailbox. to improve performance. Planning to increase from 20Gb to 32GB  

Now i want know How much SWAP memory to be allocated when we are using 32GB in Exchange Server. So i can increase the partition 21Gb HDD -> required for pagefile  

Please advise

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Many thanks for the details  

I am increasing CPUs in VM like 4CPU to 8CPU is it good to increase for Exchange Server?  

Please advise

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-25*

This is the official guidance:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2016#hardware-requirements-for-exchange-2016    

You will notice there is no difference for a physical or VM, so in your case, set it     

32 GB of RAM or more installed: 32GB plus 10MB (32,778MB)    

The paging file size is set that way so it you can get a full memory dump in case of a crash.     

You do not absolutely have to set it that value, its just recommended.    

Hope that helps!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-25*

You can  use this to calculate  

https://www.alitajran.com/pagefile-exchange-2013-2016-best-practice/#Calculating_the_pagefile_Exchange_20132016
