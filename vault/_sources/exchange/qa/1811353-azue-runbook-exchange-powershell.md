---
title: "Azue runbook - Exchange PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1811353/azue-runbook-exchange-powershell
question_id: 1811353
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-automation", "microsoft-security-ms-graph", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Azue runbook - Exchange PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1811353/azue-runbook-exchange-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to automate mail flow reporting via Azure runbooks using an app registration (service principal) to authenticate. The runbook will query Exhchange Online powershell modules for mailflow data.

The only Entra permissions that seem to allow this is Global Admin or Global Reader. 

If we were running this script and authenticating as a user then we could apply one of the compliance portal permissions to the user (Organization Management) for example

This script however is running in azure via a schedule and the app registration (service principal) required entra level permissions. 

https://learn.microsoft.com/en-us/powershell/exchange/find-exchange-cmdlet-permissions?view=exchange-ps

Surely there is another way this can be automated? 

We use runbooks to query API's and store the resulting data in Azure container storage and then out to PowerBI reporting. 

We would really like to report on mailfllow in this manner without having to over privelage our (service principal

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-12*

Security reader should also work. And if you want to go more granular, Exchange Online now supports role assignments to service principals, so in theory you can create/use a role with just the cmdlets you want. I have some notes on the process here: https://michev.info/blog/post/4302/exo-rbac-improvements-3-limiting-cba
