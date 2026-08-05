---
title: "Servers lose hour configuration, domain GPO."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/820517/servers-lose-hour-configuration-domain-gpo
question_id: 820517
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Servers lose hour configuration, domain GPO.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/820517/servers-lose-hour-configuration-domain-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Wen have some problems with some servers that they had the time 3 minutes out of phase. DCs are corrects, they synchronize with a an external source without problems.    

I have configured a GPO to force clients to synchronize with DCs with this options:    

    

The crossed out part is our DC PDC.    

After a few days i check some servers with w32tm /query /source and some had de PDC as source but other had Local cmos clock. I checked this servers and they had the correct GPO option configuration in     

With this servers dont take the PDC as source?    

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-18*

I have been checking events and i found the problem. We have two DCs, DC1 have all roles. DC1 take the hour of an external source.   

The most of servers has like time source DC2.   

DC1 have time-service events, 50  

DC2 have time-service events, 24, 50 and 124.   

1 - If the GPO is configured with the DC1 as a time source why the most of servers have DC2 as a time source ?  

2 - Why there are time-service events ? both DCs are in the same vlan. DC1 has no conectivity problems with his external time source.  

Many thanks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-11*

Why i put the commands in a .bat file:  

Why are you doing that?
