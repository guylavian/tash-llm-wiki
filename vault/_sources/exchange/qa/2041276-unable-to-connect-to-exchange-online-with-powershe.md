---
title: "Unable to connect to Exchange Online with PowerShell Runtime 7.2 in Azure Automation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2041276/unable-to-connect-to-exchange-online-with-powershe
question_id: 2041276
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["azure-automation", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Unable to connect to Exchange Online with PowerShell Runtime 7.2 in Azure Automation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2041276/unable-to-connect-to-exchange-online-with-powershe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Cannot connect to Exchange Online with PowerShell Runtime 7.2 in Azure Automation.  

I would like to know how to connect to Exchange Online with Runtime 7.2.

The commands I have tried are as follows.

```
Connect-ExchangeOnline -ManagedIdentity -Organization customdomain.onmicrosoft.com

get-exomailbox user@custom.domain | Select DisplayName

DisConnect-ExchangeOnline -Confirm:$False
```

The following error was output.

`InvalidOperation: Unable to find type [Microsoft.Exchange.Management.RestApiClient.ExchangeEnvironment].`

It succeeds when tried with Runtime 5.1, so it does not seem to be the wrong command.

The settings I have made to prepare my environment are as follows.

-  ExchangeOnlineManagement module installed as Runtime 7.2.

-  As the system-assigned ManagedID is used, check that the status is on in the Automation account under Account Settings > ID > System Assigned.

-  In the Enterprise Applications menu of Entra ID, I looked for this Automation account, a Managed ID account, and added [Exchange.ManageAsApp] from [Office 365 Exchange Online] to the permissions.

The command New-MgServicePrincipalAppRoleAssignment was used.

Confirmed that the permission type has been added as Application.

-  In the ‘Roles and administrators’ menu of the Entra ID, the Automation account was added to the Exchange administrator.

In addition, although we thought it was unnecessary, we also added the following module as Runtime 7.2, but it did not improve the situation.

PackageManagement  

PowerShellGet

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2024-10-11*

In regards to this question *"I have the same problem in my dev machine with powershell 7.2 when importing the module ExchangeOnlineManagement (it works with PS 5.1):"   

*  

The problem is solved when installing version  3.5.0 "install-module ExchangeOnlineManagement  -RequiredVersion 3.5.0"  

As we can see in the in the module Release Notes, V3.5.1 was upgraded from .net 6 to .net 8   

https://www.powershellgallery.com/packages/ExchangeOnlineManagement/3.6.0
