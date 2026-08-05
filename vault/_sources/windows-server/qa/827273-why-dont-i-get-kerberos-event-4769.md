---
title: "why don't I get kerberos event 4769"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/827273/why-dont-i-get-kerberos-event-4769
question_id: 827273
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# why don't I get kerberos event 4769

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/827273/why-dont-i-get-kerberos-event-4769 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This article https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4769 describes kerberos service ticket events. I am having an issue with encryption type matching and want to examine what happens with these events, yet both of my domain controllers have no such event. I get the impression that it is something that happens often; so, why aren't there any event 4769 in the security logs? The logs go back about 6 days.    

Also, I thought that maybe I needed to enable event logging with the registry entry described here https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-kerberos-event-logging. I created that logLevel entry set to 1 and left it for a couple hours. Still nothing.    

domain controllers: Windows Server 2012 R2    

domain members: Server 2008 R2 - Server 2019

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-28*

Hi there,  

First of all, check your auditing settings:  

In the Group Policy Management Editor, choose Computer Configuration → Go to Policies → Go to Windows Settings → Go to Security Settings → Go to Local Policies → Go to Audit Policy. Set the following audit policies:  

-Audit account management: "Success"  

-Audit directory service access: "Success"  

-Audit logon events: "Success" and "Failure"  

You can also check if you have some objects which are out of auditing policy  

--If the reply is helpful, please Upvote and Accept it as an answer–
