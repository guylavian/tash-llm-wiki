---
title: "Netlogon and sysvol folder are not showing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2130112/netlogon-and-sysvol-folder-are-not-showing
question_id: 2130112
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Netlogon and sysvol folder are not showing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2130112/netlogon-and-sysvol-folder-are-not-showing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Any have a solution to resolve my issue.

I have 3 DC and 1 is 2016 and another 2 is 2022

2016 is PDC and 2022 are ADC , planning to role transfer after it was completed sysvol and netlogon folder are not visible in share , But ad authentications are working fine, Need support team

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-17*

Hello,

Thank you for posting in Q&A forum.

Based on your description, you encountered the problem that the SYSVOL and Netlogon shares are not visible after the FSMO role is transferred.

You can follow the following official documents to troubleshoot: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
