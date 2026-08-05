---
title: "Exchange 2019 - Exchange Archive not working for one user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/213323/exchange-2019-exchange-archive-not-working-for-one
question_id: 213323
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 - Exchange Archive not working for one user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/213323/exchange-2019-exchange-archive-not-working-for-one (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have created an retention policy for my organzation, but for one user the archive doest work and stop at 593.77 kB.  

When i check the Export-MailboxdiagnosticLogs username -ComponentName MRM i see the following:

RunspaceId : ef37d437-91b0-43d2-a9a0-91ccdb407091  

MailboxLog : 7/4/2019 6:43:04 AM Exception: Microsoft.Exchange.WorkloadManagement.ResourceUnhealthyException: Resource  

'DiskLatency(Guid:b6fcae1d-62ff-4b2d-9957-f723866e1899 Name:EURPR05DG276-db128 Volume:\?\Volume{d097912  

7-85d5-47d0-a311-87e8b7e67a14})' is unhealthy and shouldn't be accessed.  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCHealthMonitor.InternalThrottleStoreCall(List  

`1 archiveResourceDependencies)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ElcSubAssistant.ThrottleStoreCallAndCheckForShu               tdown(IExchangePrincipal mailboxOwner, List`1 archiveResourceDependencies)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.ProcessFolderContent  

s(IFolder folder, DefaultFolderType folderTypeToCollect, ItemQueryType itemQueryType, AgeLimitAndAction a  

geLimitAndAction)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.ProcessFolderType(De  

faultFolderType defaultFolderType, AgeLimitAndAction ageLimitAndAction)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.CollectItemsToExpire  

()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.CollectItemsWithGuard()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.InvokeInternal()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.Invoke()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerManager.Invoke(MailboxDataFor  

Tags mailboxDataForTags, ElcParameters parameters)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupSubAssistant.Invoke(MailboxSession ma  

ilboxSession, MailboxDataForTags mailboxDataForTags, ElcParameters parameters)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.InvokeCore(MailboxSession mailboxS  

ession, List`1 customDataToLog, StatisticsLogEntry logEntry, ElcParameters parameters)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.<>c__DisplayClass29_0.<InvokeInter               nalAssistant>b__0()                  at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Act  

ion`1 catchDelegate)               5/20/2019 11:44:39 PM Exception: Microsoft.Exchange.WorkloadManagement.ResourceUnhealthyException: Resour               ce 'DiskLatency(Guid:b6fcae1d-62ff-4b2d-9957-f723866e1899 Name:EURPR05DG276-db128 Volume:\\?\Volume{d0979               127-85d5-47d0-a311-87e8b7e67a14}\)' is unhealthy and shouldn't be accessed.                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCHealthMonitor.InternalThrottleStoreCall(List`1 archiveResourceDependencies)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ElcSubAssistant.ThrottleStoreCallAndCheckForShu  

tdown(IExchangePrincipal mailboxOwner, List`1 archiveResourceDependencies)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.TagExpirationExecutor.InternalExpireInBatches(L               ist`1 listToSend, Action retentionActionType, IFolder sourcefolder)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ExpirationExecutor.ExecuteTheDoomed()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.InvokeInternal()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.Invoke()  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerManager.Invoke(MailboxDataFor  

Tags mailboxDataForTags, ElcParameters parameters)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupSubAssistant.Invoke(MailboxSession ma  

ilboxSession, MailboxDataForTags mailboxDataForTags, ElcParameters parameters)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.InvokeCore(MailboxSession mailboxS  

ession, List`1 customDataToLog, StatisticsLogEntry logEntry, ElcParameters parameters)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.<>c__DisplayClass29_0.<InvokeInter               nalAssistant>b__0()                  at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Act  

ion`1 catchDelegate)               4/22/2019 5:31:45 PM Exception: Microsoft.Exchange.WorkloadManagement.ResourceUnhealthyException: Resourc               e 'DiskLatency(Guid:b6fcae1d-62ff-4b2d-9957-f723866e1899 Name:EURPR05DG276-db128 Volume:\\?\Volume{d09791               27-85d5-47d0-a311-87e8b7e67a14}\)' is unhealthy and shouldn't be accessed.                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCHealthMonitor.InternalThrottleStoreCall(List`1 archiveResourceDependencies)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ElcSubAssistant.ThrottleStoreCallAndCheckForShu  

tdown(IExchangePrincipal mailboxOwner, List`1 archiveResourceDependencies)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.ProcessFolderContent               s(IFolder folder, DefaultFolderType folderTypeToCollect, ItemQueryType itemQueryType, AgeLimitAndAction a               geLimitAndAction)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.ProcessFolderType(De               faultFolderType defaultFolderType, AgeLimitAndAction ageLimitAndAction)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.DumpsterExpirationEnforcer.CollectItemsToExpire               ()                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.CollectItemsWithGuard()                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.InvokeInternal()                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerBase.Invoke()                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupEnforcerManager.Invoke(MailboxDataFor               Tags mailboxDataForTags, ElcParameters parameters)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.SysCleanupSubAssistant.Invoke(MailboxSession ma               ilboxSession, MailboxDataForTags mailboxDataForTags, ElcParameters parameters)                  at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.InvokeCore(MailboxSession mailboxS               ession, List`1 customDataToLog, StatisticsLogEntry logEntry, ElcParameters parameters)  

at Microsoft.Exchange.MailboxAssistants.Assistants.ELC.ELCAssistant.<>c__DisplayClass29_0.<InvokeInter  

nalAssistant>b__0()  

at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Act               ion`1 catchDelegate)

LogName : MRM

The user was an Exchange Online User, but we migrated it back to our local on-premis Exchange 2019 Server.  

When i check the logging it looks like he still wants to connect to anExchange Online Server: Name:EURPR05DG276-db128

Anyone any idea how to fix this

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-30*

@Erik Vissers | QNP ICT & Telecom Professionals       

Hi,    

Please refer to this Microsoft KB on archive mailbox issues : Archive mailbox issues for a mailbox that's migrated to or from Office 365    

    

I suppose that Scenario 4 may apply to your situation.    

Please follow the solution provided in the document to see if it can resolve your problem.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
