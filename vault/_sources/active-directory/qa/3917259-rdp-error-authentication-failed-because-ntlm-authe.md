---
title: "RDP Error \"Authentication failed because NTLM authentication has been disabled\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3917259/rdp-error-authentication-failed-because-ntlm-authe
question_id: 3917259
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 31
qa_tags: []
---
# RDP Error "Authentication failed because NTLM authentication has been disabled"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3917259/rdp-error-authentication-failed-because-ntlm-authe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If this has been covered, I ask that someone point me to a solution. I have the following two devices:

Workstation with Windows 11 24H2

Laptop with Windows 10 22H2

Home server with Linux Mint 22.1 Cinnamon Version 6.4.6

Using my Windows 11 WS, if I attempt to RDP to my Laptop, I get the NTLM error.  I can RDP to my Linux Mint server without issue.  I have not attempted an RDP from the Linux Mint server to my Windows 11 WS as I will not have a use for that.

Using my Windows 10 Laptop, I cannot RDP to my Windows 11 WS because of another issue:

https://answers.microsoft.com/en-us/windows/forum/windows_11-desktop/credssp-encryption-oracle-remediation-error-using/f97da553-cf6b-40a9-af24-7b75305f8ae4

Getting the three of these machines to talk to each other has been a struggle.  Any help to resolve the two issues with my Windows machines will be greatly appreciated.  Thank you.

## Answer (community) — community member

*upvotes: 5 · updated: 2025-01-31*

I have resolved my own issue.  I went to sysdm.cpl>>Remote

Uncheck "Allow connections only from computers running Remote Desktop with Network Level Authentication (recommended)

This was checked on my Windows 11 and Windows 10 computers.
