---
title: "Connecting Exchange Online along with MicrosoftTeams in a single shell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237399/connecting-exchange-online-along-with-microsofttea
question_id: 2237399
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Connecting Exchange Online along with MicrosoftTeams in a single shell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237399/connecting-exchange-online-along-with-microsofttea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to automate a process that gives a report on the security checks of ExchangeOnline and MicrosoftTeams. I can able to authenticate in powershell using   

-  Connect-ExchangeOnline -AppId $ClientId -Certificate $cert -Organization $Organization   

-  Connect-MicrosoftTeams -Certificate $cert -ApplicationId $ClientId -TenantId $TenantIdindividually in different shells.  

The following issue occurs when I try to run the commands in same pwsh session  

Error:  

OperationStopped: Could not load file or assembly 'Microsoft.IdentityModel.Abstractions, Version=7.3.1.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35'. The located assembly's manifest definition does not match the assembly

reference. (0x80131040)  

I am using Ubuntu 24.04 LTS and following are the dependencies i have installed.

-  ExchangeOnlineManagement  - v3.5.1

-  Microsoft.PowerShell.Management - v7.0.0.0

-  Microsoft.PowerShell.Security   - v7.0.0.0

-  Microsoft.PowerShell.Utility    - v7.0.0.0

-  MicrosoftTeams - v6.9.0

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-21*

Hi @KALYANA SUDHEER PENUGONDA  ，  

Welcome to the Microsoft Q&A platform!  

It looks like there is a mismatch between the list of assemblies and the actual loaded files, consider using the isolated session Start-Job in the same powershell.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
