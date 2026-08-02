---
title: "Active Directory External One Way Trust Permission Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1476166/active-directory-external-one-way-trust-permission
question_id: 1476166
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory External One Way Trust Permission Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1476166/active-directory-external-one-way-trust-permission (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have the following situation / issue:

Domain A has a working external one way trust with domain B.

In domain A the global group G-1 exists

In domain B the local group L-1 exists which contains the G-1 group of domain A\L-1

The group L-1 is a member of the administrator group of domain B

The server SRV-1 ist joined  the domain B 

The group L-1 is a member of the local administrators group on the SRV-1

A user of the domain A who ist member of the group A\L-1 (and therefore has the local administrator permission on the server and the administrator permission on the domain) wants to add another group from the domain B to the local administrator group on the server SRV-1.

When he searches for the group in domain B in the corresponding add dialog (netplwiz - group administrators - add) he gets a login prompt and after entering his correct login data the error message "During the usage of the provided Username and Password an error occured: Username or Password is incorrect".

At the same time, the firewall shows that SRV-1 wants to communicate with the domain controllers of domain A on ports 88 and 389 and not with those of domain B.

Is this a design or conifg error?

Unfortunately, I can't find any comparable cases / information on this issue.

I can provide further information / screenshots if required.

I look forward to any feedback.

Regards

Kai

## Answers

_No answers on this thread._
