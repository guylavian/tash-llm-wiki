---
title: "Unable to connect to exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2122962/unable-to-connect-to-exchange-online
question_id: 2122962
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to connect to exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2122962/unable-to-connect-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

While using `Connect-ExchangeOnline -CertificateThumbprint $CertificateThumbprint -AppId $ClientId -Organization $Organization` Command to establish connection to exchange online, randomly I get the error the following error:

```
Module could not be correctly formed. Please run Connect-ExchangeOnline again.
At C:\Users\MY-USER\Documents\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.6.0\netFramework\ExchangeOnlineManagement.psm1:766 char:21
+                     throw $_.Exception;
+                     ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : RuntimeException
```

Everything was working fine, this started happening out of no-where, and even now it works like 7 times and fails once.

The App that I use is granted the following API Permissions:
And also has a role named as Exchange Administrator from Microsoft Entra set of roles assigned to itself. 

-  I also looked here: https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps and can see that the permissions and certificate are set properly. 

-  I also updated the ExchangeOnlineManagement module, no luck yet 

-  This is part of a bigger playbook which runs automatically every night at 1 AM to offboard users, when it runs as a scheduled job everything works fine, but if I am to trigger the whole playbook and launch it or try this command only I get this error

Thanks for the help

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-26*

Hi @Yaser Mowlawizadah  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you're encountering an intermittent issue with the Exchange Online Management Module. Here are a few troubleshooting steps you can try to resolve this problem:

-  Make sure you are using the latest version of the module.

```
Update-Module -Name ExchangeOnlineManagement
```

-  Sometimes, reinstalling the module can fix issues related to corrupted files.

```
Uninstall-Module -Name ExchangeOnlineManagement -AllVersions 
Install-Module -Name ExchangeOnlineManagement
```

-  Sometimes, clearing the current PowerShell session and restarting it can help.

```
Remove-Module ExchangeOnlineManagement 
Start-Sleep -Seconds 10 
Import-Module ExchangeOnlineManagement 
Connect-ExchangeOnline
```

-  Make sure you have a stable and reliable network connection as intermittent connectivity issues can sometimes cause this problem.

-  Test by connecting from a different machine or user profile to determine if the issue is specific to your current setup.

-  You can enable diagnostic logging to get more detailed information about what might be causing the issue.

```
$DebugPreference = "Continue" 
Connect-ExchangeOnline -UserPrincipalName  -ShowProgress $true -Verbose
```

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
