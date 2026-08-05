---
title: "How to connect to ExchangeOnline to Get-DistributionGroup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2113075/how-to-connect-to-exchangeonline-to-get-distributi
question_id: 2113075
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-identity-manager", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to connect to ExchangeOnline to Get-DistributionGroup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2113075/how-to-connect-to-exchangeonline-to-get-distributi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys, 

I am trying to create and also get distribution list using a powershell runbook (version 5.1) setup in an Azure Automation account. But am having trouble connecting to Exchange Online.

=========

My Script (1):-

Connect-ExchangeOnline -ManagedIdentity -Organization "contoso.onmicrosoft.com"

Get-DistributionGroup

ERROR MESSAGE:

This throws the Unauthorized error 

========

I have registered an app in Azure and assigned necessary permissions. 

(- Exchange.ManageAsApp, - Group.Read.WriteAll)

Please any help would be much appreciated. Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-29*

Did you follow these steps? Including adding the Exch Role to the service principal?

https://practical365.com/use-azure-automation-exchange-online/
