---
title: "1 M365 tenant, 2 Active Directory same domain suffix"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5375771/1-m365-tenant-2-active-directory-same-domain-suffi
question_id: 5375771
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["m365-office-install-redeem-activate-business-unknown-platform", "office-exchange-hybrid-management"]
---
# 1 M365 tenant, 2 Active Directory same domain suffix

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5375771/1-m365-tenant-2-active-directory-same-domain-suffi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I want to know if it is possible to have one suffix in both Active Directory forests. Let me explain below.  

There is a domain with suffix domain-a.com. There is also a domain with suffix domain-b.com.  

There is already a domain trust between these domains. They see each other.

Domain-a.com was the first with synchronized users to the M365 tenant. Domain-a.com is the main domain suffix in this tenant.   

After the domain trust the users from Domain-b.com are also synchronized to the tenant Domain-a.com.

Authentication works from both ways. 

I have got the question to create a new domain. Let's say Domain-c.com. They want to have this domain-c.com as an UPN in Domain-a.com and Domain-b.com. This would be for all users. Domain-c.com also needs to be used in the Domain-a.com M365 tenant.  

My question is as follows, is this possible without any issues with syncrhonizing to the tenant and also authentatication to the M365 services?   

Also, when an user from Domain-A.com (with Domain-C.com suffix) authenticates from within the Domain-B.com domain, is this authentication going well? This is regarding the shared folders on the network of Domain-A.com.  

Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-05*

Hi John,

I created a new topic. And this is the link: https://learn.microsoft.com/en-us/answers/questions/2006685/1-m365-tenant-2-active-directory-same-domain-suffi?page=1#answer-1781354

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-04*

honestly this is so unhelpful . This question was absolutely spot on what I was looking for a now has to post it elsewhere where it will be hard to find . 

If the OP sees this could you post the link to your new post in the other forum as I can’t see it anywhere

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-26*

Hello Kevin Otten,

Good day! Thank you for posting to Microsoft Community.

I understand that you want to know if it is possible to have one suffix (Domain-c.com) in both Active Directory forests (Domain-a.com and Domain-b.com) without any issues with synchronization to the M365 tenant and authentication to M365 services. While our primary focus is on Outlook basics, I’d like to provide some guidance regarding your query.

Regarding your specific issue related to the Microsoft Exchange Hybrid environment, I recommend posting your concerns in the relevant community. You can find specialized assistance in the "Exchange Hybrid Issues” on Microsoft Exchange Hybrid Management - Microsoft Q&A. Experts in this category possess extensive knowledge of Microsoft Exchange Hybrid environment and can provide tailored solutions to unique problems.

I apologize for redirecting you to a different community, but I believe this step will ensure faster and more accurate assistance for your specific scenario.

Thank you for your cooperation and understanding. Please do not hesitate to post your queries in Microsoft Community, and we will always do our best to assist you!

Sincerely 

Feroz Mahmud | Microsoft Community Moderator
