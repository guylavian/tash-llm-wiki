---
title: "Exchange Server on-premises, is there a solution that prohibits users to expand members of distribution groups in the address book?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2032012/exchange-server-on-premises-is-there-a-solution-th
question_id: 2032012
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Server on-premises, is there a solution that prohibits users to expand members of distribution groups in the address book?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2032012/exchange-server-on-premises-is-there-a-solution-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Server deployed on-premises, is there a solution that prohibits users to expand the members of distribution groups in the address book? Currently tried to set it in the AD group object, with powershell command Set-ADGroup -Identity "groupname" -replace @{hideDLMembership=$false}; 

Once set, in OWA and the Windows outlook client, you can disable expansion and can't view group members. However, if you use the MAC client,  you can still access and view the group members normally.

Is there a feasible solution for the on-premises Exchange Server system to prevent users from viewing and expanding distribution group members? Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-09-03*

I'm not aware of any way to prevent that. 

Hiding the members is not the same as preventing expansion.

The only way to prevent users from expansion would be to use a dynamic distrib group.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-03*

Hi,

Welcome to the Microsoft Q&A platform!

You can try to use the `Add-ADPermission` cmdlet to set permissions. 

For example, to prevent a specific user or group from expanding a distribution group:

```
Add-ADPermission -Identity "DistributionGroupName" -User "UserOrGroupName" -Deny -ExtendedRights "Read Members"
```

More details about this cmdlet you can refer to:Add-ADPermission

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer!
