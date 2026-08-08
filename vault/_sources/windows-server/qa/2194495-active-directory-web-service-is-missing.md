---
title: "Active Directory Web Service is missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194495/active-directory-web-service-is-missing
question_id: 2194495
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory Web Service is missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194495/active-directory-web-service-is-missing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Two domain controllers running Server 2019 Standard.

Both are fully up to date.

Domain and Forest functioning level is 2016.

I recently attempted to open Active Directory Administrative Center (ADAC) on my PC.

RSAT installed and working no issue until this.

ADAC generates an error "Cannot connect to any domain. Refresh or try again when connection is available"

If I click "Ok" and click any bookmark, the first error is "The bookmarked item cannot be found or no longer exists."

The second error is "Cannot find an available server in the domain.com domain that is running the Active Directory Web Service (ADWS)"

The actual "Active Directory Web Service" within services.msc does not exist in either domain controller.

ADAC was working fine recently and now it does not work from my PC or on either DC.

All demonstrate the same error.

I have since found some powershell commands that point to the same missing ADWS service.

Get-ADUser command in powershell comes back with "Get-ADUser : Unable to find a default server with Active Directory Web Services running"

Both DCs are Global Catalogs

Both DC's are running DNS Server Service

One DC uses its own static IP as DNS server (not 127.0.0.1)

Second DC points to first DC for DNS

nslookup tests I did all seem to show correct information.

My first instinct was to check the health of Active Directory.

I ran "DCDiag /v" on both DCs

No errors on either other than reference to some occasional replication issues. (Usually happens during backups)

I ran repadmin /showrepl on both DCs

No errors reported.

I ran repadmin /replsum on both DCs

No erorrs reported.

It appears that AD is healthy.

How did ADWS dissapear?

As mentioned, ADAC worked fine up until as recently as a month ago.

I have no other symptoms manifesting themselves as problems and there seems to be no issues on the network I am aware of.

I am just a little leary this might be the beginning of a bigger issue.

I can find no info about ADWS going MIA.

Before I resort to moving FSMO roles and redoing Domain Controllers, I thought I would put this to the community to see if anyone else has seen/experienced this.

Input appreciated.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-08-28*

Hello   

Good day!

1) Is there anything I should watch out for once a server has been demoted from being a DC before I re-promote it?

A1: You had better use one server with different DC name and different IP (one server with different DC name and the IP).

Or you may need to rename this Demoted DC and re-promote it.

- Does demoting leave any kind of "mess" that needs cleaning up before promotion to a DC again?

A2: Before you re-promote the demoted DC, you had better perform metadata cleanup of this demoted DC so that all the records about the demoted DC are deleted completely.  

On the running and open DC, run the commands in the link below to perform metadata cleanup of this demoted DC.

petri.com

- Should I consider a complete wipe and reinstall instead of just re-promoting each of the two original servers?

A3: I think this may be the best option.

-  If I don't need to (not necessary) format and reinstall the OS on the servers (in your opinion) then that works because I have multiple locations within a SDWAN environment all looking to the one server for DHCP and both for DNS.

-  Conversely, I do like the idea of a fresh start...my opinion.

2) At any time during my outlined steps to repair, say between doing the 1st demote/promote, should I wait a few days/week and observe functionality before doing the second demote/promote?

A4: You can follow this idea, or you don't have to wait for a few days, but after each step, you need to confirm the working status of each domain controller itself and the AD replication status.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Good morning,

Confirmed. That directory exists on both DCs.

Does this mean the windows service can be reinstalled?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Hello

Good day!  

After you install AD DS role, there will be AD DS and ADWS services running in the services.msc console.

*This service provides a Web Service interface to instances of the directory service (AD DS and AD LDS) that are running locally on this server. If this service is stopped or disabled, client applications, such as Active Directory PowerShell, will not be able to access or manage any directory service instances that are running locally on this server.*Please check if there is ADWS folder and C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe on the DC.  

For example:

There is no ADWS on one server without ADDS role installed.  

For example:

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Good evening,

In answer to your questions...to be honest, the only reason I went looking for ADWS at all is because of the error I encounter when attempting to open ADAC so really, I never noticed or observed the ADWS service on either DC because everything was working fine.  One would assume ADWS MUST have been there for ADAC to be working before. As far as changes go, we made some vLan changes but that was early February this year and the vLan and IP subnet never changed for these two DCs. I know I used the ADAC with no issue between then and when I discovered this issue. 

I checked the Roles and Features as you suggested and they are installed exactly as you have shown with one exception.

Where you show ".NET Framework 4.8"; I am showing ".NET Framework 4.7" as shown below. I did notice you mentioned 4.7 in bullet 4 so I am assuming this isn't a show stopper.

The rest looks the same:

Other than an annoyance, the issue (so far) does not seem detrimental to AD but I was hoping this was a simple oversight on my part.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-10*

Hello Kur_gen,  

Thank you for posting in Microsoft Community forum.  

Have you seen the Active Directory Web Service before on the two Domain Controllers? If so, what changes have you made before the Active Directory Web Service missing?

If the Active Directory Web Service is missing on two domain controllers running Server 2019 Standard, you can try the following steps to resolve the issue: 

-  Open the Server Manager on the affected domain controllers. 

-  Click on Add Roles and Features. 

-  Click Next until you reach the Features section. 

-  Expand the .NET Framework 4.7 or .NET Framework 4.7 Features.   

5.Check if these roles below are installed.

After the installation is complete, the Active Directory Web Service should be available on the domain controllers. If the issue persists, you may need to check the event logs for any related errors 

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
