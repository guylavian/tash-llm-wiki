---
title: "Microsoft Exchange Hybrid Configuration Wizard fails to uninstall Agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3261850/microsoft-exchange-hybrid-configuration-wizard-fai
question_id: 3261850
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 11
qa_tags: []
---
# Microsoft Exchange Hybrid Configuration Wizard fails to uninstall Agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3261850/microsoft-exchange-hybrid-configuration-wizard-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

i have a problem with the Exchange Hybrid Configuration Wizard. Wanted to change configuration from "Modern" to "Classic" which should uninstall the Hybrid Agent. Unfortunately the Uninstall stucks and cant complete the wizard. In the log file there is this
 failure:  

*ERROR* 10343 [Client=UX, Page=HybridConnectorInstall, Thread=14]   

System.AggregateException: One or more errors occurred. ---> System.NullReferenceException: Object reference not set to an instance of an object.  

at Microsoft.Online.CSE.Hybrid.App.Interop.HybridConnectorInstaller.<UninstallConnectorAgentAsync>d__63.MoveNext()  

--- End of inner exception stack trace ---  

at System.Threading.Tasks.Task.ThrowIfExceptional(Boolean includeTaskCanceledExceptions)  

at System.Threading.Tasks.Task.Wait(Int32 millisecondsTimeout, CancellationToken cancellationToken)  

at Microsoft.Online.CSE.Hybrid.App.ViewModel.Pages.HybridConnectorInstall.AsyncUnInstallInternal(CancellationToken cancellationToken)  

at Microsoft.Online.CSE.Hybrid.App.ViewModel.Pages.HybridConnectorInstall.AsyncMainInternal(CancellationToken cancellationToken)  

at Microsoft.Online.CSE.Hybrid.App.ViewModel.Pages.HybridConnectorInstall.AsyncMain(CancellationToken cancellationToken)  

---> (Inner Exception #0) System.NullReferenceException: Object reference not set to an instance of an object.  

 at Microsoft.Online.CSE.Hybrid.App.Interop.HybridConnectorInstaller.<UninstallConnectorAgentAsync>d__63.MoveNext()<---  

Tried with restarting Server (Exchange 2016 on Windows Server 2016), but still the same. Has anybody have the same problem and could solve it?  

Thank you  

Georgios

## Answers

_No answers on this thread._
