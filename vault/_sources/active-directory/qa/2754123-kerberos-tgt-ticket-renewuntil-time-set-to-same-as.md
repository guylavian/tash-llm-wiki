---
title: "Kerberos TGT Ticket RenewUntil time set to same as End Time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2754123/kerberos-tgt-ticket-renewuntil-time-set-to-same-as
question_id: 2754123
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 11
qa_tags: []
---
# Kerberos TGT Ticket RenewUntil time set to same as End Time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2754123/kerberos-tgt-ticket-renewuntil-time-set-to-same-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a client where the Kerberos RenewUntil time for the TGT is set to the same time as the End Time of the ticket.

This causes us an issue as we have a service that can have a long running connection toa SQL database and this crashesif it is being used after the End Time has been reached.

The End Time is set to 10 hours (as standard) and the Renew Until time shows the same date and time when we look at it using KLIST TGT

This is the output from KLIST TGT:

C:\Users\XXXXXXX>klist tgt

Current LogonId is XXXXXXX

Cached TGT:

ServiceName        : krbtgt

TargetName (SPN)   : krbtgt

ClientName         : XXXXXXXXX

DomainName         : XXXXXXXXX

TargetDomainName   : XXXXXXXXX

AltTargetDomainName: XXXXXXXXX

Ticket Flags       : 0x40e00000 -> forwardable renewable i

Session Key        : KeyType 0x12 - AES-256-CTS-HMAC-SHA1-

                   : KeyLength 32 - 00 00 00 00 00 00 00 0

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

StartTime          : 10/6/2017 15:23:33 (local)

EndTime            : 
10/7/2017 1:23:33 (local)

RenewUntil         : 
10/7/2017 1:23:33 (local)

TimeSkew           :  + 0:00 minute(s)

EncodedTicket      : (size: 1528)

On our own servers and on most of our other clients the RenewUntil value is set to 7 days (or in some cases 30 days) after the StartTime. We have asked them to check their domain controller default policy settings and these all match ours:

Policy

Enforce user logon restrictions: Enabled

Maximum lifetime for sevice ticket: 600 minutes

Maximum lifetime for user ticket: 10 hours

Maximum lifetime for user ticket renewal: 7 days

Maximum tolerance for computer clock synchronization:
5 minutes

Can anyone explain why we see this. We need to rule this out as a cause of our problems, but it appears to be the most likely answer.

## Answer (community) — community member

*upvotes: 0 · updated: 2017-10-12*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet SQL Server Forums.

https://social.technet.microsoft.com/Forums/sqlserver/en-US/home?category=sqlserver

"MSDN SQL Server Forums"

https://social.msdn.microsoft.com/Forums/sqlserver/en-US/home?category=sqlserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
