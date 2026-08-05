---
title: "WServer 2012 R2 and Exchange 2013 - Schannel error 36888 Error 70 State 105 after setting .NET 4.x reg key \"SystemDefaultTlsVersions\" to 1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/360373/wserver-2012-r2-and-exchange-2013-schannel-error-3
question_id: 360373
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# WServer 2012 R2 and Exchange 2013 - Schannel error 36888 Error 70 State 105 after setting .NET 4.x reg key "SystemDefaultTlsVersions" to 1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/360373/wserver-2012-r2-and-exchange-2013-schannel-error-3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a fresh install of Exchange 2013 deployed in coexistence with Exchange 2010. The first is on a Windows server 2012 R2, the second is on a Windows server 2008 R2.   

I do not have any issues at the moment on my Exchenge servers, nor from client side, but I would like to understand if I can figure out why I get so many errors from Schannel after setting the key reported in the subject.  

The only change I made was to apply reg entries specified at https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761. To be more specific I added these keys:  

```
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
"DisabledByDefault"=dword:00000000
"Enabled"=dword:00000001
```

and this key:  

```
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
"SystemDefaultTlsVersions"=dword:00000001
[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319]
"SystemDefaultTlsVersions"=dword:00000001
```

I firstly applied the Schanel keys and rebooted the server. EventLog was clean. Then I applied the .NET Framework key and rebooted: EventLog started to fill with plenty of this error:  

```
Log Name:       System
Source:            Schannel
Date:               16/04/2021 12:36:19
Event ID:         36888
Task Category: None
Level:               Error
Keywords:      
User:               SYSTEM
Computer:       ********

Description:
A fatal alert was generated and sent to the remote endpoint. This may result in termination of the connection. The TLS protocol defined fatal error code is 70. The Windows SChannel error state is 105.

Event Xml:

  
    
    36888
    0
    2
    0
    0
    0x8000000000000000
    
    219151
    
    
    System
    **********
    
  
  
    70
    105
  

```

Temporarily, I turned off Schannel logging, since I don't have any issues, but I'd like to understand what's going on under the hood.   

Can you help me?  

Thank you,  

Francesco B. B.  

======================================  

EDIT  

By diving a bit more in the EventLog on my Exchange 2013, I found issues related to the MSExchange FrontEnd HTTP Proxy.  

