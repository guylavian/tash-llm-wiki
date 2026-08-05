---
title: "Installing Exchange 2016 CU18 error: /PrepareAD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/121834/installing-exchange-2016-cu18-error-preparead
question_id: 121834
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Installing Exchange 2016 CU18 error: /PrepareAD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/121834/installing-exchange-2016-cu18-error-preparead (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Current environment:  Exchange 2010 SP3 on Windows Server 2008 R2.  One Exchange 2010 server (Mailbox, CAS, and HUB), and one Exchange Edge Transport 2010.   

All prerequisites for Exchange 2016 have been installed: Windows components, .NET 4.8, Visual C++ Red, and UM.  

Forest/Domain Functional Level: 2008R2.  Site has Global Catalog.  

Trying to upgrade to Exchange 2016 CU18, one Mailbox role and one Edge Transport Role.  

After successfully running the extended Schema prep, I went ahead and attempted the /PrepareAD command.  I received the following error below:   

The following error was generated when "$error.Clear();   

              initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions

" was run: "Microsoft.Exchange.Data.Directory.AdminLimitExceededException: The administrative limit for this request was exceeded. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The administration limit on the server was exceeded.  

   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)  

   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)  

   at Microsoft.Exchange.Data.Directory.GuardedDirectoryExecution.ExecuteT  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.GuardedSendRequest(String forestName, GuardedDirectoryExecution guardedDirectoryExecution, DirectoryRequest request, TimeSpan timeout, Func`3 sendRequestDelegate, Int64& concurrency)      at Microsoft.Exchange.Data.Directory.PooledLdapConnection.SendRequest(DirectoryRequest request, LdapOperation ldapOperation, Nullable`1 clientSideSearchTimeout, IADLogContext logContext, Boolean shouldLogLastFilter)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-15*

The only other member group that I was not a part of, according to your list, is 'Group Policy Creator Owner'.  I added it.  Also, the FW team removed all rules between the Exchange Server and DCs.  Rebooted the Exchange box and attempted to run Setup.exe.  Same error during Step 1 of 15: Organization Preparation.    

Error:  

The following error was generated when "$error.Clear();   

	initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions

" was run: "Microsoft.Exchange.Data.Directory.AdminLimitExceededException: The administrative limit for this request was exceeded. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The administration limit on the server was exceeded.  

   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)  

   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)  

   at Microsoft.Exchange.Data.Directory.GuardedDirectoryExecution.ExecuteT  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.GuardedSendRequest(String forestName, GuardedDirectoryExecution guardedDirectoryExecution, DirectoryRequest request, TimeSpan timeout, Func`3 sendRequestDelegate, Int64& concurrency)      at Microsoft.Exchange.Data.Directory.PooledLdapConnection.SendRequest(DirectoryRequest request, LdapOperation ldapOperation, Nullable`1 clientSideSearchTimeout, IADLogContext logContext, Boolean shouldLogLastFilter)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)  

   --- End of inner exception stack trace ---  

   at Microsoft.Exchange.Data.Directory.ADDataSession.AnalyzeDirectoryError(PooledLdapConnection connection, DirectoryRequest request, DirectoryException de, Int32 totalRetries, Int32 retriesOnServer, String callerFilePath, Int32 callerFileLine, String memberName)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)  

   at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation)  

   at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADConfigurationSession.Save(ADConfigurationObject instanceToSave, String callerFilePath, Int32 callerFileLine, String memberName)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateWKGuid(ADContainer container, ADObjectId dn, Guid wkGuid)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateGroup(ADOrganizationalUnit usgContainer, String groupName, Int32 groupId, Guid wkGuid, String groupDescription, GroupTypeFlags groupType, Boolean createAsRoleGroup)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateRoleGroup(ADOrganizationalUnit usgContainer, RoleGroupDefinition roleGroup)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateAndValidateRoleGroups(ADOrganizationalUnit usgContainer, RoleGroupCollection roleGroups)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-12*

Looking at the Exchange setup logs and Events Viewer, it looks like the Exchange setup is erroring out when it tries to create a security object/account ‘Compliance Management’ in the Microsoft Exchange Security Groups OU.  Do you think that has anything to do with Active Directory Split Permissions?    

Exchange Setup Logs:    

    

Event Viewer: Two errors.    

First error in Event Viewer:    

The following error was generated when "$error.Clear();    

```
initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions
```

" was run: "Microsoft.Exchange.Data.Directory.AdminLimitExceededException: The administrative limit for this request was exceeded. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The administration limit on the server was exceeded.    

---------------------------------------------    

Second Error in Event Viewer:    

ExSetup.exe    

2060    

Get Servers for myexampledomain.local    

TopologyClientTcpEndpoint (localhost)    

3    

System.ServiceModel.EndpointNotFoundException: Could not connect to net.tcp://localhost:890/Microsoft.Exchange.Directory.TopologyService. The connection attempt lasted for a time span of 00:00:02.0470637. TCP error code 10061: No connection could be made because the target machine actively refused it 127.0.0.1:890.  ---> System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 127.0.0.1:890

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

@Paul Siso      

I also want to confirm with you that what is the RU version of your Exchange 2010? You need to update Exchange 2010 at least to RU 11, before installing Exchange 2016 coexist with it. After installing Exchange 2016, then migration mailboxes from Exchange 2010 to Exchange 2016(You cannot update from Exchange 2010 to Exchange 2016 directly).    

You also need to update DC to Windows Server 2008 R2 SP1. As far as I know, this issue may caused by some setting on Windows server, if you still cannot install Exchange 2016 successfully, I would suggest you migrate DC to Windows server 2012 R2, then try to install Exchange 2016 again.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-11*

Hi  

I have seen a number of people posting issues with Shared Mailboxes on CU18, you might want to hold off your upgrade till CU19
