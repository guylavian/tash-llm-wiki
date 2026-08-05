---
title: "Demote a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/498941/demote-a-domain-controller
question_id: 498941
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Demote a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/498941/demote-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

We have 4 domain controllers in total (2 production site / 2 disaster recovery site). One of the two that they are located to DR stopped out of the blue to install the windows updates. I tried almost everything that i could found over the internet and nothing help me to solve it. So i took the decision to create a new virtual machine with the role of a domain controller and demote the one that is broken.   

My question is this... If i will demote the dc can i reuse its name and ip for the new virtual machine or i will have issues with the AD or AD site and services? Could you please let me know?  

Thank you in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-03*

Thank you FanFan :) I will try this today and i will let you know! Do i have to do something with the metadata of the dc that i will demote?
