---
title: "Active Directory Domain/Forest Upgrade Order 2003-2019 and Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/712755/active-directory-domain-forest-upgrade-order-2003
question_id: 712755
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Active Directory Domain/Forest Upgrade Order 2003-2019 and Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/712755/active-directory-domain-forest-upgrade-order-2003 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning the upgrade of our on-prem AD environment from 2003 forest and domain functional levels - can you please sense check our plan?  

This is the planned order:  

Decommission the last 2003 DC  

Raise the domain and forest functional levels to 2008 (a prerequisite to use the dfsrmig tool)  

Migrate from FRS to DFSR  

Introduce 2016 DCs and decommission all previous DC versions  

Raise the domain and forest functional levels to 2016  

Upgrade Exchange 2013 which supports AD only up to 2016. Exchange 2019 supports 2016 Active Directory environments, but not 2022.  

Introduce 2019 DCs and decommission all previous DC versions  

We do not have on-prem mailboxes (hybrid exchange), but for as long as we need to keep an exchange server for management, we will stay clear of AD 2022.  

How does that sound?  

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-28*

Hello @ppgdtp7       

I would recommend you the next step by step guide toward 2012R2 which should be the steepest gap in features and require surgical precision:     

https://learn.microsoft.com/en-us/archive/blogs/canitpro/step-by-step-active-directory-migration-from-windows-server-2003-to-windows-server-2012-r2    

From there is should be business as usual, and there are several guides you can find to rise and upgrade from 2012R2 until 2019, then should be seamless to 2022.     

Hope this helps with your query,    

------------    

--If the reply is helpful, please Upvote and Accept as answer--
