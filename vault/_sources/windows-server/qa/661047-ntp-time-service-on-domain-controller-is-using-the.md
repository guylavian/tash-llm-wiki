---
title: "NTP Time service on Domain Controller is using the wrong Reg key"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/661047/ntp-time-service-on-domain-controller-is-using-the
question_id: 661047
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# NTP Time service on Domain Controller is using the wrong Reg key

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/661047/ntp-time-service-on-domain-controller-is-using-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

I just found out our DC01 server (a virtual server 2012 R2 box),   

under Regedit:   

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\w32time\Parameters -   

NTPserver key is actually pointing to one of the old IP which does not exist any more.....  

I don't know why or who set it up like this.   

How can I rectify this situation? Does it mean this whole time DC01's time service is pointing to nothing....What value should this key hold? Can I safely change it to a different value like time.windows.net?   

Thanks  

ML

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-12-13*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

On the PDC emulator  

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

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-14*

Hello @Namless Shelter       

Yes, in this case, the machine may have been receiving NTP sync from the Host through Hyper-V Integration Services, but it is recommended you configure an authoritative time server for your domain:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/configure-authoritative-time-server    

Hope this helps with your query,    

----------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-14*

No worries, it does not work like that.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/configure-w32ime-against-huge-time-offset    

domain members are unaware of differences between the PDC emulator and its configured time source. If the time is off by a large delta then you could manually correct it in small increments beforehand.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-14*

Sure, you can try anything you like. The issue is not knowing what is lingering. Better option is to delete / recreate the service as I've shown above.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-13*

Usually, the time source is a hardware clock or an internet time source. Whatever is being used; use the ip address in the commands I posted above. Manual registry editing is very much error prone and too complex to discuss in forums. Better to start a case with microsoft product support for that. W32tm is a much cleaner / simpler method.     

https://learn.microsoft.com/en-us/archive/blogs/nepapfe/its-simple-time-configuration-in-active-directory    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
