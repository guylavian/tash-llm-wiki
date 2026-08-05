---
title: "Windows 2008 Domain Controller migration to 2016+ Child Domain, CA and exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/191074/windows-2008-domain-controller-migration-to-2016-c
question_id: 191074
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Windows 2008 Domain Controller migration to 2016+ Child Domain, CA and exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/191074/windows-2008-domain-controller-migration-to-2016-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have been assign the project to migrate our Windows 2008 domain controllers to windows 2016 domain controller. We have 8 Domain controllers and a child domain with 2 DC. To add we have an Exchange 2016 server and a Windows 2012 CA server. Questions:  

Do we need to do a DCPROMO /adprep and forestprep on all Domain controller  

what do we need to do with the child domain. Can we do the upgrade on the parent domain and not the child domain or we need to plan for both.   

Do we need to add a CU for Exchange 2016  

Is there anything to do with our Windows 2012 CA server that is not a DC by the way. 1 CA with 1 SUBCA  

thx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

Hi,  

I am glad to hear that your issue was successfully resolved\I am pleased to know that the information is helpful to you. If there is anything else we can do for you, please feel free to post in the forum.  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-09*

Thx for your answer, but why should you start with the Child Domain. Is it a logical route even if its not important to start with it.  

You can do either one as first step.  

Also what do you think about a in place upgrade, is it recommended?  

An in-place upgrade is never recommended, especially for a domain controller. Standing up new domain controllers is a very simple and quick process, not worth the risk.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

Thx for your answer, but why should you start with the Child Domain. Is it a logical route even if its not important to start with it.  

Also what do you think about a in place upgrade, is it recommended?  

thx
