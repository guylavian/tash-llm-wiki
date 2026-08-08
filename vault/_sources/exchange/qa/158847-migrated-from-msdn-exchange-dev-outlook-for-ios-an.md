---
title: "[Migrated from MSDN Exchange Dev]Outlook for iOS and Android Active Sync message size limitations."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158847/migrated-from-msdn-exchange-dev-outlook-for-ios-an
question_id: 158847
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Outlook for iOS and Android Active Sync message size limitations.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158847/migrated-from-msdn-exchange-dev-outlook-for-ios-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Outlook for iOS and Android Active Sync message size limitations.  

[Original post]  

The Outlook for iOS and Android app is not allowing attachments slightly over 10 MB. I believe it may be that if the Outlook for iOS and Android app does not connect directly to our on-premies Exchange servers, instead it seems to connect to a service hosted in Microsoft Cloud. Using the native iOS mail app, it connects directly to our on prem Exchange servers. The native iOS mail app and GMAIL app is able to send emails with attachments over 10 MB.  

These were the settings set for our ActiveSync on our on prem Exchange 2016 servers to 35 MB.  

```
%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-Server-ActiveSync/" -section:system.webServer/security/requestFiltering /requestLimits.maxAllowedContentLength:36700160

%windir%\system32\inetsrv\appcmd.exe set config "Default Web Site/Microsoft-Server-ActiveSync/" -section:system.web/httpRuntime /maxRequestLength:35000

%windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-ActiveSync/" -section:system.webServer/security/requestFiltering /requestLimits.maxAllowedContentLength:36700160

%windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-ActiveSync/" -section:system.web/httpRuntime /maxRequestLength:35000

%windir%\system32\inetsrv\appcmd.exe set config "Exchange Back End/Microsoft-Server-ActiveSync/" -section:appSettings /[key='MaxDocumentDataSize'].value:36700160
```

Any insight on this?  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

This is the error from the EAS http proxy log:  

```
2020-11-13T16:41:29.398Z,67ddb515-32b6-4020-a4ec-0665116b692d,15,1,1979,6,,Eas,xxx-serverxxx,/Microsoft-Server-ActiveSync/default.eas,,Basic,true,******,,Sid~S-1-5-21-3039674024-3586367722-4225467210-4300,Outlook-iOS-Android/1.0,52.96.16.37:49660,********,200,,ClientDisconnect,POST,Proxy,*********,15.01.1979.000,IntraForest,WindowsIdentity,,,,14796248,,,,0,0,,0,,0,,0,0,,0,585,0,479,1,103,,,,,0,1,585,0,,2,,3,585,,?Cmd=SmartForward&User=***%5C***&DeviceId=f6256279b5fc49a39037c025b7f895bc&DeviceType=Outlook,,BeginRequest=2020-11-13T16:41:28.813Z;CorrelationID=;ProxyState-Run=None;FEAuth=BEVersion-1942063035;RoutingEntry=DatabaseGuid:20053c46-d566-4ce2-b744-b937480194ff%4Server:***********T+1942063035@637408062379136327;BeginGetRequestStream=2020-11-13T16:41:28.815Z;OnRequestStreamReady=2020-11-13T16:41:28.815Z;ProxyState-Complete=ProxyRequestData;SharedCacheGuard=0;EndRequest=2020-11-13T16:41:29.398Z;,StreamProxy=StreamProxy-Request-ExpectReadCallback;HttpException=ClientDisconnect;,,|RoutingDB:20053c46-d566-4ce2-b744-b937480194ff,,,CafeV1
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

@KaelYao,  

We've tried multiple accounts on multiple different devices, all the same result with the Outlook for iOS and Android app. In addition, it would take hours to get a NDR from the Outlook instead of our on premises Exchange servers on the mobile phone, that's why I think the Outlook for iOS and Android App does not connect directly to our on-premises Exchange servers.  

Below is the NDR on the mobile device and the message headers of the original email.  

Original message details  

Created date: 11/8/2020 4:33:14 AM  

Sender address: xxxxxxxxxxx  

Recipient addresses: xxxxxxxxxxxxx  

Subject: 23:32  

Technical details  

MessageDeliveryFailedException: Could not deliver the message [len=70, data=00000000127228D3C9EAA949BFEC5FEBB957E45A070092857C233CCA064DA4A2473B41CA4EDA00000000010F000092857C233CCA064DA4A2473B41CA4EDA000000004B2F0000] sent at 11/8/2020 4:33:52 AM.  

Failure code: f5f0  

Message headers:  

```
From: "xxxxxxxxxxx" 
    To: "xxxxxxxxx" 
    Subject: 23:32
    Thread-Topic: 23:32
    Thread-Index: AQHWtYhFMMfuEa1LLU6K//NKoXp+Xw==
    X-MS-Exchange-MessageSentRepresentingType: 1
    Date: Sun, 8 Nov 2020 04:33:52 +0000
    Message-ID: 
    Content-Language: en-US
    X-MS-Has-Attach:
    X-MS-Exchange-Organization-SCL: -1
    X-MS-TNEF-Correlator:
    Content-Type: multipart/alternative;
                    boundary="_000_SN6PR17MB2640B2A16901656D268E8437F4EB0SN6PR17MB2640namp_"
    MIME-Version: 1.0
```
