---
title: "Hybrid Exchange 365 vary slow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1003428/hybrid-exchange-365-vary-slow
question_id: 1003428
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Hybrid Exchange 365 vary slow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1003428/hybrid-exchange-365-vary-slow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

According to my agency using the Hybrid Exchange 365 service, I have encountered a problem with very slow mail delivery.  As far as causal analysis, it was found that the IP addresses of Hostname my-Organization.xxx.outlook.com were pointed to ip numbers 104.47.26.10 , 104.47.26.74 , 104.47.110.36 . Details as in the picture    

    

The problem is that IP 104.47.110.36 does not have a PTR record, causing Ms Exchange On–Premise not to forward mails to that IP, thus waiting for the que to be sent to the new IP with PTR, causing slow mail problems.    

    

The initial workaround was to force a run to an IP other than 104.47.110.36. Found that the slow mail problem has disappeared. But in the long run, I think Microsoft should be a solution to this problem in a way that's more relevant, sustainable, and to help solve the problem for many organizations that are likely to encounter the same problem.

## Answers

_No answers on this thread._
