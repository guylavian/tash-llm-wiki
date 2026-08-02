---
title: "Demote second Domain Controller in Child Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/619866/demote-second-domain-controller-in-child-domain
question_id: 619866
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Demote second Domain Controller in Child Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/619866/demote-second-domain-controller-in-child-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a root domain and one child domain as below and each of them has 2 domain controllers:    

abc.com (Root)    

sub.abc.com (Sub domain)    

In sub.abc.com, there are 2 domain controllers and I would like to demote the second one which is not holding any FSMO role of sub.abc.com. When I go through the demotion wizard I can see the "Remove DNS delegation" is ticked by default without any credentials provided. Shall I proceed with Next without putting any credentials or I have to untick it since I still have a domain controller running in the child domain? If I proceed with ticking the "Remove DNS delegation" will it remove anything and affect the DNS functionality of the child domain and any domain controller that is still running?

## Answers

_No answers on this thread._
