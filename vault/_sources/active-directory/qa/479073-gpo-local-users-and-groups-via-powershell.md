---
title: "GPO Local Users and groups via Powershell?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/479073/gpo-local-users-and-groups-via-powershell
question_id: 479073
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Local Users and groups via Powershell?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/479073/gpo-local-users-and-groups-via-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone    

I 've been practicing with Powershell and the GroupPolicy module, trying to make my life easier and i was wondering if any of you has tried it in the past.    

I managed to bulk create 50 GPOs using the New-GPO cmdlet    

Each of these GPO is linked to an OU for which i want to configure in Computer Configuration - Preferences-Control Panel Settings-Local Users and Groups    

a New Local Group with an Update action for group name Administrators (built-in) and add a specific security group (different for each GPO).    

I am attaching a screenshot as an example.    

    

The purpose is to add AD members to those security groups in the future who will act as local admins.    

Is something like that possible via Powershell or do i have to on each GPO and edit it manually?    

Thank you very much for your time reading this.    

Regards     

Kostas

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-19*

Hello @Konstantinos  ,    

Thank you for posting here.    

Based on the description, you want to know if it is possible to edit each GPO via PS, after my discussion with our PS engineer, he said you can create a GPO via PS, but you cannot edit each GPO via PS, so you have to edit each GPO manually.    

Tip: I am engineer from AD DS team.    

Hope the information above is helpful to you.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
