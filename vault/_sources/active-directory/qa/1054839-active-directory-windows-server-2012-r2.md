---
title: "Active Directory - Windows Server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1054839/active-directory-windows-server-2012-r2
question_id: 1054839
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory - Windows Server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1054839/active-directory-windows-server-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

 I want to update the NTP time source on my Domain Controllers as we're updating our NTP appliances. The commands I've seen to do this are:    

w32tm.exe /config /syncfromflags:manual /manualpeerlist:10.1.1.1,0x8 10.1.1.2,0x8 /reliable:yes /update    

The question I have is what does the 0x8 do? Is it needed?    

From reading below, I still don't know the difference between setting 0x8, 0x1 or something else.    

https://learn.microsoft.com/en-us/services-hub/health/remediation-steps-ad/configure-the-root-pdc-with-an-authoritative-time-source-and-avoid-widespread-time-skew    

https://jackstromberg.com/2013/10/configuring-external-time-source-on-your-primary-domain-controller/    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/time-synchronization-not-succeed-non-ntp    

Please advise    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-20*

Thanks Jimmy,    

 The bit I was missing was understanding the context, in essence if you're syncing with a non Windows NTP server, then use 0x8 for client mode?
