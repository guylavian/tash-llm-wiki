---
title: "Unable to create Distribution lists using exchange online with app-only authentication(Azure AD Application) with exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688178/unable-to-create-distribution-lists-using-exchange
question_id: 1688178
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Unable to create Distribution lists using exchange online with app-only authentication(Azure AD Application) with exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688178/unable-to-create-distribution-lists-using-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Requirement: To create Distribution lists using exchange online with app-only authentication.

Description:

-  I am using Azure AD credentials to connect to exchange online, because i wanted to create distribution lists automatically without user involvement.

-  After authentication, whenever I am using commands like New-DistributionGroup, Add-DistributionGroupMember,Remove-DistributionGroup ,Remove-DistributionGroupMember ,Update-DistributionGroupMember an error showing like below

New-DistributionGroup : "The term 'New-DistributionGroup' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the

spelling of the name, or if a path was included, verify that the path is correct and try again".

-  New-DistributionGroup

- 

```

```

-  CategoryInfo : ObjectNotFound: (New-DistributionGroup:String) [], CommandNotFoundException

-  FullyQualifiedErrorId : CommandNotFoundException

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-28*

Hi，@Mariyada, Ajaynath Reddy

Thanks for posting your question in the Microsoft Q&A forum.

When you run New-DistributionGroup, a message appears that the command is not recognized.

If only administrator role are not enough, a query reveals that it also requires the "Recipient Management" or "Security Administrator" roles.

You can add users to role groups  in EAC- Admin roles.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-27*

Did you assign a matching admin role to the service principal corresponding to your app? The "Exchange Recipient Management" role or equivalent role/role group in Exchange Online is required.
