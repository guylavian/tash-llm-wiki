---
title: "How to set Active Directory Required fields when creating groups?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2131303/how-to-set-active-directory-required-fields-when-c
question_id: 2131303
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to set Active Directory Required fields when creating groups?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2131303/how-to-set-active-directory-required-fields-when-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a requirement to use certain fields (like company name, department, location) in AD when creating a new account or groups.    I want to be able to force the folks who create accounts to enter something in these fields.  I need this for account auditing purposes.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-17*

Hello,

Thank you for posting in Q&A forum.

Unfortunately, AD by itself does not have a built-in feature to enforce mandatory fields directly. However, you can create a custom solution using PowerShell scripts. You can write a PowerShell script to ensure that the required fields are filled in when creating a user or group, and use this script as part of the standard process. At the same time, ensure that only authorized personnel can execute these scripts, which can effectively ensure data integrity and consistency.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
