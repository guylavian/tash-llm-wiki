---
title: "Exchange server 2016 Free/busy issue after Disabling TLS 1.0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142364/exchange-server-2016-free-busy-issue-after-disabli
question_id: 142364
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange server 2016 Free/busy issue after Disabling TLS 1.0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142364/exchange-server-2016-free-busy-issue-after-disabli (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,  

We have 3 exchange servers and we have recently disabled TLS 1.0.  

Since then the users in the same servers are able to lookup for free/busy but the users mounted on other exchange servers, free/busy does not work.

When we mount all the DBs in the same servers, we don't have any issues with the free/busy lookup.

We also get the event 4002 on both the servers when free/busy issues persists

Process 23020: ProxyWebRequest CrossSite from S-1-X-21-XXX8696XXXX-XXXXXXXXX-XXXXXXXXX-XXXX to https://server1.domain.com:444/EWS/Exchange.asmx failed. Caller SIDs: NetworkCredentials. The exception returned is Microsoft.Exchange.InfoWorker.Common.Availability.ProxyWebRequestProcessingException: Proxy web request failed. ---> System.Net.WebException: The underlying connection was closed: An unexpected error occurred on a send. ---> System.IO.IOException: Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host. ---> System.Net.Sockets.SocketException: An existing connection was forcibly closed by the remote host  

at System.Net.Sockets.Socket.EndReceive(IAsyncResult asyncResult)  

at System.Net.Sockets.NetworkStream.EndRead(IAsyncResult asyncResult)  

--- End of inner exception stack trace ---  

at System.Net.TlsStream.EndWrite(IAsyncResult asyncResult)  

at System.Net.ConnectStream.WriteHeadersCallback(IAsyncResult ar)  

--- End of inner exception stack trace ---  

at System.Web.Services.Protocols.WebClientAsyncResult.WaitForResponse()  

at System.Web.Services.Protocols.WebClientProtocol.EndSend(IAsyncResult asyncResult, Object& internalAsyncState, Stream& responseStream)  

at System.Web.Services.Protocols.SoapHttpClientProtocol.EndInvoke(IAsyncResult asyncResult)  

at Microsoft.Exchange.InfoWorker.Common.Availability.Proxy.Service.EndGetMailTips(IAsyncResult asyncResult)  

at Microsoft.Exchange.InfoWorker.Common.MailTips.MailTipsApplication.EndProxyWebRequest(ProxyWebRequest proxyWebRequest, QueryList queryList, IService service, IAsyncResult asyncResult)  

at Microsoft.Exchange.InfoWorker.Common.Availability.ProxyWebRequest.EndInvoke(IAsyncResult asyncResult)  

at Microsoft.Exchange.InfoWorker.Common.Availability.AsyncWebRequest.EndInvokeWithErrorHandling()  

--- End of inner exception stack trace ---  

. Name of the server where exception originated: Server1. LID: 43532. Make sure that the Active Directory site/forest that contain the user's mailbox has at least one local Exchange 2010 server running the Availability service. Turn up logging for the Availability service and test basic network connectivity.

Kindly advice to resolve the issue.

Cheers  

Priya

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

how do you disable the TLS? Event ID 4002 occurs, it maybe disabled by mistake i met the same issue, the free/busy doesn't work, how can i fix it?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-29*

@Priya Jayaraman       

Hi,Priya.    

From your post,I suppose that the three servers are all Exchange 2016 and added to a DAG.    

What CU are you running on the servers?    

To my knowledge,your problem may possibly occurs from the HTTPs proxy between Exchange servers is still using TLS1.0.    

Disabling it may cause the proxy to fail which affects EWS(responsible for free/busy information)    

You may need to upgrade to CU9 or later If you want to disable TLS1.0.    

For more information,here are some helpful articles from Exchange Team Blog:    

Exchange Server TLS guidance, part 1: Getting Ready for TLS 1.2    

Exchange Server TLS guidance Part 2: Enabling TLS 1.2 and Identifying Clients Not Using It    

Exchange Server TLS guidance Part 3: Turning Off TLS 1.0/1.1    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
