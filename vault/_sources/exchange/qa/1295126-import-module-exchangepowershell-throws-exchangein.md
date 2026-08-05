---
title: "import-module exchangepowershell throws exchangeinstallpath missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1295126/import-module-exchangepowershell-throws-exchangein
question_id: 1295126
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# import-module exchangepowershell throws exchangeinstallpath missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1295126/import-module-exchangepowershell-throws-exchangein (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i'd like to automate some stuff and need to use Add-RecipientPermission.

I used install-module exchangepowershell -scope currentuser

and tried to load the module with

import-module exchangepowershell

but i get the below error. 

```
import-module : Exchange Server system variable ExchangeInstallPath missing.
At line:1 char:1
+ import-module exchangepowershell
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (Exchange Server...llPath missing.:String) [Import-Module], RuntimeException
    + FullyQualifiedErrorId : Exchange Server system variable ExchangeInstallPath missing.,Microsoft.PowerShell.Commands.ImportModuleCommand
```

I am wondering whats wrong, this should work on a client machine, not on an exchange server. We use the cloud version of outlook, so there is no exchange on premise at all.

whats also wierd, i have a win10 machine in the network (no access right now) and that works, but i dont know what i did or whats the current situation. right now i am connected through a vpn to a dev server (win11 client) that is inside the AD

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2023-05-31*

If you are using Exchange Online, follow these steps to connect:

the correct command to import:

```
Import-Module ExchangeOnlineManagement
```

https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-06-01*

Hi @ OliDE,

This cmdlet is available only in the cloud-based service (Exchange online).

In addition to using this command(Import-Module ExchangeOnlineManagement) to import the Exchange PowerShell module, you need to log on to Exchange Online PowerShell with an Exchange administrator account:

 

```
Connect-ExchangeOnline -UserPrincipalName ******@contoso.onmicrosoft.com
```

 

After entering the password for successful verification, use the Exchange Online related commands.

For details of how to connect Exchange online PowerShell, please refer to this link: Connect to Exchange Online PowerShell | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

it was a permission problem... unfortunately there seems to be no delete comment option

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

this is so wierd... i changed nothing and it works again now. calling add-recipientinformation now works, thanks!
