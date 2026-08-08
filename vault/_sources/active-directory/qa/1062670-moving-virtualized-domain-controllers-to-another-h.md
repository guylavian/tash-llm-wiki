---
title: "Moving Virtualized Domain Controllers to another host (hyperv to hyperv)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1062670/moving-virtualized-domain-controllers-to-another-h
question_id: 1062670
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Moving Virtualized Domain Controllers to another host (hyperv to hyperv)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1062670/moving-virtualized-domain-controllers-to-another-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have upgraded our Hypervisor. It was previously Windows Server 2012 R2 and it has two VMs (DC1 and DC2, both Windows Server 2012 R2). Yes I know this isn't a good design and we'll be moving one DC to another host once we procure a new server.     

The upgrade (clean install of HyperV Server 2019) went well and the VMs were moved. The VMs can be started and I can login to them but they don't like the new host/hypervisor or the move itself. All the domain functions stopped working although the services are up (ie: DNS, ADDS, etc.):    

-  It will not authenticate any login requests    

-  Group Policy Management can't be loaded (saying it cannot find our forest/or there is no DC while it is the DC)    

-  AD users and computers can't be launched either (also saying the domain doesn't exist or can't be contacted)    

This likely is occurring because of the new NIC that gets created but I made sure that the new NIC has the same configurations (and deleted the old NIC). The funny thing is that on the first login it properly displays our domain name and shows Domain as the Network profile. However after a reboot it gets changed to either Private or Public network profile and it will never go back to Domain. We already tried restarting the NLA service as well as putting it on the delayed start.     

We also tried:    

-  Importing the VMs    

-  Import after copying the VM files as well as the Virtual Machine Disks    

-  Creating a new VM with the Virtual Machine Disks    

-  Do a restore using Altaro    

-  Try performing the Altaro restore to another Windows Server 2012 R2 host in case this was coming from the NIC that gets created by HyperV 2019    

-  Power on the DC VMs with no virtual switch - the DCs still cannot access themselves for domain data.     

What gives? If I remember correctly I could just move the virtualized DCs either way. Am I missing something?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-26*

Please run;    

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

then put `unzipped` text files up on OneDrive and share a link.
