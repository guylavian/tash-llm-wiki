---
title: "Exchange 2019 cu 19 owa"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/336875/exchange-2019-cu-19-owa
question_id: 336875
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 cu 19 owa

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/336875/exchange-2019-cu-19-owa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, Recently i have updated exchange cu from 12 to 19 and it was successful. But i realised some issue arise pertaining to owa. my owa: domain.com/owa i'm able to login but unable to open up my email with error 404. the url is https://domain.com/owa/owa#path=/mail But if i change the url to https://domain.com/owa/#path=/mail which is without owa from #path, i'm able to open my email without any issue. Any solutions for me?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-31*

Hi @William Tey   ,  

Does your Exchange server version is Exchange 2016 CU19?  

Is there a problem with logging in to ECP?  

Have you set up a redirect to login OWA URL?

1.Please run the first command below to verify that the url and Authentication method of OWA are correct. You can also run the second command to verify that the authentication method of ECP is the same as that of OWA.

```
Get-OWAVirtualdirectory | fl *url*,*auth*  
Get-ECpVirtualdirectory | fl *url*,*auth*
```

2.Please check the authentication method of OWA backend in IIS, the following picture is the default setting  

3.Please try to recycle the MSExchangeOWAAppPool in Application Pools in IIS. Then run the “IISRESET” in the CMD started by the administrator to reset the IIS.

4.Please run the following commands to remove and re-create the OWA virtual directory. Then run the “IISRESET” in the CMD started by the administrator to reset the IIS.

```
Remove-OwaVirtualDirectory -Identity <>  
New-OwaVirtualDirectory -WebSiteName <> -ExternalUrl <> -InternalUrl <>
```

For more information : New-OwaVirtualDirectory and Remove-OwaVirtualDirectory

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
