---
title: "Error demoting Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/442772/error-demoting-domain-controller
question_id: 442772
fetched: 2026-07-25
answer_count: 19
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Error demoting Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/442772/error-demoting-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

I'm currently transfering the role of DC from two server to two other servers. The OS I am running is Windows Server 2019. I demoted one server without problems but when I try to demote my other server it gives the following error: "No other DC could be contacted but other DC are in the directory." In order to safely transfer to role of DC to the new DC's they need to be contacted before I proceed since forcing the demoting will break AC in my domain (I have tried this).    

When I go the AC sites and services the servers seem to replicate with eachother.   

Another problem is that w32time is broken on the old DC, that is why I'm trying to transfer the role to new DC's in the first place. I am not sure whether this is the cause of the problem.   

I tried altering the DNS settings: On the old DC the primary DNS points to a new DC and the secondary to itself. On the new DC the primary points to the old and the secondary to itself.   

Does anybody have any idea what I could do to fix this?  

Thanks in advance,  

Greetings Daniël

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-19*

The Windows Time service could not be stopped may need to reboot  

Also check that the Windows Time service is running on PDCe and that it is reachable by the problem domain controller.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-19*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

For all besides the PDCe  

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

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-19*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-18*

-  On DC1 I'd add server's own static ip address (192.168.50.111) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service    

-  On DC2 I'd add server's own static ip address (192.168.50.112) listed for DNS then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service    

-  SRV2 is multi-homed. Multihoming domain controllers will always cause no end to grief for active directory domain DNS Try disabling the other adapters.    

-  I'd remove the 192.168.50.102 address from all since it is not a domain controller    

-  I'd make sure the domain controller times are within ~5 minutes then also work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

if problems persist then put up a new set of files to look at.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-06-18*

At least correct the time manually. Otherwise please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
