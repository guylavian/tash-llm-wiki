---
title: "[Migrated from MSDN Exchange Dev] Exchange 2016 CU 18 installation: abort of the CU-18 installation (step 3 of 11 Admintools)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176351/migrated-from-msdn-exchange-dev-exchange-2016-cu-1
question_id: 176351
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2016 CU 18 installation: abort of the CU-18 installation (step 3 of 11 Admintools)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176351/migrated-from-msdn-exchange-dev-exchange-2016-cu-1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Exchange 2016 CU 18 installation: abort of the CU-18 installation (step 3 of 11 Admintools)  

[Original post]  

Hello :-),  

i have a problem with a "Exchange 2016 CU 18 installation".  

abort of the CU-18 installation (step 3 of 11 Admintools):  

Error:  

Der folgende Fehler wurde generiert, als „$error.Clear();  

if (Test-Path ($Env:SystemRoot + „\system32\mmc.exe“)) {Copy-Item -Path ($RoleInstallPath+“Bin\mmc.exe.config“) -Destination (Split-Path (where.exe mmc)) -Force}  

„ ausgeführt wurde: „System.Management.Automation.CommandNotFoundException: Die Benennung „where.exe“ wurde nicht als Name eines Cmdlet, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die Schreibweise des Namens, oder ob der Pfad korrekt ist (sofern enthalten), und wiederholen Sie den Vorgang.  

bei System.Management.Automation.CommandDiscovery.LookupCommandInfo(String commandName, CommandTypes commandTypes, SearchResolutionOptions searchResolutionOptions, CommandOrigin commandOrigin, ExecutionContext context)  

bei System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String commandName, CommandOrigin commandOrigin, Nullable‚1 useLocalScope)  

bei System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)  

bei System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[] commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)  

bei System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)  

bei System.Management.Automation.Interpreter.ActionCallInstruction‚6.Run(InterpretedFrame frame)  

bei System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

bei System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)  

bei System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)“.  

Does somebody now this problem?  

Thank you for help :-)  

Stefan SH

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-26*

Hi Stefan,    

As per the error you shared above, please try renaming the mmc.exe.config file which is located at the path below:    

C:\Windows\System32    

    

For example, you can rename it to "mmc.exe.config.old".    

Then re-run the setup.exe to check the result.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
