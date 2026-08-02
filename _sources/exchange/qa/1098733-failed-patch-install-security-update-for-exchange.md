---
title: "Failed Patch Install Security Update For Exchange Server 2016 CU23 (KB5019077)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1098733/failed-patch-install-security-update-for-exchange
question_id: 1098733
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Failed Patch Install Security Update For Exchange Server 2016 CU23 (KB5019077)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1098733/failed-patch-install-security-update-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We had a failed Exchange Server 2016 update last night, Security Update for Exchange Server 2016 CU23 (KB5019077). This morning we had to change all exchange services from disabled to enabled but the "Microsoft Filtering Management Service" will not start. Which stops all other exchange services from starting.    

We have tried copying the configurationserver.xml from the CU23 ISO, and also from another working 2016 Cu23 server but still it won't start.    

I've attempted some of the repairs in https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues#services-dont-start-after-su-installation  but keep hitting dead ends.    

All updates that installed last night    

Success - 2022-10 Cumulative Update for Windows Server 2016 for x64-based Systems (KB5018411)    

Failed - Security Update For Exchange Server 2016 CU23 (KB5019077)    

Success - Windows Malicious Software Removal Tool x64 - v5.106 (KB890830)    

Success - 2022-10 Cumulative Update for .NET Framework 4.8 for Windows Server 2016 for x64 (KB5018515)    

I have been able to uninstall 2022-10 Cumulative Update for .NET Framework 4.8 for Windows Server 2016 for x64 (KB5018515) but it hasn't made any difference.    

Below is a copy of the ServiceControl.log showing last nights failed auto patch, and an attempt to reinstall the patch this afternoon.    

Any help or advice/next steps would be greatly welcomed. We have database backups so worst case we can rebuild or possibly move the client to 365 but would like to repair if possible.    

Thanks    

