---
title: "Exchange Online PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1120602/exchange-online-powershell
question_id: 1120602
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1120602/exchange-online-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to switch from basic authentication to oauth and found this code in the documentation:    

$oauthTokenAsPassword = ConvertTo-SecureString '<EncodedOAuthToken>' -AsPlainText -Force    

$o365cred = New-Object System.Management.Automation.PSCredential ("admin@Company portal   .onmicrosoft.com", $oauthTokenAsPassword)    

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/PowerShell-LiveID/?BasicAuthToOAuthConversion=true&email=SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}[@](/users/na/?userId=a28c79c1-c609-48db-b55f-1783d1187afb).onmicrosoft.com -Credential $o365cred -Authentication Basic -AllowRedirection    

Import-PSSession $Session    

How do we replace for '<EncodedOAuthToken>'? Any help is appreciated. Thank you!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-08*

If the idea is to pass an access token directly, the latest preview version of the module should support that: https://www.powershellgallery.com/packages/ExchangeOnlineManagement/3.1.0-Preview1    

Otherwise, use Connect-ExchangeOnline as suggested above.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-07*

Use the Exchange Online module that supports Modern Auth    

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps
