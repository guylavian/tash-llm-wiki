---
title: "Exchange 2013 CU23 IMAP setup \"NO LOGIN failed\" error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1156767/exchange-2013-cu23-imap-setup-no-login-failed-erro
question_id: 1156767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 CU23 IMAP setup "NO LOGIN failed" error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1156767/exchange-2013-cu23-imap-setup-no-login-failed-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am trying to setup IMAP access on my Exchange 2013 CU23 (with november 2022 update installed). Server edition is 2012 R2 with the latest WIndows updates installed.

I followed this MS official documentation: https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-imap4?view=exchserver-2016

Both internal and external settings are set the same (we have a split brain dns setup).

The problem is that I cannot login successfully to the IMAP server. The error returned is "NO LOGIN failed". 

I tried both to set the IMAP LoginType to 1 (PlainText) and 3 (SecureLogin). Same result.

Restarting the IMAP4 services do not change the behavior.

I try to authenticate with normal users who have the IMAP4 enabled. Tests are done with Android mobiles and with the Connectivity Analyzer Microsoft tool. The latter returns the following:

The IMAP service is being tested.
There was an error testing the IMAP service
Additional Details
Protocol Log: S: * OK The Microsoft Exchange IMAP4 service is ready.
C: 1 CAPABILITY
S: * CAPABILITY IMAP4 IMAP4rev1 AUTH=PLAIN AUTH=NTLM AUTH=GSSAPI STARTTLS UIDPLUS MOVE ID CHILDREN IDLE NAMESPACE LITERAL+
S: 1 OK CAPABILITY completed.
C: 2 STARTTLS
S: 2 OK Begin TLS negotiation now.
C: 3 CAPABILITY
S: * CAPABILITY IMAP4 IMAP4rev1 AUTH=PLAIN AUTH=NTLM AUTH=GSSAPI UIDPLUS MOVE ID CHILDREN IDLE NAMESPACE LITERAL+
S: 3 OK CAPABILITY completed.
C: 4 LOGIN biokolormakeup\frasav ********
S: 4 NO LOGIN failed.
Exception details:
Message: Il server IMAP ha riportato uno stato di errore "4 NO LOGIN failed.".
Type: Microsoft.M365.RCA.Services.Protocols.Imap.ImapServerErrorException
Stack trace:
at Microsoft.M365.RCA.Services.Protocols.Imap.ImapCommand`1.CheckForOk(IList`1 response)
at Microsoft.M365.RCA.Services.Protocols.Imap.LoginCommand.ProcessResponse(IList`1 response) at Microsoft.M365.RCA.Services.Protocols.ProtocolClient.&lt;SendCommandAsync&gt;d__17`1.MoveNext()
--- End of stack trace from previous location where exception was thrown ---
at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
at Microsoft.M365.RCA.ConnectivityTests.ImapPop.BaseProtocolTest.<PerformTestInternalAsync>d__12.MoveNext()

I also checked the Event logs (Security logs) on Exchange and domain controllers to look for any error, but I cannot find anything related to my test attempts.

I do not know what else I can try or to look at to resolve this issue. Please help.
Thank you,
Francesco

Please note: the reason why I need to enable IMAP4, is because in the last few months EAS is behaving oddly on Android devices. MS Outlook app support is already trying to figure out what is going on EAS (MS Exchange support says that is an app related issue, nothing on my server). In the meanwhile I need to give my users a working way to read emails on their mobiles.

Update: 

1.
Logs of IMAP service are full of the following (<> placeholders where sensitive data has been removed):

2023-01-09T13:16:59.348Z,00000000000000E2,0,192.168.3.212:993,192.168.3.212:22162,,39,0,53,OpenSession,,
2023-01-09T13:16:59.348Z,00000000000000E2,1,192.168.3.212:993,192.168.3.212:22162,,1,15,143,capability,,R=ok
2023-01-09T13:16:59.473Z,00000000000000E2,2,192.168.3.212:993,192.168.3.212:22162,<username>,122,41,23,login,<username@keyman  .local> *****,"R=""aXSV NO LOGIN failed."";Msg=Proxy:<CAS FQDN>:1993:SSL;ErrMsg=ProxyNotAuthenticated"
2023-01-09T13:16:59.473Z,00000000000000E2,3,192.168.3.212:993,192.168.3.212:22162,<username>,0,0,0,CloseSession,,
2023-01-09T13:17:08.223Z,00000000000000E4,0,127.0.0.1:993,127.0.0.1:22207,,27,0,53,OpenSession,,
2023-01-09T13:17:08.223Z,00000000000000E4,1,127.0.0.1:993,127.0.0.1:22207,,1,12,140,capability,,R=ok
2023-01-09T13:17:08.223Z,00000000000000E4,2,127.0.0.1:993,127.0.0.1:22207,,0,0,0,CloseSession,,
2023-01-09T13:17:11.129Z,00000000000000E5,0,127.0.0.1:993,127.0.0.1:22219,,29,0,53,OpenSession,,
2023-01-09T13:17:11.129Z,00000000000000E5,1,127.0.0.1:993,127.0.0.1:22219,,1,12,140,capability,,R=ok
2023-01-09T13:17:11.239Z,00000000000000E5,2,127.0.0.1:993,127.0.0.1:22219,HealthMailboxab28d88,107,76,99,login,HealthMailboxab28d8826ea8428d805c5e21cdff9077@<smtpdomain> *****,"R=""z NO [Error=ProxyNotAuthenticated Proxy=<CAS FQDN>:1993:SSL] LOGIN failed."";Msg=Proxy:<CAS FQDN>:1993:SSL;ErrMsg=ProxyNotAuthenticated"
2023-01-09T13:17:11.239Z,00000000000000E5,3,127.0.0.1:993,127.0.0.1:22219,HealthMailboxab28d88,0,0,0,CloseSession,,
2023-01-09T13:18:08.364Z,00000000000000E7,0,127.0.0.1:993,127.0.0.1:22357,,39,0,53,OpenSession,,
2023-01-09T13:18:08.364Z,00000000000000E7,1,127.0.0.1:993,127.0.0.1:22357,,1,12,140,capability,,R=ok
2023-01-09T13:18:08.364Z,00000000000000E7,2,127.0.0.1:993,127.0.0.1:22357,,0,0,0,CloseSession,,

2.
Moreover, I am checking these solutions, I will follow up on these in case they help me finding a solution:

-  https://social.technet.microsoft.com/Forums/lync/en-US/b14005e4-6416-463b-91db-a4f14620c9f2/imap-connection-failure-no-login-failed-proxynotauthenticated?forum=exchangesvrclients

-  http://clintboessen.blogspot.com/2018/03/binding-certificate-breaks-imap-or-pop.html

UPDATE 3
I managed to get it working. I do not exactly know why it fixed the problem but somehow it did the trick. 

Following the MS article linked above about how to setup imap, I initially used this command to set the service:

Set-ImapSettings -ExternalConnectionSettings "mail.contoso.com:993:SSL","mail.contoso.com:143:TLS" -InternalConnectionSettings "mail.contoso.com:993:SSL","mail.contoso.com:143:TLS" -X509CertificateName mail.contoso.com

After reading posts of other people having the same or similar behavior as me, someone got imap start working by reassigning the 3rd party ssl certificate to the IMAP service. 
Note before continuing: it's worth noting that my Exchange EventLog, the system EventLog, was full of Schannel errors starting exactly from the time I ran the powershell cmdlet here above. My 3rd party certificate was assigned only to IIS and IMAP services at that time.

In order to reassign the 3rd party certificate to the IMAP service, I followed Clint Boessen's advice (see linked blog article above):

-  Set-ImapSettings -X509CertificateName <Exchange Server FQDN> (I reassigned the default Exchange certificate to the imap service)

-  Enable-ExchangeCertificate -Thumbprint <Thumbprint of my 3rd party CA certificate> -Services IMAP (I assigned back my 3rd party ca cert to the IMAP service)

Surprisingly (for me, but there will be a reason, of course), after hitting enter on the cmdlet above, I checked again the services assigned to my 3rd party ca certificate, and the services assigned were IIS, IMAP and SMTP (??). I did not specify SMTP in the cmdlet above.
So I checked again the system EventLog and Schannel errors were gone. (?? again)
I tested IMAP service with Test-ImapConnectivity cmdlet and it succeeded. I tried also the Microsoft Connectivity Analyzer tool and it succeeded as well.

So, I don't know if it was a matter of reassigning the certificate to the IMAP service or, in order to use IMAP, you need to assign both IMAP and SMTP services to your 3rd party ca certificate. It maybe that some Exchange experts here can answer this question. There is no mention about this requirement in the official MS documentation linked above about enabling IMAP4.

But, in the end, this is how I managed to get IMAP start working. Hope it can help someone having the same issue.

Please, some moderator can mark this last update as answer, better if adding some explaination to my doubts here above too. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-10*

For sending emails, when you use SMTP, we will be using the CAS client connector and might need to run the below cmd.

```
Set-ReceiveConnector “*CASHostnameClient Frontend CASHostname” -AdvertiseClientSettings $True -FQDN NLBUrl
```

I am using Windows NLB, so I am using NLBUrl in the cmd to get high availability. 
http://technet.microsoft.com/en-us/library/jj657728(v=exchg.150).aspx#settings
