---
title: "can't load exchange 2013 hybrid ECP website"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/141534/cant-load-exchange-2013-hybrid-ecp-website
question_id: 141534
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# can't load exchange 2013 hybrid ECP website

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/141534/cant-load-exchange-2013-hybrid-ecp-website (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we are at office 365 hybrid setup and have windows 2012 server with Exchange 2013 hybrid server  

can't load exchange 2013 ECP website after I deleted IIS W3SVC1 log files by using delete shift, to clearup space and I could not bring back those deleted log files   

Now Getting ERROR: ERROR- Can not right configuration file  

 : C:\Windows\System32\inetsrv\config\applicationhost.config  

Anyone has workaround to fix this please

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-28*

@Bundoo  

What's the detailed version of your Exchange 2013? You can check with the following command:

```
Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion
```

What error message do you get after entering the URL of EAC? You can post the screenshot here, and don't forget to cover your personal information.  

Does OWA work as normal?

As SethWH mentioned, the error you provided may be caused by the server does not have available disk space. Here is the same error for your reference: IIS 7.5 Unable to write configuration file.  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If EAC still cannot work after freeing up disk space, here are more suggestions for you:  

-  Please check and make sure all needed Exchange services are running well.  

-  Recycle MSExchangeECPAppPool in Application Pools from IIS Manager. Application Pools > MSExchangeECPAppPool > Recycle.  

-  Run UpdateCas.ps1 and UpdateConfigFiles.ps1 from the exchange bin directory C:\Program Files\Microsoft\Exchange Server\V15\Bin.  

After that, use the following command to restart IIS:    iisreset /noforce  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-27*

Hello,

I don't think shift-deleting log files in inetpub would have caused this. Did you end up freeing space? Sometimes these errors can be related to insufficient space. How often is a full system backup (w/ System State) taken on the server? A full backup on Exchange will free up log space.

Once space has been cleared, are you able to reset exchange services (after hours or when use is minimal)?

Powershell script:

```
$services = Get-Service | ? { $_.name -like "MSExchange*" -and $_.Status -eq "Running"}

#Restart each service
foreach ($service in $services)
{
    Restart-Service $service.name -Force
}
```
