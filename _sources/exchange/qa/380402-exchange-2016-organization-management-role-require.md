---
title: "Exchange 2016 \"Organization Management\" role required to be local admin on server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/380402/exchange-2016-organization-management-role-require
question_id: 380402
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 "Organization Management" role required to be local admin on server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/380402/exchange-2016-organization-management-role-require (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In my organization, there are security concerns for adding multiple people to the "Organization Management" role.  We have an on-prem Exchange 2016 server, in a forest with other child domains owning their own Exchange servers.  It is my understanding that the "Organization Management" role is automatically added to the local administrators group on each Exchange server.  So that would allow an employee in our child domain, admin access to all other Exchange servers in the forest.  Does anyone know if "Organization Management" role is required to be in the local admins group?  Or can it be removed, as long as the technician doing tasks is a member of another local administrators group, on their specific Exchange server?  

Or if there is a way to split the "Organization Management" role so that it is not granted to the whole forest?  

Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-04*

In that case, try this    

https://learn.microsoft.com/en-us/powershell/module/exchange/new-managementscope?view=exchange-ps    

```
New-ManagementScope -Name "Child Domain Mailbox Servers" -ServerList ChildDomainMailboxServer1, ChildDomainMailboxServer2
```

Then Create the new role copies from Org Mgmt    

https://learn.microsoft.com/en-us/exchange/permissions-exo/role-groups    

```
$RoleGroup = Get-RoleGroup "Organization Management"  
New-RoleGroup "Child Domain Mgmt" -Roles $RoleGroup.Roles
```

Or Copy in EAC and give the new group a name that makes sense    

Then Set this new Role Group to the Custom Write Scope created above. You can do this in EAC:    

https://learn.microsoft.com/en-us/exchange/permissions-exo/role-groups#use-the-classic-eac-to-modify-role-groups    

Test this out and if it works, create more as needed.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-04*

Hi @tmorow       

Does anyone know if "Organization Management" role is required to be in the local admins group? Or can it be removed, as long as the technician doing tasks is a member of another local administrators group, on their specific Exchange server?    

Regarding this question, I tried searching around but couldn't find an official documentation stating whether it's a supported scenario or not.     

However, considering that as we know, the Organization management group and some others Exchange groups are added by default in the Exchange server installation process, and during my research, I did see some threads discuccssing issues which might be related to the missing "Organization Management" role in the local admins group, like this link, so personally I would recommend leaving it as it is in case it affects any functionality of the Exchange server environment.     

That being said, as regards to your requirement about restricting child domain technician's access to the other Exchange servers, agree with Andy that you may consider adjusting the management scope. If it can meet your needs, you can accept Andy's suggestion as Answer so that it can also benefit from your thread. If you still have any further questions or concerns, feel free to post back.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-03*

Make the technician a Server Admin, not a member of the Org Mgmt role.     

Use RBAC to give them any other perms they may need    

https://learn.microsoft.com/en-us/exchange/server-management-exchange-2013-help