```
[00:50:54] -----------------------------------------------   
  
[00:50:54] * ServiceControl.ps1: 21/11/2022 00:50:54   
  
[00:50:54] Performing service control with options:    
  
[00:50:56] Saving service and registry data   
  
[00:50:56] State file C:\ExchangeSetupLogs\ServiceState.xml already exists.   
  
[00:50:56] Overwrite is specified. File C:\ExchangeSetupLogs\ServiceState.xml is going to be overwritten with a new state.   
  
[00:50:56] Saving service state to 'C:\ExchangeSetupLogs\ServiceState.xml'...   
  
[00:50:58] State file C:\ExchangeSetupLogs\ServiceStartupMode.xml already exists.   
  
[00:50:58] Overwrite is specified. File C:\ExchangeSetupLogs\ServiceStartupMode.xml is going to be overwritten with a new state.   
  
[00:50:58] Saving services startup mode.   
  
[00:50:59] Adding to installed roles list: AdminTools   
  
[00:50:59] Adding to installed roles list: ClientAccessMailboxRole   
  
[00:50:59] Adding to installed roles list: Mailbox   
  
[00:50:59] Adding to installed roles list: Bridgehead   
  
[00:50:59] Adding to installed roles list: Mailbox   
  
[00:50:59] Adding to installed roles list: UnifiedMessaging   
  
[00:50:59] Stopping services for the following roles: AdminTools ClientAccess FrontendTransport Bridgehead Mailbox UnifiedMessaging   
  
[00:50:59] Stopping services for 'AdminTools ClientAccess FrontendTransport Bridgehead Mailbox UnifiedMessaging'...   
  
[00:50:59] Stopping service 'WinMgmt'.   
  
[00:51:10] Stopping service 'W3Svc'.   
  
[00:52:41] Stopping service 'pla'.   
  
[00:52:41] Stopping service 'MSExchangeUM'.   
  
[00:52:55] Stopping service 'MSExchangeTransportLogSearch'.   
  
[00:52:55] Stopping service 'MSExchangeTransport'.   
  
[00:53:12] Stopping service 'MSExchangeThrottling'.   
  
[00:53:15] Stopping service 'MSExchangeSubmission'.   
  
[00:53:28] Stopping service 'MSExchangeServiceHost'.   
  
[00:53:30] Stopping service 'MSExchangeRPC'.   
  
[00:53:31] Stopping service 'MSExchangeRepl'.   
  
[00:53:42] Stopping service 'MSExchangePOP3BE'.   
  
[00:53:43] Stopping service 'MSExchangePOP3'.   
  
[00:53:44] Stopping service 'MSExchangeMailboxReplication'.   
  
[00:58:46] Stopping service 'MSExchangeMailboxAssistants'.   
  
[00:58:46] Stopping service 'MSExchangeIS'.   
  
[00:59:00] Stopping service 'MSExchangeIMAP4BE'.   
  
[00:59:01] Stopping service 'MSExchangeIMAP4'.   
  
[00:59:02] Stopping service 'MSExchangeHMRecovery'.   
  
[00:59:02] Stopping service 'MSExchangeHM'.   
  
[00:59:03] Stopping service 'MSExchangeFrontendTransport'.   
  
[00:59:14] Stopping service 'MSExchangeFastSearch'.   
  
[00:59:14] Stopping service 'MSExchangeEdgeSync'.   
  
[00:59:15] Stopping service 'MSExchangeDiagnostics'.   
  
[00:59:15] Stopping service 'MSExchangeDelivery'.   
  
[00:59:26] Stopping service 'MSExchangeDagMgmt'.   
  
[00:59:26] Stopping service 'MSExchangeAntispamUpdate'.   
  
[00:59:26] Stopping service 'MSExchangeADTopology'.   
  
[01:00:01] Stopping service 'IISAdmin'.   
  
[01:00:07] Stopping service 'hostcontrollerservice'.   
  
[01:00:41] Killing instead of Stopping 'FMS'.   
  
[01:00:41] Disabling services for 'AdminTools ClientAccess FrontendTransport Bridgehead Mailbox UnifiedMessaging'...   
  
[01:00:41] Disabling service 'FMS'.   
  
[01:00:41] Disabling service 'hostcontrollerservice'.   
  
[01:00:41] Disabling service 'IISAdmin'.   
  
[01:00:41] Disabling service 'MSExchangeADTopology'.   
  
[01:00:41] Disabling service 'MSExchangeAntispamUpdate'.   
  
[01:00:41] Disabling service 'MSExchangeDagMgmt'.   
  
[01:00:41] Disabling service 'MSExchangeDelivery'.   
  
[01:00:41] Disabling service 'MSExchangeDiagnostics'.   
  
[01:00:41] Disabling service 'MSExchangeEdgeSync'.   
  
[01:00:41] Disabling service 'MSExchangeFastSearch'.   
  
[01:00:41] Disabling service 'MSExchangeFrontendTransport'.   
  
[01:00:41] Disabling service 'MSExchangeHM'.   
  
[01:00:41] Disabling service 'MSExchangeHMRecovery'.   
  
[01:00:41] Disabling service 'MSExchangeIMAP4'.   
  
[01:00:41] Disabling service 'MSExchangeIMAP4BE'.   
  
[01:00:41] Disabling service 'MSExchangeIS'.   
  
[01:00:41] Disabling service 'MSExchangeMailboxAssistants'.   
  
[01:00:41] Disabling service 'MSExchangeMailboxReplication'.   
  
[01:00:41] Disabling service 'MSExchangePOP3'.   
  
[01:00:41] Disabling service 'MSExchangePOP3BE'.   
  
[01:00:41] Disabling service 'MSExchangeRepl'.   
  
[01:00:41] Disabling service 'MSExchangeRPC'.   
  
[01:00:41] Disabling service 'MSExchangeServiceHost'.   
  
[01:00:41] Disabling service 'MSExchangeSubmission'.   
  
[01:00:41] Disabling service 'MSExchangeThrottling'.   
  
[01:00:41] Disabling service 'MSExchangeTransport'.   
  
[01:00:41] Disabling service 'MSExchangeTransportLogSearch'.   
  
[01:00:41] Disabling service 'MSExchangeUM'.   
  
[01:00:41] Disabling service 'pla'.   
  
[01:00:41] Disabling service 'RemoteRegistry'.   
  
[01:00:41] Disabling service 'SearchExchangeTracing'.   
  
[01:00:41] Disabling service 'W3Svc'.   
  
[01:00:41] Disabling service 'WinMgmt'.   
  
[01:00:41] Disabling service 'wsbexchange'.   
  
[01:00:41] Script completed succesfully.   
  
[17:15:24] -----------------------------------------------   
  
[17:15:24] * ServiceControl.ps1: 21/11/2022 17:15:24   
  
[17:15:24] Performing service control with options:    
  
[17:15:24] Saving service and registry data   
  
[17:15:24] State file C:\ExchangeSetupLogs\ServiceState.xml already exists.   
  
[17:15:24] Overwrite is specified. File C:\ExchangeSetupLogs\ServiceState.xml is going to be overwritten with a new state.   
  
[17:15:24] Saving service state to 'C:\ExchangeSetupLogs\ServiceState.xml'...   
  
[17:15:26] State file C:\ExchangeSetupLogs\ServiceStartupMode.xml already exists.   
  
[17:15:26] Overwrite is specified. File C:\ExchangeSetupLogs\ServiceStartupMode.xml is going to be overwritten with a new state.   
  
[17:15:26] Saving services startup mode.   
  
[17:15:26] Adding to installed roles list: AdminTools   
  
[17:15:26] Adding to installed roles list: ClientAccessMailboxRole   
  
[17:15:26] Adding to installed roles list: Mailbox   
  
[17:15:26] Adding to installed roles list: Bridgehead   
  
[17:15:26] Adding to installed roles list: Mailbox   
  
[17:15:26] Adding to installed roles list: UnifiedMessaging   
  
[17:15:26] Stopping services for the following roles: AdminTools ClientAccess FrontendTransport Bridgehead Mailbox UnifiedMessaging   
  
[17:15:26] Stopping services for 'AdminTools ClientAccess FrontendTransport Bridgehead Mailbox UnifiedMessaging'...   
  
[17:15:27] Stopping service 'WinMgmt'.   
  
[17:15:27] [Error] System.Management.Automation.CommandNotFoundException: The term 'Stop-SetupService' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.   
  
   at System.Management.Automation.ExceptionHandlingOps.CheckActionPreference(FunctionContext funcContext, Exception exception)   
  
   at System.Management.Automation.Interpreter.ActionCallInstruction`2.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.Interpreter.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.LightLambda.RunVoid1[T0](T0 arg0)   
  
   at System.Management.Automation.DlrScriptCommandProcessor.RunClause(Action`1 clause, Object dollarUnderbar, Object inputToProcess)   
  
--- End of stack trace from previous location where exception was thrown ---   
  
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()   
  
   at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)   
  
   at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)   
  
   at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)   
  
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-22*

Thank you LilyLi2-MSFT, I did your process using the Security Update For Exchange Server 2016 CU23 (KB5019758) and it worked like a charm.    

imamitsingh, thank you for your response

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-22*

Here is a Microsoft doc about the common issues during the update process: Repair failed installations of Exchange Cumulative and Security updates     

Also, check these helpful links for help -     

https://www.reddit.com/r/exchangeserver/comments/v0xj3a/exchange_2016_cu_23_update_failed/     

https://www.stellarinfo.com/article/install-exchange-cumulative-updates.php
