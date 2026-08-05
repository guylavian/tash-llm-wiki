---
title: "How to Create GPO to Disallow  Windows gemes such as Solitaire"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1613009/how-to-create-gpo-to-disallow-windows-gemes-such-a
question_id: 1613009
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to Create GPO to Disallow  Windows gemes such as Solitaire

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1613009/how-to-create-gpo-to-disallow-windows-gemes-such-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to Create GPO to Disallow  Windows gemes such as Solitaire

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-13*

Hi Mohamed Gabr,

You can create an AppLocker rule to deny the application from running. The AppLocker is located under Computer Configuration > Policies > Windows Settings > Security Settings > Application Control Policies.

Please refer to this link for more details.

https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/applocker/administer-applocker

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
