---
title: "How to decommissioning Domain Controller Server (active and not active)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1242915/how-to-decommissioning-domain-controller-server-ac
question_id: 1242915
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to decommissioning Domain Controller Server (active and not active)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1242915/how-to-decommissioning-domain-controller-server-ac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have active domain controller and not active Domain controller. Both of them wll be processed decommission, so please help us for the best practice to do it.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-04-18*

You can use server manager to decommission and remove the role for the active one. For the inactive one and possibly the other as well, once powered off / removed from the network you can remove remnants of old ones from active directory.    

Clean up Active Directory Domain Controller server metadata  

Step-By-Step: Manually Removing A Domain Controller Server  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 1 · updated: 2023-04-18*

Hello
Thank you for your question and reaching out. I can understand you are  having query\issues related  to DC removal.
First of all you can Remove Inactive Domain controller using ntdsutil  then  verify AD health and SYSVOL replication is working good . then you can proceed with Active DC removal.
I would like to invite you  to have a look on below reference url for step-by-step guide.
https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564
--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-04-18*

Sites and services of the active directory, unprotecting the connections to the other servers, then unprotecting the server, and finally eliminating the server, being automatically removed from Users and computers in the active directory. Then use the Ntdsutil command; you do not see it anymore, so it does nothing.
