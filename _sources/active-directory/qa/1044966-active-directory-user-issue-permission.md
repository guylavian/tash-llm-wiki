---
title: "Active directory User issue permission"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1044966/active-directory-user-issue-permission
question_id: 1044966
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Active directory User issue permission

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1044966/active-directory-user-issue-permission (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI     

I have created on test user directly under active directory >users,  but this user falls to some other group automatically, and even this user does not have administrator permission in workstation even this user member of administrator group.     

always asking for local administrator password in all machine , how can i check whether any domain wide policy is running , because i want to know how a normal user falls under lot of security group.    

screen shot attached.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-14*

Hi,    

The following PowerShell will result in a report of the GPOs being applied when a user logs in:    

Get-GPResultantSetOfPolicy    

   [-Computer <String>]    

   [-User <String>]    

   -ReportType <ReportType>    

   -Path <String>    

   [<CommonParameters>]    

Please refer here:    

https://learn.microsoft.com/powershell/module/grouppolicy/get-gpresultantsetofpolicy?view=windowsserver2022-ps    

---------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
