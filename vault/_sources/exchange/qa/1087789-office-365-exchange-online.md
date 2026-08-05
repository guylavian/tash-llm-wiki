---
title: "Office 365 exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1087789/office-365-exchange-online
question_id: 1087789
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Office 365 exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1087789/office-365-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there!    

I'm very new to this Microsoft azure, my question is why I'm not able to find "Office 365 Exchange Online" package inside the permission -> APIs My Organization uses.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

Try this using a global admin and check if the API is available.    

```
Connect-AzureAD -TenantId   
New-AzureADServicePrincipal -AppId 00000002-0000-0ff1-ce00-000000000000
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-14*

Do you have at least one license that enables the Exchange Online functionality within this tenant? As the name suggests (API my organization uses), you will only find entries corresponding to apps in use within the directory. You can always provision a trial plan that includes any Exchange Online SKU, if this is a test tenant or something.
