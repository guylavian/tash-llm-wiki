---
title: "Azure AD connect not syncing hide from address list in MS office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1821065/azure-ad-connect-not-syncing-hide-from-address-lis
question_id: 1821065
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Azure AD connect not syncing hide from address list in MS office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1821065/azure-ad-connect-not-syncing-hide-from-address-lis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an on-prem AD but have Office 365/Azure/Entra and now I can not go into MS admin and hide from the address list. when I turn on the toggle I get "Could't update mailbox global address list info" See the screenshot below

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-17*

Hi，@Debbie Drummond

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, this problem occurred after migrating the on-pre mailbox to Online.

Reason：

On-premises is the source of truth for users, they cannot be edited directly in O365.

Solution：

As Andy said, you need to manage the Exch attributes on-prem as well to complete the modification.

You also extend your on-premises AD schema with the Exchange attributes, then you will be able to make the changes. Alternatively, you can disable dirsync, make the changes, re-enable it.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-16*

Did you migrate mailboxes from on-prem? Are you syncing Exch Atttributes and ad Accounts from on-prem? 

If so, then you would need to manage the Exch attributes on-prem as well.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-16*

If you are syncing from on-prem, then you need to hide the mailbox on-prem via the on Exch Mgmt tools and that will sync to Azure.
