---
title: "Active Directory losing network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/596136/active-directory-losing-network
question_id: 596136
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory losing network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/596136/active-directory-losing-network (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

experiencing a problem last days when our Domain Controller becomes inaccessible by Domain Computers.  

It happens once a week and when we restart an external Cisco switch that is conneced to the server, everything becomes normal.  

The same switch is used by other computers and they normally work but DC server, which is a VM hosted  

on a Hyper-V Core Server, stops working with no reason. The Hyper-V Core Server host is also accessible without problem,   

connected to the same switch.   

So, we think that the switch is not a problem, it could be something on the DC virtual machine that is cleaned up by restarting the switch,  

i.e by resetting the host or VM network adapters. In Event Log on the DC virtual machine and in the Event Log of the Core Hyper-V server   

we can not find anything related to the problem. Both, DC and Hyper-V Core server are running windows 2016 Server OS.  

Please can you advice me about  what could cause behavior like this?  

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-20*

Hi Dave,   

thank you very much,   

yes, it's possible that this config that is done in the past causes these problems.  

I will let you know what is outcome of the new setting, We have to wait at least one week to see :-)  

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-20*

Hi Dave,   

on more detail, the IP address of primary DNS (the DC itself) I added yesterday because it was missing, i.e the primary DNS was configured   

with IP address of external DNS which is now secondary. So, this configuration is set after we restarted the switch and we can see, if the problem happens again then it means it did not help.  

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-20*

Hi  Dave,   

thank you for the answer, I uploaded the logs to Onedrive, here is the link:  

https://1drv.ms/u/s!AphlujMliJTba4DOst-vqz3NeM8?e=4SXGcE  

I put dc log only for one dc since we have only one dc in our network.  

I did not upload problemworkstation log because when problem happens all workstations have problem with communication to DC.  

All workstations are in the same network as DC (192.168.100.x). If you still need it, please tell me and I will ask one of users to send me the log.  

Regards.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-10-19*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
