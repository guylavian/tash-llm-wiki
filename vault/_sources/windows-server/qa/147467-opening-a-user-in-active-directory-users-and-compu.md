---
title: "Opening a user in Active Directory Users and Computers causes an unexpected restart with 1 minute warning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147467/opening-a-user-in-active-directory-users-and-compu
question_id: 147467
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Opening a user in Active Directory Users and Computers causes an unexpected restart with 1 minute warning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147467/opening-a-user-in-active-directory-users-and-compu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a Windows Server 2016 Datacenter edition on Amazon Web Services.  

I recently upgraded it to a domain then did the quick start for remote desktop services.  

The system reboots whenever I try to edit a user in Active Directory Users and Computers.  Previously this worked fine.  It is otherwise stable.  

The Active Directory Users and Computers program reports:  

The following active directory domain services error occurred:  The server is not operational  

followed by:  

Your PC will automatically start in one minute  

The application event log reports  

Source: wininit  

A critical system process, C:\Windows\system32\lsass.exe, failed with status code c0000005.  The machine must now be restarted.  

Event ID: 1015  

and  

Source:  Application Error  

Event ID: 1000  

Faulting application name: lsass.exe, version: 10.0.14393.2580, time stamp: 0x5bbdaebc  

Faulting module name: lsadb.dll, version: 10.0.14393.3866, time stamp: 0x5f2c805e  

Exception code: 0xc0000005  

Fault offset: 0x000000000000dddd  

Faulting process id: 0x33c  

Faulting application start time: 0x01d6b07cf813f274  

Faulting application path: C:\Windows\system32\lsass.exe  

Faulting module path: C:\Windows\system32\lsadb.dll  

Report Id: d35f3550-217f-486f-a672-a1aebd96b79f  

Faulting package full name:   

Faulting package-relative application ID:   

The system log reports  

Source:  Eventlog  

Event ID:  6008  

The previous system shutdown at 1:33:46 PM on 11/1/2020 was unexpected.  

Would you please assist me in returning Active Directory Users and Computers to normal operation and preventing these unexpected shutdowns.  Let me know what additional details you need.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-01*

Not really, you can also start a case here with product support but they'll tell you the same thing.  

https://support.serviceshub.microsoft.com/supportforbusiness  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-01*

Are there any options that wouldn't require a new virtual machine?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-01*

The roles are likely conflicting. I'd suggest standing up a dedicated virtual machine for active directory domain services.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-01*

Under Server Manager the following roles are showing:  

AD DS  

DNS  

File and Storage Services  

IIS  

Multipoint Services  

Print Services  

Remote Desktop Services  

Local Server  

All Servers  

Thank you for your interest,  

Ben

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-01*

What other roles are installed? Sounds like active directory domain services is somehow broken. I'd start with errors found in the system event log.  

--please don't forget to Accept as answer if the reply is helpful--
