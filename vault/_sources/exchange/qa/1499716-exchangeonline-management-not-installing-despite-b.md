---
title: "ExchangeOnline-Management not installing despite being set in requirements.psd1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1499716/exchangeonline-management-not-installing-despite-b
question_id: 1499716
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-functions", "office-exchange-online"]
---
# ExchangeOnline-Management not installing despite being set in requirements.psd1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1499716/exchangeonline-management-not-installing-despite-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am using the following code to see which modules are installed:

However, this is what the output looks like:  

 

This is what my requirements.psd1 looks like so I know I'm installing ExchangeOnlineManagement:

I also set Exchange.ManageAsApp in Permissions through Powershell:

I've even tried to install ExchangeOnlineManagement in the ps1 script using:  

Install-Module -Name ExchangeOnlineManagement -RequiredVersion 3.4.0  

Does anybody know why I'm not seeing ExchangeOnlineManagement when I query for the available modules?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-17*

I ended up just recreating another Function App. I still don't know why ExchangeOnline-Management wasn't available, but starting from scratch worked.
