---
title: "Connect-Exchange Online (Error while sending the request)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1432055/connect-exchange-online-error-while-sending-the-re
question_id: 1432055
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Connect-Exchange Online (Error while sending the request)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1432055/connect-exchange-online-error-while-sending-the-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm getting the below Error while connecting to Exchange Online (PowerShell Script) when called from .Net Application. 

```
#Import-Module ExchangeOnlineManagement
        #Connect-ExchangeOnline -Credential $Creds
```

```
An error occurred while sending the request.
At C:\Program 
Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.4.0\netFramework\ExchangeOnlineManagement.psm1:762 char:21
+                     throw $_.Exception.InnerException;
+                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (:) [], HttpRequestException
    + FullyQualifiedErrorId : An error occurred while sending the request.
```

I've checked the Credentials. Updated the Exchange Online Module. Checked .Net Framework and its Compatible. 

I'm using Windows PowerShell 5.1.  

Policy is been set to Bypass. 

Thanks & Regards

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-03-05*

I had the same issue, but was able to solve it by specifying Tls 1.2.

Add this line:

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

That should get you past that error.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-13*

We tried with registry keys for TLS, with latest updates for Exchange and Windows server.

The error was fixed temporarely, but now is back in all machines behind our customer network. So I just updated the Sonicwall, but the error persists.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-26*

Any steps to solve this issue?
