---
title: "Exchange Hybrid SEtup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/342112/exchange-hybrid-setup
question_id: 342112
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange Hybrid SEtup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/342112/exchange-hybrid-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 Exchane 2013 servers running on CU1 currently in my environment and Having issues upgrading it to Latest CU Getting below error so i wanted to know can i install a fresh server just for the hybrid configuration leaving my existing setup as it is, Will i be able to configure Hybrid. Please suggest

The following error was generated when "$error.Clear();  

$dependentAssemblyGeneratorExePath = [System.IO.Path]::Combine($RoleInstallPath, "bin", "DependentAssemblyGenerator.exe");  

$exchangeBinPath = [System.IO.Path]::Combine($RoleInstallPath, "bin");  

$frontEndPath = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd");  

$clientAccessPath = [System.IO.Path]::Combine($RoleInstallPath, "ClientAccess");  

$sharedWebConfig = [System.IO.Path]::Combine($RoleInstallPath, "FrontEnd", "HttpProxy", "SharedWebConfig.config");

```
$a = &"$dependentAssemblyGeneratorExePath" -exchangePath "$exchangeBinPath" -exchangePath "$frontEndPath" -exchangePath "$clientAccessPath" -configFile "$sharedWebConfig";
      $a | % { if ($_.Length > 0) { Write-ExchangeSetupLog -Info "$_.ToString()" } }
      Start-SetupProcess -Name "iisreset" -Args "/timeout:120"
    " was run: "Microsoft.Exchange.Configuration.Tasks.TaskException: Process execution failed with exit code 1062.
```

at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

at Microsoft.Exchange.Management.Tasks.RunProcessBase.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__b()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

@Sunil Kumar      

If you want to update Exchange 2013 to the lasted CU(CU 23), you need to install .NET Framework 4.7.2 or 4.8 first. Then try to update Exchange to the lasted CU. If you still cannot update Exchange successfully. I would suggest you have a check in Event Viewer, whether there exist error about installing. Here is a related issue which due to the lack of MSMQ.    

Yes, you can also create a new Exchange server coexist with the old Exchange server, then deploy hybrid with this new Exchange server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
