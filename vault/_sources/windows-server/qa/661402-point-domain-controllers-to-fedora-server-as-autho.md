---
title: "Point Domain Controllers to Fedora server as authoritative time source"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/661402/point-domain-controllers-to-fedora-server-as-autho
question_id: 661402
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Point Domain Controllers to Fedora server as authoritative time source

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/661402/point-domain-controllers-to-fedora-server-as-autho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have a requirement to implement NTP with NTS for a client as they must have external time source updates authenticated. I am planning to deploy a Fedora server which supports NTS and sync this with Cloudflare. I'm presuming there is no issue with pointing Domain Controllers to the Fedora server for time source?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-14*

Hello @Alistair Russell       

This should mean no issue for the AD PDC. Here you have some useful command lines and settings for Windows: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/configure-authoritative-time-server    

Hope this helps with your query,    

--------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-12-13*

The following commands will help to configure an NTP server in your domain controller. Run the commands one by one in an elevated command prompt  

```
net stop w32time
w32tm /config /syncfromflags:manual /manualpeerlist:"fedora server ip/name"
w32tm /config /reliable:yes
net start w32time
w32tm /config /update
w32tm /resync
```

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-13*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

so you can point the PDC emulator to the new source.  

w32tm /unregister  

net stop w32time  

w32tm /register  

net start w32time  

w32tm /config /manualpeerlist:<ntp ip address> /syncfromflags:manual /reliable:yes /update  

net stop w32time  

net start w32time  

then check the results  

w32tm /query /source  

w32tm /query /configuration  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
