---
title: "2012 R2 DC as Specific Global Catalog fo Exchange 2010 RU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/342405/2012-r2-dc-as-specific-global-catalog-fo-exchange
question_id: 342405
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# 2012 R2 DC as Specific Global Catalog fo Exchange 2010 RU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/342405/2012-r2-dc-as-specific-global-catalog-fo-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am running Exchange 2010 SP3 RU23 with 2 Windows 2008 Server Domain Controllers acting as it GC.   

One of the Windows 2008 holds all of the fsmo roles and having replication issues.   

I am looking to remove that 2008 as specific GC for Exchange. Does Exchange 2010 support a 2012 R2 server as specific GC to use ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

Hi @Anser Leon   ,    

Agree with Andy. And since you have all the FSMO roles on the GC where the problem occurred, please make sure to transfer all the FSMO roles before removing the GC.    

In addition, considering that Exchange 2010 is end of support. If poosible, please upgade to a higher version as soon as possible.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
