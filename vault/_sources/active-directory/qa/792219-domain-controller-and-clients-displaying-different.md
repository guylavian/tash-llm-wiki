---
title: "Domain Controller and Clients displaying different times"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/792219/domain-controller-and-clients-displaying-different
question_id: 792219
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller and Clients displaying different times

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/792219/domain-controller-and-clients-displaying-different (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,  

I was hoping someone would help, for some reason our DC and computer clients are displaying different times, DC might display 15:18 and the client would display 15:21 and my phone would display 15:15, 3 different times, I am relatively new at fixing these types of errors and I am a bit concern by making changes to the time settings as this could brake authentication between the DC and the clients :(  

running w32tm /query /source on DC returns time.windows.com,0x9 and running the same command on the clients machines return the FQDN of the DC, DC is on a VM but the setting to sync time from the host is not ticked.  

I would really appreciate any help here.  

Best regards

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-03-29*

Up to 5 minutes differential is acceptable.    

Some general info    

-  All domain members should use NT5DS domain time.     

-  Desktops and member servers sync with any domain controller.     

-  Domain controllers sync with PDC emulator (one per domain)     

-  PDC emulator in child domain can sync with any domain controller in parent domain.     

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.    

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/    

If you needed high accuracy you could follow along here.    

https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
