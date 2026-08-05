---
title: "Windows 10 TWAIN drivers and GPO (.ds file)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3207769/windows-10-twain-drivers-and-gpo-ds-file
question_id: 3207769
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 22
qa_tags: []
---
# Windows 10 TWAIN drivers and GPO (.ds file)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3207769/windows-10-twain-drivers-and-gpo-ds-file (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I was wondering if anyone run to this issue. We are having problems with installing drivers for Fujitsu scanners in our Windows 10 Enterprise environment. Looks like this might be related to our GPO policy but we can't pin
 point it. Here is the issue:

Just installed approved TWAIN drivers for fujitsu scanner (PaperStream IP) on Windows 10 device . After plugging the scanner to the USB port the system should detect and create a model specific .ds file in C:\Windows\twain_32\Fjicube

-  unfortunately nothing happens. 

-  We already ruled out antivirus settings and permission settings.

-  We did run ProcMon but unfortunately nothing happens after we plug in the scanner to the USB port. Just a note – the WIA drivers are installing correctly and we can see the scanner in Device
 Manager.

-  The WIA, Shell Hardware detection and Remote Procedure Call (RPC) services are up and running

-  We already tried local admin account – same issue

We moved our test Windows 10 device to “No GPO” AD group (no group policies applied), plugged the scanner into an USB, the system picked it up, created the model specific .ds file in  C:\Windows\twain_32\Fjicube
 and now our TWAIN software is working as a charm.

Any idea what can block this very specific procedure on windows 10?

Thanks

Marek

## Answer (community) — community member

*upvotes: 1 · updated: 2019-08-19*

Hi Marek

My name is Andre Da Costa; an Independent Consultant, Windows Insider MVP and Windows & Devices for IT MVP.  I'm here to help you with your problem.

Sorry for the inconvenience of having to suggest the re-route, but Technet has a lot of experts there that know the ins and outs of enterprise issues; especially domain configurations for clients, Windows 10 deployment and migration. So, they will be better able to diagnose and determine whats causing the block. 

Thanks for your corporation.

Technet forums - Windows 10 IT Pro - Microsoft

https://social.technet.microsoft.com/Forums/en-...
