---
title: "Exchange 2016: IMAP4 not working (user and mailbox are in a different site)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316735/exchange-2016-imap4-not-working-user-and-mailbox-a
question_id: 316735
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016: IMAP4 not working (user and mailbox are in a different site)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316735/exchange-2016-imap4-not-working-user-and-mailbox-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

IMAP4 on Exchange server not working. When we telnet to port:993 we get a black screen (screenshot)    

the test the IMAP settings output:     

[PS] C:\Windows\system32>Test-ImapConnectivity -ClientAccessServer EX01 -MailboxCredential (Get-Credential domain\user) |fl Port,connectionType,Result,Error    

Port           : 0    

ConnectionType : Plaintext    

Result         : Failure    

Error          : Unable to create MailboxSession object to access the mailbox [email address].    

```
Detailed error information:  
             [Microsoft.Exchange.Data.Storage.WrongServerException]: The user and the mailbox are in different  
             Active Directory sites. Inner error [Microsoft.Mapi.MapiExceptionMailboxInTransit]:  
             MapiExceptionMailboxInTransit: Detected site violation (hr=0x0, ec=1292)
```

We've modified the IMAP4 config file: Microsoft.Exchange.Imap4.exe.config    

to allow cross site authentication, the restarted the service but it didn't resolve the issue.     

IMAP4 component shows health    

[PS] C:\Windows\system32>Get-ServerHealth EX01 | ?{$_.HealthSetName -like "IMAP*"}    

Server          State           Name                 TargetResource       HealthSetName   AlertValue ServerComp    

                                                                                                     onent  

------          -----           ----                 --------------       -------------   ---------- ----------    

EX01     NotApplicable   ImapCTPMonitor       MSExchangeImap4      IMAP            Healthy    None    

EX01     NotApplicable   ProcessProcessorT... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   ImapSelfTestMonitor  MSExchangeImap4BE    IMAP.Protocol   Healthy    None    

EX01     NotApplicable   ImapDeepTestMonitor  MSExchangeImap4BE    IMAP.Protocol   Healthy    None    

EX01     NotApplicable   PrivateWorkingSet... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   ProcessProcessorT... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   CrashEvent.M.exch... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   PrivateWorkingSet... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   ProcessProcessorT... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   ProcessProcessorT... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   CrashEvent.M.exch... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     Online          ImapProxyTestMonitor MSExchangeImap4      IMAP.Proxy      Healthy    ImapProxy    

EX01     NotApplicable   PrivateWorkingSet... microsoft.exchang... IMAP.Protocol   Healthy    None    

EX01     NotApplicable   PrivateWorkingSet... microsoft.exchang... IMAP.Protocol   Healthy    None    

Event Logs show the following warning:     

The Test-CasConnectivity cmdlet failed. Find the entry in TransientErrorCache. BaseUrl: . MbxServre: EX01.contoso.local. Error: Target: EX01.contoso.local|HQ    

Error: Unable to create MailboxSession object to access the mailbox [email address].    

Detailed error information:    

[Microsoft.Exchange.Data.Storage.WrongServerException]: The user and the mailbox are in different Active Directory sites. Inner error [Microsoft.Mapi.MapiExceptionMailboxInTransit]: MapiExceptionMailboxInTransit: Detected site violation (hr=0x0, ec=1292)    

Details:    

Client Access Server Name: EX01.contoso.local    

Scenario: Create a MailboxSession object.    

Scenario Description: Creating MailboxSession object to access the mailbox [email address].    

User Name: user    

Performance Counter Name:     

Result: Failure    

Site: HQ    

Latency: -00:00:00.0010000    

Secure Access: True    

ConnectionType: Plaintext    

Port: 0    

Latency (ms): -1    

Virtual Directory Name:     

URL: null    

URL Type: Unknown    

Error:     

Unable to create MailboxSession object to access the mailbox [user].    

Detailed error information:    

[Microsoft.Exchange.Data.Storage.WrongServerException]: The user and the mailbox are in different Active Directory sites. Inner error [Microsoft.Mapi.MapiExceptionMailboxInTransit]: MapiExceptionMailboxInTransit: Detected site violation (hr=0x0, ec=1292)    

-------------------------------------    

. Warning: .    

Thank you for your continuous support!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Hi,    

1 Check the IMAP services, make sure all IMAP services are running on all servers. We can also try to restart these services and check if any helps. (There are two services : Microsoft Exchange IMAP4 & Microsoft Exchange IMAP4 Backend  )     

2 Check the certificate, make sure it had been assigned to IMAP service. If you are using a 3rd party cert, you can try to switch to self-certificate as a test and check again.     

3 Would you try specify the mailbox server that the test mailbox belongs to with "-MailboxServer name" ?    

4 Run below command to turn on IMAP protocol logging to help resolve issue:    

   a. Enable logging: Set-ImapSettings -server <CAS server name> -ProtocolLoggingEnabled $true    

   b. Get the location of log file and mailbox server: Get-ImapSettings -server <CAS server name>    

5 Do you have a LB?     

You can have another test in EXRCA: https://testconnectivity.microsoft.com/tests/Imap/input    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
