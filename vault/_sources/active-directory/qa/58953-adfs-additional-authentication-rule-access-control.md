---
title: "ADFS additional authentication rule -> access control rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58953/adfs-additional-authentication-rule-access-control
question_id: 58953
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS additional authentication rule -> access control rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58953/adfs-additional-authentication-rule-access-control (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On our ADFS 2016 farm we have a global additional authentication rule which I would like to change to an RPT-specific access control rule to have more flexibility.  

The current additional authentication rule is:  

exists([Type == "http://schemas.microsoft.com/ws/2012/01/insidecorporatenetwork", Value == "false"])  

 && NOT exists([Type == "http://schemas.microsoft.com/2012/01/requestcontext/claims/x-ms-forwarded-client-ip", Value =~ "\b123.45.67.89\b"])  

 => issue(Type = "http://schemas.microsoft.com/ws/2008/06/identity/claims/authenticationmethod", Value = "http://schemas.microsoft.com/claims/multipleauthn");  

Additionally, I would like to add an AD group as an exclusion in this rule, lets call it: "no_mfa".  

Is it possible to add all this in an access control rule, and if so, can you give me an example? I tested several options, and it seems that none of them work in the same way as the additional authentication rule.

## Answers

_No answers on this thread._
