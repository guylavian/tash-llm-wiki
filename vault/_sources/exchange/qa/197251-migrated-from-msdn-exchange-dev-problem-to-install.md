---
title: "[Migrated from MSDN Exchange Dev] Problem to install exchange 2019 for migrating from 2013 to 2019."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197251/migrated-from-msdn-exchange-dev-problem-to-install
question_id: 197251
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# [Migrated from MSDN Exchange Dev] Problem to install exchange 2019 for migrating from 2013 to 2019.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197251/migrated-from-msdn-exchange-dev-problem-to-install (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]
 This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.    

[MSDN thread link]
 Problem to install exchange 2019 for migrating from 2013 to 2019.    

[Original post]

Dear All,    

I have problem with install exchange 2019 for migration from 2013 to 2019. bellow error has occurrence.    

My account is    

-domain admin    

-enterprise Admin and Schema admin    

i create a new user and give all permission and test again but not working!!!    

C:\Windows\system32>M:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD /OrganizationName:"First Organization"    

Microsoft Exchange Server 2019 Cumulative Update 7 Unattended Setup    

Copying Files...    

File copy complete. Setup will now collect additional information needed for installation.    

Performing Microsoft Exchange Server Prerequisite Check    

   Prerequisite Analysis                                                                             100%    

Setup will prepare the organization for Exchange Server 2019 by using 'Setup /PrepareAD'. No Exchange Server 2016 roles    

have been detected in this topology. After this operation, you will not be able to install any Exchange Server 2016    

roles.    

For more information, visit: https://learn.microsoft.com/Exchange/plan-and-deploy/deployment-ref/readiness-checks?view=exchserver-2019    

Configuring Microsoft Exchange Server    

  Organization Preparation                                                                          100%    

The following error was generated when "$error.Clear();    

 $createTenantRoot = ($RoleIsDatacenter -or    

$RoleIsPartnerHosted);    

 $createMsoSyncRoot = $RoleIsDatacenter;    

$RoleDatacenterIsManagementForest is set only in    

Datacenter deployment; interpret its absense as $false    

 [bool]$isManagementForest = ($RoleDatacenterIsManagementForest    

-eq $true);    

 if ($RolePrepareAllDomains)    

 {    

 initialize-DomainPermissions -AllDomains:$true    

-CreateTenantRoot:$createTenantRoot -CreateMsoSyncRoot:$createMsoSyncRoot -IsManagementForest:$isManagementForest;    

 }    

elseif ($RoleDomain -ne $null)    

 {    

 initialize-DomainPermissions -Domain $RoleDomain -CreateTenantRoot:$createTenantRoot    

-CreateMsoSyncRoot:$createMsoSyncRoot -IsManagementForest:$isManagementForest;    

 }    

 else    

 {    

initialize-DomainPermissions -CreateTenantRoot:$createTenantRoot -CreateMsoSyncRoot:$createMsoSyncRoot    

-IsManagementForest:$isManagementForest;    

 }    

 " was run: "Microsoft.Exchange.Data.Directory.ADOperationException: Active    

Directory operation failed on DC1.ab.local. This error is not retriable. Additional information: Access is    

denied.    

Active directory response: 00000005: SecErr: DSID-03152612, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0    

 --->    

System.DirectoryServices.Protocols.DirectoryOperationException: The user has insufficient access rights.    

 at    

System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll    

resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)    

 at    

System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)    

 at    

Microsoft.Exchange.Data.Directory.GuardedDirectoryExecution.ExecuteT    

 at Microsoft.Exchange.Data.Directory.PooledLdapConnection.GuardedSendRequest(String forestName,    

GuardedDirectoryExecution guardedDirectoryExecution, DirectoryRequest request, TimeSpan timeout, Func`3     sendRequestDelegate, Int64& concurrency)      at     Microsoft.Exchange.Data.Directory.PooledLdapConnection.SendRequest(DirectoryRequest request, LdapOperation     ldapOperation, Nullable`1 clientSideSearchTimeout, IADLogContext logContext, Boolean shouldLogLastFilter)    

 at    

Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request,    

ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)    

 --- End of inner exception stack trace    

---    

 at Microsoft.Exchange.Data.Directory.ADDataSession.AnalyzeDirectoryError(PooledLdapConnection connection,    

DirectoryRequest request, DirectoryException de, Int32 totalRetries, Int32 retriesOnServer, String callerFilePath,    

Int32 callerFileLine, String memberName)    

 at    

Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request,    

ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)    

 at    

Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean    

bypassValidation)    

 at    

Microsoft.Exchange.Data.Directory.SystemConfiguration.ADConfigurationSession.Save(ADConfigurationObject instanceToSave,    

String callerFilePath, Int32 callerFileLine, String memberName)    

 at    

Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.CreateMonitoringMailboxContainer(MesoContainer meso)    

at Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.InternalProcessRecord()    

 at    

Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()    

 at    

Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean    

terminatePipelineIfFailed)".    

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the    

<SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-14*

Hi,    

My account is    

-domain admin    

-enterprise Admin and Schema admin    

Please add the account to the "Exchange Organization Management role group" as well and see how it goes. See the prerequisites listed in this link.    

If issue persists, it's suggested to follow the steps below and check the result:    

-  Open Group Policy Management on DC, expand domain name, expand the Domain Controllers OU, right click "Default Domain Policy" > Edit> Expand Policies under Computer Configuration > Windows Settings > Security Settings -> Local Policies > User Rights Assignment  >Take ownership of files or other objects    

-  Select "Define these policy settings", add Administrators group, click Apply:    

    

-  Run "Gpupdate /force"    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-14*

Hi,

Please try the below steps,

1.Have you installed all pre-requisites for Exchange 2019 - https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2019  

2.Did you run \Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema - Is it successful?  

3.Try adding the account you are using to "Organization Management" group and run PrepareAD  

4.Enable the Inheritance to the admin account you are using - Go to Active directory users and computers -> Turn on Advanced features: View, Advanced features -> Go to the properties of the user account -> Security tab -> Advanced ->if it says "Disabled inheritance" that means its enabled, otherwise enable it  

5.Re-launch the command prompt and run

If still issue persists, please share the Exchange setup logs as sometimes it could be issue with specific container, for instance Deleted objects  

https://social.technet.microsoft.com/Forums/lync/en-US/36fa5502-36c4-4c9f-9f4f-8507ec777f5b/insuffaccessrights-on-exchange-2013-sp1-during-preparead?forum=exchangesvrdeploy

If the above suggestion helps, please click on "Accept Answer" and upvote it
