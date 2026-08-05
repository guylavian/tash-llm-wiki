---
title: "Change Exchange Server 2016 Certificate Setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301516/change-exchange-server-2016-certificate-setting
question_id: 301516
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Change Exchange Server 2016 Certificate Setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301516/change-exchange-server-2016-certificate-setting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good night, how can I change the search name ve001s101.xxxxxx.local to mail.xxxxxx ****, because the certificate is giving me an error and I already changed everything that pointed in the DNS to ve001s101.xxxxxxx.local to this address to mail.xxxxx **** but still the error I really appreciate your help since it is the first time that I enter this forum Saludos![74850-captura.png][1] [1]: /api/attachments/74850-captura.png?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

@JC Suárez      

".local" isn't  a valid certificate for Exchange server if you want to access from the Internet, I would suggest you use ".com" to replace it. If you just use Exchange within your organization, you can still use "mail.domain.local"    

If you want to use "mail.domain.com", you need to add "domain.com" as an accepted domain on Exchange server, then change all mailbox email address from "domain.local"  to "domain.com".    

Then change all service URL from "server.domain.local" to "mail.domain.com". You can use commands below to check them:    

```
Get-OutlookAnywhere | Select Server,InternalHostName,ExternalHostName  
Get-MAPIVirtualDirectory | Select Server,InternalURL,ExternalURL   
Get-OABVirtualDirectory | Select Server,InternalURL,ExternalURL  
Get-WebServicesVirtualDirectory | Select Server,InternalURL,ExternalURL  
Get-ClientAccessServer | Select Name,AutoDiscoverServiceInternalUri
```

After modify service URL, you need to run IISReset in CMD to restart IIS service.    

If you need to access Exchange server from internal of your organization, you also need to add "domain.com" as a Lookup Zones on your DC, then copy all DNS records(Such as Autodiscover, mail, ExchangeSverer) from "domain.local" lookup zone to the  "domain.com" lookup zone.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
