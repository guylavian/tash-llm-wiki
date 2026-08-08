---
title: "Syncing domain controller time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/727586/syncing-domain-controller-time
question_id: 727586
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Syncing domain controller time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/727586/syncing-domain-controller-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 Hyper-V virtual machine DC's and a regular DC that will be removed eventually.  

The DC's show different time.  

I would like to sync the DC time to time.windows.com,0x9 and have everything else sync to the DC.  

I have it set in local group policy on the DC vm to NT5DS time.windows.com/0x9 and the host set to NTP time.windows.com,0x9.  

However, the time is still off and I cannot manually change the time on any DC.  

What cmd is/other setting is needed to do what I need?  

What cmd is needed to point the time source of the other DC's to the PDC DC virtual machine?  

I do have one DC that isn't a vm but its w32tm source is the local CMOS.  

When querying the w32tm source on the virtual machine DC's, it says wm ic time synchronization provider and it seems like tinkering with that setting might not be wise.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-16*

I've tried cmd like that in the past and it didn't work.  

Other than the 1 physical DC using it's own CMOS time, the config I started with seems to be working.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-08*

This isn't right. Better to turn of Time sync in integration services,     

    

then on PDC emulator    

w32tm /unregister    

net stop w32time    

w32tm /register    

net start w32time    

w32tm /config /manualpeerlist:<ntp ip address> /syncfromflags:manual /reliable:yes /update    

net stop w32time    

net start w32time    

then check    

w32tm /query /source    

w32tm /query /configuration    

many can be found here.    

https://tf.nist.gov/tf-cgi/servers.cgi    

Some general info    

-  All domain members should use NT5DS domain time.     

-  Desktops and member servers sync with any domain controller.     

-  Domain controllers sync with PDC emulator (one per domain)     

-  PDC emulator in child domain can sync with any domain controller in parent domain.     

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.    

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
