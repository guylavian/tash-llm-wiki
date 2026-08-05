---
title: "Exchange2019 relay recive connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193037/exchange2019-relay-recive-connector
question_id: 1193037
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange2019 relay recive connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193037/exchange2019-relay-recive-connector (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

Installed Exchange2019 server, but can't work sending e-mail to internet mail

Have 

-  ADDC server dc01.local-domain.local 192.168.4.101

-  Exchange server exchange.local-domain.local 192.168.4.17

-  Domain name company.com, as a web site and for mailing like ******@company.com

What i did

In DNS: 

-  added mx 10 mail.company.com.

-  added A mail=router IP

-  TXT for spf

In Exchange

-  mail-flow>accepted domains
   added domain company.com (type authoritative, default)

-  standard send connector (domain=*)

-  address policy: smtp:******@company.com and aslis:local-domain.local

-  like in https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/allow-anonymous-relay?view=exchserver-2019  

   New-ReceiveConnector -Name "Anonymous Relay" -TransportRole FrontendTransport -Custom -Bindings 0.0.0.0:25 -RemoteIpRanges 192.168.4.17,127.0.0.1  

   Set-ReceiveConnector "Anonymous Relay" -PermissionGroups AnonymousUsers  

   Get-ReceiveConnector "Anonymous Relay" | Add-ADPermission -User "NT AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"

In Router

-  port forwarding 25,80,110,143,443,465,587,717,993,995 to 192.168.4.17

In this case I can 

-  send and receive mail from internal mail (test******@company.com can send and receive mail from ******@company.com)

-  receive mail from internet mail (like ******@gmail.com)

-  when I send mail from test******@company.com to ******@gmail.com I have a error  

-  EXCHANGE.local-domain.local rejected your message to the following email addresses:  

   @gmail.com (@gmail.com)  

   Your message couldn't be sent because the mail server is not ready to accept your message.  

   EXCHANGE.local-domain.local gave this error:  

   SMTP; Unable to relay recipient in non-accepted domain  

   Diagnostic information for administrators:  

   Generating server: EXCHANGE.local-domain.local  

   @gmail.com  

   EXCHANGE.local-domain.local  

   Remote Server returned '550 5.7.54 SMTP; Unable to relay recipient in non-accepted domain'  

   Original message headers:  

   Received: from EXCHANGE.local-domain.local (192.168.4.17) by EXCHANGE.local-domain.local  

   (192.168.4.17) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.2.1118.7; Sat, 25 Mar 2023 08:23:47 +0500  

   Received: from EXCHANGE.local-domain.local ([::1]) by EXCHANGE.local-domain.local ([::1]) with mapi id 15.02.1118.007; Sat, 25 Mar 2023 08:23:47 +0500  

   From: testmail test@company.com  

   To: "******@gmail.com" ******@gmail.com  

   Subject: 112333  

   Thread-Topic: 112333  

   Thread-Index: AdleySt3XEmRGDcnQZK9O85ATlHlHg==  

   Date: Sat, 25 Mar 2023 03:23:46 +0000  

   Message-ID: ******@company.com  

   Accept-Language: en-US, ru-RU  

   Content-Language: ru-RU  

   X-MS-Has-Attach:  

   X-MS-TNEF-Correlator:  

   x-originating-ip: [192.168.4.253]  

   Content-Type: multipart/alternative;  

   boundary="000_11f0292549774ef4a6935728a6fbe338companycom"  

   MIME-Version: 1.0

Tests  

exchange managment shell  

Get-ReceiveConnector "Anonymous Relay" | Format-List Enabled,TransportRole,Bindings,RemoteIPRanges  

Enabled : True  

TransportRole : FrontendTransport  

Bindings : {0.0.0.0:25}  

RemoteIPRanges : {127.0.0.1, 192.168.4.17} 

Get-ADPermission "Anonymous Relay" -User "NT AUTHORITY\ANONYMOUS LOGON" | where {($.Deny -eq $false) -and ($.IsInherited -eq $false)} | Format-Table User,ExtendedRights  

User ExtendedRights  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Any-Sender}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Any-Recipient}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-Accept-Headers-Routing}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Submit}  

NT AUTHORITY\ANONYMOUS LOGON {ms-Exch-SMTP-Accept-Authoritative-Domain-Sender}  

   Telnet  

   open 192.168.4.17 25  

   220 EXCHANGE.local-domain.local Microsoft ESMTP MAIL Service ready at Sat, 25 Mar 2023 08:35:43 +0500  

   ehlo  

   250-EXCHANGE.local-domain.local Hello [192.168.4.17]  

   250-SIZE 37748736  

   250-PIPELINING  

   250-DSN  

   250-ENHANCEDSTATUSCODES  

   250-STARTTLS  

   250-8BITMIME  

   250-BINARYMIME  

   250-CHUNKING  

   250 SMTPUTF8  

   mail from:test******@company.com  

   250 2.1.0 Sender OK  

   rcpt to:******@gmail.com  

   250 2.1.5 Recipient OK  

   data  

   354 Start mail input; end with .  

   subject:test  

   message  

   .  

   250 2.6.0 9b98be1d-b712-437c-9265-9bd13869f9ff@EXCHANGE.local-domain.local [InternalId=4032974290969, Hostname=EXCHANGE.local-domain.local] 1563 bytes in 2.970, 0,514 KB/sec Queued mail for delivery  

   quit

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-28*

Hi @Aleksandr Kandalov  ,

From the RemoteIPRanges : {127.0.0.1, 192.168.4.17} part, it seems you only have your Exchange server’s ip addresses added to the Remote Address Settings.

Please note that if you would like network hosts to use this anonymous relay receive connector to relay messages to internet, you may need to add the hosts’ ip addresses to this connector.

As mentioned in the documentation:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-03-25*

Hello @Aleksandr Kandalov  

If you read the Docs we need a Send Connector 

Do you have a Send connector created ?

New-SendConnector -Name <Name> -AddressSpaces * -Internet [-SourceTransportServer <fqdn1>,<fqdn2>...]

I can see you have a mention there , just making sure cause you mention Domain it is not Domain it is generally *

make sure traffic is not Proxied from your Router also and remove any Packet Inspectin

Can you provide the Send and Receive connectors please ?

In case this answer helped kindly mark it as Accepted !

I will keep am eye in case you have more info !

Have a nice day !
