---
title: "How to query Active Directory for all employees directly and indirectly reporting to a general manager?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189207/how-to-query-active-directory-for-all-employees-di
question_id: 2189207
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to query Active Directory for all employees directly and indirectly reporting to a general manager?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189207/how-to-query-active-directory-for-all-employees-di (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For internal billing purposes, we need to find all the employees directly and indirectly reporting to the general manager.

For example, the general manager is item A in LDAP (Active Directory), and 

-  item B has property "manager=A", so B directly reports to A.

-  Moreover, item C has property "manager=B", so C reports to A as well, indirectly.    In the mini example, general manager A's team includes B and C.
To start from the general manager's item in LDAP and iteratively find all the employees under him through the relation of "manager=xxx" property. The data structure is like a multi-children tree, and our first thought is to write a python script and implement a BFS (breath-first search).

Our Question:
However, before re-inventing any wheels, we hope to double-check whether there is a way to do it within the built-in functions and tools.We highly appreciate any hints and suggestions.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Hello yzgoa,  

Thank you for posting in Microsoft Community forum.  

For checking the organization relationship for reporting to the general manager.  

I have viewed in my lab.  

I have set four people in lab.  

The organizational relationship from low to high is:  

t2-xiashu\t2\t2-manager\t2-manager-manager  

I have set manager for t2-xiashu and t2 and t2-manager.  

I can only see directly reporting to a general manager for all employees, but I cannot see indirectly reporting to a general manager.  

For example:  

The manager of t2-xiashu is t2.

  

https://learn-attachment.microsoft.com/api/attachments/eb55e1c6-2f2e-42db-982c-25a5110b6011?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/5fe3b8aa-f723-4b35-a6bb-c1020fb6ba43?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">

The manager of t2-manager is t2-manager-manager.

  

Meanwhile, I can see all the directly and indirectly reporting to a general manager for all employees under organization tab in Teams.   

  

For the last option for you, maybe you can query the information you need via Teams team engineers.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
