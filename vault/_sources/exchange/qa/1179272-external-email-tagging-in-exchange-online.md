---
title: "External Email Tagging in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179272/external-email-tagging-in-exchange-online
question_id: 1179272
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# External Email Tagging in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179272/external-email-tagging-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Hello,

I'm trying to enable External Email Tagging in Exchange Online, with:

Set-ExternalInOutlook –Enabled $true
But as a normal admin I would like to check settings before changing them.

What I did:
1. Import-Module ExchangeOnlineManagement
2. Connect-ExchangeOnline  
3. Provided login and password
4. get-ExternalInOutlook 
5. Gro this error

get-ExternalInOutlook
get-ExternalInOutlook : The term 'get-ExternalInOutlook' is not recognized as the name of a cmdlet, function, script file, or operable program. Check t
he spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ get-ExternalInOutlook
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (get-ExternalInOutlook:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-09*

Looks like I have missing powershell modules

Get-ManagementRole : The term 'Get-ManagementRole' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spe

lling of the name, or if a path was included, verify that the path is correct and try again.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-09*

You really should be an org mgmt admin role user to set this.

You can view with org viewer

```
$Perms = Get-ManagementRole -Cmdlet Get-ExternalInOutlook

$Perms | foreach {Get-ManagementRoleAssignment -Role $_.Name -Delegating $false | Format-Table -Auto      Role,RoleAssigneeType,RoleAssigneeName}
```

Role                       RoleAssigneeType RoleAssigneeName

Organization Configuration RoleGroup        Organization Management

Role                    RoleAssigneeType RoleAssigneeName

View-Only Configuration RoleGroup        Hygiene Management

View-Only Configuration RoleGroup        Compliance Management

View-Only Configuration RoleGroup        Organization Management

View-Only Configuration RoleGroup        View-Only Organization Management
