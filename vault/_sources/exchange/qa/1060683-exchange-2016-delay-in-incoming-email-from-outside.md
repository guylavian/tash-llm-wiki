---
title: "Exchange 2016 Delay in Incoming Email from Outside"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1060683/exchange-2016-delay-in-incoming-email-from-outside
question_id: 1060683
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Delay in Incoming Email from Outside

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1060683/exchange-2016-delay-in-incoming-email-from-outside (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I installed Exchange 2016 CU23 last night, and all went normally. However, upon restarting and verifying services etc, incoming email from external email addresses was being delayed for random amounts of time. It could be delayed anywhere from a few minutes to a couple of hours. I checked disk space first thing, and it is fine. I haven't noticed any backpressure signs. I am getting some errors in event logs related to w3wp.exe, but OWA, ECP, internal mail flow and outbound mail flow all work fine. It is just incoming mail from external senders that are being delayed. The databases (2 of them) are showing mounted in ecp, but blank in EMS. One exchange server w/ exchange on C: drive, DBs on separate drive and Logs on another separate drive.

I'm worried the update process might have made the frontend connectors corrupted or something similar.

-  (Process w3wp.exe, PID 35904) Connection leak detected for key domain.local/Exec_group/adminuser in Microsoft.Exchange.Configuration.Authorization.WSManBudgetManager class. Leaked Value 1.

-  Watson report about to be sent for process id: 6944, with parameters: E12IIS, c-RTL-AMD64, 15.01.2507.013, w3wp#MSExchangeOWAAppPool, M.E.C.Owa2.Server, M.E.C.O.S.C.OwaMapiNotificationManager.SubscribeToSuiteNotification, System.NotSupportedException, 80d2-dumptidset, 15.01.2507.013.

-  Transport service is disconnecting performance counters with process lifetime from their old process.

-  [PS] C:\Windows\system32>Get-MailboxDatabase | Format-List Name, Server, Mounted

Name : DB01-2016  

Server : EXCH2016  

Mounted :

Name : DB02-2016  

Server : EXCH2016  

Mounted :

-  The Client Access server isn't currently enabled and the Microsoft Exchange Unified Messaging call router can't listen on any TCP/UDP ports. Any existing connections will be disconnected.

-  The MaxActiveDatabases attribute on the Information Store object in Active Directory has not been configured.

Remote connectivity analyzer shows this when testing:

Attempting to send a test email message to user@keyman  .com using MX mail.domain.com.  

Delivery of the test email message failed.  

Additional Details  

The server returned status code -1 - Failure sending mail.

Exception details:

Message: Failure sending mail.

Type: System.Net.Mail.SmtpException

Stack trace:

at System.Net.Mail.SmtpClient.Send(MailMessage message)

at Microsoft.M365.RCA.ConnectivityTests.SmtpMessageTest.PerformSmtpMessageTest(RcaTestContext parent, String mailExchangerHost, ISmtpAddress emailAddress, ContextInfo contextInfo, SmtpOptions smtpOptions)

Exception details:

Message: Unable to connect to the remote server

Type: System.Net.WebException

Stack trace:

at System.Net.ServicePoint.GetConnection(PooledStream PooledStream, Object owner, Boolean async, IPAddress& address, Socket& abortSocket, Socket& abortSocket6)

at System.Net.PooledStream.Activate(Object owningObject, Boolean async, GeneralAsyncDelegate asyncCallback)

at System.Net.ConnectionPool.GetConnection(Object owningObject, GeneralAsyncDelegate asyncCallback, Int32 creationTimeout)

at System.Net.Mail.SmtpConnection.GetConnection(ServicePoint servicePoint)

at System.Net.Mail.SmtpClient.GetConnection()

at System.Net.Mail.SmtpClient.Send(MailMessage message)

Exception details:

Message: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond xxx.xxx.xxx.xxx:25

Type: System.Net.Sockets.SocketException

Stack trace:

at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)

Any ideas or thoughts are much appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

I've deleted and re-created the default receive connectors. After doing so, emails are coming in much faster. Not sure what happened but I will continue monitoring for a few days.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

Server is out of maintenance, and serviceHealth shows all is running.  We have a fortimail smarthost and I've been looking for any issues there.  It appears the delay is taking place before it hits our smarthost.  Once it hits the Fortimail, it goes through to the Exchange server normally.  What's strange is nothing changed in the fmail or firewall or with our mx records. Just an exchange CU install.  I'll keep digging.    

Edit: Noticing a lot of the delayed emails are exactly 10 minutes now.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-24*

Is the server fully out of maintence?     

```
Get-ServerComponentState -Identity Mailbox01
```

should show all active    

How about all the services? all good?    

```
Test-ServiceHealth
```
