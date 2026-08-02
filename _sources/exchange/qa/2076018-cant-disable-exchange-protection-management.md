---
title: "Can't disable Exchange protection Management."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2076018/cant-disable-exchange-protection-management
question_id: 2076018
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can't disable Exchange protection Management.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2076018/cant-disable-exchange-protection-management (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Exchange 2016. Last CU.

Im try disable with script:

Why he cant load EMS ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-23*

Hi @Андрей Михалевский,

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing a common problem with the Exchange Management Shell (EMS) when trying to disable Extended Protection. Here are some steps to help you troubleshoot and resolve this issue: 

-  Make sure you are running the Exchange Management Shell as an administrator. Right-click the EMS shortcut and select "Run as Administrator". 

-  Make sure you have the latest version of the ExchangeExtendedProtectionManagement.ps1 script. Microsoft frequently updates these scripts to fix bugs and improve functionality. 

-  Run the script with the -PrerequisitesCheckOnly parameter to ensure that all prerequisites are met: 

```
.\ExchangeExtendedProtectionManagement.ps1 -PrerequisitesCheckOnly
```

-  The error message "Length cannot be less than zero. Parameter name: Length" indicates that there may be a problem with the script or environment. Check the detailed error log for more information. 

-  Sometimes, reinstalling the latest cumulative update (CU) or security update can resolve EMS issues. Make sure your server is fully updated. 

-  If the script has partially applied changes, you may need to roll back the configuration. Restore the IIS application configuration using the following command: 

```
.\ExchangeExtendedProtectionManagement.ps1 -RollbackType "RestoreIISAppConfig"
```

-  Ensure that the TLS settings on the Exchange server are consistent and meet the requirements for Extended Protection. 

If these steps do not resolve the issue, please share any specific error messages or logs you see and I can help further!

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-22*
