---
title: "Unable to get domain/domain controllers to use external time service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/350063/unable-to-get-domain-domain-controllers-to-use-ext
question_id: 350063
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Unable to get domain/domain controllers to use external time service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/350063/unable-to-get-domain-domain-controllers-to-use-ext (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

2008R2/2019 DC's. (process of retiring the 2008R2)    

When querying source, it is either the root PDC or CMOS (on the PDC).    

After changing the PDC to another server other servers were still pointing to the old PDC and the old PDC was still showing CMOS as the source.    

2008R2 is the old PDC. 2019 is the new PDC.    

Even after running the commands in this guide, the 2019 was till pointing to the 2008R2 and 2008R2 was still using the CMOS.    

configure-the-root-pdc-with-an-authoritative-time-source-and-avoid-widespread-time-skew    

I would like my domain to use an external time service.    

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-14*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-09*

Glad to hear of success. As to the minute difference it should correct. Windows does not step time, unless certain bounds are exceeded, but rather disciplines the clock. That means w32tm adjusts the frequency of the clock at a regular interval, using the Clock Update Frequency setting, which defaults to once a second with Windows Server 2016. If the clock is behind, it accelerates the frequency and if it's ahead, it slows the frequency down. However, during that time between clock frequency adjustments, the hardware clock is in control. If there's an issue with the firmware or the hardware clock, the time on the machine can become less accurate.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-09*

I had run DSPatrick's cmd's in the past and did another query source and looks like it is now pointing to an external server now.  However, the 2 DC are less than a minute apart (both have the same query outputs) and both are about a minute ahead of my non-domain computer set on auto time config.  

The old dc has not been demoted yet.  

new dc  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters  

Key Name: NtpServer  

Type: REG_SZ(String Value)  

Data: Peers  （external ip address,0x8）  

old dc  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\Type  

Key Name: Type  

Type: REG_SZ(String Value)  

Data: 0x5  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\Type  

Key Name: Type  

Type: REG_SZ(String Value)  

Data: NTP  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters  

Key Name: NtpServer  

Type: REG_SZ(String Value)  

Data: Peers  （external ip address,0x8）

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-09*

Hi,  

Welcome to ask here!  

After changing the PDC to another server, the old DC demoted or still act as DC?  

If still act as a DC, the time source for the clients has no issues.  

If the old PDC was demoted, then we need to make the clients to sync time with DCs.  

We just need to make the old DC to sync time with the new PDC.  

On the PDC, make sure the following registry values were right:  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config  

Key Name: AnnounceFlags  

Type: REG_DWORD (DWORD Value )  

Data: 0x5  

   

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\Type  

Key Name: Type  

Type: REG_SZ(String Value)  

Data: NTP   

   

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters   

Key Name: NtpServer  

Type: REG_SZ(String Value)  

Data: Peers  （time.windows.com,0x9）  

On the old DC, make sure the following registry values were right:  

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\Type  

Key Name: Type  

Type: REG_SZ(String Value)  

Data: NT5DS  

   

Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config  

Key Name: AnnounceFlags  

Type: REG_DWORD (DWORD Value )  

Data: 0xa  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-08*

Some general info  

-  All domain members should use NT5DS domain time.   

-  Desktops and member servers sync with any domain controller.   

-  Domain controllers sync with PDC emulator (one per domain)   

-  PDC emulator in child domain can sync with any domain controller in parent domain.   

-  PDC emulator in parent domain syncs with either a hardware clock or possibly an external source.  

https://blogs.technet.microsoft.com/nepapfe/2013/03/01/its-simple-time-configuration-in-active-directory/  

On the PDC emulator  

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

--please don't forget to Accept as answer if the reply is helpful--
