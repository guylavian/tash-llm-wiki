---
title: "Domain Controller Windows Time Synchronization Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2845881/domain-controller-windows-time-synchronization-pro
question_id: 2845881
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Domain Controller Windows Time Synchronization Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2845881/domain-controller-windows-time-synchronization-pro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all, I'm configuring my domain controller (Windows Server 2012 R2) to be synchronized with pool.ntp.org but the w32time source still remain Local CMOS Clock. 

-  The PDC is a VM (VMware 6.0) and there is only this DC in the domain.   

-  I tried to use VM client to sync with NTP server and it is successful (I can see its port 123 UDP traffic from router NAT table), means the port didn't block. And the time for VM client has 5 minutes delay although synced with NTP server.  

-  already disabled VM client time synchronization to guest OS.  

-  Already restart and re-register the PDC w32time service, configure the pool.ntp.org peerlist successful, but when query status still pointing to Local CMOS Clock.  

-  When query configuration, type is 'NTP' and NTPServer is 'pool.ntp.org'  

-  No group policy about time server.  

-  Windows Firewall and antivirus already turned off

-  Already checked the Windows Time registry of PDC from other domain and the settings are same.

Any idea how to resolve this?

## Answer (community) — community member

*upvotes: 0 · updated: 2018-04-13*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
