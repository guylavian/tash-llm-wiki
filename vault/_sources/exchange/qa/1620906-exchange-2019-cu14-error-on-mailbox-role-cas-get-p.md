---
title: "Exchange 2019 CU14 - Error on Mailbox Role - CAS - Get-PushNotificationsVirtualDirectory - Cannot bind argument to parameter 'RequireSSL' because it is null."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1620906/exchange-2019-cu14-error-on-mailbox-role-cas-get-p
question_id: 1620906
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019 CU14 - Error on Mailbox Role - CAS - Get-PushNotificationsVirtualDirectory - Cannot bind argument to parameter 'RequireSSL' because it is null.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1620906/exchange-2019-cu14-error-on-mailbox-role-cas-get-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Attempted to install CU14 for Exchange 2019; small environment, single server. The update errors out at the same place. Digging through the logs doesn't provide much insight that I've been able to use. The Exchange Services are now unusable. 

Exchange Powershell does not function with a generic error of [ 'The WinRM client cannot process the request. It cannot determine the content type of the HTTP response from the destination computer. The content type is absent or invalid.' ] so I cannot run the Exchange Health Checker script. 

I'm not seeing anything else out there on this specific error. During one of the iterations, I found that several files from the update were not copied correctly to the install directory (using a different drive letter for Exchange's root).

I have verified protected mode on all relevant IIS directories along with SSL requirements and the right certs for the correct directories assigned correctly.

Attempted to uninstall Exchange puts it in a loop; can't uninstall as it detects an upgrade was in-progress but it never completes the upgrade... error below happens each time. I haven't gotten any further so not sure if other errors may exist past this dialog. :/

Any thoughts on this specific issue would be much appreciated.  Thanks in advance Everyone.

Error:

The following error was generated when "$error.Clear(); 

```
($PushNotificationVDConfig = Get-PushNotificationsVirtualDirectory -ShowMailboxVirtualDirectories -server $RoleFqdnOrName -DomainController $RoleDomainController) | Remove-PushNotificationsVirtualDirectory -DomainController $RoleDomainController;

	

	if ($RoleDoNotEnableEP)

	{

      New-PushNotificationsVirtualDirectory -Role Mailbox -OAuthAuthentication:$RoleIsDatacenter -DomainController $RoleDomainController -RequireSSL $PushNotificationVDConfig.RequireSSL -ExtendedProtectionFlags $PushNotificationVDConfig.ExtendedProtectionFlags -ExtendedProtectionSPNList $PushNotificationVDConfig.ExtendedProtectionSPNList -ExtendedProtectionTokenChecking $PushNotificationVDConfig.ExtendedProtectionTokenChecking;

	}

	else

	{

	  New-PushNotificationsVirtualDirectory -Role Mailbox -OAuthAuthentication:$RoleIsDatacenter -DomainController $RoleDomainController -RequireSSL $PushNotificationVDConfig.RequireSSL -ExtendedProtectionFlags $PushNotificationVDConfig.ExtendedProtectionFlags -ExtendedProtectionSPNList $PushNotificationVDConfig.ExtendedProtectionSPNList -ExtendedProtectionTokenChecking $RoleEPTokenCheckingRequireOrNone;

	}     

  " was run: "System.Management.Automation.ParameterBindingException: Cannot bind argument to parameter 'RequireSSL' because it is null.
```

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

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-18*

Hi @J,

I would suggest following this link to see if it can help you with the Exchange Management Shell issue:

Error (The WinRM client... cannot determine the content type of the HTTP response from the destination computer) when you try to start Exchange Management Shell/Console

If you can access Exchange Management Shell successfully, please run healthchecker.ps1 and see if it will return possible causes.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
