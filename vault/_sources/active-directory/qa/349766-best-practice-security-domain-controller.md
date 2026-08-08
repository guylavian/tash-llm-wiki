---
title: "Best practice security Domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/349766/best-practice-security-domain-controller
question_id: 349766
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Best practice security Domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/349766/best-practice-security-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I would like to know if you have some link / ressource / idea about the best practice to protect domain controller and server.  

I mean : Applocker, bitlocker, ...  

What settings need to be applied today to be protect from main security issue (except microsoft updates).  

Does bitlocker is necessary on virtual machine or only on physical client PC / servers ?  

I don't know anything about security and I don't know where to start to learn.... I'm not interested about Azure feature in the first time because I don't have lot of customer with Azure in their environment.  

Thank you for your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-08*

Unfortunately I don't have ullimited money to open all the case I would like with product support.  

I'm asking here if some people can give me some informations / link to read and improve myself.  

Thanks for your help.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-08*

Well yes greater security does mean some level of hardening. I'd suggest starting a case here with product support.  

https://support.serviceshub.microsoft.com/supportforbusiness  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-08*

Thanks for this link.  

Then, there is no detail like here :  

"you can often take advantage of new functionality and security that may not be available in domains or forests with domain controllers running legacy operating system."  

=> What is it talking about ? What are new security functionality in 2016 ? 2019 ?  

Use tool to secure Domain controllers -> What do you use most of the time ?   

I don't want hardening. I just want main security protection about common issue.  

RDP restriction => OK ! good idea.  

Patching -> OK  

Block internet + outbound connection -> OK  

Do you have some more idea to give me with your experience maybe ?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-08*

You can follow along here.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/securing-domain-controllers-against-attack    

--please don't forget to Accept as answer if the reply is helpful--
