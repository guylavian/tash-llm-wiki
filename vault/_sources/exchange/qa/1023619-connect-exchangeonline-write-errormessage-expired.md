---
title: "Connect-ExchangeOnline: Write-ErrorMessage : Expired or Invalid pagination request. Default Expiry time is 00:30:00"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1023619/connect-exchangeonline-write-errormessage-expired
question_id: 1023619
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 4
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Connect-ExchangeOnline: Write-ErrorMessage : Expired or Invalid pagination request. Default Expiry time is 00:30:00

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1023619/connect-exchangeonline-write-errormessage-expired (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I wrote a script a while back that gets the the UserPrincipalName, DisplayName, LastLogonTime, CreationTime, Inactive Days, MailboxType, AssignedLicenses, ItemCount, MB Size, and Roles from MSOnline and Exchange Online. It works fine on one server and my laptop but it fails with the message below. The server that I run it from is being decommissioned so I need to move it to a new server.  Why would the script work on a server and my laptop but nowhere else?      

```
PS>TerminatingError(Invoke-WebRequest): "{"error":{"code":"BadRequest","message":"Invalid Operation","innererror":{"message":"Invalid Operation","type":"Microsoft.Exchange.Admin.OData.Core.ODataServiceException","stacktrace":"   at Microsoft.Exchange.AdminApi.CommandInvocation.CommandInvocation.InvokeCommand(QueryContext queryContext, CmdletInvokeInputType cmdletInvokeInputType)\r\n   at Microsoft.Exchange.Admin.OData.Core.PathSegmentToExpressionTranslator.Translate(OperationImportSegment segment)\r\n   at Microsoft.Exchange.Admin.OData.Core.QueryContext.ResolveQuery(ODataContext context, Int32 level)\r\n   at Microsoft.Exchange.Admin.OData.Core.Handlers.OperationHandler.Process(IODataRequestMessage requestMessage, IODataResponseMessage responseMessage)\r\n   at Microsoft.Exchange.Admin.OData.Core.Handlers.RequestHandler.Process(Stream requestStream)","internalexception":{"message":"Expired or Invalid pagination request. Default Expiry time is 00:30:00","type":"System.Exception","stacktrace":""}}}}"  
    Write-ErrorMessage : Expired or Invalid pagination request. Default Expiry time is 00:30:00  
    At C:\Users\Me\AppData\Local\Temp\tmpEXO_3gsqzody.faf\tmpEXO_3gsqzody.faf.psm1:1107 char:13  
    +             Write-ErrorMessage $ErrorObject $IsFromBatchingRequest  
    +             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
        + CategoryInfo          : NotSpecified: (:) [Get-Mailbox], Exception  
        + FullyQualifiedErrorId : [Server=DM6PR14MB4156,RequestId=ebb50db0-607b-668c-4603-4639ca0ba4c1,TimeStamp=Wed, 21   
    Sep 2022 18:52:31 GMT],Write-ErrorMessage  
    Write-ErrorMessage : Expired or Invalid pagination request. Default Expiry time is 00:30:00  
    At C:\Users\Me\AppData\Local\Temp\tmpEXO_3gsqzody.faf\tmpEXO_3gsqzody.faf.psm1:1107 char:13  
    +             Write-ErrorMessage $ErrorObject $IsFromBatchingRequest  
    +             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
        + CategoryInfo          : NotSpecified: (:) [Get-Mailbox], Exception  
        + FullyQualifiedErrorId : [Server=DM6PR14MB4156,RequestId=ebb50db0-607b-668c-4603-4639ca0ba4c1,TimeStamp=Wed, 21 Sep 2022 18:52:31 GMT],Write-Erro  
       rMessage
```

## Answer (community) — Q&A User

*upvotes: 4 · updated: 2023-05-30*

When you send a command that returns more then 1.000 elements (e.g. Get-Mailbox in larger setups), the API endpoint returns the first 1.000 elements and a next link to the next page of 1.000 elements. This next link contains a skip token and helps the server to know where to continue. If the Powershell Module sends this second page request and you use certificate authentication like described in this article, it can happen that you immediately receive this timeout message. If this happens, please ensure you use the .onmicrosoft.com domain for the organization parameter and not a custom domain configured for your tenant.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-05-29*

have same issue, run a script and after 30 min in stops with error:

```
Write-ErrorMessage : Expired or Invalid pagination request. Default Expiry time is 00:30:00
At C:\Users\dmaa-t0\AppData\Local\Temp\21\tmpEXO_pha5tw53.per\tmpEXO_pha5tw53.per.psm1:1120 char:13
+             Write-ErrorMessage $ErrorObject
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Get-UnifiedGroup], Exception
    + FullyQualifiedErrorId : [Server=DB8PR03MB6137,RequestId=cf88c852-180d-5b56-cd1b-8c9ad358856c,TimeStamp=Mon, 29 May 2023 08:28:22 GMT],Write-ErrorMessage
```

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-09-30*

The script I was using was an old script that used Get-Mailbox and Get-MailboxStatistics which continued to fully function using ExchangeOnlineManagement Module V2.  However, when I moved the script to a new server, I installed the newest ExchangeOnlineManagement Module, V3. It seems that Get-Mailbox and Get-MailboxStatistics have been limited on V3.  I've updated my scripts to use Get-EXOMailbox and Get-EXOMailboxStatistics.  Using the newer commands has resolved the issue.
