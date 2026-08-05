---
title: "Exchange 500 Error only on Receive Connectors Page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/157776/exchange-500-error-only-on-receive-connectors-page
question_id: 157776
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 500 Error only on Receive Connectors Page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/157776/exchange-500-error-only-on-receive-connectors-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

i have the Problem that i get an 500 Unexpected Error only if i try to open "Receive Connectors" Page in ECP.    

See attached Screenshot.    

By the way. Its a fresh install.    

Anyone knows how to solve that?

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-11*

So after a complete AD Clean and Reinstallation of Server 2019 and Exchange it's working.  

Thanks for help anyway!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Thanks for the Answer.  

Nothing helps again.  

i will setup the whole Server again and give feedback after that.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-11*

Hi @Bastian KB IT  ,    

Have you noticed any error events in the Application logs which could be related to this issue?    

Are you able to access the Receive Connector page via https://localhost/ecp on the server?    

Please have a go by recreating the ecp virtual directory and see the results.    

-  In EMS, please run the following command:     

```
Remove-EcpVirtualDirectory -Identity   
New-EcpVirtualDirectory -Server  -ExternalURL  -InternalURL 
```

-  Restart IIS by running iisreset /noforce from a command prompt window and check the result.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

Hello and Thank You for your Answer.

-    Version: Exchange Server 2019 CU6

-    Same Problem in Browsers Chrome and Firefox

-    With an other (fresh) Admin Account it's also not working

-    all other Points are working as expected

Output from Get-ReceiveConnector:

[PS] C:\Windows\system32>Get-ReceiveConnector

>

Identity Bindings Enabled  

EXCHANGE-SRV01\Default EXCHANGE-SRV01 {0.0.0.0:2525, [::]:2525} True  

EXCHANGE-SRV01\Client Proxy EXCHANGE-SRV01 {[::]:465, 0.0.0.0:465} True  

EXCHANGE-SRV01\Default Frontend EXCHANGE-SRV01 {[::]:25, 0.0.0.0:25} True  

EXCHANGE-SRV01\Outbound Proxy Frontend EXCHANGE-SRV01 {[::]:717, 0.0.0.0:717} True  

EXCHANGE-SRV01\Client Frontend EXCHANGE-SRV01 {[::]:587, 0.0.0.0:587} True

-    i also recycled the MSExchangeECPAppPool in IIS and restarted the Server

-    after execution of UpdateCas.ps1 and UpdateConfigFiles.ps1 nothing changed

Any other suggestions?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-10*

Hi,  

Please find below my suggestions,  

What is the version of the Exchange Server?  

Have you tried in different browsers?  

Have you tried with different admin accounts?  

All other ECP options are working fine?  

What is the result when you run Get-ReceiveConnector in EMS?  

Have you tried recycling MSExchangeECPAppPool App pool?   

If all other options in ECP is working fine, then it could be an issue with the corruption or permissions on one of the receive connector. If some of other options also has an problem in ECP, then try running UpdateCas.ps1 and UpdateConfigFiles.ps1 from the exchange bin directory.  

https://social.technet.microsoft.com/Forums/en-US/f5842201-c59b-4e5d-9956-d031e846c817/500-unexpected-error-when-accessing-receive-connectors-link-in-ecp?forum=Exch2016Adm  

If the above suggestion helps, please click on "Accept Answer" and upvote it.
