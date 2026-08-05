---
title: "MSExchangeDagMgmt won't start after upgrade Echange 2016 cu17 to cu18 ."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/187901/msexchangedagmgmt-wont-start-after-upgrade-echange
question_id: 187901
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# MSExchangeDagMgmt won't start after upgrade Echange 2016 cu17 to cu18 .

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/187901/msexchangedagmgmt-wont-start-after-upgrade-echange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.  

I have 4 serveurs on my DAG .  

The fisrt 3 upgrade succefully to CU18.  

But the last seem to not upgrade completly.  

Ater rester DAG service " MSExchangeDagMgmt" Won't start .  

I have try to launch the CU18 setup again and he don't finish .  

The databases seem to replicate correctly, but can't be active ion this server.  

In event log i have:  

Watson report about to be sent for process id: 30524, with parameters: E12, c-RTL-AMD64, 15.01.2106.002, MSExchangeDagMgmt, MSExchangeDagMgmt, M.E.C.D.DagComponentManager..ctor, System.TypeInitializationException, 2c86-dumptidset, 15.01.2106.002.  

ErrorReportingEnabled: False   

On exchange CU18 setup ( E:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Upgrade):  

Configuring Microsoft Exchange Server  

```
Language Files                                                                                                                                                COMPLETED
Restoring Services                                                                                                                                            COMPLETED
Language Configuration                                                                                                                                        COMPLETED
Exchange Management Tools                                                                                                                                     COMPLETED
Mailbox role: Transport service                                                                                                                               COMPLETED
Mailbox role: Client Access service                                                                                                                           COMPLETED
Mailbox role: Unified Messaging service                                                                                                                       COMPLETED
Mailbox role: Mailbox service                                                                                                                                 FAILED
```

The following error was generated when "$error.Clear();  

 start-SetupService -ServiceName MSExchangeDagMgmt  

" was run:  

"Microsoft.Exchange.Configuration.Tasks.ServiceDidNotReachStatusException: Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

 at  

Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

 at  

Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)  

 at  

Microsoft.Exchange.Management.Tasks.ManageSetupService.WaitForServiceStatus(ServiceController serviceController, ServiceControllerStatus status, Unlimited`1 maximumWaitTime,   Boolean ignoreFailures, Boolean sendWatsonReportForHungService)    at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(ServiceController serviceController,   Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)  

 at  

Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(String serviceName, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1  

maximumWaitTime, String[] serviceParameters)  

 at Microsoft.Exchange.Management.Tasks.StartSetupService.InternalProcessRecord()  

 at  

Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

 at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean  

terminatePipelineIfFailed)".  

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

And in the ExchangeSetup.log:  

[12/06/2020 11:54:30.0417] [2] [WARNING] Service checkpoint has not progressed. Previous checkpoint='0'- Current checkpoint='0'.  

[12/06/2020 11:54:30.0417] [2] Previous service status query time is '06/12/2020 12:54:05'.  

[12/06/2020 11:54:30.0417] [2] Current service status query time is '06/12/2020 12:54:30'.  

[12/06/2020 11:54:30.0417] [2] Will wait '25000' milliseconds for the service 'MSExchangeDagMgmt' to reach status 'Running'.  

[12/06/2020 11:54:55.0447] [2] Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server after waiting for '25000' milliseconds.  

[12/06/2020 11:54:55.0450] [2] Service Control Manager reports no process ID for service MSExchangeDagMgmt.  

[12/06/2020 11:54:55.0462] [2] Unable to get the process ID for service MSExchangeDagMgmt because another similar process 0 was found  

[12/06/2020 11:54:55.0462] [2] [ERROR] Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

[12/06/2020 11:54:55.0463] [2] [ERROR] Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

[12/06/2020 11:54:55.0465] [2] Ending processing start-SetupService  

[12/06/2020 11:54:55.0466] [1] The following 1 error(s) occurred during task execution:  

[12/06/2020 11:54:55.0466] [1] 0.  ErrorRecord: Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

[12/06/2020 11:54:55.0466] [1] 0.  ErrorRecord: Microsoft.Exchange.Configuration.Tasks.ServiceDidNotReachStatusException: Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)  

   at Microsoft.Exchange.Management.Tasks.ManageSetupService.WaitForServiceStatus(ServiceController serviceController, ServiceControllerStatus status, Unlimited`1 maximumWaitTime, Boolean ignoreFailures, Boolean sendWatsonReportForHungService)      at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(ServiceController serviceController, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)  

   at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(String serviceName, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)  

   at Microsoft.Exchange.Management.Tasks.StartSetupService.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)  

[12/06/2020 11:54:55.0467] [1] [ERROR] The following error was generated when "$error.Clear();   

	start-SetupService -ServiceName MSExchangeDagMgmt

" was run: "Microsoft.Exchange.Configuration.Tasks.ServiceDidNotReachStatusException: Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

   at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)  

   at Microsoft.Exchange.Management.Tasks.ManageSetupService.WaitForServiceStatus(ServiceController serviceController, ServiceControllerStatus status, Unlimited`1 maximumWaitTime, Boolean ignoreFailures, Boolean sendWatsonReportForHungService)      at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(ServiceController serviceController, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)  

   at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(String serviceName, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)  

   at Microsoft.Exchange.Management.Tasks.StartSetupService.InternalProcessRecord()  

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".  

[12/06/2020 11:54:55.0467] [1] [ERROR] Service 'MSExchangeDagMgmt' failed to reach status 'Running' on this server.  

[12/06/2020 11:54:55.0468] [1] [ERROR-REFERENCE] Id=MailboxServiceControlLast___2BE75C4DA081420B9B78009DB6C8CDFA Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[12/06/2020 11:54:55.0468] [1] Setup is stopping now because of one or more critical errors.  

[12/06/2020 11:54:55.0468] [1] Finished executing component tasks.  

[12/06/2020 11:54:55.0476] [1] Ending processing Install-MailboxRole  

[12/06/2020 11:54:55.0481] [0] CurrentResult console.ProcessRunInternal:198: 1  

[12/06/2020 11:54:55.0485] [0] CurrentResult launcherbase.maincore:90: 1  

[12/06/2020 11:54:55.0485] [0] CurrentResult console.startmain:52: 1  

[12/06/2020 11:54:55.0486] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1  

[12/06/2020 11:54:55.0486] [0] The Exchange Server setup operation didn't complete.  More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

[12/06/2020 11:54:55.0486] [0] CurrentResult main.run:235: 1  

[12/06/2020 11:54:55.0486] [0] CurrentResult setupbase.maincore:396: 1  

[12/06/2020 11:54:55.0487] [0] End of Setup  

[12/06/2020 11:54:55.0487] [0] **********************************************

## Answers

_No answers on this thread._
