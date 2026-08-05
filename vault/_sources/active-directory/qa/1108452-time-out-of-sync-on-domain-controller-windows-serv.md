---
title: "Time out of sync on Domain Controller Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1108452/time-out-of-sync-on-domain-controller-windows-serv
question_id: 1108452
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Time out of sync on Domain Controller Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1108452/time-out-of-sync-on-domain-controller-windows-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I created and promoted domain controller on my ESXi host.    

On the host I've got correct time:    

    

But on DC is not:    

    

I tried to repair w32tm on registry, but it doesn't fix it.    

I need to get correct time on DC, how to fix it? Before I haven't had this problem when I deployed DC.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-29*

I'd check the system event log for Time-Service events.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-29*

The NTP server used may be problematic. Might try another.    

https://tf.nist.gov/tf-cgi/servers.cgi    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-29*

Are you trying to sync with host? or with some other source?    

Some general info    

-  All domain members should use NT5DS domain time.     

-  Desktops and member servers sync with any domain controller.     

-  Domain controllers sync with PDC emulator (one per domain)     

-  PDC emulator in child domain can sync with any domain controller in parent domain.     

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.    

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
