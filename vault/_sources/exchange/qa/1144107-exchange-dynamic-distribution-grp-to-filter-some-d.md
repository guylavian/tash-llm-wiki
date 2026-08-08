---
title: "Exchange Dynamic Distribution grp to filter some domain users to receive email only."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1144107/exchange-dynamic-distribution-grp-to-filter-some-d
question_id: 1144107
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Dynamic Distribution grp to filter some domain users to receive email only.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1144107/exchange-dynamic-distribution-grp-to-filter-some-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,    

I already existing DDL grp created for office1 users. the users in office1 contains  users from different email domain such as  @StEv  .com and @Company portal   .com    

currently, we decided not to let @Company portal   .com users to receive the emails.    

I checked the DDL  filter rule, not sure what is the parameter to put for this.    

can anyone coach me this? TQ in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-29*

Hi @QUEK SOON TEE  ,    

Welcome to the Microsoft Q&A platform!    

Through my tests, in Dynamic Distribution Groups, we don't have such a direct option to restrict members of specific domains from receiving email.    

In your case, we recommend that you create a new dynamic distribution group based on a specific domain.    

```
New-DynamicDistributionGroup -name "All Users - Domain Name" -RecipientFilter "(RecipientTypeDetails -eq 'UserMailbox') -and (EmailAddresses -like '*@contoso.com')"
```

Besides, if you do not want to create a new DDL again, then you can also set up the following rule that users who are in a dynamic distribution group and have a domain of @Company portal   .com will not be able to receive email.    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-28*

There is also a way to understand exactly from which user this filter is applied with a GET on the DDL?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-28*

You can add a condition (or exception) to your rule, based on the domain part of the UPN or EmailAddresses. For example:     

```
(WindowsLiveID -eq '*@tenant.onmicrosoft.com')
```

where WindowsLiveID value will match the UPN (used as workaround as UPN field doesn't support the corresponding filter). Alternatively, you can use fields such as Company or any of the customattributeXX values.
