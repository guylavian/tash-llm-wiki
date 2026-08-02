---
title: "Exchange Server 2019 Randomly falls over with .Net Runtime Errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1441799/exchange-server-2019-randomly-falls-over-with-net
question_id: 1441799
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2019 Randomly falls over with .Net Runtime Errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1441799/exchange-server-2019-randomly-falls-over-with-net (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Guys,

We have be running hybrid 2019 exchange now for over a year, and all of a sudden, we cannot login to ECP or Exchange powershell management, it was on cu12 with no new patches applied and suddenly just stopped with application and .net errors, tried to fix, but gave up and rebuilt a brand new server 2019, but this time installed exchange 2019 CU13, been running fine for a over a month, and then boom, same thing again, and no new patches installed either, two main errors below, just tried an inplace upgrade, which installed, but same error persists, anybody come across this before ?

Faulting application name: w3wp.exe, version: 10.0.17763.1, time stamp: 0xcfdb13d8

Faulting module name: clr.dll, version: 4.8.4645.0, time stamp: 0x648f6f63

Exception code: 0xc0000005

Fault offset: 0x0000000000018551

Faulting process id: 0x4f58

Faulting application start time: 0x01da211f8bc302ed

Faulting application path: c:\windows\system32\inetsrv\w3wp.exe

Faulting module path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\clr.dll

Report Id: 0e4bc20a-9467-467a-b09c-83a1666a4ac0

Faulting package full name: 

Faulting package-relative application ID: 

and

Application: w3wp.exe

Framework Version: v4.0.30319

Description: The process was terminated due to an internal error in the .NET Runtime at IP 00007FFA83E78551 (00007FFA83E60000) with exit code 80131506.

Cheers

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-27*

This was caused by a Trellix AV, removed it off the system and hey presto, works again.
