---
title: "OWA  timezone and regional settings error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/379292/owa-timezone-and-regional-settings-error
question_id: 379292
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# OWA  timezone and regional settings error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/379292/owa-timezone-and-regional-settings-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have upgraded to exchange 2016 CU20 . But many existing users and new users getting below error while accessing outlook web access :  

"This method or property is not supported after HttpRequest.Form, Files, InputStream, or BinaryRead has been invoked."  

how can we solve this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-03*

Hi @Muhammed Shehim   ,  

Did you change any Exchange related settings before this issue occured?

1..As a workaround, you could run the following command to setting the correct timezone and regional for all user mailboxes:

```
Get-mailbox -ResultSize unlimited | Set-MailboxRegionalConfiguration -Timezone "<>"
```

Have you set up the Web Application Proxy for OWA?  

2.Please run the following command to check the settings of the OWA virtual directory, especially whether the internal and external URLs are the same.

```
Get-OWAVirtualdirectory | fl *auth*,*url*
```

3.If you set the WAP, please run the following command and see if the issue is resolved:

```
Get-WebApplicationProxyApplication [app name] | SetWebApplicationProxyApplication -DisableTranslateUrlInRequestHeaders -DisableTranslateUrlInResponseHeaders
```

There is a similar case：Connection to the backend server failed. Error: (0x80072ef1). OWA with Claim through WAP and ADFS

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-01*

could anyone help to solve this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-01*

when we run the below command web access is working. But all the new users we create and old few users also facing this issue. how can we solve this issue without manually running the below command for each user  

Set-MailboxRegionalConfiguration -Identity test15 -Language en-US -LocalizeDefaultFolderName -TimeZone "Arabian Standard Time" -TimeFormat "h:mm tt'
