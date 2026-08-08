---
title: "Windows PDC use GPO to point Microsemi device IP addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67250/windows-pdc-use-gpo-to-point-microsemi-device-ip-a
question_id: 67250
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows PDC use GPO to point Microsemi device IP addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67250/windows-pdc-use-gpo-to-point-microsemi-device-ip-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a PDC windows 2012 r2 domain controller that I need to use GPO to point to multiple microsemi devices by IP.    

I"m following this article to the "T". https://theitbros.com/configure-ntp-time-sync-group-policy     

I'm getting hung up on the following GPO setting: Configure windows ntp client    

Am I to comma separate IP address values or just use spaces?    

Is this supposed to be reflect on the PDC servers registry? HKLM\SYSTEM\CurrentControlSet\Services\W32Time\Parameters    

Here are my settings     

After I apply, I run the following commands:    

gpupdate /force    

w32tm /resync    

w32tm /query /status    

And here is the output which I'm unsure if im to see all the IP's listed. I'm just making sure that my PDC is pointed properly so all my clients get updated. Is this also supposed to be reflective on the PDC's registry location?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-14*

You're welcome. Yes, as long as the clients are using domain time (NT5DS). Some general info;  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-14*

Thanks for your help, so now essentially my PDC points to a few GPS devices by IP addresses. And all my clients should continue to get time from my PDC correct?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-14*

I'd check the results of;    

`w32tm /query /configuration`  

--please don't forget to Accept as answer if the reply is helpful--
