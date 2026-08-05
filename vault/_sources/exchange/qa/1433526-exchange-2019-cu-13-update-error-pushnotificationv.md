---
title: "Exchange 2019 CU 13 Update-Error: $PushNotificationVDConfig.RequireSSL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1433526/exchange-2019-cu-13-update-error-pushnotificationv
question_id: 1433526
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU 13 Update-Error: $PushNotificationVDConfig.RequireSSL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1433526/exchange-2019-cu-13-update-error-pushnotificationv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

System:

Windows Server 2019

Exchange 2019 CU12 installed -> Update to CU13

During the update we get the following error:

```
Error:
The following error was generated when "$error.Clear(); 
        ($PushNotificationVDConfig = Get-PushNotificationsVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController) | Remove-PushNotificationsVirtualDirectory -DomainController $RoleDomainController;
        New-PushNotificationsVirtualDirectory -Role Mailbox -OAuthAuthentication:$RoleIsDatacenter -DomainController $RoleDomainController -RequireSSL $PushNotificationVDConfig.RequireSSL -ExtendedProtectionFlags $PushNotificationVDConfig.ExtendedProtectionFlags -ExtendedProtectionSPNList $PushNotificationVDConfig.ExtendedProtectionSPNList -ExtendedProtectionTokenChecking $PushNotificationVDConfig.ExtendedProtectionTokenChecking;
      " was run: "System.Management.Automation.ParameterBindingException: Cannot bind argument to parameter 'RequireSSL' because it is null.
   at System.Management.Automation.ParameterBinderBase.HandleNullParameterForSpecialTypes(CommandParameterInternal argument, String parameterName, Type toType, Object currentValue)
   at System.Management.Automation.ParameterBinderBase.CoerceTypeAsNeeded(CommandParameterInternal argument, String parameterName, Type toType, ParameterCollectionTypeInformation collectionTypeInfo, Object currentValue)
   at System.Management.Automation.ParameterBinderBase.BindParameter(CommandParameterInternal parameter, CompiledCommandParameter parameterMetadata, ParameterBindingFlags flags)
   at System.Management.Automation.CmdletParameterBinderController.BindParameter(CommandParameterInternal argument, MergedCompiledCommandParameter parameter, ParameterBindingFlags flags)
   at System.Management.Automation.CmdletParameterBinderController.BindParameter(UInt32 parameterSets, CommandParameterInternal argument, MergedCompiledCommandParameter parameter, ParameterBindingFlags flags)
   at System.Management.Automation.CmdletParameterBinderController.BindParameters(UInt32 parameterSets, Collection`1 arguments)
   at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParametersNoValidation(Collection`1 arguments)
   at System.Management.Automation.CmdletParameterBinderController.BindCommandLineParameters(Collection`1 arguments)
   at System.Management.Automation.CommandProcessor.BindCommandLineParameters()
   at System.Management.Automation.CommandProcessor.Prepare(IDictionary psDefaultParameterValues)
   at System.Management.Automation.CommandProcessorBase.DoPrepare(IDictionary psDefaultParameterValues)
   at System.Management.Automation.Internal.PipelineProcessor.Start(Boolean incomingStream)
   at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)
--- End of stack trace from previous location where exception was thrown ---
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Management.Automation.Internal.PipelineProcessor.SynchronousExecuteEnumerate(Object input)
   at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)
   at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".
```

The update fails and I retried this with the same result.

I already tried to change the value of IIS -> Sites -> Exchange Back End -> PushNotifications -> SSL Settings

as well as SSL Settings for the "bin" path within Exchange Back End -> PushNotifications.

I tried to deactivate it, Activate Ignore and Activate Accept.

Result does not change, every time the update process quits with this error.

I tried to download the ISO again, same result.

Tampering with the corresponding DLL is not an option because the installer will not load the DLLs (understandably)

It feels like the entire VirtualDirectory is missing or was missing to begin with since it is being removed at the beginning of the command and is supposed to be recreated ?

```
$PushNotificationVDConfig = Get-PushNotificationsVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController) | Remove-PushNotificationsVirtualDirectory -DomainController $RoleDomainController;
```

I am currently struggeling to find ideas

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-22*

Hi @Markus Rohrbach  ,

Welcome to our Q&A forum!

Based on your description, it seems like the update process is failing due to an error related to the Push Notifications Virtual Directory.

To troubleshoot our issue, I recommend running an Exchange server Health Check to find out if there are any configuration issues with your Win server 2019. You can refer to: https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/

Please feel free to let us know if any updates.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
