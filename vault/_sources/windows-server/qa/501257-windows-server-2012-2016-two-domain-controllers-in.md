---
title: "Windows server 2012 + 2016 two domain controllers in LAN without internet access. How to properly configure NTP server and client."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/501257/windows-server-2012-2016-two-domain-controllers-in
question_id: 501257
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows server 2012 + 2016 two domain controllers in LAN without internet access. How to properly configure NTP server and client.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/501257/windows-server-2012-2016-two-domain-controllers-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two domain controllers   

First one: windows server 2012 physical server. Let's name it the main domain controller;  DC1  

Second one: windows server 2016 virtual machine on a hyper-v host (which is not in the domain). DC2  

The main problem is that we don't have internet access, so we have to manually adjust the time on the main server.  

But now when I adjust time DC1, this doesn't apply to DC2.  

Even if I type w32tm /resync command on DC2 - it says it has been completed successfully, but the time still stays the same.  

How do I properly set the NTP server and clients, so if I change time on DC1 it gets synchronized with DC2 and all the clients?  

What is the proper way to do that? Via GPOs?   

Can you please share the settings for this installment?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-06*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

on all but the PDC emulator  

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

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
