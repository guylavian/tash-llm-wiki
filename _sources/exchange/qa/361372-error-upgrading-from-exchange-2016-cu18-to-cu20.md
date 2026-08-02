---
title: "Error upgrading from Exchange 2016 CU18 to CU20"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361372/error-upgrading-from-exchange-2016-cu18-to-cu20
question_id: 361372
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Error upgrading from Exchange 2016 CU18 to CU20

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361372/error-upgrading-from-exchange-2016-cu18-to-cu20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. I'm getting this error on step 13 of 15 when i upgrade Exchange CU18 tot CU20:

[04-17-2021 11:23:39.0874] [2] Configuratiewijzigingen in sectie "system.webServer/modules" zijn toegepast voor "MACHINE/WEBROOT/APPHOST" op configuratieopslagpad "MACHINE/WEBROOT/APPHOST"  

[04-17-2021 11:23:39.0874] [2] Ending processing Write-ExchangeSetupLog  

[04-17-2021 11:23:39.0875] [1] The following 1 error(s) occurred during task execution:  

[04-17-2021 11:23:39.0876] [1] 0. ErrorRecord: Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Message'. Specified method is not supported.  

[04-17-2021 11:23:39.0876] [1] 0. ErrorRecord: System.Management.Automation.ParameterBindingException: Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Message'. Specified method is not supported. ---> System.NotSupportedException: Specified method is not supported.  

at System.Management.Automation.ParameterBinderBase.CoerceTypeAsNeeded(CommandParameterInternal argument, String parameterName, Type toType, ParameterCollectionTypeInformation collectionTypeInfo, Object currentValue)  

--- End of inner exception stack trace ---  

at System.Management.Automation.CmdletParameterBinderController.VerifyArgumentsProcessed(ParameterBindingException originalBindingException)  

at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParametersNoValidation(Collection`1 arguments)    at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParameters(Collection`1 arguments)  

at System.Management.Automation.CommandProcessor.BindCommandLineParameters()  

at System.Management.Automation.CommandProcessorBase.DoPrepare(IDictionary psDefaultParameterValues)  

at System.Management.Automation.Internal.PipelineProcessor.Start(Boolean incomingStream)  

at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  

at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)  

at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

[04-17-2021 11:23:40.0359] [1] [ERROR] The following error was generated when "$error.Clear();  

# Array of module names to unlock  

[System.Array] $moduleNames = "AnonymousAuthenticationModule",  

"AnonymousIdentification",  

"BasicAuthenticationModule",  

"CertificateMappingAuthenticationModule",  

"CgiModule",  

"ConfigurationValidationModule",  

"CustomErrorModule",  

"DefaultAuthentication",  

"DefaultDocumentModule",  

"DigestAuthenticationModule",  

"DirectoryListingModule",  

"DynamicCompressionModule",  

"FailedRequestsTracingModule",  

"FastCgiModule",  

"FileAuthorization",  

"FormsAuthentication",  

"HttpCacheModule",  

"HttpLoggingModule",  

"HttpRedirectionModule",  

"IsapiFilterModule",  

"IsapiModule",  

"OutputCache",  

"Profile",  

"ProtocolSupportModule",  

"RequestFilteringModule",  

"RoleManager",  

"ScriptModule-4.0",  

"ServerSideIncludeModule",  

"ServiceModel",  

"ServiceModel-4.0",  

"Session",  

"StaticCompressionModule",  

"StaticFileModule",  

"UrlAuthorization",  

"UrlMappingsModule",  

"UrlRoutingModule-4.0",  

"WindowsAuthentication",  

"WindowsAuthenticationModule";  

$windir = $env:windir;

```
$a = &"$windir\system32\inetsrv\appcmd.exe" "set" "config" "/section:system.webServer/modules" "/lockItem:false"
      Write-ExchangeSetupLog -Info ($a)

      foreach($moduleName in $moduleNames)
      {
          $a = &"$windir\system32\inetsrv\appcmd.exe" "set" "config" "/section:system.webServer/modules" "/.[name=`'$moduleName`'].lockItem:false"
          Write-ExchangeSetupLog -Info ($a)
      }
    " was run: "System.Management.Automation.ParameterBindingException: Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Message'. Specified method is not supported. ---> System.NotSupportedException: Specified method is not supported.
```

at System.Management.Automation.ParameterBinderBase.CoerceTypeAsNeeded(CommandParameterInternal argument, String parameterName, Type toType, ParameterCollectionTypeInformation collectionTypeInfo, Object currentValue)  

--- End of inner exception stack trace ---  

at System.Management.Automation.CmdletParameterBinderController.VerifyArgumentsProcessed(ParameterBindingException originalBindingException)  

at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParametersNoValidation(Collection`1 arguments)    at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParameters(Collection`1 arguments)  

at System.Management.Automation.CommandProcessor.BindCommandLineParameters()  

at System.Management.Automation.CommandProcessorBase.DoPrepare(IDictionary psDefaultParameterValues)  

at System.Management.Automation.Internal.PipelineProcessor.Start(Boolean incomingStream)  

at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  

--- End of stack trace from previous location where exception was thrown ---  

at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  

at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)  

at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)  

at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".  

[04-17-2021 11:23:40.0360] [1] [ERROR] Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Message'. Specified method is not supported.  

[04-17-2021 11:23:40.0360] [1] [ERROR] Specified method is not supported.  

[04-17-2021 11:23:40.0382] [1] [ERROR-REFERENCE] Id=CafeComponent___UnlockModulesInAppHost Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[04-17-2021 11:23:40.0471] [1] Setup is stopping now because of one or more critical errors.  

[04-17-2021 11:23:40.0471] [1] Finished executing component tasks.  

[04-17-2021 11:23:42.0551] [1] Ending processing Install-CafeRole  

[04-17-2021 11:30:11.0679] [0] CurrentResult setupbase.maincore:396: 0  

[04-17-2021 11:30:11.0972] [0] End of Setup  

[04-17-2021 11:30:11.0972] [0] **********************************************

I'm using a Windows 2016 Server standard. Until now, i never have this problem updating a CU for Exchange.  

What can be the problem? Need help so i can install the new security patch. Please help!  

Thank you for your time.

ps. For now i recovered a failover point.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-01*

Yes! I finished it today. I have a Hyper-V replica server. On a failover test, i could install the update without any problems.  

At the end, i replaced the hard disks (6x 2tb raid10) with new disks.  No i have installed it today, and it's all fine.  

Thank you for your support!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-20*

i will try this weekend, both answers. I will let you know. Probarly i still need some help. Thank you for your time so far!
