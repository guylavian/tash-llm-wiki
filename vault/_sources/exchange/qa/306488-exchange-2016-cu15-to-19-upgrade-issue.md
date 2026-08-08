---
title: "Exchange 2016 cu15 to 19 upgrade issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/306488/exchange-2016-cu15-to-19-upgrade-issue
question_id: 306488
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 cu15 to 19 upgrade issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/306488/exchange-2016-cu15-to-19-upgrade-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Attempting to upgrade exchange 2016 cu15 to cu19 and I am getting an error that I can't find an answer to.

[03/09/2021 16:50:30.0545] [1] Processing component 'Admin Tools Configuration' (Configuring the server.).  

[03/09/2021 16:50:30.0546] [1] Executing:  

if (Test-Path ($Env:SystemRoot + "\system32\mmc.exe")) {Copy-Item -Path ($RoleInstallPath+"Bin\mmc.exe.config") -Destination (Split-Path (where.exe mmc)) -Force}

[03/09/2021 16:50:30.0681] [1] The following 1 error(s) occurred during task execution:  

[03/09/2021 16:50:30.0681] [1] 0. ErrorRecord: The term 'where.exe' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

[03/09/2021 16:50:30.0682] [1] 0. ErrorRecord: System.Management.Automation.CommandNotFoundException: The term 'where.exe' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

at System.Management.Automation.CommandDiscovery.LookupCommandInfo(String commandName, CommandTypes commandTypes, SearchResolutionOptions searchResolutionOptions, CommandOrigin commandOrigin, ExecutionContext context)  

at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String commandName, CommandOrigin commandOrigin, Nullable`1 useLocalScope)    at System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)    at System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[] commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)    at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)    at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

[03/09/2021 16:50:30.0687] [1] [ERROR] The following error was generated when "$error.Clear();  

if (Test-Path ($Env:SystemRoot + "\system32\mmc.exe")) {Copy-Item -Path ($RoleInstallPath+"Bin\mmc.exe.config") -Destination (Split-Path (where.exe mmc)) -Force}  

" was run: "System.Management.Automation.CommandNotFoundException: The term 'where.exe' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

at System.Management.Automation.CommandDiscovery.LookupCommandInfo(String commandName, CommandTypes commandTypes, SearchResolutionOptions searchResolutionOptions, CommandOrigin commandOrigin, ExecutionContext context)  

at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String commandName, CommandOrigin commandOrigin, Nullable`1 useLocalScope)    at System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)    at System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[] commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)    at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)    at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".  

[03/09/2021 16:50:30.0687] [1] [ERROR] The term 'where.exe' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.  

[03/09/2021 16:50:30.0692] [1] [ERROR-REFERENCE] Id=AdminToolsComponent___99aa0a89-1e09-4dd5-8f17-998a1cbe2154 Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[03/09/2021 16:50:30.0692] [1] Setup is stopping now because of one or more critical errors.  

[03/09/2021 16:50:30.0692] [1] Finished executing component tasks.  

[03/09/2021 16:50:30.0712] [1] Ending processing Install-AdminToolsRole  

[03/09/2021 16:50:30.0715] [0] CurrentResult console.ProcessRunInternal:198: 1  

[03/09/2021 16:50:30.0720] [0] CurrentResult launcherbase.maincore:90: 1  

[03/09/2021 16:50:30.0720] [0] CurrentResult console.startmain:52: 1  

[03/09/2021 16:50:30.0720] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1  

[03/09/2021 16:50:30.0720] [0] The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

[03/09/2021 16:50:30.0721] [0] CurrentResult main.run:235: 1  

[03/09/2021 16:50:30.0722] [0] CurrentResult setupbase.maincore:396: 1  

[03/09/2021 16:50:30.0722] [0] End of Setup  

[03/09/2021 16:50:30.0722] [0] **********************************************

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi @Paul Copsey   ,    

-  Please check whether the "where.exe" and “mmc.exe” file exists in the following path:    

c：\ windows \ system32    

c：\ windows \ syswow64    

-  I noticed an error occurred in the installer at the specific "Exchange Management Tools". According to my research, I found a similar case. An error also occurred in where.exe. Another user using poweruser tool to run cmd as TrustedInstaller, temporarily renamed c:\windows\syswow64\mmc.exe to mmc.unused. Then try to upgrade again.     

The similar case: Exchange 2016 cu11 to cu19 update fails    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

I have attempted to run this using local admin and domain admin.  

Ran this on powershell and through gui  

I attempted the above command for the installation and go the same error   

It always fails at same place:  

Microsoft Exchange Server 2016 Cumulative Update 19 Unattended Setup  

Languages  

Management tools  

Mailbox role: Transport service  

Mailbox role: Client Access service  

Mailbox role: Unified Messaging service  

Mailbox role: Mailbox service  

Mailbox role: Front End Transport service  

Mailbox role: Client Access Front End service  

Performing Microsoft Exchange Server Prerequisite Check  

```
Configuring Prerequisites                                                                        COMPLETED
Prerequisite Analysis                                                                            COMPLETED
```

Configuring Microsoft Exchange Server  

```
Language Files                                                                                   COMPLETED
Restoring Services                                                                               COMPLETED
Language Configuration                                                                           COMPLETED
Exchange Management Tools                                                                        FAILED
```

The following error was generated when "$error.Clear();  

 if (Test-Path ($Env:SystemRoot + "\system32\mmc.exe"))  

{Copy-Item -Path ($RoleInstallPath+"Bin\mmc.exe.config") -Destination (Split-Path (where.exe mmc)) -Force}  

 " was run:  

"System.Management.Automation.CommandNotFoundException: The term 'where.exe' is not recognized as the name of a  

cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify  

that the path is correct and try again.  

 at System.Management.Automation.CommandDiscovery.LookupCommandInfo(String  

commandName, CommandTypes commandTypes, SearchResolutionOptions searchResolutionOptions, CommandOrigin commandOrigin,  

ExecutionContext context)  

 at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String  

commandName, CommandOrigin commandOrigin, Nullable`1 useLocalScope)    at   System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)    at   System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[]   commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)    at   System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput,   CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][]   commandRedirections, FunctionContext funcContext)    at   System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)  

 at  

System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

 at  

System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

 at  

System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".  

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the  

<SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Hi @Paul Copsey   ,    

How did you upgrade the Exchange server?  Use the unattended mode or the Exchange setup wizard?    

ErrorRecord: The term 'where.exe' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.    

Accoridng to the error information, the term “where.exe” is not recognized. Please make sure that you run the correct command to upgrade the Exchange server.    

```
:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Upgrade [/DomainController:] [/EnableErrorReporting]
```

For more information you could refer to: Install an Exchange CU using unattended Setup from the command line    

In addition, please note the following points:    

-  The account is a required member of the Exchange Organization Management role group.    

-  Before upgrading the Exchange server, please prepare AD and domian.    

For more information: Prepare Active Directory and domains for Exchange Server    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
