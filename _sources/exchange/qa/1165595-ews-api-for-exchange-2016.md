---
title: "EWS API for Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165595/ews-api-for-exchange-2016
question_id: 1165595
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# EWS API for Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165595/ews-api-for-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've got a EWS API script to delete emails from Inbox and not subfolders for 2010 and not sure why it's not working for 2016.   

Getting the following error,

```
Exception calling "FindItems" with "2" argument(s): "The request failed. The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel."
At line:1 char:1
+ $Service.FindItems( 'Inbox', ( New-Object Microsoft.Exchange.WebServi ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : ServiceRequestException
```

Partial Code

```
Add-Type -Path 'C:\Program Files\Microsoft\Exchange\Web Services\2.0\Microsoft.Exchange.WebServices.dll'

$Service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService(
    [Microsoft.Exchange.WebServices.Data.ExchangeVersion]::$ExchangeVersion
)
$Service.UseDefaultCredentials = $true
$Service.URL = New-Object Uri( $EwsUrl )
$Service.ImpersonatedUserId = New-Object Microsoft.Exchange.WebServices.Data.ImpersonatedUserId(
    [Microsoft.Exchange.WebServices.Data.ConnectingIdType]::SmtpAddress, $SmtpAddress

$Service.FindItems( 'Inbox', ( New-Object Microsoft.Exchange.WebServices.Data.ItemView( $PageSize, $Offset ) ) )
Exception calling "FindItems" with "2" argument(s): "The request failed. The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel."
At line:1 char:1
+ $Service.FindItems( 'Inbox', ( New-Object Microsoft.Exchange.WebServi ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : ServiceRequestException
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-31*

This fixes the issue,

[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-31*

The following worked by ignoring the certificate !

[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-31*

Looks like a TLS 1.2 issue your operating system should handle correctly the TLS connection see https://learn.microsoft.com/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client

you can force this in PowerShell by using

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

 at the top of your script it's not recommended as you want you script to just follow on whenever TLS is updated on the server eg TLS 1.3 which should happen if you set the registry entries correctly. But if you need a quick fix that should work
