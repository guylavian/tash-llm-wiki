---
title: "Exchange Hybrid configuration wizard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1286629/exchange-hybrid-configuration-wizard
question_id: 1286629
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange Hybrid configuration wizard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1286629/exchange-hybrid-configuration-wizard (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am in the process of implementing HCW. I am getting the attached error. As per the error, WinRM still requires basic authentication to be enabled on hybrid server. Below article has some info around the WinRM and basic authentication.

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online

 However, i couldn't find any MS article states HCW requires WinRM basic authentication as a pre-req. Below are my questions

-  Is the basic authentication to be enabled on the hybrid server permanently?

-  Why HCW still requires basic auth to be enabled on the hybrid server?

-  Is the basic authentication to be enabled on all the Exchange servers in the organization?

Kindly help me to get some answers.

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-23*

Hi All,

WinRM basic authentication is required for Hybrid configuration wizard. Which is not listed as a pre-requisite.

MS support has confirmed this
