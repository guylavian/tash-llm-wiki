---
title: "certificate for server core domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/700561/certificate-for-server-core-domain-controller
question_id: 700561
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# certificate for server core domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/700561/certificate-for-server-core-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

I deployed server core 2019 domain controller in my forest.  

Existing 2012R2 domain controllers receiving certificates vai autoenrollment policy.  

However Automatic certificate enrollment  via GPO does not get applied for server core domain controller.  

I have offline Root CA and SUBCA in my forest. This is single domain domain forest.  

Queries   

1.)Does server core does not support autoenrollment ?   

2.)Do I need to use CSR method ? to get the certificate for server core domain controller  

3.)Manually I have to request the certificate via MMC from a different server?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-16*

Hello.  

try to use this link :  

managing-windows-pfx-certificates-through-powershell-3pj
