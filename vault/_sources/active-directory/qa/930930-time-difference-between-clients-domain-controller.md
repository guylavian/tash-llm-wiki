---
title: "Time difference between Clients & Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/930930/time-difference-between-clients-domain-controller
question_id: 930930
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Time difference between Clients & Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/930930/time-difference-between-clients-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We are facing a issue with time difference in our AD domain. Some pcs in the domain are having 2 or 3 minutes of time difference between the DCs. We have 2 DCs and the time is accurate on the DCs. Users are complaining because they are getting late to join for the meeting because of these time differences. What could be the reason behind this & how can we rectify this?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-07-18*

Some general info    

-  All domain members should use NT5DS domain time.     

-  Desktops and member servers sync with any domain controller.     

-  Domain controllers sync with PDC emulator (one per domain)     

-  PDC emulator in child domain can sync with any domain controller in parent domain.     

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.    

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/    

Also you can follow along here.    

https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
