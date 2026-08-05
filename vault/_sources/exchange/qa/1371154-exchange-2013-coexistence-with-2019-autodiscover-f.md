---
title: "Exchange 2013 coexistence with 2019, autodiscover from external not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371154/exchange-2013-coexistence-with-2019-autodiscover-f
question_id: 1371154
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 coexistence with 2019, autodiscover from external not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371154/exchange-2013-coexistence-with-2019-autodiscover-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have an environment with Exchange 2013 coexistence with 2019 hybrid, oauth enabled. There are F5 load balancers and firewall in between Internet and Exchange servers.

When we tested internal network, Outlook 2019 works fine. all OK.

We we tested external network, Outlook with IOS/Andriod also works fine, no issue was found now.

However, when we wanna double confirm oAuth, we got errors when running command "Test-oAuthConnectivity" and using "Microsoft Remote Connectivity Analyzer".

Please kindly advise whats going on? which part could cause this issue? Thanks.

Error:

Testing Outlook Mobile Hybrid Modern Authentication (HMA) for SMTP email address: ******@contos.com.

Testing Outlook Mobile Hybrid Modern Authentication (HMA) failed.

Additional DetailsElapsed Time: 8990 ms.

Test StepsSending an Autodiscover request to the on-premises Exchange Autodiscover service:  on-premises Exchange Autodiscover service didn't return a valid response that passed analysis.Test 

Steps

Sending an Autodiscover request to the on-premises Exchange Autodiscover service: 

The on-premises Exchange Autodiscover service didn't return a valid response.Additional 

DetailsException details:  

Message: The underlying connection was closed: An unexpected error occurred on a receive.  

Type: System.Net.WebException  

Stack trace:  

at System.Net.HttpWebRequest.GetResponse()  

at Microsoft.M365.RCA.Services.RcaHttpRequest.GetResponse()  

Exception details:  

Message: Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host.  

Type: System.IO.IOException  

Stack trace:  

at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)  

at System.Net.FixedSizeReader.ReadPacket(Byte[] buffer, Int32 offset, Int32 count)  

at System.Net.Security._SslStream.StartFrameHeader(Byte[] buffer, Int32 offset, Int32 count, AsyncProtocolRequest asyncRequest)  

at System.Net.Security._SslStream.StartReading(Byte[] buffer, Int32 offset, Int32 count, AsyncProtocolRequest asyncRequest)  

at System.Net.Security._SslStream.ProcessRead(Byte[] buffer, Int32 offset, Int32 count, AsyncProtocolRequest asyncRequest)  

at System.Net.TlsStream.Read(Byte[] buffer, Int32 offset, Int32 size)  

at System.Net.PooledStream.Read(Byte[] buffer, Int32 offset, Int32 size)  

at System.Net.Connection.SyncRead(HttpWebRequest request, Boolean userRetrievedStream, Boolean probeRead)  

Exception details:  

Message: An existing connection was forcibly closed by the remote host  

Type: System.Net.Sockets.SocketException  

Stack trace:  

at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-27*

Hi all,

Thanks all of your information. For future reference:

We found out the root cause is the Firewall setting.

-  Test-OAuthConnectivity PS failed: We misconfigure some settings in firewall so Autodiscover and EWS from External is not working;

-  Microsoft Remote Connectivity Analyze Tools failed: Firewall missed to allow some IPs in https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide, Commom ID 46

https://learn.microsoft.com/en-us/connectivity-analyzer/exchange-remote-connectivity-analyzer-tool

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-09-19*

Hi @Louis CI Lo  ,

Might be related to this.

Have you enabled TLS1.2?

https://learn.microsoft.com/en-us/exchange/exchange-tls-configuration?view=exchserver-2019

https://learn.microsoft.com/en-us/dotnet/framework/network-programming/tls#configuring-security-via-the-windows-registry

Regards

Shaofan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

First point related DNS records, update the virtual directories to 2019 and migrate all mailboxes to 2019, then shut down the 2013 temporarily. If all works well, then you could decommission your 2013 server.

For the migration, refer to the step-by-step guide: How Do I Migrate from Exchange 2013 to 2019?

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
