---
title: "Problem during Exchange 2019 setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2103279/problem-during-exchange-2019-setup
question_id: 2103279
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Problem during Exchange 2019 setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2103279/problem-during-exchange-2019-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I am adding an Exchange 2019 server to an organization that already has Exchange servers.

An error occurs during installation.

I see error messages in the event logЖ  

Source: MSExchange CmdletLogs

ID: 6

Cmdlet failed. Cmdlet Configure-WSManIISHosting, parameters -EnableKerberosModule "True".

Source: MSExchange CmdletLogs

ID: 6

Cmdlet failed. Cmdlet Configure-WSManIISHosting, parameters -EnableKerberosModule "True".

Source: MSExchange CmdletLogs

ID: 6

Cmdlet failed. Cmdlet Install-BridgeheadRole, parameters -DomainController "IDC06.main.msa.com" -UpdatesDir $null -CustomerFeedbackEnabled "True" -LanguagePacksPath "E:\" -StartTransportService "True" -DisableAMFiltering "False".

Source: MSExchangeSetup

ID: 1002

Exchange Server component Mailbox role: Transport service failed. 

Error: Error:

The following error was generated when "$error.Clear(); 

```
configure-WSManIISHosting -EnableKerberosModule;

			" was run: "System.InvalidOperationException: Running the command 'C:\Windows\system32\net.exe start winrm' failed.
```

Output message: The service is starting or stopping.  Please try again later.

Error message:  

Process exit code: 2.

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)

   at Microsoft.Exchange.Management.Deployment.ConfigureWSManIISHostingBase.ExecuteCmd(String appPath, String arguments, String executionPath, Boolean writeError, Boolean needToRestoreIIS)

   at Microsoft.Exchange.Management.Deployment.ConfigureWSManIISHostingBase.RestartWSManService()

   at Microsoft.Exchange.Management.Deployment.ConfigureWSManIISHostingBase.RebuildWSManRegistry()

   at Microsoft.Exchange.Management.Deployment.ConfigureWSManIISHosting.CheckRequiredRegistryKeys()

   at Microsoft.Exchange.Management.Deployment.ConfigureWSManIISHosting.InternalProcessRecord()

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

I ask for help in solving the problem

## Answers

_No answers on this thread._
