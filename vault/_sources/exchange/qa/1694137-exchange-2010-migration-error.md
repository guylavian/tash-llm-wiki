---
title: "Exchange 2010 migration error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1694137/exchange-2010-migration-error
question_id: 1694137
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2010 migration error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1694137/exchange-2010-migration-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all

Having issues trying to migrate a 1GB mailbox from Exchange 2016 across a slow link. The migration goes to 95% and then fails. These are the steps below which I have followed, but no difference to the end result. Any ideas on what else to try?

I have added the KeepAliveTime [Decimal 300000] to the registry and restarted the server HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\TcpIp\Parameters

Changed the C:\Program Files\Microsoft\Exchange Server\V15\Bin\MSExchMailboxReplication.exe.config file to reflect the following:

< MrsProxyClientHttpsBinding

receiveTimeout="00:00:50" changed to "00:05:00"

sendTimeout="00:00:50" changed to"00:05:00"

<MRSProxyConfiguration

DataImportTimeout="00:01:00" changed to DataImportTimeout="00:20:00"

<MRSConfiguration

ExportBufferSizeKB="512" added this directly afterwards ExportBufferSizeOverrideKB="7500"

 

Ran this cmd

C:\Windows\system32>Get-MoveRequestStatistics ******@domain.com -IncludeReport | Export-Clixml c:\temp\SSRO.xml

C:\Windows\system32>$stats = Import-Clixml c:\temp\SSRO.xml

C:\Windows\system32>$stats.report.failures[-1]

 

Which gives the following error

Timestamp         : 6/11/2024 10:36:06 AM

FailureType       : SourceMailboxConnectionStalePermanentException

FailureCode       : -2146233088

MapiLowLevelError : 0

FailureSide       : Source

FailureSideInt    : 1

ExceptionTypes    : {Exchange, MRS, MRSPermanent}

ExceptionTypesInt : {1, 10, 12}

Message           : Couldn't connect to the source mailbox. --> The call to 'net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService' failed because no service  was listening on the specified endpoint. Error details: Could not connect to net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService. The connection attempt lasted for a time span of 00:00:04.0900108. TCP error code 10061: No connection could be made because the target machine actively refused it 10.x.x.x:808.  --> No connection could be made because the target machine actively  refused it 10.x.x.x:808 --> Could not connect to net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService. The connection attempt lasted for a time span of 00:00:04.0900108. TCP error code 10061: No connection could be made because the target machine actively refused it 10.x.x.x:808.  --> No connection could be made because the target machine actively refused it 10.x.x.x:808

MessageData       :

DataContext       : --------

                    Operation: IMailbox.Connect

                    Operation: [Connect] IMailbox.Connect

                    OperationSide: Source

                    76fdbb05-4594-48f1-9080-04a8fd7d788d (Primary)

                    Flags: None

DataContextData   :

StackTrace        :

InnerException    : EndpointNotFoundTransientException: The call to 'net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService' failed because no service was listening on the specified endpoint. Error details: Could not connect to net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService. The connection attempt lasted for a time span of 00:00:04.0900108. TCP error code 10061: No connection could be made because the target machine actively refused it 10.x.x.x:808.  --> No connection could be made because the target machine actively refused it 10.x.x.x:808 --> Could not connect to net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService. The connection attempt lasted for a time span of 00:00:04.0900108. TCP error code 10061: No connection could be made because the target  machine actively refused it 10.x.x.x:808.  --> No connection could be made because the target machine actively refused it 10.x.x.x:808

UnknownElements   :

UnknownAttributes :

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-12*

The MRS service was already enabled but I restarted it

When I ran this  Get-WebServicesVirtualDirectory | FL MRSProxyEnabled it was false so i ran the cmd to enabled it.

If the MRS service is already running, should the MRSProxy be automatically enabled or are they not related?

Even after making these changes, still experiencing the same issues

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-12*

Hi,

According to the error displayed : Could not connect to net.tcp://servername/Microsoft.Exchange.MailboxReplicationService.ProxyService

You appear to be unable to access the Exchange Mailbox Replication Service (MRS) on the source Exchange server.

Check whether the status of the Microsoft Exchange Mailbox Replication Service on the source Exchange server is running.

Make sure MRS Proxy is enabled on the source Exchange server.

Run Get-WebServicesVirtualDirectory | FL MRSProxyEnabled

If it is False, set it to True, run the command: Set-WebServicesVirtualDirectory -Identity "ServerName\EWS (Default Web Site)" -MRSProxyEnabled $true

Please feel free to contact me for any updates.
