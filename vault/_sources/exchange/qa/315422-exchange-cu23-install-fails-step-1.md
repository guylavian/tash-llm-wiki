---
title: "Exchange CU23 install fails step 1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315422/exchange-cu23-install-fails-step-1
question_id: 315422
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange CU23 install fails step 1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315422/exchange-cu23-install-fails-step-1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

has anyone come across this error during setup of Exchange 2013 CU23?  

FAILEDAT STEP 1 OF 18   

Error: The following error was generated when "$error.Clear(); initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions   

" was run: "Microsoft.Exchange.Management.Tasks.InvalidWKObjectTargetException: The well-known object entry with the GUID "bec6ddb3-3b2a-4be8-97eb-2dce9477e389", which is on the "CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=DOMAIN,DC=ca" container object's otherWellKnownObjects attribute, refers to a group "CN=Help Desk,OU=Information Technology,DC=DOMAIN,DC=ca" of the wrong group type. Either delete the well-known object entry, or promote the target object to "Universal, SecurityEnabled". at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl) at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateGroup(ADOrganizationalUnit usgContainer, String groupName, Int32 groupId, Guid wkGuid, String groupDescription, GroupTypeFlags groupType, Boolean createAsRoleGroup) at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateRoleGroup(ADOrganizationalUnit usgContainer, RoleGroupDefinition roleGroup) at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateAndValidateRoleGroups(ADOrganizationalUnit usgContainer, RoleGroupCollection roleGroups) at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answers

_No answers on this thread._
