---
title: "Windows server 2012 domain controller installation in 2 sites best practice."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/187603/windows-server-2012-domain-controller-installation
question_id: 187603
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows server 2012 domain controller installation in 2 sites best practice.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/187603/windows-server-2012-domain-controller-installation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.  

I am new to windows server. I have 2 sites( site-A and site-B) and each site has 2 domain controllers.  

Site-A DCs= DC-1 , DC-2  

Site-B DCs= DC-3 , DC-4  

 I want to setup each dc as writeable dc. After installing first dc, when i add each new dc, in “Aditional options” step, ask me to choose replication from(..........) and i can choose “any domain controller” or a dc which i have previouslly installed.  

 In this case, Which is the best selection for intrasite and intersite?( any domain controller or a distic dc). I mean, i have to choose all replication as “any domain controller“ or atleast a ditinc DC in each site?  

Best regards  

Sina hr

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-05*

I'd select “any domain controller“ then define sites and subnets.    

https://www.rebeladmin.com/2015/02/why-active-directory-sites-and-subnets/    

then bridgeheads will handle site to site replications.    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff800799(v=ws.10)?redirectedfrom=MSDN    

--please don't forget to Accept as answer if the reply is helpful--
