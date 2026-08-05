---
title: "Upgrade of Windows Domain controller from 2012 r2 to 2022 and member servers supported list."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195834/upgrade-of-windows-domain-controller-from-2012-r2
question_id: 2195834
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Upgrade of Windows Domain controller from 2012 r2 to 2022 and member servers supported list.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195834/upgrade-of-windows-domain-controller-from-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,

We are upgrading our domain controllers from 2012 r2 to 2022.

Forest and domain functional level are 2003 for 2012 r2

Below list of member servers and workstations currently running

Windows Server 2012 R2

Windows Server 2016 1607

Windows Server 2008

Windows Server 2008 R2

Windows 7

Windows Server 2012

Windows Server 2003

Windows 8.1

With exchange 2007 (SMTP) and exchange 2013 Hybrid

With 2022 domain controller forest and domain functional level will be 2012.

we will uninstall the exchange 2007 and move the SMTP to Exchange 2013

I want to know more about, after upgrading the AD to 2022, existing member servers of 2003, 2008 will continue to work?

Exchange 2007 I must uninstall as it will not support domain controller of 2022 with forest and domain functional level of 2012.

Any suggestions and recommendations appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

Hello mohammedarifuddin ,

Yes, Windows XP, Windows 7, and Windows 8 clients can still work with a Windows Server 2022 domain controller with a forest and domain functional level of 2012. However, it's important to note that Microsoft no longer provides support for Windows XP and Windows 7, and support for Windows 8 has ended as well. This means that these operating systems may not receive security updates and patches, which could leave them vulnerable to security threats. It's recommended to upgrade to a newer operating system that is still supported by Microsoft.

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

Hello Qiuyang,

Just got to know there are some windows older clients such as windows xp, windows 7 and windows 8, so this machines will still continue to work after upgrading to windows server 2022 domain controller with forest and domain functional level as 2012.

Regards,

Arif

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

Hello mohammedarifuddin ,

Greetings! Let me know if you have any further questions.

Best regards,

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

Hello Qiuyang,

Thank you for your reply, appreciated.

Regards,

Arif
