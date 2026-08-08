---
title: "SCOM Powershell: How do I scope views or folders for an existing user role?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1360686/scom-powershell-how-do-i-scope-views-or-folders-fo
question_id: 1360686
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["msc-operations-manager", "msc-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# SCOM Powershell: How do I scope views or folders for an existing user role?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1360686/scom-powershell-how-do-i-scope-views-or-folders-fo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How do we scope views/folders for a user role? 

There's a way to scope tasks using the -TaskScope property:

```
$Role = Get-SCOMUserRole -Name "Constoso SQL Operators"
$NewTaskList = Get-SCOMTask -Name "*SQL*"
$Role | Set-SCOMUserRole -TaskScope $NewTaskList
```

 But there is no equivalent for views or folders, e.g.  -ViewScope

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-06*

Hi,

In System Center Operations Manager, you can't directly scope views or folders for a user role using a built-in parameter like `-ViewScope` as you do with tasks. Instead, scoping views and folders for user roles in SCOM is typically done through role-based access control (RBAC) profiles.
