---
title: "[Migrated from MSDN Exchange Dev] POP & IMAP connection proxy issue from Exchange 2016 to 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186144/migrated-from-msdn-exchange-dev-pop-imap-connectio
question_id: 186144
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] POP & IMAP connection proxy issue from Exchange 2016 to 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186144/migrated-from-msdn-exchange-dev-pop-imap-connectio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] POP & IMAP connection proxy issue from Exchange 2016 to 2010  

I have the exchange hybrid setup where exchange server 2010, 2016 with O365 hybrid setup configured. I want to migrate mailboxes from exchange 2010 to 2016 but before that I just wanted to ensure all CAS request should proxy from exchange 2010 to 2016, So that when we change DNS records to point our all traffic to exchange 2016 that will proxy the connection to exchange 2010 server if any mailbox located in 2010. During my testing I found as of now this is not happing OWA URL not getting proxied to Exchange 2010 from 2016. POP & IMAP also not getting proxied.  

Exchange server 2010 = SP3 with Rollup24  

Exchange server 2016 = CU15  

Error for owa access while access mailbox hosted on exchange 2010 and webmail URL is for exchange 2016.  

https://owa.server.com/owa/auth/errorFE.aspx?CafeError=CAS14WithNoWIA  

Something went wrong  

We can't get that information right now. Please try again later.  

X-ClientId: 8FFA1D6312C746738AFBFA575F5D5200  

X-FEServer "Server_Name"  

Date:12/3/2020 4:44:59 PM  

Error for pop while testing in Microsoft remote analyzer.  

Already checked with UPN & doamin\mailboxusername  

Additional Details  

Protocol Log: C: CAPA  

S: +OK The Microsoft Exchange POP3 service is ready.  

S: +OK  

S: TOP  

S: UIDL  

S: SASL PLAIN  

S: USER  

S: .  

C: USER <Testmailbox which is located in exchange 2010>.  

S: +OK  

C: PASS ********  

S: -ERR Logon failure: unknown user name or bad password.  

at Microsoft.M365.RCA.Services.Protocols.Pop.PopCommand`1.CheckForOk(IList`1 response) in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Pop\PopCommand.cs:line 36  

at Microsoft.M365.RCA.Services.Protocols.Pop.PassCommand.ProcessResponse(IList`1 response) in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Pop\PassCommand.cs:line 43   at Microsoft.M365.RCA.Services.Protocols.ProtocolClient.<SendCommandAsync>d__17`1.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\ProtocolClient.cs:line 103  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)  

at Microsoft.M365.RCA.Services.Protocols.Pop.PopProtocolClient.<LoginUserPass>d__6.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Pop\PopProtocolClient.cs:line 104  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)  

at Microsoft.M365.RCA.ConnectivityTests.ImapPop.BaseProtocolTest.<PerformTestInternalAsync>d__12.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\6\sources\dev\m365rca\src\connectivitytests\ImapPop\BaseProtocolTest.cs:line 137  

Error for IMAP while testing in Microsoft remote analyzer.  

Additional Details  

Protocol Log: C: 1 CAPABILITY  

S: +OK The Microsoft Exchange POP3 service is ready.  

Exception: Microsoft.M365.RCA.Services.Protocols.Imap.ImapServerErrorException: The IMAP server responded with an error status "+OK The Microsoft Exchange POP3 service is ready.".  

at Microsoft.M365.RCA.Services.Protocols.Imap.ImapCommand`1.CheckForOk(IList`1 response) in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Imap\ImapCommand.cs:line 66  

at Microsoft.M365.RCA.Services.Protocols.Imap.CapabilityCommand.ProcessResponse(IList`1 response) in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Imap\CapabilityCommand.cs:line 32   at Microsoft.M365.RCA.Services.Protocols.ProtocolClient.<SendCommandAsync>d__17`1.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\ProtocolClient.cs:line 103  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)  

at Microsoft.M365.RCA.Services.Protocols.Imap.ImapProtocolClient.<Capability>d__3.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\19\sources\dev\m365rca\src\services\Protocols\Imap\ImapProtocolClient.cs:line 54  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)  

at Microsoft.M365.RCA.ConnectivityTests.ImapPop.BaseProtocolTest.<PerformTestInternalAsync>d__12.MoveNext() in d:\dbs\sh\nibr\1102_065131_0\cmd\6\sources\dev\m365rca\src\connectivitytests\ImapPop\BaseProtocolTest.cs:line 135

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi,  

Just adding one more thing recently we have renewed the exchange certificate and disabled TLS 1.0, 1.1, not sure if that is causing this issue Before this POP & IMAP test was getting successful via MS test connectivity URL.  

Note: POP & IMAP is working for the same server mailboxes, Only problem is the connection not getting proxy from exchange 2016 to 2010.  

For owa redirection I found a solution in https://www.admin-enclave.com/en/articles/exchange/251-exchange-2010-to-exchange-2016-co-existence-migration-owa-redirect-not-working.html blog.  

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi    

Please check if the POP and IMAP are running on the server properly?    

In addition, could you please provide the configuration for your OWA virtual directories, which should be configured like below:    

    

For IMAP and POP in Exchange 2010 and 2016 coexistence:    

When the Exchange 2016 Client Access component receives a POP or IMAP request, it will authenticate the user and perform a service discovery.    

If the target mailbox is E2010, MBX2016 will enumerate the POP or IMAP InternalConnectionSettings property value for each Exchange 2010 Client Access server within the mailbox’s site. Therefore, it is important to ensure that the InternalConnectionSettings maps to the server's FQDN, and not a load-balanced namespace.    

Detailed information here: Client Connectivity in an Exchange 2016 Coexistence Environment with Exchange 2010    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
