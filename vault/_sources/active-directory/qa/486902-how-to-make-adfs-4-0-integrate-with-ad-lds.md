---
title: "how to make ADFS 4.0 integrate with AD LDS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/486902/how-to-make-adfs-4-0-integrate-with-ad-lds
question_id: 486902
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# how to make ADFS 4.0 integrate with AD LDS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/486902/how-to-make-adfs-4-0-integrate-with-ad-lds (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,  

We are using below components  

WIndows 2019 server  

ADFS 4.0  

ADLDS is installed in a different machine. Please let me know how to integrate ADFS 4.0 with AD LDS for user authentication. Currently, ADFS is using AD to authenticate users. Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Thank you for the quick help. I followed the documentation and managed to authenticate users with ADLDS. But weird thing is ADFS is still looking for doamin name\username to authenticate users even though i'm using ADLDS users.
