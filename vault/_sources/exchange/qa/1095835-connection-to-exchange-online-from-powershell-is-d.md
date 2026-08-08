---
title: "connection to exchange online from powershell is declining suddenly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1095835/connection-to-exchange-online-from-powershell-is-d
question_id: 1095835
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# connection to exchange online from powershell is declining suddenly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1095835/connection-to-exchange-online-from-powershell-is-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We encountered a problem that we are not able to connect to exchange from powershell anymore, It's connects normally from another account so the problem isn't from machine, it in the account. It was fine before yesterday, Today I wake up suddenly to find this error:

New-PSSession : [ps.outlook.com] Connecting to remote server ps.outlook.com failed with the following error message :  

Access is denied. For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:12  

-  $Session = New-PSSession -ConfigurationName Microsoft.Exchange -Conne ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : AccessDenied,PSSessionOpenFailed

I've tried many solution in the internet with no results: security defaults are disabled, Basic Auth enabled for all protocols.

I use this commands for connection:

$LiveCred = Get-Credential  

$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://ps.outlook.com/powershell/ -Credential $LiveCred -Authentication Basic -AllowRedirection  

Import-PSSession $Session

I Need Help Urgently Please.  

Thanks in advance

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-11-19*

The method you are using is decade old by now, update your scripts. And make sure you are using modern auth, as legacy methods are now blocked. Using the V3 module will let you bypass all these issues: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#install-and-maintain-the-exchange-online-powershell-module
