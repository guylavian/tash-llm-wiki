---
title: "Write-ErrorMessage : Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|The operation couldn't be performed because object '#usretailallleadership ' couldn't be found on 'DU2P123A09DC005.GBRP123A009.PROD.OUTLOOK.COM'."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2108696/write-errormessage-ex6f9304-microsoft-exchange-con
question_id: 2108696
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Write-ErrorMessage : Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|The operation couldn't be performed because object '#usretailallleadership ' couldn't be found on 'DU2P123A09DC005.GBRP123A009.PROD.OUTLOOK.COM'.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2108696/write-errormessage-ex6f9304-microsoft-exchange-con (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

PS C:\Users\marlon.womack> Set-ExecutionPolicy Remotesign -Scope CurrentUser

Import Exchange Module

Install-Module ExchangeOnlineManagement

Connect-ExchangeOnline

Import-Module ExchangeOnlineManagement 

$GroupList = Import-CSV C:\TMP\Retail_Import_Test.csv

ForEach ($group in $GroupList)

{

```
ForEach ($user in $GroupList)

{

    # Logic for handling users can be added here

}
```

$sanitizedAlias = $group.GroupName -replace ' ', '' -replace '[^a-zA-Z0-9]', ''

   Set-DistributionGroup -Alias $sanitizedAlias -managedby @{add=$($user.ManagedBy)}

#Set-DistributionGroup -Identity $group.GroupName -managedby @{add=$($user.ManagedBy)}

}

This V3 EXO PowerShell module contains new REST API backed Exchange Online cmdlets which doesn't require WinRM for Client-Server communication. You can now run these cmdlets after turning off WinRM Basic Auth in your client machine thus making it more secure

. 

Unlike the EXO* prefixed cmdlets, the cmdlets in this module support full functional parity with the RPS (V1) cmdlets.

V3 cmdlets in the downloaded module are resilient to transient failures, handling retries and throttling errors inherently. 

REST backed EOP and SCC cmdlets are also available in the V3 module. Similar to EXO, the cmdlets can be run without WinRM basic auth enabled. 

For more information check https://aka.ms/exov3-module

cmdlet Set-DistributionGroup at command pipeline position 1

Supply values for the following parameters:

Identity: #usretailallleadership

Write-ErrorMessage : Ex94914C|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|Couldn't find object "Erin Harrington ". Please make sure that it was spelled correctly or specify a different object.

At C:\Users\marlon.womack\AppData\Local\Temp\tmpEXO_oo1e12vi.htt\tmpEXO_oo1e12vi.htt.psm1:1205 char:13

- 

```
Write-ErrorMessage $ErrorObject
```

- 

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : NotSpecified: (:) [Set-DistributionGroup], ManagementObjectNotFoundException

-  FullyQualifiedErrorId : [Server=LO0P265MB6319,RequestId=cdbee040-8423-345d-3ab7-de141358c6dd,TimeStamp=Mon, 21 Oct 2024 23:12:29 GMT],Write-ErrorMessage

cmdlet Set-DistributionGroup at command pipeline position 1

Supply values for the following parameters:

Identity: #usretailallleadership

Write-ErrorMessage : Ex94914C|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|Couldn't find object "Erin Harrington ". Please make sure that it was spelled correctly or specify a different object.

At C:\Users\marlon.womack\AppData\Local\Temp\tmpEXO_oo1e12vi.htt\tmpEXO_oo1e12vi.htt.psm1:1205 char:13

- 

```
Write-ErrorMessage $ErrorObject
```

- 

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : NotSpecified: (:) [Set-DistributionGroup], ManagementObjectNotFoundException

-  FullyQualifiedErrorId : [Server=LO0P265MB6319,RequestId=051b4746-ac7d-91e1-204b-fc905edd84c8,TimeStamp=Mon, 21 Oct 2024 23:13:04 GMT],Write-ErrorMessage

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-22*

The Set-DistributionGroup expects some way to find the distribution group. That's usually the -Identity parameter. You haven't provided anything that uniquely identifies the DL.

What property name in your CSV can be used as aunique identity? The identity can be one of these:

-  Name

-  Alias

-  Distinguished name (DN)

-  Canonical DN

-  Email address

-  GUID

Looking at your code, I expect that something like this might work:

```
Set-DistributionGroup -Identity $group.Name -Alias $sanitizedAlias -managedby @{add=$($user.ManagedBy)}
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-21*

Write-ErrorMessage $ErrorObject

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-21*

Write-ErrorMessage $ErrorObject

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-21*

Write-ErrorMessage $ErrorObject
