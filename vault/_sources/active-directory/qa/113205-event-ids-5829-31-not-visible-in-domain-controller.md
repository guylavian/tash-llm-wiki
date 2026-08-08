---
title: "Event ID's 5829-31 Not Visible in Domain Controller logs after August 2020 Patches"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113205/event-ids-5829-31-not-visible-in-domain-controller
question_id: 113205
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Event ID's 5829-31 Not Visible in Domain Controller logs after August 2020 Patches

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113205/event-ids-5829-31-not-visible-in-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we have applied the August 2020 patches on our Domain Controllers but do not see any logs with Event ID 5829-5831 since the updates. There is at least one Server 2003 machine (i.e. out of support OS) on our domain which I assume is still using insecure Netlogon but I can't confirm this as I don't see it reflected anywhere in the logs.   

My suspicion was that we might have to enable and configure the included GPO: "Domain controller: Allow vulnerable Netlogon secure channel connections", but I don't want to enable it and then "allow" vulnerable connections just to test this.  

We also have non-Windows devices on our domain and I'm sure some of them are using insecure Netlogon connections to the DC's. Does anyone know how I can get the results I need in event viewer? I would like to be ready for the enforcement phase in February.  

Thanks.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-01*

On the suspect machines you can confirm via PowerShell    

`Test-ComputerSecureChannel`    

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/test-computersecurechannel?view=powershell-5.1    

As to Server 2003 its unlikely to apply unless it use AES for Secure RPC    

https://support.microsoft.com/en-us/help/3050509/improving-cipher-security-in-windows-server-2003-sp2    

This specific CVE only applies to AES for Secure RPC    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Yes, I'm aware of the information in that link and the description of how it is supposed to work, but there are no logs being generated for any of those Event ID's, so I can't tell if any machines on my network are using vulnerable netlogon to communicate. My concern is more for the out of support operating systems such as the Server 2003 machine on my domain which I suspect is using the old protocol, but I can't confirm this because the logging doesn't seem to be working properly. Is there an event ID which would confirm that secure RPC is being used by that machine?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Hello,    

Thank you so much for posting here.    

After the August 11, 2020 updates have been applied to DCs, events can be collected in DC event logs to determine which devices in your environment are using vulnerable Netlogon secure channel connections (referred to as non-compliant devices). Monitor patched DCs for event ID 5829 events. The events will include relevant information for identifying the non-compliant devices. To monitor for events, use available event monitoring software or by using a script to monitor your DCs.     

For more information about this, we could refer to the document provided by Dave.    

If we only install August 11, 2020 updates, non-compliant machines will be able to get logged on. Event ID 5829 is generated when a vulnerable connection is allowed during the initial deployment phase. These connections will be denied when DCs are in enforcement mode.     

Event ID 5830 will be logged when a vulnerable Netlogon secure channel machine account connection is allowed by "Domain controller: Allow vulnerable Netlogon secure channel connections" group policy.     

Event ID 5831 will be logged when a vulnerable Netlogon secure channel trust account connection is allowed by "Domain controller: Allow vulnerable Netlogon secure channel connections" group policy.     

Otherwise, we actually find some non-compliant devices, and we want "the Netlogon service deny vulnerable Netlogon secure channel connection from a machine account" and we does not set "Domain controller: Allow vulnerable Netlogon secure channel connections" group policy for Domain Controllers, we may receive Event ID 5827 and Event ID 5828.     

Event ID 5827 will be logged when a vulnerable Netlogon secure channel connection from a machine account is denied.     

Event ID 5828 will be logged when a vulnerable Netlogon secure channel connection from a trust account is denied.     

If we are sure that some machines are using insecure Netlogon connections, we could use available event monitoring software or by using a script to monitor for events.     

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-30*

This document explains how to manage the changes in netlogon secure channel  

https://support.microsoft.com/en-us/help/4557222/how-to-manage-the-changes-in-netlogon-secure-channel-connections-assoc  

--please don't forget to Accept as answer if the reply is helpful--
