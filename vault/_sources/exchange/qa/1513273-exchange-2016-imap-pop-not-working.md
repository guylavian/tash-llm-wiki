---
title: "Exchange 2016 - IMAP/POP not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1513273/exchange-2016-imap-pop-not-working
question_id: 1513273
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 - IMAP/POP not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1513273/exchange-2016-imap-pop-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I have Exchange Server 2016 configured on Windows Server 2019. 
I have a FortiGate firewall and FortiMail between the firewall and the Exchange server.
The incoming ports are configured as 25,465,587,993, 995 to FortiMail.
The send connector is configured to FortiMail IP address.
I have to use IMAP or POP via Thunderbird because not everyone has Outlook.
I am testing communication with Exchange Server on IMAP port on https://testconnectivity.microsoft.com/ and the test failed:

The IMAP service is being tested.There was an error testing the IMAP serviceAdditional DetailsProtocol Log: C: 1 CAPABILITY S: * OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN AUTH=LOGIN] mail service ready. S: * CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN AUTH=LOGIN S: 1 OK Pre-login capabilities listed, post-login capabilities have more. C: 2 LOGIN ******@contoso.com ******** S: 2 NO [AUTHENTICATIONFAILED] Authentication failed. Exception details: Message: Serwer IMAP zwrócił stan błędu „2 NO [AUTHENTICATIONFAILED] Authentication failed.”. Type: Microsoft.M365.RCA.Services.Protocols.Imap.ImapServerErrorException Stack trace: at Microsoft.M365.RCA.Services.Protocols.Imap.ImapCommand`1.CheckForOk(IList`1 response) at Microsoft.M365.RCA.Services.Protocols.Imap.LoginCommand.ProcessResponse(IList`1 response) at Microsoft.M365.RCA.Services.Protocols.ProtocolClient.<SendCommandAsync>d__17`1.MoveNext() --- End of stack trace from previous location where exception was thrown --- at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw() at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task) at Microsoft.M365.RCA.ConnectivityTests.ImapPop.BaseProtocolTest.<PerformTestInternalAsync>d__12.MoveNext()

Has anyone had problems with IMAP like this and have a solution to resolve the issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-27*

dears 

please share the steps i have the same issue

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-13*

Not sure if you solved this already, and it might be a very obvious question, but is IMAP & POP enabled and configured on the server, as it is not enabled by default?
https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-pop3?view=exchserver-2019
https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-imap4?view=exchserver-2019
If so, it can also be that the PopProxy and ImapProxy components are in inactive state.
https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/cannot-connect-to-pop3-or-imap4?source=recommendations
