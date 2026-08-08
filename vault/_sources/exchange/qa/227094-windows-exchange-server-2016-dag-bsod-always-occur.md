---
title: "Windows Exchange server 2016 DAG BSOD always occurred"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227094/windows-exchange-server-2016-dag-bsod-always-occur
question_id: 227094
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Windows Exchange server 2016 DAG BSOD always occurred

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227094/windows-exchange-server-2016-dag-bsod-always-occur (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a DAG consists two nodes which are running with Exchange 2016 version 15.1 (Build 1847.3). Both nodes are based on VMware vsphere server 6.5 and feed a 128GB RAM and Dell ME4012 full SSD HD array. Both were having BSOD issue always, the date of happening was randomly, it's very strange of that,  not only one the nodes but both of them were BSOD at the same time. From the mini-dump file we can see the application SVCHOST.EXE crash.  I checked VMware resource, total are no problem, we tried install Windows updates but nothing changed.     

Appriciated a lot for andy advise. Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

Agree with Andy, you shoule first check the logs there.    

You can also follow this article to troubleshoot: https://techcommunity.microsoft.com/t5/exchange-team-blog/what-did-managed-availability-just-do-to-this-service/ba-p/593304    

Did you meet the BSOD issue before creating DAG? Try removing the failover cluster feature, reboot, re-enabl failover cluster feature and see if it works.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-12*

Check the Managed Availability logs and see if Exchange itself is initiating these reboots:    

https://www.codetwo.com/admins-blog/managed-availability-in-exchange-2013/    

(applies to 2016 as well)
