---
title: "Explicit Deny GPO configured on Windows Server 2012 R2 Standard not working for Windows 10"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2746991/explicit-deny-gpo-configured-on-windows-server-201
question_id: 2746991
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Explicit Deny GPO configured on Windows Server 2012 R2 Standard not working for Windows 10

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2746991/explicit-deny-gpo-configured-on-windows-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

First of all, thank you for anyone who can provide any insight on my problem.

Problem: I have a GPO configured on Windows Server 2012 R2 Standard that is configured to push a login agreement where the user has to click "OK" to log into their machine. I have a security group set up to explicitly deny this GPO from
 deploying to certain machines. This GPO is running with a Windows 7 WMI filter and
works perfectly fine. I created the same GPO for my Windows 10 machines using a Windows 10 WMI filter and the explicit deny is not being applied so the log on agreement is being push to computers that should not be getting them (computers that
 are set up to auto-login). 

I have the deny set up in the delegation tab for the respective GPO exactly like the Windows 7 variant, which works perfectly fine.   

Any help with figuring this out will be a great help. 

Sincerely,

Nic

## Answer (community) — community member

*upvotes: 0 · updated: 2017-05-12*

Hi,

Your question is beyond the scope of these Forums

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
