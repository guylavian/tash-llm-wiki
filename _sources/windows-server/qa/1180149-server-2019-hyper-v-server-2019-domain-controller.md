---
title: "server 2019 hyper V server 2019 domain controller Ordinal Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180149/server-2019-hyper-v-server-2019-domain-controller
question_id: 1180149
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# server 2019 hyper V server 2019 domain controller Ordinal Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180149/server-2019-hyper-v-server-2019-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 2019 hyper V server 2019 domain controller I installed quick books and file doctor and reinstalled c++ multiple versions to get my network work shares working right, which wasn't right. Hence, I de-installed my virus software, thinking it was a firewall issue. After reboot, I continue to get ordinal errors; I cannot go to the control panel, services, etc. I tried to use DISM will only get to 4%. I cannot get installer services to work. I used REVOunistaller portable to remove the multiple versions of C++. It did remove, but I still cannot install the current version of C++. Seated, I can only get portable programs to work, but nothing will install. I've tried booting from the server disc, but repair does not work, and safe mode with networking does not work for some reason. It just reboots again back into regular mode.

I need to create users and modify my domain, but I got another Ordinal (355, 5815) error. I can access the command prompt, and I tried SFC / Scsannnow. It does not find anything wrong.

when trying to install C++ i get a setup failed (0x80070641)

The weird thing is that it changed my network settings after the reboot. I did reset my network settings as a precaution. I had to change my network adapter to an IP address I originally had.

Any suggestions? It's all related.

I get failed. I do have a server disc in the DVD drive to try and do an offline DISM, but I'm not doing something right because it will not work. Maybe my directory is not correct. I need the correct syntax.

Help, please.

Thank you

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-13*

Might try standing up a new one for replacement. I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-13*

The much cleaner / safer method is to install the hyper-v role (as only role) on host, then stand up two virtual machines, one for active directory domain services, and another as application server. Mixing other roles / applications on a domain controller, multi-homing are all recipes for disaster.

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
