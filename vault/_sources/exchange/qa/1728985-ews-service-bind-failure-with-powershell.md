---
title: "EWS service bind failure with powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1728985/ews-service-bind-failure-with-powershell
question_id: 1728985
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# EWS service bind failure with powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1728985/ews-service-bind-failure-with-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm facing an issue while trying to use a powershell script to connecto to Exchange 2016 EWS service to extract calendar info from users' mailboxes.

The error I get is

Exception calling "Bind" with "2" argument(s): "The request failed. The remote server returned an error: (401) Unauthorized."

At D:\Scripts\CalendarDumpToCSV\CalendarDumpToCSV-prova.ps1:141 char:1

-  $Calendar = [Microsoft.Exchange.WebServices.Data.Folder]::Bind($servi ...

- 

```
+ CategoryInfo          : NotSpecified: (:) [], MethodInvocationException

    + FullyQualifiedErrorId : ServiceRequestException
```

The relevant part of the script is 

$folderid= new-object Microsoft.Exchange.WebServices.Data.FolderId([Microsoft.Exchange.WebServices.Data.WellKnownFolderName]::Calendar,$MailboxName)   

$Calendar = [Microsoft.Exchange.WebServices.Data.Folder]::Bind($service,$folderid)

The user that is used to make the bind is the exchange Org Admin and has also been granted impersonation rights with 

New-ManagementRoleAssignment -name:impersonationAssignmen -Role:ApplicationImpersonation -User:******@xxx.xx

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-25*

I followed another thread's solution and installed the scripts into another server from the exchange server itself and worked without impersonation.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-06-25*

You need to impersonate the owner of the folder before attempting the Bind operation. Something like this should do:

```
$smtpAddress = "******@domain.com"

$service.ImpersonatedUserId = New-Object Microsoft.Exchange.WebServices.Data.ImpersonatedUserId([Microsoft.Exchange.WebServices.Data.ConnectingIdType]::SmtpAddress, $smtpAddress)
```
