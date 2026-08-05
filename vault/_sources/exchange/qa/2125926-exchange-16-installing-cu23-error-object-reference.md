---
title: "Exchange 16 installing CU23 error \"Object reference not set to an instance of an object\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125926/exchange-16-installing-cu23-error-object-reference
question_id: 2125926
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange 16 installing CU23 error "Object reference not set to an instance of an object"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125926/exchange-16-installing-cu23-error-object-reference (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

trying to install CU23 (currently on CU20, I believe) on an on-prem exchange server in hybrid online configuration

getting the error message on Step 1: Organization Preparation

Error:

The following error was generated when "$error.Clear(); 
initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions
" was run: "System.NullReferenceException: Object reference not set to an instance of an object.
   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateOrMoveEWPGroup(ADGroup ewp, ADOrganizationalUnit usgContainer)
   at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)
   at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)
   at Microsoft.Exchange.Configuration.Tasks.Task.ProcessRecord()
   at System.Management.Automation.CommandProcessor.ProcessRecord()".

last part of exchangesetuplog:

[12/02/2024 23:54:28.0268] [2] Used domain controller DC.XXX.XXX to read object CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,OU=Mystery People,DC=Apache,DC=County.
[12/02/2024 23:54:28.0268] [2] Used domain controller DC.XXX.XXX to read object CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,OU=Mystery People,DC=Apache,DC=County.
[12/02/2024 23:54:28.0268] [2] Used domain controller DC.XXX.XXX to read object CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,OU=Mystery People,DC=Apache,DC=County.
[12/02/2024 23:54:28.0268] [2] Group CN=Managed Availability Servers,OU=Microsoft Exchange Security Groups,OU=Mystery People,DC=Apache,DC=County already exists.
[12/02/2024 23:54:28.0273] [2] [ERROR] Object reference not set to an instance of an object.
[12/02/2024 23:54:28.0283] [2] [WARNING] An unexpected error has occurred and a Watson dump is being generated: Object reference not set to an instance of an object.
[12/02/2024 23:54:29.0777] [1] The following 1 error(s) occurred during task execution:
[12/02/2024 23:54:29.0778] [1] 0. ErrorRecord: Object reference not set to an instance of an object.
[12/02/2024 23:54:29.0778] [1] 0. ErrorRecord: System.NullReferenceException: Object reference not set to an instance of an object.
at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateOrMoveEWPGroup(ADGroup ewp, ADOrganizationalUnit usgContainer)
at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()
at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)
at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)
at Microsoft.Exchange.Configuration.Tasks.Task.ProcessRecord()
at System.Management.Automation.CommandProcessor.ProcessRecord()
[12/02/2024 23:54:29.0779] [1] [ERROR] The following error was generated when "$error.Clear();
initialize-ExchangeUniversalGroups -DomainController $RoleDomainController -ActiveDirectorySplitPermissions $RoleActiveDirectorySplitPermissions
" was run: "System.NullReferenceException: Object reference not set to an instance of an object.
at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.CreateOrMoveEWPGroup(ADGroup ewp, ADOrganizationalUnit usgContainer)
at Microsoft.Exchange.Management.Tasks.InitializeExchangeUniversalGroups.InternalProcessRecord()
at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)
at Microsoft.Exchange.Configuration.Tasks.Task.ProcessTaskStage(TaskStage taskStage, Action initFunc, Action mainFunc, Action completeFunc)
at Microsoft.Exchange.Configuration.Tasks.Task.ProcessRecord()
at System.Management.Automation.CommandProcessor.ProcessRecord()".
[12/02/2024 23:54:29.0779] [1] [ERROR] Object reference not set to an instance of an object.
[12/02/2024 23:54:29.0780] [1] [ERROR-REFERENCE] Id=443949901 Component=
[12/02/2024 23:54:29.0780] [1] Setup is stopping now because of one or more critical errors.
[12/02/2024 23:54:29.0780] [1] Finished executing component tasks.
[12/02/2024 23:54:29.0793] [1] Ending processing Install-ExchangeOrganization
[12/02/2024 23:58:35.0104] [0] CurrentResult setupbase.maincore:396: 0
[12/02/2024 23:58:35.0105] [0] End of Setup
[12/02/2024 23:58:35.0105] [0] **********************************************

I inherited this server/exchange environment with the note 'exchange server has update issue' :|
I'm not seeing what is missing from these logs. Any help would be appreciated.('Computers' OU does exist, this is the only related solution I could find)

## Answers

_No answers on this thread._
