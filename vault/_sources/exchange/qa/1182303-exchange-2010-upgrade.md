---
title: "Exchange 2010 Upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182303/exchange-2010-upgrade
question_id: 1182303
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 Upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182303/exchange-2010-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am seeking help for a best possible scenario for our Exchange hybrid setup. The current setup is, all mailboxes on exchange online with three Exchange 2010 servers running on windows 2008 R2 on-premise servers (DAG). AD is also running on Windows 2008. As both Windows 2008 and 2008 R2 are discontinued, I would like to upgrade them to Windows 2019.

As far as I know, if I go ahead with introducing a new Windows 2019 server to the domain, Exchange 2010 will have compatibility issues and may stop working.

Complete decommissioning of Exchange 2010 and moving the AD to Azure is also not possible as we have many applications like MS Navision still authentication to on-premise AD.

In this case I would like to know which is the best possible method to upgrade the entire on-premise setup to Windows 2019.

Thanks!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-02-20*

I would migrate from 2010 to 2016, then from 2016, migrate to 2019 to be supported:

https://learn.microsoft.com/en-us/answers/questions/80238/migration-from-exchange-2010-to-2019

https://community.spiceworks.com/topic/2301536-upgrading-exchange-2010-to-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-16*

Hi,

Thank you for the replies.

Finally I am starting this migration process.

Facing an error while running the exchange server 2016 CU 23 on a Windows 2016 Server. I have already successfully completed the below steps :

-  Install-WindowsFeature RSAT-Clustering-CmdInterface, NET-Framework-45-Features, RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-Clustering-PowerShell, Web-Mgmt-Console, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS

-  Installed Microsoft Unified Communications Managed API (UCMA)

-  Installed Microsoft .NET Framework 4.8

4.Setup.exe /PrepareAD /TenantOrganizationConfig MyTenantOrganizationConfig.xml /IAcceptExchangeServerLicenseTerms

5.setup.exe /PrepareDomain

After all these steps while running setup, below error is triggered during readiness check:

Executionpolicy for LocalMachine is set as RemoteSigned

```
Error:

The following error was generated when "$error.Clear(); 

          if($RoleInstallWindowsComponents)

          {          

            # Install any Windows Roles or Features required for the Management Tools role

            & $RoleBinPath\InstallWindowsComponent.ps1 -ShortNameForRole "AdminTools" -ADToolsNeeded $RoleADToolsNeeded

          }

        " was run: "System.Management.Automation.PSSecurityException: File C:\Windows\Temp\ExchangeSetup\InstallWindowsComponent.ps1 cannot be loaded because you opted not to run this software now. ---> System.UnauthorizedAccessException: File C:\Windows\Temp\ExchangeSetup\InstallWindowsComponent.ps1 cannot be loaded because you opted not to run this software now.

   --- End of inner exception stack trace ---

   at System.Management.Automation.AuthorizationManager.ShouldRunInternal(CommandInfo commandInfo, CommandOrigin origin, PSHost host)

   at System.Management.Automation.CommandDiscovery.ShouldRun(ExecutionContext context, PSHost host, CommandInfo commandInfo, CommandOrigin commandOrigin)

   at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(CommandInfo commandInfo, CommandOrigin commandOrigin, Nullable`1 useLocalScope, SessionStateInternal sessionState)

   at System.Management.Automation.CommandDiscovery.LookupCommandProcessor(String commandName, CommandOrigin commandOrigin, Nullable`1 useLocalScope)

   at System.Management.Automation.ExecutionContext.CreateCommand(String command, Boolean dotSource)

   at System.Management.Automation.PipelineOps.AddCommand(PipelineProcessor pipe, CommandParameterInternal[] commandElements, CommandBaseAst commandBaseAst, CommandRedirection[] redirections, ExecutionContext context)

   at System.Management.Automation.PipelineOps.InvokePipeline(Object input, Boolean ignoreInput, CommandParameterInternal[][] pipeElements, CommandBaseAst[] pipeElementAsts, CommandRedirection[][] commandRedirections, FunctionContext funcContext)

   at System.Management.Automation.Interpreter.ActionCallInstruction`6.Run(InterpretedFrame frame)

   at System.Management.Automation.Interpreter.EnterTryCatchFinallyInstruction.Run(InterpretedFrame frame)".
```

Thanks
Thomas

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-21*

Hi @Thomas P Simon  ,

As far as I know, if I go ahead with introducing a new Windows 2019 server to the domain, Exchange 2010 will have compatibility issues and may stop working.

True. According to Exchange Server supportability matrix - Supported Active Directory environments, running Exchange 2010 in an AD environment of Windows server 2019 is Not supported. 

Windows Server 2019 Active Directory servers require Exchange 2016 CU12 or later, and currently, only Exchange 2019 can run on Windows server 2019:  

So, take all these factors into consideration, agree with Andy that it's suggested to first migrate to Exchange Server 2016 hybrid, decommission the Exchange Server 2010, and then migrate from Exchange 2016 to Exchange 2019, run the Hybrid Configuration Wizard in 2019 and then remove 2016.

You can use the Microsoft Deployment Assistant tool https://assistants.microsoft.com/ when upgrading the Exchange server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
