---
title: "Using Active Directory groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/563993/using-active-directory-groups
question_id: 563993
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Using Active Directory groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/563993/using-active-directory-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Can you explain to me in more detail, with examples, where and when I should use any Active Directory group? Where and when do I use local, global, universal? What is the case when I have to grant access somewhere in a trust relationship?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-09-28*

Local groups are needed to grant rights to resources.  

Global groups unite departments.  

Universal - used when there is more than one domain in the forest.  

-  And how to do when you need to grant access to resources of another domain in another forest with trust relationship?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-09-23*

Hi    

I will quote an article;    

About Active Directory groups    

Groups are used to collect user accounts, computer accounts, and other groups into manageable units. Working with groups instead of with individual users helps simplify network maintenance and administration.    

There are two types of groups in Active Directory:    

```
Distribution groups Used to create email distribution lists.    

Security groups Used to assign permissions to shared resources.
```

Security groups    

Security groups can provide an efficient way to assign access to resources on your network. By using security groups, you can:    

```
Assign user rights to security groups in Active Directory.    

User rights are assigned to a security group to determine what members of that group can do within the scope of a domain or forest. User rights are automatically assigned to some security groups when Active Directory is installed to help administrators define a person’s administrative role in the domain.    

For example, a user who is added to the Backup Operators group in Active Directory has the ability to back up and restore files and directories that are located on each domain controller in the domain. This is possible because, by default, the user rights Backup files and directories and Restore files and directories are automatically assigned to the Backup Operators group. Therefore, members of this group inherit the user rights that are assigned to that group.    

You can use Group Policy to assign user rights to security groups to delegate specific tasks. For more information about using Group Policy, see User Rights Assignment.    

Assign permissions to security groups for resources.    

Permissions are different than user rights. Permissions are assigned to the security group for the shared resource. Permissions determine who can access the resource and the level of access, such as Full Control. Some permissions that are set on domain objects are automatically assigned to allow various levels of access to default security groups, such as the Account Operators group or the Domain Admins group.    

Security groups are listed in DACLs that define permissions on resources and objects. When assigning permissions for resources (file shares, printers, and so on), administrators should assign those permissions to a security group rather than to individual users. The permissions are assigned once to the group, instead of several times to each individual user. Each account that is added to a group receives the rights that are assigned to that group in Active Directory, and the user receives the permissions that are defined for that group.
```

Like distribution groups, security groups can be used as an email entity. Sending an email message to the group sends the message to all the members of the group.    

For explanation on the group scoop, global, universal, etc... please see the full article there, it's well wrote;    

Active Directory Security Groups
