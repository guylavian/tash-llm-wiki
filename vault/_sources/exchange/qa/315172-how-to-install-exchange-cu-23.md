---
title: "How to install Exchange CU 23?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315172/how-to-install-exchange-cu-23
question_id: 315172
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# How to install Exchange CU 23?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315172/how-to-install-exchange-cu-23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey All  

On the back of the Hafnium threat I need to install the latest CU to be able to install the out of band patches.  

We are hybrid and only use the internal exchange servers (these are on CU20)  for management and the email relay for internal systems.  

Never done this before.  

How should I install CU23?  

Do I need to prepare schema or is like any other next next update?  

Anything I should be aware of?  

Thanks a million guys.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-16*

@SenhorDolas      

I noticed that you deployed hybrid in your organization. The attack is using 443 port, although you may restrict the IP addresses allowed to connect, I still recommend that you update Exchange to the latest CU and install the patch for safety reasons.    

As the information that provided by AndyDavid, you need to install .net 4.7.2 or 4.8, then update(Double-click the installation package) Exchange 2013 to CU 23 and install the patch(Run PowerShell with administrator right, then run this patch from PowerShell).    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
