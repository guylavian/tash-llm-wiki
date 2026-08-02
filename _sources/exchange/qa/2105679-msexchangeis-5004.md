---
title: "MSExchangeIS 5004"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105679/msexchangeis-5004
question_id: 2105679
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchangeIS 5004

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105679/msexchangeis-5004 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. Exchange 2016 on-premise.

MSExchangeIS 5004

Microsoft.Exchange.Server.Storage.DirectoryServices.DirectoryTransientErrorException: ErrorCode: AdUnavailable, LID: 52664 - Unable to retrieve mailbox information for mailbox with guid f1267fe9-8d02-4ead-8e81-9c2f22fac6fe ---> Microsoft.Exchange.Data.Directory.ADTransientException: Cannot find Template Tenant. at Microsoft.Exchange.Data.Directory.ADSessionSettingsFactory.FromConsumerOrganization() at Microsoft.Exchange.Data.Directory.ADLatencyTracker.MeasureSettingsCreationTime(Func`1 settingsCreationFunc, String memberName) at Microsoft.Exchange.Data.Directory.ADSessionSettings.FromConsumerOrganizationUserScopeSet(Guid mailboxGuid) at Microsoft.Exchange.Data.Directory.TenantPartitionHint.GetTenantScopedADSessionSettingsServiceOnly(Nullable`1 mailboxGuid) at Microsoft.Exchange.Data.Directory.ADSessionSettingsFactory.FromTenantPartitionHintAndMailboxGuid(TenantPartitionHint partitionHint, Guid mailboxGuid) at Microsoft.Exchange.Data.Directory.ADSessionSettings.<>c__DisplayClass170_0.<FromTenantPartitionHintAndMailboxGuid>b__0() at Microsoft.Exchange.Data.Directory.ADLatencyTracker.MeasureSettingsCreationTime(Func`1 settingsCreationFunc, String memberName) at Microsoft.Exchange.Data.Directory.ADSessionSettings.FromTenantPartitionHintAndMailboxGuid(TenantPartitionHint partitionHint, Guid mailboxGuid) at Microsoft.Exchange.Server.Storage.DirectoryServices.ADObjectWrappers.ADRecipientSession..ctor(IExecutionContext context, ConsistencyMode consistencyMode, TenantHint tenantHint, ADObjectId localDatabaseId, String domainController, CreateADRecipientSessionFlags flags) at Microsoft.Exchange.Server.Storage.DirectoryServices.ADObjectWrappers.ADObjectWrapperFactory.CreateADRecipientSession(IExecutionContext context, ConsistencyMode consistencyMode, TenantHint tenantHint, ADObjectId localDatabaseId, String domainController, CreateADRecipientSessionFlags flags) at Microsoft.Exchange.Server.Storage.DirectoryServices.Directory.LoadMailboxInfoByGuid(IExecutionContext context, TenantHint tenantHint, String domainController, Guid mailboxGuid, GetMailboxInfoFlags flags, Boolean& ours) --- End of inner exception stack trace --- at Microsoft.Exchange.Server.Storage.DirectoryServices.Directory.LoadMailboxInfoByGuid(IExecutionContext context, TenantHint tenantHint, String domainController, Guid mailboxGuid, GetMailboxInfoFlags flags, Boolean& ours) at Microsoft.Exchange.Server.Storage.DirectoryServices.Directory.GetMailboxInfoHelper(IExecutionContext context, TenantHint tenantHint, String domainController, Guid mailboxGuid, GetMailboxInfoFlags flags) at Microsoft.Exchange.Server.Storage.DirectoryServices.Directory.GetMailboxInfoImpl(IExecutionContext context, TenantHint tenantHint, Guid mailboxGuid, GetMailboxInfoFlags flags) at Microsoft.Exchange.Server.Storage.DirectoryServices.DirectoryBase.GetMailboxInfo(IExecutionContext context, TenantHint tenantHint, Guid mailboxGuid, GetMailboxInfoFlags flags) at Microsoft.Exchange.Server.Storage.MapiDisp.MailboxCleanup.GetMailboxInfoFromAD(Context context, TenantHint tenantHint, Guid mdbGuid, Guid mailboxGuid, MailboxInfo& directoryMailboxInfo)

Get-Mailbox -ResultSize Unlimited | Select Name,GUID | where GUID -eq "f1267fe9-8d02-4ead-8e81-

9c2f22fac6fe"

no result

What the problem ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-18*

Agree with Jake Zhang-MSFT points, Need to one more point, If the mailbox was deleted, consider checking for disconnected mailboxes in the database-

Get-MailboxStatistics -Database "YourDatabaseName" | Where-Object {$_.DisconnectReason -ne $null}

If the mailbox is disconnected, you may be able to reconnect it. Refer similar thread for the same.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-18*

Hi @Андрей Михалевский,

Welcome to the Microsoft Q&A platform!

Based on your description, the error MSExchangeIS 5004 you are encountering along with DirectoryTransientErrorException means that the Exchange server cannot retrieve the mailbox information from Active Directory. This can happen for a number of reasons, here are some steps to resolve the issue:

 

-  Make sure your Active Directory service is available and responsive. The error indicates a transient problem with AD, so check the connectivity and performance of the domain controller.

-  The Get-Mailbox command you ran did not return any results for the specified GUID. This could mean that the mailbox does not exist or has been deleted. Double-check the GUID and make sure it is correct.

-  If you have multiple domain controllers, make sure AD replication is working properly. The mailbox may exist, but the information has not yet been replicated to all DCs.

-  Verify that the Exchange server has the necessary permissions to read from Active Directory. Insufficient permissions can cause problems when Exchange tries to access mailbox information.

-  Restart the Exchange service to see if the issue is resolved. Sometimes a simple restart can clear transient errors.

-  The error mentions ADSessionSettingsFactory.FromConsumerOrganization(). This may indicate an issue with session setup. Make sure the Exchange server is configured correctly to communicate with AD.

-  The error "Cannot find template tenant" may indicate an issue with multi-tenant configuration. If you are not using a multi-tenant setup, this may be a configuration error.

 

By following these steps, you should be able to identify and resolve the issue that is preventing Exchange from accessing the mailbox information. If the issue persists, it may be helpful to provide more context or error logs for further diagnosis.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
