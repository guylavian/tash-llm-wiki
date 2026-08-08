---
title: "Domain Controller Restarting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197614/domain-controller-restarting
question_id: 2197614
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Domain Controller Restarting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197614/domain-controller-restarting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a DC running Server 2022 it is restarting in the Active directory environment only.

Steps I followed:-

scanned with AV

scanned all the clients with AV

updated driver and firmware

hardware health is ok

OS is up to date

unchecked automatic start

finally reinstalled the OS but still issue is same.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-26*

Hello akg2023,  

Thank you for your reply.  

Did you mean if this server is a server in workgroup, it will not restart (working fine)?  

Did you mean if this server is a member server in one domain, it will not restart (working fine)?  

However, if it is a Domain Controller, it will restart?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hi,

I don’t have those updates

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hello akg2023,  

Thank you for your reply.  

Please check if the following link helps.  

January updates causing unexpected reboots on domain controllers : r/sysadmin (reddit.com)

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hi Daisy,

Exactly only in domain controler, I did not configure task schedule, as you can see in the snap the lsass is failing.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hello akg2023,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description "I have a DC running Server 2022 it is restarting in the Active directory environment only.", did you mean when this server is only one server (not a domain controller), then it will not restart?  

2.How often does the domain controller restart?  

3.Check if you have configured any scheduled task to restart this domain controller or any script to restart this domain controller.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
