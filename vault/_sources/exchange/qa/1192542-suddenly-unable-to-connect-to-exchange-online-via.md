---
title: "Suddenly unable to connect to Exchange Online via Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1192542/suddenly-unable-to-connect-to-exchange-online-via
question_id: 1192542
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Suddenly unable to connect to Exchange Online via Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1192542/suddenly-unable-to-connect-to-exchange-online-via (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Suddenly (started on 13 of March) I can't connect to the ExchangeOnline via Powershell.

With no changes to the infrastructure I started getting the following error.  Could you suggest troubleshooting steps, please? 

```
An error occurred while sending the request.
At C:\Program 
Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.1.0\netFramework\ExchangeOnlineManagement.psm1:729 char:21
+                     throw $_.Exception.InnerException;
+                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (:) [], HttpRequestException
    + FullyQualifiedErrorId : An error occurred while sending the request.
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-03-24*

Hi @Tomasz Kasinski  ,

Based on your description, we have the following suggestions to troubleshoot our issue.

- 

-  Please confirm whether other administrator accounts can connect. Or whether it is feasible to use other machines to connect.

-  If other admin accounts can connect normally, it is recommended to use the following cmdlet to view the remote PowerShell access status for your account.

```
Get-User -Identity "" | Format-List RemotePowerShellEnabled
```

-  If none of the above works, check the service health status on the M365 Admin Center and see if there’s any potentially related advisory.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
