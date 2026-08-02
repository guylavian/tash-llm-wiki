---
title: "I had remove existing Exchange server, them I install new exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/407558/i-had-remove-existing-exchange-server-them-i-insta
question_id: 407558
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# I had remove existing Exchange server, them I install new exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/407558/i-had-remove-existing-exchange-server-them-i-insta (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

PS E:\> .\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema

Microsoft Exchange Server 2019 Cumulative Update 9 Unattended Setup

Copying Files...  

File copy complete. Setup will now collect additional information needed for installation.

Languages  

Mailbox role: Front End Transport service  

Mailbox role: Client Access Front End service  

Front End Transport service cannot be installed without Mailbox service.  

Client Access Front End service cannot be installed without Mailbox service.

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-24*

You mean you uninstalled it then tried to reinstall?  

That won't work typically because there are registry entries and fragments left behind when you remove Exchange.  

Instead, rebuild the entire server and start with a fresh O/S
