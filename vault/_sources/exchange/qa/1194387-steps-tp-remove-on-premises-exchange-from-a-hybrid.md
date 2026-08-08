---
title: "Steps tp remove on premises Exchange from a hybrid setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194387/steps-tp-remove-on-premises-exchange-from-a-hybrid
question_id: 1194387
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Steps tp remove on premises Exchange from a hybrid setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194387/steps-tp-remove-on-premises-exchange-from-a-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a single Exchange server on premises, it was being used just as a transport server for our scan to email and for some application email. Everything has now been reconfigured so the Exchange server is not required, email is sent via Exchange Online and does not touch on premises Exchange.

We want to decommission this server, but I am having trouble finding a definitive answer as to how I can do this without causing issues.

How can I remove this from service and switch to just Exchange online?

Active Directory is all on premises, we have an AADC server to sync AD to Azure/M365. The Exchange server is a Hyper-V virtual machine running Server 2016 and Exchange 2016

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-29*

If you are syncing with AADConnect, its not supported to remove the last Exchange Server unless you meet certain requriements:

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange

Requirements:

https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools

Otherwise you can follow the steps listed in the first doc I linked but you will have manage recipients on-prem directly in AD or a 3rd party application ( again, not supported in that scenario unless you follow link two above)
