---
title: "GPO vs WMI Filter Processing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1845632/gpo-vs-wmi-filter-processing
question_id: 1845632
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO vs WMI Filter Processing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1845632/gpo-vs-wmi-filter-processing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi MSFT,

If i have the same WMI filter applying to 10x individual GPOs, does Windows evaluate that filter once or 10 times?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2024-07-29*

Hello,

Thank you for posting in Q&A forum.

10 times.Windows evaluates the WMI filter each time it processes a Group Policy Object (GPO) that is linked to that filter. So if you have the same WMI filter applied to 10 individual GPOs, Windows will evaluate that filter 10 times, once for each GPO. This can have performance implications, especially if the WMI filter is complex or if there are many GPOs being processed.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-30*

Official word from MSFT via Advisory ticket is:

"if all of group policies are having the exact same WMI filter, then, it will only run once."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-30*

Official word from MSFT via Advisory ticket is:

"if all of group policies are having the exact same WMI filter, then, it will only run once."
