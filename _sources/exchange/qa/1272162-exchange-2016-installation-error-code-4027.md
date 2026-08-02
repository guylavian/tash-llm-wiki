---
title: "Exchange 2016 Installation-- Error Code 4027"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1272162/exchange-2016-installation-error-code-4027
question_id: 1272162
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Installation-- Error Code 4027

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1272162/exchange-2016-installation-error-code-4027 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am attempting to install Exchange 2016 on a Windows Server 2016 (new install). This is NOT in a VM. The purpose is to upgrade to 2019 from 2010.  

I am getting the following error:

```
Log Name:      Application

Source:        MSExchange ADAccess

Date:          4/30/2023 7:24:28 PM

Event ID:      4027

Task Category: General

Level:         Error

Keywords:      Classic

User:          N/A

Computer:      ex.mydomain.com

Description:

Process ExSetupUI.exe (PID=5264). WCF request (Get Servers for mydomain.com) to the Microsoft Exchange Active Directory Topology service on server (TopologyClientTcpEndpoint (localhost)) failed. Make sure that the service is running. In addition, make sure that the network ports that are used by Microsoft Exchange Active Directory Topology service are not blocked by a firewall. The WCF call was retried 3 time(s). Error Details 

 System.ServiceModel.EndpointNotFoundException: Could not connect to net.tcp://localhost:890/Microsoft.Exchange.Directory.TopologyService. The connection attempt lasted for a time span of 00:00:02.0468804. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:890.  ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:890

   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

   at System.Net.Sockets.Socket.Connect(EndPoint remoteEP)

   at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   --- End of inner exception stack trace ---

Server stack trace: 

   at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   at System.ServiceModel.Channels.BufferedConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   at System.ServiceModel.Channels.ConnectionPoolHelper.EstablishConnection(TimeSpan timeout)

   at System.ServiceModel.Channels.ClientFramingDuplexSessionChannel.OnOpen(TimeSpan timeout)

   at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)

   at System.ServiceModel.Channels.ServiceChannel.OnOpen(TimeSpan timeout)

   at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)

Exception rethrown at [0]: 

   at System.Runtime.Remoting.Proxies.RealProxy.HandleReturnMessage(IMessage reqMsg, IMessage retMsg)

   at System.Runtime.Remoting.Proxies.RealProxy.PrivateInvoke(MessageData& msgData, Int32 type)

   at System.ServiceModel.ICommunicationObject.Open()

   at Microsoft.Exchange.Net.ServiceProxyPool`1.GetClient(Int32 retry, Boolean& doNotReturnProxyAfterRetry, Boolean useCache)

   at Microsoft.Exchange.Net.ServiceProxyPool`1.TryCallServiceWithRetry(Action`1 action, String debugMessage, WCFConnectionStateTuple proxyToUse, Int32 numberOfRetries, Boolean doNotReturnProxyOnSuccess, Exception& exception)

Event Xml:

  

    

    4027

    2

    1

    0x80000000000000

    

    3109

    Application

    ex.mydomain.com

    

  

  

    ExSetupUI.exe

    5264

    Get Servers for mydomain.com

    TopologyClientTcpEndpoint (localhost)

    3

    System.ServiceModel.EndpointNotFoundException: Could not connect to net.tcp://localhost:890/Microsoft.Exchange.Directory.TopologyService. The connection attempt lasted for a time span of 00:00:02.0468804. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:890.  ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:890

   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

   at System.Net.Sockets.Socket.Connect(EndPoint remoteEP)

   at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   --- End of inner exception stack trace ---

Server stack trace: 

   at System.ServiceModel.Channels.SocketConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   at System.ServiceModel.Channels.BufferedConnectionInitiator.Connect(Uri uri, TimeSpan timeout)

   at System.ServiceModel.Channels.ConnectionPoolHelper.EstablishConnection(TimeSpan timeout)

   at System.ServiceModel.Channels.ClientFramingDuplexSessionChannel.OnOpen(TimeSpan timeout)

   at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)

   at System.ServiceModel.Channels.ServiceChannel.OnOpen(TimeSpan timeout)

   at System.ServiceModel.Channels.CommunicationObject.Open(TimeSpan timeout)

Exception rethrown at [0]: 

   at System.Runtime.Remoting.Proxies.RealProxy.HandleReturnMessage(IMessage reqMsg, IMessage retMsg)

   at System.Runtime.Remoting.Proxies.RealProxy.PrivateInvoke(MessageData& msgData, Int32 type)

   at System.ServiceModel.ICommunicationObject.Open()

   at Microsoft.Exchange.Net.ServiceProxyPool`1.GetClient(Int32 retry, Boolean& doNotReturnProxyAfterRetry, Boolean useCache)

   at Microsoft.Exchange.Net.ServiceProxyPool`1.TryCallServiceWithRetry(Action`1 action, String debugMessage, WCFConnectionStateTuple proxyToUse, Int32 numberOfRetries, Boolean doNotReturnProxyOnSuccess, Exception& exception)

  

```

-  I have inbound and outbound rules for port 890 in the firewall (Windows) on the new and old exchange servers, as well as on both domain controllers.

-  IPv6 is enabled on all servers

-  When I ping the domain from the Exchange server to be I get a response using both IPv4 and IPv6. Both DC's are also pingable as is the new Exchange server

-  Net.TCP Port Sharing is set to automatic and started on all servers

-  DNS has been flushed on new Exchange server.

-  All dcdiag test pass including DNS

Once Exchange 2016 is up and running correctly, the 2010 will be removed before upgrading 2016. Once 2019 is up and running correctly 2016 will be removed.

I just remove two 2008 DC's. All reference to these two servers have been removed. Both were removed by running dcpromo. Once both 2008 DCs were remove scheme was updated/upgraded to 2016.  

Anybody have any ideas?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-09*

Hi @ Kevin，

Based on the installation error you provided, it appears that there is an attempt to find a mailbox database that does not exist.

For further troubleshooting, I recommend that you run the following command in EMS to check whether there is a system mailbox without an associated database:

```
Get-Mailbox –Arbitration | ft Name, ServerName, Database –Auto
```

If it exists, please open Active Directory Users and Computers, locate the user, and remove it.

For more information about this error, please refer to this link:Error Solved: "Exchange 2016 database is mandatory on usermailbox" - TechNet Articles - United States (English) - TechNet Wiki (microsoft.com)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-02*

Check this thread for more insight - https://learn.microsoft.com/en-us/answers/questions/367794/error-during-exchange-2019-installation-(id-1002-4

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-01*

Hi @ Kevin,

In order to better identify the issue, I would like to confirm the following points with you:

1.       Do both old and new servers have this error?

2.       Are there other related errors in Event Viewer?

3.       Are all ports open between DC and Exchange?

 

In addition, for testing purposes, I recommend that you could temporarily disable the firewall to see if you can successfully install Exchange 2016.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
