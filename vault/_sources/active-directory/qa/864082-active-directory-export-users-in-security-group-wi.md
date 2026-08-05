---
title: "Active Directory export users in security group with select properties"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/864082/active-directory-export-users-in-security-group-wi
question_id: 864082
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Active Directory export users in security group with select properties

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/864082/active-directory-export-users-in-security-group-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a security group.  All members in this group, and nested groups, I need to extract the display name, creation date, password last changed, and one or two other properties.  The Get-ADGroupMembership does not contain these properties.  

I am trying to do something like (I know this is way off but it illustrates the end goal logic to you I believe:  

$sam= Get-ADGroupMember -id "Sample Security Group" -Recursive |select sama*  

Get-ADUser -Properties * -id $sam  |select name,whencreated,passwordlastset,enabled,lastlogondate

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-25*

I don't think you were too far off. Try this:  

```
Get-ADGroupMember -id "Sample Security Group" -Recursive |
    ForEach-Object{
        Get-ADUser -Properties * -id $_.samaccountname |
            Select-Object name,whencreated,passwordlastset,enabled,lastlogondate
    }
```
