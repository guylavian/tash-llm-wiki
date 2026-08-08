---
title: "GPO-Security Updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199937/gpo-security-updates
question_id: 2199937
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# GPO-Security Updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199937/gpo-security-updates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I require some advice regarding updates and Security GPO Server Hardening.

Recently i was given a mini project to harden all our W2012 servers which are all out of contract and microsoft do not provide any further updates for this version of windows. I have been tasked with creating a GPO to harden the security policies of these servers. When I Depp-Dived the issues on the servers I noticed that they have not been patched since Microsoft stopped free updates 3 years ago. Basically we have not paid for any ESU on these servers X5.

My question is how on earth can I create a GPO and harden the servers when they are not fully patched. Surely they should all be fully patched first before I embark on this project to apply a Security hardened GPO to the 5 servers?

Does anyone have any advice\thoughts on this.

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-24*

Hello czql5v007,  

Thank you for posting in Microsoft Community forum.  

Surely they should all be fully patched first before I embark on this project to apply a Security hardened GPO to the 5 servers?  

A: You should install all patches via ESU first, and then apply a Security hardened GPO to the 5 servers.  

For security baseline, you can read links below.   

Secure Windows Server 2012 R2 and Windows Server 2012 | Microsoft Learn

Security baselines guide - Windows Security | Microsoft Learn

Download Security Compliance Toolkit and Baselines from Official Microsoft Download Center  

Here is a similar thread about GPO hardening (server 2019).  

Windows 2019 Hardening Guide - Microsoft Q&A

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
