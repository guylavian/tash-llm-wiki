---
title: "ExchangeOnline Import-Module ExchangePowershell error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1296266/exchangeonline-import-module-exchangepowershell-er
question_id: 1296266
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ExchangeOnline Import-Module ExchangePowershell error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1296266/exchangeonline-import-module-exchangepowershell-er (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to get Disable-DistributionGroup to work as we are trying to convert a distro list to a shared mailbox. I have been trying to get this to work for the last 2 days, searching for an answer but cannot seem to find it. I recently just upgraded to ExchangeOnlineManagement 3.1.0, also tried on 3.0.0. I can install the ExchangePowerShell but when i try to import it, it keeps giving me the following error listed below.

ExchangeOnlineManagement imports with no issue, any ideas on how to get past this issue is greatly appreciated.

```
PS C:\Windows\system32> Import-Module ExchangePowerShell
Import-Module : Exchange Server system variable ExchangeInstallPath missing.
At line:1 char:1
+ Import-Module ExchangePowerShell
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (Exchange Server...llPath missing.:String) [Import-Module], RuntimeException
    + FullyQualifiedErrorId : Exchange Server system variable ExchangeInstallPath missing.,Microsoft.PowerShell.Comman
   ds.ImportModuleCommand
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-02*

Hi @ Michael Freeman,

please refer to the commands to connect to the exchange online powershell with Global Administrator or Exchange Administrator:

 

```
import-module ExchangeOnlineManagement

 Connect-ExchangeOnline -UserPrincipalName ******@xx.ch
```

 

After the connection is successful, you can run the relevant Exchange commands such as Disable-DistributionGroup .

Here is a similar thread for you reference: import-module exchangepowershell throws exchangeinstallpath missing - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
