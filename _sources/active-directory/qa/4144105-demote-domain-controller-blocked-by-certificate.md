---
title: "Demote Domain Controller blocked by Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4144105/demote-domain-controller-blocked-by-certificate
question_id: 4144105
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Demote Domain Controller blocked by Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4144105/demote-domain-controller-blocked-by-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moving 2012r2 Domain Controllers DC1 to new 2016 Domain Controllers DC01.

Roles for DNS & DHCP are already removed and now trying to remove AD

DC1 has Active Directory Certificate Services Role blocking me from Demoting the Server

How do I proceed to move Schema Master and Domain Naming Master to Windows 2016 DC01

Microsoft Windows [Version 6.3.9600] 

(c) 2013 Microsoft Corporation. All rights reserved. 

C:\Windows\system32>netdom query fsmo 

Schema master               DC1.mtc.mansion.rosewoodhotels.local 

Domain naming master        DC1.mtc.mansion.rosewoodhotels.local 

PDC                         DC01.mtc.mansion.rosewoodhotels.local 

RID pool manager   DC01.mtc.mansion.rosewoodhotels.local 

Infrastructure master   DC01.mtc.mansion.rosewoodhotels.local 

The command completed successfully. 

C:\Windows\system32>

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-07-28*

Hi, I'm David.

Sorry. The Microsoft Community is a forum for home users.

Due to the scope of your question, I suggest you access the link below, which will direct you to the Microsoft Q&A page.

https://learn.microsoft.com/en-us/answers/index...

Microsoft Q&A has IT professionals and system administrators who can best help with this type of question.

Best regards.
