---
title: "Eventid 37: Kerberos-Key-Distribution-Center Warnings after installing November 2021 Updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/637506/eventid-37-kerberos-key-distribution-center-warnin
question_id: 637506
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Eventid 37: Kerberos-Key-Distribution-Center Warnings after installing November 2021 Updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/637506/eventid-37-kerberos-key-distribution-center-warnin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,  

i´ve three Windows Server 2019 Domain Controllers (build 17763) in a single Domain. After installing the regular MS Updates yesterday, KDC Warnings with Eventid 37 are floating the Systemlog on all DCs.  

Sample:  

The Key Distribution Center (KDC) encountered a ticket that did not contain information about the account that requested the ticket while processing a request for another ticket. This prevented security checks from running and could open security vulnerabilities. See https://go.microsoft.com/fwlink/?linkid=2173051 to learn more.  

Ticket PAC constructed by: %DC%  

Client: %FQDN of Domain%\%Clientname$%  

Ticket for: krbtgt  

I installed the two updates as mentioned in https://support.microsoft.com/en-us/topic/november-14-2021-kb5008602-os-build-17763-2305-out-of-band-8583a8a3-ebed-4829-b285-356fb5aaacd7 but the problem still exists.

## Answers

_No answers on this thread._
