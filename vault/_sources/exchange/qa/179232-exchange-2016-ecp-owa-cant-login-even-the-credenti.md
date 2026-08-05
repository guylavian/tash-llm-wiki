---
title: "Exchange 2016 ECP & OWA Can't login even the credentials are fine"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/179232/exchange-2016-ecp-owa-cant-login-even-the-credenti
question_id: 179232
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange 2016 ECP & OWA Can't login even the credentials are fine

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/179232/exchange-2016-ecp-owa-cant-login-even-the-credenti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

After we applied CU18 then we can't login to OWA or ECP from one of the server. We are getting the login page and nothing happens after we put the credentials.  

But if we put the wrong credentials it says " The user name or password you entered isn't correct"  

Nothing happen if we put the correct credentials.  

Thanks  

smi

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-30*

@SMI   

How much Exchange servers do you have?
Do you mean you can login from other Exchange servers? 
Which version of Exchange 2016 do you upgrade from?
Do you set the same URL for OWA&ECP virtual directory? You can use the following command to check. When you post the screenshot of the output, please don't forget to replace your domain name or other personal information:

```
Get-OwaVirtualDirectory|fl Id,InternalUrl,ExternalUrl
Get-EcpVirtualDirectory|fl Id,InternalUrl,ExternalUrl
```

Here are some suggestions for you.

-   Microsoft .NET Framework 4.8 and Visual C++ Redistributable Packages for Visual Studio 2013 are required for Exchange 2016 cu18. Please make sure they are installed successfully. For your reference: Cumulative Update 18 for Exchange Server 2016.

-   Check and make sure all needed services are running well after restarting the computer.

-   Recycle MSExchangeECPAppPool and MSExchangeOWAAppPool in Application Pools from IIS Manager. Application Pools > MSExchangeECPAppPool/MSExchangeOWAAppPool> Recycle.

-   Please also try to restart IIS:    iisreset /noforce

If the response is helpful, please click "Accept Answer" and upvote it.
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
