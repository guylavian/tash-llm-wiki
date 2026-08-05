---
title: "Unable to uninstall Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278517/unable-to-uninstall-exchange-2019
question_id: 2278517
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Unable to uninstall Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278517/unable-to-uninstall-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019, Server 2019.

Exchange server A became corrupted. Filter service won't start  so transport, etc. won't start.

Exchange server B was created and all mailboxes/functions were moved to B. 

A was powered off and B functioned as normal.

The time has come to officially decommission A.

However, uninstall is unable to continue.

To my knowledge, there are no mailboxes (user, system, arbitration, etc.) still on A.

When I check the AuditLog mailbox on A using the powershell cmdlet in the image, it shows a system mailbox I cannot see the full name of that doesn't show up on any other mailbox list.

When I check the AuditLog mailbox on B, it doesn't show a AuditLog mailbox.

Is it ok to delete the AuditLog mailbox on A? Do I need to to create one on B? If so, how do I create a system mailbox for AuditLog? 

What all else do I need to do to make the uninstall successful? There are no migration requests either. 

Thanks.

## Answers

_No answers on this thread._
