---
title: "PowerShell-> ExchangeOnlineManagement-> Connect-ExchangeOnline is failing with 500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1669426/powershell-exchangeonlinemanagement-connect-exchan
question_id: 1669426
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# PowerShell-> ExchangeOnlineManagement-> Connect-ExchangeOnline is failing with 500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1669426/powershell-exchangeonlinemanagement-connect-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

New-ExoPSSession : Connecting to remote server outlook.office365.com failed with the following error message : The

WinRM client received an HTTP server error status (500), but the remote service did not include any other information

about the cause of the failure. For more information, see the about_Remote_Troubleshooting Help topic.

At C:\Program

Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\2.0.5\netFramework\ExchangeOnlineManagement.psm1:475 char:30

-  ... PSSession = New-ExoPSSession -ExchangeEnvironmentName $ExchangeEnviro ...

- 

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : ResourceUnavailable: (:) [New-ExoPSSession], PSRemotingTransportException

-  FullyQualifiedErrorId : System.Management.Automation.Remoting.PSRemotingDataStructureException,Microsoft.Exchang

   e.Management.ExoPowershellSnapin.NewExoPSSession

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-17*

Hi @Microsoft CDX,

Thank you for posting to Microsoft Community. We are happy to help you.

According to the information, I understand that there is an issue connecting to Exchange Online by PowerShell. The cause of this error may be Remote PowerShell (RPS) is being deprecated and disabled in your tenant.

The older Exchange Online module use RPS for client to server communication. Unfortunately, RPS is legacy technology that is outdated and can pose security risks. Therefore, the V2 module would no longer work after RPS is completely turned off. You could refer to Deprecation of Remote PowerShell in Exchange Online – Re-enabling or Extending RPS support - Microsoft Community Hub for more information.

Therefore, please consider updating to V3 module as the following link Connect to Exchange Online PowerShell | Microsoft Learn to see if it works for you.

If there is anything else we can do for you, please feel free to contact me.
