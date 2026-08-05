---
title: "understanding of Active Directory forest trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/883200/understanding-of-active-directory-forest-trust
question_id: 883200
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# understanding of Active Directory forest trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/883200/understanding-of-active-directory-forest-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need clarity on Active Directory forest trust. Lets say we have 2 different forests e.g abc.com and def.com. we create 2 way trust between them. assume abc.com office is in Dubai and def.com office is in AbuDhabi.     

my question here is that if a user of AbuDhabi office (def.com users) visits Dubai Office(abc.com) and his laptop is joined to def.com so will he be able to login to his laptop from Dubai office network?    

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-13*

Hi Sajidami82,    

This should work fine if configured correctly.  Please see the below article regarding Forest Trusts:    

https://learn.microsoft.com/en-us/azure/active-directory-domain-services/tutorial-create-forest-trust    

--------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
