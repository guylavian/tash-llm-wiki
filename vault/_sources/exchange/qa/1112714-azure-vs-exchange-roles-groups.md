---
title: "Azure vs exchange roles groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1112714/azure-vs-exchange-roles-groups
question_id: 1112714
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-rbac", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Azure vs exchange roles groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1112714/azure-vs-exchange-roles-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to administer Exchange online in Azure, what is the relationship between those roles:    

exchange online management role:  Organization Management    

vs    

Azure AD built-in role:  Exchange Administrator    

Do you need both or either of them?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-02*

Hi @Martin P   ，    

Based on the official description on these 2 roles, since users with Azure AD built-in role Exchange Administrator have global permissions within Microsoft Exchange Online, when the service is present. Also has the ability to create and manage all Microsoft 365 groups, manage support tickets, and monitor service health. the Azure AD built-in role Exchange Administrator seem more permission than Organization Management role.     

Here are some comparisons between the two sides:    

Exchange online management role: Organization Management:    

    

    

    

Detailed information: Organization Management    

Azure AD built-in role: Exchange Administrator:    

    

Detailed information: Exchange Administrator    

Then you could choose one that based on your need.    

If an Answer is helpful, please click "Accept Answer" and upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-01*

The Azure role is the same as the Exch org mgmt.     

The benefit of the Azure role is that you can enable it for PIM, so I would use that one instead of assigning the Exch Org Mgmt one    

It also provides additional Azure roles such as accessing the Health DashBoard and opening service tickets - so I recommend using that one and not Exchange org mgmt :)     

https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/UserRolesViewModelMenuBlade/~/description/menuId/members/roleName/Exchange%20Administrator/roleObjectId/29232cdf-9323-42fd-ade2-1d097af3e4de/isRoleCustom~/false/roleTemplateId/29232cdf-9323-42fd-ade2-1d097af3e4de/resourceId/b1c14d5c-3625-45b3-a430-9552373a0c2f/isInternalCall~/true    

https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure
