---
title: "Kerberos Ticket not applying group membership TTL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1067355/kerberos-ticket-not-applying-group-membership-ttl
question_id: 1067355
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Kerberos Ticket not applying group membership TTL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1067355/kerberos-ticket-not-applying-group-membership-ttl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently testing some scenarios of JIT access for admin rights on computers. When add time-based group membership through AD for 15 minutes and log onto the required computer, the Kerberos ticket still is issued for the full 10 hours duration, instead of being the same as the remaining TTL on the group membership. We currently apply the default 10hours/7days for Kerberos, nothing more.    

Anyone else once hit that issue?    

For more info: https://www.admin-magazine.com/Archive/2018/47/Just-in-time-administration-in-Active-Directory/(offset)/3

## Answers

_No answers on this thread._
