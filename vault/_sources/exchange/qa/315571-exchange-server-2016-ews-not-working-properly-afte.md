---
title: "[Exchange Server 2016\\ EWS not working properly after CU Update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315571/exchange-server-2016-ews-not-working-properly-afte
question_id: 315571
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# [Exchange Server 2016\ EWS not working properly after CU Update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315571/exchange-server-2016-ews-not-working-properly-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys, I need some help. I updated my Exchange Serves 2016 (Dag), everything working without EWS. I tried before recreate EWS Virtual Directories, but after removing both directories i had possibility to add only one EWS Directory. When I added to other server i got communicate: ![77991-exchange1.jpg][1] SMTP and ActiveSync working properly but when i had failed test in microsoft activity with EWS and RCP: EWS ![77937-exchange2.jpg][2] RCP: ![77897-exchange3.jpg][3] And my checks from Powershells ![77955-exchange4.jpg][4] ![78001-exchange5.jpg][5] When i'm entrying to EWS URL im getting request for WIndows Auth and i can see that: URL with internl server is avaible too. ![78002-exchange6.jpg][6] Organization Config: EwsAllowEntourage : EwsAllowList : {Outlook-Android/, Outlook-iOS/} EwsAllowMacOutlook : EwsAllowOutlook : EwsApplicationAccessPolicy : EnforceAllowList EwsBlockList : EwsEnabled : True CAS Config: EwsEnabled : True EwsAllowOutlook : EwsAllowMacOutlook : EwsAllowEntourage : EwsApplicationAccessPolicy : EwsAllowList : EwsBlockList : After use Get-ClientAccessServer and Test Outlook Webservices Source ServiceEndpoint Scenario Result Latency (MS) ------ --------------- -------- ------ ------- DEIMOS.pak.local sun.pak.local Autodiscover: Outlook Provider Failure 5 DEIMOS.pak.local sun.pak.local Exchange Web Services Failure 24 DEIMOS.pak.local Availability Service Skipped 0 DEIMOS.pak.local sun.pak.local Offline Address Book Failure 6 DEIMOS.pak.local deimos.pak.local Autodiscover: Outlook Provider Failure 4 DEIMOS.pak.local deimos.pak.local Exchange Web Services Failure 23 DEIMOS.pak.local Availability Service Skipped 0 DEIMOS.pak.local deimos.pak.local Offline Address Book Failure 4 When i used just Test-Outlookwebservices i got "Unable to to find the client access monitoring user". Windows Firewall is disabled. I have Eset Email Security but i checked with turned off. Next check. Get-WebServicesVirtualDirectory | fl Identity,auth Identity : DEIMOS\EWS (Default Web Site) CertificateAuthentication : InternalAuthenticationMethods : {Ntlm, WindowsIntegrated, WSSecurity, OAuth} ExternalAuthenticationMethods : {Ntlm, WindowsIntegrated, WSSecurity, OAuth} LiveIdNegotiateAuthentication : WSSecurityAuthentication : True LiveIdBasicAuthentication : False BasicAuthentication : False DigestAuthentication : False WindowsAuthentication : True OAuthAuthentication : True AdfsAuthentication : False Any ideas for resolution ? I can not add new outlook clients desktop, and i had disconnected Macs with outlook after updated CU. [1]: /api/attachments/77991-exchange1.jpg?platform=QnA [2]: /api/attachments/77937-exchange2.jpg?platform=QnA [3]: /api/attachments/77897-exchange3.jpg?platform=QnA [4]: /api/attachments/77955-exchange4.jpg?platform=QnA [5]: /api/attachments/78001-exchange5.jpg?platform=QnA [6]: /api/attachments/78002-exchange6.jpg?platform=QnA Please help me, any ideas ? Whats is wrong ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Any help ideas ?  

Shared calendar in outlook clients doesnt work. I OWA is working properly.The same situation with searching messages in outlook destkop.  

Update  

Resolution:  

Rebuilidng OWA on other server - any effects  

After rebulidng  

https://github.com/MicrosoftDocs/OfficeDocs-Support/blob/public/Exchange/ExchangeServer/administration/403-forbidden-view-free-busy-information.md

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Looks good...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Seem like Outlook Servcies dont have access to Address book etc.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-16*

Hi @Windykacja   ,    

Do you mean you tried to create EWS Virtual Directory on both servers and failed?    

Please remove them first and then retry creating.     

```
Remove-WebServicesVirtualDirectory -Identity Server\"EWS (Default Web Site)"  
New-WebServicesVirtualDirectory -ServerName -InternalURL Https://Server.Domain.com/EWS/Exchange.asmx
```

Replace the Server & Domain to your Exchange Server names and Domain names.    

The 2nd picture shows the 403 Forbidden error of EWS, please check the Auth method of EWS, by default it's     

    

For the 4th picture you provided, it seems that the certificate bindings of Autodiscover and ActiveSync has problems.    

And the Test-OutlookWebServices errors, you could use the Test-OutlookWebServices | FL to find the error messages.    

When i used just Test-Outlookwebservices i got "Unable to to find the client access monitoring user".    

You can do this:    

-  Open PowerShell in Admin mode.    

-  CD 'C:\Program Files\Microsoft\Exchange Server\V15\Scripts'    

-  .\new-TestCasConnectivityUser.ps1    

-  Type a Password.    

-  Test-OutlookWebServices | FL    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
