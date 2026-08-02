---
title: "Find Active Directory Members with Multiple Group Entries"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2276470/find-active-directory-members-with-multiple-group
question_id: 2276470
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Independent Advisor"]
---
# Find Active Directory Members with Multiple Group Entries

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2276470/find-active-directory-members-with-multiple-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There is a need to identify users in multiple Active Directory (AD) groups that start with a specific keyword, such as `grp_`. This includes groups like `grp_USER`, `grp_ADMIN`, and `grp_BACKUP`. The goal is to locate users who have multiple group entries rather than a single one. How can this be achieved?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-20*

Hello,

```
Thank you for posting the question on Microsoft Windows forum!

Based on your query of locating users having multiple group entries rather than a single one, you can try the following Powershell script to see if it works in your specific scenario:
```

-  To retrieve groups with the specified prefix by using Get-ADGroup to find all AD groups that start with grp_:    $groups = Get-ADGroup -Filter 'Name -like "grp_*"' | Select-Object -ExpandProperty Name

-  Then collecting user memberships in a hashtable ($groupMemberships), storing users as keys and their corresponding groups as values.   $groupMemberships = @{}   foreach ($group in $groups) {

```
**$users = Get-ADGroupMember -Identity $group | Where-Object { $_.objectClass -eq "user" }**

**foreach ($user in $users) {**

    **$groupMemberships[$user.SamAccountName] += ,$group**

**}**
```

   }

-  Finally, filtering users who appear in more than one group and lists their memberships.   $multiGroupUsers = $groupMemberships.Keys | Where-Object { $groupMemberships[$] -is [array] -and $groupMemberships[$].Count -gt 1 }   foreach ($user in $multiGroupUsers) {

```
**Write-Output "$user is in groups: $($groupMemberships[$user] -join ', ')"**
```

   }

You can refer to the below articles for more information about the above Powershell commands.

-  https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2025-ps

-  https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2025-ps

Hope the above information is helpful!
