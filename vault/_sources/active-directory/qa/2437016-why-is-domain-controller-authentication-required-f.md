---
title: "Why is Domain Controller authentication required for a local user connecting with SMB over TCP?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2437016/why-is-domain-controller-authentication-required-f
question_id: 2437016
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# Why is Domain Controller authentication required for a local user connecting with SMB over TCP?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2437016/why-is-domain-controller-authentication-required-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a smartphone that can access shared folders using SMB over TCP, but it can logon to my office computer (WinXP SP3) only if the PC is connected to the corporate network (on LAN or VPN), otherwise I get the following error:

Logon Failure:  

     Reason:        An error occurred during logon  

     User Name:    [local admin user]  

     Domain:        ?  

     Logon Type:    3  

     Logon Process:    NtLmSsp   

     Authentication Package:    MICROSOFT_AUTHENTICATION_PACKAGE_V1_0  

     Workstation Name:    JCIFS0_1_D3  

     Status code:    0xC000005E  

     Substatus code:    0x0

Which in short means "no domain controller available to authenticate user". That's a nuisance. Why would Windows check the DC to authenticate a local admin user over NTLM?

Could it be a limitation of SMB? Or should I change some Windows security settings?

Thank you,

/_urka

## Answer (community) — community member

*upvotes: 0 · updated: 2010-08-27*

Hi

The Network is probably configured this way for security reasons.

This question better adreesses to the IT people of the business.

Jack-MVP Windows Networking. WWW.EZLAN.NET
