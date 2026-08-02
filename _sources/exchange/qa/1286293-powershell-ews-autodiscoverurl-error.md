---
title: "PowerShell EWS AutoDiscoverURL Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1286293/powershell-ews-autodiscoverurl-error
question_id: 1286293
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# PowerShell EWS AutoDiscoverURL Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1286293/powershell-ews-autodiscoverurl-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon.

I hope you are well.

I am looking for the option to access an Outlook mailbox (Exchange) through a token without having to enter the credentials of a user. With the following code:

$TenantId = “xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”  

$AppClientId = “xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”  

$ClientSecret = “xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”  

$RequestBody = @{client_id=$AppClientId;client_secret=$ClientSecret;grant_type=”client_credentials”;scope=”https://graph.microsoft.com/.default”;}  

$OAuthResponse = Invoke-RestMethod -Method Post -Uri https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token -Body $RequestBody  

$AccessToken = $OAuthResponse.access_token  

Import-Module "C:\Program Files\Microsoft\Exchange\Web Services2.2\Microsoft.Exchange.WebServices.dll"  

$MailboxName ="******@dominio.onmicrosoft.com"  

$Service = [Microsoft.Exchange.WebServices.Data.ExchangeService]::new()  

$Service.Credentials = [Microsoft.Exchange.WebServices.Data.OAuthCredentials]$AccessToken  

$Service.Url = “https://outlook.office365.com/EWS/Exchange.asmx”  

$Service.AutodiscoverUrl($MailboxName,{$true})

It is throwing the following error:

```
Exception calling "AutodiscoverUrl" with arguments "2": "The Autodiscover service couldn't be located."
Online: 29 Character: 1
+ $Service.AutodiscoverUrl($MailboxName,{$true})
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     + CategoryInfo : NotSpecified: (:) [], MethodInvocationException
     + FullyQualifiedErrorId : AutodiscoverLocalException
```

I hope you can help me

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-18*

Hello there,

For O365 mailboxes, you can safely hardcode the Autodiscover URL to "https://outlook.office365.com/EWS/Exchange.asmx"

and avoid any lookup issues.

AutoDiscoverv1 doesn't support the client credentials flow so you need to remove the line

$ews.AutodiscoverUrl($MailboxName,{$true})

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-18*

I will recommend to you enable Traces, to achieve this following:

`Service.TraceEnabled = true;`

I was facing the same issue then when I enabled traces. These traces will guide you on what exactly is happening. In my case, the SSL certificate issue is there to solve it. I followed the following post.

There can be many issues, such as:

Users can be blocked.

The DNS can't find autodiscover.domain.com.
