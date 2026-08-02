---
title: "ADFS - configuration to support Multi Forest environment."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/46126/adfs-configuration-to-support-multi-forest-environ
question_id: 46126
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS - configuration to support Multi Forest environment.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/46126/adfs-configuration-to-support-multi-forest-environ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Friends,  

One our client is going to implement Cloud based SAP solution.   

Currently client is having 3 different Active Directory Forests and there is a trust between.   

The question is here, can we install one ADFS server and add and configure other AD forest as well and configure SAP application to use ADFS for authentication purpose.   

We are trying to understand whether it is doable and supported by Microsoft ( one ADFS server for Multi-Forest )   

Need your expert advice if you guys have come across such scenarios.   

Thanks in advance,  

Abul

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-07-13*

Yes, you should have bi-directional trusts between forest/Domains to use single ADFS instance   

Regards,  

Ganesamoorthy.S  

www.windowstricks.in
