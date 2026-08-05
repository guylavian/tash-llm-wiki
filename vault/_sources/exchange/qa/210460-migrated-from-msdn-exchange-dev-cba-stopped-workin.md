---
title: "[Migrated from MSDN Exchange Dev]CBA stopped working in Exchange 2019 activesync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/210460/migrated-from-msdn-exchange-dev-cba-stopped-workin
question_id: 210460
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# [Migrated from MSDN Exchange Dev]CBA stopped working in Exchange 2019 activesync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/210460/migrated-from-msdn-exchange-dev-cba-stopped-workin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.    

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/8b754ed4-5bff-4975-98c1-45b23937cfa8/cba-stopped-working-in-exchange-2019-activesync?forum=exchangesvrdevelopment    

Hi All,    

we had working exchange 2019 installation for more than a year. Activesync configured with certificate based authentication and everything was working fine. All of the sudden yesterday all mobile devices stopped synchronizing with the server. When troubleshooting the issue we found out that activesync is working with basic authentication (login and password) but no longer working with certificates. No configuration changes was made at the moment, PKI working fine in the domain.    

Today we installed new exchange 2019 server in the same domain hoping CBA will work on it, but all in vain. The server behaves exactly like the old one. When we trying to open  url https://server/microsoft-server-activesync and use certificate for authentication then we get 403 error,  if we use login and pass everything is ok.    

CBA was setup with https://learn.microsoft.com/ru-ru/exchange/plan-and-deploy/post-installation-tasks/configure-certificate-based-auth?view=exchserver-2019, and we have the same configurations in other lorganizations where there are E2013 and E2016 - all works fine.    

Please help, need new ideas.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-25*

Hi Lou,    

the issue resolved. The problem was with non-self-signed certificate being installed in Trusted Root Certification Authorities Certificate store via group policy.    

https://learn.microsoft.com/en-us/troubleshoot/iis/http-403-forbidden-access-website    

thank you very much for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-25*

Hi Lou,    

thank you for your answer.    

not the same certificates but the infrastructure configured same way.    

attached the screenshot of the Get-ActiveSyncVirtualDirectory -Server “ServerName” | FL    

thanks!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-25*

Hi Freddy,

and we have the same configurations in other lorganizations where there are E2013 and E2016 - all works fine.

You mean the a same Certificate works fine on 2013/2016 but not 2019? Any different settings between these servers?

When we trying to open url https://server/microsoft-server-activesync and use certificate for authentication then we get 403 error

You can find a detailed error code in C:\inetpub\logs\LogFiles\W3SVC\XXXX.log file, search Microsoft-Server-ActiveSync and you will find the error code like:  

According to your description, I think the ActiveSync is still using basic authentication, please sse this command and check the following:

```
Get-ActiveSyncVirtualDirectory -Server “ServerName” | FL
```

Part 1. These values are correct with your certificate.  

Part 2. These three auth methods are disabled, and ClientCertAuth is required.  

You can also take a screenshot and share with me by covering your personal information. This article Configure certificate-based authentication for Exchange ActiveSync and The HTTP status code in IIS 7.0 and later versions may help you.

Regards,

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
