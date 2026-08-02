---
title: "Unhide user's mailbox in Exchange Admin Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282761/unhide-users-mailbox-in-exchange-admin-center
question_id: 1282761
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unhide user's mailbox in Exchange Admin Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282761/unhide-users-mailbox-in-exchange-admin-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a user that has Hide from Global Address List (GAL) set to 'yes' in Exchange Admin Center.

When I set to 'NO' and save I get "Operation Failed"

I checked the "msExchHideFromAddressLists" attribute on our on premises AD and that attribute isn't even listed.

We don't have an on premises Exchange Server

I'm stumped any help is appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-05-11*

Ok, are you using AADConnect to sync from on-prem to Azure? If so, then the only way to make that work is add the Exchange schema by this method ( and then refresh the AADconnect schema in the AADConnect Wizard)

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019

or not sync from on-prem.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-11*

Was Exchange ever installed? Its not supported to remove it from -prem unless you meet certain requirements if you are syncing with AAdConnect.

If Exchange was previously installed, then that attribute should be available. If are not seeing it on-prem, it could be just your filter view of that account. Make sure the view is set to show all values - even ones that are blank.
