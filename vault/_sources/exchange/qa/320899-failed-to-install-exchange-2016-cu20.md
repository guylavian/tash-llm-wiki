---
title: "Failed to install Exchange 2016 CU20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320899/failed-to-install-exchange-2016-cu20
question_id: 320899
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Failed to install Exchange 2016 CU20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320899/failed-to-install-exchange-2016-cu20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error:  

The following error was generated when "$error.Clear();   

	install-AdministrativeGroup -DomainController $RoleDomainController

" was run: "Microsoft.Exchange.Data.Directory.ADObjectAlreadyExistsException: Active Directory operation failed on WCL-DC01.DOMAIN.local. The object 'CN=Folder Hierarchies,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=DOMAIN Construction Ltd,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=DOMAIN,DC=local' already exists. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object exists.  

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

   at Microsoft.Exchange.Management.Deployment.InstallAdministrativeGroup.InstallConfigurationObjectTObject  

   at Microsoft.Exchange.Management.Deployment.InstallAdministrativeGroup.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  

Can anyone tell me what this error means and how to get past it?  

CU20 update fails on Exchange 2016 Server on step 1

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-18*

resolved by following this   

https://blog.expta.com/2013/04/active-directory-operation-failed.html
