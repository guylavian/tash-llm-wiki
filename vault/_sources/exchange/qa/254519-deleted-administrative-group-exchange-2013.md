---
title: "Deleted Administrative group exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/254519/deleted-administrative-group-exchange-2013
question_id: 254519
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Deleted Administrative group exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/254519/deleted-administrative-group-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After a former administrator deleted several security groups involving exchange wellknown objects. We tried to recover executing prepad.

Prepad failed for a ACL overflow:

[01/24/2021 17:30:48.0403] [2] [ERROR] Length of the access control list exceed the allowed maximum.  

[01/24/2021 17:30:48.0403] [2] [WARNING] An unexpected error has occurred and a Watson dump is being generated: Length of the access control list exceed the allowed maximum.  

01/24/2021 17:30:50.0794 The following 1 error(s) occurred during task execution:  

01/24/2021 17:30:50.0810 0. ErrorRecord: Length of the access control list exceed the allowed maximum.  

01/24/2021 17:30:50.0810 0. ErrorRecord: System.OverflowException: Length of the access control list exceed the allowed maximum.  

at System.Security.AccessControl.RawAcl.InsertAce(Int32 index, GenericAce ace)  

at System.Security.AccessControl.CommonAcl.AddQualifiedAce(SecurityIdentifier sid, AceQualifier qualifier, Int32 accessMask, AceFlags flags, ObjectAceFlags objectFlags, Guid objectType, Guid inheritedObjectType)  

at System.Security.AccessControl.DiscretionaryAcl.AddAccess(AccessControlType accessType, SecurityIdentifier sid, Int32 accessMask, InheritanceFlags inheritanceFlags, PropagationFlags propagationFlags, ObjectAceFlags objectFlags, Guid objectType, Guid inheritedObjectType)  

at System.Security.AccessControl.DirectoryObjectSecurity.ModifyAccess(AccessControlModification modification, ObjectAccessRule rule, Boolean& modified)  

at System.Security.AccessControl.DirectoryObjectSecurity.AddAccessRule(ObjectAccessRule rule)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.ApplyAcesOnAcl(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, String objectIdentityString, ActiveDirectorySecurity acl, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.ApplyAcesOnSd(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, ADObjectId id, RawSecurityDescriptor rsd, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.SetAces(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, ADObject obj, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)  

at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)  

at Microsoft.Exchange.Configuration.Tasks.Task.ProcessRecord()  

at System.Management.Automation.CommandProcessor.ProcessRecord()  

01/24/2021 17:30:50.0810 [ERROR] The following error was generated when "$error.Clear();  

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

" was run: "System.OverflowException: Length of the access control list exceed the allowed maximum.  

at System.Security.AccessControl.RawAcl.InsertAce(Int32 index, GenericAce ace)  

at System.Security.AccessControl.CommonAcl.AddQualifiedAce(SecurityIdentifier sid, AceQualifier qualifier, Int32 accessMask, AceFlags flags, ObjectAceFlags objectFlags, Guid objectType, Guid inheritedObjectType)  

at System.Security.AccessControl.DiscretionaryAcl.AddAccess(AccessControlType accessType, SecurityIdentifier sid, Int32 accessMask, InheritanceFlags inheritanceFlags, PropagationFlags propagationFlags, ObjectAceFlags objectFlags, Guid objectType, Guid inheritedObjectType)  

at System.Security.AccessControl.DirectoryObjectSecurity.ModifyAccess(AccessControlModification modification, ObjectAccessRule rule, Boolean& modified)  

at System.Security.AccessControl.DirectoryObjectSecurity.AddAccessRule(ObjectAccessRule rule)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.ApplyAcesOnAcl(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, String objectIdentityString, ActiveDirectorySecurity acl, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.ApplyAcesOnSd(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, ADObjectId id, RawSecurityDescriptor rsd, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.DirectoryCommon.SetAces(TaskVerboseLoggingDelegate verboseLogger, TaskWarningLoggingDelegate warningLogger, ErrorLoggerDelegate errorLogger, ADObject obj, Boolean remove, ActiveDirectoryAccessRule[] aces)  

at Microsoft.Exchange.Management.Tasks.InitializeDomainPermissions.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)  

at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)

After been unable to complete the prepad run, we got our management groups duplicated with no roles asigned to them:  

Does anyone know if there a way to manually assign the roles to the new group?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-02*

Hi, @Allan Ruiz       

From the screenshot, it seems the default "Organization Management" role group was deleted.    

You may refer to this document about the detailed information of the roles assigned to this group: Organization Management    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-01*

You can click on that and add the roles.    

Double Click on the role and hit the plus side to add
