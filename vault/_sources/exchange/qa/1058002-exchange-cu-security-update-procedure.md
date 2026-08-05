---
title: "Exchange CU security update procedure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1058002/exchange-cu-security-update-procedure
question_id: 1058002
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange CU security update procedure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1058002/exchange-cu-security-update-procedure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am not an expert into update the Exchange CU security update (Exchange Server 2016 CU23 Oct22SU) and I would like some help to understand the options available to do this task.  

Reading the micrisoft documentation (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019)  

it seems if want to install the CU I have 2 steps:

Download the CU ISO file

1) - Prepare AD

```
E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareSchema  
     E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD /OrganizationName:"Contoso Corporation"  
     E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAllDomains
```

2) - Install Exchange CU

```
1. Install an Exchange CU using the Setup wizard  
   2. Install an Exchange CU using unattended Setup from the command line (E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade /DomainController:dc01.contoso.com)
```

What about to install/update just the Security update (Exchange Server 2016 CU23 Oct22SU)?  

I have to download and install it or do I need to do the first step as well -->prepare AD?  

Do I have also execute the maintenance scripts:  

---Start-ExchangeServerMaintenanceMode v1.8.ps1  

---Stop-ExchangeServerMaintenanceMode v1.5.ps1.

PS: What exactly do they do?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-30*

The installation went well , but, unfortunately after installed the extended protection I received two inconveniences:    

```
1) Public ecp link was not reachable.   
     2) Public folrder were not visible
```

Most likely the problem is due to the KEMP that standing in the middle is unable to manage the SSL traffic generated after enabling the extended protection.     

https://microsoft.github.io/CSS-Exchange/Security/Extended-Protection/    

    

I had to do a roll-back    

I found someone had the same issue using this solution :     

Set-OutlookAnywhere -Identity 'Exch_SERVER1\RPC (Default Web Site)' -SSLOffloading $false -InternalClientsRequireSsl $true -ExternalClientsRequireSsl $true    

Run this command could help?     

Any advice?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

Hi @Marc  ,    

Agree Andy, you do not need to PrepareAD. It is recommended that you run the maintenance script to put the server into maintenance mode before installing SU and exit maintenance mode after the installation is complete.    

Extended Protection enhances the existing authentication functionality in Microsoft Exchange Server to help mitigate authentication relay or "man in the middle" attacks.    

Yes, your steps are right.    

You can also get this Exchange SU through the method in the official article.    

For more information about installing the Exchange SU, you can refer to: install-exchange-security-update    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-23*

Although Windows Extended Protection (EP) is enabled the health Check has found vulnerability to all CUs below (CU23 October).     

How do I download them?    

Are the steps below the right one?    

https://support.microsoft.com/en-us/topic/description-of-the-security-update-for-microsoft-exchange-server-2019-and-2016-october-11-2022-kb5019077-b5ae8793-5e5c-4faa-972d-9228945973e5

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-21*

When installing a SU, unless specifically called out in the KB, you do not need to PrepareAD    

https://techcommunity.microsoft.com/t5/exchange-team-blog/released-october-2022-exchange-server-security-updates/ba-p/3646263    

    

Since you are applying updates, I would still run the maintenance scripts to ensure the servers are not being accessed by clients or handle mail flow etc..
