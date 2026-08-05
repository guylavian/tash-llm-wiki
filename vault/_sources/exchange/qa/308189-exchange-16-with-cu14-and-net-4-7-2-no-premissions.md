---
title: "Exchange 16 with CU14 and NET 4.7.2 no Premissions to Update ti New CU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/308189/exchange-16-with-cu14-and-net-4-7-2-no-premissions
question_id: 308189
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 16 with CU14 and NET 4.7.2 no Premissions to Update ti New CU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/308189/exchange-16-with-cu14-and-net-4-7-2-no-premissions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI     

i wanted to Update one of my Servers with onPrem Exchnage to the new CU19. I ran into premission Problems when i try to update to a new CU     

This is My Server:     

SRV 16 with Exch. 16 and CU14     

NET 4.7.2     

I had to retsore the Server to get it running again ....     

What i tried so far:     

NET FW Update to 4.8 worked and the Exch. is still running after this.     

Upgrade directly to CU 19 doesn't work it fails  right after the the check for preinstall requirements     

Upgrade to CU 15 fails at step 5 after the file copy goes through     

The Logs Show these errors:     

```
[03.10.2021 10:27:33.0852] [1] Installing a new product. Package: G:\exchangeserver.msi. Property values: DISABLEERRORREPORTING=1 PRODUCTLANGUAGELCID=1033 DEFAULTLANGUAGENAME=ENU DEFAULTLANGUAGELCID=1033 INSTALLCOMMENT="Installierte Sprache für dieses Produkt: English (United States)" REINSTALLMODE=amus REBOOT=ReallySuppress TARGETDIR="C:\Program Files\Microsoft\Exchange Server\V15" ADDLOCAL=AdminTools,Bridgehead,ClientAccess,UnifiedMessaging,Mailbox,FrontendTransport,Cafe,AdminToolsNonGateway  
[03.10.2021 10:29:41.0997] [1] [ERROR] Installing product G:\exchangeserver.msi failed. Schwerwiegender Fehler bei der Installation. Error code is 1603. Last error reported by the MSI package is 'The installer has insufficient privileges to access this directory: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.1913.  The installation cannot continue.  Log on as administrator or contact your system administrator.'.  
[03.10.2021 10:29:41.0997] [1] [ERROR] Schwerwiegender Fehler bei der Installation  
[03.10.2021 10:29:42.0000] [1] [ERROR] Installing product G:\exchangeserver.msi failed. Schwerwiegender Fehler bei der Installation. Error code is 1603. Last error reported by the MSI package is 'The installer has insufficient privileges to access this directory: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.1913.  The installation cannot continue.  Log on as administrator or contact your system administrator.'.  
[03.10.2021 10:29:42.0000] [1] [ERROR] Schwerwiegender Fehler bei der Installation  
[03.10.2021 10:29:42.0019] [1] [ERROR] Installing product G:\exchangeserver.msi failed. Schwerwiegender Fehler bei der Installation. Error code is 1603. Last error reported by the MSI package is 'The installer has insufficient privileges to access this directory: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.1913.  The installation cannot continue.  Log on as administrator or contact your system administrator.'.  
[03.10.2021 10:29:42.0019] [1] [ERROR] Schwerwiegender Fehler bei der Installation
```

And this:     

```
=== Logging started: 10.03.2021  11:27:34 ===  
Error 1303. The installer has insufficient privileges to access this directory: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\15.1.1913.  The installation cannot continue.  Log on as administrator or contact your system administrator.
```

But.... i'm Admin .... i should be able to go through witrh that install ...    

I found this when i went to the folder this message is talking about:     

    

This is true for all of the folders under this path. There is only one User "Everyone" with the right to "read"...     

On a different Exchange i can see that there are more entries in that specific folder.     

So what am i supposed to do now ....     

I can not find much about this error and the few sources i've found tell me to reinstall and moove the exchage :/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

How is that even Possible ... on all my other exchanges the premissions are set correctly.  Is this maybe a sighn of intrusion; someone fiddled with the exchange ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Hi,    

What kind of admin do you mean?    

In my lab its permission looks like:    

    

And the account that I use when installing is the administrator of the domain. Is that same for you?    

Did you prepare schema/AD/domain before running the setup? Follow the doc here if you didn't: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

You can also try updating via powershell:    

```
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Upgrade [/DomainController:] [/EnableErrorReporting]
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
