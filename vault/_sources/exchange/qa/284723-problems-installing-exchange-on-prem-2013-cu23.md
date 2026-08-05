---
title: "Problems installing Exchange on-prem 2013 CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/284723/problems-installing-exchange-on-prem-2013-cu23
question_id: 284723
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Problems installing Exchange on-prem 2013 CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/284723/problems-installing-exchange-on-prem-2013-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are having problem upgrading our Exchange on-prem 2013 CU15 to Exchange on-prem 2013 CU23.  

The problem we are experiencing are in the prepare domain step and results in the follow error log.  

Any ideas about what we can do to continue our installation?

01-27-2021 13:40:29.0619] [2] Beginning processing initialize-DomainPermissions  

[01-27-2021 19:20:41.0882] [2] [ERROR] Failed to create a connection to any of the servers in the topology provider.  

[01-27-2021 19:20:41.0913] [1] The following 1 error(s) occurred during task execution:  

[01-27-2021 19:20:41.0913] [1] 0. ErrorRecord: Failed to create a connection to any of the servers in the topology provider.  

[01-27-2021 19:20:41.0913] [1] 0. ErrorRecord: Microsoft.Exchange.Data.Directory.ADTransientException: Failed to create a connection to any of the servers in the topology provider.  

at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, ADObjectId domain, String serverName, Int32 port, NetworkCredential credential)  

at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, NetworkCredential networkCredential, ADObjectId domain)  

at Microsoft.Exchange.Data.Directory.ADDataSession.GetConnection(String preferredServer, Boolean isWriteOperation, String optionalBaseDN, ADObjectId& rootId, ADScope scope)  

at Microsoft.Exchange.Data.Directory.ADDataSession.InternalFind[TResult](ADObjectId rootId, String optionalBaseDN, ADObjectId readId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults, IEnumerable`1 properties, Boolean includeDeletedObjects)   at Microsoft.Exchange.Data.Directory.ADDataSession.Find[TResult](ADObjectId rootId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults, IEnumerable`1 properties, Boolean includeDeletedObjects)  

at Microsoft.Exchange.Data.Directory.ADDataSession.Find[TResult](ADObjectId rootId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults)  

at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADForest.FindRootDomain(Boolean readFromDc)  

at Microsoft.Exchange.Management.Tasks.SetupTaskBase.ReadRootDomainFromDc(OrganizationId orgId)  

at Microsoft.Exchange.Management.Tasks.SetupTaskBase.PrepareSessionsForRootOrg()  

at Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.InternalBeginProcessing()  

at Microsoft.Exchange.Configuration.Tasks.Task.<BeginProcessing>b__5()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)  

[01-27-2021 19:20:41.0913] [1] [ERROR] The following error was generated when "$error.Clear();  

$createTenantRoot = ($RoleIsDatacenter -or $RoleIsPartnerHosted);  

$createMsoSyncRoot = $RoleIsDatacenter;

$RoleDatacenterIsManagementForest is set only in Datacenter deployment; interpret its absense as $false

[bool]$isManagementForest = ($RoleDatacenterIsManagementForest -eq $true);

if ($RolePrepareAllDomains)  

{  

initialize-DomainPermissions -AllDomains:$true -CreateTenantRoot:$createTenantRoot -CreateMsoSyncRoot:$createMsoSyncRoot -IsManagementForest:$isManagementForest;  

}  

elseif ($RoleDomain -ne $null)  

{  

initialize-DomainPermissions -Domain $RoleDomain -CreateTenantRoot:$createTenantRoot -CreateMsoSyncRoot:$createMsoSyncRoot -IsManagementForest:$isManagementForest;  

}  

else  

{  

initialize-DomainPermissions -CreateTenantRoot:$createTenantRoot -CreateMsoSyncRoot:$createMsoSyncRoot -IsManagementForest:$isManagementForest;  

}  

" was run: "Microsoft.Exchange.Data.Directory.ADTransientException: Failed to create a connection to any of the servers in the topology provider.  

at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, ADObjectId domain, String serverName, Int32 port, NetworkCredential credential)  

at Microsoft.Exchange.Data.Directory.ConnectionPoolManager.GetConnection(ConnectionType connectionType, String partitionFqdn, NetworkCredential networkCredential, ADObjectId domain)  

at Microsoft.Exchange.Data.Directory.ADDataSession.GetConnection(String preferredServer, Boolean isWriteOperation, String optionalBaseDN, ADObjectId& rootId, ADScope scope)  

at Microsoft.Exchange.Data.Directory.ADDataSession.InternalFind[TResult](ADObjectId rootId, String optionalBaseDN, ADObjectId readId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults, IEnumerable`1 properties, Boolean includeDeletedObjects)   at Microsoft.Exchange.Data.Directory.ADDataSession.Find[TResult](ADObjectId rootId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults, IEnumerable`1 properties, Boolean includeDeletedObjects)  

at Microsoft.Exchange.Data.Directory.ADDataSession.Find[TResult](ADObjectId rootId, QueryScope scope, QueryFilter filter, SortBy sortBy, Int32 maxResults)  

at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADForest.FindRootDomain(Boolean readFromDc)  

at Microsoft.Exchange.Management.Tasks.SetupTaskBase.ReadRootDomainFromDc(OrganizationId orgId)  

at Microsoft.Exchange.Management.Tasks.SetupTaskBase.PrepareSessionsForRootOrg()  

at Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.InternalBeginProcessing()  

at Microsoft.Exchange.Configuration.Tasks.Task.<BeginProcessing>b__5()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  

[01-27-2021 19:20:41.0913] [1] [ERROR] Failed to create a connection to any of the servers in the topology provider.  

[01-27-2021 19:20:41.0913] [1] [ERROR-REFERENCE] Id=DomainGlobalConfig___27a706ffe123425f9ee60cb02b930e81 Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[01-27-2021 19:20:41.0913] [1] Setup is stopping now because of one or more critical errors.  

[01-27-2021 19:20:41.0913] [1] Finished executing component tasks.  

[01-27-2021 19:20:41.0944] [1] Ending processing Install-ExchangeOrganization  

[01-27-2021 19:20:41.0944] [0] CurrentResult console.ProcessRunInternal:198: 1  

[01-27-2021 19:20:41.0944] [0] CurrentResult launcherbase.maincore:90: 1  

[01-27-2021 19:20:41.0944] [0] CurrentResult console.startmain:52: 1  

[01-27-2021 19:20:41.0944] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1  

[01-27-2021 19:20:41.0944] [0] The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

[01-27-2021 19:20:41.0944] [0] CurrentResult main.run:235: 1  

[01-27-2021 19:20:41.0944] [0] The registry key, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\V15\Setup, wasn't found.  

[01-27-2021 19:20:41.0944] [0] CurrentResult setupbase.maincore:396: 1  

[01-27-2021 19:20:41.0944] [0] End of Setup  

[01-27-2021 19:20:41.0944] [0] **********************************************

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

Hi,    

Please can you run dcdiag on each of your domain controllers to check that there aren't any AD replication issues/other issues.     

Also, please make sure that the Exchange server has registered its name in DNS correctly and check for any events in the application and system log.     

What's your .NET Framework version currently?    

Possible cause: According to Microsoft Updates Guidance and Upgrade Paths for CU’s & .NET,  you might need upgrading your Exchange server to CU20 and .net version to 4.7.1, then upgrade Exchange server to CU22.     

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
