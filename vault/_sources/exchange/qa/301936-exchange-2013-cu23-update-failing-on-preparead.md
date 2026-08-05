---
title: "Exchange 2013 CU23 update Failing on /PrepareAD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301936/exchange-2013-cu23-update-failing-on-preparead
question_id: 301936
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 CU23 update Failing on /PrepareAD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301936/exchange-2013-cu23-update-failing-on-preparead (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to apply the CU23 update for Exchange 2013 and I am getting the following error. I have looked everywhere for a fix and I cannot find anything.   

03/06/2021 17:22:38.0495] [2] [ERROR] Active Directory operation failed on DC1.removed.local. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=removed,DC=local' already exists.  

[03/06/2021 17:22:38.0495] [2] [ERROR] The object exists.  

[03/06/2021 17:22:38.0511] [2] Ending processing initialize-ExchangeUniversalGroups  

[03/06/2021 17:22:38.0511] [1] The following 1 error(s) occurred during task execution:  

[03/06/2021 17:22:38.0527] [1] 0.  ErrorRecord: Active Directory operation failed on DC1.removed.local. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=removed,DC=local' already exists.  

[03/06/2021 17:22:38.0527] [1] 0.  ErrorRecord: Microsoft.Exchange.Data.Directory.ADObjectEntryAlreadyExistsException: Active Directory operation failed on DC1.removed.local. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=removed,DC=local' already exists. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object exists.  

   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)  

   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.SendRequest(DirectoryRequest request, LdapOperation ldapOperation, Nullable`1 clientSideSearchTimeout, IActivityScope activityScope, String callerInfo)      at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)      --- End of inner exception stack trace ---      at Microsoft.Exchange.Data.Directory.ADDataSession.AnalyzeDirectoryError(PooledLdapConnection connection, DirectoryRequest request, DirectoryException de, Int32 totalRetries, Int32 retriesOnServer)      at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)      at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation)  

   at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADRecipient instanceToSave)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.AddMember(ADObject obj, IRecipientSession session, ADGroup destGroup, WriteVerboseDelegate writeVerbose)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateAndValidateRoleGroups(ADOrganizationalUnit usgContainer, RoleGroupCollection roleGroups)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)  

[03/06/2021 17:22:38.0527] [1] [ERROR] The following error was generated when "$error.Clear();   

	initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions

" was run: "Microsoft.Exchange.Data.Directory.ADObjectEntryAlreadyExistsException: Active Directory operation failed on DC1.removed.local. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=removed,DC=local' already exists. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object exists.  

   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnTimeOut)  

   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)  

   at Microsoft.Exchange.Data.Directory.PooledLdapConnection.SendRequest(DirectoryRequest request, LdapOperation ldapOperation, Nullable`1 clientSideSearchTimeout, IActivityScope activityScope, String callerInfo)      at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)      --- End of inner exception stack trace ---      at Microsoft.Exchange.Data.Directory.ADDataSession.AnalyzeDirectoryError(PooledLdapConnection connection, DirectoryRequest request, DirectoryException de, Int32 totalRetries, Int32 retriesOnServer)      at Microsoft.Exchange.Data.Directory.ADDataSession.ExecuteModificationRequest(ADObject entry, DirectoryRequest request, ADObjectId originalId, Boolean emptyObjectSessionOnException, Boolean isSync)      at Microsoft.Exchange.Data.Directory.ADDataSession.Save(ADObject instanceToSave, IEnumerable`1 properties, Boolean bypassValidation)  

   at Microsoft.Exchange.Data.Directory.Recipient.ADRecipientObjectSession.Save(ADRecipient instanceToSave)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.AddMember(ADObject obj, IRecipientSession session, ADGroup destGroup, WriteVerboseDelegate writeVerbose)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateAndValidateRoleGroups(ADOrganizationalUnit usgContainer, RoleGroupCollection roleGroups)  

   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  

[03/06/2021 17:22:38.0527] [1] [ERROR] Active Directory operation failed on DC1.removed.local. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=removed,DC=local' already exists.  

[03/06/2021 17:22:38.0527] [1] [ERROR] The object exists.  

[03/06/2021 17:22:38.0527] [1] [ERROR-REFERENCE] Id=443949901 Component=  

[03/06/2021 17:22:38.0527] [1] Setup is stopping now because of one or more critical errors.  

[03/06/2021 17:22:38.0527] [1] Finished executing component tasks.  

[03/06/2021 17:22:38.0527] [1] Ending processing Install-ExchangeOrganization  

[03/06/2021 17:22:38.0527] [0] CurrentResult console.ProcessRunInternal:198: 1  

[03/06/2021 17:22:38.0542] [0] CurrentResult launcherbase.maincore:90: 1  

[03/06/2021 17:22:38.0542] [0] CurrentResult console.startmain:52: 1  

[03/06/2021 17:22:38.0542] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1  

[03/06/2021 17:22:38.0542] [0] The Exchange Server setup operation didn't complete.  More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

[03/06/2021 17:22:38.0542] [0] CurrentResult main.run:235: 1  

[03/06/2021 17:22:38.0542] [0] The registry key, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\V15\Setup, wasn't found.  

[03/06/2021 17:22:38.0542] [0] CurrentResult setupbase.maincore:396: 1  

[03/06/2021 17:22:38.0542] [0] End of Setup

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-11*

Hi @Michael Houston        

This applies to all versions of Exchange:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/setup/ex2019-setup-does-not-run-correctly-started-powershell

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-11*

Thanks for all the responses.  I am not sure why, but when running setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms from an elevated Power Shell, I was getting the error, but when I tried running from a Command Prompt, it worked.  

If anyone knows why, please let me know.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-08*

Hi @Michael Houston  ,    

From the error you shared, it seems that the issue could be related to the "Microsoft Exchange Security Groups".      

Do you have multiple OUs in your environment and have by any chance moved the "Microsoft Exchange Security Groups" out from the root to a different OU? Also you can have a look at the thread below and see if the solution there can be helpful:    

New Exchange 2013 (CU13) Install- failing after prepareschema, preparead and preparealldomains succeeded    

In case the error persists, it's suggested to create a backup of AD, then follow the links below to recreate the Exchange Security Groups:    

Exchange 2019 - Re-create the Exchange Security Groups in AD    

How to Recreate Corrupted Microsoft Security Groups in Exchange 2010    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-07*

What version are you updating from? There are only schema changes if you're upgrading from CU6 or earlier.    

https://learn.microsoft.com/en-us/exchange/exchange-2013-active-directory-schema-changes-exchange-2013-help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-06*

Have your tried downloading the update and running it with the EA (enterprise admin) account as it looks like it is trying to update the schema?
