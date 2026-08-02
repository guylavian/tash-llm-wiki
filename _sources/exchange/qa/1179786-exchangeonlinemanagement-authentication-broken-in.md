---
title: "ExchangeOnlineManagement authentication broken in Azure Automation Runbook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179786/exchangeonlinemanagement-authentication-broken-in
question_id: 1179786
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["azure-automation", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# ExchangeOnlineManagement authentication broken in Azure Automation Runbook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179786/exchangeonlinemanagement-authentication-broken-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since the morning of Thursday 9 Feb 2023, I've not been able to successfully authenticate with ExchangeOnlineManagement via an Azure Automation runbook using either a credential flow or Managed Identity. I can replicate this issue across three different tenants on three different subscriptions. It was working fine up until Thursday, now I get the following error:

PowerShell v5.1 / ExchangeOnlineManagement v3.1.0 using Managed Identity

PowerShell v7.1 / ExchangeOnlineManagement v3.1.0 using Managed Identity

PowerShell v7.1 / ExchangeOnlineManagement v3.1.0 using Credential flow

## Answer (community) — Microsoft Moderator

*upvotes: 5 · updated: 2023-03-01*

@Steve Johnson  , Rajesh1257, Martyn Burgess - based on the investigation it appears that some of the default PS modules are not getting loaded in the script when it is executing in the Azure Sandbox. In addition to EXO module please upload the following modules as well to Automation Account to ensure that they are available for loading by the runbook job -  

-  PowerShell Gallery | PackageManagement 1.4.8.1 and 

-  PowerShell Gallery | PowerShellGet 2.2.5 

Hope this helps. Please let us know if you have any questions.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-08-02*

So, yet another bug and how to solve it.

If you want to use Az.Storage on the same Runbook with EXOv3, you will need to not use:

```
Get-EXORecipient -ResultSize Unlimited
```

You will use, as this one works.

```
Get-Recipient -ResultSize Unlimited
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-02*

You want more? Disconnect-ExchangeOnline, the most basic cmdlet, fails to execute on Runtime 7.2 with an erroneous Job fail and without any exception logged.

Does not work as any of the below:

`Disconnect-ExchangeOnline -Confirm:$False`

`(access denied error)`

`Disconnect-ExchangeOnline -ConnectionId`

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-02*

Just to give an idea of the mess, if one tries to do this, it works.

```
Get-EXORecipient -ResultSize Unlimited
```

BUT if the poor fellow, also tries to import another needed Module (from the Azure ones!) this is what they get for the same snippet.

```
Import-Module Az.Storage

Get-EXORecipient: 
Line |
  28 |  $ValidAddresses = Get-EXORecipient -ResultSize Unlimited
     |                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     | Could not load file or assembly 'Microsoft.OData.Core, Version=7.15.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35'. Could not find or load a specific file. (0x80131621)
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-02*

Azure Automate, is a flying circus. I have been so disappointed by this service and module; I feel it is a pack of crumbling pieces.

Issue after an issue after an issue. Latest one is the same code snippet failing on one runbook and working on the other, both on the same Runtime and Automation account.

Really, Azure automate should NOT be considered a dependable service, rather something in Preview.
