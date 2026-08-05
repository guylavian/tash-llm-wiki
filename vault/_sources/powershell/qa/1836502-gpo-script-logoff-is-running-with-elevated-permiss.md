---
title: "GPO script logOff is running with elevated permissions, can't run OneDrive correctly."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1836502/gpo-script-logoff-is-running-with-elevated-permiss
question_id: 1836502
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-onedrive-business-platform-windows", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO script logOff is running with elevated permissions, can't run OneDrive correctly.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1836502/gpo-script-logoff-is-running-with-elevated-permiss (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

GPO script logOff is running with elevated permissions, can't run OneDrive correctly (it reports that it is not possible to run as administrator, even though I configured the policy in userconfiguration - windows settings - scripts LogOn\LogOff) How to run it with the current user's permissions that performs the exit?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-24*

Hi,

Please create a new scheduled task under User Configuration > Preferences > Control Panel Settings > Scheduled Tasks and select New > Scheduled task (At least Windows 7) to run your script. In the General tab, choose the user account to use and check "Run with highest privileges". 

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
