---
title: "Exchange 2013 - Permission for granting \"Send As\" permission"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160424/exchange-2013-permission-for-granting-send-as-perm
question_id: 160424
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 - Permission for granting "Send As" permission

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160424/exchange-2013-permission-for-granting-send-as-perm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I can grant userA "send as" permission for distribution groupA by administrator account via EAC, I want userB can grant "send as" permission for other users on groupA too, which role in "admin roles" I have to assign userB to archive this ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-12*

The Recipient Management role will give UserB the ability to grant SEND AS to any mail-enabled object in EAC, unless you scoped a custom role to a specific group of recipients using RBAC.    

Regardless, here is how you find which role is required for a specific command    

In this case, send as is granted with add-adpermission for on-prem    

```
$Perms = Get-ManagementRole -Cmdlet Add-ADPermission
```

Name RoleType    

Active Directory Permissions ActiveDirectoryPermissions    

```
$Perms | foreach {Get-ManagementRoleAssignment -Role $_.Name -Delegating $false | Format-Table -Auto Role,RoleAssigneeType,RoleAssigneeName}
```

Role RoleAssigneeType RoleAssigneeName    

Active Directory Permissions RoleGroup Organization Management    

Active Directory Permissions RoleGroup Recipient Management    

To using the built-in role, add the UserB to "Recipient Management" at a minimum    

https://learn.microsoft.com/en-us/powershell/exchange/find-exchange-cmdlet-permissions?view=exchange-ps    

Alternatively, they can add SEND AS via ADUC if they have perms there as well :)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Thanks for your reply,  

In my case , userB is assigned to The Recipient Management role but he cannot grant SEND AS , so I try to find which role is required for "Add-ADPermission" command, this is result :  

$Perms = Get-ManagementRole -Cmdlet Add-ADPermission  

$Perms | foreach {Get-ManagementRoleAssignment -Role $_.Name -Delegating $false | Format-Table -Auto Role,RoleAssigneeType,RoleAssigneeName}

```
Role                         RoleAssigneeType RoleAssigneeName
----                         ---------------- ----------------
Active Directory Permissions        RoleGroup Organization Management
```

Recipient Management role is not listed , only Organization Management , I don't want to add userB into Organization Management role, what should I do ?  

I didn't custom any role as default , here information about Recipient Management role at EAC:  

Recipient Management

```
Members of this management role group have rights to create, manage, and remove Exchange recipient objects in the Exchange organization. 

Assigned Roles 

Distribution Groups 
Mail Recipient Creation 
Mail Recipients 
Mailbox Import Export 
Message Tracking 
Migration 
Move Mailboxes 
Recipient Policies 
Team Mailboxes
```
