---
title: "uninstall exchange 2016 after migrating to exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/417144/uninstall-exchange-2016-after-migrating-to-exchang
question_id: 417144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# uninstall exchange 2016 after migrating to exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/417144/uninstall-exchange-2016-after-migrating-to-exchang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

during the first attempt to uninstall exchange 2016 i got this error:  

"": "Microsoft.Exchange.Configuration.Tasks.ServiceStopFailureException: Unable to stop service 'MSExchangeUM'. Error: 'Unable to stop MSExchangeUM service on computer'. '.'. ---> System.InvalidOperationException: Unable to stop service MSExchangeUM on computer '.'. ---> System.ComponentModel.Win32Exception: Service not started  

   --- End of inner exception stack trace ---  

   in System.ServiceProcess.ServiceController.Stop ()  

   in Microsoft.Exchange.Management.Tasks.ManageSetupService.StopService (ServiceController serviceController, Boolean ignoreServiceStopTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime)      --- End of inner exception stack trace ---      in Microsoft.Exchange.Configuration.Tasks.Task.ThrowError (Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)      in Microsoft.Exchange.Configuration.Tasks.Task.WriteError (Exception exception, ErrorCategory category, Object target)      in Microsoft.Exchange.Management.Tasks.ManageSetupService.StopService (ServiceController serviceController, Boolean ignoreServiceStopTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime)  

   in Microsoft.Exchange.Management.Tasks.ManageSetupService.StopService (String serviceName, Boolean ignoreServiceStopTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime)  

   in Microsoft.Exchange.Management.Tasks.StopSetupService.InternalProcessRecord ()  

   in Microsoft.Exchange.Configuration.Tasks.Task. <ProcessRecord> b__91_1 ()  

   in Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc (String funcName, Action func, Boolean terminatePipelineIfFailed) "."  

after a restart of the server and if I try again to uninstall exchange 2016 from the control panel I get this error:  

An incomplete installation was detected. run the installer to complete the exchange setup  

while if I try with:  

Setup / mode: uninstall / IAcceptExchangeServerLicenseTerms  

I get this error:  

Unable to complete the uninstall operation because there are open files in powershell (11780).  

Close the process and restart the installation.  

For more information, please visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.ProcessNeedsToBeClosedOnUninstall.aspx

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-02*

Hi @Luca Zibelli   ,    

As you have started the services, I think you could directly uninstall Exchange now.    

And the error you met, Unable to complete the uninstall operation because there are open files in powershell (11780), it is because the process 11780 is related with Exchange server. It may be a OWA or EAC page opened in a browser or other processes. You could restart the server and use powershell cmd to unisntall it or find the related process on Task Manager and end that task.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
