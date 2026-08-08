---
title: "Network-shares on Domain-Controller not available"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1396809/network-shares-on-domain-controller-not-available
question_id: 1396809
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Network-shares on Domain-Controller not available

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1396809/network-shares-on-domain-controller-not-available (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

the network folder shares of our domain controller are no longer accessible. When a domain client tries to access the IP address/DNS via Explorer ("\DC"), they receive the error message: "\DC" is not accessible.

When attempting to list the sharing permissions on the server itself through Server Manager, an error message is displayed: "Error retrieving folder permissions" (screenshot attached). The admin share "\DC\C$" also does not work.

As a result, DFSR replication is not functioning as well, but that's a separate issue.

We can rule out the firewall as the cause of the problem.

The server is running on Windows Server 2012 R2.

Can you please assist me with this?

Thank you very much, and best regards, Sebastian

## Answers

_No answers on this thread._
