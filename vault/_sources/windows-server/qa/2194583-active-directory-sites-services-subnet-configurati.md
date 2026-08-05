---
title: "Active Directory Sites & Services Subnet configurations - can a Super Subnet be created and have exception subnets within that Super subnet?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194583/active-directory-sites-services-subnet-configurati
question_id: 2194583
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory Sites & Services Subnet configurations - can a Super Subnet be created and have exception subnets within that Super subnet?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194583/active-directory-sites-services-subnet-configurati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

if a super subnet is defined xxx.xxx.0.0/16 -assigned to Site AAAA and then a subnet xxx.xxx.yyy.0/24 is created - assigned to Site ZZZZ  which Site will take preference for  xxx.xxx.yyy.0/24 ?  Will xxx.xxx.0.0/16 remain assigned to AAAA Site?

there are a few instances where a super subnet could be created but have some /24 created as exceptions.  

Is this recommended? Will it work as I hope?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-09*

Thank you Doug_KE - that is exactly the question you have answered!! And that answer is very welcomed. Again thanks for the response and confirmation..
