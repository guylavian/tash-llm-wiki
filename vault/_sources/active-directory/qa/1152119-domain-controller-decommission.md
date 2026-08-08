---
title: "Domain Controller Decommission"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1152119/domain-controller-decommission
question_id: 1152119
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Decommission

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1152119/domain-controller-decommission (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have 14 domain controllers in our environment on few of them old OS so we're planning to decommission them. Before decommission what points we have to check like :

1) FSMO roles.  

2) Forwarding.  

3) Check domain controller is not last domain controller. what else?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-08*

Hi,    

You should check all critical applications and services if they still configured with one of old DCs.    

Regarding the server and computer integrated in this domain , they will define the new closest domain controller through the DClocator process.    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-05*

Hello    

Thank you for your question and reaching out. I can understand you are  having query\issues related  to DC Decommission.    

-  Please verify AD health is Good in stat and all DCs are in Sync before Demote.    

-  Please verify Sites and Services and subnet before Demote.    

-  Please verify and DNS delegation of that DC or DHCP entries.    

-  Please verify that if there are any other additional Roles installed on these DC.    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-01-05*

Check health is 100% before doing anything. (dcdiag, repadmin, event logs free of errors, etc. Then just transfer the roles off if needed (check current role holder netdom query fsmo) to another healthy one, then decommission / demote the old one. Nothing else needs to be done.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
