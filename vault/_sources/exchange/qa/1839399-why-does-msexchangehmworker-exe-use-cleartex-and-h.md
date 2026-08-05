---
title: "Why does MSExchangeHMWorker.exe use clearTex and how can I solve this issue?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1839399/why-does-msexchangehmworker-exe-use-cleartex-and-h
question_id: 1839399
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Why does MSExchangeHMWorker.exe use clearTex and how can I solve this issue?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1839399/why-does-msexchangehmworker-exe-use-cleartex-and-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Why does MSExchangeHMWorker.exe use clear Texen and how can I solve this issue?

This log is related to this service:

LogName=Security

EventCode=4624

EventType=0

ComputerName=*******

SourceName=Microsoft Windows security auditing.

Type=Information

RecordNumber=3745106803

Keywords=Audit Success

TaskCategory=Logon

OpCode=Info

Message=An account was successfully logged on.

Subject:

Security ID: NT AUTHORITY\SYSTEM

Account Name: *

Account Domain: *

Logon ID: 0x3E7

Logon Information:

Logon Type: 8

Restricted Admin Mode: -

Virtual Account: No

Elevated Token: No

Impersonation Level: Impersonation

New Logon:

Security ID: **

Account Name: HealthMailbox9114d76

Account Domain: *

Logon ID: 0x1903D9441

Linked Logon ID: 0x0

Network Account Name: -

Network Account Domain: -

Logon GUID: {63624362-9c4c-0506-1390-edf73bc515d5}

Process Information:

Process ID: 0x2c7c

Process Name: C:\Program Files\Microsoft\Exchange Server\V15\Bin\MSExchangeHMWorker.exe

Network Information:

Workstation Name: *

Source Network Address: -

Source Port: -

Detailed Authentication Information:

Logon Process: Advapi

Authentication Package: Negotiate

Transited Services: -

Package Name (NTLM only): -

Key Length: 0

In Splunk, this log is fired for the so-and-so rule

I want to know why this service uses cleartext (logon type=8)

Is it a security issue? How do I fix it?

## Answers

_No answers on this thread._
