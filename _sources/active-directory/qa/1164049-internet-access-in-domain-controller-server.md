---
title: "Internet access in domain controller server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164049/internet-access-in-domain-controller-server
question_id: 1164049
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Internet access in domain controller server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164049/internet-access-in-domain-controller-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As per security protocols we have been asked to block internet access on our domain controller server. Our domain controller server has Active directory domain services and DNS server roles setup in it.

Kindly let me know if there would be any impact if we disable internet on the domain controller server.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hello there,

A domain controller needs a VPN connection , when you have a remote site to ensure authentication or replicate with local domain controller. It's not recommended to expose a domain controller on internet.

Securing Domain Controllers Against Attack https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/securing-domain-controllers-against-attack

Similar discussion here https://learn.microsoft.com/en-us/answers/questions/958377/impact-of-removing-internet-explore-in-domain-cont

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-25*

Hi @Avinash Yadav  ,

this is a good approach to secure critical service like domain controllers.

The two impact you can occurred:

-  If the IP of domain controller is used as DNS resolver on client computer, client can be impacted to navigate on internet, because the local DNS server ( domain controller in your case) need to forward DNS request to external DNS server.

-  If you don't have a WSUS server ,and the domain controllers download update from Microsoft download site, windows update can be impacted 

Please don't forget to mark helpful answer as accepted
