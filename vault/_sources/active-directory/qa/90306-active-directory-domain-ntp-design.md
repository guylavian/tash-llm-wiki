---
title: "Active Directory Domain NTP Design"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/90306/active-directory-domain-ntp-design
question_id: 90306
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Domain NTP Design

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/90306/active-directory-domain-ntp-design (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 100 DC's in 8 countries ( US, UK, AUS, NZ, France and in Asia ) some DC's are in Azure, AWS and Vmware/xen hypervisors.  

Noticed some RDP login issues to Vmware servers and DNS issues to AWS.  

I thought PDC is set to external time source or load balancer and rest point to pdc.  

So how do i change all other dc's point back to PDC?  

Will location cause any issues?  

if PDC goes offline, do I have to configure the NTP to external on that server?  

AS

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-23*

Hi, Other answers are correct, the best option is to rely on AD for time synchronisation.  

I just want to add : beware of time sync with physical host on virtual server it may disturb the overall process.  

Solution is just to rely on AD and disable sync with host :)  

Hope this helps  

Alexandre

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-14*

Hello @Asela De Costa  ,    

Thank you for posting here.    

Although the Windows Time service is not an exact implementation of the Network Time Protocol (NTP), it uses the complex suite of algorithms that is defined in the NTP specifications to ensure that clocks on computers throughout a network are as accurate as possible.    

You can refer to the content of this link, hope it will help you：    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc773013(v=ws.10)?redirectedfrom=MSDN    

Best regards,    

Stephanie Yu    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-09*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

 https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

to point the members back to domain time (NT5DS)  

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

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-09*

Yes, it is a general practice to configure the Domain Controller that is running the PDC FSMO role to point to a NTP server.  At that point, all other domain controllers will get their time from the DC hosting the PDC FSMO role, just like all other domain members.  

If the DC hosting the PDC FSMO role goes offline, what you do depends upon how long it is expected to be off.  Generally there will be little time drift over short periods of time.  Domain controllers will continue to provide time for member servers.  If the PDC role is going to be down for more than a day or two, you may seize the PDC FSMO role to any other DC and then configure that DC to your NTP.
