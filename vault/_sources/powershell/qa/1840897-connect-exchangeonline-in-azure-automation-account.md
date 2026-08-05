---
title: "Connect-ExchangeOnline in Azure Automation account gives Unable to find type (EXO 3.5.1 PS7.2)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1840897/connect-exchangeonline-in-azure-automation-account
question_id: 1840897
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 4
qa_tags: ["azure-automation", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Connect-ExchangeOnline in Azure Automation account gives Unable to find type (EXO 3.5.1 PS7.2)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1840897/connect-exchangeonline-in-azure-automation-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have setup an Azure Automation account and loaded the EXO 3.5.1 module along with PackageManagement V1.4.8.1 and PowerShellGet v2.2.5. I open a new PowerShell runbook and just posted a Connect-ExchangeOnline -ManagedIdentity - Organisation "xyz.onmicrosoft.com" command. Saved and tested and got an error

```
System.Management.Automation.RuntimeException: Unable to find type [Microsoft.Exchange.Management.RestApiClient.ExchangeEnvironment].
   at System.Management.Automation.TypeOps.ResolveTypeName(ITypeName typeName, IScriptExtent errorPos)
   at System.Management.Automation.Language.Compiler.GetAttribute(TypeConstraintAst typeConstraintAst)
   at System.Management.Automation.Language.TypeConstraintAst.GetAttribute()
   at System.Management.Automation.Language.Compiler.GetRuntimeDefinedParameter(ParameterAst parameterAst, Boolean& customParameterSet, Boolean& usesCmdletBinding)
   at System.Management.Automation.Language.Compiler.GetParameterMetaData(ReadOnlyCollection`1 parameters, Boolean automaticPositions, Boolean& usesCmdletBinding)
   at System.Management.Automation.Language.FunctionDefinitionAst.System.Management.Automation.Language.IParameterMetadataProvider.GetParameterMetadata(Boolean automaticPositions, Boolean& usesCmdletBinding)
   at System.Management.Automation.CompiledScriptBlockData.InitializeMetadata()
   at System.Management.Automation.CompiledScriptBlockData.Compile(Boolean optimized)
   at System.Management.Automation.ScriptBlock.Compile(Boolean optimized)
   at System.Management.Automation.PSScriptCmdlet..ctor(ScriptBlock scriptBlock, Boolean useNewScope, Boolean fromScriptFile, ExecutionContext context)
   at System.Management.Automation.CommandProcessor.Init(IScriptCommandInfo scriptCommandInfo)
   at System.Management.Automation.CommandProcessor..ctor(IScriptCommandInfo scriptCommandInfo, ExecutionContext context, Boolean useLocalScope, Boolean fromScriptFile, SessionStateInternal sessionState)
   at System.Management.Automation.CommandDiscovery.GetScriptAsCmdletProcessor(IScriptCommandInfo scriptCommandInfo, ExecutionContext context, Boolean useNewScope, Boolean fromScriptFile, SessionStateInternal sessionState)
   at System.Management.Automation.CommandDiscovery.CreateCommandProcessorForScript(FunctionInfo functionInfo, ExecutionContext context, Boolean useNewScope, SessionStateInternal sessionState)
   at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(CommandInfo commandInfo, CommandOrigin commandOrigin, Nullable`1 useLocalScope, SessionStateInternal sessionState)
   at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String commandName, CommandOrigin commandOrigin, Nullable`1 useLocalScope)
   at System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)
   at System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[] commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)
   at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)
   at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)
   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)
```

The Automation account managed identity was given the necessary permissions to connect to the Exchange Online PowerShell and the Exchange Administrator role following https://learn.microsoft.com/en-au/powershell/exchange/connect-exo-powershell-managed-identity?view=exchange-ps&WT.mc_id=M365-MVP-9501

Have repeated the exercise with a brand new RG, AA and RB with same result

I notice that other users have been reporting the same issue in the last few days on Reddit

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 2 · updated: 2024-08-07*

Hello All,

After the ExchangeOnlineManagement PowerShell module was released, we noticed that the latest version, 3.5.1, was released on July 11, 2024. Since then, the Azure Function app PowerShell has been failing with the following error. However, when we reverted back to version 3.5.0, it started working fine.

ERROR: Unable to find type [Microsoft.Exchange.Management.RestApiClient.ExchangeEnvironment]. 

https://www.powershellgallery.com/packages/ExchangeOnlineManagement/3.5.1

Could you please help us determine if there is a problem with this specific latest version?

## Answer (community) — community member

*upvotes: 1 · updated: 2024-07-31*

I ended up downgrading the PowerShell version of the EXO 3.5.1 module and the Azure Runbook to PS v5.1 and that fixed the issue for me.

It is a shame when PS 7.2 is the recommend version and upgraded modules like EXO aren't simply tested against it. In my case it was the most basic Connect-ExchangeOnline command with a managed identity (something that is becoming more common now) that failed. Someone might need to look at the testing framework

## Answer (community) — community member

*upvotes: 1 · updated: 2024-07-31*

Hi!

Same problem here with an Azure Function. 

My function worked successfully until july 16th. I've downgraded ExchangeOnlineManagement module version to 3.5.0 and it works again for me.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-07-29*

Hi,

Same issue with Azure Functions.

If you downgrade the version of the ExchangeOnline Powershell module (3.4 or 3.5), it will work again ;)
