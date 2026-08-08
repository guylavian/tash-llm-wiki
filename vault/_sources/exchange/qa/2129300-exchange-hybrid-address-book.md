---
title: "Exchange Hybrid Address book"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2129300/exchange-hybrid-address-book
question_id: 2129300
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid Address book

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2129300/exchange-hybrid-address-book (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In a Hybrid environment is the Online GAL made from only the synchronized object from AD ?

what if distribution groups are synchronized from On-Prem to ExO but some members are not present on the tenant ( not synced with Entra ID connector ) ?

Can the AD "mail contact" be synced without issue ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-12*

Hi @Stefano Colombo  ,

Welcome to the Microsoft Q&A platform!

In a hybrid environment, the Online Global Address List (GAL) is indeed created from objects synchronized from your on-premises Active Directory (AD) using tools like Microsoft Entra Connect (formerly Azure AD Connect).

Regarding your second question, if distribution groups are synchronized from on-premises to Exchange Online (ExO) but some members are not present in the tenant (i.e., not synced with Entra ID connector), those members will not appear in the distribution group in ExO. This can cause incomplete or missing group memberships in the cloud.

As for synchronizing AD "mail contacts," yes, they can be synced without issue. Mail contacts created in your on-premises AD can be synchronized to Exchange Online, allowing them to appear in the GAL and be used for email routing.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
