---
title: "Error connecting to Exchange Online PowerShell: \"The connection for this site is not secure\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1372751/error-connecting-to-exchange-online-powershell-the
question_id: 1372751
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Error connecting to Exchange Online PowerShell: "The connection for this site is not secure"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1372751/error-connecting-to-exchange-online-powershell-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to connect to Exchange Online PowerShell using PowerShell 7.3.6. The version of ExchangeOnlineManagement that is installed is 3.3.0. When I try to Connect-ExchangeOnline, it brings me to the Microsoft login screen, I click my account then it shows "The connection for this site is not secure". EOM 3.3.0 works fine on PowerShell 5.1, however I like PowerShell 7 better, any ideas on whats going on?

I tried [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 in powershell 7 with no luck

## Answer (community) — Q&A User

*upvotes: 3 · updated: 2023-09-22*

I actually figured out that I needed to clear my browser cache.
