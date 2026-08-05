---
title: "Memory leak in Windows kernel with GPO setting \"Audit System Integrity\" set to \"Success and Failure\" (Windows 2016 Server and Windows 10)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3182587/memory-leak-in-windows-kernel-with-gpo-setting-aud
question_id: 3182587
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Memory leak in Windows kernel with GPO setting "Audit System Integrity" set to "Success and Failure" (Windows 2016 Server and Windows 10)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3182587/memory-leak-in-windows-kernel-with-gpo-setting-aud (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello to all

I have detected a memory leak in Windows kernel

Environment:  

2016 Server (2016 DataCenter edition) acting as a domain controller  

Windows 10 workstations (Windows 10 Enterprise 2016 LTSB) and 

2016 Servers (2016 DataCenter editions) in other roles, such as terminal servers.

Occurs on:  

Both Windows 2016 Servers and Windows 10 Workstations  

Most likely the problem also occurs on lighter editions of Windows OS.

The culprit, security-hardening GPO setting, set into the domain controller:  

"Advanced Audit Policy Configuration"  

  "System"  

    "Audit System Integrity"  

      "Success and Failure"  

For example, Microsoft's recommendation 

"SCM Windows Server 2016 - Member Server Baseline - Computer (20180219)"

sets this GPO setting   

Symptoms:  

Any application that is started leaks 5-20 kB memory on the kernel side.  

Servers and workstations run out of memory after 1-2 weeks, depending on the operating conditions.  

The Taskmanager does not show any application using huge amounts of memory,   

just that the total amount of available memory gets lower and lower.  

It does not seem to matter if the application is 32-bit or 64-bit.

Steps to verify:  

-  Install poolmon from the Windows Driver toolKit (WDK) into the target machine  

-  You can use any test application or create a test .cmd file containing  

   @echo off  

   :loop  

   cmd /c "echo foo"  

   timeout /t 1  

   goto loop  

-  Set the GPO setting so that it applies in the target machine,  

   preferably in a domain environment and by using "gpupdate /force"  

-  Start poolmon from the command prompt using the following command-line  

   poolmon -b -iToke  

-  Start the .cmd file created in step 2 from the command prompt  

-  Watch the amount of kernel memory used by driver tag "Toke" to get ever higher, about 5-10 kB every screen update  

   Eventually this eats up all available memory.  

-  After a while, set the GPO setting from "Success and Failure" to "Failure" only.  

   Use "gpupdate /force" if needed. The memory counters reported by poolmon should stabilize shortly.  

   After a while, the memory counters of the driver tag should remain somewhat constant instead of growing all the time.  

Notes:

Some other driver tags also show ever growing memory counters such as "SeAt" tag,

but the "Toke" tag had the highest counter values.

This was tested originally on virtual machines.  

I'd like to have this problem corrected on the kernel side.

// U

## Answer (community) — community member

*upvotes: 0 · updated: 2019-02-11*

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
