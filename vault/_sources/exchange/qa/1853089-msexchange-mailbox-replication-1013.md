---
title: "MSExchange Mailbox Replication 1013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1853089/msexchange-mailbox-replication-1013
question_id: 1853089
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchange Mailbox Replication 1013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1853089/msexchange-mailbox-replication-1013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Exchange 2016. Last CU last SU. On-premise.

I got error:

```
The Microsoft Exchange Mailbox Replication service was unable to synchronize Active Directory data with the request. 
DB:b9b032e6-a637-4823-97af-1de4c181b561
 RequestType:FolderMove
 RequestGuid:
 Failure:
MapiExceptionRecoveryMDBMismatch: Unable to open message store. (hr=0x80004005, ec=1165)
Diagnostic context:
    Lid: 55847   EMSMDBPOOL.EcPoolSessionDoRpc called [length=145]
    Lid: 43559   EMSMDBPOOL.EcPoolSessionDoRpc returned [ec=0x0][length=326][latency=0]
    Lid: 52176   ClientVersion: 15.1.2507.39
    Lid: 50032   ServerVersion: 15.1.2507.6039
    Lid: 35180  
    Lid: 23226   --- ROP Parse Start ---
    Lid: 27962   ROP: ropLogon [254]
    Lid: 17082   ROP Error: 0x48D     
    Lid: 26937  
    Lid: 21921   StoreEc: 0x48D     
    Lid: 27962   ROP: ropExtendedError [250]
    Lid: 1494    ---- Remote Context Beg ----
    Lid: 44410   StoreEc: 0x8004010F
    Lid: 36892   StoreEc: 0x8004010F
    Lid: 57721   StoreEc: 0x8004010F
    Lid: 61692   StoreEc: 0x8004010F
    Lid: 50608  
    Lid: 45768   StoreEc: 0x48D     
    Lid: 56872   dwParam: 0xFE
    Lid: 42712   StoreEc: 0x48D     
    Lid: 45434   Guid: ed2d5550-2625-4b8e-8f62-8d081c0d543c
    Lid: 10786   dwParam: 0x0        Msg: 15.01.2507.039:MS-EX03:b9b032e6-a637-4823-97af-1de4c181b561
    Lid: 1750    ---- Remote Context End ----
    Lid: 27962   ROP: ropGetPropsSpecific [7]
    Lid: 26881  
    Lid: 21817   ROP Failure: 0x48D     
    Lid: 46042   StoreEc: 0x48D     
    Lid: 32441  
    Lid: 1706    StoreEc: 0x48D     
    Lid: 24761  
    Lid: 20665   StoreEc: 0x48D     
    Lid: 25785  
    Lid: 29881   StoreEc: 0x48D     
Stack trace: 
   at Microsoft.Mapi.MapiExceptionHelper.InternalThrowIfErrorOrWarning(String message, Int32 hresult, Boolean allowWarnings, Int32 ec, DiagnosticContext diagCtx, Exception innerException)
   at Microsoft.Mapi.MapiExceptionHelper.ThrowIfError(String message, Int32 hresult, IExInterface iUnknown, Exception innerException)
   at Microsoft.Mapi.ExRpcConnection.OpenMsgStore(OpenStoreFlag storeFlags, String mailboxDn, Guid mailboxGuid, Guid mdbGuid, String& correctServerDn, ClientIdentityInfo clientIdentityAs, String userDnAs, String applicationId, Byte[] tenantHint, CultureInfo cultureInfo)
   at Microsoft.Mapi.MapiStore.OpenMapiStore(String serverDn, String userDn, String mailboxDn, Guid guidMailbox, Guid guidMdb, String userName, String domainName, String password, String httpProxyServerName, ConnectFlag connectFlags, OpenStoreFlag storeFlags, CultureInfo cultureInfo, Boolean wantRedirect, String& correctServerDN, ClientIdentityInfo clientIdentity, String applicationId, Client xropClient, Boolean wantWebServices, Byte[] clientSessionInfo, TimeSpan connectionTimeout, TimeSpan callTimeout, Byte[] tenantHint)
   at Microsoft.Mapi.MapiStore.OpenMailbox(String serverDn, String userDn, Guid guidMailbox, Guid guidMdb, String userName, String domainName, String password, ConnectFlag connectFlags, OpenStoreFlag storeFlags, CultureInfo cultureInfo, WindowsIdentity windowsIdentity, String applicationId, TimeSpan connectionTimeout, TimeSpan callTimeout, Byte[] tenantPartitionHint)
   at Microsoft.Exchange.MailboxReplicationService.MapiUtils.GetSystemMailbox(Guid mdbGuid, DatabaseInformation db, String dcName, NetworkCredential cred, Boolean allowCrossSiteLogon)
   at Microsoft.Exchange.MailboxReplicationService.MapiHandler.OpenStore(RequestIndexLocation indexLocation, Guid databaseGuid, Guid mailboxGuid, TenantPartitionHint tenantHint)
   at Microsoft.Exchange.MailboxReplicationService.MapiHandler.d__2.MoveNext()
   at Microsoft.Exchange.MailboxReplicationService.MapiHandler.d__6.MoveNext()
   at Microsoft.Exchange.MailboxReplicationService.RequestIndexEntryHandler`1.RemoveStaleEntries(IEnumerable`1 entries, RequestIndexEntryProvider requestIndexEntryProvider)
   at Microsoft.Exchange.MailboxReplicationService.ADInconsistencyCheck.CleanMapiDatabaseOrphan(MRSRequestType requestType, RequestJobProvider rjProvider, Guid dbGuid)
   at Microsoft.Exchange.MailboxReplicationService.ADInconsistencyCheck.<>c__DisplayClass39_2.b__0()
   at Microsoft.Exchange.MailboxReplicationService.CommonUtils.ProcessKnownExceptionsWithoutTracing(Action actionDelegate, FailureDelegate processFailure)
```

I don't understand the cause of the error and can't find any information about this event id.

Update: This is a recovery database. Maybe it should be given some flag so that Exchange does not process it ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-05*

Hi @Андрей Михалевский,

Welcome to the Microsoft Q&A platform!

According to your description,it looks like you are encountering a `MapiExceptionRecoveryMDBMismatch` error when trying to perform a folder move operation in Exchange 2016. This error, along with the diagnostic context you provided, indicates issues with MAPI (Messaging Application Programming Interface) when trying to open the message store.

Given that this is a recovery database, it is possible that Exchange is trying to process it as if it were a normal database, leading to this error.

Here's some potential steps to help resolve the issue:

-  Ensure that the recovery database is in the correct state. The recovery database should be mounted and recognized as a recovery database.

```
Get-MailboxDatabase -Identity "RecoveryDatabaseName" | Format-List Name, Recovery
```

   You should see `Recovery=True` in the output.

-  Try dismounting and then remounting the recovery database to see if this resolves any inconsistencies.

```
Dismount-Database -Identity "RecoveryDatabaseName" Mount-Database -Identity "RecoveryDatabaseName"
```

-  It's possible to set a flag to indicate that this is a recovery database, and prevent Exchange from processing it as a regular database. Use the `-Recovery` parameter to ensure this database is treated accordingly.

-  Sometimes the configuration of the Mailbox Replication Service (MRS) can affect how it processes requests. Ensure the MRS configuration is set correctly and consider restarting the service.

```
Restart-Service MSExchangeMailboxReplication
```

-  Review any pending or stuck move requests that might be associated with this database.

```
Get-MoveRequest | Where-Object {$_.Status -eq 'Failed' -or $_.Status -eq 'Queued'}
```

   You can remove problematic requests with:

```
Remove-MoveRequest -Identity "RequestIdentity"
```

Additionally, since this is a recovery database, double-check that all the steps you followed during the creation and mounting of this database were correct. Sometimes re-creating the recovery database might be the simplest solution if you aren't able to identify the exact cause of the error.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
