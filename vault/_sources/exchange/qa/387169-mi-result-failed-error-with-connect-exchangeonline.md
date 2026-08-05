---
title: "MI_RESULT_FAILED Error with Connect-ExchangeOnline running in app only mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387169/mi-result-failed-error-with-connect-exchangeonline
question_id: 387169
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 3
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# MI_RESULT_FAILED Error with Connect-ExchangeOnline running in app only mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387169/mi-result-failed-error-with-connect-exchangeonline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to get to the root cause of the MI_RESULT_FAILED error I'm seeing?

Environment:
Running in a Docker container: mcr.microsoft.com/azure-powershell:5.9.0-ubuntu-18.04

> $PSVersionTable
> 
> Name                           Value
> ----                           -----
> PSVersion                      7.1.3
> PSEdition                      Core
> GitCommitId                    7.1.3
> OS                             Linux 5.10.25-linuxkit #1 SMP Tue Mar 23 09:27:39 UTC 2021
> Platform                       Unix
> PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0…}
> PSRemotingProtocolVersion      2.3
> SerializationVersion           1.1.0.1
> WSManStackVersion              3.0

Error:

> Exception: /root/.local/share/powershell/Modules/ExchangeOnlineManagement/2.0.4/netCore/ExchangeOnlineManagement.psm1:475
> Line |
>  475 |  … PSSession = New-ExoPSSession -ExchangeEnvironmentName $ExchangeEnviro …
>      |                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>      | Connecting to remote server outlook.office365.com failed with the following error message :
>      | MI_RESULT_FAILED For more information, see the about_Remote_Troubleshooting Help topic.

Error Log:

> Version,Organization,ScriptName,ScriptExecutionGuid,CommandName,CommandParams,RecordCount,SentBytesCount,TotalLatencyMs,ErrorLog
> v2,,,,Connect-ExchangeOnline,CertificateFilePath;CertificatePassword;AppId;Organization;EnableErrorReporting;LogDirectoryPath;LogLevel,0,0,0,FullyQualifiedErrorId=1PSSessionOpenFailed;CategoryInfo=OpenError: (System.Management.A…tion.RemoteRunspace:RemoteRunspace) [New-PSSession] PSRemotingTransportException;ExceptionType=System.Management.Automation.Remoting.PSRemotingTransportException;ErrorCode=1;TransportMessage=MI_RESULT_FAILED;;ExceptionMessage=System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server outlook.office365.com failed with the following error message : MI_RESULT_FAILED For more information see the about_Remote_Troubleshooting Help topic.\n   at Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession.HandleError(PSDataCollection`1 errors)\n   at Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession.ExecutePsCommand(PSCommand command)\n   at Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession.ProcessNewConnection()\n   at Microsoft.Exchange.Management.ExoPowershellSnapin.NewExoPSSession.ProcessRecord()\n   at System.Management.Automation.Cmdlet.DoProcessRecord() in /PowerShell/src/System.Management.Automation/engine/cmdlet.cs:line 173\n   at System.Management.Automation.CommandProcessor.ProcessRecord() in /PowerShell/src/System.Management.Automation/engine/CommandProcessor.cs:line 388|

Using the same connection parameters with `Connect-PnPOnline` works fine.

## Answers

_No answers on this thread._
