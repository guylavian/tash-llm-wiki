---
title: "Huge number of Kerberos pre-authentication failed(4771) Event generates in DC but no account lockout is happening"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3225655/huge-number-of-kerberos-pre-authentication-failed
question_id: 3225655
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 28
qa_tags: []
---
# Huge number of Kerberos pre-authentication failed(4771) Event generates in DC but no account lockout is happening

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3225655/huge-number-of-kerberos-pre-authentication-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Can you please help me to find out the reason of following issue. 

In our domain after enabling audit we found that huge numbers(around 50k) of Kerberos pre-authentication failed(4771) security failure events are generating in DCs. If any one can explain why this events are generating so frequently. However I found no account
 lockout has happened. One sample event is as follows.

"

Log Name:      Security

Source:        Microsoft-Windows-Security-Auditing

Date:          2019-08-05 09:40:05

Event ID:      4771

Task Category: Kerberos Authentication Service

Level:         Information

Keywords:      Audit Failure

User:          N/A

Computer:      DC.domain.com

Description:

Kerberos pre-authentication failed.

Account Information:

Security ID:
domain\user

Account Name:
user

Service Information:

Service Name:
krbtgt/domain.com

Network Information:

Client Address:
::ffff:IP_address

Client Port:
57415

Additional Information:

Ticket Options:
0x40810010

Failure Code:
0x18

Pre-Authentication Type:
2

Certificate Information:

Certificate Issuer Name:

Certificate Serial Number: 

Certificate Thumbprint:

Certificate information is only provided if a certificate was used for pre-authentication.

Pre-authentication types, ticket options and failure codes are defined in RFC 4120.  

If the ticket was malformed or damaged during transit and could not be decrypted, then many fields in this event might not be present.  

"

I can see that in few cases more than 100 events generated in 30 mins for one user. But no account lockout happened of that user because the failure code is 0x18.

I have checked that account lockout policy is also not satisfying for account unlocking. policy is as below.

Account Policies/Account Lockout Policy

Account lockout duration 0 minutes    

Account lockout threshold 10 invalid logon attempts    

Reset account lockout counter after 30 minutes    

The reported users may use hand-held devices(certificate based) and can use multiple machines. I found the time difference between DC and End computers used by those affected users.

Please anyone can help me to investigate the root cause of huge numbers of logon failure/4771 events in our domain.

## Answers

_No answers on this thread._
