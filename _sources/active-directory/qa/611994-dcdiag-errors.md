---
title: "dcdiag errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/611994/dcdiag-errors
question_id: 611994
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# dcdiag errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/611994/dcdiag-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am getting the below errors on my primary domain controller DC1 while checking dc health. Does it need an authoritative or nor authoritative restore?

C:\>dcdiag /q  

Warning: DsGetDcName returned information for \dc1.domain.local, when  

we were trying to reach DC2.  

SERVER IS NOT RESPONDING or IS NOT CONSIDERED SUITABLE.  

......................... DC2 failed test Advertising  

Unable to connect to the NETLOGON share! (\DC2\netlogon)  

[DC2] An net use or LsaPolicy operation failed with error 67,  

The network name cannot be found..  

......................... DC2 failed test NetLogons  

An error event occurred. EventID: 0x00000014  

Time Generated: 10/30/2021 06:32:54  

Event String:  

Installation Failure: Windows failed to install the following update  

with error 0x80246013: 2021-04 Servicing Stack Update for Windows Server 2012 f  

or x64-based Systems (KB5001401).  

An error event occurred. EventID: 0x0000272C  

Time Generated: 10/30/2021 07:01:42  

Event String:  

DCOM was unable to communicate with the computer 8.8.8.8 using any o  

f the configured protocols; requested by PID 1300 (C:\Windows\system32\dcdia  

g.exe).  

An error event occurred. EventID: 0x0000272C  

Time Generated: 10/30/2021 07:02:03  

Event String:  

DCOM was unable to communicate with the computer 8.8.4.4 using  

any of the configured protocols; requested by PID 1300 (C:\Windows\system32  

\dcdiag.exe).  

......................... DC2 failed test SystemLog

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-01*

Hi @create share       

A DC restore might be a little extreme for a DNS error or is there more background on the issues you have been having with DC2?    

Gary.
