---
title: "How to control my Window Server Active Directory domain controller from USA to Australia?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185125/how-to-control-my-window-server-active-directory-d
question_id: 1185125
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# How to control my Window Server Active Directory domain controller from USA to Australia?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185125/how-to-control-my-window-server-active-directory-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I configured active directory in Australia, but now I am in USA and I am not sure how to control the domain(AD DS) server that I worked in Australia. Can someone please tell me what should I do to get access my domain controller server from USA to Australia? so that I can make some changes on my GPO and other configuration? 

Or lets say, I made a active directory in USA but in another state, how should I manage my domain controller from different state? How to control Place "A" from Place "B"? 

I am using window server 2019 datacenter. How does those network work from one place to another please explain me in detail and with picture for more clarification. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-01*

Hello

Thank you for your question and reaching out. I can understand you are  having query\issues related  to AD connect from different location.

You can go with VPN or mpls connectivity from one area to another. Also you would required addtional hardware to setup connvitouvy betwenn two locations ( Firewall ,  Router , Switches )

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-28*

The simplest and most common solution is to connect the sites via a VPN connection.    

Configure a Multisite Deployment  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
