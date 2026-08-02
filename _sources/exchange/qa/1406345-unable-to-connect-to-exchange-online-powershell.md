---
title: "Unable to connect to Exchange Online Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1406345/unable-to-connect-to-exchange-online-powershell
question_id: 1406345
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Unable to connect to Exchange Online Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1406345/unable-to-connect-to-exchange-online-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am unable to login to Exchange Online Powershell using the following steps. I am a global admin and the Powershell is opened in elevated mode.

I enter the code below

`Connect-ExchangeOnline -UserPrincipalName <mylogin>`

Then the login opens and I select my user

It loads for some time then closes and I get the following message in Powershell 

This V3 EXO PowerShell module contains new REST API backed Exchange Online cmdlets which doesn't require WinRM for Client-Server communication. You can now run these cmdlets after turning off WinRM Basic Auth in your client machine thus making it more secure.
Unlike the EXO* prefixed cmdlets, the cmdlets in this module support full functional parity with the RPS (V1) cmdlets.
V3 cmdlets in the downloaded module are resilient to transient failures, handling retries and throttling errors inherently.
REST backed EOP and SCC cmdlets are also available in the V3 module. Similar to EXO, the cmdlets can be run without WinRM basic auth enabled.
For more information check https://aka.ms/exov3-module

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-04*

Horrible banner massage!
