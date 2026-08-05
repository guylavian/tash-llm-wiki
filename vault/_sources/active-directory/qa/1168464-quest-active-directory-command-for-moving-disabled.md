---
title: "Quest Active Directory command for moving Disabled Objects"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1168464/quest-active-directory-command-for-moving-disabled
question_id: 1168464
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Quest Active Directory command for moving Disabled Objects

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1168464/quest-active-directory-command-for-moving-disabled (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I want a Quest Active Directory command for moving Disabled computers from one OU to Another.

$SourceOU = "OU=IG Workstations W10,DC=igi,DC=ig,DC=local"

$TargetOU = "OU=Disabled Computers,OU=Disabled Objects,DC=igi,DC=ig,DC=local"

I would like the script to query for Disabled computers in Source OU and move Disabled Objects to Target OU

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-07*

Why not use the PowerShell cmdlets (Get-ADComputer and Move-ADObject)?

To get the disabled AD computer objects using the Quest module, use this:

```
Get-QADComputer -ldapFilter '(userAccountControl:1.2.840.113556.1.4.803:=2)'
```
