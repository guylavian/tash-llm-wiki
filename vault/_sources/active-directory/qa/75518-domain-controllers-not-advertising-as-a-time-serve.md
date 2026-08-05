---
title: "Domain controllers not advertising as a time server - Preparing to migrate SYSVOL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/75518/domain-controllers-not-advertising-as-a-time-serve
question_id: 75518
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain controllers not advertising as a time server - Preparing to migrate SYSVOL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/75518/domain-controllers-not-advertising-as-a-time-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2012 R2 DC, Server 2016 DC.  

Forest level 2008 R2.  

Running this cmd: Dcdiag /e /test:sysvolcheck /test:advertising  

Shows both DC's aren't advertising as a time server.  

Ran the following cmd's on the 2012 R2 DC and no change:  

net stop w32time  

 w32tm /unregister  

 w32tm /register  

 net start w32time  

The AD replication tool from Microsoft shows no errors.  

This is in preparation of migrating SYSVOL from FRS to DFSR

## Answer (community) — community member [Mvp]

*upvotes: 4 · updated: 2020-08-24*

Some general info    

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

--On PDCe--    

`w32tm /unregister`  

`net stop w32time`  

`w32tm /register`  

`net start w32time`  

`w32tm /config /manualpeerlist:<ntp ip address> /syncfromflags:manual /reliable:yes /update`  

`net stop w32time`  

`net start w32time`  

then check  

`w32tm /query /source`  

`w32tm /query /configuration`  

--on all others--    

`w32tm /unregister`  

`net stop w32time`  

`w32tm /register`  

`net start w32time`  

`w32tm /config /syncfromflags:domhier /update`  

`net stop w32time`  

`net start w32time`  

then check  

`w32tm /query /source`  

`w32tm /query /configuration`  

for the migration you can follow along here.    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-16*

Well, I saw it disappear so ...