TLS connections (rpc http proxy requests) to Exchange 2010 CAS (https://<CAS2010_name>/rpc/rpcproxy.dll) fail when enabling the .NET Framework reg key above. The event details:  

```
Log Name:      Application
Source:        MSExchange Front End HTTP Proxy
Date:          16/04/2021 13:26:19
Event ID:      3005
Task Category: Core
Level:         Warning
Keywords:      Classic
User:          N/A
Computer:      ******************

Description:
[RpcHttp] Marking ClientAccess 2010 server ****************** (https:///rpc/rpcproxy.dll) as unhealthy due to exception: System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.
   at System.Net.HttpWebRequest.GetResponse()
   at Microsoft.Exchange.HttpProxy.ProtocolPingStrategyBase.Ping(Uri url)

Event Xml:

  
    
    3005
    3
    1
    0x80000000000000
    
    903722
    Application
    ***************
    
  
  
    RpcHttp
    ********************
    https://******************/rpc/rpcproxy.dll
    System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.
   at System.Net.HttpWebRequest.GetResponse()
   at Microsoft.Exchange.HttpProxy.ProtocolPingStrategyBase.Ping(Uri url)
  

```

My guess is that by setting that key, now .NET on my WServer2012R2 with Exchange 2013 tries to connect to the CAS2010 with TLS1.2, but this protocol version is not enabled on my WServer2008R2/Exchange 2010.  

I tried to open the link in IE from my WServer2012R2/Exchange2013 and by looking at the page properties it shows that is using TLS1.0 protocol version (TLS 1.0, AES with 256 bit encryption (High); ECDH_P384 with 256 bit exchange).   

I reverted the registry change (just the one related to .NET 4.x to use system defaults for TLS connections), rebooted the server and I have no more entries related to MSExchange FrontEnd HTTP Proxy.  

I suppose, at this point, that the next step is to enable TLS1.2 also on WServer2008R2/Exchange2010, am I right? Maybe it's not enabled, I guess.  

Let me know.   

Thank you.  

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

@Andy David - MVP   , I thought that by adding the registry keys listed in my first post, simply I'm telling my server (and clients) to use TLS1.2 in an "opportunistic way". That is, TLS 1.2 is available for use, but also lower versions are still negotiable. I have not disabled lower TLS protocol versions yet. I'm basing my thoughts on this MS blog series: https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761.     

And, to be honest and to give you a comprehensive view, I set the .NET 4.x key to use TLS1.2 because of this MSExchangeApplicationLogic warning event, since the Microsoft store is only reachable by using TLS 1.2:    

```
Log Name:      Application  
Source:        MSExchangeApplicationLogic  
Date:          15/04/2021 12:11:18  
Event ID:      3042  
Task Category: Extension  
Level:         Warning  
Keywords:      Classic  
User:          N/A  
Computer:      ****************  
  
Description:  
Scenario: GetConfig. CorrelationId: b1994b58-53f2-420f-8f02-46d08bb33ac7. The url from the Config response contains no tokens. Url: https://o15.officeredir.microsoft.com/r/rlidMktplcWSConfig15?CV=15.0.1497.12&Client=WAC_Outlook&corr=b1994b58-53f2-420f-8f02-46d08bb33ac7 Element:  
  https://api.addins.omex.office.net/appinfo/query  

```

But, honestly, if these TLS settings break more important stuff (and RPC proxy calls are definitely more important stuff than the store apps), I leave it as is now and I will think to TLS 1.2 when Exchange 2010 will be removed from my environment...    

Thank you,    

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

@Andy David - MVP   , thank you but I think I found the culprit and actually there are issues, as opposite to my initial thoughts.    

By diving a bit more in the EventLog on my Exchange 2013, I found issues related to the MSExchange FrontEnd HTTP Proxy.    

TLS connections (rpc http proxy requests) to Exchange 2010 CAS (https://<CAS2010_name>/rpc/rpcproxy.dll) fail when enabling the .NET Framework reg key above. The event details:    

```
Log Name:      Application  
Source:        MSExchange Front End HTTP Proxy  
Date:          16/04/2021 13:26:19  
Event ID:      3005  
Task Category: Core  
Level:         Warning  
Keywords:      Classic  
User:          N/A  
Computer:      ******************  
  
Description:  
[RpcHttp] Marking ClientAccess 2010 server ****************** (https:///rpc/rpcproxy.dll) as unhealthy due to exception: System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.  
   at System.Net.HttpWebRequest.GetResponse()  
   at Microsoft.Exchange.HttpProxy.ProtocolPingStrategyBase.Ping(Uri url)  
  
Event Xml:  
  
    
      
    3005  
    3  
    1  
    0x80000000000000  
      
    903722  
    Application  
    ***************  
      
    
    
    RpcHttp  
    ********************  
    https://******************/rpc/rpcproxy.dll  
    System.Net.WebException: The request was aborted: Could not create SSL/TLS secure channel.  
   at System.Net.HttpWebRequest.GetResponse()  
   at Microsoft.Exchange.HttpProxy.ProtocolPingStrategyBase.Ping(Uri url)  
    

```

My guess is that by setting that key, now .NET on my WServer2012R2 with Exchange 2013 tries to connect to the CAS2010 with TLS1.2, but this protocol version is not enabled on my WServer2008R2/Exchange 2010.    

I tried to open the link in IE from my WServer2012R2/Exchange2013 and by looking at the page properties it shows that is using TLS1.0 protocol version (TLS 1.0, AES with 256 bit encryption (High); ECDH_P384 with 256 bit exchange).     

I reverted the registry change (just the one related to .NET 4.x to use system defaults for TLS connections), rebooted the server and I have no more entries related to MSExchange FrontEnd HTTP Proxy.    

I suppose, at this point, that the next step is to enable TLS1.2 also on WServer2008R2/Exchange2010, am I right? Maybe it's not enabled, I guess.    

Let me know.     

Thank you.    

Francesco B. B.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-16*

You probably have a TLS 1.0 or 1.1 client attempting to access Exchange.    

If you arent seeing any issues, then I wouldnt reverse any change.     

https://learn.microsoft.com/en-us/windows/win32/secauthn/schannel-error-codes-for-tls-and-ssl-alerts    

70 = TLS1_ALERT_PROTOCOL_VERSION
