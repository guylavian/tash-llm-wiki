---
title: "server 2016 exchange 2016 cu20 setup fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361545/server-2016-exchange-2016-cu20-setup-fails
question_id: 361545
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# server 2016 exchange 2016 cu20 setup fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361545/server-2016-exchange-2016-cu20-setup-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft Exchange Server 2016 Cumulative Update 20 Unattended Setup  

Languages  

Management tools  

Mailbox role: Transport service  

Mailbox role: Client Access service  

Mailbox role: Unified Messaging service  

Mailbox role: Mailbox service  

Mailbox role: Front End Transport service  

Mailbox role: Client Access Front End service  

Performing Microsoft Exchange Server Prerequisite Check  

```
Configuring Prerequisites                                                                         COMPLETED
Prerequisite Analysis                                                                             COMPLETED
```

Configuring Microsoft Exchange Server  

```
Language Files                                                                                    COMPLETED
Restoring Services                                                                                COMPLETED
```

An unexpected error has occurred and a Watson dump is being generated: Access to the path 'C:\Program  

Files\Microsoft\Exchange Server\V15\Bin\perf\amd64\dscperf.ini.tmp' is denied.  

Using ExchangeServer2016-x64-CU20.ISO to update CU19.  

Note the file dscperf.ini.tmp is not present in the specified directory.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-04-27*

Is exchange's non-support of essential server a recent occurrence? I don't recall seeing this before.  

I ran SBS 2003 for about 13 years if only because SBS 2008 and 2012 weren't viable from my point of view. I think I started server 2016 at exchange cu15 or so and until this recent mess with everyone around the world hacking exchange, the combination has worked pretty well for me... a very small business as it were.  

art

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-27*

I'm working with Windows Essentials 2016.  In the past 6 days I did a new install of both the server and exchange cu20 that completed without error but CU20 is not yet in usable condition. I noticed that CU20 installed more domain user accounts than Essentials "allows" (25). I can get owa and ecp working but I relied on PowerShell script to specify various parameters like FQDNs for various services, DNS and SSL certs. A telnet test to each of ports 25, 110, 143, 587, 993 and 995 completes a connection to each port.  Tommorow I'll have some time to review why I can't send/receive e-mail.  

I did have a non-exchange issue when I switched the default RDP port, but the server's approach to locking down firewall rules got in my way. I did find an appropriate PS script to configure the port/firewall I want to use.  

One observation is that it's a challenge to identify the necessary PS exchange modules that are needed. Much of Microsoft's own content doesn't identify these modules. The article above that you reference does include the necessary power shell modules.  

I have downloaded an evaluation copy of Essentials 2019 but haven't had the time to work on it along while some very messy 20H2 updates added to my workload.  

thanks,  

art

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-21*

Are you installing Exchange on Windows Essentials?    

Thats not supported    

https://learn.microsoft.com/en-us/windows-server-essentials/manage/integrate-an-on-premises-exchange-server-with-windows-server-essentials

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-21*

Log Name: Application  

Source: MSExchangeTransportDelivery  

Date: 4/21/2021 12:22:38 PM  

Event ID: 10005  

Task Category: PoisonMessage  

Level: Error  

Keywords: Classic  

User: N/A  

Computer: gershwin.PARROTBYTE.local  

Description:  

The transport process couldn't load poison message information from the registry. Access to the registry failed with the following error: Access to the registry key 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\Transport\PoisonMessage\InternetMessageIds' is denied.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

<System>  

<Provider Name="MSExchangeTransportDelivery" />  

<EventID Qualifiers="49156">10005</EventID>  

<Level>2</Level>  

<Task>10</Task>  

<Keywords>0x80000000000000</Keywords>  

<TimeCreated SystemTime="2021-04-21T19:22:38.739886100Z" />  

<EventRecordID>1457445</EventRecordID>  

<Channel>Application</Channel>  

<Computer>gershwin.PARROTBYTE.local</Computer>  

<Security />  

</System>  

<EventData>  

<Data>Access to the registry key 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\Transport\PoisonMessage\InternetMessageIds' is denied.</Data>  

</EventData>  

</Event>

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-19*

Hi @Art Lazanoff       

Do you currently have some antivirus software running on this server?     

If there are any, please disable them and check if you are able to upgrade successfully.    

If you are using the Setup wizard to update, you may also try the unattended mode.    

Please locate the path of the setup.exe file and run the following command via powershell:    

```
Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Upgrade
```

Check if the problem persists.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
