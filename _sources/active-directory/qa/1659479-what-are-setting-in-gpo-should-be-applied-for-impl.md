---
title: "what are setting in GPO Should be applied for implementing tiering in AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659479/what-are-setting-in-gpo-should-be-applied-for-impl
question_id: 1659479
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# what are setting in GPO Should be applied for implementing tiering in AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659479/what-are-setting-in-gpo-should-be-applied-for-impl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello Experts,

Wants to implement tiering model in AD ,what are settings we can implement in GPO point to implement tier.  

Any supported links and examples of GPO would be helpful.

thanks  

Richa

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-24*

Hello,

In Active Directory, create OUs that reflect the organizational structure, and create and link corresponding GPOs for the company, headquarters, and departments. Setting priorities implements a hierarchical model of group policy to ensure unified application of basic security settings across the company (such as password complexity requirements). The headquarters has its own application configuration, and each department has customized software restrictions and permission settings.

Recommended reference links:

Active Directory Tiering Model (linkedin.com)

The Fundamentals of AD tiering — Improsec | improving security

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
