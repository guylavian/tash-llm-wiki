---
title: "Getting an error when trying to setup Exchange Online ForwardingAddress in Azure Runbook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689319/getting-an-error-when-trying-to-setup-exchange-onl
question_id: 1689319
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-automation", "office-exchange-office-exchange-server-development", "windows-business-windows-server-user-experience-powershell"]
---
# Getting an error when trying to setup Exchange Online ForwardingAddress in Azure Runbook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689319/getting-an-error-when-trying-to-setup-exchange-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to setup an Azure Automation Runbook in which I convert a User Mailbox to a Shared Mailbox and setup a ForwardingAddress.

I setup all the permissions and converting the mailbox is working, setting a forwarding address throws the following error: 

```
|Microsoft.Exchange.Data.Directory.InsufficientPermissionsException|Source server:AM0PR08MB4529.eurprd08.prod.outlook.com doesn't have write permission to target DC:. Usually it indicates that target forest isn't an account partition of source forest. The user has insufficient access rights.
```

This is the script I am using:

```
Param (
 [string] $Employee = ""
 )

Connect-ExchangeOnline -ManagedIdentity -Organization .onmicrosoft.com

$Mailbox = Get-Mailbox -Identity $Employee -ErrorAction SilentlyContinue

if ($Mailbox -eq $null) {}
    elseif ($Mailbox.RecipientTypeDetails -eq "SharedMailbox") {}
    else {
        Set-Mailbox -Identity $Employee -Type Shared -ErrorAction SilentlyContinue
}

Set-Mailbox -Identity $Employee -DeliverToMailboxAndForward $true -ForwardingAddress ""
```

If anyone knows a way to solve this please let me know.

Thank you!

## Answers

_No answers on this thread._
